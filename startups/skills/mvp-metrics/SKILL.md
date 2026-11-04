---
name: mvp-metrics
description: Define the success metrics per hypothesis the MVP tests. No hypothesis without a metric, no metric without a threshold, no threshold without a timeframe. Writes 09-mvp/mvp-metrics.md.
argument-hint: "[no args]"
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

## Runtime preflight

Read [the runtime guide](../../RUNTIME.md) before this workflow.


# mvp-metrics

Method: Lean Startup validated-learning discipline — metric / threshold / timeframe triple. See [Startups sources](../../SOURCES.md) (Ries 2011; Maurya 2022) and `references.md` for the binding rule.

Idempotency: safe to re-run; rewrites `09-mvp/mvp-metrics.md` in place. Append-only history lives in `log.md`.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Resolve the venture workspace as specified in `../../RUNTIME.md`.
2. Read `09-mvp/mvp-spec.md` — primary hypothesis + MVP type.
3. Read hypothesis register; pull the primary hypothesis row and any
   secondary hypotheses the MVP would also touch.

## Phase 2: Define metrics

For each hypothesis the MVP tests, define:

- **Metric** (the event / measure)
- **Threshold and direction** (minimum, maximum or interval)
- **Minimum usable sample and guardrails** (including an inconclusive outcome)
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

| Hypothesis | Metric | Direction | Threshold | Timeframe | Source | Minimum sample / guardrails |
|---|---|---|---|---|---|---|
| H-NN | <event> | <comparison> | <line> | <window> | <where> | <criteria> |

## MVP-type metrics

| Metric | Threshold | Timeframe | Source |

## Decision rules

When the timeframe ends:

- All pre-specified directional comparisons pass, the sample is sufficient and guardrails hold: evidence supports the tested hypothesis; assess generalisability before scaling.
- Missing or unreliable data, insufficient sample or mixed evidence: inconclusive; repair instrumentation or collect more evidence.
- A decision criterion fails with adequate evidence: record the result and decide whether to refine, retest or pivot. Do not claim every failed metric disproves the entire business model.

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
