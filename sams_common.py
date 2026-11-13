"""Shared bits for Sams' phone side (Telegram bridge, approvals, routines, OpenRouter router).

Everything private lives in ~/.sams (chmod 700): telegram_token, openrouter_key, chat_id,
pair_code, routines.json, approvals/<id>, telegram.pid. Nothing here is ever printed or logged.
"""
import json, os, time
from pathlib import Path

import requests

HOME = Path.home()
SAMS = HOME / ".sams"
APPROVALS = SAMS / "approvals"
ROUTINES = SAMS / "routines.json"
PIDFILE = SAMS / "telegram.pid"
LOGFILE = Path("/tmp/sams-telegram.log")
WORKDIR = HOME / "Documents/Jarvis"
SKILLS = WORKDIR / "skills"
ORB = WORKDIR / "orb"
CLAUDE = str(HOME / ".local/bin/claude")


def secret(name):
    p = SAMS / name
    try:
        return p.read_text().strip() or None
    except OSError:
        return None


def ensure_dirs():
    SAMS.mkdir(mode=0o700, exist_ok=True)
    APPROVALS.mkdir(mode=0o700, exist_ok=True)
    SKILLS.mkdir(exist_ok=True)


def log(*a):
    line = time.strftime("%H:%M:%S ") + " ".join(str(x) for x in a)
    try:
        with open(LOGFILE, "a") as f:
            f.write(line + "\n")
    except OSError:
        pass


# ---------- Telegram Bot API ----------
class TelegramError(Exception):
    pass


def tg(method, _timeout=30, files=None, **params):
    token = secret("telegram_token")
    if not token:
        raise TelegramError("no Telegram token in ~/.sams/telegram_token")
    url = f"https://api.telegram.org/bot{token}/{method}"
    try:
        if files:
            r = requests.post(url, data=params, files=files, timeout=_timeout)
        else:
            r = requests.post(url, json=params, timeout=_timeout)
        data = r.json()
    except (requests.RequestException, ValueError) as e:
        # never include the URL (it holds the token)
        raise TelegramError(f"{method}: {type(e).__name__}") from None
    if not data.get("ok"):
        raise TelegramError(f"{method}: {data.get('description', 'error')}")
    return data["result"]


def chat_id():
    c = secret("chat_id")
    return int(c) if c and c.lstrip("-").isdigit() else None


def split_text(text, n=4000):
    """Telegram allows 4096 chars per message; split at paragraph/line/space boundaries."""
    text = text.strip() or "(tomt svar)"
    out = []
    while len(text) > n:
        cut = max(text.rfind("\n\n", 0, n), text.rfind("\n", 0, n), text.rfind(" ", 0, n))
        if cut < n // 2:
            cut = n
        out.append(text[:cut].rstrip())
        text = text[cut:].lstrip()
    out.append(text)
    return out


# ---------- transport: "imessage" (default; Sams' own Apple ID in the macOS user "sams") or "telegram" ----------
SHARED = Path("/Users/Shared/Sams")      # outbox/ (main user -> sams user), inbox/ (sams user -> main user)


def transport():
    return (secret("transport") or "imessage").lower()


def owner():
    """Samuel's phone number / Apple ID email that Sams texts and accepts messages from."""
    return secret("owner_handle")


def imessage_send(text):
    if not owner():
        raise TelegramError("no ~/.sams/owner_handle")
    out = SHARED / "outbox"
    if not out.is_dir():
        raise TelegramError("iMessage bridge folder /Users/Shared/Sams/outbox is missing")
    name = f"{time.time_ns()}.json"
    tmp = out / ("." + name)
    tmp.write_text(json.dumps({"to": owner(), "text": text, "ts": time.time()}, ensure_ascii=False))
    os.chmod(tmp, 0o660)
    tmp.replace(out / name)   # atomic: the agent never sees a half-written file
    return name


def send(text, reply_markup=None, chat=None):
    """Send plain text to Samuel. Returns the last message id."""
    if transport() == "imessage":
        return imessage_send(text.strip() or "(tomt svar)")
    chat = chat or chat_id()
    if not chat:
        raise TelegramError("Sams is not paired with a Telegram chat yet (send /start <code> to the bot)")
    mid = None
    parts = split_text(text)
    for i, part in enumerate(parts):
        kw = {"chat_id": chat, "text": part, "disable_web_page_preview": True}
        if reply_markup and i == len(parts) - 1:
            kw["reply_markup"] = reply_markup
        mid = tg("sendMessage", **kw)["message_id"]
    return mid


def paired():
    return bool(owner()) if transport() == "imessage" else bool(chat_id())


def bridge_running():
    try:
        pid = int(PIDFILE.read_text())
        os.kill(pid, 0)
        return True
    except (OSError, ValueError):
        return False


def load_json(path, default):
    try:
        return json.loads(Path(path).read_text())
    except (OSError, ValueError):
        return default


def save_json(path, data):
    path = Path(path)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    os.chmod(tmp, 0o600)
    tmp.replace(path)


def skills_index():
    """One line per self-learned skill (name: description), read from each SKILL.md frontmatter."""
    lines = []
    for f in sorted(SKILLS.glob("*/SKILL.md")):
        name, desc = f.parent.name, ""
        try:
            head = f.read_text()[:800]
        except OSError:
            continue
        hl = head.splitlines()
        for i, ln in enumerate(hl):
            if ln.startswith("description:"):
                desc = ln.split(":", 1)[1].strip()
                if desc in ("|", ">", "|-", ">-", ""):   # YAML block: take the indented lines below
                    desc = " ".join(x.strip() for x in hl[i + 1:i + 4] if x.startswith((" ", "\t")))
                desc = desc.strip('"')[:200]
                break
        lines.append(f"- {name}: {desc}")
    return "\n".join(lines) or "(ingen endnu)"


MEMORY_PROMPT = """\
MEMORY (like Azaris/Hermes): when you learn something LASTING about Samuel (a preference, a contact, a price, a \
recurring fact, a correction of how you work), add it as one short line to the right section of \
~/Documents/Jarvis/CLAUDE.md with Edit, without asking and without announcing it. No secrets/passwords, no \
one-off details, no duplicates; fix outdated lines instead of adding contradicting ones. Every change is \
versioned: if he says something you remembered is wrong, run ~/Documents/Jarvis/orb/sams-memory history and \
sams-memory undo <id> (or edit the line)."""


def memory_snapshot(msg):
    import subprocess
    try:
        subprocess.run([str(ORB / "sams-memory"), "snapshot", msg], capture_output=True, timeout=30)
    except Exception:
        pass


SKILLS_PROMPT = """\
SKILLS (your own + vetted ones from OpenClaw's ClawHub): procedures in ~/Documents/Jarvis/skills/<name>/SKILL.md.
Index: {index}
- FIRST check the index: if a skill matches the request (e.g. any weather question -> weather), Read that SKILL.md BEFORE doing anything else (no WebSearch first) and follow it.
- After you finish a NEW non-trivial multi-step workflow, hit a dead end and found the working path, or \
Samuel corrected your approach: create or patch a skill (Write/Edit). Format: YAML frontmatter with \
name and description (one line: when to use it), then sections When to use / Procedure / Pitfalls / \
Verification. Lessons, not logs: no dates, no incident stories, no secrets. Keep it under ~150 lines; \
prefer patching an existing skill over making a near-duplicate. Don't mention skill bookkeeping unless asked."""
