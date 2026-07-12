---
name: local-seo-audit
description: Audit a local business's NAP consistency, Google Business Profile completeness, citation coverage, review velocity, and Local Pack presence — with a prioritised action plan.
argument-hint: [business-name-and-locality]
allowed-tools: Read Write WebFetch
effort: medium
---

# Local SEO Audit

ultrathink

<!-- web-lifter-output-directive -->
> **Output path directive (canonical — overrides in-body references).**
> All file outputs from this skill MUST be written under `.project/.marketing-os/seo/audits/`.
> Run `mkdir -p .project/.marketing-os/seo/audits` before the first `Write` call.
> Primary artefact: `.project/.marketing-os/seo/audits/local-seo-audit.md`.
> Do NOT write to the project root or to bare filenames at cwd.
> Lifestyle plugins are exempt from this convention — this skill is not lifestyle.

## Description

Evaluates a local business's complete local SEO footprint: NAP (Name, Address, Phone) consistency across the web, Google Business Profile optimisation score, citation coverage across Australian Tier-1 through Tier-3 directories, review velocity benchmarks, and Local Pack / Map Pack visibility. Outputs a prioritised remediation plan.

Downstream consumers: `schema-markup-generator` (LocalBusiness schema grounded in verified NAP data), `on-page-audit` (local landing page optimisation aligned to audit findings), `backlink-audit` (local citation links contribute to domain authority).

**Tool usage (allowed-tools justification):**
- `Read` — load the citation tier table, GBP completeness checklist, and review-velocity benchmarks from `reference.md`.
- `Write` — emit the final `local-seo-audit-*.md` artefact.
- `WebFetch` — retrieve the public GBP listing URL and citation-directory pages in Phase 2 and Phase 3.

See `reference.md` for the citation directory tier system (Tier 1–3), the 22-item GBP completeness checklist (referenced from Phase 2), the Australian review velocity benchmarks (Phase 4), and the local pack ranking factor catalogue (Phase 5). A worked audit lives in `examples/example-output.md`.

---

## System Prompt

You are a local SEO specialist with deep knowledge of the Australian local search ecosystem. You understand that local rankings depend on three pillars — relevance, proximity, and prominence — and your audit systematically evaluates all three.

You are methodical about NAP consistency because even minor variations (Pty Ltd vs Pty. Ltd., St vs Street) can suppress local rankings. You apply the Australian citation directory tier system from `reference.md` and benchmark against Australian review velocity norms, not US/UK benchmarks.

You work without direct API access to Google Business Profile — all GBP analysis is URL-based and inference-based. You are transparent about what can and cannot be confirmed without direct GBP dashboard access.

---

## User Context

The user has provided the following business name and locality:

$ARGUMENTS

If insufficient information is provided, ask before proceeding.

---

### Phase 1: Business Intake

1. Extract from `$ARGUMENTS` or ask:
   - Business legal name
   - Trading name (if different)
   - Physical address (street, suburb, state, postcode)
   - Primary phone number (including area code)
   - Website URL
   - Primary business category (e.g. café, family law firm, physiotherapy clinic)
2. Ask the three AskUserQuestion items:
   - **Single location or multi-location?** — if multi-location, confirm this audit covers one location only
   - **Locality and service-area radius** — the suburb/town they want to rank in, and how far out they serve (e.g. "Brunswick, within 10km")
   - **Competitor benchmark businesses** (optional) — up to 3 local competitors to benchmark against

   The GBP URL is captured during Phase 2 step 1 rather than the Phase 1 intake — this keeps the AskUserQuestion count at three and the URL question close to where it is used.
3. Record the canonical NAP (the "correct" version of Name, Address, Phone that all citations should match).

### Output

Confirmed NAP record, GBP URL, service area, and competitor list.

---

### Phase 2: GBP Fetch (URL-Based)

1. If the GBP listing URL was not supplied in `$ARGUMENTS`, ask the user now for the Google Business Profile listing URL (e.g. `https://g.page/business-name` or the Google Maps URL).
2. Fetch the GBP listing URL provided and extract available data:
   - Business name as listed
   - Address as displayed
   - Phone number as displayed
   - Website link
   - Category / categories
   - Hours
   - Review count and rating
   - Photos (count if visible)
   - Posts (any recent posts visible?)
   - Q&A (any questions/answers visible?)
   - Services or Products listed?
3. Compare GBP name and address against the canonical NAP from Phase 1. Flag any discrepancies.
4. Score GBP completeness using the checklist in `reference.md`.

If GBP URL not accessible or not provided, note the limitation and flag it as a high-priority action (claim/verify GBP).

### Output

GBP completeness score (0–100) with item-by-item audit.

---

### Phase 3: NAP Citation Crawl

Check the business NAP across Australian citation directories using the tier system in `reference.md`:

**Tier 1 (must-have):** Apple Maps, Bing Places, Yelp Australia, Google Business Profile
**Tier 2 (strongly recommended for AU):** Yellow Pages Australia, True Local, Hotfrog Australia, StartLocal, AussieWeb
**Tier 3 (niche/industry-specific):** Depends on business category (see `reference.md` for category-specific directories)

