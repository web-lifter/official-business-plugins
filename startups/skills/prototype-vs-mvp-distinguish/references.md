# prototype-vs-mvp-distinguish — references

See [`startups/SOURCES.md`](../../../../SOURCES.md) for the canonical citation list.

## Primary sources

- **Ries, Eric.** *The Lean Startup.* Crown Business, 2011.
  - Canonical definition: an MVP is "that version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort." (Ch. 6.)
  - Frames the audience requirement: validated learning requires real customers, not a research panel.
  - Frames the environment requirement: the product slice must be *shipped*.

- **Osterwalder; Pigneur; Bernarda; Smith.** *Value Proposition Design.* Wiley, 2014.
  - The test-card / learning-card discipline — every test must specify the hypothesis, the metric, the threshold, and the timeframe.
  - Underpins the "What it proves" dimension in the rubric.

- **Maurya, Ash.** *Running Lean* (3rd ed.). O'Reilly, 2022.
  - Practical operationalisation of the MVP definition with experiment design and risk × impact × effort prioritisation.
  - Source of the "scope = smallest end-to-end thing testing the primary hypothesis" framing.

## The five dimensions

| Dimension | Cited authority |
|-----------|-----------------|
| Audience  | Ries (Ch. 6, on real customers vs friendlies) |
| Fidelity  | Ries (the "build" step requires a shipped slice) |
| Scope     | Maurya (smallest viable test of the primary risk) |
| Environment | Ries (validated learning requires the product to *operate* in the real environment, not a sandbox) |
| What it proves | Osterwalder *et al.* (test cards: hypothesis + metric + threshold + timeframe) |

## Why blocking (with --force)

The five-dimension rule is conjunctive: a single failure produces a prototype, not an MVP. The `--force` override exists for documented edge cases (Wizard of Oz with paying customers, pre-order pages with hard commitments). The override is logged loudly so that the audit trail surfaces every override for later review.
