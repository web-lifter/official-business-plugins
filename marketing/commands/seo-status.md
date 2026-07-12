---
name: seo-status
description: Show which SEO data providers have credentials configured in the marketing credentials file.
argument-hint: ""
---

# /marketing:seo-status

You report which SEO data providers have credentials configured. marketing reads credentials from a single plaintext JSON file — there is no vault, passphrase, or OAuth.

## Workflow

### 1. Locate the Python interpreter

Read `${CLAUDE_PLUGIN_DATA}/python_path.txt` for the venv Python path. If it does not exist, start a new Claude Code session so the `ensure-venv.sh` hook can build the venv, then retry. If that still fails, any system `python` (3.11+) also works.

### 2. Run the status script

```bash
"$PYTHON" "${CLAUDE_PLUGIN_ROOT}/scripts/seo_status.py" --json
```

This never prints secret values — only whether each provider is configured.

### 3. Render the result

Parse the JSON and show:

- The path to the credentials file in use (or a note that none was found).
- A table of providers and whether each is configured:

```markdown
## SEO Toolkit — Credential Status

Credentials file: `C:\Users\<you>\.claude\plugins\data\marketing\credentials.json`

| Provider            | Configured |
|---------------------|:----------:|
| SerpAPI             | yes        |
| DataForSEO          | no         |
| Ahrefs              | no         |
| Moz                 | no         |
| PageSpeed Insights  | yes        |
```

### 4. Next step

If no credentials file exists, tell the user to run `/marketing:seo-setup` (or create the file manually — see below). If some providers are unconfigured, point them at the same file.

## The credentials file

Single plaintext JSON file at `~/.claude/plugins/data/marketing/credentials.json`:

```json
{
  "serpapi":    { "api_key": "YOUR_SERPAPI_KEY" },
  "dataforseo": { "login": "YOUR_LOGIN", "password": "YOUR_PASSWORD" },
  "ahrefs":     { "api_key": "YOUR_AHREFS_KEY" },
  "moz":        { "access_id": "YOUR_ID", "secret": "YOUR_SECRET" },
  "psi":        { "api_key": "YOUR_PSI_KEY" }
}
```

Only include the providers you use. Each value can also be supplied via an environment variable (`SERPAPI_KEY`, `DATAFORSEO_LOGIN`/`DATAFORSEO_PASSWORD`, `AHREFS_API_KEY`, `MOZ_ACCESS_ID`/`MOZ_SECRET`, `PSI_API_KEY`), which takes precedence over the file.

## Security note

Never print credential values in the transcript — the status script only reports presence.
