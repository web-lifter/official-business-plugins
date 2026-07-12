#!/usr/bin/env python3
"""Create/reuse a virtualenv for the clustering engine and install requirements.

The skill calls this once before the first run. It builds a venv at a stable
location (default: ``$CLAUDE_PLUGIN_DATA/keyword-clustering-and-mapping/.venv``,
falling back to ``<scripts>/.venv``) and installs ``requirements.txt`` into it.

Prints the path to the venv's Python on the last line so the skill can capture it:
    PYTHON=<...>
Subsequent runs reuse the venv (idempotent — pip is a no-op when satisfied).
"""

from __future__ import annotations

import os
import subprocess
import sys
import venv

_HERE = os.path.dirname(os.path.abspath(__file__))
_REQS = os.path.join(_HERE, "requirements.txt")


def _venv_root() -> str:
    data = os.environ.get("CLAUDE_PLUGIN_DATA") or os.environ.get("SEO_DATA_DIR")
    if data:
        return os.path.join(data, "keyword-clustering-and-mapping", ".venv")
    return os.path.join(_HERE, ".venv")


def _venv_python(root: str) -> str:
    if os.name == "nt":
        return os.path.join(root, "Scripts", "python.exe")
    return os.path.join(root, "bin", "python")


def main() -> int:
    root = _venv_root()
    py = _venv_python(root)
    if not os.path.exists(py):
        print(f"Creating venv at {root} …", file=sys.stderr)
        os.makedirs(os.path.dirname(root), exist_ok=True)
        venv.EnvBuilder(with_pip=True).create(root)
    print("Installing requirements (first run can take several minutes) …", file=sys.stderr)
    rc = subprocess.call([py, "-m", "pip", "install", "-q", "--upgrade", "pip"])
    rc |= subprocess.call([py, "-m", "pip", "install", "-q", "-r", _REQS])
    if rc != 0:
        print("ERROR: dependency install failed. See pip output above.", file=sys.stderr)
        return rc
    # NLTK data used by the preprocessing step (stem/lemmatize/stopwords).
    subprocess.call(
        [py, "-c", "import nltk; [nltk.download(p, quiet=True) for p in ('stopwords','wordnet','omw-1.4')]"]
    )
    print(f"PYTHON={py}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
