"""Token diet for Sams: which model, MCP servers, tools and skills each `claude -p` process gets.

Measured 9.11.2026 (first API call of a fresh session, Haiku tokenizer): the default setup costs
~37.5k input tokens before a word is said (6 MCP servers, 73 skills, 2 plugins with hooks, all
built-in tools). Every MCP server/skill/plugin listing is paid again on every single call.

* FRONT (the voice chat): only the Gmail connector (calendar is osascript via Bash), a handful of
  built-in tools, no skills, no plugins.  -> ~15k.  Haiku by default, Sonnet for task-like
  requests, Opus only when he asks for it.
* WORKERS (10.11.2026): Sonnet for everything; Opus only when Samuel explicitly asks for it
  (`jarvis-task new --opus ...`). DaVinci, Resolve, Fusion and video jobs keep the FULL default
  toolset on Opus (davinci-resolve MCP, all skills incl. fusion-*, plugins). Other jobs get Gmail
  plus only the connectors and skills their title/instructions mention.
  Measured 9.11: Opus coding workers cost 4-15M input tokens each (100-175k contexts) and were
  the biggest orb spenders, which is why Opus is no longer chosen by keywords.
"""
import json, re

HAIKU = "claude-haiku-5-5"
SONNET = "claude-sonnet-5-5"
OPUS = "claude-opus-5-5"

# Every MCP server this Mac knows (user config + claude.ai connectors). Anything not explicitly
# allowed for a process is denied via the deniedMcpServers setting. Unknown servers added later are
# allowed (fail open) so nothing breaks silently.
LOCAL_SERVERS = ["davinci-resolve", "voicemode"]
CONNECTORS = {"gmail": "claude.ai Gmail", "figma": "claude.ai Figma",
              "trello": "claude.ai Trello", "docs": "claude.ai Claude Docs"}
# Plugins that add skills, agents and per-prompt hooks (the context-optimizer's prompt coach injects
# text into every message). Off for the front and for non-DaVinci workers.
PLUGINS = ["voicemode@voicemode", "claude-context-optimizer@synced"]


def _settings(allow):
    """--settings JSON that denies every known MCP server not in `allow` and disables the plugins."""
    deny = [s for s in LOCAL_SERVERS + list(CONNECTORS.values()) if s not in allow]
    return json.dumps({"enabledPlugins": {p: False for p in PLUGINS},
                       "deniedMcpServers": [{"serverName": s} for s in deny]})


# ---------- front ----------
# 11.11.2026 (Samuel: "flere værktøjer til stemmen"): skills on, Trello + Claude Docs connectors too.
FRONT_TOOLS = ["Bash", "Read", "Edit", "Write", "ToolSearch", "WebSearch", "WebFetch", "Skill"]
FRONT_ARGS = ["--settings", _settings({CONNECTORS["gmail"], CONNECTORS["trello"], CONNECTORS["docs"]}),
              "--tools", *FRONT_TOOLS]

# Task-like requests get Sonnet (better judgment for delegating/doing quick tool work); the real
# work itself is delegated to workers, so the front never needs Opus unless he asks.
FRONT_TASK_RE = re.compile(
    r"\b(make|build|create|write|draft|fix|edit|change|update|rename|move|organi[sz]e|plan|research|"
    r"analy[sz]e|compare|summari[sz]e|figure out|code|script|install|set up|setup|configure|debug|"
    r"davinci|resolve|timeline|render|fusion|fairlight|grade|invoice|spreadsheet|document|trello|figma|"
    r"reply|answer (him|her|them|the mail)|book|schedule|cancel)\b", re.I)
# Hard / high-stakes work gets Opus without being asked (Samuel 11.11.2026: "Opus når det er svært"),
# like Hermes' model-picker "high" tier: money, contracts, irreversible, security, deep research, complex code.
HARD_RE = re.compile(
    r"\b(architect\w*|complex|tricky|hard (bug|problem)|debug\w* .{0,40}(crash|race|deadlock|hang)|"
    r"contract\w*|kontrakt\w*|legal|juridisk\w*|tax|skat\w*|moms|vat|invoice dispute|negotiat\w*|forhandl\w*|"
    r"security|sikkerhed\w*|irreversible|deep research|grundig research|strateg\w*|business plan|"
    r"self-improv\w*|selvforbedring|improve (your|its) own)\b", re.I)
FRONT_OPUS_RE = re.compile(r"\b(think (hard|carefully|it through)|use opus|opus|your best|be smart)\b", re.I)


def pick_front_model(text, current, sticky):
    """(model, sticky): Opus only on request; Sonnet for task-like requests; else Haiku.
    A short follow-up ("yes, do it") stays on the bigger model for a couple of turns."""
    if FRONT_OPUS_RE.search(text) or HARD_RE.search(text):
        return OPUS, 2
    if FRONT_TASK_RE.search(text) or len(text.split()) > 100:
        return (OPUS, sticky) if current == OPUS and sticky > 0 else (SONNET, 2)
    if current != HAIKU and sticky > 0:
        return current, sticky - 1
    return HAIKU, 0


