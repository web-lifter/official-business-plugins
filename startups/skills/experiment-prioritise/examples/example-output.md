---
title: Hypothesis priority — top 5
slug: hypothesis-priority-2026-05-21
type: experiment-prioritise
status: draft
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# Hypothesis priority — top 5

Formula: `score = risk × impact × ease`. Max 125. Each dimension 1–5.
Open hypotheses filtered from the register on 2026-05-21.

## Ranked list

| Rank | ID | Statement (short) | Risk | Impact | Ease | Score | Suggested type |
|---|---|---|---|---|---|---|---|
| 1 | H-001 | AU mid-market in-house counsel pays AU$300/seat/month | 5 | 5 | 5 | **125** | Customer interview (PSM) |
| 2 | H-002 | Senior in-house counsel produces a redline in < 25 min using the tool | 5 | 5 | 2 | **50** | Concierge MVP |
| 3 | H-008 | AU/NZ specialisation produces ≥ 1.5x usefulness uplift vs US-centric reviewer | 4 | 4 | 3 | **48** | Wizard of Oz / side-by-side |
| 4 | H-003 | LLM clause classifier reaches ≥ 85% precision on 14 risky-clause categories | 4 | 4 | 2 | **32** | Held-out test set evaluation |
| 5 | H-009 | Microsoft AppSource AU/NZ listing produces ≥ 8 qualified leads/month at day 90 | 3 | 3 | 3 | **27** | A/B / listing live + tracking |

## Recommendation

Run `/experiment-design H-001` to confirm the experiment type (likely
customer interview with van Westendorp PSM), then
`/test-card-build H-001 customer-interview`. H-001 is unambiguously
the top priority: highest possible score, no test card yet, and every
downstream hypothesis (revenue, channel, partnership cost) depends on
the segment willingness-to-pay landing.

H-002 is the strong second — but at ease=2 (six-week concierge with
real pilots) we should not start it until H-001's first 10 interviews
return interim signal. If H-001's interim signal is negative, the
concierge pilot is wasted.

## Scoring notes

- H-001 ease=5: the interview-class test is fast and cheap (~AU$0
  incremental, 6 weeks duration).
- H-002 ease=2: concierge pilot is expensive (6–8 weeks, AU$2–3k
  including refund float).
- H-003 ease=2: requires the held-out test set, which itself requires
  the AU/NZ corpus build. Real cost in calendar time even though the
  inference cost is low.
- H-008 was elevated by [competitor-insights.md](../../../04-competitors/insights.md) — its
  current score of 48 may rise once H-001 confirms the segment values
  the AU/NZ specialisation enough to drive purchase (the
  "useful enough" signal in H-008 is partially a re-test of H-001).
- H-004 (procurement as separate segment) was already refuted by
  LC-002 — excluded from the open list.
