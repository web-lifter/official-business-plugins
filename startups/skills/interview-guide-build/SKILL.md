---
name: interview-guide-build
description: Generate a customer-discovery interview guide tied to the hypotheses being tested. Constrained to ≤ 30 minutes, open questions, the standard "why / why not / who else / can we follow up" closers. Writes segments/<slug>/interview-guide.md.
argument-hint: "<segment-slug> [optional: hypothesis-id-or-comma-list]"
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# interview-guide-build

Idempotency: re-runs replace the segment's `interview-guide.md` with a freshly generated guide. Use a purpose suffix (e.g. `interview-guide-pricing.md`) to keep parallel guides.

Method: Lean Startup customer-discovery interview techniques (Ries, *The Lean Startup*, 2011; Maurya, *Running Lean*, 2022) — open questions, behavioural recall, the four closers. See `references.md` and `startups/SOURCES.md`.

The guide is structured but not scripted: ≤ 30 minutes total, open
questions, follow-up depth, and the four closers ("why," "why not,"
"who else should we talk to," "can we follow up").

## User Context

$ARGUMENTS

`<segment-slug>` is required. Optional comma-separated hypothesis IDs
narrow the focus to specific hypotheses; without them, the guide
covers the full hypothesis register.

---

## Phase 1: Pre-flight

1. Verify the venture profile.
2. Verify the segment folder exists with at least `profile.md` and
   `early-adopters.md` populated. The guide is built around them.
3. Read the hypothesis register and filter to hypotheses tagged with
   the matching BMC cells (Customer Segments, Value Propositions, or
   any explicitly listed in the optional argument).

---

## Phase 2: Build the section structure

**Objective:** Map sections to time-blocks and to hypotheses.

The guide has 5 fixed sections:

1. **Open** (≤ 3 min) — context, permission, what we're hoping to
   learn, no pitching.
2. **Day-in-the-life walk** (≤ 8 min) — open questions about how the
   interviewee currently does the relevant job. No mention of our
   solution. Map their answers to jobs/pains/gains.
3. **Problem deep-dive** (≤ 10 min) — focused questions on the
   highest-priority pains. Test which pains are real vs imagined.
4. **Solution probe** (≤ 6 min, optional) — only if the interviewee
   raises the topic of solutions or asks what we're working on. Show
   minimal context, then test reactions to the value proposition. Skip
   entirely if the interview is purely problem-discovery.
5. **Close** (≤ 3 min) — the four closers: why, why not, who else,
   follow up.

Each section has 3-5 candidate questions. The guide picks the best 1-2
per section based on the hypotheses being tested.

---

## Phase 3: Generate questions per section

**Objective:** Produce open, non-leading questions tied to specific
hypotheses.

For each hypothesis in scope, generate one or two questions that would
provide evidence for or against it. Validate each question against:

- **Open** — cannot be answered yes/no
- **Non-leading** — does not assume the answer
- **Specific** — about a concrete behaviour or recent event, not a
  hypothetical

Reject and regenerate questions that fail any of these. Examples in
`reference.md` §1.

For the day-in-the-life walk, prefer questions like:

- "Walk me through the last time you [job to be done]."
- "What did you do right before / right after?"
- "What were you using? Who was involved?"
- "What was the most frustrating part?"

For the problem deep-dive:

- "When did this last happen?"
- "What did you try?"
- "Why did that approach not work?"
- "What did it cost you (time / money / mood)?"

For the solution probe:

- "If [scenario], what would you do?" — never "Would you use [our
  product]?" — that's a leading hypothetical, not a behavioural
  question.

For the close (the four closers, verbatim):

- "Why does this matter to you?"
- "Why haven't you solved this already?"
- "Who else should we talk to?"
- "Can we follow up in a few weeks?"

---

## Phase 4: Write the guide

Replace
`02-customer-discovery/segments/<slug>/interview-guide.md`:

```markdown
---
<frontmatter, type: profile, status: active>
---

# Interview guide — <segment label>

Target time: 30 minutes. Bias to open questions, behavioural recall,
and follow-ups (why, why not, who else, can we follow up).

## Hypotheses in scope

- H-NN: <statement>
- ...

## 1. Open (≤ 3 min)

- "Thanks for the time. Quick context: ..."
- "Mind if I record? Just so I can re-listen rather than scribble."
- "I'll keep it to 30."

## 2. Day-in-the-life walk (≤ 8 min)

- <generated question 1>
- <generated question 2>

## 3. Problem deep-dive (≤ 10 min)

- <generated question 1>
- <generated question 2>

## 4. Solution probe (≤ 6 min, only if appropriate)

- <generated question 1>

## 5. Close (≤ 3 min)

- Why does this matter to you?
- Why haven't you solved this already?
- Who else should we talk to?
- Can we follow up in a few weeks?

## Rubric for capturing

When logging via `/interview-log`, capture for each hypothesis:

- Confirmed | Refuted | Ambiguous
- The quote or behaviour that informs the call
- Follow-up needed?
```

---

## Phase 5: Log

Append:
`## [<today>] interview-guide | <slug> built (<N> hypotheses)`.

---

## Important principles

- **Open questions only.** Yes/no questions in a guide are an instant
  fail. Regenerate.
- **30 minutes hard cap.** A 45-minute guide gets cut for time and
  loses the close.
- **Behavioural, not hypothetical.** "What would you do?" is weaker
  than "What did you do last time?"
- **Solution probe is optional.** Pure problem-discovery guides skip
  it. Don't pitch unless they ask.
- **The four closers are mandatory.** "Who else should we talk to?"
  alone is worth the entire interview.

## Edge cases

1. **Hypothesis register is empty** — refuse, route to
   `/hypothesis-register` first.
2. **All hypotheses lack falsifiers** — generate the guide anyway but
   warn that the answers will be hard to interpret without
   measurement criteria.
3. **Segment profile is empty** — refuse, route to
   `/customer-profile-build`.
4. **Multiple guides for one segment** — allowed; suffix with a
   purpose tag, e.g. `interview-guide-pricing.md`. The default is
   `interview-guide.md`.
