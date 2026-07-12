---
name: competitor-insights
description: Synthesise across competitor-table, all SWOTs, and shadow BMCs — what did we learn, what does that change in our hypotheses? Outputs 04-competitors/insights.md plus proposed register updates.
argument-hint: [optional: --segment=<slug>]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# competitor-insights

Synthesises across the competitor table, all SWOTs, and shadow BMCs to surface white space, crowded space, and shared risks. Read-only on the hypothesis register — change proposals are surfaced, not auto-applied.

**Idempotency:** overwrites `04-competitors/insights.md` each run; prior version is in git.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `04-competitors/competitor-table.md`, all
   `04-competitors/swot/*/README.md`, and all
   `05-business-model/shadow-*-v*.md`.
3. Read our latest BMC and VPCs for comparison.

## Phase 2: Synthesise

Look for:

- **White space** — segments / value propositions / channels no one
  serves well
- **Crowded space** — where everyone competes; differentiation must
  be sharp
- **Common weaknesses** — patterns in competitor weaknesses (slow
  support, narrow integrations) we can exploit
- **Common strengths** — patterns in competitor strengths (brand,
  capital) we can't match — implies wedge strategy
- **Pricing patterns** — is the market under or over-priced?
- **Channel patterns** — who's distributing through what? Are any
  channels under-used?
- **Risks our model shares with theirs** — common threats

## Phase 3: Compose actionable insights

For each pattern, propose a hypothesis update or a new hypothesis:

- "All direct competitors charge per-seat; pricing is a hypothesis
  worth testing — propose H-NN: 'Café owners prefer flat-rate
  pricing.'"
- "All competitors target chains; independents are under-served — our
  segment hypothesis is well-positioned."

## Phase 4: Write

Write `04-competitors/insights.md`:

```markdown
---
title: Competitor insights
slug: competitor-insights
type: competitor
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Competitor insights

Generated from <N> competitors, <N> SWOTs, <N> shadow BMCs.

## White space

- ...

## Crowded space

- ...

## Common weaknesses

- ...

## Common strengths

- ...

## Pricing patterns

- ...

## Channel patterns

- ...

## Shared risks

- ...

## Proposed hypothesis updates

(User approves each before applying)

- [ ] New hypothesis: <statement>
- [ ] Update H-NN: <change>
```

## Phase 5: Log

Append: `## [<today>] competitor-insights | <N> insights`.

## Important principles

- **Actionable, not decorative.** Every insight implies a hypothesis
  or action.
- **Synthesis, not summary.** Don't restate the SWOTs; abstract
  across them.
- **Read-only on the register.** Hypothesis changes are proposed; the
  user approves and runs `/hypothesis-register` themselves.
