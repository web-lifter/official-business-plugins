# customer-discovery-status — references

The four-question gate this skill enforces operationalises Steve Blank's verify / pivot / refine decision from the customer-development model. See [`startups/SOURCES.md`](../../../SOURCES.md) for full citations.

## Why a blocking gate

- **Blank, Steve.** *The Four Steps to the Epiphany.* K&S Ranch, 2005.
  - The dominant cause of startup failure is moving to solution-building before validating the problem, segment, early adopters, and willingness-to-engage. Blank's verify/pivot/refine decision sits *between* customer discovery and customer validation — refusing to move forward without evidence is the core discipline.
- **Blank, Steve & Dorf, Bob.** *The Startup Owner's Manual.* K&S Ranch, 2012.
  - Concrete operational tests for each of the four questions: problem-care evidence (interview frequency and unprompted mention), right-segment evidence (prioritised pains/gains + 5-criteria earlyvangelists), right-early-adopter evidence (named individuals engaged ≥ 2 times), and willingness-to-engage evidence (a hard commitment — pre-order, LOI, payment, scheduled deep-dive).

## Override discipline

The skill itself is read-only. When a *dependent* skill bypasses the gate with `--force`, that dependent skill must append the override to `.memex/log.md`:

```
## [<today>] gate-override | <skill> bypassed customer-discovery-status (<rollup>)
```

The log entry is the audit trail. Founders who override a yellow or red gate are telling future-them why — the absence of a log entry where a gate was bypassed is itself a finding worth surfacing in `venture-handoff-doc`.

## Per-segment, not venture-wide

Multi-segment ventures must pass on the *primary* segment. Secondary segments may sit on yellow without halting work on the primary. This matches Blank's emphasis that startup focus is segment-by-segment, not market-wide.
