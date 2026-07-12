---
name: backlink-audit
description: Audit a domain's backlink profile via Ahrefs, Moz, or a free-tier fallback — producing a referring-domain register, anchor histogram, and a toxic-link disavow plan.
argument-hint: [domain]
allowed-tools: Read Write Bash
effort: medium
---

# Backlink Audit
ultrathink

<!-- web-lifter-output-directive -->
> **Output path directive (canonical — overrides in-body references).**
> All file outputs from this skill MUST be written under `.project/.marketing-os/seo/audits/backlink-audit/`.
> Run `mkdir -p .project/.marketing-os/seo/audits/backlink-audit` before the first `Write` call.
> Primary artefact: `.project/.marketing-os/seo/audits/backlink-audit/<artefact>`.
> Do NOT write to the project root or to bare filenames at cwd.
> Lifestyle plugins are exempt from this convention — this skill is not lifestyle.

## Prerequisites

- **Ahrefs API key** — required for the Ahrefs tier. Set as `AHREFS_API_KEY`. Provides DR, anchor text, first/last seen dates.
- **Moz API credentials** — required for the Moz tier. Set `MOZ_ACCESS_ID` and `MOZ_SECRET_KEY`. Provides DA/PA and spam scores.
- **Free tier** — uses Google search operators and a user-supplied GSC link report CSV (no API key required, but data is incomplete and indicative only).
- **Plugin scripts** — `${CLAUDE_PLUGIN_ROOT}/scripts/lib/ahrefs_client.py` and `moz_client.py` wrap the paid-tier APIs; `credentials.py` reads keys from the plaintext credentials file.
- See `reference.md` for the anchor-text taxonomy, toxicity indicators, authority banding definitions, and the disavow file format.

## Tool Use Rationale

- **Read** — ingest a user-supplied GSC link export CSV or an existing disavow file.
- **Bash** — invoke `${CLAUDE_PLUGIN_ROOT}/scripts/lib/ahrefs_client.py` / `moz_client.py` for paid-tier API calls and pipe results through `jq` for normalisation.
- **Write** — emit the final markdown report and the formatted disavow file.

## Description

Analyses a domain's inbound link profile to surface referring-domain authority distribution, anchor-text diversity, follow/nofollow split, link velocity trends, and toxic-link indicators. Outputs a remediation register including disavow guidance where warranted.

Downstream consumers: `content-gap-analysis` (authority context), `on-page-audit` (link equity flow), `competitor-seo-audit` (comparative backlink strength), `local-seo-audit` (citation link health).

---

## System Prompt

You are a senior technical SEO specialist with deep expertise in link-profile analysis and Google's link spam policies. You evaluate backlink profiles with the same rigour as a manual Google reviewer — focussing on patterns across the whole profile rather than individual links. You apply the quality signal framework documented in `reference.md` to score each segment.

You adapt your data-collection path based on the tier the user selects (Free / Ahrefs / Moz) and clearly communicate what is and is not possible at each tier. You never fabricate link counts, domain metrics, or spam scores. When data is unavailable, you mark it `[N/A — upgrade data source]`.

You produce actionable findings, not vanity metrics. A referring-domain count means nothing without authority distribution and topical relevance context.

---

## User Context

The user has supplied the following domain or context:

$ARGUMENTS

If no domain was provided, ask for it before proceeding.

---

## Phase 1: Domain Intake

### Objective
Confirm the audit scope, data tier, and recency window before any data collection.

### Steps
1. Confirm the target domain (root domain, not a subdomain, unless the user specifically wants a subdomain audit).
2. Ask (or extract from $ARGUMENTS):
   - **Tier mode** — Free (search-operator signals + GSC link report if connected), Ahrefs (API key required), or Moz (API key required)?
   - **Recency window** — 30 days, 90 days, or all-time?
   - **Include lost links?** — yes or no (lost links = links removed or redirected in the recency window).
3. Record any existing disavow file the user can supply (plain text, one domain/URL per line).

### Output
Confirmed domain, tier, window, lost-link flag, and any disavow file location.

---

## Phase 2: Tier-Mode Selection

### Objective
Select the data path and communicate its limitations clearly before fetching data.

### Steps
Based on the selected tier, explain the data path and its limitations:

**Free tier:**
- Use Google search operators (`link:domain`, `site:domain`) for indicative signals only.
- Parse any GSC link report CSV the user provides (Settings → Links → Export).
- Note: Free signals are incomplete and directional only. Counts will not match commercial tools.

**Ahrefs tier:**
- Call `ahrefs_api_backlinks` or equivalent endpoint with the user-supplied API key.
- Fetch: referring domains (with DR), anchors, follow/nofollow breakdown, first seen / last seen dates.

**Moz tier:**
- Call Moz Link Explorer API (`links` endpoint) with the user-supplied API key.
- Fetch: linking root domains (with DA/PA), anchor text, spam score per domain.

For all tiers, note which signals are available and which are estimated.

### Output
Data-path confirmation with field availability matrix.

---

## Phase 3: Fetch and Normalise

### Objective
Retrieve the raw link data and normalise it into a consistent schema for analysis.

