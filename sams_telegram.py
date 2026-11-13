#!/Users/samueltang/Documents/Jarvis/orb/venv/bin/python
"""Sams on Telegram: chat, voice notes, photos, approval cards and scheduled routines.

Runs as its own LaunchAgent (dk.ststeadi.sams-telegram), independent of the orb app, so Samuel can
reach Sams from his phone while the Mac is on. Like Hermes Agent's messaging gateway:
  * text / voice note / photo / file  -> one Claude session per conversation (resumed between
    messages, fresh after a long pause), Haiku/Sonnet/Opus picked per message
  * Claude down or out of quota       -> answered by a FREE OpenRouter model (sams_llm), clearly marked
  * inline Ja/Nej buttons              -> answers for `sams-approve` (approval cards)
  * routines (~/.sams/routines.json)   -> run on their cron schedule, result sent here (`sams-routine`)
Commands: /start <code> (pair once), /ny (new conversation), /status, /rutiner, /hjaelp
Log: /tmp/sams-telegram.log (never contains tokens or message texts beyond short previews).
"""
import json, os, queue, re, signal, subprocess, sys, tempfile, threading, time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import jarvis_profiles  # noqa: E402
import sams_jobs  # noqa: E402
import sams_llm  # noqa: E402
from sams_common import (SAMS, APPROVALS, ROUTINES, PIDFILE, WORKDIR, CLAUDE, SKILLS_PROMPT,  # noqa: E402
                         TelegramError, tg, send, secret, chat_id, ensure_dirs, log, load_json,
                         save_json, skills_index, transport, owner, SHARED,
                         MEMORY_PROMPT, memory_snapshot)

WHISPER_URL = "http://127.0.0.1:2022/v1/audio/transcriptions"
INBOX_DIR = SAMS / "inbox"          # photos/files he sends (Claude can Read them)
STATE = SAMS / "telegram_state.json"   # offset, session id, last turn, short history for fallback
FRESH_AFTER_IDLE = 3 * 3600
FRESH_AFTER_TOKENS = 120_000
TURN_TIMEOUT = 30 * 60
ROUTINE_TIMEOUT = 20 * 60

TG_PROMPT = """You are Sams, Samuel's personal assistant (the same Sams as the voice orb on his Mac), \
now texting with him on his PHONE (Telegram). He writes Danish (sometimes English, often dictated with typos): \
answer in the language he used, and read past typos to what he means.
HOW YOU TALK (ChatGPT voice style, same as the orb): like a sharp, warm friend texting back, not a report. \
Natural spoken Danish, contractions and everyday words; vary your sentence openings; no "Selvfølgelig!", "Godt \
spørgsmål" or other filler, no generic closing question like "Er der andet?". Short by default (1-3 sentences); \
longer only when he asks for detail or the task truly needs it. Not lightweight: give a real, considered answer \
or opinion, plus one interesting detail when it earns its place. Humor only from the situation, light touch. \
Be curious about what he's actually trying to do; ask at most ONE question, only when you can't proceed sensibly \
without it — otherwise make a reasonable assumption, say it in a few words, and go. If he answers your question \
with something short ("ja", "til mig selv"), continue from context instead of asking again. \
Doing work: if you can answer from what you know, answer now. Otherwise say in one sentence what you're checking, \
then do it. Never say something is done/sent/booked until it actually is ("jeg tjekker" vs "jeg har tjekket"). \
Talk about his task, not your tools. Tell continuation, correction, cancellation and a new request apart. \
Plain text only (markdown shows as raw symbols: no **, #, backticks, no headings or tables unless he asks); \
a short dash list is fine when listing several things.
You run on his Mac with his tools: Bash (calendar via osascript, mail via orb/mail-read and the Gmail \
connector, files, apps), web search, etc. Follow CLAUDE.md. Do the work yourself in this chat; for long \
jobs say briefly what you'll do first, then do it.
APPROVAL CARDS: before anything big or irreversible (sending a mail/message, paying, deleting, booking, \
changing someone else's data) run: ~/Documents/Jarvis/orb/sams-approve "<exactly what will happen, incl. the \
full text to be sent>" — it asks him on his phone (he answers JA/NEJ) and prints JA, NEJ or TIMEOUT. Only JA counts as his \
explicit yes. Never ask for approval of trivial or read-only things.
CODE JOBS: track every coding job you start for him with ~/Documents/Jarvis/orb/sams-cloudjob (add / start / progress <id> <pct> \"what now\" / done); run `sams-cloudjob next` to pick the next job - his queue order decides. He sees it by writing \"code med Sams\".

ROUTINES: he can ask for recurring jobs ("hver morgen kl 7 ..."). Manage them with \
~/Documents/Jarvis/orb/sams-routine add "<cron: min hour dom mon dow>" "<name>" "<full instructions>" | list | \
remove <id> | run <id>. Times are local Danish time. Confirm the schedule in words.
OTHER AIs: Claude (you) is the main brain. FREE models via ~/Documents/Jarvis/orb/sams-llm ask --kind \
general|fast|reasoning|code|long|vision|danish "prompt" when another model makes more sense: a second \
opinion, a huge document (1M-token context), cheap bulk summarising/translation, video/audio input. Don't \
send private data (mails, passwords, health, money) to them unless he says it's fine.
PHONE CALLS: ~/Documents/Jarvis/orb/sams-call "<what to say>" rings his phone (only if it's set up; if it \
prints NOT_CONFIGURED, say so). Use it only when he asks or for something truly urgent he asked to be called about.
Images/files he sends are saved locally; the message gives the path — Read it.
SIRI: a message starting with "(siri)" came from Siri on his iPhone and your answer is READ ALOUD: answer in 1-3 short spoken sentences, no lists, links or emojis. For long jobs say you're on it.
"""

