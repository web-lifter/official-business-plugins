---
title: MVP build plan
slug: mvp-build-plan
type: mvp-spec
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# MVP build plan

**Source:** [mvp-spec](mvp-spec.md)
**Tech stack:** [tech-stack](tech-stack.md) — Next.js 15 + Supabase + Cloudflare Workers
**Architecture:** [architecture-overview](architecture/architecture-overview.md)
**Primary hypothesis under test:** H-002 (redline time < 25 min median).
**Team:** Priya (founder, partial dev), Tom (CTO, full-time).

## Foundations

| Ticket | Acceptance criteria | Deps | Estimate |
|--------|--------------------|------|---------|
| F-01 Init Next.js 15 + pnpm + shadcn/ui | Repo bootstrapped; `pnpm dev` renders landing; CI green | — | XS (0.5d) |
| F-02 Supabase project + local CLI | Project ref recorded; `.env.local` populated; `supabase start` works | F-01 | S (1d) |
| F-03 Migrations M-01..M-07 (per migration-plan.md) | All migrations apply cleanly; smoke `npm run test:rls` passes | F-02 | M (2d) |
| F-04 Auth flow (Supabase OAuth + email fallback) | Sign-in, sign-out, org create on first sign-in; cookies HttpOnly | F-03 | M (2d) |
| F-05 Cloudflare Workers project (`contractiq-llm`, `-classifier`, `-webhook`) | `wrangler dev` runs locally; KV + Queue created in preview env | F-01 | M (1.5d) |

**Foundations total: ~7 dev-days**

## Core value flow (tests H-002)

| Ticket | Acceptance criteria | Deps | Estimate | Hypothesis |
|--------|--------------------|------|---------|-----------|
| C-01 Contract upload UI (`/contracts/new`) | Drag-drop accepts `.docx`/`.pdf` ≤ 25 MB; shows progress; 413 on oversize | F-04 | S (1d) | H-002 |
| C-02 Upload API (`POST /api/contracts/upload`) | Multipart accepted; file stored in Supabase Storage; `contracts` row queued | F-03, F-04 | S (1d) | H-002 |
| C-03 Enqueue classifier on upload | Worker receives `contract_id`; CF Queue persists; 202 returned | F-05, C-02 | S (1d) | H-002 |
| C-04 Document parser (docx via `mammoth`, pdf via PDF.js) | Plain-text extraction with page boundaries on 20-page sample MSA | F-05 | M (2d) | H-002 |
| C-05 Classifier Worker (Anthropic API + 14-category taxonomy) | Returns `Finding[]` for sample MSA in < 40s; idempotent on `contract_id` | C-04 | L (3d) | H-002, H-003 |
| C-06 Findings persistence | `classifier_runs` + `findings` rows written; status flips to `ready` | F-03, C-05 | S (1d) | H-002 |
| C-07 Findings UI (`/contracts/{id}`) | Group by risk level; clause text + page link; pending count badge | F-04, C-06 | M (2d) | H-002 |
| C-08 Accept/Reject per finding | PATCH endpoint + UI; `reviewed_by`, `reviewed_at` populated; toast feedback | C-07 | S (1d) | H-002 |
| C-09 Redline export (docx tracked-changes) | Generated docx applies accepted changes via OOXML; downloads via signed URL | C-08 | L (3d) | H-002 |

**Core total: ~15 dev-days**

## Instrumentation

| Ticket | Acceptance criteria | Deps | Estimate | Metric |
|--------|--------------------|------|---------|-------|
| I-01 PostHog client + server init (EU region) | `posthog.init`; alias on sign-up; consent banner gates client | F-04 | S (1d) | all funnels |
| I-02 Event firing per events-spec.md | All events fire in dev; sanity-checked in PostHog UI | I-01, C-02, C-06, C-09 | S (1d) | H-001, H-002 |
| I-03 Funnel dashboards in repo (`dashboards/*.json`) | Imported via CI; visible in PostHog | I-02 | XS (0.5d) | all |
| I-04 Sentry init (client + Workers) | Errors visible in Sentry; release tagging on deploy | F-05 | S (1d) | reliability |

**Instrumentation total: ~3.5 dev-days**

## Polish

| Ticket | Acceptance criteria | Deps | Estimate |
|--------|--------------------|------|---------|
| P-01 Landing page (`/`) + pricing page (`/pricing`) | Static, Tailwind, Australian copy; UVP front-and-centre | F-01 | S (1d) |
| P-02 Empty-state and error-state copy | All routes have user-friendly 4xx/5xx; no raw stack traces | C-07 | XS (0.5d) |
| P-03 Loading states for classifier (Supabase Realtime poll) | Spinner with elapsed time; auto-refresh when status flips | C-06 | S (1d) |

**Polish total: ~2.5 dev-days. Strict cap — anything beyond is gold-plating for H-002.**

## Launch

| Ticket | Acceptance criteria | Deps | Estimate |
|--------|--------------------|------|---------|
| L-01 Stripe checkout (deferred but stubbed) | `/pricing` clicks → "Join waitlist" form (not Stripe yet — H-001 tests willingness manually) | P-01 | XS (0.5d) |
| L-02 Vercel + CF production deploy (per deploy plans) | `contractiq.com.au` resolves; SSL valid; preview deploys per PR | F-05, P-01 | S (1d) |
| L-03 Support channel: shared inbox + Intercom widget | `help@contractiq.com.au` forwards to Priya; widget on logged-in pages | L-02 | XS (0.5d) |
| L-04 Privacy policy + ToS draft (lawyer-reviewed by Priya) | Linked from footer; references Privacy Act 1988 schedule 1 | P-01 | XS (0.5d) |

**Launch total: ~2.5 dev-days**

## Total estimate

- **Engineering days:** ~30 dev-days
- **Calendar weeks** (1.5 FTE × 60% productive): **~7 weeks** end-to-end
- **Critical path:** F-01 → F-02 → F-03 → F-04 → C-02 → C-03 → C-05 → C-06 → C-07 → C-08 → C-09 → L-02

## Risks

- **C-05 classifier accuracy** — H-003 falsifier is precision < 70%. If precision is below 70% at end of week 4, all C-* tickets after C-06 are at risk. Mitigation: hold C-09 (redline export) until H-003 read is green.
- **C-04 PDF parsing on scanned contracts** — unknown OCR need. Mitigation: scope MVP to text-based PDFs; OCR pushed to v2.
- **F-04 Google Workspace OAuth for in-house counsel** — some firms restrict third-party OAuth. Mitigation: email/password fallback shipped at F-04.
- **L-04 lawyer review of legal docs** — Priya is the lawyer; cost is time only.

## Hand-off

Pair with `/mvp-feasibility` for the regulatory/resource cross-check before kick-off.
