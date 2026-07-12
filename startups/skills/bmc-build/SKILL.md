---
name: bmc-build
description: Construct the initial Business Model Canvas from venture vision and customer-discovery state. Tags every cell as hypothesis or fact. Writes 05-business-model/bmc-vN.md (or 01-hypotheses/bmc-v1.md).
argument-hint: [optional: --version=N]
allowed-tools: Read Write Edit Glob Grep
effort: high
---

# bmc-build

Implements the nine-cell Business Model Canvas (Osterwalder & Pigneur, *Business Model Generation*, 2010) as a hypothesis sheet — every cell entry is tagged `hypothesis` or `fact`. See `references.md`.

**Idempotency:** re-running with the same version is a no-op; bumping the version requires `/bmc-update`.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Determine target version: existing `bmc-v*.md` files → max + 1, or
   1 if none. v1 lives in `01-hypotheses/`; v≥2 lives in
   `05-business-model/`.
3. Read venture state: vision, hypothesis register, segment profiles,
   latest VPCs, competitor table, channel strategy if any.

## Phase 2: Populate the 9 cells

For each cell, surface candidate content from the read files; let the
user confirm or edit each:

1. **Customer Segments** — segments with `status: active` from
   `02-customer-discovery/segments/`
2. **Value Propositions** — value maps from latest VPCs
3. **Channels** — from `06-relationships-channels/channel-strategy.md`
   if it exists; otherwise mark all `hypothesis`
4. **Customer Relationships** — from `get-keep-grow.md` if it exists
5. **Revenue Streams** — derived from hypothesis register +
   competitor pricing, or empty if nothing yet
6. **Key Resources** — what we need to deliver the value (people,
   tech, IP, capital)
7. **Key Activities** — the activities the business does to deliver
8. **Key Partnerships** — outside parties we depend on
9. **Cost Structure** — major fixed and variable costs

Tag each cell entry as `hypothesis` or `fact`. A cell entry is `fact`
only if a learning card with `status: accepted` evidence supports it;
otherwise it's `hypothesis`.

## Phase 3: Write the BMC

Path: `05-business-model/bmc-v<N>.md` (or `01-hypotheses/bmc-v1.md`
if N=1):

```markdown
---
title: Business Model Canvas v<N>
slug: bmc-v<N>
type: bmc
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Business Model Canvas v<N>

## Customer Segments
- <entry> [hypothesis|fact] — <evidence link if fact>

## Value Propositions
- ...

## Channels
- ...

## Customer Relationships
- ...

## Revenue Streams
- ...

## Key Resources
- ...

## Key Activities
- ...

## Key Partnerships
- ...

## Cost Structure
- ...

## Notes

- Hypotheses driving this version: <H-IDs>
- Predecessor: <link to bmc-v(N-1) if exists>
- Front/back-stage view: see `bmc-front-back-split` output
```

## Phase 4: Cross-link

For each `hypothesis`-tagged cell entry, ensure there's a matching row
in the hypothesis register (run `/hypothesis-register add` for any
that's missing).

## Phase 5: Log

Append: `## [<today>] bmc | v<N> built (<H-N> hypothesis | <F-N> fact)`.

## Important principles

- **Every cell is hypothesis or fact.** Default is hypothesis.
- **Facts need evidence.** Don't tag fact without a learning card.
- **v1 is honest.** v1 is allowed to be all hypotheses; that's the
  point.
- **Cross-link, don't duplicate.** Each cell entry references the
  source page; never restate the segment description, VPC content, etc.

## Edge cases

1. No segments yet — produce an aspirational v1 with all cells
   `hypothesis` and a note pointing to discovery.
2. Multiple segments — list all in Customer Segments; the BMC is a
   composite view.
3. v1 already exists — `bmc-build` refuses if v1 exists in
   `01-hypotheses/`; route to `/bmc-update`.