ROUTINE_PROMPT = """You are Sams, Samuel's assistant, running one of his scheduled ROUTINES unattended. \
The result is sent to him as a text message on his phone. Follow CLAUDE.md (never send mails/messages or delete \
anything; for those, use ~/Documents/Jarvis/orb/sams-approve "<exact action>" which asks him on Telegram \
and prints JA/NEJ/TIMEOUT; only JA counts). Be token-frugal. Final answer: a short plain-text message in \
Danish, no markdown. If there is genuinely nothing worth telling him, answer exactly: NOTHING"""

OPUS_RE = re.compile(r"\b(opus|tænk grundigt|tænk dig godt om|think hard|use opus|dit bedste)\b", re.I)
TASK_RE = re.compile(
    r"\b(lav|byg|skriv|ret|fix|opdater|flyt|find|søg|undersøg|sammenlign|planlæg|book|aflys|svar|"
    r"kladde|mail|faktura|kalender|aftale|rutine|hver (dag|morgen|aften|uge)|påmind|husk|"
    r"make|build|write|draft|edit|update|research|compare|plan|schedule|reply|remind|invoice|code|script)\w*",
    re.I)

stop = threading.Event()
MODE = os.environ.get("SAMS_MODE") or ("siri" if os.environ.get("SAMS_SIRI_ONLY") else "full")
# full   = everything here (Telegram polling, routines, endpoint) - the always-on cloud server, or the Mac alone
# helper = the Mac when the cloud runs Telegram: only the endpoint (+ worker), answers the cloud's sams-mac
# siri   = endpoint only (old cloud test mode)
CLOUD_NOTE = ("\nRIGHT NOW you run on Sams' always-on cloud server (Linux), NOT his Mac: no Apple Calendar, "
              "Apple Mail, iMessage/WhatsApp databases, osascript or Mac files here. For those run "
              "~/Documents/Jarvis/orb/sams-mac \"<the task in plain words>\" - the Mac's Sams does it with its own "
              "tools and prints the answer (can take minutes). MAC_OFFLINE = the Mac is off/asleep: say so and "
              "offer to do it later (e.g. a one-off routine). There is NO Gmail connector on this server either: mail "
              "lookups (bookings, tickets, invoices) also go through sams-mac. Web search and OpenRouter models "
              "(sams-llm) work here directly. If the Mac is offline, say so in one sentence and still help with "
              "what the web can answer (e.g. look up the ferry/flight timetable).\n"
              ) if sys.platform.startswith("linux") else ""
HELPER_PREFIX = ("(fra cloud-Sams: do this on the Mac and reply with the result for the cloud Sams to pass on. "
                 "Do NOT send messages, ask approval cards or message Samuel yourself; if something needs his "
                 "yes, say exactly what and stop.) ")
work_q: "queue.Queue" = queue.Queue()
state_lock = threading.Lock()


def load_state():
    return load_json(STATE, {"offset": 0, "session": None, "last": 0, "ctx": 0, "history": [], "sticky": 0})


def save_state(st):
    with state_lock:
        save_json(STATE, st)


# ---------- helpers ----------
def typing_while(event):
    while not event.wait(4.5):
        try:
            tg("sendChatAction", chat_id=chat_id(), action="typing", _timeout=10)
        except TelegramError:
            pass


FFMPEG = "/opt/homebrew/bin/ffmpeg" if Path("/opt/homebrew/bin/ffmpeg").exists() else "ffmpeg"
LINUX = sys.platform.startswith("linux")
PIPER_VOICE = SAMS / "piper/da_DK-talesyntese-medium.onnx"


def local_transcribe(wav):
    """Cloud server: faster-whisper on CPU (small model, int8, Danish first)."""
    # loaded per call and freed again: the server has only 1 GB RAM (Claude needs it too)
    import gc, wave
    import numpy as np
    from faster_whisper import WhisperModel
    with wave.open(str(wav)) as w:   # 16 kHz mono s16 from ffmpeg; decode ourselves (PyAV mismatch)
        audio = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768.0
    m = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=2)
    try:
        segs, _ = m.transcribe(audio, beam_size=1, vad_filter=True)
        return " ".join(x.text.strip() for x in segs).strip()
    finally:
        del m
        gc.collect()


def download(file_id, suffix):
    info = tg("getFile", file_id=file_id)
    token = secret("telegram_token")
    r = requests.get(f"https://api.telegram.org/file/bot{token}/{info['file_path']}", timeout=60)
    r.raise_for_status()
    INBOX_DIR.mkdir(mode=0o700, exist_ok=True)
    p = INBOX_DIR / f"{time.strftime('%Y%m%d-%H%M%S')}-{file_id[-8:]}{suffix}"
    p.write_bytes(r.content)
    return p


