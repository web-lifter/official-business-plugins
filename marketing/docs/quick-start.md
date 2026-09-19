# Marketing setup and first run

Install the plugin through the host's supported marketplace surface, then read
`marketing/RUNTIME.md`. A successful import does not imply that Python packages,
Chrome or paid-provider credentials exist. No session-start installation runs.

For Markdown planning from supplied documents, no local setup is necessary.
Use `seo-status` for readiness information and `seo-setup` when local helpers are
actually required. Prefer already authorised connectors in ChatGPT.

## Explicit local environment

```bash
# From a repository checkout; this only checks readiness:
python marketing/scripts/setup_environment.py
# Only after reviewing and approving downloads:
python marketing/scripts/setup_environment.py --install
# Optional large semantic/advanced clustering packages, when needed:
python marketing/scripts/setup_environment.py --install --optional
```

Use the exact `PYTHON=<path>` emitted on success. The data root is `PLUGIN_DATA`,
then `CLAUDE_PLUGIN_DATA`, then `SEO_DATA_DIR`, or
`~/.claude/plugins/data/marketing`. Setup never writes a venv into installed
plugin code. A missing or stale environment produces a nonzero readiness result.
Do not treat a failed install as success or continue with an unverified interpreter.

Credentials can be supplied through provider-specific environment variables or a
local `credentials.json` in the documented data location. `SEO_CREDENTIALS_FILE`
is an exclusive explicit override. These files are plaintext, not encrypted.
Do not put secrets in the repository or chat. No provider call is required merely
to check that the file has valid structure; paid API tests require authorisation.

Lighthouse is optional and must be installed separately according to its current
official Node/Chrome requirements. The wrapper no longer invokes an automatic
`npx` download or disables Chrome sandboxing. A simulated CLI argument test is not
a browser performance measurement.
