"""Kode-jobs ("Code med Sams"): jobliste med fremdrift og prioriteret kø.

Lagres i ~/.sams/cloudjobs.json (liste; rækkefølgen i listen ER køen - øverst = vigtigst).
Ingen hemmeligheder her. Bruges af `sams-cloudjob` (CLI) og Telegram-visningen i sams_telegram.py.

Job: {id, title, project, status, progress (0-100), current, created, updated}
status: queued | running | blocked | done | failed
Køen styrer rækkefølgen: next_job() returnerer det øverste job der stadig er 'queued'.
"""
import fcntl, secrets, time
from contextlib import contextmanager

from sams_common import SAMS, load_json, save_json

JOBS = SAMS / "cloudjobs.json"
STATUSES = ("queued", "running", "blocked", "done", "failed")
ICON = {"queued": "⏳", "running": "🔧", "blocked": "✋", "done": "✅", "failed": "❌"}
LABEL = {"queued": "i kø", "running": "arbejder", "blocked": "venter på dig", "done": "færdig", "failed": "fejlet"}
ACTIVE = ("running", "blocked", "queued")   # visningsrækkefølge for status; køen styrer inden for gruppen


@contextmanager
def locked():
    SAMS.mkdir(mode=0o700, exist_ok=True)
    with open(SAMS / "cloudjobs.lock", "a") as lf:
        fcntl.flock(lf, fcntl.LOCK_EX)
        yield


def load():
    jobs = load_json(JOBS, [])
    return jobs if isinstance(jobs, list) else []


def _find(jobs, jid):
    hits = [j for j in jobs if j["id"] == jid or j["id"].startswith(jid)]
    if len(hits) != 1:
        raise KeyError(jid)
    return hits[0]


def add(title, project="", current="", top=False):
    with locked():
        jobs = load()
        job = {"id": secrets.token_hex(2), "title": title.strip(), "project": project.strip(), "status": "queued",
               "progress": 0, "current": current.strip(), "created": time.time(), "updated": time.time()}
        if top:
            jobs.insert(0, job)
        else:
            # nye jobs kommer efter de aktive, men før afsluttede
            at = next((i for i, j in enumerate(jobs) if j["status"] in ("done", "failed")), len(jobs))
            jobs.insert(at, job)
        save_json(JOBS, jobs)
        return job


def update(jid, status=None, progress=None, current=None, title=None, project=None):
    with locked():
        jobs = load()
        j = _find(jobs, jid)
        if status is not None:
            if status not in STATUSES:
                raise ValueError(f"status skal være en af {STATUSES}")
            j["status"] = status
            if status == "done":
                j["progress"] = 100
        if progress is not None:
            j["progress"] = max(0, min(100, int(progress)))
        for k, v in (("current", current), ("title", title), ("project", project)):
            if v is not None:
                j[k] = v
        j["updated"] = time.time()
        save_json(JOBS, jobs)
        return j


def move(jid, how):
    """how: up | down | top. Flytter ét trin blandt de aktive jobs (færdige blander sig ikke i køen)."""
    with locked():
        jobs = load()
        j = _find(jobs, jid)
        act = [x for x in jobs if x["status"] in ACTIVE]
        done = [x for x in jobs if x["status"] not in ACTIVE]
        i = act.index(j) if j in act else None
        if i is None:
            return j
        if how == "top":
            act.insert(0, act.pop(i))
        elif how == "up" and i > 0:
            act[i - 1], act[i] = act[i], act[i - 1]
        elif how == "down" and i < len(act) - 1:
            act[i + 1], act[i] = act[i], act[i + 1]
        save_json(JOBS, act + done)
        return j


def remove(jid):
    with locked():
        jobs = load()
        jobs.remove(_find(jobs, jid))
        save_json(JOBS, jobs)


def next_job():
    """Det job der skal laves først: øverst i køen med status 'queued' (None hvis ingen)."""
    return next((j for j in load() if j["status"] == "queued"), None)


def bar(p, n=10):
    k = round(n * p / 100)
    return "▓" * k + "░" * (n - k)


def active_jobs(jobs=None):
    return [j for j in (load() if jobs is None else jobs) if j["status"] in ACTIVE]


def view_text(max_done=3):
    jobs = load()
    act = active_jobs(jobs)
    done = sorted([j for j in jobs if j["status"] not in ACTIVE], key=lambda j: -j.get("updated", 0))[:max_done]
    if not jobs:
        return "💻 Code med Sams\n\nIngen kodejobs endnu."
    lines = ["💻 Code med Sams", ""]
    if act:
        lines.append("Kø (øverst = vigtigst, laves først):")
    for n, j in enumerate(act, 1):
        proj = f" · {j['project']}" if j.get("project") else ""
        lines.append(f"{n}. {ICON[j['status']]} {j['title']}{proj}")
        lines.append(f"   {LABEL[j['status']]} · {bar(j['progress'])} {j['progress']}%")
        if j.get("current"):
            lines.append(f"   ➜ {j['current']}")
    if not act:
        lines.append("Intet i kø.")
    if done:
        lines += ["", "Senest afsluttet:"] + [f"{ICON[j['status']]} {j['title']}" for j in done]
    return "\n".join(lines)


def view_keyboard():
    """Inline-knapper: for hvert aktivt job ⬆️ ⬇️ 🔝 plus en opdater-knap. callback_data 'cj:<id>:<handling>'."""
    rows = []
    act = active_jobs()
    for n, j in enumerate(act, 1):
        label = f"{n}. {j['title'][:14]}"
        rows.append([{"text": label, "callback_data": "cj:" + j["id"] + ":noop"},
                     {"text": "⬆️", "callback_data": f"cj:{j['id']}:up"},
                     {"text": "⬇️", "callback_data": f"cj:{j['id']}:down"},
                     {"text": "🔝", "callback_data": f"cj:{j['id']}:top"}])
    rows.append([{"text": "🔄 Opdater", "callback_data": "cj:-:refresh"}])
    return {"inline_keyboard": rows}
