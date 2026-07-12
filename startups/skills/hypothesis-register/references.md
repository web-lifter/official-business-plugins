# hypothesis-register — references

The hypothesis-status conventions enforced by this skill (`open` → `accepted` / `refuted` / `superseded`, never deleted, status-flips require evidence) come from two primary sources. See [`startups/SOURCES.md`](../../../SOURCES.md) for full citations.

## Hypothesis-status conventions

- **Blank, Steve.** *The Four Steps to the Epiphany.* K&S Ranch, 2005.
  - Frames the customer-development model as a sequence of falsifiable beliefs. A hypothesis that fails its test is *refuted* and triggers a pivot; one that passes is *accepted* and the corresponding BMC cell flips from `hypothesis` to `fact`.
- **Blank, Steve & Dorf, Bob.** *The Startup Owner's Manual.* K&S Ranch, 2012.
  - Source of the operating discipline that every hypothesis must have a falsifier, a measurement, a threshold, and a timeframe before it can be tested. Hypotheses without these four elements are beliefs, not hypotheses.

## Validated-learning loop

- **Ries, Eric.** *The Lean Startup.* Crown Business, 2011.
  - The build-measure-learn loop frames a hypothesis flip as the *unit* of validated learning. Every flip must be backed by evidence linked from the register row.
- **Maurya, Ash.** *Running Lean* (3rd ed.). O'Reilly, 2022.
  - Practical conventions for hypothesis tracking, including the "no-deletes, status-only" rule this skill enforces. Maurya treats the register as an append-only ledger.

## Why deletes are refused

A deleted hypothesis is a deleted decision. Chronology is part of the audit trail — if the team flipped a hypothesis to `refuted` six months ago, a future founder reading the venture must be able to see why, not encounter a register that pretends the belief was never held. The skill therefore offers `superseded` and `deprecated` as terminal states but never `Edit`s a row to remove it.

## Cascade discipline

When a flip happens, dependent artefacts (BMC cells, VPC versions, pages under `03-value-proposition/` or `05-business-model/`) may become stale. The skill surfaces them but does *not* auto-modify them — the user runs the follow-up skills explicitly. This pattern (recommend, don't enforce) is consistent with Blank's emphasis on founder judgement at every step.
