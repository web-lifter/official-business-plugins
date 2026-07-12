---
name: experiment-design
description: Pick the best experiment type for a hypothesis — interview, survey, smoke test, concierge, fake door, Wizard of Oz, A/B, pre-order, LOI. Recommends with rationale and drafts for /test-card-build.
argument-hint: <hypothesis-id>
allowed-tools: Read Glob Grep
effort: low
---

# experiment-design

Matches a hypothesis to the right experiment type using the menu codified in Ash Maurya's *Running Lean* (3rd ed., 2022) and the Strategyzer test-card library. See `references.md`.

**Idempotency:** read-only; never writes test cards (that is `/test-card-build`). Re-running with a sharper hypothesis can pick a different recommendation — that is the point.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read the hypothesis row.
3. Read `02-customer-discovery/test-cards/` for any existing tests
   covering this hypothesis (avoid duplicate experiment types).

## Phase 2: Match hypothesis to experiment type

Apply the matrix from `test-card-build/reference.md` §2 (Hypothesis cell
→ best test types). Pick top 1-3 candidates.

## Phase 3: Score each candidate

For each candidate, sketch:

- **What it tests** (the falsifier it can verify)
- **Sample target** (per `test-card-build/reference.md` §1)
- **Time / cost** estimate
- **Confidence** the test can produce a clear answer
- **Risk** the test is biased or under-powered

Pick the recommendation: highest confidence within reasonable cost.

## Phase 4: Output

Print to chat:

```markdown
# Experiment recommendation for H-<NN>

Hypothesis: <statement>

## Top recommendation: <type>

- Why: <rationale>
- Sample: <n>
- Time: <duration>
- Cost: <range>
- Risk: <bias / power notes>

## Alternatives

- <type 2>: <why it could work, why it didn't win>
- <type 3>: <ditto>

## Next step

Run `/test-card-build H-<NN> <type>` to draft the test card.
```

## Important principles

- **Recommend, don't prescribe.** The user picks; this skill argues.
- **Avoid duplicates.** Don't recommend the same type that's already
  been tried for this hypothesis.
- **Confidence × cost.** A cheap test with high confidence beats an
  expensive test with high confidence.
- **Read-only.** Never writes test cards; that's `/test-card-build`.

## Edge cases

1. Hypothesis is vague (fails falsifiability) — refuse; route to
   `/hypothesis-falsifiability-check`.
2. All cheap experiments already tried — recommend the smallest
   expensive one.
3. Hypothesis mixes problem and solution claims — split first; design
   per half.
