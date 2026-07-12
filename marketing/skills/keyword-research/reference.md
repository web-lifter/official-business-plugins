# Keyword Research — Reference

## Ahrefs Parent Topic Model

The **Parent Topic** is the broadest keyword that, if ranked for, would likely satisfy the same searcher need as the child keyword. It is determined by examining which keyword Google uses as the "umbrella" for a cluster of related queries — typically identifiable because the same URL ranks for all of them.

**Rules for assigning parent topic:**
1. The parent topic must be a real keyword (not an invented category label).
2. A parent topic can have only one level of hierarchy in this model (no grandparents).
3. If a keyword could be its own parent (high volume, broad intent), it IS the parent topic.
4. Child keywords are variations, long-tails, or sub-intents of the parent.

**Example:**
| Parent Topic | Child Keywords |
|---|---|
| running shoes australia | best running shoes australia, cheap running shoes australia, running shoes for flat feet australia, buy running shoes online australia |
| how to run faster | how to run faster tips, how to run faster for beginners, how to improve running speed |

---

## Backlinko Search Intent Matrix

### Primary Intents

| Intent | Definition | Signals |
|---|---|---|
| **Informational** | User wants to learn something | "how to", "what is", "why does", "guide", "tips", question phrasing |
| **Navigational** | User wants to reach a specific site or page | Brand names, "login", "contact", "[brand] website" |
| **Commercial** | User is researching before a purchase decision | "best", "review", "vs", "top", "compare", "[category] for [use case]" |
| **Transactional** | User is ready to take action (buy, sign up, download) | "buy", "price", "cheap", "discount", "near me", "hire", "book" |

### Sub-Intent Lookup Table

| Sub-Intent | Parent Intent | Trigger Patterns | Typical SERP Format |
|---|---|---|---|
| How-to | Informational | "how to", "how do I", "steps to" | List articles, videos, featured snippets |
| Definition | Informational | "what is", "meaning of", "define" | Featured snippet, Knowledge Panel |
| Example | Informational | "example of", "sample", "template" | Article, tool page |
| Guide | Informational | "guide", "tutorial", "walkthrough", "explained" | Long-form article |
| Best | Commercial | "best", "top", "leading", "recommended" | Listicle, comparison article |
| Compare | Commercial | "vs", "versus", "compared to", "difference between" | Comparison table article |
| Review | Commercial | "review", "reviews", "is [X] worth it", "pros and cons" | Review article, aggregator |
| Buy | Transactional | "buy", "order", "purchase", "shop", "deal", "discount" | eCommerce PLP/PDP, Google Shopping |
| Hire | Transactional | "hire", "find a", "near me", "local", "book a" | Local Pack, service page |
| Navigational/Brand | Navigational | Brand name as primary term | Sitelinks SERP, direct brand result |

### Mixed Intent Handling
Some keywords carry two strong intents simultaneously. Flag these as `[MIXED INTENT]` and use the sub-intent column to record both. Example: "best mortgage broker Melbourne" is Commercial/Best + Transactional/Hire.

---

## Difficulty Banding

Difficulty scores are sourced from DataForSEO or Ahrefs Keyword Difficulty (KD). They represent the estimated effort required to rank on page 1 organically, on a 0–100 scale.

| Band | Score Range | Interpretation | Typical Competitor Profile |
|---|---|---|---|
| **Easy** | 0–30 | Low competition; achievable with moderate domain authority and good on-page SEO | Few or no authoritative sites targeting exact match; thin SERP |
| **Medium** | 31–60 | Moderate competition; requires quality content + some link building | Mix of established blogs and niche sites; some DR 40–60 domains |
| **Hard** | 61+ | High competition; requires significant authority and link acquisition | Major publishers, aggregators, high-DR domains dominating SERP |

**Quick Win definition:** volume ≥ volume floor AND difficulty ≤ 30. These are the highest-priority targets for new or low-authority sites.

---

## API Reference

### SerpAPI — Useful Endpoints

| Endpoint | Purpose | Key Parameters |
|---|---|---|
| `GET /search` | Organic results + related searches + PAA | `q`, `gl` (country), `hl` (language), `num` |
| Related searches | Extracted from response `.related_searches[].query` | — |
| PAA | Extracted from response `.related_questions[].question` | — |

**Locale codes for Australia:** `gl=au&hl=en`

### DataForSEO — Useful Endpoints

| Endpoint | Purpose | Key Parameters |
|---|---|---|
| `POST /keywords_data/google_ads/search_volume/live` | Monthly search volume | `keywords[]`, `location_code` (2036 = AU), `language_code` (en) |
| `POST /keywords_data/google_ads/keywords_for_keywords/live` | Keyword suggestions | `keywords[]`, `location_code`, `language_code` |
| `POST /keywords_data/keyword_difficulty/live` | Keyword difficulty score | `keywords[]`, `location_code`, `language_code` |

**Australian location code:** `2036`
**Language code:** `en`

---

## CSV Output Schema

The canonical output CSV for `keyword-research` has these columns (order must be preserved for downstream compatibility):

| Column | Type | Description |
|---|---|---|
| `keyword` | string | Normalised keyword (lowercase) |
| `volume` | integer | Monthly search volume (average 12-month) |
| `difficulty` | integer | Keyword difficulty score 0–100 |
| `difficulty_band` | string | Easy / Medium / Hard |
| `intent` | string | Informational / Navigational / Commercial / Transactional |
| `sub_intent` | string | Sub-intent from matrix above |
| `parent_topic` | string | Parent topic keyword |
| `source` | string | serpapi-related / serpapi-paa / dataforseo-suggest / dataforseo-volume |
| `mixed_intent` | boolean | true if keyword spans two primary intents |

This schema is compatible with `keyword-list-developer` which adds: `current_url`, `serp_features`.
