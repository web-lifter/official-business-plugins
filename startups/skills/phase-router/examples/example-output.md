# Phase router — ContractIQ

Generated 2026-05-21.

## Current state (one paragraph)

ContractIQ has a written vision sketch, one primary segment (`au-midmarket-inhouse-counsel`) with `profile.md` and `early-adopters.md` filled in, and 7 logged interviews. The hypothesis register has 3 open hypotheses (H-001 demand, H-002 usability, H-003 scale) all with falsifiers. No interview-summary.md exists yet; no VPC version exists for the segment. BMC v0 not built.

## Next actions (1–3, priority order)

### 1. `/interview-analyse au-midmarket-inhouse-counsel`

- **Why:** 7 interviews logged, no aggregate summary. The verify/pivot/refine gate cannot fire until the touch-points per hypothesis are counted across the full sample.
- **Evidence:** `02-customer-discovery/segments/au-midmarket-inhouse-counsel/interviews/interview-001.md` through `interview-007.md`.
- **Skips:** none.

### 2. `/value-map-build au-midmarket-inhouse-counsel`

- **Why:** Customer profile (right half of VPC) is `status: active` with 6 prioritised pains and 6 prioritised gains, but no left half has been built. Spellbook, LawGeex and LinkSquares analysis is queued behind this — UVP work depends on a v1 value map.
- **Evidence:** `02-customer-discovery/segments/au-midmarket-inhouse-counsel/profile.md`, hypothesis register row H-002.
- **Skips:** none.

### 3. `/customer-discovery-status au-midmarket-inhouse-counsel`

- **Why:** Once `interview-analyse` lands, the four-question gate becomes meaningful. Running it now would return 🟡 (Q1/Q2 likely pass; Q3 needs 3 named earlyvangelists with 5/5 criteria — currently 2; Q4 needs ≥ 1 hard commitment learning card).
- **Evidence:** `02-customer-discovery/segments/au-midmarket-inhouse-counsel/early-adopters.md`.
- **Skips:** running `/mvp-scope` now would bypass this gate; route to gap-fill first.

## Routing rules matched

- Rule 4 — ≥ 5 interviews per segment, no analysis → `interview-analyse`
- Rule 5 — customer profile exists, no VPC → `value-map-build`
- Rule 13 — pre-`customer-discovery-status` 🟢, no MVP scope → gate-check before MVP work

## Also worth knowing

- Zero pivots logged in `07-validation/pivot-refine-log.md` — venture is in stable discovery.
- Hypothesis H-001 (willingness to pay AU$300/seat/month) needs one hard-commitment learning card before Q4 of the gate can turn green. See `/test-card-build H-001`.
- Tom Whitaker's prototype is on Python + Streamlit; do not start MVP architecture work until Priya Natarajan confirms a 🟢 gate.
