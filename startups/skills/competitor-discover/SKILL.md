---
name: competitor-discover
description: Surface competitors across five sources — direct, indirect, substitutes, current workaround, do-nothing. Web-search required; cite every competitor with a URL.
argument-hint: [optional: --segment=<slug>]
allowed-tools: Read Write Edit Glob Grep WebSearch
effort: medium
---

# competitor-discover

Surfaces candidate competitors across the five-source taxonomy (direct, indirect, substitutes, customer workaround, do-nothing) commonly used in lean discovery. See `references.md`.

**Idempotency:** read-only on `competitor-table.md`; produces a candidate list for `/competitor-table-build` to canonicalise. Re-running re-discovers (useful when the segment definition changes).

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read primary segment profile, latest VPC, BMC value-propositions
   cell. These ground the search terms.

## Phase 2: Search the five sources

For each source category, generate 3-5 candidates:

1. **Direct competitors** — products solving the same problem for the
   same segment. Search by job-to-be-done; not by product name.
2. **Indirect competitors** — products solving a related problem in a
   way that overlaps.
3. **Substitutes** — different category but same outcome (a
   spreadsheet substitutes for accounting software).
4. **Customer's current workaround** — what they're doing now (per
   the segment's `early-adopters.md` "cobbled together a workaround").
5. **Do-nothing** — the cost of changing nothing. Often the largest
   competitor for early-stage ventures.

Use `WebSearch` for the first three categories; the latter two come
from venture state.

For each, capture:

- Name
- URL (from web search) or note ("no website — manual workaround")
- One-line description
- Source category
- Date discovered

## Phase 3: Write the discovery output

Write or append to `04-competitors/competitor-table.md` — but
`competitor-table-build` is the canonical writer. This skill produces
the candidate list.

Output to chat:

```markdown
# Competitor candidates — <segment>

## Direct
| Name | URL | Why it competes |

## Indirect
...

## Substitutes
...

## Current workaround
...

## Do-nothing
What the segment loses by not solving this. Quantify if possible.

## Next step

Run `/competitor-table-build` to canonicalise these into the table.
```

## Phase 4: Log

Append: `## [<today>] competitor-discover | <N> candidates surfaced`.

## Important principles

- **All five sources.** Skipping any is a known failure mode (e.g.
  forgetting do-nothing).
- **Cite sources.** Every web-found competitor has a URL.
- **Search by job, not product.** "Café reconciliation tool" not
  "QuickBooks alternative."
- **Read-only on competitor-table.** This skill surfaces; the next
  skill writes.

## Edge cases

1. Heavy do-nothing competition — flag prominently; many ventures
   underestimate "they're getting by."
2. Candidate appears in multiple categories — list once, tag both.
3. Web-search disabled — proceed with venture-state-only sources;
   flag the limitation.
