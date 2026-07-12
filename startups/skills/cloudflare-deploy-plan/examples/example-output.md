---
title: Cloudflare deploy plan
slug: deploy-cloudflare
type: deploy-plan
status: active
owner: ContractIQ
created: 2026-05-21
updated: 2026-05-21
---

# Cloudflare deploy plan

**Tech stack:** [tech-stack](../tech-stack.md)
**Architecture:** [architecture](../architecture/architecture-overview.md)

## Account state (probed via MCP)

- Account: `a7f1…b03c` — ContractIQ Pty Ltd
- Workers: 0
- D1 databases: 0 (we use Supabase Postgres, not D1)
- KV namespaces: 0
- R2 buckets: 0 (contract files live in Supabase Storage for MVP)
- Hyperdrive configs: 0
- Queues: 0

Empty account — everything below is to be created.

## Services we'll use

| Service | Purpose | Resource name | Binding |
|---------|---------|--------------|---------|
| Worker | API gateway for LLM classification (`/llm/*`) | `contractiq-llm` | — (top-level Worker) |
| Worker | Queue consumer — runs the classifier | `contractiq-classifier` | — |
| Worker | Webhook back to Vercel on classifier completion | `contractiq-webhook` | — |
| Queue | `classifier-jobs` — buffers contracts for classification | `classifier-jobs` | `CLASSIFIER_QUEUE` |
| KV | Idempotency keys + rate-limit buckets | `contractiq-kv` | `KV` |
| Durable Objects | Streaming LLM session state | `LLMSession` class | `LLM_SESSIONS` |

Deliberately not used for MVP: D1 (Supabase is the DB), R2 (Supabase Storage is the file store), Hyperdrive (Workers talk to Supabase via REST, not direct Postgres).

## Wrangler config sketch

```toml
name = "contractiq-llm"
main = "src/index.ts"
compatibility_date = "2026-05-05"
compatibility_flags = ["nodejs_compat"]

[[kv_namespaces]]
binding = "KV"
id = "<created via wrangler kv:namespace create>"

[[queues.producers]]
binding = "CLASSIFIER_QUEUE"
queue = "classifier-jobs"

[[queues.consumers]]
queue = "classifier-jobs"
max_batch_size = 1
max_retries = 3
dead_letter_queue = "classifier-jobs-dlq"

[durable_objects]
bindings = [
  { name = "LLM_SESSIONS", class_name = "LLMSession" }
]

[[migrations]]
tag = "v1"
new_classes = ["LLMSession"]

[vars]
ENVIRONMENT = "production"

# Secrets set via `wrangler secret put`:
#   ANTHROPIC_API_KEY
#   SUPABASE_URL
#   SUPABASE_SERVICE_ROLE_KEY
#   VERCEL_WEBHOOK_SECRET
```

Per-environment (`[env.preview]`) overrides flip `ENVIRONMENT` and bind to preview KV / Queue resources.

## Resource creation plan

Each row is a separate gated apply via the Cloudflare MCP.

| Resource | Type | Name | Notes |
|----------|------|------|-------|
| `contractiq-kv` | KV namespace | preview + production | Idempotency keys (24h TTL) + rate-limit windows |
| `classifier-jobs` | Queue | production | Concurrency 4, max retries 3 |
| `classifier-jobs-dlq` | Queue | production | Dead-letter for poison messages; alarmed in Sentry |
| `contractiq-llm` | Worker | production | Routes: `contractiq.com.au/llm/*` |
| `contractiq-classifier` | Worker | production | Queue consumer only |
| `contractiq-webhook` | Worker | production | Internal — invoked by classifier on completion |

## CLI commands the user will run

```sh
# One-time
wrangler login

# KV
wrangler kv:namespace create "contractiq-kv"
wrangler kv:namespace create "contractiq-kv" --preview

# Queues
wrangler queues create classifier-jobs
wrangler queues create classifier-jobs-dlq

# Secrets (per Worker)
wrangler secret put ANTHROPIC_API_KEY
wrangler secret put SUPABASE_URL
wrangler secret put SUPABASE_SERVICE_ROLE_KEY
wrangler secret put VERCEL_WEBHOOK_SECRET

# Deploy
wrangler deploy
```

**No skill in this marketplace runs these commands.** Tom runs them locally.

## Risks

- **Worker 30 s CPU ceiling** on the paid plan — classifying an 80-page MSA can exceed this. Mitigation: chunk per section before LLM call.
- **Queue at-least-once delivery** — classifier must be idempotent on `contract_id`. Mitigation: dedupe by checking `findings.run_id`.
- **KV eventual consistency (~60 s globally)** — fine for rate-limit windows; the idempotency key check tolerates one duplicate run window.
- **Anthropic API egress from Cloudflare** — billed normally; no extra cost on CF side.
