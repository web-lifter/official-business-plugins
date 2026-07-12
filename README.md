# Web Lifter — Official Business Plugins

The Web Lifter **business** plugin marketplace for Claude Code.

**5 plugins · 121 skills · Australian English throughout · evidence-backed markdown outputs.**

Lifestyle plugins (health, finance, productivity) live in the separate [official-lifestyle-plugins](https://github.com/web-lifter/official-lifestyle-plugins) marketplace. Engineering-lifecycle tooling lives in [John OS](https://github.com/johnoconnor0/johns-os). All of them write to the shared `.project/` workspace (see [`OUTPUT-CONVENTIONS.md`](OUTPUT-CONVENTIONS.md)).

## Quick Start

The marketplace manifest is at this repo's root, so it installs with the standard one-liner:

```bash
# Add the marketplace
/plugin marketplace add web-lifter/official-business-plugins

# Install plugins — the @suffix is the marketplace name
/plugin install marketing@official-business-plugins
/plugin install startups@official-business-plugins
/plugin install data-science@official-business-plugins
/plugin install economics@official-business-plugins
/plugin install business-operations@official-business-plugins
```

### Updating

Claude Code reads marketplaces from a local cache re-fetched on demand:

```bash
/plugin marketplace update official-business-plugins
/plugin update marketing@official-business-plugins
```

See [`CHANGELOG.md`](CHANGELOG.md) for what changed in each release.

## Plugins

| Plugin | Skills | Summary |
|---|---:|---|
| [`business-operations`](business-operations/) | 5 | Revenue channel mapping, KPI frameworks, stakeholder briefs, bottleneck detection, pricing strategy |
| [`data-science`](data-science/) | 9 | Dataset profiling & quality audit, data dictionaries, pipeline architecture, cohort analysis, anomaly detection, A/B test design, experiment readouts, forecasting, causal-impact analysis |
| [`economics`](economics/) | 9 | Unit economics (CAC/LTV), market sizing (TAM/SAM/SOM), pricing architecture, cost structure, break-even, cost-benefit, competitive dynamics, elasticity, moat-strength audit |
| [`marketing`](marketing/) | 28 | End-to-end brand creation (identity, guidelines, audience, logo, colour, design tokens, disclaimers, copy) + end-to-end SEO (keyword research + clustering, SERP & competitor analysis, on-page/technical/CWV audits, backlinks, content briefs, schema + entity modelling, local SEO) |
| [`startups`](startups/) | 70 | Full venture workflow — venture chassis, customer discovery, value-proposition & business-model canvases, competitor analysis, relationships & channels, prototyping, MVP planning + engineering bridge, Lean-Startup experimentation. Ships 9 orchestrator agents. |

## Repository layout

```
official-business-plugins/
├── .claude-plugin/marketplace.json   # Marketplace catalogue (5 plugins)
├── <plugin>/
│   ├── .claude-plugin/plugin.json
│   ├── skills/<skill>/               # SKILL.md + templates/ + examples/ + evals/
│   ├── agents/  commands/  hooks/    # where applicable
│   └── settings.json
├── scripts/                          # check-versions, check-validate, check-version-bumps
├── tests/                            # Python smoke tests for embedded scripts
├── CHANGELOG.md  SECURITY.md  OUTPUT-CONVENTIONS.md  LICENSE
└── README.md
```

## Validation

```bash
node scripts/check-versions.mjs    # marketplace ↔ plugin.json version sync
node scripts/check-validate.mjs    # delegates to `claude plugin validate`
```

Both must pass green. See [`.claude/CLAUDE.md`](.claude/CLAUDE.md) for development standards.

## License

MIT
