#!/usr/bin/env bash
# Lighthouse CLI wrapper for marketing.
#
# Runs Lighthouse for a given URL in headless Chrome mode, outputting JSON to
# stdout. Falls back with an error JSON if npx or lighthouse are unavailable.
#
# Usage:
#   bash lighthouse_runner.sh <url>
#   bash lighthouse_runner.sh <url> --strategy mobile
#   bash lighthouse_runner.sh https://example.com.au --strategy desktop

set -euo pipefail

URL="${1:-}"
STRATEGY="mobile"

if [ -z "$URL" ]; then
  echo '{"error":"Usage: lighthouse_runner.sh <url> [--strategy mobile|desktop]"}'
  exit 1
fi

# Parse optional --strategy flag
shift
while [[ $# -gt 0 ]]; do
  case "$1" in
    --strategy) STRATEGY="${2:-mobile}"; shift 2 ;;
    *) shift ;;
  esac
done

# Check npx is available
if ! command -v npx >/dev/null 2>&1; then
  echo '{"error":"npx not found. Install Node.js (https://nodejs.org/) then run: npm install -g lighthouse"}'
  exit 1
fi

# Check lighthouse is available via npx
if ! npx --yes lighthouse --version >/dev/null 2>&1; then
  echo '{"error":"Lighthouse not found. Install it with: npm install -g lighthouse"}'
  exit 1
fi

# Run Lighthouse — output JSON to stdout
npx lighthouse "$URL" \
  --output json \
  --output-path stdout \
  --strategy "$STRATEGY" \
  --chrome-flags="--headless --no-sandbox --disable-dev-shm-usage" \
  --quiet \
  2>/dev/null