# ---------- workers ----------
DAVINCI_RE = re.compile(
    r"\b(davinci|resolve|fusion|fairlight|timeline|colou?r[- ]?grad\w*|grad(e|ing)|footage|clips?|render\w*|"
    r"luts?|nodes?|node-based|text\+|lower[- ]thirds?|titles? card|b-?roll|motion[- ]?graphics?|keyframes?|"
    r"video|edit(ing)? the (video|film|cut)|reels?|shorts|captions?|subtitles?|rotoscop\w*|sound ?design|"
    r"sfx|mix(ing)? the audio|dctl|macro|\.drp|\.setting)\b", re.I)
# Jobs about the orb's own code mention DaVinci/video words in passing ("keep Resolve jobs on the full
# profile"); they are only DaVinci jobs if the TITLE says so (the 10.11 token job wrongly got Opus+all).
ORB_CODE_RE = re.compile(r"\b(sams orb|jarvis orb|the orb|orb/|jarvis_\w+|jarvis-task|worker_profile|system_prompt)\b", re.I)
SKILL_RE = re.compile(
    r"\b(pdf|docx|word|excel|xlsx|spreadsheet|csv|powerpoint|pptx|slides?|presentation|deck|chart|graph|"
    r"dataviz|skills?|browser|chrome|website|web ?page|computer use|screen|settings\.json|hooks?|plugin|"
    r"claude code|claude api|figma|sam ?2|separate|isolate|cut out|morning brief|schedule[ds]? (task|agent)|"
    r"routine|cron|review)\b", re.I)
MCP_KEYWORDS = {
    "figma": re.compile(r"\b(figma|figjam|mock-?ups?|ui design)\b", re.I),
    "trello": re.compile(r"\btrello\b", re.I),
    "docs": re.compile(r"\b(claude docs?|docs?|document|report|write-?up|handbook|guide|notes doc)\b", re.I),
}
VOICE_RE = re.compile(r"\b(voicemode|voice mode)\b", re.I)


def is_davinci_job(title, instructions=""):
    """DaVinci/Resolve/Fusion/video job? Orb-code jobs only count if the title itself is about video."""
    if DAVINCI_RE.search(title):
        return True
    return bool(DAVINCI_RE.search(instructions)) and not ORB_CODE_RE.search(f"{title}\n{instructions}")


# Hard spend cap per worker process (claude -p --max-budget-usd, measured in API-equivalent dollars).
# Safety net only: WORKER_PROMPT asks code jobs to stop with QUESTION: well before this. Measured 10.11:
# Opus orb-code jobs cost ~$2.3-3.5 each, Sonnet ones ~$0.4-0.7. DaVinci jobs are never capped.
# Raised 11.11.2026 (Samuel: "større arbejdsbudget").
BUDGET_SONNET = 6.00
BUDGET_OPUS = 15.00


def is_orb_code_job(title, instructions=""):
    return bool(ORB_CODE_RE.search(f"{title}\n{instructions}"))


def worker_profile(title, instructions="", opus=False):
    """-> dict(model, args, kind) for a background worker, chosen from its title + instructions.
    opus: Samuel explicitly asked for Opus / the best model (jarvis-task new --opus)."""
    text = f"{title}\n{instructions}"
    if is_davinci_job(title, instructions):
        # FULL toolset: davinci-resolve MCP, fusion-* / davinci-* skills, plugins, everything (unchanged).
        return {"model": OPUS, "args": [], "kind": "davinci-full"}
    allow = {CONNECTORS["gmail"]}
    allow |= {CONNECTORS[k] for k, rx in MCP_KEYWORDS.items() if rx.search(text)}
    if VOICE_RE.search(text):
        allow.add("voicemode")
    args = ["--settings", _settings(allow)]
    if not SKILL_RE.search(text):
        args.append("--disable-slash-commands")
    opus = opus or bool(HARD_RE.search(text))
    model = OPUS if opus else SONNET
    args += ["--max-budget-usd", f"{BUDGET_OPUS if opus else BUDGET_SONNET:.2f}"]
    kind = "+".join(sorted(k for k, v in CONNECTORS.items() if v in allow))
    return {"model": model, "args": args, "kind": f"slim[{kind}{',skills' if '--disable-slash-commands' not in args else ''}]"}


# Tiny no-tools process for summarising a long mail outside the front's context (orb/mail-read).
SUMMARY_ARGS = ["--settings", _settings(set()), "--strict-mcp-config", "--disable-slash-commands",
                "--tools", "", "--no-session-persistence"]
