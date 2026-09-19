#!/usr/bin/env python3
"""Initialise or locate a venture workspace without requiring an external plugin."""
from __future__ import annotations
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys

PHASES = ("00-vision", "01-hypotheses", "02-customer-discovery", "03-value-proposition",
          "04-competitors", "05-business-model", "06-relationships-channels", "07-validation",
          "08-prototype", "09-mvp")

def slug(value: str) -> str:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise ValueError("venture slug must be lowercase letters/digits separated by single hyphens")
    return value

def _profile(path: Path) -> dict:
    data = json.loads(path.read_text())
    if not isinstance(data, dict) or data.get("profile") != "venture":
        raise ValueError(f"not a venture profile: {path}")
    return data

def resolve_workspace(project: Path, name: str | None = None) -> Path:
    project = project.resolve()
    if name:
        candidate = project / ".project/plans/startups" / slug(name)
        if candidate.is_dir():
            _profile(candidate / "venture.json")
            return candidate.resolve()
        raise ValueError(f"venture not initialised: {candidate}")
    if (project / "venture.json").is_file():
        _profile(project / "venture.json")
        return project
    legacy = project / "memex.config.json"
    if legacy.is_file():
        _profile(legacy)
        if not (project / ".memex").is_dir():
            raise ValueError("legacy venture config exists but .memex directory is missing")
        return (project / ".memex").resolve()
    if project.name == ".memex" and (project.parent / "memex.config.json").is_file():
        _profile(project.parent / "memex.config.json")
        return project
    candidates = sorted((project / ".project/plans/startups").glob("*/venture.json"))
    if len(candidates) != 1:
        raise ValueError("specify --venture when there are zero or multiple workspaces")
    _profile(candidates[0])
    return candidates[0].parent.resolve()

def initialise(project: Path, name: str) -> dict:
    name = slug(name)
    project = project.resolve()
    root = project / ".project/plans/startups" / name
    # Do not follow an existing symlink out of the user's project.
    if not root.resolve().is_relative_to(project):
        raise ValueError("workspace resolves outside the project")
    config = root / "venture.json"
    if root.exists() and any(root.iterdir()):
        if not config.is_file() or _profile(config).get("name") != name:
            raise ValueError("existing non-venture directory will not be overwritten")
    today = date.today().isoformat()
    docs = {
        "venture.json": json.dumps({"profile": "venture", "name": name, "schema_version": 1}, indent=2) + "\n",
        "index.md": "# " + name + "\n\n" + "\n".join(f"- [{d}]({d}/)" for d in PHASES) + "\n",
        "log.md": f"# Venture log\n\n## [{today}] init | venture {name} created\n",
        "00-vision/vision-sketch.md": "---\nstatus: draft\n---\n# Vision sketch\n\n## Customers' top problems\nTo be answered.\n\n## How our idea helps\nTo be answered.\n\n## Day-in-the-life: before vs after\nTo be answered.\n",
        "00-vision/day-in-life.md": "---\nstatus: draft\n---\n# Day in the life\n\n## Before\nTo be answered.\n\n## After\nTo be answered.\n",
        "01-hypotheses/hypothesis-register.md": "# Hypothesis register\n\n| ID | Cell | Statement | Falsifier | Metric | Direction | Threshold | Timeframe | Status | Updated |\n|---|---|---|---|---|---|---|---|---|---|\n",
    }
    root.mkdir(parents=True, exist_ok=True)
    # The profile is the recovery marker; create it before phase directories.
    if not config.exists():
        with config.open("x", encoding="utf-8") as f:
            f.write(docs["venture.json"])
        profile_created = True
    else:
        profile_created = False
    for d in (*PHASES, ".open-questions", "02-customer-discovery/segments"):
        destination = root / d
        if not destination.resolve().is_relative_to(root.resolve()):
            raise ValueError("workspace child resolves outside the venture")
        destination.mkdir(parents=True, exist_ok=True)
    created, preserved = (["venture.json"], []) if profile_created else ([], ["venture.json"])
    for rel, body in docs.items():
        if rel == "venture.json":
            continue
        path = root / rel
        if not path.resolve().is_relative_to(root.resolve()):
            raise ValueError("workspace file resolves outside the venture")
        try:
            with path.open("x", encoding="utf-8") as f:
                f.write(body)
            created.append(rel)
        except FileExistsError:
            preserved.append(rel)
    return {"workspace": str(root), "created": created, "preserved": preserved}

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("init", "resolve"))
    p.add_argument("--project", type=Path, default=Path.cwd())
    p.add_argument("--venture")
    a = p.parse_args()
    try:
        if a.action == "init":
            if not a.venture:
                p.error("init requires --venture")
            print(json.dumps(initialise(a.project, a.venture), indent=2))
        else:
            print(resolve_workspace(a.project, a.venture))
    except (OSError, ValueError) as exc:
        p.error(str(exc))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
