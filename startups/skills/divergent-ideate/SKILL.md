---
name: divergent-ideate
description: Run a structured divergence pass — generate many ideas without critique. Constraints kept light, judgement deferred. Outputs a ranked-by-novelty list under 08-prototype/divergent-<date>.md.
argument-hint: <problem-statement-or-hypothesis-id>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# divergent-ideate

Methodology: the design-thinking diverge/converge loop. See `references.md` for the underlying literature (SCAMPER, IDEO).

Idempotency: re-running on the same trigger produces a new dated file (`divergent-<YYYY-MM-DD>.md`); prior files are preserved.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read context — segment profiles, latest VPC, latest BMC,
   competitor insights. These ground the ideation but should not
   constrain it.

## Phase 2: Generate ideas via prompts

Use the divergence prompts from `reference.md` §1 to generate at
least 20 candidate solution ideas. Categories:

1. **Direct solutions** — straightforward applications of the value
   prop
2. **Inverse solutions** — what if we did the opposite of the
   obvious?
3. **Constraint-relaxing solutions** — what if cost / time / tech
   weren't constraints?
4. **Constraint-tightening solutions** — what if we had only a
   weekend / $0 / no internet?
5. **Cross-domain solutions** — what would <other industry> do?
6. **Strange / playful solutions** — at least 2-3 deliberately weird
   ones

Don't critique during generation. Critique happens in `converge-ideas`.

## Phase 3: Score for novelty

For each idea, score:

- Novelty (1-5) — how different from existing competitors / venture's
  current path
- Stretch (1-5) — how stretching for the team

Sort by novelty descending.

## Phase 4: Write

Write `08-prototype/divergent-<YYYY-MM-DD>.md`:

```markdown
---
title: Divergent ideation — <topic>
slug: divergent-<date>
type: prototype
status: draft
owner: <venture name>
created: <today>
updated: <today>
---

# Divergent ideation — <topic>

Source context: <H-NN | VPC | BMC | competitor insights>

## Ideas (<N> total)

### Category: Direct
1. <idea> [novelty 4 / stretch 2]
2. ...

### Category: Inverse
...

### Category: Constraint-relaxing
...

### Category: Constraint-tightening
...

### Category: Cross-domain
...

### Category: Strange
...

## Top 5 by novelty (for converge-ideas)

1. ...
```

## Phase 5: Log

Append: `## [<today>] divergent | <N> ideas`.

## Important principles

- **No critique.** Critique kills divergence. The next skill
  (`converge-ideas`) does the killing.
- **Quantity over quality.** ≥ 20 ideas; pad with weird ones if
  you're stuck.
- **All six categories.** Skipping cross-domain or strange usually
  means staying in the same shape as competitors.
- **Read-only on hypothesis register.** Ideas may inspire new
  hypotheses, but only `converge-ideas` proposes register updates.

## Edge cases

1. User stops at < 20 — push back once; if they insist, log and warn.
2. Many ideas converge on one theme — fine; the skill records the
   theme as a meta-finding.