def transcribe(path):
    with tempfile.TemporaryDirectory() as td:
        wav = Path(td) / "v.wav"
        subprocess.run([FFMPEG, "-loglevel", "error", "-y", "-i", str(path),
                        "-ar", "16000", "-ac", "1", str(wav)], check=True, timeout=60)
        if LINUX:
            return local_transcribe(wav)
        with open(wav, "rb") as f:
            r = requests.post(WHISPER_URL, files={"file": ("v.wav", f, "audio/wav")},
                              data={"model": "whisper-1", "response_format": "json"}, timeout=120)
        r.raise_for_status()
        return (r.json().get("text") or "").strip()


def pick_model(text, st):
    if OPUS_RE.search(text) or jarvis_profiles.HARD_RE.search(text):
        st["sticky"] = 2
        return jarvis_profiles.OPUS
    if TASK_RE.search(text) or len(text) > 160 or text.startswith("[Samuel sendte"):  # photos/files: Haiku misreads images
        st["sticky"] = max(st.get("sticky", 0), 1)
        return jarvis_profiles.SONNET
    if st.get("sticky", 0) > 0:
        st["sticky"] -= 1
        return jarvis_profiles.SONNET
    return jarvis_profiles.HAIKU


LIMIT_RE = re.compile(r"(usage limit|rate limit|overloaded|quota|credit balance|529|429|limit reached|"
                      r"session limit|weekly limit|try again later|authentication|login)", re.I)


def run_claude(prompt, model, args, system, resume=None, timeout=TURN_TIMEOUT):
    """One-shot `claude -p` (JSON output). -> dict(result, session_id, is_error, ctx)"""
    cmd = [CLAUDE, "-p", "--output-format", "json", "--permission-mode", "auto", "--model", model,
           *args, "--append-system-prompt", system]
    if resume:
        cmd += ["--resume", resume]
    try:
        p = subprocess.run(cmd, input=prompt, cwd=WORKDIR, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"result": "", "is_error": True, "error": "timeout", "session_id": resume, "ctx": 0}
    try:
        data = json.loads(p.stdout.strip().splitlines()[-1])
    except (ValueError, IndexError):
        return {"result": "", "is_error": True, "error": (p.stderr or p.stdout)[-300:], "session_id": resume, "ctx": 0}
    u = data.get("usage") or {}
    ctx = u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
    return {"result": (data.get("result") or "").strip(), "is_error": bool(data.get("is_error")),
            "error": data.get("subtype", ""), "session_id": data.get("session_id") or resume, "ctx": ctx}


def tg_args(text):
    """Tools for a Telegram turn: same slim per-job selection as the orb's workers (Gmail + whatever the
    text mentions), keeping the full built-in tool set."""
    prof = jarvis_profiles.worker_profile(text[:300], text)
    return [a for a in prof["args"]] if prof["kind"] != "davinci-full" else []


def fallback_answer(text, st, why):
    hist = []
    for u, a in st.get("history", [])[-6:]:
        hist += [{"role": "user", "content": u}, {"role": "assistant", "content": a}]
    try:
        ans, model = sams_llm.ask(text, kind="danish", history=hist,
                                  system="You are Sams, Samuel's helpful personal assistant. Answer briefly in the "
                                         "language he writes. You have NO access to his mail, calendar or files right now.")
        ans = re.sub(r"\*\*|__|^#+\s*|`", "", ans, flags=re.M)   # plain text on the phone
        return f"(Claude svarer ikke lige nu: {why}. Svar fra gratis model {model.split('/')[-1]}, uden adgang til dine ting.)\n\n{ans}"
    except sams_llm.NoModel as e:
        log("fallback failed", e)
        return f"Claude svarer ikke lige nu ({why}), og ingen gratis model kunne svare heller. Prøv igen om lidt."


# ---------- one conversation turn ----------
def handle_turn(text, quiet=False):
    """quiet: a helper request from the cloud Sams -> own session, nothing sent to Telegram, no state change."""
    st = {} if quiet else load_state()
    now = time.time()
    if st.get("session") and (now - st.get("last", 0) > FRESH_AFTER_IDLE or st.get("ctx", 0) > FRESH_AFTER_TOKENS):
        st["session"] = None
    model = pick_model(text, st)
    system = TG_PROMPT + CLOUD_NOTE + "\n" + MEMORY_PROMPT + "\n" + SKILLS_PROMPT.format(index=skills_index())
    stamp = time.strftime("[%a %d.%m.%Y %H:%M] ")
    done = threading.Event()
    if transport() == "telegram" and not quiet:
        threading.Thread(target=typing_while, args=(done,), daemon=True).start()
        try:
            tg("sendChatAction", chat_id=chat_id(), action="typing", _timeout=10)
        except TelegramError:
            pass
    log(f"turn ({model.split('-')[1]}, {'resume' if st.get('session') else 'new'}): {text[:60]!r}")
    try:
        r = run_claude(stamp + text, model, tg_args(text), system, resume=st.get("session"))
        if r["is_error"] and st.get("session") and not LIMIT_RE.search(r["error"] + r["result"]):
            log("resume failed, retrying fresh:", r["error"][:120])
            r = run_claude(stamp + text, model, tg_args(text), system)
        if (r["is_error"] or not r["result"]) and model == jarvis_profiles.HAIKU \
                and not LIMIT_RE.search(r["error"] + r["result"]):
            log("escalating to Sonnet after a failed Haiku turn")   # like Hermes' escalate_model
            r = run_claude(stamp + text, jarvis_profiles.SONNET, tg_args(text), system, resume=r.get("session_id") or st.get("session"))
    finally:
        done.set()
    if r["is_error"] or not r["result"]:
        why = "kvote/overbelastet" if LIMIT_RE.search(r["error"] + r["result"]) else (r["error"] or "fejl")[:60]
        log("claude failed:", why, (r["result"] or "")[:150])
        answer = fallback_answer(text, st, why)
    else:
        answer = re.sub(r"\*\*|__|^#{1,6}\s+|`", "", r["result"], flags=re.M)   # plain text on the phone
        st["session"], st["ctx"] = r["session_id"], r["ctx"]
    if quiet:
        daily_log("[fra cloud-Sams] " + text, answer)
        return answer
    st["last"] = time.time()
    st["history"] = (st.get("history", []) + [[text[:1500], answer[:1500]]])[-8:]
    save_state(st)
    send(answer)
    if text.startswith("(talebesked)") and transport() == "telegram":
        try:
            send_voice(answer)
        except Exception as e:
            log("voice reply failed", type(e).__name__, str(e)[:120])
    daily_log(text, answer)
    memory_snapshot("phone turn: " + " ".join(text.split())[:60])
    return answer


