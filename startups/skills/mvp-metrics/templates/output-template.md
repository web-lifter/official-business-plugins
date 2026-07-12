---
title: MVP metrics
slug: mvp-metrics
type: mvp-spec
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# MVP metrics

**MVP type:** {{pre-order | audience-building | show-and-tell | partial product}}
**MVP spec:** [mvp-spec](mvp-spec.md)

## Hypothesis-driven metrics

| Hypothesis | Metric | Threshold | Timeframe | Source |
|-----------|--------|-----------|-----------|--------|
| {{H-NN}} | {{event/measure}} | {{≥/≤ value}} | {{window}} | {{where}} |

## MVP-type-standard metrics

| Metric | Threshold | Timeframe | Source |
|--------|-----------|-----------|--------|
| {{name}} | {{value}} | {{window}} | {{where}} |

## Decision rules

At end of timeframe:
- All hypothesis metrics ≥ threshold → MVP succeeded; proceed to scale.
- Any hypothesis metric < threshold → MVP refuted on that hypothesis; build learning card; decide pivot vs refine.

## Hand-off

Next: `/mvp-analytics-plan` translates these metrics into events to instrument.
