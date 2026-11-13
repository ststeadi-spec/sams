#!/Users/samueltang/Documents/Jarvis/orb/venv/bin/python
"""Sams' second brain: FREE OpenRouter models next to Claude (Claude stays the main brain on
Samuel's subscription). Like Hermes Agent's model-picker + fallback chain, but only ':free' models.

  sams-llm ask [--kind general|fast|reasoning|code|long|vision|danish] [--image FILE] "prompt"
      -> picks the best free model for the kind, falls through a chain on errors/rate limits,
         prints the answer (and the model used on stderr)
  sams-llm models          -> the free models available right now, per kind
  sams-llm pick <kind>     -> which model would be used

Used by: the Telegram bridge (fallback when Claude is down/out of quota) and by Claude itself
(via Bash) when another model makes more sense: second opinion, huge documents (1M context),
cheap bulk summarising/translation, video/audio input.
"""
import base64, json, mimetypes, sys, time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sams_common import SAMS, secret, load_json, save_json, log  # noqa: E402

API = "https://openrouter.ai/api/v1"
CACHE = SAMS / "openrouter_models.json"
CACHE_TTL = 6 * 3600
BENCH = SAMS / "openrouter_bench.json"   # model -> unix time until which it's skipped (rate limited)

# Preference per kind: substrings matched against the live free-model list, best first.
# The live list changes often; anything matching is used, and 'openrouter/free' (OpenRouter's own
# free router) is always the last resort.
PREFS = {
    "general":   ["nemotron-3-ultra", "gemma-4-31b", "inkling-2", "nemotron-3.5-super", "ernie-5.5"],
    "fast":      ["nemotron-3.5-lightning", "gemma-4-26b", "lfm-3", "inkling-2-small"],
    "reasoning": ["nemotron-3-ultra", "reasoning", "nemotron-3.5-super", "inkling-2", "gemma-4-31b"],
    "code":      ["code", "nemotron-3-ultra", "inkling-2", "gemma-4-31b"],
    "long":      ["inkling-2", "nemotron-3-ultra", "nemotron-3.5", "ernie-5.5", "dots-3"],
    "vision":    ["nemotron-3.5-super-vl", "gemma-4-31b", "inkling-2", "dots-3", "omni"],
    "danish":    ["gemma-4-31b", "nemotron-3-ultra", "inkling-2", "ernie-5.5"],
}
SKIP = ("lyria",)   # music generators etc. that are listed as free but aren't chat models


def free_models(refresh=False):
    data = load_json(CACHE, {})
    if not refresh and data.get("t", 0) > time.time() - CACHE_TTL and data.get("models"):
        return data["models"]
    try:
        r = requests.get(f"{API}/models", timeout=20)
        allm = r.json()["data"]
    except Exception as e:
        log("openrouter models fetch failed", type(e).__name__)
        return data.get("models") or []
    out = []
    for m in allm:
        p = m.get("pricing") or {}
        free = m["id"].endswith(":free") or m["id"] == "openrouter/free" or (p.get("prompt") == "0" and p.get("completion") == "0")
        if not free or any(s in m["id"] for s in SKIP):
            continue
        out.append({"id": m["id"], "ctx": m.get("context_length") or 0,
                    "in": (m.get("architecture") or {}).get("input_modalities") or ["text"]})
    save_json(CACHE, {"t": time.time(), "models": out})
    return out


def chain(kind="general", need_ctx=0, need_image=False):
    """Ordered list of free model ids to try for this kind."""
    models = free_models()
    bench = load_json(BENCH, {})
    now = time.time()
    ok = [m for m in models if m["ctx"] >= need_ctx and (not need_image or "image" in m["in"])
          and bench.get(m["id"], 0) < now]
    order = []
    for pref in PREFS.get(kind, PREFS["general"]):
        for m in ok:
            if pref in m["id"] and m["id"] not in order and m["id"] != "openrouter/free":
                order.append(m["id"])
    if kind == "long":
        order += [m["id"] for m in sorted(ok, key=lambda m: -m["ctx"]) if m["id"] not in order and m["id"] != "openrouter/free"]
    order = order[:4]
    if any(m["id"] == "openrouter/free" for m in ok) or not order:
        order.append("openrouter/free")
    return order