DANISH_RE = re.compile(r"[æøå]|\b(og|ikke|jeg|du|det|har|til|er|en|på|med|kan|skal)\b", re.I)


def send_voice(answer):
    """Voice-to-voice like Azaris: answer a voice note with a voice note (macOS voices, free, local).
    Danish -> Sara, otherwise an English voice. Long answers are cut to the first ~700 chars (the text
    message has everything)."""
    spoken = re.sub(r"https?://\S+", "link", answer)
    spoken = re.sub(r"[*_#`>|]", "", spoken)
    if len(spoken) > 700:
        cut = spoken.rfind(". ", 0, 700)
        spoken = spoken[:cut + 1 if cut > 200 else 700] + " Resten står i beskeden."
    voice = "Sara" if len(DANISH_RE.findall(spoken)) >= 2 else "Samantha"
    with tempfile.TemporaryDirectory() as td:
        aiff, ogg = Path(td) / "a.aiff", Path(td) / "a.ogg"
        if LINUX:   # Piper, free local Danish voice (English text is read with it too)
            aiff = Path(td) / "a.wav"
            subprocess.run([sys.executable, "-m", "piper", "-m", str(PIPER_VOICE), "-f", str(aiff)],
                           input=spoken, text=True, check=True, timeout=180, capture_output=True)
        else:
            subprocess.run(["/usr/bin/say", "-v", voice, "-r", "185", "-o", str(aiff), spoken], check=True, timeout=120)
        subprocess.run([FFMPEG, "-loglevel", "error", "-y", "-i", str(aiff), "-c:a", "libopus",
                        "-b:a", "32k", "-ar", "48000", "-ac", "1", str(ogg)], check=True, timeout=120)
        with open(ogg, "rb") as f:
            tg("sendVoice", _timeout=60, files={"voice": ("svar.ogg", f, "audio/ogg")}, chat_id=chat_id())


def daily_log(text, answer):
    try:
        d = WORKDIR / "memory/daily"
        d.mkdir(parents=True, exist_ok=True)
        with open(d / f"{time.strftime('%Y-%m-%d')}.md", "a") as f:
            f.write(f"{time.strftime('%H:%M')} [Telegram] He: {' '.join(text.split())[:300]} / "
                    f"Sams: {' '.join(answer.split())[:400]}\n")
    except OSError:
        pass


def worker():
    while not stop.is_set():
        try:
            item = work_q.get(timeout=1)
        except queue.Empty:
            continue
        box = item if isinstance(item, dict) else None
        try:
            ans = handle_turn(box["text"], box.get("quiet", False)) if box else handle_turn(item)
            if box:
                box["answer"] = ans
        except Exception as e:   # never let one message kill the bridge
            log("turn error", type(e).__name__, str(e)[:200])
            try:
                send(f"Der gik noget galt: {type(e).__name__}. Prøv igen.")
            except TelegramError:
                pass
        finally:
            if box:
                box["done"].set()
            work_q.task_done()


# ---------- Siri: "Spørg Sams" shortcut on the iPhone ----------
# A tiny HTTP endpoint the iPhone Shortcut calls over Tailscale (private network, never the open
# internet): POST /ask {"text": "..."} with header X-Sams-Key -> {"answer": "..."} which Siri reads aloud.
# Off unless ~/.sams/siri_bind holds the address to listen on (the Tailscale IP, or 127.0.0.1 for tests).
SIRI_PORT = 8787
WAKE_RE = re.compile(r"^\W*((hej|hey|hi|spørg|sporg|åbn|åben|open|ask|kære)\s+)*"
                     r"(sams|sam|samsøe|samsø|jarvis|az|min assistent)\b[\s,.!?:-]*", re.I)
SIRI_WAIT = 50   # Shortcuts gives up after ~60 s; after this the answer still comes on Telegram


