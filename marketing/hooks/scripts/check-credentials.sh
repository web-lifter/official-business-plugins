#!/usr/bin/env bash
# marketing SessionStart hook — checks whether a credentials file exists and
# nudges the user to create one if not. Never blocks session startup. No vault,
# no passphrase: credentials live in a single plaintext JSON file.

set -euo pipefail

DATA_DIR="${CLAUDE_PLUGIN_DATA:-$HOME/.claude/plugins/data/marketing}"
CANONICAL="$HOME/.claude/plugins/data/marketing/credentials.json"

# Credentials may live in the plugin data dir, the canonical path, or be
# supplied entirely via environment variables — any of these is fine.
if [ -f "$DATA_DIR/credentials.json" ] || [ -f "$CANONICAL" ] \
  || [ -n "${SEO_CREDENTIALS_FILE:-}" ] || [ -n "${SERPAPI_KEY:-}" ]; then
  exit 0
fi

echo '{"systemMessage":"marketing: no credentials file found. Run `/marketing:seo-setup` to create one, then paste in your SerpAPI/DataForSEO/Ahrefs/Moz/PSI keys."}'
exit 0
