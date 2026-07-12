# architecture-design — references

## Diagram conventions

- **Mermaid Live Editor.** <https://mermaid.live/> — the canonical syntax reference for the `graph TB` and `sequenceDiagram` notations this skill emits.
- **C4 model (Brown, Simon).** <https://c4model.com/> — context, container, component, code. This skill produces a container-level view by default; deeper levels are out of scope for an MVP overview.

## Sync vs async boundaries

- **Cloudflare Workers limits.** <https://developers.cloudflare.com/workers/platform/limits/> — CPU time, sub-request count, and Queue delivery semantics.
- **Vercel function runtimes.** <https://vercel.com/docs/functions/runtimes> — Edge vs Node serverless trade-offs (cold-start, library compatibility, regional execution).

## Architectural-decision discipline

- See `../adr-writer/references.md` for the Nygard 2011 ADR template. This skill emits an architecture overview; major decisions implied by that overview should be promoted to a numbered ADR.

## Rules this skill enforces

1. **Mermaid, always.** Diagrams are source-controlled text, not screenshots.
2. **Components annotated with providers.** "App" is useless; "Vercel — Next.js 15 SSR" is informative.
3. **Sync/async called out per boundary.** Most architectural defects live at these boundaries.
4. **Risks have mitigations or are open questions.** No risk without a follow-up.
5. **No infra mutations.** This skill is a planner; deployment work lives in `vercel-deploy-plan` and `cloudflare-deploy-plan`.

See `startups/SOURCES.md` for the broader citation context.