def siri_server():
    import hmac
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    bind, key = secret("siri_bind"), secret("siri_key")
    if not bind or not key:
        return
    if bind.startswith("0.") or bind in ("::", "*"):
        log("siri: refusing to listen on all interfaces; put the Tailscale IP in ~/.sams/siri_bind")
        return

    class H(BaseHTTPRequestHandler):
        def log_message(self, *a):
            pass

        def reply(self, code, obj):
            body = json.dumps(obj, ensure_ascii=False).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_POST(self):
            if self.path not in ("/ask", "/approval") or not hmac.compare_digest(self.headers.get("X-Sams-Key", ""), key):
                return self.reply(403, {"answer": "Adgang nægtet."})
            if self.path == "/approval":   # the cloud got his tap on a card that this machine asked
                try:
                    req = json.loads(self.rfile.read(min(int(self.headers.get("Content-Length", 0)), 2000)))
                    aid, ans = req["id"], req["ans"]
                    assert re.fullmatch(r"[0-9a-f]{8,32}", aid) and ans in ("yes", "no")
                except Exception:
                    return self.reply(400, {"ok": False})
                f = APPROVALS / aid
                ok = f.exists() and f.read_text().strip() == "PENDING"
                if ok:
                    f.write_text("JA" if ans == "yes" else "NEJ")
                log("approval relayed", aid, ans if ok else "(not pending)")
                return self.reply(200, {"ok": ok})
            try:
                n = min(int(self.headers.get("Content-Length", 0)), 20000)
                raw = self.rfile.read(n).decode("utf-8", "replace")
                try:
                    req = json.loads(raw)
                    text = (req.get("text") or "").strip()
                except (ValueError, AttributeError):
                    req, text = None, raw.strip()
            except Exception:
                return self.reply(400, {"answer": "Jeg fik ikke noget spørgsmål."})
            text = text if req and req.get("quiet") else WAKE_RE.sub("", text).strip()   # he often repeats the shortcut's name into the dictation
            if len(text) < 3:
                return self.reply(200, {"answer": "Ja? Start mig igen, og stil spørgsmålet lige efter navnet."})
            log(f"siri request ({len(text)} chars)")
            quiet = bool(req.get("quiet")) if isinstance(req, dict) else False
            box = {"text": (HELPER_PREFIX + text if quiet else f"(siri) {text}"),
                   "done": threading.Event(), "answer": None, "quiet": quiet}
            busy = work_q.unfinished_tasks > 0
            work_q.put(box)
            if box["done"].wait(600 if quiet else SIRI_WAIT) and box["answer"]:
                return self.reply(200, {"answer": box["answer"]})
            self.reply(200, {"answer": ("Jeg er i gang med noget andet, " if busy else "Det tager lidt tid. ")
                                       + "Svaret kommer på Telegram."})

    srv, warned = None, False
    while srv is None and not stop.is_set():   # the Tailscale IP may not be up yet (boot, wake from sleep)
        try:
            srv = ThreadingHTTPServer((bind, SIRI_PORT), H)
        except OSError as e:
            if not warned:
                log("siri: cannot listen on", bind, e, "- retrying every 20 s"); warned = True
            stop.wait(20)
    if srv is None:
        return
    log(f"siri endpoint on {bind}:{SIRI_PORT}")
    threading.Thread(target=lambda: (stop.wait(), srv.shutdown()), daemon=True).start()
    srv.serve_forever()


# ---------- "Code med Sams": kodejobs + prioriteret kø (sams_jobs) ----------
CODE_RE = re.compile(r"^\W*(/code(@\w+)?|code\s+med\s+sams|kode\s+med\s+sams)\W*$", re.I)
MOVE_RE = re.compile(r"^\s*(?:job\s+)?(\d+)\s+(op|ned|øverst|top)\s*$", re.I)   # "2 op", "job 3 øverst"


def send_code_view():
    kb = sams_jobs.view_keyboard() if transport() == "telegram" else None
    send(sams_jobs.view_text(), reply_markup=kb)


def handle_code_text(text):
    """True hvis beskeden var kodejob-visning eller 'N op/ned/øverst' (nummer = placering i den viste kø)."""
    if CODE_RE.match(text):
        send_code_view(); return True
    m = MOVE_RE.match(text)
    act = sams_jobs.active_jobs()
    if m and 1 <= int(m.group(1)) <= len(act):
        how = {"op": "up", "ned": "down"}.get(m.group(2).lower(), "top")
        sams_jobs.move(act[int(m.group(1)) - 1]["id"], how)
        send_code_view(); return True
    return False


def on_code_callback(cb, jid, action):
    if action != "noop" and action != "refresh":
        try:
            sams_jobs.move(jid, action)
        except KeyError:
            pass
    msg = cb["message"]
    try:
        tg("answerCallbackQuery", callback_query_id=cb["id"])
        tg("editMessageText", chat_id=msg["chat"]["id"], message_id=msg["message_id"],
           text=sams_jobs.view_text(), reply_markup=sams_jobs.view_keyboard())
    except TelegramError as e:
        log("code view update failed", e)   # fx "message is not modified" ved Opdater uden ændring


# ---------- incoming updates ----------
HELP = ("Skriv eller send en talebesked, billede eller fil.\n"
        "/ny  ny samtale\n/status  hvad kører\n/rutiner  dine faste rutiner\n"
        "/code  kodejobs og kø (eller skriv \"code med Sams\")\n"
        "Skriv \"opus\" eller \"tænk grundigt\" for den stærkeste model.")


