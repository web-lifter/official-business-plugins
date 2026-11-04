#!/usr/bin/env python3
"""Repository-specific static checks; not a substitute for live host import tests."""
from __future__ import annotations
import ast
import importlib.util
import json
from pathlib import Path
import re
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)$")

def mcp_errors(data: object) -> list[str]:
    if not isinstance(data, dict):
        return ["Claude .mcp.json must be an object"]
    unsupported = sorted(set(data) - {"mcpServers"})
    if unsupported:
        return ["Claude .mcp.json uses unsupported top-level fields: " + ", ".join(unsupported)]
    if not isinstance(data.get("mcpServers"), dict):
        return ["mcpServers must be an object"]
    return []

def check(root: Path = ROOT) -> list[str]:
    errors = []
    def fail(path, message):
        errors.append(f"{path}: {message}")
    catalogue = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    entries = catalogue.get("plugins")
    if not isinstance(entries, list) or not entries:
        return ["marketplace requires a non-empty plugin list"]
    names = set()
    for entry in entries:
        name, source = entry.get("name"), entry.get("source")
        if not name or name in names:
            fail("marketplace", "plugin names must be present and unique")
        names.add(name)
        if not isinstance(source, str) or not source.startswith("./"):
            fail(name, "source must be a ./-prefixed relative directory")
            continue
        directory = (root / source).resolve()
        if not directory.is_relative_to(root.resolve()):
            fail(name, "source escapes repository")
            continue
        try:
            m = json.loads((directory / ".claude-plugin/plugin.json").read_text())
        except (OSError, ValueError) as exc:
            fail(name, str(exc)); continue
        if m.get("name") != name or m.get("version") != entry.get("version"):
            fail(name, "name or version differs from marketplace")
        if not isinstance(m.get("version"), str) or not SEMVER.fullmatch(m["version"]):
            fail(name, "repository releases require MAJOR.MINOR.PATCH without leading zeros")
        for field in ("skills", "commands", "agents", "hooks", "mcpServers"):
            value = m.get(field)
            for rel in value if isinstance(value, list) else [value]:
                if rel is None or isinstance(rel, dict):
                    continue
                if not isinstance(rel, str) or not rel.startswith("./"):
                    fail(name, f"{field}: invalid relative path"); continue
                target = (directory / rel).resolve()
                if not target.is_relative_to(directory) or not target.exists():
                    fail(name, f"{field}: missing or escaping path {rel}")
                if field == "agents" and target.suffix != ".md":
                    fail(name, "agent paths must be individual Markdown files")
        skills = list((directory / "skills").glob("*/SKILL.md"))
        if not skills:
            fail(name, "no skills found")
        count_match = re.match(r"(\d+) (?:marketing )?skills", m.get("description", ""))
        if count_match and int(count_match[1]) != len(skills):
            fail(name, "manifest skill count is stale")
        for skill in skills:
            text = skill.read_text()
            try:
                if not text.startswith("---\n"):
                    raise ValueError("frontmatter must start on line 1")
                meta = yaml.safe_load(text.split("---", 2)[1])
                if not isinstance(meta, dict):
                    raise ValueError("frontmatter must be a mapping")
                for field in ("name", "description", "argument-hint", "effort"):
                    if not isinstance(meta.get(field), str) or not meta[field].strip():
                        fail(skill, f"{field} must be a non-empty string")
                if meta.get("name") != skill.parent.name:
                    fail(skill, "name differs from directory")
                if meta.get("effort") not in ("low", "medium", "high", "xhigh", "max"):
                    fail(skill, "invalid effort")
                if len(text.splitlines()) >= 500:
                    fail(skill, "entrypoint must stay under 500 lines")
                for required in ("LICENSE.txt", "templates/output-template.md", "examples/example-output.md", "agents/openai.yaml"):
                    if not (skill.parent / required).is_file():
                        fail(skill, f"missing {required}")
                for linked in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
                    # Check packaged support links; output-document links describe future user artefacts.
                    if linked.startswith(("http:", "https:", "#")) or any(c in linked for c in "{}<>"):
                        continue
                    if any(word in linked.lower() for word in ("reference", "runtime.md", "sources.md", "templates/", "examples/")):
                        target = (skill.parent / linked.split("#")[0]).resolve()
                        if not target.is_relative_to(directory) or not target.exists():
                            fail(skill, f"missing/escaping packaged support link: {linked}")
                for ref in re.findall(r"`(references?\.md)`", text):
                    if not (skill.parent / ref).is_file():
                        fail(skill, f"missing {ref}")
            except (ValueError, yaml.YAMLError, IndexError, TypeError) as exc:
                fail(skill, str(exc))
    for path in root.rglob("*"):
        if not path.is_file() or any(part in (".git", ".venv", "__pycache__", "node_modules") for part in path.parts):
            continue
        try:
            if path.suffix == ".json":
                data = json.loads(path.read_text())
                if path.name == ".mcp.json":
                    for message in mcp_errors(data): fail(path, message)
            elif path.suffix in (".yaml", ".yml"):
                yaml.safe_load(path.read_text())
            elif path.suffix == ".py":
                ast.parse(path.read_text(), filename=str(path))
            if path.name.startswith("requirements") and path.suffix == ".txt" and "file:///" in path.read_text():
                fail(path, "non-portable machine-local dependency")
        except (ValueError, SyntaxError, yaml.YAMLError) as exc:
            fail(path, str(exc))
    return errors

if __name__ == "__main__":
    try:
        errors = check()
    except (OSError, ValueError, KeyError) as exc:
        errors = [str(exc)]
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Static portability checks: {len(errors)} error(s)")
    raise SystemExit(bool(errors))
