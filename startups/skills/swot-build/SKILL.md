---
name: swot-build
description: Generate a SWOT for a top competitor. Enforces the internal (S/W) vs external (O/T) distinction. Writes 04-competitors/swot/<competitor-slug>/README.md.
argument-hint: <competitor-slug-or-name>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# swot-build

Builds a four-quadrant SWOT for a competitor, enforcing the internal (Strengths / Weaknesses) vs external (Opportunities / Threats) distinction credited to Albert Humphrey's SRI work in the 1960s. See `references.md`.

**Idempotency:** re-runs refresh the SWOT; with `--archive`, the prior version is preserved as `README.md.archive-<date>`.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Look up the competitor in `competitor-table.md`. Halt if not
   present — route to `/competitor-table-build`.
3. Slugify the competitor name for the folder.

## Phase 2: Walk the four quadrants

Use `AskUserQuestion`:

1. **Strengths (internal)**: what does the competitor do well? Brand,
   product depth, distribution, talent, capital, IP, partnerships.
2. **Weaknesses (internal)**: where do they struggle? Slow product,
   bad UX, poor support, narrow focus, dependence on a partner.
3. **Opportunities (external)**: market trends or shifts they could
   exploit. Regulatory changes, new tech, demographic shifts, supply-
   chain shifts.
4. **Threats (external)**: market trends or shifts that work against
   them. Same list, opposite direction.

For each, validate the internal/external distinction. Reject items
that violate it (e.g. "great brand" listed as Opportunity — that's a
Strength).

## Phase 3: Compose insights

After the four quadrants, write a `## What it means for us` section:

- Which strengths can we not match? (Compete on something else.)
- Which weaknesses can we exploit? (Wedge.)
- Which opportunities should we move on before they do?
- Which threats apply to us too?

## Phase 4: Write

Write `04-competitors/swot/<slug>/README.md`:

```markdown
---
title: SWOT — <competitor name>
slug: swot-<slug>
type: swot
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# SWOT — <competitor name>

Source row: [competitor-table.md](../../competitor-table.md)
Last verified: <date>

## Strengths (internal)
- ...

## Weaknesses (internal)
- ...

## Opportunities (external)
- ...

## Threats (external)
- ...

## What it means for us

- Cannot match: ...
- Wedge: ...
- Move first: ...
- Shared threat: ...
```

## Phase 5: Log

Append: `## [<today>] swot | <slug> built`.

## Important principles

- **S/W internal; O/T external.** The skill rejects items that violate
  the distinction.
- **Insights are actionable.** Every "what it means" item should
  imply a hypothesis or action.
- **One folder per competitor.** Required by `readme-required` hook.
- **Re-runnable.** Refreshes the SWOT; archives prior to
  `<slug>/README.md.archive-<date>` if `--archive`.

## Edge cases

1. User confuses strength with opportunity — surface the rule, prompt
   to re-categorise.
2. Competitor in wind-down — Strengths and Opportunities will be
   sparse; that's a useful insight in itself.
