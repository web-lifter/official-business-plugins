# Web Lifter - Official Business Plugins

Business workflows for ChatGPT, Codex and Claude Code: **5 plugins, 122 skills**.
Australian English, evidence-backed Markdown, explicit permissions and portable
workspace behaviour. Import compatibility is separate from having a shell,
provider credentials or a mounted project in a particular chat.

| Plugin | Skills | Scope |
|---|---:|---|
| [business-operations](business-operations/) | 5 | Revenue, KPI, stakeholder, bottleneck and pricing workflows |
| [data-science](data-science/) | 9 | Data quality, experiments, cohorts, pipelines, forecasting and causal analysis |
| [economics](economics/) | 9 | Unit economics, pricing, market size, costs, investment and competition |
| [marketing](marketing/) | 30 | Brand, SEO, keyword clustering, plus explicit setup and status |
| [startups](startups/) | 69 | Venture discovery, design, experimentation and MVP planning |

## ChatGPT and Codex

Use the repository root when adding this GitHub marketplace through a supported
marketplace import surface. The native catalogue is
[.agents/plugins/marketplace.json](.agents/plugins/marketplace.json), with one
`.codex-plugin/plugin.json` per plugin. The Claude catalogue is retained for
compatible importers. Use one catalogue/install source, not two installations of
the same plugin. Availability varies by host and workspace policy.

A sync of `main` cannot pick up unmerged review-branch changes. After merging a
reviewed change, resync and check each plugin's imported version. Then exercise
one ordinary workflow and one missing-capability scenario. Packaging checks
alone do not prove the workspace import or an authenticated integration works.

See [COMPATIBILITY.md](COMPATIBILITY.md) for the host matrix and acceptance checks.

## Claude Code

```text
/plugin marketplace add web-lifter/official-business-plugins
/plugin install startups@official-business-plugins
/plugin install marketing@official-business-plugins
/plugin marketplace update official-business-plugins
```

The other plugin names use the same `@official-business-plugins` suffix.

## Runtime and safety

Every plugin bundles a `RUNTIME.md`. Skills use available tools rather than
assuming Claude-specific tool names exist in another host. A hosted chat returns
its actual sandbox files or Markdown, never a claim that it wrote to an unmounted
repository. Local outputs follow [OUTPUT-CONVENTIONS.md](OUTPUT-CONVENTIONS.md).

Startups is self-contained: new ventures use
`.project/plans/startups/<slug>/`; existing Memex venture profiles are optional
legacy workspaces, not a dependency. No automatic migration occurs.

Marketing no longer installs packages on session start. Invoke `seo-setup` for an
explicit dependency review and opt-in installation. Python 3.11+ is required for
bundled helpers; Lighthouse is separately installed and invoked only on request.
Paid APIs and connector mutations require authorisation. Never put keys in a chat,
report or repository; prefer an already authorised connector in ChatGPT.

## Repository layout

```text
.agents/plugins/marketplace.json     # Generated native catalogue
.claude-plugin/marketplace.json      # Authoritative plugin inventory/versions
<plugin>/.codex-plugin/plugin.json   # Generated OpenAI package metadata
<plugin>/.claude-plugin/plugin.json  # Claude package metadata
<plugin>/RUNTIME.md                  # Capability and output contract
<plugin>/skills/<skill>/SKILL.md     # One shared instruction tree
<plugin>/skills/<skill>/agents/openai.yaml
startups/agents/                     # Optional Claude orchestrators
scripts/                            # Packaging and version checks
tests/                             # Deterministic regression tests
```

## Development and checks

```bash
python -m pip install -r requirements-dev.txt
python scripts/sync-openai.py          # Regenerate native metadata after edits
python scripts/sync-openai.py --check
python scripts/check-portability.py
node scripts/check-versions.mjs
python -m pytest tests -q
node scripts/check-validate.mjs        # Requires installed official Claude CLI
```

The CI workflow also executes generated cohort SQL against a temporary PostgreSQL
17 service and invokes the official Claude validator. It does not call paid APIs,
deploy infrastructure or claim to run prompt-quality evaluations.

[Audit and 69-skill Startups disposition](docs/audits/2026-09-19-marketplace-audit.md)
| [Changelog](CHANGELOG.md) | [Security](SECURITY.md) | [Development standards](AGENTS.md)

MIT. Lifestyle and John OS engineering repositories remain separate projects.
