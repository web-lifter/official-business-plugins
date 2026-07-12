---
name: interview-log
description: Capture an interview as raw notes plus structured extraction — which jobs/pains/gains were confirmed, new, or refuted, and which hypotheses moved. Append-only — once filed, an interview is never edited.
argument-hint: "<segment-slug> [optional: interviewee-name-or-pseudonym]"
allowed-tools: Read Write Bash Glob Grep
effort: medium
---

# interview-log

Idempotency: append-only. Every invocation creates a new `interview-NNN.md` file; existing interviews are never overwritten.

Method: Lean Startup customer-discovery interview practice (Ries, 2011; Maurya, 2022) plus Blank's evidence-trail discipline (each interview is the canonical record behind any hypothesis flip). See `startups/SOURCES.md`.

Each logged interview is an immutable artifact. Edits create follow-up
notes, never overwrite the original. This is the bedrock of the
hypothesis register's evidence trail.

## User Context

$ARGUMENTS

`<segment-slug>` is required. Optional interviewee name (or pseudonym).

---

## Phase 1: Pre-flight

1. Verify the venture profile.
2. Verify segment folder exists with `interview-guide.md`.
3. Compute the next interview number: scan
   `02-customer-discovery/segments/<slug>/interviews/interview-*.md`,
   take the max suffix + 1, zero-padded to 3 digits.

---

## Phase 2: Capture raw notes

**Objective:** Produce the verbatim notes section first, while the
interview is fresh.

Use `AskUserQuestion` (or accept paste-in via `$ARGUMENTS` continuation)
to gather:

1. **Date and duration** of the interview
2. **Interviewee** (name / pseudonym, role, employer, contact channel)
3. **Recording permission** state (recorded / notes-only / off-record)
4. **Raw notes** — free-form text, ideally near-verbatim. The user
   pastes their own notes; the skill does not invent.

Refuse to proceed if raw notes are < 100 words. A logged interview
without substance is noise.

---

## Phase 3: Structured extraction

**Objective:** Walk through the interview guide section-by-section and
extract structured findings.

For each section of the segment's `interview-guide.md`:

1. **Findings** — bullet list of what the interviewee said.
2. **Hypothesis touch-points** — for each hypothesis whose questions
   appeared in this section: did the interview *confirm*, *refute*, or
   leave *ambiguous*? Include the quote or behaviour as evidence.
3. **New jobs / pains / gains** — anything the interviewee mentioned
   that isn't yet on the segment's `profile.md`.
4. **New segments / sub-segments** — if the interviewee fits a
   different segment than expected.
5. **Outliers / surprises** — anything that doesn't fit the model.
6. **Follow-ups** — questions that came up but weren't answered;
   referrals offered.

The extraction is structured but the user has the final say on every
finding. Don't synthesise — let the user mark each touch-point.

---

## Phase 4: Write the file

**Objective:** Persist the interview with the canonical structure.

Write
`02-customer-discovery/segments/<slug>/interviews/interview-NNN.md`:

```markdown
---
title: Interview <NNN> — <interviewee>
slug: interview-<NNN>
type: interview
status: active
owner: <venture name>
created: <interview date>
updated: <interview date>
---

# Interview <NNN> — <interviewee>

- Date: <YYYY-MM-DD>
- Duration: <minutes>
- Recording: <yes / notes only / off-record>
- Interviewee: <name or pseudonym>, <role>, <employer>
- Channel: <how the interview happened>

## Raw notes

<verbatim text from Phase 2>

## Findings

### Day-in-the-life
<bullets>

### Problem deep-dive
<bullets>

### Solution probe
<bullets, or "skipped">

### Close
<bullets, including referrals>

## Hypothesis touch-points

| Hypothesis | Outcome | Evidence |
|---|---|---|
| H-NN | confirm|refute|ambiguous | "<quote>" or <behaviour> |

## New jobs / pains / gains

- [ ] <new item — type — priority guess>

## New segments / sub-segments

- <if any, with reasoning>

## Outliers and surprises

- <bullets>

## Follow-ups

- <referral, or unanswered question>
- <permission to follow up: yes/no>
```

---

## Phase 5: Cascade and log

**Objective:** Surface the next actions but do not auto-flip
hypotheses.

1. For each hypothesis touch-point with `confirm` or `refute`, surface
   to the user: "Should we increment the evidence counter for this
   hypothesis? (Three same-direction confirmations from different
   interviewees flips the status.)"
2. Do **not** automatically flip hypothesis status. The flip happens
   when a learning card is built — that's the right moment for the
   decision.
3. For each "new jobs / pains / gains" item, surface: "Add this to the
   segment's profile.md? Run /customer-profile-build with --update."
4. For each new sub-segment proposal, suggest
   `/customer-segment-define`.
5. Append a log entry:
   `## [<today>] interview | <slug>/interview-<NNN> logged (<N>
   findings)`.

---

## Important principles

- **Append-only.** Once filed, an interview is never edited. If
  corrections are needed, file a follow-up note in the same folder.
- **No invention.** The skill records what the user supplies. It does
  not infer findings from raw notes without confirmation.
- **Hypothesis flips are deliberate.** Logging an interview surfaces
  evidence; flipping a hypothesis is the user's call, made when a
  learning card is written.
- **Privacy.** Pseudonyms allowed; sensitive PII goes outside the
  repo.
- **Re-running creates a new interview file.** Each run produces a new
  `interview-NNN.md`; never overwrites.

## Edge cases

1. **Interview ended early (< 10 min)** — log it, but flag in the
   findings: "interview cut short — limited signal."
2. **Off-record interview** — the recording field is `off-record`;
   the raw-notes section may be paraphrased.
3. **Interviewee fits a different segment** — log under the *current*
   segment, surface the sub-segment proposal in Phase 5.
4. **Duplicate interview number** (concurrent runs) — increment again
   and warn.
