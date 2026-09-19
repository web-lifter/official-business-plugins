#!/usr/bin/env python3
"""Explicit, persistent virtualenv setup. Without --install this is a read-only check."""
from __future__ import annotations
import argparse
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parents[1]

def data_dir() -> Path:
    return Path(os.environ.get("PLUGIN_DATA") or os.environ.get("CLAUDE_PLUGIN_DATA")
                or os.environ.get("SEO_DATA_DIR") or Path.home() / ".claude/plugins/data/marketing")

def requirement_digest(path: Path, seen: set[Path] | None = None) -> bytes:
    seen = set() if seen is None else seen
    path = path.resolve()
    if path in seen:
        raise ValueError("cyclic requirements include")
    seen.add(path)
    content = path.read_bytes()
    parts = [content]
    for line in content.decode().splitlines():
        if line.strip().startswith("-r "):
            parts.append(requirement_digest(path.parent / line.strip()[3:].strip(), seen.copy()))
    return b"\0".join(parts)

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--install", action="store_true", help="Permit package downloads and environment changes")
    p.add_argument("--clustering-only", action="store_true")
    p.add_argument("--optional", action="store_true", help="Include large semantic/advanced clustering dependencies")
    a = p.parse_args(argv)
    if sys.version_info < (3, 11):
        p.error("Python 3.11 or later is required")
    req = ROOT / "requirements.txt"
    if a.clustering_only:
        req = ROOT / "skills/keyword-clustering-and-mapping/scripts/requirements.txt"
    reqs = [req]
    if a.optional:
        reqs.append(ROOT / "skills/keyword-clustering-and-mapping/scripts/requirements-optional.txt")
    fingerprint = hashlib.sha256(b"\0".join(requirement_digest(f) for f in reqs)
                                + str(sys.version_info[:2]).encode()).hexdigest()
    root = data_dir() / ("clustering-venv" if a.clustering_only else "venv")
    py = root / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    stamp = root / ".requirements-sha256"
    ready = py.is_file() and stamp.is_file() and stamp.read_text().strip() == fingerprint
    if ready:
        print(f"PYTHON={py}")
        return 0
    if not a.install:
        print("Environment absent or requirements changed. Review dependencies, then rerun with --install.", file=sys.stderr)
        return 1
    # Failed installs cannot leave a success stamp or a published interpreter pointer.
    root.parent.mkdir(parents=True, exist_ok=True)
    stamp.unlink(missing_ok=True)
    (data_dir() / "python_path.txt").unlink(missing_ok=True)
    if not py.exists():
        venv.EnvBuilder(with_pip=True).create(root)
    for requirement in reqs:
        subprocess.run([str(py), "-m", "pip", "install", "-r", str(requirement)], check=True)
    stamp.write_text(fingerprint + "\n")
    (data_dir() / "python_path.txt").write_text(str(py) + "\n")
    print(f"PYTHON={py}")
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Setup failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
