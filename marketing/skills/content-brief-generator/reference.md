# Content Brief Generator — Reference Framework

## Brief Structure

A complete editorial brief contains these sections in order:

1. Brief header (keyword, cluster, funnel stage, date, assignee)
2. Target audience summary
3. SERP intent and format signals
4. Title proposals + recommended slug
5. Meta description
6. Full heading structure (H1–H3)
7. Section-by-section guidance (purpose, keywords to use, min word count)
8. PAA questions to answer
9. Internal link plan (from/to)
10. External citation targets
11. Image and media recommendations
12. Schema markup recommendation
13. Word-count target + section allocation
14. E-E-A-T signals required
15. On-page SEO checklist

---

## SERP Intent Classification

| Intent | Query Signals | Typical SERP Format | Content Type |
|---|---|---|---|
| Informational | "what is", "how to", "guide", "tips", "why" | Long-form guides, FAQs, featured snippets | Guides, tutorials, glossaries |
| Commercial Investigation | "best", "top", "vs", "review", "compare", "alternative" | Listicles, comparison tables, reviews | Round-ups, comparisons |
| Transactional | "buy", "price", "cheap", "order", "near me" | Product pages, local results | Landing pages, product pages |
| Navigational | Brand name, "login", "contact" | Brand website | Not usually targeted |

---

## Heading Structure Guidelines

### H1
- Contains the primary keyword (naturally)
- Matches the page's topic promise exactly
- Under 60 characters preferred (displays fully in SERP)
- One H1 per page

### H2
- Represents a major topic section
- Should map to a reader question or a member keyword from the cluster
- Can contain secondary keywords naturally
- Minimum 150 words per H2 section

### H3
- Drill-down within an H2 section
- Use for steps, sub-categories, or specific sub-questions
- Avoid more than 2 levels of nesting (H1 → H2 → H3 is sufficient for most content)

### FAQ Section
- Use H2 for "Frequently Asked Questions"
- Each PAA question becomes an H3
- Answers should be 40–60 words for Featured Snippet eligibility
- Longer answers can follow but the opening 40–60 words should stand alone

---

## Word-Count Targets by Funnel Stage and Format

| Funnel Stage | Format | Target Word Count |
|---|---|---|
| TOFU | FAQ / Glossary | 800–1,200 |
| TOFU | Informational Guide | 1,500–2,500 |
| TOFU | Pillar / Comprehensive Guide | 3,000–5,000 |
| MOFU | Comparison / Review | 1,500–2,500 |
| MOFU | Round-up (Top 10 style) | 2,000–3,500 |
| BOFU | Product/Service Landing Page | 800–1,500 |
| BOFU | Case Study | 1,000–2,000 |

**Word-count allocation rule:** Break total word count across H2 sections proportionally to section importance. The intro and conclusion together should be < 15% of total.

---

## Internal Link Plan Framework

### Pages That Should Link TO the New Page

Priority sources for incoming internal links:
1. The hub/pillar page of the cluster this page belongs to
2. Related cluster members that are already published
3. High-authority pages (most external inbound links) that are topically adjacent
4. Category/archive pages
5. Homepage (for pillar pages only)

### Pages This New Page Should Link TO

Priority targets for outgoing internal links:
1. Hub page of the cluster (spoke → hub link)
2. Product or service pages relevant to the topic (monetisation pathway)
3. Related cluster members (cross-linking within cluster)
4. Glossary or definition pages for technical terms introduced

### Anchor Text Rules

- Use descriptive, specific anchor text that describes the destination page's topic
- Do not use "click here", "read more", or generic anchors
- Do not use the exact target keyword of the destination page every time — vary with synonyms and related phrases
- Maximum 1 exact-match anchor per target page across the site

---

## Schema Markup Recommendation Matrix

| Page Type | Recommended Schema |
|---|---|
| How-to guide | HowTo |
| FAQ / PAA content | FAQPage |
| Product comparison | Product + Review + AggregateRating |
| Review article | Review |
| News/announcement | NewsArticle |
| Recipe | Recipe |
| Local business landing page | LocalBusiness + Service |
| Event | Event |
| Informational guide (generic) | Article or BlogPosting |
| E-commerce category | ItemList |

**Stacking note:** Multiple schema types can be applied to one page. E.g., a guide with a FAQ section can use both `Article` and `FAQPage`.

---

## E-E-A-T Signal Checklist

**Experience** — Has the author / site done or tested this first-hand?
- Original photographs or screenshots of the product/process
- "I tested", "we compared", "in our experience" statements
- Dates of testing/research

**Expertise** — Does the author have domain credentials?
- Author bio with relevant qualifications or job title
- Credentials displayed inline (e.g. "As a registered financial adviser…")
- Citations of peer-reviewed or industry-standard sources

**Authoritativeness** — Is the site recognised by others in the field?
- Links from industry publications and associations
- Awards, certifications, or membership bodies noted
- Guest coverage or media mentions referenced

**Trustworthiness** — Can the reader verify the claims?
- All statistics cited with source and date
- Affiliate/sponsored disclosures where required
- Privacy policy, contact details, physical address (for local businesses)

### YMYL Topics (Your Money or Your Life)

For pages touching health, finance, legal, or safety:
- **Require named author** with credentials
- **Require medical/legal/financial professional review** — note in brief
- **Require citations to .gov.au, .edu.au, or peer-reviewed sources**
- **Require disclaimer** ("This is general information only…")

---

## AusE Tone Calibration

Australian English defaults:
- Spelling: optimise, analyse, recognise, colour, behaviour, organisation, programme (vs program for software)
- Currency: AUD, A$, or $ with Australian context stated; never assume USD
- Dates: DD/MM/YYYY format
- Measurements: metric (km, kg, cm, °C)
- Localisation cues: state-specific references (VIC, NSW, QLD, etc.) add local SEO signals
- Tone: Australians respond well to direct, unpretentious language; avoid hyperbolic American marketing style ("revolutionary", "game-changing")

---

## Key References

- Google Quality Rater Guidelines (E-E-A-T framework)
- Google Search Central: How to Write Titles and Descriptions
- schema.org — FAQPage, HowTo, Article specifications
- Koray Tuğberk GÜBÜR: Semantic Content Brief methodology
