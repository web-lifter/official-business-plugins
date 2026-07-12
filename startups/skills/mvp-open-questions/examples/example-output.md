---
title: MVP open questions
slug: mvp-open-questions
type: open-question
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# MVP open questions

Aggregated from `09-mvp/`. Each item links to its source line.

## From mvp-spec.md
- "TBD: should v1 include the negotiation-brief export, or defer to v2?" — `mvp-spec.md:62`

## From tech-stack.md
- "? Does the team have prior experience with Cloudflare Durable Objects, or is this our first time?" — `tech-stack.md:104`

## From architecture/architecture-overview.md
- "? CF Worker 30 s CPU ceiling vs 60+ s classifier runs on 80-page MSAs — chunk per section?" — `architecture-overview.md:78`
- "? Anthropic rate limits at org scale — capacity planning deferred" — `architecture-overview.md:81`
- "? Document parsing libraries on Workers — `mammoth` polyfill scope unknown" — `architecture-overview.md:84`

## From schema/migrations-plan.md
- "TODO: confirm Supabase Storage signed-URL TTL across all access paths" — `migrations-plan.md:142`

## From deploy/vercel.md
- "? ISR + Supabase cache invalidation on `/pricing` once dynamic" — `vercel.md:134`

## From deploy/cloudflare.md
- "? Queue at-least-once delivery — classifier idempotency on `contract_id` confirmed in code, but no test yet" — `cloudflare.md:115`

## From feasibility.md
- "? Anthropic ZDR addendum — Priya to confirm by end of week" — `feasibility.md:48`
- "? Privacy Act 1988 schedule 1 — APP 8 cross-border disclosure consent flow at upload time" — `feasibility.md:36`

## Promoted to `.open-questions/`

The following items have been promoted to first-class open-question files for tracking:

- [`.open-questions/wcfw-cpu-ceiling.md`](../.memex/.open-questions/wcfw-cpu-ceiling.md) — high (blocks C-05)
- [`.open-questions/anthropic-zdr-contract.md`](../.memex/.open-questions/anthropic-zdr-contract.md) — high (regulatory)
- [`.open-questions/privacy-act-app8-consent.md`](../.memex/.open-questions/privacy-act-app8-consent.md) — high (regulatory; UX work)
- [`.open-questions/pdf-scan-scope.md`](../.memex/.open-questions/pdf-scan-scope.md) — medium (resolved by scoping; tracked for v2)
- [`.open-questions/queue-idempotency-test.md`](../.memex/.open-questions/queue-idempotency-test.md) — medium (test gap)

12 items aggregated; 5 promoted.
