#!/usr/bin/env python3
"""Check this template before a commit: skills, templates, links, public-safety terms, JSON and Python syntax.

  python3 scripts/check-template.py

No dependencies. Exits 1 with a list of problems.
"""
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", "node_modules", ".venv", "__pycache__"}
errors = []
try:   # files git ignores (keys, local notes) are not published
    out = subprocess.run(["git", "ls-files", "--others", "--ignored", "--exclude-standard"], cwd=ROOT, capture_output=True, text=True).stdout
    IGNORED = {ROOT / line for line in out.splitlines()}
except OSError:
    IGNORED = set()


def files(pattern="*"):
    for p in ROOT.rglob(pattern):
        rel = p.relative_to(ROOT).parts
        if p.is_file() and p not in IGNORED and not SKIP.intersection(rel) and rel[0] not in (".claude", ".agents"):
            yield p


def need(ok, msg):
    if not ok:
        errors.append(msg)


# skills and their catalog
catalog = json.loads((ROOT / "skills/catalog.json").read_text())["skills"]
names = [s["name"] for s in catalog]
need(len(names) == len(set(names)), "duplicate skill names in skills/catalog.json")
actual = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
need(set(names) == actual, f"catalog and skills differ: {sorted(set(names) ^ actual)}")
for s in catalog:
    path = ROOT / s["path"]
    if not path.exists():
        errors.append(f"missing skill file {s['path']}")
        continue
    fm = re.match(r"\A---\n(.*?)\n---\n", path.read_text(), re.S)
    need(fm is not None, f"no frontmatter in {s['path']}")
    if fm:
        for key in ("name", "description"):
            m = re.search(rf"^{key}: (.+)$", fm[1], re.M)
            val = m[1].strip().strip('"') if m else None
            need(val == s[key], f"catalog {key} differs from {s['path']}")
            # unquoted YAML breaks on ": " or " #" inside a value
            need(val is not None and ": " not in val and " #" not in val, f"{s['path']}: {key} needs quoting (contains ': ' or ' #')")
        need(s["name"] == path.parent.name, f"{s['path']}: name must match its folder")
for alias in (".agents/skills", ".claude/skills"):
    need((ROOT / alias).is_symlink() and (ROOT / alias).resolve() == ROOT / "skills", f"{alias} must link to skills/")
need((ROOT / "AGENTS.md").read_text() == (ROOT / "CLAUDE.md").read_text(), "AGENTS.md and CLAUDE.md differ")

# templates the skills point at
for t in ("comparison-brief.md", "guide-brief.md", "STRATEGY.md", "goal.json", "experiments.json"):
    need((ROOT / "templates" / t).exists(), f"missing templates/{t}")
goal = json.loads((ROOT / "templates/goal.json").read_text())
want = {"ai_answers_naming_us", "nonbrand_clicks", "nonbrand_impressions", "bing_impressions", "keywords_in_top_10", "money_pages_indexed"}
ids = {m["id"] for m in goal["metrics"]}
need(ids == want, f"templates/goal.json metrics differ: {sorted(ids ^ want)}")
for m in goal["metrics"]:
    need(all(k in m for k in ("baseline", "baselineDate", "target", "targetDate")), f"templates/goal.json: {m['id']} needs baseline, baselineDate, target, targetDate")
exps = json.loads((ROOT / "templates/experiments.json").read_text())
need(isinstance(exps, list) and all(e.get("example") is True for e in exps), "templates/experiments.json: a list whose entries are all marked example")

# relative links in markdown resolve inside the repo
for md in files("*.md"):
    text = re.sub(r"^\s*```.*?^\s*```", "", md.read_text(), flags=re.M | re.S)
    for target in re.findall(r"\]\(([^\s)]+)\)", text):
        u = urlsplit(target)
        if u.scheme or u.netloc or not u.path:
            continue
        dest = (md.parent / unquote(u.path)).resolve()
        need(dest.exists() and dest.is_relative_to(ROOT), f"broken link in {md.relative_to(ROOT)}: {target}")
    # a bare <word> outside code renders as an empty HTML tag on GitHub
    prose = re.sub(r"`[^`\n]*`", "", text)
    for tag in re.findall(r"(?<![\w`])<([a-z][\w .-]*)>", prose):
        if tag.split()[0] not in {"br", "img", "details", "summary", "sub", "sup", "kbd", "b", "i", "a", "p"}:
            errors.append(f"{md.relative_to(ROOT)}: <{tag}> outside code renders as an empty tag; wrap it in backticks")

# public safety: no private names, paths, secrets or em dashes in text files
TEXT = {".md", ".py", ".mjs", ".js", ".json", ".html", ".css", ".sh", ".yaml", ".yml", ".txt", ".svg"}
BANNED = [r"/Users/", r"/home/[a-z]", "\u2014"]   # machine paths and em dashes
PRIVATE = ROOT / "scripts/private-terms.txt"   # optional and git-ignored: 1 regex per line that must never ship
if PRIVATE.exists():
    BANNED += [line.strip() for line in PRIVATE.read_text().splitlines() if line.strip() and not line.startswith("#")]
SECRETS = [r"sk-[A-Za-z0-9]{20,}", r"ghp_[A-Za-z0-9]{30,}", r"github_pat_[A-Za-z0-9_]{30,}", r"AKIA[0-9A-Z]{16}",
           r"-----BEGIN [A-Z ]*PRIVATE KEY", r"xox[bp]-[A-Za-z0-9-]{20,}", r"AIza[0-9A-Za-z_-]{35}", r"\"private_key_id\"\s*:"]
for p in files():
    rel = p.relative_to(ROOT)
    if p.suffix not in TEXT or p == PRIVATE or p == Path(__file__).resolve():
        continue
    text = p.read_text(errors="ignore")
    for pat in BANNED:
        if re.search(pat, text, re.I):
            errors.append(f"{rel}: private or banned term /{pat}/")
    for pat in SECRETS:
        if re.search(pat, text):
            errors.append(f"{rel}: looks like a secret /{pat}/")

# JSON parses, Python compiles, nothing huge sneaks in
for p in files("*.json"):
    try:
        json.loads(p.read_text())
    except Exception as e:
        errors.append(f"{p.relative_to(ROOT)}: invalid JSON ({e})")
for p in files("*.py"):
    try:
        compile(p.read_text(), str(p), "exec")
    except SyntaxError as e:
        errors.append(f"{p.relative_to(ROOT)}: line {e.lineno}: {e.msg}")
for p in files():
    if p.stat().st_size > 5 * 1024 * 1024:
        errors.append(f"{p.relative_to(ROOT)} is {p.stat().st_size // 1024 // 1024} MB; keep large files out of the template")

if errors:
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print(f"template ok: {len(names)} skills, templates, links, public safety, JSON and Python checked"
      + ("" if PRIVATE.exists() else " (no scripts/private-terms.txt, so only the generic terms)"))
