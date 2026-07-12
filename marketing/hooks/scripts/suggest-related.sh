#!/usr/bin/env bash
# marketing Stop hook — inspects the transcript tail for the last SEO skill
# invoked and suggests 2-3 sibling skills the user might want to run next.
# Emits a systemMessage JSON to stdout. Silent if no skill is detected.

set -euo pipefail

# Skill → suggested follow-on skills mapping
declare -A SUGGESTIONS
SUGGESTIONS["keyword-research"]="serp-analysis, keyword-list-developer"
SUGGESTIONS["keyword-list-developer"]="keyword-clustering-and-mapping"
SUGGESTIONS["keyword-clustering-and-mapping"]="content-brief-generator, internal-linking-planner, content-gap-analysis"
SUGGESTIONS["serp-analysis"]="competitor-seo-audit, content-brief-generator"
SUGGESTIONS["competitor-seo-audit"]="content-gap-analysis, backlink-audit"
SUGGESTIONS["on-page-audit"]="schema-markup-generator, internal-linking-planner"
SUGGESTIONS["technical-seo-audit"]="core-web-vitals-report, on-page-audit"
SUGGESTIONS["core-web-vitals-report"]="technical-seo-audit"
SUGGESTIONS["backlink-audit"]="competitor-seo-audit"
SUGGESTIONS["content-gap-analysis"]="content-brief-generator, keyword-clustering-and-mapping"
SUGGESTIONS["content-brief-generator"]="schema-markup-generator, internal-linking-planner"
SUGGESTIONS["internal-linking-planner"]="on-page-audit"
SUGGESTIONS["schema-markup-generator"]="on-page-audit"
SUGGESTIONS["gsc-performance-report"]="keyword-research, content-gap-analysis"
SUGGESTIONS["local-seo-audit"]="schema-markup-generator, on-page-audit"
SUGGESTIONS["redirect-map-builder"]="broken-link-scanner, technical-seo-audit"
SUGGESTIONS["broken-link-scanner"]="redirect-map-builder, internal-linking-planner"

# Read the transcript tail from CLAUDE_TRANSCRIPT_PATH if set, otherwise
# attempt to read from stdin (Claude Code may pipe it).
TRANSCRIPT_TAIL=""
if [ -n "${CLAUDE_TRANSCRIPT_PATH:-}" ] && [ -f "$CLAUDE_TRANSCRIPT_PATH" ]; then
  TRANSCRIPT_TAIL=$(tail -c 4096 "$CLAUDE_TRANSCRIPT_PATH" 2>/dev/null || true)
fi

# Fall back to CLAUDE_TRANSCRIPT if the path variant isn't available
if [ -z "$TRANSCRIPT_TAIL" ] && [ -n "${CLAUDE_TRANSCRIPT:-}" ]; then
  TRANSCRIPT_TAIL="${CLAUDE_TRANSCRIPT: -4096}"
fi

if [ -z "$TRANSCRIPT_TAIL" ]; then
  exit 0
fi

# Find the last skill name mentioned in the transcript (match /marketing:<skill>)
LAST_SKILL=""
for skill in "${!SUGGESTIONS[@]}"; do
  if echo "$TRANSCRIPT_TAIL" | grep -qiF "marketing:$skill"; then
    LAST_SKILL="$skill"
  fi
done

# Also detect bare skill invocations like "keyword-research" in the transcript
if [ -z "$LAST_SKILL" ]; then
  for skill in "${!SUGGESTIONS[@]}"; do
    if echo "$TRANSCRIPT_TAIL" | grep -qiF "$skill"; then
      LAST_SKILL="$skill"
      break
    fi
  done
fi

if [ -z "$LAST_SKILL" ]; then
  exit 0
fi

RELATED="${SUGGESTIONS[$LAST_SKILL]:-}"
if [ -z "$RELATED" ]; then
  exit 0
fi

# Format the suggestions into slash-command form
FORMATTED=$(echo "$RELATED" | tr ',' '\n' | while IFS= read -r s; do
  s="${s#"${s%%[![:space:]]*}"}"  # ltrim
  s="${s%"${s##*[![:space:]]}"}"  # rtrim
  [ -n "$s" ] && echo "  \`/marketing:$s\`"
done | paste -sd '' -)

# Build a clean, newline-formatted message
MSG="You just ran \`/marketing:$LAST_SKILL\`. You might also find these useful:\\n$(echo "$RELATED" | tr ',' '\n' | while IFS= read -r s; do s="${s#"${s%%[![:space:]]*}"}"; s="${s%"${s##*[![:space:]]}"}"; [ -n "$s" ] && echo "- /marketing:$s"; done | tr '\n' '|' | sed 's/|/\\n/g')"

printf '{"systemMessage":"%s"}\n' "$MSG"
exit 0
