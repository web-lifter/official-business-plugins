---
name: funnel-instrumentation-spec
description: Produce a concrete event/property spec from a funnel-model output. Translates Awareness → Sign-up → Activation → Conversion → Retention into named events with properties. Pairs with mvp-analytics-plan.
argument-hint: [no args]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# funnel-instrumentation-spec

Idempotency: side-effect-free planner; rewrites `09-mvp/analytics/funnel-instrumentation.md` in place.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `06-relationships-channels/funnel-model.md`. Halt if missing.
3. Read `09-mvp/analytics/events-spec.md` if it exists.

## Phase 2: Map stages to events

For each funnel stage, define the canonical event:

- Awareness → `page_viewed` with `route` property
- Sign-up → `user_signed_up`
- Activation → `<value-revealing-event>` (the specific first action
  that proves activation)
- Conversion → `payment_completed` or `commitment_made`
- Retention (week N) → `session_started` with cohort filter

For each:

- Required properties
- When it fires (client / server / both)
- Sample rate

## Phase 3: Compose threshold tracking

For each metric in `mvp-metrics.md`, write the analytics query that
would compute it:

```
funnel "Sign-up → Conversion"
  step 1: user_signed_up
  step 2: payment_completed (within 14 days)
threshold: ≥ 30%
```

## Phase 4: Write

Write `09-mvp/analytics/funnel-instrumentation.md`:

```markdown
---
title: Funnel instrumentation spec
slug: funnel-instrumentation
type: analytics-plan
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Funnel instrumentation spec

Source funnel: [funnel-model](../../06-relationships-channels/funnel-model.md)
Source metrics: [mvp-metrics](../mvp-metrics.md)

## Events per stage

| Stage | Event | When | Properties |
|---|---|---|---|

## Threshold queries

### Sign-up → Conversion (target ≥ 30%)
- Funnel: user_signed_up → payment_completed
- Window: 14 days
- Cohort filter: signup source

### Activation rate (target ≥ 50%)
- Funnel: user_signed_up → <activation event>
- Window: 7 days

(... more queries ...)

## Dashboards

- One dashboard per primary metric
- Hand-off: tool's dashboard config (PostHog insight JSON, etc.) lives
  in repo at `dashboards/`
```

## Phase 5: Log

Append: `## [<today>] funnel-instrumentation | <N> events; <M>
queries`.

## Important principles

- **Each stage has exactly one canonical event.** Multiple sources of
  "activation" make the funnel ambiguous.
- **Window matters.** "≥ 30% paid" means nothing without "within 14
  days."
- **Dashboards in repo.** Source-controlled config.
