---
name: bmc-revenue-cost-sketch
description: Back-of-envelope pass at the BMC's Revenue Streams and Cost Structure using customer profile, channels, and pricing hypotheses. A sketch, not a financial model. Delegates to business-economics/unit-economics for the rigorous version.
argument-hint: [optional: --segment=<slug> for per-segment sketches]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# bmc-revenue-cost-sketch

A bracketed, range-only sketch of the BMC's Revenue Streams and Cost Structure cells. Intentionally pre-rigour; delegates to `business-economics/unit-economics` for the modelled version. See `references.md`.

**Idempotency:** re-running overwrites the sketch at the same version; cost-range deltas land in the changelog footer.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read the latest BMC, latest VPCs, channel strategy, hypothesis
   register (filter to revenue / cost / pricing hypotheses).
3. Read `04-competitors/competitor-table.md` if it exists — for
   benchmark pricing.

## Phase 2: Sketch revenue

For each segment / VPC pairing:

1. Pick a revenue model archetype from the menu in `reference.md` §1
   (subscription, transaction, usage-based, licence, freemium,
   marketplace fee, ad-supported, services, hybrid).
2. Sketch a price point — bracketed range, not a precise number. Cite
   competitor benchmarks if available.
3. Estimate willingness-to-pay (high / medium / low) based on the
   segment's pains and gains.

## Phase 3: Sketch costs

Group costs into:

- **Fixed**: people, infra baseline, licences
- **Variable**: per-customer COGS (compute, support, payments)
- **One-time**: build, launch, IP, legal

Use bracketed ranges. Mark each as `hypothesis` (default) since a
real model needs benchmarks the venture probably doesn't have yet.

## Phase 4: Write the sketch

Write `05-business-model/revenue-cost-sketch-vN.md` (where N matches
the BMC version):

```markdown
---
title: Revenue / cost sketch for BMC v<N>
slug: revenue-cost-sketch-v<N>
type: bmc
status: draft
owner: <venture name>
created: <today>
updated: <today>
---

# Revenue / cost sketch — BMC v<N>

This is a sketch, not a financial model. Brackets and labels, not
spreadsheets. Run `business-economics/unit-economics` for the rigorous
version once real numbers exist.

## Revenue

### Per segment

| Segment | Archetype | Price range | Willingness-to-pay | Confidence |
|---|---|---|---|---|

## Costs

### Fixed (per month)
- ...

### Variable (per customer)
- ...

### One-time
- ...

## Hypotheses surfaced

- H-NN: <derived from a price-range or willingness-to-pay assumption>
```

## Phase 5: Log

Append: `## [<today>] revenue-cost-sketch | v<N> sketched`.

## Important principles

- **Sketch, not spreadsheet.** Brackets only. Force the user to
  confront the unknowns.
- **Every assumption is a hypothesis.** Surface them for the register.
- **Delegate to unit-economics for rigour.** This skill is intentional
  about its limits.

## Edge cases

1. No competitor pricing data — sketch with two-decade brackets ($0-100,
   $100-1k, $1k-10k); flag the absence.
2. Marketplace / multi-sided model — produce one section per side.
