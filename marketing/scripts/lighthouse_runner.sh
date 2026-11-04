#!/usr/bin/env bash
# Explicit local Lighthouse execution; never install packages or disable Chrome sandboxing.
set -euo pipefail
fail() { printf '%s\n' '{"error":"Usage: lighthouse_runner.sh https://host [--strategy mobile|desktop]; requires an installed lighthouse executable"}'; exit 2; }
[ "$#" -ge 1 ] || fail
URL="$1"; shift
case "$URL" in http://*|https://*) ;; *) fail ;; esac
STRATEGY=mobile
while [ "$#" -gt 0 ]; do
  case "$1" in
    --strategy) [ "$#" -ge 2 ] || fail; STRATEGY="$2"; shift 2 ;;
    *) fail ;;
  esac
done
case "$STRATEGY" in mobile|desktop) ;; *) fail ;; esac
LH="${LIGHTHOUSE_BIN:-lighthouse}"
command -v "$LH" >/dev/null 2>&1 || fail
ARGS=("$URL" --output=json --output-path=stdout --chrome-flags=--headless --quiet)
if [ "$STRATEGY" = desktop ]; then ARGS+=(--preset=desktop); fi
exec "$LH" "${ARGS[@]}"