def _bench(model, seconds):
    b = load_json(BENCH, {})
    b[model] = time.time() + seconds
    save_json(BENCH, b)


class NoModel(Exception):
    pass


def ask(prompt, kind="general", system=None, history=None, image=None, timeout=120, max_tokens=2000):
    """-> (answer, model). history: list of {"role","content"} before this prompt."""
    key = secret("openrouter_key")
    if not key:
        raise NoModel("no OpenRouter key in ~/.sams/openrouter_key")
    content = prompt
    if image:
        mime = mimetypes.guess_type(image)[0] or "image/jpeg"
        b64 = base64.b64encode(Path(image).read_bytes()).decode()
        content = [{"type": "text", "text": prompt},
                   {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}"}}]
    msgs = ([{"role": "system", "content": system}] if system else []) + (history or []) + \
           [{"role": "user", "content": content}]
    need_ctx = (len(json.dumps(msgs)) // 3) + max_tokens
    errors = []
    for model in chain(kind, need_ctx=need_ctx, need_image=bool(image)):
        try:
            r = requests.post(f"{API}/chat/completions", timeout=timeout,
                              headers={"Authorization": f"Bearer {key}", "X-Title": "Sams"},
                              json={"model": model, "messages": msgs, "max_tokens": max_tokens})
        except requests.RequestException as e:
            errors.append(f"{model}: {type(e).__name__}")
            continue
        if r.status_code == 429:
            _bench(model, 600)
            errors.append(f"{model}: rate limited")
            continue
        if r.status_code in (401, 402):
            raise NoModel(f"OpenRouter refused the key ({r.status_code})")
        if r.status_code == 403:   # model-specific: region block, moderation, data policy
            _bench(model, 7 * 24 * 3600)
            errors.append(f"{model}: 403 not available")
            continue
        try:
            data = r.json()
            text = (data["choices"][0]["message"].get("content") or "").strip()
        except Exception:
            text = ""
            data = {}
        if r.status_code >= 400 or not text:
            if r.status_code >= 500 or r.status_code == 404:
                _bench(model, 300)
            errors.append(f"{model}: {r.status_code} {str(data.get('error', ''))[:80]}")
            continue
        used = data.get("model") or model
        log("openrouter", kind, "->", used)
        return text, used
    raise NoModel("all free models failed: " + "; ".join(errors))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "models":
        ms = free_models(refresh=True)
        for m in sorted(ms, key=lambda m: -m["ctx"]):
            print(f"{m['id']:55} {m['ctx']:>8}  {','.join(m['in'])}")
        print()
        for k in PREFS:
            print(f"{k:10} -> {', '.join(chain(k))}")
        return 0
    if cmd == "pick":
        print(chain(rest[0] if rest else "general")[0]); return 0
    if cmd == "ask":
        kind, image, words = "general", None, []
        i = 0
        while i < len(rest):
            if rest[i] == "--kind":
                kind = rest[i + 1]; i += 2
            elif rest[i] == "--image":
                image = rest[i + 1]; i += 2
            else:
                words.append(rest[i]); i += 1
        prompt = " ".join(words)
        if not prompt and not sys.stdin.isatty():
            prompt = sys.stdin.read()
        if not prompt:
            print("no prompt", file=sys.stderr); return 2
        try:
            text, model = ask(prompt, kind=kind, image=image)
        except NoModel as e:
            print(f"error: {e}", file=sys.stderr); return 1
        print(text)
        print(f"[model: {model}]", file=sys.stderr)
        return 0
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
