---
name: seo-setup
description: Set up a local marketing environment or explain connector-based SEO access without collecting secrets in chat.
argument-hint: "[local environment or supplied configuration]"
allowed-tools: Read Write Edit Glob Grep Bash
effort: low
---

# seo-setup

## User Context

$ARGUMENTS

## Phase 1: Choose the execution mode

Read [the runtime guide](../../RUNTIME.md). In ChatGPT, use existing authorised connectors or supplied exports. Do not request API keys in the conversation. With a local project, inspect Python and installed dependencies before proposing changes.

## Phase 2: Explicit environment setup

The bundled `../../scripts/setup_environment.py` checks the environment without changes. Only after the user authorises package downloads, run it with `--install`. Add `--optional` only when semantic/advanced clustering is required. It stores the virtualenv in `PLUGIN_DATA`, then `CLAUDE_PLUGIN_DATA`, then the documented home-directory fallback, never in installed plugin code. There are no automatic SessionStart installs.

## Phase 3: Credentials where genuinely needed

Prefer provider-specific environment variables or approved connectors. For a local credentials file, honour `SEO_CREDENTIALS_FILE`, then the runtime data directory, then `~/.claude/plugins/data/marketing/credentials.json`. Preserve existing content. Create only on explicit request, with owner-only permissions where supported. It is plaintext, not encrypted. A path outside the repo reduces accidental inclusion but does not guarantee secrecy or prevent a user committing it elsewhere. Never print secret values or ask the user to paste them into chat.

## Phase 4: Verify

Run `seo-status` to report configured providers without network calls. Configured is not authenticated or permission-tested. Explain any remaining missing dependency. Return the [setup summary](templates/output-template.md); do not claim a remote or paid service was tested.
