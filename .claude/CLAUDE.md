# Claude development notes

Read [the cross-host contributor contract](../AGENTS.md) first. This repository
preserves Claude packaging while adding generated native OpenAI manifests.

## Claude-specific components

Source manifests live at `<plugin>/.claude-plugin/plugin.json`; the root catalogue
is `.claude-plugin/marketplace.json`. Use documented fields and plugin-relative
paths. Enumerate individual agent Markdown files. Do not duplicate auto-discovered
standard hooks in a manifest. This release deliberately ships no lifecycle hooks;
setup and diagnostics are explicit skills instead.

Skill frontmatter example (quote the argument hint so it is a string, not YAML's
flow-sequence syntax):

```yaml
---
name: skill-name
description: Use when the user requests a specific task; produce its stated output.
argument-hint: "[required context]"
effort: medium
---
```

The repository also accepts documented Claude fields already used by its skills,
such as `allowed-tools`. They are host hints, not cross-platform security grants.
Do not add arbitrary top-level keys to `.mcp.json`; a JSON comment convention is
not valid just because JSON parsing succeeds. Unused MCP files should be absent.

## Validation

```bash
python scripts/sync-openai.py
python scripts/check-portability.py
node scripts/check-versions.mjs
python -m pytest tests -q
node scripts/check-validate.mjs
```

The last command delegates to `claude plugin validate` and fails if unavailable.
It is not a live ChatGPT importer test. Consult the current official specifications:
https://code.claude.com/docs/en/skills
https://code.claude.com/docs/en/plugins-reference
