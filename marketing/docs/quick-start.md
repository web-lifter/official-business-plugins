# SEO Toolkit — Quick Start

Get from zero to your first SEO analysis in under five minutes.

---

## Prerequisites

- Claude Code with this plugin installed
- Python 3.11+ on your PATH
- At least one SEO data provider API key (free options: SerpAPI trial, PageSpeed Insights API key)

---

## Step 1 — Install Python dependencies

When you start a new Claude Code session with this plugin loaded, the `ensure-venv.sh` hook automatically creates a virtual environment at `${CLAUDE_PLUGIN_ROOT}/.venv` and installs all dependencies from `requirements.txt`.

You can verify this worked by checking:

```bash
cat "${CLAUDE_PLUGIN_DATA}/python_path.txt"
# Should print something like: /Users/you/.claude/plugins/data/marketing/.venv/bin/python
```

If the venv was not created, check `${CLAUDE_PLUGIN_DATA}/install.log` for errors. The most common cause is Python < 3.11 on your PATH.

---

## Step 2 — Add your API keys

Run:

```
/marketing:seo-setup
```

This creates a plaintext file at `~/.claude/plugins/data/marketing/credentials.json`. Open it and paste in the keys for the providers you use, then save — that's the whole setup. No vault, no passphrase, no OAuth.

```json
{
  "serpapi": { "api_key": "YOUR_SERPAPI_KEY" },
  "psi":     { "api_key": "YOUR_PSI_KEY" }
}
```

Good free starting points:

- **SerpAPI** — free 100 searches/mo, great for SERP analysis. Key: https://serpapi.com/dashboard.
- **PSI** — completely free Google API key. Enable at https://console.cloud.google.com → APIs & Services → PageSpeed Insights API.

(Each key can also be set via an environment variable instead — `SERPAPI_KEY`, `PSI_API_KEY`, etc.)

---

## Step 3 — Verify

```
/marketing:seo-status
```

Renders a table showing which providers are configured. Edits to the credentials file take effect immediately — no restart.

---

## Step 4 — Run your first analysis

### If you connected SerpAPI

```
/marketing:keyword-research [seed keyword or topic]
```

For example:

```
/marketing:keyword-research accounting software for small business Australia
```

This will pull SERP data, classify intent, and return a structured keyword report.

### If you configured PSI

```
/marketing:core-web-vitals-report [your-domain.com.au]
```

This will measure LCP, INP, CLS, and TTFB for your homepage and top landing pages.

---

## Optional — Install Lighthouse CLI

The `core-web-vitals-report` skill can use either the PSI API (cloud, no install needed) or the local Lighthouse CLI (more detailed, works on staging/local environments). To install Lighthouse:

```bash
npm install -g lighthouse
```

Verify it is available:

```bash
npx lighthouse --version
```

Once installed, the `scripts/lighthouse_runner.sh` helper will automatically use it for local URL audits. The PSI API remains the default for production URLs.

---

## Next steps

- Add more provider keys to `~/.claude/plugins/data/marketing/credentials.json` — see `docs/data-sources.md` for which to prioritise.
- Run a full technical audit: `/marketing:technical-seo-audit [your-domain.com.au]`
- Analyse your competitors: `/marketing:competitor-seo-audit [competitor-domain.com.au]`
- Build a keyword cluster map: `/marketing:keyword-clustering-and-mapping [topic]`

For a full list of available skills, run:

```
/marketing:
```

(typing the prefix will show available completions in Claude Code)
