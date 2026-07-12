# SEO Toolkit — Credentials

marketing reads all provider API keys from **one plaintext JSON file**. There is no encryption, no passphrase, no OAuth, and no setup wizard. You create the file once, paste your keys in, and every skill reads from it.

---

## Where the file lives

The canonical location is:

| OS | Path |
|---|---|
| Windows | `%USERPROFILE%\.claude\plugins\data\marketing\credentials.json` |
| macOS / Linux | `~/.claude/plugins/data/marketing/credentials.json` |

The loader checks these locations in order and uses the first that exists:

1. `$SEO_CREDENTIALS_FILE` — explicit path override
2. `$CLAUDE_PLUGIN_DATA/credentials.json` — the installed plugin's data dir
3. `~/.claude/plugins/data/marketing/credentials.json` — the canonical default

The simplest approach: always use the canonical path.

---

## File shape

```json
{
  "serpapi":    { "api_key": "..." },
  "dataforseo": { "login": "...", "password": "..." },
  "ahrefs":     { "api_key": "..." },
  "moz":        { "access_id": "...", "secret": "..." },
  "psi":        { "api_key": "..." }
}
```

Only include the providers you use — delete the rest. Edits take effect immediately; no restart needed.

Create it the easy way by running `/marketing:seo-setup`, or copy `credentials.example.json` from the plugin root.

---

## Where to get each key

| Provider | What it unlocks | Get a key |
|---|---|---|
| `serpapi` | SERP data, keyword research | https://serpapi.com/dashboard |
| `dataforseo` | Keyword volume, suggestions (login + password) | https://app.dataforseo.com/api-access |
| `ahrefs` | Backlink data, domain metrics | https://app.ahrefs.com/account/api |
| `moz` | Domain Authority, link metrics (access ID + secret) | https://moz.com/products/api/keys |
| `psi` | PageSpeed Insights / Core Web Vitals | https://console.cloud.google.com → Credentials → API key (enable "PageSpeed Insights API") |

---

## Environment-variable overrides

Each credential can also be supplied via an environment variable, which **takes precedence** over the file. Handy for CI or one-off scripted runs:

| Provider | Variable(s) |
|---|---|
| `serpapi` | `SERPAPI_KEY` |
| `dataforseo` | `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD` |
| `ahrefs` | `AHREFS_API_KEY` |
| `moz` | `MOZ_ACCESS_ID`, `MOZ_SECRET` |
| `psi` | `PSI_API_KEY` |

---

## Checking status

```
/marketing:seo-status
```

Shows which providers are configured (presence only — never prints key values).

---

## Security notes

- The file is **plaintext**. It lives in your `~/.claude` data directory, outside any git repository, so it is never committed.
- On a shared machine, restrict it yourself (e.g. `chmod 600` on POSIX).
- Deleting access: remove the provider's block from the file (and revoke the key in the provider's dashboard if you want to fully kill it).

---

## Troubleshooting

**"… key not found. Add it to …"** — the provider has no entry in the file and no env var is set. Run `/marketing:seo-setup` or edit the file directly.

**"credentials.json is not valid JSON"** — you have a syntax error (trailing comma, missing quote). Fix it or delete and re-create via `/marketing:seo-setup`.
