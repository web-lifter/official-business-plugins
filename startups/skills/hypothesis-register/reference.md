# hypothesis-register — reference

## §1. Falsifiability heuristic

A hypothesis is falsifiable if it answers all four:

1. **What** observation would refute it? (Falsifier)
2. **How** do we measure that? (Measurement)
3. **What's the line?** (Threshold)
4. **When do we decide?** (Timeframe)

Common failure modes — refuse and ask for sharpening:

| Pattern | Why it fails | Fix |
|---|---|---|
| "Users will love it" | No measurement, no threshold | Pick a behaviour: invites, retention, paid conversion |
| "We can build this in 3 months" | Not a customer-facing claim | Move to feasibility, not the register |
| "Most customers prefer X" | "Most" is vague | Specify: "≥ 60% of segment-A interviewees pick X over Y" |
| "It's a big market" | No falsifiable threshold | "≥ 100k matching businesses on the ABS register" |
| "If we charge $X they'll pay" | Missing threshold and timeframe | "≥ 60% of segment-A pre-orders at $X within 14 days" |

The full ruleset is in `claude-memex/templates/profiles/venture/.memex/.rules/hypothesis-rules.md`.

## §2. Why per-row status, not per-page

The register is a single document of many hypotheses. Memex's
frontmatter-check hook validates page-level frontmatter, not table-row
metadata. Therefore:

- The page-level `status:` field on `hypothesis-register.md` is `active`
  whenever the page exists.
- Per-row status lives in the table column. The hypothesis's *real*
  state is the table cell.
- The `index-update.py` hook still picks up the per-row counts because
  the page's *content* (the table) is what the hook scans, not just the
  frontmatter.

This is consistent with how the venture profile counts hypotheses in
`index.md` sections "Hypotheses (open)", "Hypotheses (validated)",
"Hypotheses (refuted)" — they read the table, not the frontmatter.

## §3. Row format

```markdown
| ID | Cell | Statement | Status | Falsifier | Measurement | Threshold | Timeframe | Evidence | Updated |
|---|---|---|---|---|---|---|---|---|---|
| H-01 | Customer Segments | Cafés in inner Sydney spend ≥ 4 hours a week reconciling invoices | open | Same cafés spend < 1 hour | Survey 20 owners | ≥ 70% report ≥ 4h | 30 days | — | 2026-05-05 |
```

Rules:

- IDs are zero-padded to 2 digits while < 100, then 3 digits.
- Cell uses the canonical 9 BMC cell names (capitalised).
- Statement uses present tense, full sentence, < 30 words.
- Status is from the enum.
- Evidence is a `;`-separated list of relative markdown links (e.g.
  `[interview-003](../02-customer-discovery/segments/cafes/interviews/interview-003.md)`).
- Updated is `YYYY-MM-DD`.

## §4. Cascade rules on flip

| Flip | Cascade |
|---|---|
| `open` → `accepted` | Recommend `/bmc-update H-<NN>` to flip the cell to `fact`; the BMC bump produces a new version |
| `open` → `refuted` | Recommend `/bmc-update H-<NN>`; the cell stays `hypothesis` but the cell content changes; recommend the user file a `pivot-refine-log` entry if the refutation is major |
| `accepted` → `refuted` | Same as above + flag every `03-value-proposition/` and `05-business-model/` page that cites the hypothesis as stale |
| any → `superseded` | Link forward to the new hypothesis ID in the row's `Statement` field; keep the old row |
| any → `deprecated` | Means "this whole line of inquiry is no longer relevant" — usually accompanies a pivot |

The cascade is *recommended*, not automatic. The user runs the
follow-up skills explicitly.
