---
name: six-ways-to-innovate
description: Apply Strategyzer's six lenses (customer needs, value, product, experience, relationship, channel) to the current customer profile and value map. Generates candidate VP refinements as proposed hypotheses, not facts.
argument-hint: <segment-slug>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# six-ways-to-innovate

Idempotency: each run writes a dated candidates file `six-ways-candidates-<slug>-<YYYY-MM-DD>.md`. Re-running on the same day overwrites that day's file.

Method: the "six ways to innovate" lenses from Osterwalder, Pigneur, Bernarda & Smith, *Value Proposition Design* (Wiley, 2014). See `references.md` and `startups/SOURCES.md`.

This skill is **generative** — outputs are *candidate* hypotheses, not
facts. The user reviews and adds the worthwhile ones to the
hypothesis register.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read the segment's profile.md and the latest VPC.
3. Read the hypothesis register — to dedupe; don't propose hypotheses
   already in the register.

## Phase 2: Walk the six lenses

For each lens, generate 1-3 candidate refinements:

1. **Customer needs** — what jobs/pains/gains might we be missing?
   Look at adjacent segments' likely needs.
2. **Value** — price, performance, customisation. Could a different
   pricing model unlock new buyers? Could performance trade-offs win
   different customers?
3. **The product itself** — what variant of the offering opens new
   value? Different form factors, different depth.
4. **The experience** — onboarding, packaging, brand. Could a
   different experience design win where features can't?
5. **The relationship** — self-serve vs concierge vs community.
   Different relationships fit different segments.
6. **The channel** — direct vs indirect. Could a partner channel
   unlock distribution we can't get directly?

## Phase 3: Write candidates

Write or append to
`03-value-proposition/six-ways-candidates-<slug>-<YYYY-MM-DD>.md`:

```markdown
---
title: Six ways candidates — <segment>
slug: six-ways-<slug>-<date>
type: vpc
status: draft
owner: <venture name>
created: <today>
updated: <today>
---

# Six ways candidates — <segment>

## 1. Customer needs
- <candidate>
- <candidate>

## 2. Value
- <candidate>

## 3. Product
- ...

## 4. Experience
- ...

## 5. Relationship
- ...

## 6. Channel
- ...

## To register
For each candidate the user wants to test:
- Convert to a hypothesis via `/hypothesis-register add` — supply
  falsifier, measurement, threshold, timeframe.
```

## Phase 4: Log

Append: `## [<today>] six-ways | <slug> generated <N> candidates`.

## Important principles

- **Generative, not factual.** Every output is a candidate.
- **Dedupe against the register.** Don't propose what's already there.
- **Six lenses, not five.** Every lens produces at least one
  candidate, even if the answer is "nothing obvious here."
- **The user prunes.** This skill produces ideas; the human picks
  which ones become hypotheses.

## Edge cases

1. Pivot just happened — be conservative; flag candidates that would
   require another pivot.
2. Many high-priority pains unmet — focus the candidates on lenses 1
   and 2; the others are luxuries until the basics work.
