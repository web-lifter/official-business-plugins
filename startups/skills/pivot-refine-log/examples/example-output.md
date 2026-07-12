---
title: Pivot/refine log
slug: pivot-refine-log
type: rule
status: active
owner: contractiq
created: 2026-04-02
updated: 2026-05-19
---

# Pivot/refine log — ContractIQ

Append-only. Every pivot or refine decision is logged here with the canonical entry shape. Entries are never edited after the fact.

---

## [2026-05-19] refine | Narrow primary segment from "any in-house counsel" to AU/NZ mid-market (50–500 staff)

### Trigger evidence

- Interviews 1–7 in [`02-customer-discovery/segments/au-midmarket-inhouse-counsel/interviews/`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/interviews/) — 5 of 7 interviewees are sole-counsel at 50–500-staff AU/NZ companies; the two outside that band (a 1,200-staff bank, a 14-staff scale-up) gave noticeably different pain priorities.
- Hypothesis [`H-001`](../01-hypotheses/hypothesis-register.md) (willingness to pay AU$300/seat/month) is supported in the 50–500 band; the enterprise interviewee priced against LinkSquares and the micro-startup said "free or nothing".

### Decision

We refine the primary segment definition to AU/NZ companies with 50–500 staff and AU$10M–AU$200M revenue. Companies outside that band are de-prioritised for discovery, not abandoned. Priya Natarajan's network of former GC peers is the recruitment channel.

### What changed

- [`02-customer-discovery/segments/au-midmarket-inhouse-counsel/README.md`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/README.md) — band-size and revenue range tightened.
- [`02-customer-discovery/segments/au-midmarket-inhouse-counsel/early-adopters.md`](../02-customer-discovery/segments/au-midmarket-inhouse-counsel/early-adopters.md) — earlyvangelist criterion 1 narrowed.
- Interview guide question 3 reworded to surface band-size early so we can drop a candidate quickly.

### What was kept

- Buyer/user distinction (procurement holds budget, legal evaluates).
- The 14 risky-clause categories ContractIQ classifies (no change).
- The Spellbook / LawGeex / LinkSquares competitor frame.
- Brand name and `contractiq.com.au` domain.
- Tom Whitaker's Python + Streamlit prototype.

### New version pointers

- BMC: n/a — BMC v0 not yet built.
- VPC(s): n/a — value map for this segment not yet built.
- Hypothesis register: [`H-001`](../01-hypotheses/hypothesis-register.md) statement updated (still `open`); no status flips.

---

## [2026-04-02] refine | Add procurement-manager as secondary segment

### Trigger evidence

- Interview 003 referral: P3 (Brisbane edtech Head of Legal) said "the person who actually has the budget for this is our Head of Procurement, Megan."
- Same pattern in interviews 004 and 005.

### Decision

Add `au-midmarket-procurement` as a secondary segment. Do not start a parallel discovery loop until primary segment hits 🟢 on `customer-discovery-status`.

### What changed

- New segment folder scaffolded via `/customer-segment-define au-midmarket-procurement`.
- [`02-customer-discovery/segments/au-midmarket-procurement/README.md`](../02-customer-discovery/segments/au-midmarket-procurement/README.md) created with `status: draft`.

### What was kept

- Primary segment unchanged.
- All existing interviews remain logged under the primary segment.

### New version pointers

- BMC: n/a.
- VPC(s): n/a.
- Hypothesis register: no flips. One new candidate hypothesis (procurement willingness to pay) noted but not yet added.
