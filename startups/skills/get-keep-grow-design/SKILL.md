---
name: get-keep-grow-design
description: Walk the three stages of customer relationships — Get (acquisition), Keep (retention), Grow (expansion). Each stage has its own metrics and investments. Writes 06-relationships-channels/get-keep-grow.md.
argument-hint: [optional: --segment=<slug>]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# get-keep-grow-design

Methodology: the Customer Relationships cell of the Business Model Canvas (Osterwalder & Pigneur, 2010), framed as the Get / Keep / Grow lifecycle. See `references.md`.

Idempotency: re-running overwrites `06-relationships-channels/get-keep-grow.md` with the latest hypotheses and metrics.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read latest BMC (especially Customer Relationships and Channels
   cells), latest VPCs, segment profiles.

## Phase 2: Walk the three stages

Use `AskUserQuestion` for each:

### Get

- **What activities** acquire customers? (content, ads, sales, PR,
  events, partnerships, virality)
- **What metrics** indicate Get is working? (e.g. signups, MQLs, paid
  conversions per channel)
- **What does it cost** per customer? Budget bracket.
- **What hypotheses** drive Get choices? Capture as `H-NN`s.

### Keep

- **What activities** retain customers? (onboarding, support,
  community, regular value updates)
- **What metrics** indicate Keep is working? (week-N retention, NPS,
  feature adoption, churn rate)
- **What's the churn target** for the venture economics?

### Grow

- **What activities** grow each customer? (cross-sell, upsell,
  referrals, plan expansions, additional seats)
- **What metrics** indicate Grow is working? (NRR, expansion MRR,
  referral rate)
- **What's the upsell hypothesis**?

## Phase 3: Write

Write `06-relationships-channels/get-keep-grow.md`:

```markdown
---
title: Get / Keep / Grow design
slug: get-keep-grow
type: channel
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Get / Keep / Grow

## Get

| Activity | Metric | Cost / customer | Driver hypothesis |

## Keep

| Activity | Metric | Target | Driver hypothesis |

## Grow

| Activity | Metric | Target | Driver hypothesis |

## Source

- BMC: [latest](../05-business-model/bmc-vN.md)
- VPCs: [...]
- Segment profile(s): [...]
```

## Phase 4: Log

Append: `## [<today>] get-keep-grow | designed`.

## Important principles

- **All three stages.** Skipping Grow because "we'll figure it out
  later" is a known failure mode.
- **Each stage has its own metrics.** Don't measure Get with
  retention metrics.
- **Hypotheses surface for the register.** Every assumption gets
  flagged.

## Edge cases

1. Venture is pre-revenue — Grow is mostly hypothetical; that's fine.
2. B2B with one-to-one Get — list named accounts as the "activity."
3. Marketplace / two-sided — produce two parallel sets, one per side.
