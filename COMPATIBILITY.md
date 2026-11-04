# Compatibility and acceptance

## Package contract

The repository includes native OpenAI `.codex-plugin/plugin.json` files,
`.agents/plugins/marketplace.json` and per-skill `agents/openai.yaml`, generated
from the existing source catalogue/manifests. Claude manifests and its nine
Startups orchestrators remain available. Workflow instructions are not duplicated.
No MCP server or fabricated registered connector ID is bundled. A skill that
requires live external data must discover an authorised connector or clearly
state that it is working only from supplied data.

## Host matrix

| Capability | Hosted ChatGPT | Local ChatGPT/Codex | Claude Code |
|---|---|---|---|
| Markdown reasoning and supplied documents | Intended portable workflow | Supported workflow design | Supported workflow design |
| Native marketplace metadata | Import surface/workspace dependent | Native repo catalogue | Uses Claude catalogue instead |
| Python and filesystem | Only when execution/mounted files exist | Requires Python/dependencies | Requires Python/dependencies |
| Local persistent venture | Never assume a repository mount | Explicit selected project | Explicit selected project |
| Orchestrator agents | Sequential skill fallback | Host subagent capability or fallback | Nine declared Claude agents |
| SEO/browser/paid APIs | Available authorised tools only | Explicit dependencies/credentials | Explicit dependencies/credentials |
| Hooks/auto-install | None | None | Removed; use setup skill |
| Provider mutations | Separate explicit user authorisation | Same | Same |

This matrix describes the package's behaviour, not a claim that every host or
workspace integration has been exercised. Acceptance requires a real import.

## Maintainer acceptance after merge

1. Sync the repository in the intended ChatGPT marketplace, inspect per-plugin
   results and confirm the new versions. The `.mcp.json` `$comment` error should
   no longer be present because that unused file has been removed.
2. Invoke a planning skill using supplied notes with no connectors; it should
   deliver evidence-labelled Markdown and not invent account access.
3. Invoke `venture-init` in a temporary mounted project and repeat it; verify no
   overwrite or duplicate log entry. In an unmounted chat, confirm it does not
   claim a persistent initialisation occurred.
4. Invoke `seo-setup` without installation approval; no dependency download should
   occur. Exercise credential refresh and paid APIs only in an authorised test
   account with a stated spend limit, not as part of static import validation.
5. Validate each workflow family against realistic prompts and negative cases.
   Existing `evals/suite.yaml` files are evaluation specifications, not proof of
   an automated model run. Store actual model/version, input, output and verdict.

## Official specifications checked on 19 September 2026

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/skills
- https://code.claude.com/docs/en/plugins-reference
- https://code.claude.com/docs/en/hooks

Local/repo marketplace availability can vary by surface. A GitHub PR is not a
published public-directory release or a completed workspace resync.
