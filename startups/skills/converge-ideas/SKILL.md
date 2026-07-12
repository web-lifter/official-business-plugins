---
name: converge-ideas
description: Take the diverged set and converge to 1–3 finalist concepts. Applies four filters (segment fit, hypothesis test value, build cost, novelty wedge). Outputs 08-prototype/converged-<date>.md plus proposed test cards for the finalists.
argument-hint: <divergent-file-slug>
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# converge-ideas

Methodology: design-thinking convergence (impact vs feasibility, dot-voting). See `references.md`.

Idempotency: re-running on the same divergent file produces a new dated converged file.

## User Context

$ARGUMENTS

`<divergent-file-slug>` matches a `08-prototype/divergent-*.md` file.

## Phase 1: Read

1. Verify venture profile.
2. Read the matching divergent file.
3. Read segment profiles, VPCs, BMC, competitor insights.

## Phase 2: Apply four filters

For each idea, score:

1. **Segment fit** — does it serve the primary segment's high-priority
   pains/gains? (1-5)
2. **Hypothesis test value** — does building / testing it answer a
   hypothesis worth answering? (1-5)
3. **Build cost** — invert; lower is better (1-5; 5 = cheap)
4. **Novelty wedge** — does it differentiate vs competitors? (1-5)

Total score = sum. Max 20. Top 1-3 ideas advance to convergence.

## Phase 3: Compose finalists

For each finalist, write a brief:

- Concept name + 1-line description
- Which hypothesis it tests
- Which segment it serves
- Build cost estimate (hours / dollars)
- Risks
- What success looks like (early signal)

## Phase 4: Write

Write `08-prototype/converged-<YYYY-MM-DD>.md`:

```markdown
---
title: Converged finalists
slug: converged-<date>
type: prototype
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Converged finalists

Source: [divergent](divergent-<date>.md)

## Filter scores (top 5)

| # | Idea | Segment fit | Hypothesis value | Build cost (inv) | Novelty | Total |

## Finalists (top 1-3)

### F1: <name>
- Concept: ...
- Tests: H-NN
- Segment: ...
- Build cost: ...
- Risks: ...
- Success signal: ...

### F2: <name>
...

### F3: <name>
...

## Recommended next action

- Run `/paper-prototype F1` to draft a low-fidelity prototype script.
- (Optional: `/test-card-build` if a finalist needs a separate
  experiment plan.)
```

## Phase 5: Log

Append: `## [<today>] converge | <N> finalists`.

## Important principles

- **Three at most.** A founder with 5 finalists has zero finalists.
- **Filter rationale visible.** Score table is part of the artifact.
- **Hypothesis-anchored.** Every finalist tests at least one
  hypothesis. Vanity ideas drop here.
- **Re-runnable.** Re-running on the same divergent file produces a
  new converged file (with a new date in the slug).

## Edge cases

1. All ideas score similar — flag; the divergent set may be too
   homogeneous; recommend re-running with stronger Cross-domain or
   Strange prompts.
2. Top idea has high build cost — flag and prefer a Wizard of Oz or
   Concierge variant for the prototype phase.
