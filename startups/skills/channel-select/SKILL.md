---
name: channel-select
description: Match the venture to direct vs indirect channels. Outputs a channel strategy ranking primary, secondary, and tertiary channels with rationale. Writes 06-relationships-channels/channel-strategy.md.
argument-hint: [optional: --segment=<slug>]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# channel-select

Methodology: Business Model Canvas channels cell (Osterwalder & Pigneur, 2010) plus the direct-vs-indirect heuristics from David Skok and Steve Blank. See `startups/SOURCES.md`.

Idempotency: re-running overwrites `06-relationships-channels/channel-strategy.md`; prior fit-report sections are preserved unless the primary channel changed.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read segment profiles (where do they spend time?), latest BMC
   (current channels cell), competitor table (where do competitors
   distribute?).

## Phase 2: Generate candidates

For each candidate channel:

- Classify as **direct** (we own the relationship — website, app,
  retail, sales) or **indirect** (a partner does — resellers,
  marketplaces, affiliates).
- Estimate **fit** with the segment (where they actually are).
- Estimate **economics** (CAC range, scaling cost).
- Note **dependency** (do we control it, or does a platform?).

## Phase 3: Rank

Pick **primary**, **secondary**, **tertiary** channels. Justify each
with:

- Why it fits the segment
- Why it fits the product (see `product-channel-fit-check`)
- What it costs to learn
- What it costs to scale

## Phase 4: Write

Write `06-relationships-channels/channel-strategy.md`:

```markdown
---
title: Channel strategy
slug: channel-strategy
type: channel
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Channel strategy

## Primary: <name>
- Type: direct|indirect
- Why segment fit: ...
- Why product fit: ...
- Cost to learn: ...
- Cost to scale: ...
- Driver hypothesis: H-NN

## Secondary: <name>
...

## Tertiary: <name>
...

## Channels we are NOT pursuing (and why)
- <name>: <why not>
- ...

## Source

- Segment(s): [...]
- BMC channels cell: [...]
- Competitor channel patterns: see [insights.md](../04-competitors/insights.md)
```

## Phase 5: Log

Append: `## [<today>] channel-strategy | primary <name>`.

## Important principles

- **Direct vs indirect explicit.** No fuzzy "online" — name the
  channel.
- **The "NOT pursuing" list is mandatory.** Forces explicit
  trade-offs.
- **Three channels max for early venture.** More than three usually
  means none get attention.
- **Run product-channel-fit-check after.** Coherence matters.

## Edge cases

1. Indirect-only candidates (e.g. only-retail products) — fine; flag
   the dependency risk.
2. Multi-sided platform — each side gets its own channel strategy.
3. Geographic split — separate channel strategies per geography if
   distribution is materially different.
