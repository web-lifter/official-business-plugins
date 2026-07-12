---
name: customer-discovery-status
description: Run the four-question customer-discovery gate and emit a RAG-style readiness report. Blocking — MVP-planning skills check this gate before running. Overrides log automatically to .memex/log.md.
argument-hint: [optional segment-slug to check just one]
allowed-tools: Read Glob Grep Bash
effort: medium
---

# customer-discovery-status

Idempotency: read-only. The skill itself never mutates state; override logging is the responsibility of the *dependent* skill that bypassed the gate.

**Blocking gate.** `mvp-planning` skills (and the `mvp-scope` orchestrator sequence) check this gate before running. Override with `--force` on the dependent skill; the override **must be logged** to `.memex/log.md` as `## [<today>] gate-override | <skill> bypassed customer-discovery-status (<rollup>)`.

**Why the gate exists.** Steve Blank's customer-development model (*The Four Steps to the Epiphany*; *The Startup Owner's Manual*) treats discovery as gated work: a startup that moves to solution-building before validating the problem, segment, early adopters, and willingness-to-engage produces a product nobody buys. The four checks below operationalise Blank's verify/pivot/refine decision. See `references.md` and `startups/SOURCES.md`.

## User Context

$ARGUMENTS

If `$ARGUMENTS` is a segment slug, scope the gate to that segment;
otherwise produce a venture-wide RAG report (every primary segment must
pass).

---

## Phase 1: Read state

**Objective:** Gather the evidence files.

Read in parallel for each segment under
`02-customer-discovery/segments/`:

- `profile.md` (jobs/pains/gains)
- `early-adopters.md`
- `interviews/interview-*.md` (count + frontmatter)
- `interview-summary.md` if it exists
- The hypothesis register (for confirms/refutes per segment)
- Learning cards in `02-customer-discovery/learning-cards/` —
  specifically those with status `accepted` whose evidence is a
  pre-order, LOI, sign-up, payment, or scheduled deep-dive call

---

## Phase 2: Apply the four checks per segment

For each segment, evaluate:

### Q1 — Have we found a problem people care about?

- Pass: ≥ 5 interviews, with the same problem (high-priority pain)
  surfacing unprompted in ≥ 60%.
- "Unprompted" means the interviewee mentioned it before the
  interviewer did, or in response to an open day-in-the-life question.
- Read the interviews' "Findings → Day-in-the-life" sections and
  search for matches against the segment's high-priority pains.

### Q2 — Have we got the right segment?

- Pass: `profile.md` exists with `status: active`, has at least 3
  prioritised pains and 3 prioritised gains.
- Pass: `early-adopters.md` exists with `status: active`, has filled
  answers for all 5 criteria.

### Q3 — Have we got the right early adopters?

- Pass: `early-adopters.md` lists ≥ 3 named individuals, each with
  contact details and `criteria met = 5/5`, who have engaged ≥ 2 times
  (interview + ≥ 1 follow-up).
- Engagement is computed by cross-referencing the interview count per
  named individual and the follow-up notes.

### Q4 — Are they willing to engage?

- Pass: ≥ 1 learning card with `status: accepted` whose evidence is a
  hard commitment — pre-order, LOI, sign-up, payment, or a scheduled
  deep-dive call. The skill scans the learning-cards folder for these
  patterns.

---

## Phase 3: Compose the RAG report

**Objective:** Per-segment colour, plus a venture-wide rollup.

For each segment:

- 🟢 — all four questions pass
- 🟡 — at least one passes; some fail; produce the precise gap list
- 🔴 — Q1 or Q2 fails; the venture is too early for solution work in
  this segment

Venture-wide rollup is the colour of the *primary* segment (or the
worst colour if the user has not designated a primary).

Produce a markdown report with:

```markdown
# Customer-discovery status — <venture name>

Generated <today>. <Primary segment: <slug>.>

## Venture rollup: 🟢 | 🟡 | 🔴

<one-paragraph summary of what the colour means and what to do next>

## Per-segment

### <segment-slug>: 🟢 | 🟡 | 🔴

| # | Question | Status | Evidence |
|---|---|---|---|
| 1 | Have we found a problem people care about? | ✓ | <N>/<total> interviews mention high-pain in day-in-life |
| 2 | Have we got the right segment? | ✓ | profile.md (3 pains, 3 gains) + early-adopters.md (5/5 criteria) |
| 3 | Have we got the right early adopters? | ✗ | 1 named with 2× engagement (need ≥ 3) |
| 4 | Are they willing to engage? | ✗ | No learning cards with hard commitment evidence |

#### Gap list
- Q3: name 2 more earlyvangelists with 5/5 criteria and ≥ 2 contacts
- Q4: build a test card whose result is a hard commitment — see
  /test-card-build
```

---

## Phase 4: Print and return status

**Objective:** Surface the report and a machine-readable summary.

1. Print the markdown report to the chat.
2. Return a JSON block at the end suitable for downstream skills to
   parse:
   ```json
   {
     "rollup": "green|yellow|red",
     "segments": {
       "<slug>": {
         "color": "green|yellow|red",
         "q1": true,
         "q2": true,
         "q3": false,
         "q4": false,
         "gaps": ["..."]
       }
     }
   }
   ```
3. Do **not** modify any file. Logging the gate result is left to the
   dependent skill (e.g. `mvp-scope` logs the override if `--force` is
   used).

---

## Important principles

- **Read-only.** No writes, no log appends in this skill itself.
- **Blocking by convention.** This skill returns the colour; the
  *dependent* skill (e.g. `mvp-scope`) refuses to run on red without
  `--force`.
- **Override logging is the dependent skill's job.** When a downstream
  skill is forced past this gate, it logs the override:
  `## [<today>] gate-override | <skill> bypassed customer-discovery-status (<rollup>)`.
- **Per-segment is the unit.** Multi-segment ventures must pass on the
  primary; secondary segments may be yellow without halting work on
  the primary.
- **Re-runnable.** Pure aggregation; running it 10 times produces 10
  identical reports.

## Edge cases

1. **No segments defined** — return RED with "no segments defined; run
   /customer-segment-define first."
2. **Multiple segments at different colours** — rollup is the colour
   of the primary segment; report shows all.
3. **No designated primary segment** — rollup is the worst colour;
   prompt the user to designate a primary via segment frontmatter
   (`status: active` on exactly one).
4. **Engagement metric ambiguous** (referral path is not "engagement"
   in the strict sense) — count only direct interviews and follow-up
   notes; document the rule in the report.
