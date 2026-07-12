---
name: test-card-build
description: Generate a 5-part Strategyzer test card — we believe / to verify we will / measure / are right if / threshold. Writes 02-customer-discovery/test-cards/TC-NNN.md.
argument-hint: "<hypothesis-id> [optional: experiment-type]"
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# test-card-build

Builds the five-part test card from Strategyzer's *Value Proposition Design* (Osterwalder, Pigneur, Bernarda & Smith, 2014). Refuses to write a test card on a hypothesis that fails `/hypothesis-falsifiability-check`. See `references.md`.

**Idempotency:** the TC ID is auto-incremented; the threshold cannot be moved after creation. Multiple test cards per hypothesis are allowed (but ≥ 3 warns the hypothesis is probably too loose).

## User Context

$ARGUMENTS

`<hypothesis-id>` is required. Optional experiment-type from the
`reference.md` §1 menu (interview, survey, smoke test, concierge,
fake door, A/B, Wizard of Oz).

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read the hypothesis row from
   `01-hypotheses/hypothesis-register.md`.
3. Verify it passes
   `hypothesis-falsifiability-check`. If not, refuse — fix the
   hypothesis first.
4. Compute the next `TC-NNN` ID.

## Phase 2: Build the 5 parts

Use `AskUserQuestion`:

1. **We believe** — restate the hypothesis (auto-derived from the
   register; user confirms).
2. **To verify, we will** — the experiment description. Include type
   (from menu), audience, sample size target.
3. **Measure** — what data we collect; the instrument; the channel.
4. **We are right if** — the falsifier in positive form ("we observe
   X"). Auto-derived from hypothesis; user can refine.
5. **Threshold** — the line for "right." Auto-derived from
   hypothesis.

Plus an optional **Cost / time** sketch and a **Risk to mitigate**
note.

## Phase 3: Write the test card

Write `02-customer-discovery/test-cards/TC-<NNN>.md`:

```markdown
---
title: Test card TC-<NNN> — H-<NN>
slug: TC-<NNN>
type: test-card
status: open
owner: <venture name>
created: <today>
updated: <today>
---

# TC-<NNN> — <hypothesis short label>

Tests: [H-<NN>](../../01-hypotheses/hypothesis-register.md)

## We believe
<statement>

## To verify, we will
<experiment description; type from menu>

## Measure
<data captured; instrument; channel>

## We are right if
<positive observation>

## Threshold
<the line>

## Cost / time

- Time: <hours / days>
- Cost: <AUD>

## Risk to mitigate

<what could go wrong>

## Linked

- Hypothesis: H-<NN>
- Segment: <slug>
- Predecessor test card: <if any>
```

## Phase 4: Cascade

1. Note in the hypothesis register row's `Evidence` column: append
   `TC-<NNN> (open)`.
2. Append log: `## [<today>] test-card | TC-<NNN> for H-<NN>`.

## Important principles

- **One test, one hypothesis.** Test cards are atomic.
- **Falsifiability gate first.** No test card on a vague hypothesis.
- **Threshold cannot be moved after the test.** The threshold is set
  at design time; data either crosses it or doesn't.
- **Cost / time is required.** Even a sketch ("4h, $0") forces the
  user to think about throughput.

## Edge cases

1. Hypothesis fails falsifiability — refuse; route to fix.
2. No segment for the hypothesis — surface; can't recruit without one.
3. Test card already exists for this hypothesis — allowed (multiple
   tests per hypothesis), but warn if ≥ 3 — usually means the
   hypothesis isn't tight enough.
