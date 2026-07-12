---
name: funnel-model
description: Build a quantitative customer funnel — visitors → signups → activations → paid → retained — with per-step conversion rates and end-to-end yield. Hands off to mvp-planning/funnel-instrumentation-spec to translate stages into events.
argument-hint: [optional: --segment=<slug>]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# funnel-model

Methodology: Dave McClure's AARRR pirate-metrics funnel (Acquisition → Activation → Retention → Revenue → Referral) adapted to a 5-stage acquisition-to-retention flow. See `references.md`.

Idempotency: re-running overwrites `06-relationships-channels/funnel-model.md` with the latest stage definitions and rates.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `get-keep-grow.md` and `channel-strategy.md`.
3. Read competitor table for benchmark conversion rates if available.

## Phase 2: Sketch the funnel stages

Standard 5-stage funnel (adjust if the venture differs):

1. **Awareness** — reached impressions / visitors (top of funnel)
2. **Sign-up** — gave us their data
3. **Activation** — completed the value-revealing first action
4. **Conversion** — paid / committed
5. **Retention** — still using / paying after `n` periods

For each stage:

- Stage name
- Definition (what counts as "activated"? exact event)
- Hypothesised conversion rate from the prior stage
- Source for the rate (industry benchmark, competitor inference,
  guess)
- Hypothesis ID if testing a specific rate

## Phase 3: Compute end-to-end yield

End-to-end yield = product of stage conversion rates.

If yield is < 1% (typical floor for cheap channels) or > 30%
(suspiciously high), surface a warning.

## Phase 4: Write

Write `06-relationships-channels/funnel-model.md`:

```markdown
---
title: Funnel model
slug: funnel-model
type: funnel
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Funnel model

| Stage | Definition (event) | Rate from prior | Source | Hypothesis |
|---|---|---|---|---|
| Awareness | <impression / visit> | — | — | — |
| Sign-up | <event> | <%> | <source> | H-NN |
| Activation | <event> | <%> | <source> | H-NN |
| Conversion | <event> | <%> | <source> | H-NN |
| Retention (W4) | <event> | <%> | <source> | H-NN |

End-to-end yield: <%>

## Reality check

- Industry benchmark for primary channel: <yield>
- Our model is <better|worse|on-par> by <factor>
- Risk: <if better — over-optimistic; if worse — channel may not work>

## Hand-off

When the MVP is being built, run `mvp-planning/funnel-instrumentation-spec`
to translate these stages into concrete events to instrument.
```

## Phase 5: Log

Append: `## [<today>] funnel-model | yield <%>`.

## Important principles

- **Define every event.** "Activation" with no event is not measurable.
- **Cite every rate.** Guesses are flagged "guess"; benchmarks are
  cited with sources.
- **Reality-check the yield.** Too-good is suspicious; too-low is a
  channel-fit problem.
- **Hand off to MVP planning.** This skill produces the model; the
  MVP-planning plugin produces the events spec.
