---
title: Prototype-vs-MVP verdict — contractiq-clause-review
slug: mvp-gate-contractiq-clause-review
type: gate-verdict
status: fail
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Prototype-vs-MVP verdict — contractiq-clause-review

Artifact: `08-prototype/digital/contractiq-clause-review/README.md`

The founder requested classifying the clickable Figma click-through as `type: mvp-spec`. The gate refuses.

## Five-dimension check

| Dimension | Verdict | Evidence |
|-----------|---------|----------|
| Audience | **fail** | 5 paid-pilot-eligible GCs were *invited to feedback sessions*, not asked to commit money. None have signed a pilot contract. Per Ries (2011), MVP audience is real customers, not friendlies in a research setting. |
| Fidelity | **fail** | Click-through Figma. No shipped slice. No working classifier, no real `.docx` upload, no actual redline output. Manual sample contract on a paper card. |
| Scope | pass | Scope is the smallest end-to-end thing that tests H-002 (find risky clauses → review → export redline). No nice-to-haves; no obligation-tracking calendar, no cross-portfolio precedent search. |
| Environment | **fail** | No live auth, no real Supabase row-level-security, no Vercel deployment, no actual contract storage. Click-through only. |
| What it proves | pass | The README clearly states it tests H-002 (median time ≤ 25 minutes) across 5 sessions, with a defined threshold and timeframe. |

## Verdict

**Prototype.** All five dimensions are conjunctive — three failed, so the artifact cannot be relabelled `mvp-spec`.

## Actions

- Keep `type: prototype` on `08-prototype/digital/contractiq-clause-review/README.md`.
- To pass the gate, the team must:
  1. Ship a working slice on `contractiq.com.au` with Supabase auth and a real classifier (closes Audience, Fidelity, Environment).
  2. Recruit ≥ 3 named paying-or-committed early adopters from the discovery pool, not feedback-session participants (closes Audience).
  3. Define MVP success metrics with a threshold and a cut-off date (extends "What it proves" to MVP-class).
- Recommend running `/mvp-planning` to scope the work; revisit this gate when an MVP candidate exists.

## Override

- `--force` invoked: **no**
- This gate produced a hard refusal. The founder accepted the verdict in the post-gate debrief on 2026-05-21.

## Cited rule

Lean Startup MVP definition (Ries, 2011): an MVP is "the version of a new product that allows a team to collect the maximum amount of validated learning about customers with the least effort." A click-through Figma does not deliver any version of the product to a customer; it tests a usability hypothesis on a prototype. The five-dimension rubric operationalises this distinction.
