---
title: MVP deploy plan
slug: mvp-deploy-plan
type: deploy-plan
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# MVP deploy plan

**Tech stack:** [tech-stack](../tech-stack.md)
**Architecture:** [architecture](../architecture/architecture-overview.md)

## Sub-plans

- [x] Vercel — see [vercel.md](vercel.md)
- [x] Cloudflare — see [cloudflare.md](cloudflare.md)
- [ ] No other host required for MVP.

## Cross-check

### Env vars

| Var | Vercel | Cloudflare | Match? |
|-----|--------|-----------|--------|
| `NEXT_PUBLIC_SUPABASE_URL` | yes | n/a | ok (browser-only) |
| `NEXT_PUBLIC_SUPABASE_ANON_KEY` | yes | n/a | ok |
| `SUPABASE_SERVICE_ROLE_KEY` | yes (server) | yes (Worker secret) | ok — different consumers, same value |
| `SUPABASE_URL` (server-side) | yes | yes | ok |
| `ANTHROPIC_API_KEY` | no | yes (Worker secret) | ok — only Workers call Anthropic |
| `VERCEL_WEBHOOK_SECRET` | yes | yes | **ok** — symmetric secret, verified |
| `POSTHOG_KEY` | yes (server) + `NEXT_PUBLIC_` (client) | no | ok |
| `SENTRY_DSN` | yes | yes | ok — separate projects per platform |

No drift detected. Both `VERCEL_WEBHOOK_SECRET` values rotated together.

### DNS / domains

- Production: `contractiq.com.au` → Vercel apex via A records to Vercel anycast.
- `api.contractiq.com.au` → Vercel (alias).
- `llm.contractiq.com.au` → Cloudflare Worker route (`contractiq-llm`).
- Preview: `*-{branch}-contractiq.vercel.app` (Vercel default).
- DNS provider: Cloudflare (auth NS), Vercel records via Cloudflare proxy in DNS-only mode for apex.

### Observability

- **Errors:** Sentry — separate projects `contractiq-web` (Vercel) and `contractiq-workers` (CF), both releases tagged with git SHA.
- **Analytics:** PostHog EU region, single project, server+client.
- **Vercel Analytics + Speed Insights:** enabled for marketing routes only (free tier covers).
- No double-instrumentation: web events flow via PostHog; performance via Vercel Analytics; errors via Sentry. Clean separation.

## Open issues from sub-plans

- Cloudflare deploy plan notes 30 s CPU ceiling vs long-running classifier — tracked as open question `wcfw-cpu-ceiling`. Mitigation in C-05 ticket (chunk per section).
- Vercel deploy plan flags ISR cache invalidation on `/pricing` — defer; MVP `/pricing` is static.

## Recommendation

**Proceed.** Env-var matrix is clean; DNS plan is unambiguous; observability has no double-counts. Next step: `/mvp-feasibility` for the full risk roll-up.
