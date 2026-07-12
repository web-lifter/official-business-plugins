---
name: competitor-bmc-shadow
description: Produce a shadow Business Model Canvas for a top competitor — what we infer about their nine cells. Writes 05-business-model/shadow-<competitor>-vN.md. Every cell tagged inferred.
argument-hint: <competitor-slug>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# competitor-bmc-shadow

Builds an inferred BMC for a competitor using the same nine-cell structure as `bmc-build` (Osterwalder & Pigneur, 2010), tagged `inferred` rather than `hypothesis`/`fact`. See `references.md`.

**Idempotency:** new versions are additive; re-running with `--version=N` overwrites that version only.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Verify the competitor has a SWOT (`04-competitors/swot/<slug>/README.md`).
   Halt if not — route to `/swot-build`.
3. Determine target version: existing
   `05-business-model/shadow-<slug>-v*.md` → max + 1, else 1.

## Phase 2: Infer the 9 cells

For the competitor:

1. **Customer Segments** — who they serve (from competitor table).
2. **Value Propositions** — pulled from their marketing pages.
3. **Channels** — how they reach customers (web, sales, partners).
4. **Customer Relationships** — self-serve / concierge / community.
5. **Revenue Streams** — from competitor table pricing.
6. **Key Resources** — inferred from product complexity, team size.
7. **Key Activities** — what they spend their effort on.
8. **Key Partnerships** — visible integrations and named partners.
9. **Cost Structure** — sketch only, marked "inferred."

Tag every entry as `inferred` (a third tag in addition to
`hypothesis` / `fact` for shadow BMCs).

## Phase 3: Write

Write `05-business-model/shadow-<slug>-vN.md`:

```markdown
---
title: Shadow BMC — <competitor> v<N>
slug: shadow-<slug>-v<N>
type: bmc
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Shadow BMC — <competitor name> v<N>

Tags: every cell entry is `inferred` unless otherwise noted.

Source SWOT: [<slug>](../04-competitors/swot/<slug>/README.md)
Source competitor row: [competitor-table.md](../04-competitors/competitor-table.md)

## Customer Segments
- ... [inferred]

(... 8 more cells ...)

## What it suggests for our BMC

- Cells where their model differs sharply from ours: ...
- Cells where their model is similar: ...
- Implications for our hypotheses: ...
```

## Phase 4: Log

Append: `## [<today>] shadow-bmc | <slug> v<N>`.

## Important principles

- **Inferred, not factual.** Every cell tagged inferred unless we
  have hard evidence (annual report, official disclosure).
- **Hand off to insights.** The "What it suggests" section feeds
  `/competitor-insights`.
- **Don't pretend to know costs.** Cost structure is a sketch; flag
  the unknowns.

## Edge cases

1. Competitor is privately held with little public info — sparse
   shadow; flag what's unknown.
2. Open-source competitor — Cost Structure may be community-funded;
   surface as a different model.
