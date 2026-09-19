#!/usr/bin/env python3
"""Compatibility entrypoint for explicit clustering setup; pass --install to download."""
from pathlib import Path
import runpy
import sys
if __name__ == "__main__":
    target = Path(__file__).resolve().parents[3] / "scripts/setup_environment.py"
    sys.argv = [str(target), "--clustering-only", *sys.argv[1:]]
    runpy.run_path(str(target), run_name="__main__")
