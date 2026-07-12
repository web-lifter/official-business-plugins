# Fit report — AU/NZ mid-market in-house counsel v1

Generated 2026-05-21.

Appended to [`vpc-au-midmarket-inhouse-counsel-v1.md`](vpc-au-midmarket-inhouse-counsel-v1.md) under the `## Fit report` section.

## Pain coverage

| Pain (priority) | Relievers | Status |
|-----------------|-----------|--------|
| P-01 — 3+ hour late-night MSA review (high) | 1 (20-min redline) | ✓ |
| P-02 — Missed auto-renewal incidents (high) | 1 (auto-renewal sentinel) | ✓ |
| P-03 — No post-signature obligation system (high) | 1 (obligation tracker) | ✓ |
| P-04 — Generic-AI confidentiality concerns (high) | 1 (private-tenant + AU residency) | ✓ |
| P-06 — Single-point-of-failure anxiety (high) | 1 ("second pair of eyes" framing) | ✓ |
| P-05 — US-corpus tools miss AU issues (medium) | 1 (AU/NZ corpus) | ✓ |
| P-07 — Embarrassment when finance discovers missed clause (medium) | 0 | ✗ |

## Gain coverage

| Gain (priority) | Creators | Status |
|-----------------|----------|--------|
| G-01 — Redline ≤ 20 min (high) | 1 | ✓ |
| G-02 — Plain-English explanations (high) | 1 | ✓ |
| G-03 — AU/NZ-trained corpus (high) | 1 | ✓ |
| G-04 — Post-signature obligation tracker (high) | 1 | ✓ |
| G-05 — Audit-defensible decision log (medium) | 1 | ✓ |
| G-06 — Precedent lookup (medium) | 1 (within tenant) | ✓ |
| G-07 — Delegate first-pass review (medium) | 1 (junior mode) | ✓ |

## Verdict

- **Fit:** partial — one unmatched `medium`-priority pain (P-07). All `high`-priority pains and gains have at least one reliever / creator; medium coverage is 6/7 ≈ 86%, above the 70% threshold.
- **VPC status set to:** draft (one unmatched item; bumping to `active` requires addressing P-07 or accepting the gap explicitly).
- **Action:** Either (a) add a reliever for P-07 in a v2 of the value map — e.g. the audit-defensible decision log already partially serves this pain via the same mechanism; consider re-mapping G-05's mechanism to also relieve P-07. Or (b) drop P-07 from the profile's `medium` priority to `low` if interview evidence does not support its current ranking.

## Gap list

- **P-07 (embarrassment when finance discovers missed clause) has no reliever.** Likely overlap with the audit-defensible decision log (G-05 creator) — the same mechanism that creates the gain (auditable record) may also relieve this pain (the audit log is the defence when finance asks). Recommend re-mapping in [`/value-map-build au-midmarket-inhouse-counsel --version=2`](../value-map-build/).
- **Cross-company precedent gain (raised in 2/7 interviews) deliberately omitted** — conflicts with confidentiality positioning. Logged as an open question in [`.memex/.open-questions/`](../.memex/.open-questions/), not a fit gap.
