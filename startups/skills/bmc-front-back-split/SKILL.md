---
name: bmc-front-back-split
description: Render the latest BMC into front-stage (right side — what the customer sees) and back-stage (left side — what the business does) views, so users can sequence work appropriately. Pure derivation — never modifies the source BMC.
argument-hint: [optional: --version=N]
allowed-tools: Read Write Glob
effort: low
---

# bmc-front-back-split

Renders the latest BMC into front-stage (right side, customer-facing) and back-stage (left side, business-facing) views — the distinction from Osterwalder & Pigneur (*Business Model Generation*, 2010). See `references.md`.

**Idempotency:** pure derivation; overwrites the derived file each run, never mutates the source BMC.

Front-stage (right side of the canvas): customer segments, value
propositions, channels, customer relationships, revenue streams.

Back-stage (left side): key activities, key resources, key partners,
cost structure.

## User Context

$ARGUMENTS

## Phase 1: Find the BMC

Find the latest BMC (highest `bmc-v*.md` version, in either
`05-business-model/` or `01-hypotheses/`).

## Phase 2: Derive the split

Read the BMC. Group its 9 sections:

- **Front-stage**: Customer Segments, Value Propositions, Channels,
  Customer Relationships, Revenue Streams
- **Back-stage**: Key Activities, Key Resources, Key Partnerships,
  Cost Structure

For each, list the entries verbatim, tag preserved.

## Phase 3: Write the derived file

Write `05-business-model/bmc-v<N>-front-back.md`:

```markdown
---
title: BMC v<N> front/back-stage view
slug: bmc-v<N>-front-back
type: bmc
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# BMC v<N> — front/back-stage

Source: [bmc-v<N>](bmc-v<N>.md)

## Front-stage (customer-facing)

### Customer Segments
<verbatim>

### Value Propositions
<verbatim>

### Channels
<verbatim>

### Customer Relationships
<verbatim>

### Revenue Streams
<verbatim>

## Back-stage (business-facing)

### Key Activities
<verbatim>

### Key Resources
<verbatim>

### Key Partnerships
<verbatim>

### Cost Structure
<verbatim>

## Sequencing recommendation

- Front-stage hypotheses tend to be cheaper to test (interviews,
  landing pages, fake-doors). Test these first.
- Back-stage hypotheses (cost, partners, key resources) often require
  internal investigation, supplier conversations, or unit-economics
  modelling. Schedule after front-stage signal exists.
```

## Phase 4: Log

Append: `## [<today>] bmc-front-back | v<N> derived`.

## Important principles

- **Pure derivation.** Never modifies the source BMC.
- **Re-runnable.** Always overwrites the derived file.
- **Recommendation is advisory.** The split lists which side each cell
  is on; the prioritisation note is generic guidance.

## Edge cases

1. No BMC exists — refuse; route to `/bmc-build`.
2. BMC has no entries in some cells — show empty headings; the user
   knows what's missing.