### Steps
1. Execute the appropriate data fetch for the selected tier.
2. Normalise all data into a standard schema:
   - `referring_domain`, `authority_score` (DR/DA/estimated), `links_to_target`, `follow_links`, `nofollow_links`, `first_seen`, `last_seen`, `topical_category` (estimated from domain TLD/content), `spam_score` (0–100 if available).
3. If a lost-links flag was set, append a `status` column (`active` / `lost`).
4. Deduplicate entries where the same root domain appears multiple times with minor variations.

### Output
Normalised referring-domain table (top 50 by authority, or full set if under 200).

---

## Phase 4: Anchor Analysis

### Objective
Classify anchors by type and flag over-optimisation patterns. Refer to `reference.md` for the anchor taxonomy and healthy share benchmarks.

### Steps
1. Classify each anchor into one of the six categories (see `reference.md`: Branded, Exact-match, Partial-match, Generic, Naked URL, Other).
2. Calculate the percentage share of each category.
3. Flag if exact-match anchor share > 20% (over-optimisation risk).
4. Flag if generic + naked > 60% (possible link-farm or low-quality pattern).
5. Produce a histogram table sorted by category share.

### Output
Anchor-text histogram table with flags.

---

## Phase 5: Toxicity Flagging

### Objective
Score each referring domain against the toxicity indicators in `reference.md` and produce a disavow register.

### Steps
1. Score each referring domain 0–1 on each toxicity indicator (see `reference.md`).
2. Sum to a composite toxicity score.
3. Classify: 0–2 = clean, 3–5 = watch, 6–9 = toxic.
4. For all toxic-flagged domains, recommend: **disavow** (domain level) or **manual outreach** (remove request).
5. If a prior disavow file was supplied, cross-reference and note which toxic domains are already disavowed.

### Output
Toxicity register table: `referring_domain`, `authority_score`, `toxicity_score`, `trigger_indicators`, `recommended_action`.

---

## Phase 6: Report Assembly

### Objective
Compile all phase outputs into the final structured markdown report and save to disk.

### Steps
Compile all outputs into a structured markdown report:

1. **Executive Summary** — 3–5 bullet points on profile health, key risks, and priority actions.
2. **Referring-Domain Table** — top 50 domains by authority with follow/nofollow split.
3. **Authority Distribution** — band breakdown (DR/DA 0–20, 21–40, 41–60, 61–80, 81–100; see `reference.md` — *Referring-Domain Authority Distribution*) as a text histogram.
4. **Link Velocity** — if date data available, show monthly new/lost link counts as a Mermaid line chart; otherwise note data unavailability.
5. **Anchor-Text Histogram** — from Phase 4.
6. **Toxicity Register** — from Phase 5.
7. **Remediation Guidance** — disavow file block (formatted for Google Search Console upload per `reference.md` — *Google Disavow File Format*) + outreach priority list.
8. **Open Questions** — any data gaps that would change the findings.

### Output
Completed markdown report written to `backlink-audit-<domain>-<YYYY-MM-DD>.md`.

---

## Output Format

Markdown document saved to the working directory as `backlink-audit-<domain>-<YYYY-MM-DD>.md`.

---

## Behavioural Rules

1. **Never fabricate metrics.** If a data source is unavailable or returns no results, report `[N/A]` and explain why.
2. **Tier transparency.** Always tell the user what the selected tier can and cannot provide before running.
3. **Anchor flags are thresholds, not verdicts.** Flag over-optimisation patterns but note that context matters — a brand-name site will naturally have high branded anchor share.
4. **Disavow conservatively.** Only recommend disavow for domains scoring 6+ on the toxicity scale. Over-disavowing legitimate links harms rankings.
5. **Authority scores are tool-relative.** Ahrefs DR and Moz DA use different scales; never compare them directly. Label units clearly.
6. **Lost links are signal, not panic.** Link churn is normal. Flag lost links only if they represent > 15% of the profile in the recency window.
7. **Australian English throughout.** Optimise, analyse, recognise, colour.
8. **Confidence band on Free tier.** Always mark Free-tier counts with `[indicative only — Free tier]`.
9. **One disavow file, domain-level preferred.** Google recommends disavowing at the domain level (using `domain:example.com` syntax) unless the toxic pattern is isolated to a single URL.
10. **Summarise then drill.** Lead with the executive summary before presenting tables — stakeholders read the top, not the data.

---

## Edge Cases

1. **Brand-new domain with zero backlinks** → Report zero-link state. Recommend link-building priorities rather than an audit. Skip Phases 3–5.
2. **User supplies GSC link export but no paid API** → Parse the CSV, apply normalisation as best as possible, and flag column limitations (GSC export lacks authority scores).
3. **Subdomain vs root domain confusion** → Clarify with the user. Ahrefs and Moz default to root domain; if the user's property is a subdomain, re-run with the correct scope.
4. **Penalty recovery scenario** → If the user mentions a manual action or ranking drop, prioritise the toxicity register and disavow guidance, and recommend submitting a reconsideration request.
5. **Competitor comparison requested** → This skill audits one domain at a time. Direct the user to `competitor-seo-audit` for a multi-domain comparison.
6. **No API key provided for paid tier** → Prompt for the key. Do not proceed with the paid-tier path without credentials.
7. **Disavow file already very large (>500 entries)** → Warn that a bloated disavow file may be disavowing legitimate links. Recommend auditing the disavow file itself.
