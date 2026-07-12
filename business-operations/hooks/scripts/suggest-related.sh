#!/usr/bin/env bash
# business-operations Stop hook — suggests related skills based on the most
# recent business-operations skill invoked in the current transcript. Non-blocking.

set -e

TRANSCRIPT="${CLAUDE_TRANSCRIPT:-}"
if [ -z "$TRANSCRIPT" ] || [ ! -f "$TRANSCRIPT" ]; then
  exit 0
fi

DETECTED=""
# Ordered list — last match wins, so the most recently used skill is detected.
for skill in \
  revenue-channel-mapper \
  kpi-framework-generator \
  stakeholder-brief-builder \
  operational-bottleneck-detector \
  pricing-strategy-analyser
do
  if tail -200 "$TRANSCRIPT" 2>/dev/null | grep -q "business-operations:$skill"; then
    DETECTED="$skill"
  fi
done

if [ -z "$DETECTED" ]; then
  exit 0
fi

case "$DETECTED" in
  revenue-channel-mapper)
    NEXT='Related skills: /business-operations:kpi-framework-generator to set metrics per channel, and /business-operations:pricing-strategy-analyser to optimise channel economics.' ;;
  kpi-framework-generator)
    NEXT='Related skills: /business-operations:revenue-channel-mapper to ground KPIs in channel data, and /business-operations:operational-bottleneck-detector to find what is limiting key metrics.' ;;
  stakeholder-brief-builder)
    NEXT='Related skill: /business-operations:kpi-framework-generator to add metric evidence to your brief.' ;;
  operational-bottleneck-detector)
    NEXT='Related skills: /business-operations:kpi-framework-generator to track constraint metrics, and /business-operations:stakeholder-brief-builder to communicate remediation plans.' ;;
  pricing-strategy-analyser)
    NEXT='Related skills: /business-operations:revenue-channel-mapper to validate pricing by channel, and /business-operations:kpi-framework-generator to track pricing KPIs.' ;;
  *)
    exit 0 ;;
esac

echo "{\"systemMessage\":\"$NEXT\"}"
exit 0
