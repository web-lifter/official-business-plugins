---
name: venture-status
description: Print a human-readable snapshot of the current venture — phase, hypothesis tallies (open/accepted/refuted), interviews logged per segment, BMC version, outstanding test cards, recent log activity. Read-only — never mutates state.
argument-hint: [optional segment-slug to filter]
allowed-tools: Read Glob Grep Bash
effort: low
---

# venture-status

Idempotency: pure read-only aggregation. Re-running on unchanged state produces identical output.

A read-only snapshot of where the venture is. Aggregates the venture's
`index.md`, `log.md`, hypothesis register, and per-segment interview
counts into a single markdown report.

## User Context

$ARGUMENTS

If `$ARGUMENTS` contains a segment slug, scope the report to that segment
where relevant; otherwise produce a venture-wide report.

---

## Phase 1: Confirm we're inside a venture

**Objective:** Don't run on the wrong directory.

1. Check `memex.config.json` exists in the cwd and has `profile ==
   "venture"`. If not, abort with the message `not a venture workspace —
   run /venture-init first`.
2. Read `.memex/index.md` head (first 50 lines).
3. Read the tail of `.memex/log.md` (last 20 entries via `grep '^## \['`
   then take the last 20).

---

## Phase 2: Build the snapshot

**Objective:** Produce the report sections in fixed order so users build
muscle memory.

The report has these sections in this order:

1. **Header** — venture name (from `memex.config.json` or
   `00-vision/vision-sketch.md` frontmatter), today's date, current
   phase guess from `phase-router/reference.md` heuristics if available.
2. **Vision** — has `00-vision/vision-sketch.md` been filled in (status
   != `draft`)? Yes / No.
3. **Hypotheses** — count of entries in `01-hypotheses/hypothesis-register.md`
   grouped by status (`open`, `accepted`, `refuted`, `superseded`).
4. **Segments** — per segment under `02-customer-discovery/segments/`:
   slug, profile filled? early-adopters filled? interview count, last
   interview date.
5. **Test cards** — count by status (`open` / `concluded`).
6. **Learning cards** — count and the most recent one's title.
7. **VPCs** — for each segment, the latest VPC version and its fit
   status (`fit` if all prioritised pains/gains have relievers/creators,
   `partial` otherwise).
8. **BMC** — current version number, status of each cell (`hypothesis`
   vs `fact`).
9. **Competitors** — count of competitors in `competitor-table.md`,
   count of full SWOTs, whether `uvp.md` exists.
10. **Channels and funnel** — has `get-keep-grow.md` been written?
    `channel-strategy.md`? `funnel-model.md`? `churn-model.md`?
11. **Pivots and refines** — count from
    `07-validation/pivot-refine-log.md`, most recent date.
12. **Prototypes** — counts under `08-prototype/{paper,digital,feedback}/`.
13. **MVP** — does `09-mvp/mvp-spec.md` exist? metrics? tech-stack? ADR
    count? schema? deploy plans? analytics? feasibility?
14. **Open questions** — count under `.memex/.open-questions/` (excluding
    `README.md`).
15. **Recent activity** — last 5 entries from `log.md`.
16. **Suggested next actions** — call out the obvious gap (e.g. "no
    interviews logged in segment X" → run interview-log; "BMC v1 still
    has all cells tagged hypothesis" → schedule test cards).

For the suggested-next-actions section, defer to `phase-router` if
available; otherwise use the simple heuristics in
`reference.md`.

---

## Phase 3: Render and exit

**Objective:** Print the report; do not write any files.

Render as a single markdown block. Use `*italic*` for "not yet started"
states and `✓` / `✗` markers for boolean states.

Do not modify any file. Do not append to `log.md` (this skill is purely
informational; venture-status calls don't merit log entries).

---

## Important principles

- **Read-only, always.** No `Write`, no `Edit`, no log appends.
- **Stable section order.** Users learn the layout; don't shuffle
  sections based on what's interesting today.
- **Cite by file path.** Each non-trivial fact in the report names the
  file it came from (e.g. "BMC v3 — `05-business-model/bmc-v3.md`").
- **Graceful when empty.** A brand-new venture with only a vision sketch
  should still produce a useful, short report. Don't pad with
  placeholders.
- **Single pass.** Build the report from a fixed set of file reads /
  globs; don't recurse into every page in the wiki. Cap reads at ~30
  files to avoid latency on large ventures.

## Edge cases

1. **Empty venture (just `venture-init` ran)** — report says "vision
   not yet written; run /vision-sketch."
2. **Segment scoped (`$ARGUMENTS` is a segment slug)** — sections 4-7
   are scoped to that segment; other sections are still venture-wide.
3. **Stale dates** — if any frontmatter `updated:` is more than 30 days
   old and the page status is not `deprecated`, flag it in the report.
4. **Non-venture cwd** — abort early, do not produce a partial report.
