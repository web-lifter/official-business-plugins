---
title: BMC ↔ VPC linkage v1
slug: bmc-link-vpc-v1
type: bmc
status: active
owner: contractiq
created: 2026-05-21
updated: 2026-05-21
---

# BMC ↔ VPC linkage — v1

BMC: [bmc-v1](../05-business-model/bmc-v1.md)

## Segments linked

| Segment slug | BMC cell entry | VPC file |
|---|---|---|
| in-house-counsel | Head of Legal / General Counsel at AU/NZ mid-market companies | [vpc-in-house-counsel-v1](../03-value-proposition/vpc-in-house-counsel-v1.md) |
| procurement-managers | Procurement managers at the same companies | [vpc-procurement-managers-v1](../03-value-proposition/vpc-procurement-managers-v1.md) (draft, secondary) |

## Value propositions linked

| VPC value-map entry | BMC Value Propositions cell entry |
|---|---|
| Pain reliever: cut MSA review from 3h to ≤ 20min | Redline a 40-page MSA in ≤ 20 minutes |
| Pain reliever: surface PPSA / Privacy Act 1988 / Modern Slavery Act 2018 issues | AU/NZ-specific risk flagging (PPSA, Privacy Act 1988 schedule 1, Modern Slavery Act 2018) |
| Gain creator: every "Buyer shall…" clause into a calendar | Obligation-deadline extraction into calendar + dependency graph |

## Gaps surfaced

- VPC value-map includes "audit-defensible record of why a clause was
  accepted" (a `gain-creator` for in-house counsel). The BMC Value
  Propositions cell does not list this. **Proposed action:** add as a
  fourth `[hypothesis]` VP via `/bmc-update H-005` once the audit-trail
  hypothesis is registered.
- VPC for `procurement-managers` is still a draft; the BMC Customer
  Segments cell links to it but treats the segment as `[hypothesis]`
  pending interview round 2.

## Cascade

- BMC v1 cells annotated with VPC pointers (Customer Segments and Value
  Propositions cells now have the `see vpc-…` sub-bullets).
- `vpc-in-house-counsel-v1.md` got a `## BMC linkage` section pointing
  to bmc-v1 and the matching cell rows.
- Recommend running `/bmc-update` after H-001 concludes — the VPC will
  promote at least one pain-reliever entry from `hypothesis` to `fact`,
  which means the BMC Value Propositions cell should mirror that.
