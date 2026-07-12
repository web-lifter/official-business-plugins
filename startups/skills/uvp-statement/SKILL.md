---
name: uvp-statement
description: Produce the standard UVP statement — "For [customer] who [need], our [product] is a [category] that [unique benefit]. Unlike [competitor], we [differentiator]."
argument-hint: [optional: --delegate-headline]
allowed-tools: Read Write Edit Glob Grep
effort: low
---

# uvp-statement

Composes a standard "for [customer] who [need]" UVP statement — the form popularised by Geoffrey Moore in *Crossing the Chasm* and reused as the "high-concept pitch" in lean-startup literature. See `references.md`.

**Idempotency:** re-running overwrites `04-competitors/uvp.md`; prior version remains in git.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read latest VPCs, latest BMC, segment profiles, competitor table.

## Phase 2: Compose

Use the standard template, filling each slot:

- **Target customer**: from primary segment label
- **Need**: from highest-priority pain
- **Product**: from BMC Value Propositions
- **Category**: existing market category (CRM, accounting tool, dating
  app, etc.)
- **Unique benefit**: from VPC pain reliever / gain creator
- **Competitor**: top competitor from `competitor-table.md`
- **Differentiator**: 1-2 things unique vs that competitor

If no competitors documented, refuse and route to
`/competitor-discover` first.

## Phase 3: Write

Write `04-competitors/uvp.md`:

```markdown
---
title: Unique Value Proposition
slug: uvp
type: vpc
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# UVP

> For **<target customer>** who **<need>**, our **<product>** is a
> **<category>** that **<unique benefit>**. Unlike **<competitor>**,
> we **<differentiator>**.

## Source

- Segment: [<slug>](../02-customer-discovery/segments/<slug>/README.md)
- VPC: [latest](../03-value-proposition/vpc-<segment>-vN.md)
- BMC: [latest](../05-business-model/bmc-vN.md)
- Top competitor: [<name>](../04-competitors/swot/<slug>/README.md)

## Variations

- Short (≤ 12 words): ...
- Headline (≤ 8 words): ...

## Headline polish

(If `--delegate-headline`, hand off to `brand-manager/website-copy`.)
```

## Phase 4: Log

Append: `## [<today>] uvp | written`.

## Important principles

- **Standard template.** Don't innovate the form.
- **Differentiator must be observable.** "Better UX" doesn't count.
- **Re-runnable.** Re-running overwrites; old version is in git.

## Edge cases

1. Multiple primary segments — produce one UVP per segment.
2. No competitor — refuse; route to `/competitor-discover`.
