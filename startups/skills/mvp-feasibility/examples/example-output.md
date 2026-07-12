---
title: MVP feasibility
slug: feasibility
type: mvp-spec
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# MVP feasibility

**Verdict:** 🟡 — proceed with the three listed mitigations.

## Technical risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| CF Worker 30 s CPU ceiling on 80-page MSAs | high | Chunk classifier per contract section (C-05 ticket); fall back to per-page if single chunk exceeds 25 s |
| H-003 classifier precision below 70% on AU MSAs | high | Hold C-09 (redline export) until H-003 read; if < 70%, pivot UX to assistive (suggestions only, no auto-apply) before scaling |
| PDF parsing on scanned (image-only) PDFs | medium | MVP scope is text-based PDFs only; reject scans with a friendly 422; OCR deferred to v2 |
| Supabase Storage signed-URL expiry vs Worker job latency p99 | medium | Set signed-URL TTL to 2 h (vs default 1 h); Worker renews internally if needed |
| Anthropic API rate limits at org scale | low | Concern at >50 paying orgs; not MVP-blocking |

## Regulatory / legal risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Privacy Act 1988 schedule 1 (APP 8 cross-border disclosure) — contracts may contain personal info | high | PostHog EU residency; Anthropic API contracted with cross-border consent in ToS; consent flow at upload time |
| Confidentiality of contract content sent to Anthropic | high | Anthropic Zero Data Retention agreed (paid plan); contractual flow disclosed to customers in ToS draft |
| Modern Slavery Act 2018 reporting clauses — false negative could cause liability | medium | UI labels findings as "suggestions for review"; ToS explicit that ContractIQ is not a substitute for qualified legal advice |
| Legal Profession Uniform Law (NSW/VIC) — providing legal services | low | Tool is decision-support for qualified counsel, not advice to end users; reviewed by Priya |

## Resource risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| 1.5 FTE for 7 weeks vs 30 dev-days estimate | medium | Calendar buffer already in build plan (60% productive ratio); F-03 and C-05 are critical path |
| Founder split (Priya = lawyer + sales + partial dev) | medium | Block out Priya's coding to F-04 and L-04 only; rest is Tom |
| AU$0 marketing budget for the 12-counsel cohort | low | Recruit cohort from Priya's professional network (ex-GC peer group); no paid acquisition for H-002 |

## Open questions blocking

- [`wcfw-cpu-ceiling`](../.memex/.open-questions/wcfw-cpu-ceiling.md): high — must resolve before C-05 starts
- [`pdf-scan-scope`](../.memex/.open-questions/pdf-scan-scope.md): medium — resolved by scoping decision above
- [`anthropic-zdr-contract`](../.memex/.open-questions/anthropic-zdr-contract.md): high — Priya to sign Anthropic ZDR addendum by end of week

## Connector advisories (probed via MCP)

### Supabase advisors
- `policy_exists_rls_disabled`: 0 findings (RLS enabled on every public table — verified post-M-05).
- `auth_users_exposed`: 0 findings.
- `auth_otp_long_expiry`: 1 finding (OTP TTL 1 h, recommended 24 h) — accept; AU counsel sessions are typically same-day.

### Cloudflare account state
- Workers paid plan active. Quota: 10M requests/month included; current usage 0.
- Queues paid plan active. 100M operations/month included.
- KV: 1 GB free tier; expected usage < 10 MB for MVP.

## Recommendation

**Proceed with the three high-severity mitigations.** Specifically:

1. Hold C-09 (redline export) gating on the H-003 precision read at end of week 4.
2. Resolve `wcfw-cpu-ceiling` (chunking spike) before C-05 starts.
3. Sign Anthropic ZDR addendum before any production contract is uploaded.

Once those three are green, the verdict moves to 🟢 and `/mvp-build-plan` can begin in earnest.
