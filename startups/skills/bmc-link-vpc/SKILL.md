---
name: bmc-link-vpc
description: Link each VPC to the segment + value-propositions cell of the latest BMC. Adds bidirectional links so the VPC and BMC stay in sync. Read-mostly — only adds links; never replaces cell content.
argument-hint: [optional: vpc-segment-slug to link only one]
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# bmc-link-vpc

Adds bidirectional links between the BMC's Customer Segments / Value Propositions cells and each segment's Value Proposition Canvas (Osterwalder, Pigneur, Bernarda & Smith, *Value Proposition Design*, 2014). See `references.md`.

**Idempotency:** additive only — re-running adds missing links and is a no-op when all are present.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Find the latest BMC and all latest VPCs (one per segment).

## Phase 2: For each VPC

For each VPC:

1. Confirm the segment exists in the BMC's Customer Segments cell.
   If missing, list it for the user to add via `/bmc-update` with a
   manual entry.
2. Confirm the VPC's left-side products & services map to entries in
   the BMC's Value Propositions cell. If missing, list them.
3. Add a `## BMC linkage` section to the VPC file listing the
   matching BMC version and cell rows.

## Phase 3: Update the BMC

Add a footnote/sub-bullet to each Customer Segments and Value
Propositions cell entry pointing to the relevant VPC file:

```markdown
- <segment label> [hypothesis|fact] — see [vpc-<segment>-vN](../03-value-proposition/vpc-<segment>-v<N>.md)
```

## Phase 4: Log

Append: `## [<today>] bmc-link-vpc | <N> VPCs linked`.

## Important principles

- **Additive only.** Never overwrite BMC cell content; only add
  pointers.
- **Bidirectional.** VPC links to BMC; BMC links to VPC.
- **Re-runnable.** Idempotent — re-running adds the same links if
  they're missing or no-op if they're present.

## Edge cases

1. Segment in VPC not in BMC — surface; don't auto-add to the BMC
   (requires `/bmc-update`).
2. VPC's products & services much richer than BMC's Value Propositions
   cell — flag; the BMC may be too coarse.
