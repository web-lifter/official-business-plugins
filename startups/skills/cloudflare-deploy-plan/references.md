# cloudflare-deploy-plan — references

## Canonical product docs

- **Workers overview and limits.** <https://developers.cloudflare.com/workers/platform/limits/>
- **Wrangler configuration (`wrangler.toml`).** <https://developers.cloudflare.com/workers/wrangler/configuration/>
- **Cloudflare Queues.** <https://developers.cloudflare.com/queues/> — at-least-once delivery, consumer concurrency, dead-letter queues.
- **Cloudflare KV.** <https://developers.cloudflare.com/kv/> — eventual consistency (~60 s), 25 MiB value cap.
- **R2.** <https://developers.cloudflare.com/r2/> — S3-compatible object store, no egress fees to Workers.
- **D1.** <https://developers.cloudflare.com/d1/> — SQLite at the edge; replication model.
- **Hyperdrive.** <https://developers.cloudflare.com/hyperdrive/> — Postgres connection pooling for Workers.
- **Durable Objects.** <https://developers.cloudflare.com/durable-objects/> — single-instance stateful Workers.

## Operational

- **Cloudflare account / paid-plan limits.** <https://developers.cloudflare.com/workers/platform/pricing/>
- **Wrangler environments.** <https://developers.cloudflare.com/workers/wrangler/environments/> — the `[env.preview]` pattern used in the example.

## Rules this skill enforces

1. **Read-only by default.** All MCP probes are list-only; no `kv_namespace_create` or equivalent unless gated.
2. **Plan, never deploy.** This skill never runs `wrangler deploy`.
3. **Bindings explicit in `wrangler.toml`.** The TOML file is the source of truth, not the dashboard.
4. **Account state grounds the plan.** Existing resources may already meet the need — never propose duplicates.
5. **Queues are at-least-once.** Consumers must be idempotent on the business key.
6. **Secrets via `wrangler secret put`,** never in `wrangler.toml`.

## Graceful degrade

Without the Cloudflare MCP the account-state section is marked "MCP unavailable — resource IDs TBD" and the user runs the listed `wrangler` commands manually.

See `startups/SOURCES.md` for the broader citation context.