def on_message(msg):
    cid = msg["chat"]["id"]
    text = (msg.get("text") or msg.get("caption") or "").strip()
    paired = chat_id()
    if not paired:
        code = secret("pair_code")
        if code and code in re.sub(r"\D", "", text):
            p = SAMS / "chat_id"
            p.write_text(str(cid)); os.chmod(p, 0o600)
            (SAMS / "pair_code").unlink(missing_ok=True)
            send("Hej Samuel, det er Sams. Vi er forbundet nu.\n\n" + HELP, chat=cid)
            log("paired with chat", cid)
        else:
            log("ignored message from unpaired chat", cid, f"(text had {len(text)} chars, digits match: False)")
            try:
                send("Skriv koden fra Mac'en (6 cifre) for at forbinde mig.", chat=cid)
            except TelegramError:
                pass
        return
    if cid != paired:
        log("ignored message from foreign chat", cid)
        return
    if text in ("/start", "/hjaelp", "/help"):
        send(HELP); return
    if text == "/ny":
        st = load_state(); st["session"], st["history"], st["sticky"] = None, [], 0; save_state(st)
        send("Ny samtale."); return
    if text == "/status":
        send(status_text()); return
    if text == "/rutiner":
        send(routines_text()); return
    if handle_code_text(text):
        return
    try:
        if msg.get("voice") or msg.get("audio"):
            f = msg.get("voice") or msg.get("audio")
            path = download(f["file_id"], ".ogg")
            heard = transcribe(path)
            path.unlink(missing_ok=True)
            if not heard:
                send("Jeg kunne ikke høre noget i talebeskeden."); return
            log("voice note transcribed", len(heard), "chars")
            text = f"(talebesked) {heard}"
        elif msg.get("photo"):
            path = download(msg["photo"][-1]["file_id"], ".jpg")
            text = f"[Samuel sendte et billede: {path}] {text}"
            if text.rstrip().endswith("]"):  # no caption: give the context a Steadicam operator's photo usually needs
                text += " (ingen tekst; Read billedet, tænk på hans arbejde/udstyr som Steadicam-operatør, og gæt kvalificeret før du spørger)"
        elif msg.get("document"):
            d = msg["document"]
            suffix = Path(d.get("file_name") or "fil").suffix[:10]
            path = download(d["file_id"], suffix)
            text = f"[Samuel sendte filen {d.get('file_name', '')}: {path}] {text}"
    except Exception as e:
        log("media error", type(e).__name__, str(e)[:150])
        send("Jeg kunne ikke hente eller forstå filen/talebeskeden."); return
    if text:
        if work_q.qsize() or busy():
            send("Modtaget, jeg tager den når jeg er færdig med den forrige.")
        work_q.put(text)


def busy():
    return work_q.unfinished_tasks > work_q.qsize()


def relay_approval(aid, ans):
    ip, key = secret("mac_ip"), secret("siri_key")
    if not ip or not key:
        return False
    try:
        r = requests.post(f"http://{ip}:{SIRI_PORT}/approval", json={"id": aid, "ans": ans},
                          headers={"X-Sams-Key": key}, timeout=10)
        return bool(r.json().get("ok"))
    except Exception as e:
        log("approval relay to Mac failed", type(e).__name__)
        return False


def on_callback(cb):
    if not chat_id() or cb.get("message", {}).get("chat", {}).get("id") != chat_id():
        return
    data = cb.get("data") or ""
    mc = re.fullmatch(r"cj:([0-9a-f]+|-):(up|down|top|noop|refresh)", data)
    if mc:
        on_code_callback(cb, *mc.groups()); return
    m = re.fullmatch(r"ap:([0-9a-f]{8,32}):(yes|no)", data)
    if not m:
        return
    aid, ans = m.groups()
    f = APPROVALS / aid
    pending = f.exists() and f.read_text().strip() == "PENDING"
    if pending:
        f.write_text("JA" if ans == "yes" else "NEJ")
    elif not f.exists():
        pending = relay_approval(aid, ans)   # asked by the Mac's Sams (orb jobs, Mac routines)
    try:
        tg("answerCallbackQuery", callback_query_id=cb["id"], text="Godkendt" if ans == "yes" else "Afvist")
        if pending:
            msg = cb["message"]
            tg("editMessageText", chat_id=msg["chat"]["id"], message_id=msg["message_id"],
               text=msg.get("text", "") + ("\n\n✅ Godkendt" if ans == "yes" else "\n\n❌ Afvist"))
    except TelegramError as e:
        log("callback answer failed", e)
    log("approval", aid, ans if pending else f"{ans} (too late)")


def poll():
    st = load_state()
    offset = st.get("offset", 0)
    while not stop.is_set():
        try:
            updates = tg("getUpdates", _timeout=65, offset=offset, timeout=50,
                         allowed_updates=["message", "callback_query"])
        except TelegramError as e:
            log("poll error", e)
            stop.wait(10 if "Conflict" not in str(e) else 30)
            continue
        for u in updates:
            offset = u["update_id"] + 1
            try:
                if "message" in u:
                    on_message(u["message"])
                elif "callback_query" in u:
                    on_callback(u["callback_query"])
            except Exception as e:
                log("update error", type(e).__name__, str(e)[:200])
        if updates:
            st = load_state(); st["offset"] = offset; save_state(st)


# ---------- iMessage (via the "sams" macOS user's agent, files in /Users/Shared/Sams) ----------
YES_RE = re.compile(r"^\s*(ja|jep|yes|ok|okay|godkend[t]?|j)\s*[.!]*\s*$", re.I)
NO_RE = re.compile(r"^\s*(nej|no|nope|afvis|n)\s*[.!]*\s*$", re.I)


