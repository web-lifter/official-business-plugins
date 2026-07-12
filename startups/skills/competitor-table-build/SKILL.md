---
name: competitor-table-build
description: Populate the canonical competitor table — name, category, segments served, pricing, features, source URL, verified date. One table per venture.
argument-hint: [optional: --add=<name>]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# competitor-table-build

Canonicalises competitor candidates (typically from `/competitor-discover`) into the single per-venture competitor table at `04-competitors/competitor-table.md`.

**Idempotency:** new rows are appended; existing rows are re-verified when `--refresh` is passed. Same input produces the same table.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read existing `04-competitors/competitor-table.md` if any.
3. Read `competitor-discover` output from chat history if running in
   sequence; otherwise prompt for candidates.

## Phase 2: Build / extend the table

For each new competitor, capture:

- Name
- URL
- Category (direct / indirect / substitute / workaround / do-nothing)
- Primary segment served
- Pricing model + price range (if public)
- Top 3 features
- Strengths (1-2)
- Weaknesses we observe (1-2)
- Source (URL from discovery)
- Last verified (date)

Use `WebFetch` to validate pricing and features when URLs are
provided.

## Phase 3: Write

Write `04-competitors/competitor-table.md`:

```markdown
---
title: Competitor table
slug: competitor-table
type: competitor
status: active
owner: <venture name>
created: <date of first creation>
updated: <today>
---

# Competitor table

| Name | Category | Segment | Pricing | Top features | Strengths | Weaknesses | Source | Verified |
|---|---|---|---|---|---|---|---|---|
| <name> | direct | café | AUD $49/mo | recon, reports | brand | UX clunky | <url> | 2026-05-05 |

## Notes

- Top 3 to target with full SWOT: <names>
- Workaround dominance: <what segments still use spreadsheets / paper>
- Do-nothing severity: <one sentence on cost of inaction>
```

## Phase 4: Recommendation

Output to chat: "Top 3 competitors to SWOT: <names>. Run
`/swot-build <name>` for each."

## Phase 5: Log

Append: `## [<today>] competitor-table | <N> rows`.

## Important principles

- **One canonical table.** Not per-segment; multi-segment ventures
  share one.
- **Verify dates.** Pricing and features change; the verified column
  surfaces stale rows.
- **Top 3 SWOT bar.** ≥ 3 competitors with full SWOTs is the
  customer-discovery-status implicit requirement.
- **Re-runnable.** New competitors are appended; existing rows are
  re-verified if `--refresh` is passed.

## Edge cases

1. Competitor refuses public pricing — note "private; estimated
   <range> from <source>."
2. Open-source / free competitors — pricing column shows "free /
   self-host," strengths often include "data ownership."
3. Indirect competitor that's bigger than the venture — note;
   competing for attention is real.
