---
name: interview-analyse
description: Aggregate findings across all interviews in a segment — count confirms/refutes per hypothesis, surface emergent themes, flag outliers. Outputs interview-summary.md plus proposed hypothesis-register updates for the user to approve.
argument-hint: <segment-slug>
allowed-tools: Read Write Edit Glob Grep
effort: high
---

# interview-analyse

Idempotency: re-running on a segment after new interviews produces a fresh `interview-summary.md`; the prior is overwritten. History lives in the individual interview files.

Method: Blank's verify/pivot/refine gate — aggregate evidence across ≥ 5 interviews before proposing a hypothesis status change. See `startups/SOURCES.md`.

This skill is the bridge between *running* interviews and *deciding*
what they mean. It produces a per-segment summary plus a list of
hypothesis-register updates the user can approve.

## User Context

$ARGUMENTS

`<segment-slug>` is required.

---

## Phase 1: Pre-flight

1. Verify the venture profile.
2. Verify the segment has ≥ 5 interviews logged. Refuse if fewer:
   "Need ≥ 5 interviews per segment before aggregating; currently <N>."
3. Read the segment's `profile.md`, `early-adopters.md`, and all
   `interviews/interview-*.md` files in parallel.

---

## Phase 2: Aggregate hypothesis touch-points

**Objective:** For each hypothesis touched in any interview, count
confirms / refutes / ambiguous.

For each hypothesis:

- Total interviews mentioning it (denominator)
- Confirms (with same-direction direction)
- Refutes (with same-direction direction)
- Ambiguous

A hypothesis is **strongly supported** if confirms / total ≥ 0.7
across ≥ 5 interviews.
A hypothesis is **strongly refuted** if refutes / total ≥ 0.7 across ≥
5 interviews.
Otherwise it stays **inconclusive**, and the recommendation is more
interviews or a sharper test card.

---

## Phase 3: Surface emergent themes

**Objective:** Find what came up that wasn't in the original guide.

1. Diff the union of all interviews' "New jobs / pains / gains"
   sections against the segment's `profile.md`. Items that appear in ≥
   2 interviews but not in the profile are *emergent themes*.
2. Identify any "Outliers and surprises" that appear in ≥ 2
   interviews. A repeated surprise isn't a surprise — it's a missing
   model element.
3. Identify any sub-segment proposals that appear ≥ 2 times — these
   are real candidates for `/customer-segment-define` of a sub-segment.

---

## Phase 4: Build proposed register updates

**Objective:** Compose the list of hypothesis-register changes the
user should approve.

For each hypothesis:

- If strongly supported and currently `open` → propose
  `flip H-NN accepted`
- If strongly refuted and currently `open` → propose
  `flip H-NN refuted`
- If inconclusive but ≥ 5 interviews → propose either "more interviews
  with sharper questions" or "build a test card to test this
  experimentally"
- If new emergent theme → propose adding a new hypothesis (the user
  fills in falsifier/measurement/threshold/timeframe via the
  hypothesis-register skill)

Produce **proposals**, not changes. The user approves each one
individually before any flip happens.

---

## Phase 5: Write the summary

Write
`02-customer-discovery/segments/<slug>/interview-summary.md`:

```markdown
---
title: Interview summary — <segment label>
slug: interview-summary-<segment>
type: profile
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Interview summary — <segment label>

Based on <N> logged interviews, dates <earliest> – <latest>.

## Hypothesis touch-points

| Hypothesis | Total | Confirms | Refutes | Ambiguous | Direction |
|---|---|---|---|---|---|
| H-NN | <N> | <C> | <R> | <A> | strongly supported|strongly refuted|inconclusive |

## Emergent themes

- <theme>: appeared in <N> interviews
- <theme>: appeared in <N> interviews

## Sub-segment candidates

- <slug-suggestion>: <N> interviews fit
- ...

## Repeated outliers

- <surprise>: <N>×

## Proposed register updates

(User approves each before applying)

- [ ] H-NN: flip to `accepted` — confirmed in <N>/<total>
- [ ] H-NN: flip to `refuted` — refuted in <N>/<total>
- [ ] New hypothesis: <statement> — emerged in <N> interviews

## Follow-ups required

- <named interviewees pending follow-up>
- <unanswered questions>
- <referrals to chase>
```

---

## Phase 6: Apply approved updates

**Objective:** Once the user approves the proposals, dispatch the
hypothesis-register skill in `flip` or `add` mode for each.

For each approved item:

- Call the `hypothesis-register` skill with the appropriate args
  (`flip H-NN <new-status>` or `add <statement>`).
- Pass evidence: a markdown link to the segment's
  `interview-summary.md`.

---

## Phase 7: Log

Append:
`## [<today>] interview-analyse | <slug> summary across <N> interviews;
<flip count> proposed flips, <add count> new hypotheses`.

---

## Important principles

- **Aggregation, not invention.** Every claim cites the interview
  count and direction.
- **The user approves every flip.** This skill never auto-flips.
- **Strong signal threshold is 0.7 / 5+.** Below that it's inconclusive.
- **Emergent themes are surfaced, not silently absorbed.** The user
  decides whether to bake them into the profile.
- **Re-runnable.** Re-running on the same segment after new interviews
  produces a fresh summary; the prior is overwritten (history lives in
  the interview files themselves).

## Edge cases

1. **One hypothesis is touched in 1 interview, strongly confirmed** —
   not enough signal; mark as "single-interview signal," recommend
   more.
2. **Many hypotheses inconclusive** — surface as "needs sharper test
   cards"; route to `experimentation/test-card-build`.
3. **New sub-segment candidate stronger than original segment** —
   recommend `/customer-segment-define` of the sub-segment as a fresh
   segment, then re-running discovery for it.
4. **Conflicting evidence between interviews** — record both
   directions; do not average. Inconclusive is the right outcome.