def same_handle(a, b):
    if not a or not b:
        return False
    if "@" in a or "@" in b:
        return a.strip().lower() == b.strip().lower()
    da, db = re.sub(r"\D", "", a), re.sub(r"\D", "", b)
    return len(da) >= 8 and da[-8:] == db[-8:]


def answer_pending_approval(yes):
    """He texted ja/nej: answer the oldest pending approval. -> True if one was waiting."""
    pend = []
    for f in APPROVALS.iterdir():
        try:
            if f.read_text().strip() == "PENDING":
                pend.append((f.stat().st_mtime, f))
        except OSError:
            continue   # answered/removed meanwhile
    pend = [f for _, f in sorted(pend)]
    if not pend:
        return False
    pend[0].write_text("JA" if yes else "NEJ")
    log("approval", pend[0].name, "yes" if yes else "no")
    send("✅ Godkendt, jeg går videre." if yes else "❌ Afvist, jeg gør det ikke.")
    return True


def on_imessage(item):
    if not same_handle(item.get("from", ""), owner()):
        log("ignored iMessage from another sender")
        return
    text = (item.get("text") or "").replace("\ufffc", "").strip()
    if text and (YES_RE.match(text) or NO_RE.match(text)) and answer_pending_approval(bool(YES_RE.match(text))):
        return
    low = text.lower()
    if low in ("/ny", "ny samtale"):
        st = load_state(); st["session"], st["history"], st["sticky"] = None, [], 0; save_state(st)
        send("Ny samtale."); return
    if low in ("/status", "status?"):
        send(status_text()); return
    if low in ("/rutiner", "rutiner?"):
        send(routines_text()); return
    if low in ("/hjaelp", "/hjælp", "hjælp?"):
        send(HELP.replace("Skriv eller send en talebesked, billede eller fil.", "Skriv eller send en lydbesked, et billede eller en fil.")); return
    parts = []
    for a in item.get("attachments") or []:
        p = Path(a)
        if not p.exists():
            continue
        if p.suffix.lower() in (".caf", ".m4a", ".amr", ".mp3", ".aac", ".wav", ".ogg", ".opus"):
            try:
                heard = transcribe(p)
            except Exception as e:
                log("audio transcribe failed", type(e).__name__)
                heard = ""
            parts.append(f"(lydbesked) {heard}" if heard else "(lydbesked jeg ikke kunne høre)")
        elif p.suffix.lower() in (".jpg", ".jpeg", ".png", ".heic", ".gif", ".webp"):
            parts.append(f"[Samuel sendte et billede: {p}]")
        else:
            parts.append(f"[Samuel sendte filen {p.name}: {p}]")
    text = " ".join(parts + ([text] if text else [])).strip()
    if text:
        if work_q.qsize() or busy():
            send("Modtaget, jeg tager den når jeg er færdig med den forrige.")
        work_q.put(text)


def poll_imessage():
    inbox = SHARED / "inbox"
    while not stop.wait(1.5):
        try:
            files = sorted(inbox.glob("*.json"))
        except OSError:
            continue
        for f in files:
            try:
                item = json.loads(f.read_text())
            except (OSError, ValueError):
                continue
            f.unlink(missing_ok=True)
            try:
                on_imessage(item)
            except Exception as e:
                log("imessage handler error", type(e).__name__, str(e)[:200])


# ---------- routines ----------
def cron_field(spec, value, lo, hi):
    for part in spec.split(","):
        step = 1
        if "/" in part:
            part, s = part.split("/", 1); step = int(s)
            if step < 1:
                raise ValueError("step")
        if part == "*":
            a, b = lo, hi
        elif "-" in part:
            a, b = (int(x) for x in part.split("-", 1))
        else:
            a = b = int(part)
        if a <= value <= b and (value - a) % step == 0:
            return True
    return False


def cron_match(expr, t):
    f = expr.split()
    if len(f) != 5:
        return False
    mi, ho, dom, mon, dow = f
    wd = (t.tm_wday + 1) % 7   # cron: 0 = Sunday
    dow_ok = cron_field(dow, wd, 0, 7) or (wd == 0 and cron_field(dow, 7, 0, 7))
    dom_ok = cron_field(dom, t.tm_mday, 1, 31)
    day_ok = (dom_ok and dow_ok) if (dom == "*" or dow == "*") else (dom_ok or dow_ok)
    return cron_field(mi, t.tm_min, 0, 59) and cron_field(ho, t.tm_hour, 0, 23) and cron_field(mon, t.tm_mon, 1, 12) and day_ok


running_routines = set()


