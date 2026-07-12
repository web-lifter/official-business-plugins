#!/usr/bin/env bash
# marketing SessionStart hook — bootstraps a local Python venv for the
# bundled scripts and SEO analysis libraries.
#
# Creates or updates ${CLAUDE_PLUGIN_ROOT}/.venv from requirements.txt. Tracks
# a requirements.stamp file to skip the pip install when nothing has changed.
# Never blocks: on pip failure we capture stderr to install.log and let the
# check-credentials hook surface the error to the user via systemMessage.

set -euo pipefail

PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT:-$(cd "$(dirname "$0")/../.." && pwd)}"
DATA_DIR="${CLAUDE_PLUGIN_DATA:-$HOME/.claude/plugins/data/marketing}"
VENV="$PLUGIN_ROOT/.venv"
REQ="$PLUGIN_ROOT/requirements.txt"
STAMP="$DATA_DIR/requirements.stamp"
LOG="$DATA_DIR/install.log"

mkdir -p "$DATA_DIR"

# Pick a Python interpreter — prefer python3 on POSIX, python on Windows.
PY="${SEO_PYTHON:-}"
if [ -z "$PY" ]; then
  if command -v python3 >/dev/null 2>&1; then
    PY=python3
  elif command -v python >/dev/null 2>&1; then
    PY=python
  else
    echo '{"systemMessage":"marketing: Python 3.11+ not found on PATH. Install it and restart Claude Code."}'
    exit 0
  fi
fi

# Version check — require 3.11+
if ! "$PY" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)' >/dev/null 2>&1; then
  PY_VERSION=$("$PY" -c 'import sys; print(".".join(map(str, sys.version_info[:3])))' 2>/dev/null || echo unknown)
  echo "{\"systemMessage\":\"marketing: Python $PY_VERSION found, but 3.11+ is required. SEO scripts will not run.\"}"
  exit 0
fi

# Create venv if it does not exist
if [ ! -d "$VENV" ]; then
  echo "marketing: creating venv at $VENV" >&2
  "$PY" -m venv "$VENV" >>"$LOG" 2>&1 || {
    echo "{\"systemMessage\":\"marketing: venv creation failed. See $LOG.\"}"
    exit 0
  }
fi

# Detect pip path inside the venv (Windows vs POSIX)
if [ -x "$VENV/bin/pip" ]; then
  PIP="$VENV/bin/pip"
  VPY="$VENV/bin/python"
elif [ -x "$VENV/Scripts/pip.exe" ]; then
  PIP="$VENV/Scripts/pip.exe"
  VPY="$VENV/Scripts/python.exe"
else
  echo "{\"systemMessage\":\"marketing: venv pip not found at expected paths inside $VENV.\"}"
  exit 0
fi

# Write interpreter path so other hooks and scripts can find it
echo "$VPY" > "$DATA_DIR/python_path.txt"

# Only re-run pip install if requirements.txt has changed
if ! diff -q "$REQ" "$STAMP" >/dev/null 2>&1; then
  echo "marketing: installing/updating requirements (requirements.txt changed)" >&2
  "$PIP" install --upgrade pip >>"$LOG" 2>&1 || true
  if ! "$PIP" install -r "$REQ" >>"$LOG" 2>&1; then
    echo "{\"systemMessage\":\"marketing: pip install failed. See $LOG for details.\"}"
    exit 0
  fi
  cp "$REQ" "$STAMP"
  echo "marketing: requirements installed successfully" >&2
fi

exit 0
