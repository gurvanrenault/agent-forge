"""Validate agent frontmatter and skill packages. Exits non-zero on any error."""

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED_KEYS = ("name", "description", "tools", "model")
MODELS = {"haiku", "sonnet", "opus", "inherit"}
TOOLS = {
    "Agent", "Bash", "Edit", "Glob", "Grep", "LS", "MultiEdit", "NotebookEdit",
    "NotebookRead", "PowerShell", "Read", "Skill", "Task", "TodoWrite",
    "WebFetch", "WebSearch", "Write",
}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        key, sep, value = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fields[key.strip()] = value.strip()
    return None


def check_agent(path, readme):
    errors = []
    fields = parse_frontmatter(path.read_text(encoding="utf-8"))
    if fields is None:
        return ["missing or unterminated YAML frontmatter"]

    for key in REQUIRED_KEYS:
        if not fields.get(key):
            errors.append(f"missing `{key}`")

    name = fields.get("name", "")
    if name and not KEBAB.match(name):
        errors.append(f"`name` {name!r} is not kebab-case")
    if name and name != path.stem:
        errors.append(f"`name` {name!r} does not match filename {path.stem!r}")

    model = fields.get("model", "")
    if model and model not in MODELS and not model.startswith("claude-"):
        errors.append(f"unknown `model` {model!r}")

    for tool in filter(None, (t.strip() for t in fields.get("tools", "").split(","))):
        base = tool.split("(", 1)[0]
        if base not in TOOLS and not base.startswith("mcp__") and base != "*":
            errors.append(f"unknown tool {tool!r}")

    if f"agents/{path.name}" not in readme:
        errors.append("not listed in README.md")
    return errors


def check_skill(path):
    try:
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
    except zipfile.BadZipFile:
        return ["not a valid zip archive"]
    if not any(Path(n).name == "SKILL.md" for n in names):
        return ["archive has no SKILL.md"]
    return []


def main():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    failed = False
    checks = [(p, check_agent(p, readme)) for p in sorted((ROOT / "agents").glob("*.md"))]
    checks += [(p, check_skill(p)) for p in sorted((ROOT / "skills").glob("*.skill"))]

    for path, errors in checks:
        rel = path.relative_to(ROOT).as_posix()
        if errors:
            failed = True
            for error in errors:
                print(f"::error file={rel}::{error}")
        else:
            print(f"ok  {rel}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
