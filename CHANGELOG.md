# Marketplace changes - 19 September 2026

- Fix rejected marketing MCP metadata; add native OpenAI packaging and runtime fallbacks.
- Business Operations 1.1.0; Data Science 2.1.0; Economics 2.1.0; Marketing 2.1.0; Startups 1.1.0.
- Correct setup, API, cache, SQL, numerical and parsing defects with regression coverage.
- Make Startups self-contained without deleting existing skill identifiers.
- See the detailed audit and compatibility guide for migration and acceptance limits.

# Changelog

All notable changes to the Web Lifter Official Business Plugins marketplace are
documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added — marketplace extracted into its own repository (2026-07-12)

Split out of the former `web-lifter/official-claude-plugins` monorepo into this
standalone marketplace repository. The manifest now sits at the repo root, so
the marketplace installs with the standard one-liner
`/plugin marketplace add web-lifter/official-business-plugins`.

Ships 5 plugins / 121 skills:

- `business-operations` **1.0.1** — 5 skills
- `data-science` **2.0.0** — 9 skills (merged data-analysis + experimentation)
- `economics` **2.0.0** — 9 skills (merged business-economics + strategic-economics)
- `marketing` **2.0.0** — 28 skills (merged brand-manager + seo-toolkit; the SEO
  credential data dir is `~/.claude/plugins/data/marketing/`)
- `startups` **1.0.0** — 70 skills + 9 orchestrator agents

Not carried over from the old monorepo: the `engineering` plugin family, the
`ppc-management` plugin, VirusTotal scanning, and the `ai-utility-plugins` group.
