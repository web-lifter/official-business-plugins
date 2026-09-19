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

## Sample and data quality

{{Minimum usable sample, cohort definition, missing-data handling and guardrails per metric.}}

## Decision rules

At the end of the timeframe, apply each metric's pre-specified direction (minimum, maximum or interval), sample requirement and guardrails. Report supported, not supported or inconclusive. Do not infer scale readiness from a pass, or refutation from missing data.

## Hand-off

Next: `/mvp-analytics-plan` translates these metrics into events to instrument.
