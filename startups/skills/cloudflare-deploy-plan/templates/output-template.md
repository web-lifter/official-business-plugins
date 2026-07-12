---
title: Cloudflare deploy plan
slug: deploy-cloudflare
type: deploy-plan
status: active
owner: {{venture-name}}
created: {{YYYY-MM-DD}}
updated: {{YYYY-MM-DD}}
---

# Cloudflare deploy plan

**Tech stack:** [tech-stack](../tech-stack.md)
**Architecture:** [architecture](../architecture/architecture-overview.md)

## Account state (probed via MCP)

- Account: {{id}} — {{name}}
- Workers: {{count}}
- D1 databases: {{count}}
- KV namespaces: {{count}}
- R2 buckets: {{count}}
- Hyperdrive configs: {{count}}
- Queues: {{count}}

## Services we'll use

| Service | Purpose | Resource name | Binding |
|---------|---------|--------------|---------|
| {{Workers/KV/R2/...}} | {{purpose}} | {{name}} | {{BINDING_NAME}} |

## Wrangler config sketch

```toml
name = "{{project}}"
main = "src/index.ts"
compatibility_date = "{{YYYY-MM-DD}}"

# bindings ...
```

## Resource creation plan

Each resource requires a separate gated apply — see connector-confirmation.

| Resource | Type | Name | Notes |
|----------|------|------|-------|
| {{name}} | {{type}} | {{slug}} | {{notes}} |

## CLI commands the user will run

```sh
wrangler login
# ... resource creation
wrangler deploy
```

**No skill in this marketplace runs these commands.**

## Risks

- {{risk + mitigation}}
