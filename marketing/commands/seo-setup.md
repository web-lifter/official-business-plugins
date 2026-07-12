---
name: seo-setup
description: Create the marketing credentials file so you can paste in your SerpAPI / DataForSEO / Ahrefs / Moz / PageSpeed Insights API keys.
argument-hint: ""
---

# /marketing:seo-setup

You help the user create the plaintext credentials file that every marketing skill reads from. There is no vault, passphrase, or OAuth — just one JSON file.

## Workflow

### 1. Determine the target path

The canonical credentials file is:

```
~/.claude/plugins/data/marketing/credentials.json
```

On Windows that resolves to `C:\Users\<username>\.claude\plugins\data\marketing\credentials.json`. Expand `~` to the user's home directory.

### 2. Check whether it already exists

- If it exists, read it (do NOT print secret values to the transcript — just confirm which providers already have entries) and tell the user it is already set up. Offer to add any missing providers. Stop here unless they want changes.
- If it does not exist, continue.

### 3. Create the file from the template

Create the parent directory if needed, then write this template (use the `Write` tool):

```json
{
  "serpapi":    { "api_key": "" },
  "dataforseo": { "login": "", "password": "" },
  "ahrefs":     { "api_key": "" },
  "moz":        { "access_id": "", "secret": "" },
  "psi":        { "api_key": "" }
}
```

### 4. Tell the user how to fill it in

Tell the user to open that file and paste their keys into the providers they use (they can delete the providers they don't). Where to get each key:

- **SerpAPI** — https://serpapi.com/dashboard
- **DataForSEO** — https://app.dataforseo.com/api-access (login + password)
- **Ahrefs** — https://app.ahrefs.com/account/api
- **Moz** — https://moz.com/products/api/keys (Access ID + Secret)
- **PageSpeed Insights** — https://console.cloud.google.com → Credentials → API key (enable "PageSpeed Insights API")

You may offer to paste a key for them: if they give you a key, write it into the correct field with the `Write`/`Edit` tool. Otherwise they can edit the file directly — changes take effect immediately, no restart needed.

### 5. Confirm

Run `/marketing:seo-status` (or `python "${CLAUDE_PLUGIN_ROOT}/scripts/seo_status.py"`) to show which providers are now configured.

## Security note

This file is plaintext and lives outside any git repository, so it is never committed. Never echo the key values back into the transcript. The `.gitignore` patterns and the data directory keep it off version control.
