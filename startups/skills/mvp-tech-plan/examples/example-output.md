# MVP tech plan — orchestrator log for ContractIQ

Thin orchestrator. Artefacts produced by the sub-skill runs on 2026-05-21.

## Sub-skill runs

1. **`/tech-stack-recommender`** → [tech-stack](../tech-stack.md) — selected Web Lifter default: Next.js 15 + Supabase + Cloudflare Workers + Vercel + Figma. Hypothesis class: usability (partial-product MVP).
2. **`/architecture-design`** → [architecture-overview](../architecture/architecture-overview.md) — Mermaid component diagram (10 nodes), Mermaid sequence diagram for the upload-to-redline flow, six integration boundaries documented.
3. **`/adr-writer "tech stack decision"`** → [ADR-001-tech-stack](../architecture/ADR-001-tech-stack.md) — status `accepted`; alternatives considered: Remix + Fly.io, SvelteKit + Supabase + Vercel.

## Cross-check

- Tech-stack components and architecture components agree: **ok** (Next.js 15, Supabase Auth/Postgres/Storage, Cloudflare Workers + Queues + KV + Durable Objects, Vercel, Anthropic API, PostHog EU, Sentry — same set in both files).
- ADR-001 cites both `tech-stack.md` and `architecture-overview.md`: **ok**.

## Summary

- **Stack:** Web Lifter default (Next.js 15 + Supabase + Cloudflare Workers + Vercel + Figma).
- **Architecture:** [architecture-overview](../architecture/architecture-overview.md)
- **ADR:** [ADR-001-tech-stack](../architecture/ADR-001-tech-stack.md)

Next: `/mvp-schema-plan` (data-model-from-vpc → supabase-schema-design).
