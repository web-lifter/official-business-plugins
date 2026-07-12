---
name: experiment-prioritise
description: Rank open hypotheses by risk × impact × ease-of-test with the formula explicit. Outputs a ranked list of what to test next. Read-only.
argument-hint: [optional: --segment=<slug> or --cell=<bmc-cell>]
allowed-tools: Read Glob Grep
effort: low
---

# experiment-prioritise

Ranks open hypotheses by `risk × impact × ease`, the prioritisation rubric in Ash Maurya's *Running Lean* (3rd ed., 2022). See `references.md`.

**Idempotency:** read-only on the register; same input scores produce the same ranking.

## User Context

$ARGUMENTS

## Phase 1: Read

1. Verify venture profile.
2. Read `01-hypotheses/hypothesis-register.md`. Filter to `open`
   hypotheses. Apply optional segment / cell filter.
3. Read existing test cards to identify already-tested hypotheses.

## Phase 2: Score each open hypothesis

For each hypothesis, score 1-5:

- **Risk**: how big is the venture's exposure if this hypothesis is
  wrong? Use the BMC cell as a proxy — Customer Segments and Value
  Propositions usually score 4-5; Cost Structure usually 3.
- **Impact**: how much would confirming or refuting this hypothesis
  change the plan? Big cell pivots → 5; refinements → 2.
- **Ease**: how cheap and fast is the experiment? Interview-class
  tests → 5; concierge MVPs → 2; pre-orders → 3.

The user can override defaults via `AskUserQuestion`.

Score = `risk × impact × ease`. Max 125, min 1.

## Phase 3: Output ranked list

Print top 10 (or all if fewer):

```markdown
# Hypothesis priority — top <N>

| Rank | ID | Statement (short) | Risk | Impact | Ease | Score | Suggested type |
|---|---|---|---|---|---|---|---|
| 1 | H-NN | <short> | 5 | 5 | 4 | 100 | Customer interview |

## Recommendation

Run `/test-card-build H-<top-id> <type>` next.
```

## Important principles

- **Explicit formula.** No "the model decides."
- **Ease is honest.** A test that takes 3 weeks isn't easy.
- **Defaults are overridable.** The user knows the venture better
  than the heuristic.
- **Read-only.** No register changes.

## Edge cases

1. All open hypotheses score similar — flag; suggests the register
   needs sharpening, not just prioritising.
2. Highest-scoring hypothesis already has 2+ test cards — drop and
   recommend the second-highest.
3. Filter returns 0 hypotheses — surface; route to
   `/hypothesis-register add` or remove the filter.
