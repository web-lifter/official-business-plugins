---
name: mvp-metrics
description: Define the success metrics per hypothesis the MVP tests. No hypothesis without a metric, no metric without a threshold, no threshold without a timeframe. Writes 09-mvp/mvp-metrics.md.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# mvp-metrics

Method: Lean Startup validated-learning discipline — metric / threshold / timeframe triple. See `startups/SOURCES.md` (Ries 2011; Maurya 2022) and `references.md` for the binding rule.

Idempotency: safe to re-run; rewrites `09-mvp/mvp-metrics.md` in place. Append-only history lives in `.memex/log.md`.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read `09-mvp/mvp-spec.md` — primary hypothesis + MVP type.
3. Read hypothesis register; pull the primary hypothesis row and any
   secondary hypotheses the MVP would also touch.

## Phase 2: Define metrics

For each hypothesis the MVP tests, define:

- **Metric** (the event / measure)
- **Threshold** (the line)
- **Timeframe** (when we decide)
- **Source** (where the data comes from)

If the hypothesis already has these on its register row, copy them.
Otherwise, prompt the user via `AskUserQuestion` and update the
register simultaneously.

The rule: **no hypothesis without a metric, no metric without a
threshold, no threshold without a timeframe.**

## Phase 3: Add MVP-type-specific metrics

Each MVP type has standard accompanying metrics:

| MVP type | Standard metrics |
|---|---|
| Pre-order | Payment count; refund rate; support contact rate |
| Audience-building | Subscribe rate; open rate; click rate; unsubscribe rate |
| Show-and-tell | Demo views; sign-up rate; demo-to-trial rate |
| Partial product | Activation rate; weekly retention; NPS / qualitative feedback |

Add the relevant standard metrics with venture-specific thresholds.

## Phase 4: Write

Write `09-mvp/mvp-metrics.md`:

```markdown
---
title: MVP metrics
slug: mvp-metrics
type: mvp-spec
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# MVP metrics

MVP type: <type>
MVP spec: [mvp-spec](mvp-spec.md)

## Hypothesis-driven metrics

| Hypothesis | Metric | Threshold | Timeframe | Source |
|---|---|---|---|---|
| H-NN | <event> | <line> | <window> | <where> |

## MVP-type metrics

| Metric | Threshold | Timeframe | Source |

## Decision rules

When timeframe ends:

- All hypothesis metrics ≥ threshold → MVP succeeded; proceed to
  scale (and the next phase of customer development).
- Any hypothesis metric < threshold → MVP refuted on that hypothesis;
  build a learning card and decide pivot vs refine.

## Hand-off

Next: `mvp-analytics-plan` translates these metrics into events to
instrument.
```

## Phase 5: Log

Append: `## [<today>] mvp-metrics | defined`.

## Important principles

- **Triple rule: metric / threshold / timeframe.** No exceptions.
- **Metrics live with hypotheses.** Each metric ties to a hypothesis
  ID.
- **Decision rules are pre-set.** No "we'll see when the data comes
  in." The rule is set at design time.
- **Hands off to analytics planning.** This skill defines what to
  measure; the next plugin defines how.
