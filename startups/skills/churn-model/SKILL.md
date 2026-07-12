---
name: churn-model
description: Compute remaining-customers and average-duration tables for stated retention rates using `(1 − r)^n` and lifetime `1/(1 − r)`. Outputs sensitivity analysis for retention rates from 50% to 99%. Read-only on the funnel.
argument-hint: [optional: --rate=0.85]
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# churn-model

Methodology: compound-retention math `(1 − r)^n` and average lifetime `1/(1 − r)` (Reichheld, *The Loyalty Effect*, 1996). See `references.md`.

Idempotency: re-running overwrites `06-relationships-channels/churn-model.md` with the latest anchor rate.

## User Context

$ARGUMENTS

If `--rate` is given, anchor the sensitivity table around that rate.

## Phase 1: Read

1. Verify venture profile.
2. Read `funnel-model.md` for the retention stage rate if any.

## Phase 2: Generate sensitivity table

Compute remaining-customers as `(1 − churn-rate)^n` and average
lifetime as `1 / churn-rate` for `n` periods of 1, 3, 6, 12, 24.

| Period (months) | Retention rate per month | Remaining (cumulative) | Avg lifetime |
|---|---|---|---|
| 1 | 50% | 50.0% | 2 mo |
| 1 | 80% | 80.0% | 5 mo |
| 1 | 95% | 95.0% | 20 mo |
| 1 | 99% | 99.0% | 100 mo |

For each rate, also compute the implied annual retention.

## Phase 3: Compose interpretation

For the venture's anchor rate (from funnel-model or `--rate`):

- Average customer lifetime (in months)
- Remaining customers after 12 months
- Sensitivity: how much does lifetime change if rate moves ±5pp?
- Compare to industry benchmark if known

## Phase 4: Write

Write `06-relationships-channels/churn-model.md`:

```markdown
---
title: Churn model
slug: churn-model
type: funnel
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Churn model

Source funnel: [funnel-model.md](funnel-model.md)
Anchor monthly retention rate: <%>

## Sensitivity table

| Monthly retention | Annual retention | Avg lifetime (mo) |
|---|---|---|
| 50% | 0.0% | 2 |
| 60% | 0.6% | 2.5 |
| 70% | 1.4% | 3.3 |
| 80% | 6.9% | 5 |
| 85% | 14.2% | 6.7 |
| 90% | 28.2% | 10 |
| 95% | 54.0% | 20 |
| 97% | 69.4% | 33.3 |
| 99% | 88.6% | 100 |

## Interpretation

At our anchor of <%> monthly:

- Average customer lifetime: <X> months
- Cohort still here at 12 months: <%>
- ±5pp shifts lifetime by: <range>

## Implications for unit economics

- LTV at lifetime <X> months ≈ price × <X>
- CAC payback: lifetime > CAC payback months means recoverable; less
  means unsustainable
- Hand off to `business-economics/unit-economics` for the rigorous
  LTV/CAC.
```

## Phase 5: Log

Append: `## [<today>] churn-model | anchor <%>`.

## Important principles

- **Use the formula.** `(1 − r)^n` for remaining cohort share, `1/(1 − r)`
  for average lifetime.
- **Sensitivity, not point estimate.** A 5pp swing changes lifetime
  dramatically at high retention rates.
- **Surface ±5pp swings.** The user should see how fragile high-LTV
  assumptions are.
