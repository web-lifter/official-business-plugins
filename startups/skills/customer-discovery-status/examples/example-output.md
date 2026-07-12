# Customer-discovery status — ContractIQ

Generated 2026-05-21. Primary segment: `au-midmarket-inhouse-counsel`.

## Venture rollup: 🟡

The primary segment passes Q1 and Q2: 7 logged interviews surface the late-night-MSA-review pain unprompted in 6 of 7, and `profile.md` plus `early-adopters.md` are filled with prioritised jobs/pains/gains and 5/5 criteria filled. Q3 fails because only 2 named earlyvangelists meet 5/5 criteria with ≥ 2× engagement (need 3). Q4 fails because no learning cards yet record a hard commitment (pre-order, LOI, signed pilot scope). MVP-planning skills should not run yet; close Q3 and Q4 before any `/mvp-scope` work. If a downstream skill is forced past this gate it must append `## [<today>] gate-override | <skill> bypassed customer-discovery-status (yellow)` to `.memex/log.md`.

## Per-segment

### au-midmarket-inhouse-counsel: 🟡

| # | Question | Status | Evidence |
|---|----------|--------|----------|
| 1 | Have we found a problem people care about? | ✓ | 6/7 interviews mention P-01 (late-night MSA review) unprompted in day-in-life; 4/7 mention P-02 (missed auto-renewal incident) |
| 2 | Have we got the right segment? | ✓ | `profile.md` (7 pains, 7 gains, all prioritised) + `early-adopters.md` (5/5 criteria filled, 2 named) |
| 3 | Have we got the right early adopters? | ✗ | 2 named (P3 — Brisbane edtech, P5 — Sydney health-tech) with 5/5 criteria and ≥ 2× engagement; need ≥ 3 |
| 4 | Are they willing to engage? | ✗ | No learning cards with hard-commitment evidence (no pre-orders, LOIs, signed pilot scopes, payments, or scheduled deep-dive calls) |

#### Gap list

- Q3: name 1 more earlyvangelist with 5/5 criteria. P7 (Auckland fin-services, 110 staff) currently scores 4/5 — missing "actively looking for a solution"; book follow-up to verify.
- Q4: build a test card whose result is a hard commitment. Recommended: `/test-card-build H-001` — offer 3 named earlyvangelists a paid 2-week pilot at AU$2,400; success = ≥ 1 signed pilot scope.

### au-midmarket-procurement: 🔴

| # | Question | Status | Evidence |
|---|----------|--------|----------|
| 1 | Have we found a problem people care about? | ✗ | 0 interviews logged |
| 2 | Have we got the right segment? | ✗ | `profile.md` status `draft`; no prioritised pains/gains |
| 3 | Have we got the right early adopters? | ✗ | 0 named |
| 4 | Are they willing to engage? | ✗ | n/a |

#### Gap list

- This is a secondary segment. Do not start parallel discovery loops until the primary segment hits 🟢. Logged here for completeness.

## Machine-readable summary

```json
{
  "rollup": "yellow",
  "segments": {
    "au-midmarket-inhouse-counsel": {
      "color": "yellow",
      "q1": true,
      "q2": true,
      "q3": false,
      "q4": false,
      "gaps": [
        "Q3: 2/3 named earlyvangelists with 5/5 criteria",
        "Q4: 0 hard-commitment learning cards"
      ]
    },
    "au-midmarket-procurement": {
      "color": "red",
      "q1": false,
      "q2": false,
      "q3": false,
      "q4": false,
      "gaps": ["secondary segment; deferred until primary 🟢"]
    }
  }
}
```
