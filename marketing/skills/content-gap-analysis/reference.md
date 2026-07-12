# Content Gap Analysis — Reference Framework

## Koray Tuğberk GÜBÜR's Topical Authority / Semantic SEO Model

### Core Thesis

Search engines evaluate a site's authority on a topic by measuring how comprehensively it covers the semantic space around that topic. A site that thoroughly addresses all related entities, attributes, and questions within a subject domain earns higher topical authority than a site targeting individual keywords in isolation.

**Implication for gap analysis:** The goal is not to find individual missing keywords — it is to find missing *topic clusters* (semantic entities) that, if covered, would extend the site's authority into new territory.

---

## Topical Coverage Framework

### Entity-Centric Approach

Each topic cluster should be treated as an *entity* with:
- A **parent topic** (the main concept)
- **Attributes** (sub-topics that define the entity)
- **Relations** (how the entity connects to adjacent entities)
- **User questions** (the specific queries users ask about this entity)

A content cluster covering one entity should answer:
1. What is it?
2. What are its types / variants?
3. How does it work?
4. How does it compare to alternatives?
5. How do you choose / buy / use it?

When all five question types are covered, the topic cluster is considered *complete*.

### Topical Map

A topical map represents all entities a site covers and their hierarchical relationships:

```
Main Topic (Root Entity)
├── Sub-topic A (Entity)
│   ├── Sub-topic A1
│   └── Sub-topic A2
├── Sub-topic B (Entity)
│   ├── Sub-topic B1
│   └── Sub-topic B2
└── Sub-topic C (Entity)
```

Gap analysis identifies which branches of this map competitors have covered that the target site has not.

---

## Content-Cluster Theory

### Hub-and-Spoke Model

- **Hub page** (pillar): covers the parent topic comprehensively; targets high-volume, broad-intent keyword; links to all spoke pages
- **Spoke pages** (cluster members): cover specific attributes or sub-topics; target long-tail, specific-intent keywords; link back to the hub

**Cluster completeness rule:** A cluster provides maximum ranking benefit when all spokes are published and internally linked to the hub. Publishing spokes without a hub is less effective than publishing a strong hub alone.

### Cluster Sizing Guidelines

| Cluster size | Target | Notes |
|---|---|---|
| 1 page | Single-question topics (e.g. "what is stamp duty") | Suitable for FAQ or supporting content |
| 2–4 pages | Sub-topic clusters | Hub + 1–3 spokes |
| 5–10 pages | Full topic clusters | Hub + multiple spokes with comparison/how-to content |
| 10+ pages | Topic authority clusters | Reserved for core business topics; high investment |

---

## Opportunity Scoring Components

### Volume Score

- Use monthly search volume from DataForSEO, Ahrefs, or Google Keyword Planner
- Cluster volume = sum of volumes for hub keyword + top 5 member keywords
- Normalise across all clusters in the gap set to a 0–1 scale

### Difficulty Inverse Score

- Keyword Difficulty (KD) is typically 0–100 (Ahrefs scale) or 0–100 (DataForSEO)
- Difficulty Inverse = (100 − KD) / 100
- Low difficulty = high score = easier to rank

### Position Gap Score

- Measures how well competitors are ranking for the cluster's keywords
- Average competitor position for cluster keywords (1–100)
- Position gap score = (100 − avg_competitor_position) / 100
- Interpretation: if competitors rank at position 3 on average, there is a large gap (position gap score ≈ 0.97); if they rank at position 85, the gap is small (score ≈ 0.15)

---

## Keyword Classification Rules

### Branded Terms (Always Exclude from Gap Set)

- Contain a competitor's brand name
- Contain a competitor's product name or trademark
- Examples: "Nike running shoes", "Ahrefs vs Semrush"

### Navigational Queries (Exclude from Gap Set)

- Contain: login, sign up, register, contact, careers, jobs, download, pricing
- Indicate user is navigating to a specific site, not seeking information

### Informational Queries (High Priority for Content Gap)

- "How to", "what is", "guide", "tutorial", "tips"
- Best suited for blog posts, guides, FAQs
- Generally lower difficulty; strong topical authority signal

### Commercial Investigation Queries (High Priority for Content Gap)

- "Best", "top", "vs", "review", "compare", "alternative"
- Suited for comparison posts, listicles, reviews
- Users are pre-purchase; high conversion intent

### Transactional Queries (Lower Priority for Content Gap — Generally Covered by Category/Product Pages)

- "Buy", "order", "price", "cheap", "discount", "near me"
- Usually covered by existing product or service pages

---

## Content Angle Frameworks

### Angle Selection by Intent

| Intent | Recommended Angle |
|---|---|
| Informational | Definitive guide / FAQ / glossary |
| Commercial Investigation | Best-of roundup / comparison / review |
| Transactional | Category landing page / product guide |
| Navigational | Brand or feature page |

### Differentiation from Competitors

Before recommending an angle, check what competitors have already published for the cluster:
- If competitors use basic guides → produce a more comprehensive guide with original data
- If competitors use roundups → produce a comparison with unique scoring methodology
- If competitors have thin content → produce a deep-dive with expert quotes and examples

---

## Key References

- Koray Tuğberk GÜBÜR: "Topical Authority in SEO" (Holistic SEO blog series)
- DataForSEO API documentation: Ranked Keywords endpoint
- Ahrefs Content Gap tool methodology
- Google Quality Rater Guidelines — E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)
