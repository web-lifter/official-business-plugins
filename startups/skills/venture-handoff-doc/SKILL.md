---
name: venture-handoff-doc
description: Generate a one-page brief summarising the venture — problem, segment, UVP, validated hypotheses, MVP scope, open risks, current phase. Suitable for a new team member, investor, or future-you. Read-only; writes a single handoff.md.
argument-hint: [optional output filename]
allowed-tools: Read Write Glob Grep Bash
effort: medium
---

# venture-handoff-doc

Idempotency: re-running overwrites `handoff.md` with a fresh snapshot. Git history is the audit trail; no archive copies are made.

A single self-contained markdown brief that lets a new reader catch up
on the venture in five minutes.

## User Context

$ARGUMENTS

Default output is `handoff.md` in the venture root. If `$ARGUMENTS` is a
file path, use that path instead.

---

## Phase 1: Read the venture state

**Objective:** Gather the inputs.

Read in parallel:

- `00-vision/vision-sketch.md` and `00-vision/day-in-life.md`
- `01-hypotheses/hypothesis-register.md`
- All `02-customer-discovery/segments/*/profile.md` and
  `early-adopters.md`
- `02-customer-discovery/learning-cards/LC-*.md` (just the headlines)
- All `03-value-proposition/vpc-*-v*.md` (latest version per segment)
- `04-competitors/uvp.md`, `04-competitors/insights.md`
- The latest `05-business-model/bmc-v*.md`
- `06-relationships-channels/get-keep-grow.md`,
  `funnel-model.md`, `churn-model.md`
- `07-validation/pivot-refine-log.md` head (3 most recent entries)
- `09-mvp/mvp-spec.md`, `mvp-metrics.md`, `feasibility.md` if they
  exist
- `.memex/.open-questions/` — count + headline
- `.memex/log.md` tail

---

## Phase 2: Compose the brief

**Objective:** A single page (~ 1500 words) in fixed-section order.

Sections, in order:

1. **At a glance**
   - Venture name, current phase (from `phase-router` output if
     available), date.
   - One-line summary: "We help [segment] [outcome] by [approach]."
2. **The problem**
   - Pulled from `vision-sketch.md` Problem section. Cite specific
     interview evidence ("≥ X interviewees in segment Y reported ...").
3. **The segment**
   - Names of primary and secondary segments. For the primary, the
     three most prioritised jobs/pains/gains. The early-adopter
     description.
4. **The unique value proposition**
   - Pulled verbatim from `04-competitors/uvp.md`.
5. **What we've validated**
   - Each hypothesis in `accepted` status, with a link to the learning
     card that flipped it.
6. **What's still open**
   - Each hypothesis in `open` status with a falsifier defined. If a
     hypothesis is `open` *without* a falsifier, list it separately
     under a "Hypotheses needing sharpening" sub-heading.
7. **What we've ruled out**
   - Each hypothesis in `refuted` or `deprecated` status, with a
     one-line lesson.
8. **MVP scope** (only if `09-mvp/mvp-spec.md` exists)
   - The cut-keep-maybe lists from `mvp-spec.md`, condensed to the
     top 5 items each.
   - The success metrics from `mvp-metrics.md`.
9. **Recent pivots / refines**
   - Last 3 entries from `pivot-refine-log.md`, summarised.
10. **Open risks**
    - The 3 most critical entries from `.memex/.open-questions/` (sort
      by `updated:` desc).
11. **What to do next**
    - Output of `/phase-router` (top 1-3 actions).
12. **Where to dig in**
    - Pointer to `index.md` and the desktop-app workflow.

---

## Phase 3: Write the file

**Objective:** Write `handoff.md` to the venture root with full
frontmatter; do not modify any other file.

Frontmatter:

```yaml
---
title: Handoff brief — <venture name>
slug: handoff
type: vision         # closest enum match; this is a venture-level
                     # narrative, not a vision sketch
status: active
owner: <venture name>
created: <today>
updated: <today>
---
```

Append a log entry:
`## [<today>] handoff | brief generated for <recipient or "team">`.

---

## Important principles

- **One page.** ≤ 1500 words. If the venture has accumulated more, the
  brief still has to fit. Cut, don't pad.
- **Cite by file path.** Every claim has a link to the page it came
  from. The reader who wants depth follows the link.
- **No invention.** If a section's source file doesn't exist (e.g.
  `mvp-spec.md` for a venture still in discovery), the section says so
  in italics and is skipped from the structure.
- **Read-only on the venture.** This skill writes one file
  (`handoff.md`) plus one log entry. Nothing else changes.
- **Re-entrant.** Re-running overwrites `handoff.md` with a fresh
  snapshot. Old briefs are *not* archived — the venture's git history
  is the audit trail.

## Edge cases

1. **Brand-new venture (only vision exists)** — produce a brief that
   says so honestly. Sections 5-9 will be "Not yet."
2. **Venture in three pivots in 90 days** — the brief should say so
   prominently in section 9, not bury it.
3. **Open-questions count > 20** — list the top 3 in the body, append
   a footnote: "X more open questions; see `.memex/.open-questions/`."
4. **Custom output path** — write only to that path; don't update
   `handoff.md` in the root.