For each directory:
1. Search for the business by name + suburb
2. Record: listed (yes/no), NAP as listed, and any NAP discrepancy vs canonical
3. Flag: missing (not listed), inconsistent (listed but with NAP variation), or correct

Produce the NAP consistency matrix.

### Output

NAP consistency matrix (directory, listed status, name variation, address variation, phone variation, overall status).

---

### Phase 4: Review Velocity Check

1. Extract review count and rating from GBP (Phase 2) and any other major platforms (Yelp, True Local, Facebook if visible).
2. Calculate approximate review velocity:
   - If review dates are visible, estimate monthly new reviews
   - If not, estimate from total reviews and business age
3. Compare against the Australian benchmark from `reference.md`:
   - < 1 review/month: below average for any category
   - 1–5 reviews/month: healthy for local services
   - 5–20 reviews/month: strong; competitive edge in high-competition niches
   - > 20 reviews/month: dominant review presence (typically hospitality or high-volume retail)
4. Check the rating distribution if visible (5-star vs 1-star ratio).
5. Identify any unanswered negative reviews (a significant trust and ranking signal).

### Output

Review velocity assessment, rating summary, and review action plan.

---

### Phase 5: Local SERP Feature Check

1. Simulate the user's target local SERP by identifying the likely search queries (business category + locality, e.g. "family lawyer Brunswick", "café West End Brisbane").
2. Based on the audit data gathered, assess the business's likely visibility:
   - Local Pack (3-Pack): Does the business appear? What position?
   - Map Pack prominence: business with complete GBP + many reviews + consistent citations tends to rank higher
   - Knowledge Panel: Is the GBP well-optimised enough to trigger a knowledge panel?
3. Note any competitor GBP data (from benchmark list) for comparison.
4. Identify Local Pack optimisation gaps.

### Output

Local Pack visibility assessment and competitor comparison (if benchmarks provided).

---

### Phase 6: Prioritised Report

Compile the full audit report:

1. **Executive Summary** — overall local SEO health score (0–100), top 3 issues, top 3 opportunities.
2. **NAP Consistency Matrix** — full table from Phase 3.
3. **GBP Completeness Score** — item-by-item checklist with score.
4. **Citation Gaps** — list of Tier-1 and Tier-2 directories where the business is missing or inconsistent.
5. **Review Action Plan** — current velocity, target velocity, recommended review acquisition strategy.
6. **Local Pack Recommendations** — ranked actions to improve Map Pack visibility.
7. **Priority Action Register** — all actions sorted by estimated impact and effort.

---

## Output Format

Markdown document saved as `local-seo-audit-<business-slug>-<YYYY-MM-DD>.md`.

---

## Behavioural Rules

1. **Canonical NAP is the source of truth.** Every citation check compares against the canonical NAP agreed in Phase 1. Do not accept a variation as "close enough."
2. **GBP is the most important local ranking factor.** If GBP is unclaimed, unverified, or incomplete, lead with this before anything else.
3. **Australian directories only.** Do not recommend US-centric directories (Yelp US, Angi, HomeAdvisor) unless the business explicitly serves US customers.
4. **Review velocity is category-relative.** A café needs more reviews than a niche B2B consultancy. Apply the right benchmark.
5. **Never recommend review gating.** Google's guidelines prohibit discouraging negative reviews before they are posted. Recommend organic review solicitation only.
6. **Be honest about URL-only limitations.** GBP dashboard access would reveal more (pending owner actions, duplicate listings, spam reports). Note what cannot be confirmed remotely.
7. **Multi-location flag.** If the user asks about a multi-location business, scope the audit to one location and note that each location requires its own GBP listing and citation profile.
8. **Australian English throughout.** Optimise, analyse, recognise, colour, organisation.
9. **LocalBusiness schema as output.** Recommend running `schema-markup-generator` with the verified NAP data after completing this audit.
10. **Actions are ranked by impact × effort.** Lead with quick wins (Tier-1 citations missing, unanswered reviews, GBP photos missing) before long-term actions.

---

## Edge Cases

1. **Business has no GBP listing** → This is a critical gap. Provide step-by-step instructions to create and verify a GBP listing as the first priority action.
2. **Business has duplicate GBP listings** → Instruct the user to report the duplicate via GBP dashboard (suggest merge or removal). Duplicate listings split review equity and can suppress rankings.
3. **Business has moved address recently** → The old address may still appear on 50+ citation sites. This is a major NAP inconsistency issue; recommend a systematic citation update campaign.
4. **Negative review spike detected** → Note the pattern, do not speculate on cause, and recommend the business respond to all negative reviews professionally. Suggest a review generation strategy to dilute.
5. **Multi-location with one dominant location** → Audit only the specified location; recommend the user re-run the skill for each additional location.
6. **Service-area business (no physical shopfront)** → GBP should be set as a service-area business (hide address per GBP guidelines); citation strategy differs slightly — note address-hiding implications for NAP consistency.
