---
name: cloudflare-deploy-plan
description: Cloudflare deployment plan — Workers vs Pages, D1 vs Hyperdrive, KV vs R2, queues, bindings, wrangler.toml. Optionally probes the user's account via the Cloudflare MCP (read-only). Mutations would require the connector-confirmation flow.
argument-hint: [optional: --cloudflare-account=<id>]
allowed-tools: Read Write Edit Glob Grep
effort: medium
---

# cloudflare-deploy-plan

Cites the connector-confirmation idiom in
[`shared/reference/connector-confirmation.md`](../../../../shared/reference/connector-confirmation.md).
**Read-only by default.** No skill in this marketplace runs
`wrangler deploy`.

Idempotency: side-effect-free planner; rewrites `09-mvp/deploy/cloudflare.md` in place.

Graceful degrade: without the Cloudflare MCP the plan is docs-only with TBD resource IDs; the user runs the listed `wrangler` commands manually.

## User Context

$ARGUMENTS

## Phase 1: Pre-flight

1. Verify venture profile.
2. Read `tech-stack.md`, `architecture-overview.md`.
3. If Cloudflare MCP connected and `--cloudflare-account` given,
   probe in parallel (read-only):
   - `accounts_list`
   - `workers_list`
   - `d1_databases_list`
   - `kv_namespaces_list`
   - `r2_buckets_list`
   - `hyperdrive_configs_list`

## Phase 2: Decide topology

For each Cloudflare service we need:

- **Workers**: which routes / functions go on Workers? (typically
  webhooks, edge logic, image transformations)
- **Pages**: alternative for static / Jamstack frontend if not on
  Vercel
- **D1**: Cloudflare's SQLite. Use only if data lives at edge — for
  most ventures Supabase is the DB.
- **Hyperdrive**: connection pooling for Postgres → Workers. Pair
  with Supabase if Workers need Postgres.
- **KV**: edge key-value. Good for sessions / feature flags / config.
- **R2**: object storage. Cheaper than S3, no egress fees.
- **Queues**: async work between Workers.

For each chosen service:

- Binding name in `wrangler.toml`
- Resource ID / name (read from MCP or marked TBD)
- Scope (per-environment)

## Phase 3: Compose `wrangler.toml`

Sketch the binding section:

```toml
name = "<project>"
main = "src/index.ts"
compatibility_date = "2026-05-05"

[[r2_buckets]]
binding = "ASSETS"
bucket_name = "<assets-bucket>"

[[kv_namespaces]]
binding = "FEATURE_FLAGS"
id = "<kv-namespace-id>"

# ... etc
```

## Phase 4: Write

Write `09-mvp/deploy/cloudflare.md`:

```markdown
---
title: Cloudflare deploy plan
slug: deploy-cloudflare
type: deploy-plan
status: active
owner: <venture name>
created: <today>
updated: <today>
---

# Cloudflare deploy plan

Tech stack: [tech-stack](../tech-stack.md)
Architecture: [architecture](../architecture/architecture-overview.md)

## Account state (probed via MCP)

- Account: <id> — <name>
- Workers: <count>
- D1 databases: <count>
- KV namespaces: <count>
- R2 buckets: <count>
- Hyperdrive configs: <count>

## Services we'll use

| Service | Purpose | Resource | Binding |

## Wrangler config sketch

\`\`\`toml
... (binding sketch)
\`\`\`

## Resource creation plan

(Each requires a separate gated apply — see connector-confirmation.)

| Resource | Type | Name | Notes |

## CLI commands the user will run

\`\`\`sh
# Login
wrangler login

# Create resources
wrangler kv:namespace create "FEATURE_FLAGS"
wrangler r2 bucket create <name>
# etc

# Deploy
wrangler deploy
\`\`\`

**No skill in this marketplace runs these commands.**

## Risks

- <e.g. KV consistency model>
- <e.g. Worker CPU time limits>
- <e.g. Egress when crossing CF<->non-CF boundaries>
```

## Phase 5: Cascade

Recommend pairing with `/vercel-deploy-plan` if Vercel is fronting the
Workers. Recommend `/mvp-feasibility` once both plans exist to
cross-check.

## Phase 6: Log

Append: `## [<today>] cloudflare-deploy-plan | <N> resources`.

## Important principles

- **Read-only.** All MCP probes here are list-only; no
  `kv_namespace_create` etc. unless gated.
- **Plan, not deploy.** No `wrangler deploy`.
- **Bindings explicit.** wrangler.toml is the source of truth.
- **Account state grounds the plan.** Existing resources may already
  meet the need — don't propose duplicates.
- **Graceful degrade.** Without the MCP, the plan is docs-only with
  TBD resource IDs.
