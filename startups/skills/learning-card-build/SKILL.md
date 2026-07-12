---
name: learning-card-build
description: Generate a 4-part Strategyzer learning card — we tested / observed / learned / will now — for a concluded test card. Proposes the matching hypothesis-register flip.
argument-hint: <test-card-id>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# learning-card-build

Builds the four-part learning card (we tested / observed / learned / will now) from Strategyzer's *Value Proposition Design* (Osterwalder, Pigneur, Bernarda & Smith, 2014). See `references.md`.

**Idempotency:** one learning card per concluded test card; refuses to write a second LC against an already-concluded TC. Hypothesis flips are surfaced as recommendations, never auto-applied.

## User Context

$ARGUMENTS

`<test-card-id>` (e.g. `TC-007`) is required.

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read `02-customer-discovery/test-cards/TC-<NNN>.md`. Halt if it's
   already `concluded`.
3. Compute the next `LC-NNN` ID.

## Phase 2: Build the 4 parts

Use `AskUserQuestion`:

1. **We tested** — restate the hypothesis + experiment summary
   (auto-derived; user confirms).
2. **Observed** — what actually happened. Numbers. Quotes. Be
   specific.
3. **Learned** — what the observation means. One paragraph.
4. **Will now** — the action. Match to one of: confirm hypothesis,
   refute hypothesis, refine and re-test, pivot.

Plus a **Confidence** field (high / medium / low) and an **Evidence**
links field.

## Phase 3: Write the learning card

Write `02-customer-discovery/learning-cards/LC-<NNN>.md`:

```markdown
---
title: Learning card LC-<NNN> — TC-<NNN>
slug: LC-<NNN>
type: learning-card
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# LC-<NNN> — <one-line outcome>

Resolves: [TC-<NNN>](../test-cards/TC-<NNN>.md)
Hypothesis: [H-<NN>](../../01-hypotheses/hypothesis-register.md)

## We tested
<restated>

## Observed

- Sample: <n>
- Result: <number with units>
- Threshold: <threshold from TC>
- Crossed threshold? Yes / No
- Notable quotes / behaviours: ...

## Learned
<one paragraph>

## Will now

- [ ] Confirm hypothesis (recommend `/hypothesis-register flip H-<NN>
  accepted`)
- [ ] Refute hypothesis (recommend `/hypothesis-register flip H-<NN>
  refuted`)
- [ ] Refine and re-test (recommend new `/test-card-build`)
- [ ] Pivot (recommend `/pivot-refine-log pivot`)

## Confidence
<high|medium|low> — <reason>

## Evidence

- <links to interview-NNN.md, raw data, screenshots>
```

## Phase 4: Cascade

1. Update the test card: status `open` → `concluded`; link to the
   learning card.
2. Append to the hypothesis row's `Evidence` column:
   `TC-<NNN> → LC-<NNN> (<outcome>)`.
3. Surface the recommended `/hypothesis-register flip` action — do
   **not** auto-flip. The user runs it explicitly.
4. Append log: `## [<today>] learning-card | LC-<NNN> closes TC-<NNN>
   (<outcome>)`.

## Important principles

- **One learning card per concluded test.** No batch closing.
- **Observed must be specific.** Numbers, quotes, behaviours. Not "it
  went well."
- **The "will now" is mandatory.** A test that produces no follow-up
  decision is wasted.
- **Confidence is honest.** Low confidence learning cards still get
  filed; they trigger refine-and-re-test, not pivots.
- **Hypothesis flip is the user's choice.** Surface, don't auto-flip.

## Edge cases

1. Test card was never run — refuse, ask user to clarify status.
2. Mixed result (some confirmation, some refutation) — log as
   ambiguous; recommend a sharper test card, not a flip.
3. Test card scope grew during execution — note the scope drift in the
   "Observed" section; it affects confidence.
