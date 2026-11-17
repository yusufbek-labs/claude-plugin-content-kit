"""Static checks: every .json parses, every .md with frontmatter has a well-formed block,
required fields are present, and manifest paths resolve. Usage: python check.py"""
import json, re, sys
from pathlib import Path

root = Path(__file__).parent
errors = []
for p in root.rglob("*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
        print("json ok ", p.relative_to(root))
    except Exception as e:
        errors.append(f"{p}: {e}")

need = {"skills": ["name", "description"], "agents": ["name", "description"], "commands": ["description"]}
for p in (root / "plugins/content-kit").rglob("*.md"):
    kind = p.relative_to(root / "plugins/content-kit").parts[0]
    if kind not in need:
        continue
    if p.name != "SKILL.md" and kind == "skills":
        continue
    t = p.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m:
        errors.append(f"{p}: missing/malformed frontmatter")
        continue
    keys = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if not mm:
            errors.append(f"{p}: bad frontmatter line {line!r}")
        else:
            keys[mm.group(1)] = mm.group(2)
    for k in need[kind]:
        if not keys.get(k):
            errors.append(f"{p}: missing {k}")
    if kind == "skills":
        if keys.get("name") != p.parent.name:
            errors.append(f"{p}: name != folder")
        if len(keys.get("description", "")) > 1536:
            errors.append(f"{p}: description too long")
        if t.count("\n") > 500:
            errors.append(f"{p}: >500 lines")
    print("front ok", p.relative_to(root))

mk = json.loads((root / ".claude-plugin/marketplace.json").read_text())
for e in mk["plugins"]:
    d = root / e["source"]
    pj = json.loads((d / ".claude-plugin/plugin.json").read_text())
    if pj["name"] != e["name"] or not d.is_dir():
        errors.append("marketplace entry/plugin mismatch")
    if re.match(r"(claude|anthropic)", pj["name"]):
        errors.append("reserved plugin name")
print("\nFAILED:" if errors else "\nALL CHECKS PASSED")
for e in errors:
    print(" -", e)
sys.exit(1 if errors else 0)