def run_routine(r):
    rid = r["id"]
    if rid in running_routines:
        return
    running_routines.add(rid)
    try:
        log(f"routine {rid} start: {r['name']}")
        prof = jarvis_profiles.worker_profile(r["name"], r["prompt"])
        system = ROUTINE_PROMPT + CLOUD_NOTE + "\n" + MEMORY_PROMPT + "\n" + SKILLS_PROMPT.format(index=skills_index())
        res = run_claude(time.strftime("[%a %d.%m.%Y %H:%M] ") + r["prompt"], prof["model"], prof["args"],
                         system, timeout=ROUTINE_TIMEOUT)
        if res["is_error"] or not res["result"]:
            why = res["error"] or "intet svar"
            if LIMIT_RE.search(why + res["result"]):
                try:
                    ans, model = sams_llm.ask(r["prompt"], kind="danish")
                    send(f"🔔 {r['name']} (Claude var ikke tilgængelig, svar fra {model.split('/')[-1]} uden adgang til dine ting)\n\n{ans}")
                    return
                except sams_llm.NoModel:
                    pass
            send(f"🔔 Rutinen \"{r['name']}\" fejlede ({why[:80]}).")
        elif res["result"].strip().upper() != "NOTHING":
            send(f"🔔 {r['name']}\n\n{res['result']}")
        log(f"routine {rid} done")
    except Exception as e:
        log("routine error", rid, type(e).__name__, str(e)[:200])
    finally:
        running_routines.discard(rid)
        memory_snapshot(f"routine {r.get('name', rid)}")
        rs = load_json(ROUTINES, [])
        for x in rs:
            if x["id"] == rid:
                x["last_run"] = time.strftime("%Y-%m-%d %H:%M")
        save_json(ROUTINES, rs)


def scheduler():
    last_minute = None
    while not stop.wait(5):
        t = time.localtime()
        key = (t.tm_year, t.tm_yday, t.tm_hour, t.tm_min)
        if key == last_minute:
            continue
        last_minute = key
        # requests from `sams-routine run <id>`
        for f in SAMS.glob("run-*.req"):
            rid = f.stem[4:]
            f.unlink(missing_ok=True)
            for r in load_json(ROUTINES, []):
                if r["id"] == rid:
                    threading.Thread(target=run_routine, args=(r,), daemon=True).start()
        for r in load_json(ROUTINES, []):
            try:
                due = r.get("enabled", True) and cron_match(r["cron"], t)
            except (ValueError, KeyError):
                due = False
            if due:
                threading.Thread(target=run_routine, args=(r,), daemon=True).start()


def routines_text():
    rs = load_json(ROUTINES, [])
    if not rs:
        return "Ingen rutiner endnu. Skriv fx \"send mig en morgenbrief hver hverdag kl 7\"."
    return "\n".join(f"{r['id']}: {r['name']} ({r['cron']}){'' if r.get('enabled', True) else ' [slået fra]'}"
                     f" sidst: {r.get('last_run', 'aldrig')}" for r in rs)


def status_text():
    st = load_state()
    lines = [f"Samtale: {'i gang' if st.get('session') else 'ny'}",
             f"Kø: {work_q.qsize()} besked(er){', arbejder' if busy() else ''}",
             f"Rutiner: {len(load_json(ROUTINES, []))}, kører nu: {len(running_routines)}"]
    cj = sams_jobs.active_jobs()
    if cj:
        lines.append("Kodejobs: " + "; ".join(f"{j['title'][:30]} ({sams_jobs.LABEL[j['status']]}, {j['progress']}%)" for j in cj))
    try:
        tasks = json.loads((WORKDIR / "tasks/status.json").read_text())
        live = [t for t in tasks if t.get("state") in ("running", "queued")]
        if live:
            lines.append("Orb-jobs: " + "; ".join(f"#{t['id']} {t['title'][:40]} ({t['state']})" for t in live))
    except (OSError, ValueError):
        pass
    return "\n".join(lines)


def release_pid():
    """Remove the pid file only if it's ours (a newer bridge may have replaced it)."""
    try:
        if PIDFILE.read_text().strip() == str(os.getpid()):
            PIDFILE.unlink()
    except OSError:
        pass


def main():
    ensure_dirs()
    if transport() == "imessage":
        PIDFILE.write_text(str(os.getpid()))
        signal.signal(signal.SIGTERM, lambda *a: stop.set())
        log(f"bridge started (iMessage, owner set: {bool(owner())}, shared dir: {SHARED.is_dir()})")
        for target in (worker, scheduler):
            threading.Thread(target=target, daemon=True).start()
        try:
            poll_imessage()
        except KeyboardInterrupt:
            pass
        finally:
            stop.set()
            release_pid()
            log("bridge stopped")
        return
    if MODE in ("siri", "helper"):   # endpoint only; Telegram polling + routines run elsewhere
        signal.signal(signal.SIGTERM, lambda *a: stop.set())
        PIDFILE.write_text(str(os.getpid()))   # sams-approve checks that a bridge runs
        log(f"bridge started ({MODE} mode)")
        threading.Thread(target=worker, daemon=True).start()
        threading.Thread(target=siri_server, daemon=True).start()
        try:
            stop.wait()
        except KeyboardInterrupt:
            pass
        release_pid()
        log("bridge stopped")
        return
    if not secret("telegram_token"):
        log("no telegram token yet; waiting for ~/.sams/telegram_token")
        while not secret("telegram_token"):
            time.sleep(30)
    PIDFILE.write_text(str(os.getpid()))
    if not chat_id() and not secret("pair_code"):
        import secrets as _s
        p = SAMS / "pair_code"
        p.write_text(f"{_s.randbelow(900000) + 100000}"); os.chmod(p, 0o600)
    signal.signal(signal.SIGTERM, lambda *a: stop.set())
    try:
        me = tg("getMe")
        log(f"bridge started as @{me.get('username')} (paired: {bool(chat_id())})")
    except TelegramError as e:
        log("getMe failed:", e)
    for target in (worker, scheduler, siri_server):
        threading.Thread(target=target, daemon=True).start()
    try:
        poll()
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
        release_pid()
        log("bridge stopped")


if __name__ == "__main__":
    main()
