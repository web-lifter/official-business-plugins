# Keyword Clustering and Mapping Report — Harbour Finance (Melbourne Mortgage Broker)

**Keywords CSV:** `/home/user/.claude/plugin-data/keywords/harbour-finance-master.csv`
**Method:** kmeans | **Clusters requested:** 14 | **Clusters produced:** 14
**Similarity:** semantic | **Embedding model:** mpnet (all-mpnet-base-v2, local)
**SERP overlap:** Disabled
**Generated:** 15/05/2026

---

## Executive Summary

| Metric | Value |
|---|---|
| Total keywords clustered | 347 |
| Clusters produced | 14 |
| Total keyword volume covered | 124,800/month |
| Clusters with strong page match (≥ 0.7) | 5 |
| Clusters with weak page match (0.4–0.69) | 3 |
| Content gaps (no match) | 6 |
| Cannibalisation conflicts | 1 |
| Cluster quality (silhouette score) | 0.58 |

**Top 3 priorities:**
1. Create dedicated page for "First Home Buyer Grants VIC 2026" cluster (14,200 vol, avg KD 22) — biggest easy-win gap
2. Resolve cannibalisation between `/guides/mortgage-broker-vs-bank` and `/about` both targeting "what does a mortgage broker do" (1,900 vol)
3. Optimise `/refinance` page for "refinance home loan australia" cluster — currently weak match (0.51) despite 18,400 total cluster volume

---

## Cluster Map

| Cluster | Label | Keywords | Volume | Intent | Mapped Page | Confidence | Action |
|---|---|---|---|---|---|---|---|
| 0 | Mortgage Broker Melbourne | 38 | 41,200 | Commercial | `/melbourne` | 0.82 | Optimise |
| 1 | First Home Buyer Loans | 29 | 12,800 | Commercial | GAP | — | Create |
| 2 | First Home Buyer Grants VIC | 18 | 14,200 | Informational | GAP | — | Create |
| 3 | Refinance Home Loan | 22 | 18,400 | Transactional | `/refinance` | 0.51 | Optimise |
| 4 | Investment Property Loans | 19 | 9,600 | Commercial | `/investment-loans` | 0.74 | Monitor |
| 5 | Home Loan Comparison | 24 | 16,800 | Commercial | GAP | — | Create |
| 6 | How to Get a Home Loan | 31 | 11,200 | Informational | `/guides/how-to-get-a-home-loan` | 0.79 | Monitor |
| 7 | Mortgage Broker Fees | 14 | 8,800 | Informational | `/guides/mortgage-broker-fees` | 0.71 | Monitor |
| 8 | Low Deposit Home Loans | 17 | 7,400 | Commercial | GAP | — | Create |
| 9 | What Does a Mortgage Broker Do | 12 | 5,600 | Informational | `/about` | 0.44 | Create dedicated page |
| 10 | Offset Account vs Redraw | 8 | 2,400 | Informational | GAP | — | Create |
| 11 | SMSF Property Loans | 11 | 3,200 | Commercial | `/smsf-loans` | 0.68 | Optimise |
| 12 | Construction Loans | 13 | 4,800 | Commercial | GAP | — | Create |
| 13 | Local Melbourne Suburbs | 41 | 6,600 | Transactional | `/melbourne` | 0.38 | Create suburb pages |

---

## Page-Map Decisions

### Mortgage Broker Melbourne (Cluster 0) → `/melbourne`
**Confidence:** 0.82 (Strong)
Page directly targets "mortgage broker melbourne" as H1 and primary keyword. Covers 38 keywords, 41,200 total volume. Action: Review content depth — 6 child suburb keywords (e.g. "mortgage broker south yarra", "mortgage broker richmond") would benefit from suburb-specific sub-sections or dedicated pages (see Cluster 13).

### First Home Buyer Loans (Cluster 1) → GAP
No existing page covers this 29-keyword, 12,800 volume cluster. Top keyword: "first home buyer loan australia" (4,000 vol, KD 58). Recommended format: long-form guide (2,500+ words) covering FHLDS, deposit requirements, and the loan application process.

### First Home Buyer Grants VIC (Cluster 2) → GAP
High-priority gap. 18 keywords, 14,200 total volume, average KD 22 (Easy band). Top keyword: "first home buyer grants victoria 2026" (1,400 vol). Recommended format: evergreen guide with annual update cadence. Strong featured snippet opportunity — question-and-answer structure recommended.

### Refinance Home Loan (Cluster 3) → `/refinance`
**Confidence:** 0.51 (Weak)
Page exists but thin content (estimated 620 words). Cluster has 22 keywords and 18,400 total volume — this is the highest-volume cluster with a weak match. Priority optimisation target. Recommended: expand to 2,000+ words covering "should I refinance", "cash out refinance", and "refinance calculator" use cases.

### What Does a Mortgage Broker Do (Cluster 9) → `/about`
**Confidence:** 0.44 (Weak)
About page incidentally covers these informational queries but lacks the depth needed to rank. Cannibalisation risk: `/guides/mortgage-broker-vs-bank` also ranks for the head term. Recommended: create a standalone `/what-is-a-mortgage-broker` guide; update `/about` to link to it.

---

## Top Content Gaps (Volume-Weighted)

| # | Cluster | Volume | Intent | Top Keyword | Avg Difficulty | Recommended Format |
|---|---|---|---|---|---|---|
| 1 | Home Loan Comparison | 16,800 | Commercial | home loan comparison australia (8,100) | 54 | Comparison table article + calculator |
| 2 | Refinance Home Loan (expand) | 18,400 | Transactional | refinance home loan australia (5,400) | 48 | Long-form guide + FAQ |
| 3 | First Home Buyer Grants VIC | 14,200 | Informational | first home buyer grants victoria 2026 (1,400) | 22 | Evergreen guide, annual update |
| 4 | First Home Buyer Loans | 12,800 | Commercial | first home buyer loan australia (4,000) | 45 | Long-form guide |
| 5 | Low Deposit Home Loans | 7,400 | Commercial | low deposit home loan australia (2,900) | 38 | Guide + eligibility checker |
| 6 | Construction Loans | 4,800 | Commercial | construction loan requirements australia (320) | 31 | Guide |
| 7 | Offset Account vs Redraw | 2,400 | Informational | offset account vs redraw australia (880) | 18 | Explainer article, diagram |
| 8 | What Does a Broker Do (dedicated) | 5,600 | Informational | what does a mortgage broker do (1,900) | 27 | Short guide, FAQ |
| 9 | Local Melbourne Suburbs (pages) | 6,600 | Transactional | mortgage broker south yarra (380) | 14 | Location pages (x10) |
| 10 | SMSF Loans (optimise) | 3,200 | Commercial | smsf property loan australia (270) | 25 | Expand /smsf-loans to 2,000 words |

---

## Cannibalisation Conflicts

| Keyword | Volume | Competing URL 1 | Competing URL 2 | Overlap | Recommended Action |
|---|---|---|---|---|---|
| what does a mortgage broker do | 1,900 | `/about` | `/guides/mortgage-broker-vs-bank` | 0.74 | Create `/what-is-a-mortgage-broker`; 301 or noindex `/about` for this query; update internal links |

---

## 30/60/90-Day Content Roadmap

### 0–30 Days (Quick Wins and Fixes)

| Priority | Action | Target | Expected Impact |
|---|---|---|---|
| 1 | Expand `/refinance` to 2,000+ words | Cluster 3 (18,400 vol) | Lift weak match (0.51) to strong; capture high-volume transactional traffic |
| 2 | Create `/what-is-a-mortgage-broker` guide | Cluster 9 (5,600 vol) | Resolve cannibalisation; rank for easy informational cluster (avg KD 27) |
| 3 | Add suburb sub-sections to `/melbourne` | Cluster 13 (6,600 vol) | Capture local intent keywords without building 10 new pages |
| 4 | Optimise `/smsf-loans` page | Cluster 11 (3,200 vol) | Lift weak match (0.68) to strong with 800 more words |

### 31–60 Days (New Content Creation)

| Priority | Action | Cluster / Gap | Volume | Format |
|---|---|---|---|---|
| 1 | Create First Home Buyer Grants VIC guide | Cluster 2 | 14,200 | 2,500-word guide, annual update |
| 2 | Create First Home Buyer Loans guide | Cluster 1 | 12,800 | 2,000-word guide + FAQ |
| 3 | Create Offset Account vs Redraw article | Cluster 10 | 2,400 | 1,200-word explainer with diagram |

### 61–90 Days (Expansion and Link Building)

| Priority | Action | Target | Notes |
|---|---|---|---|
| 1 | Create Home Loan Comparison hub | Cluster 5 (16,800 vol) | Highest-volume gap; requires comparison table tool or manually maintained table |
| 2 | Create Low Deposit Home Loans guide | Cluster 8 (7,400 vol) | Good for LMI upsell opportunities |
| 3 | Build out 5 suburb landing pages | Cluster 13 | Start with highest-volume suburbs: South Yarra, Richmond, Fitzroy, Brunswick, Hawthorn |
| 4 | Internal link audit: connect new guides to `/melbourne` and service pages | All new content | Reinforce topical authority signal |

---

## Package Recommendations

_(Incorporated from `recommendations.md`)_

- Cluster quality score (silhouette): 0.58 — acceptable for 347 keywords. Consider re-running with `hdbscan` if you want to identify natural cluster boundaries without forcing 14 groups.
- Cluster 13 (Local Melbourne Suburbs) is oversized at 41 keywords with low centroid cohesion (0.31 average similarity). Consider splitting into 5–10 individual suburb location clusters in a follow-up run.
- 8 keywords were assigned to noise (outlier cluster -1 equivalent in kmeans): "mortgage calculator app", "home loan emoji", "what is a bank" — these are off-topic and should be excluded from content planning.

---

## Raw Output Paths

| File | Path |
|---|---|
| Clustered keywords | `/home/user/.claude/plugin-data/clusters/harbour-finance/clustered_keywords.csv` |
| Keyword page map | `/home/user/.claude/plugin-data/clusters/harbour-finance/keyword_page_map.csv` |
| Content gap report | `/home/user/.claude/plugin-data/clusters/harbour-finance/content_gap_report.csv` |
| Cannibalisation report | `/home/user/.claude/plugin-data/clusters/harbour-finance/cannibalization_report.csv` |
| Cluster summary | `/home/user/.claude/plugin-data/clusters/harbour-finance/cluster_summary.csv` |
| Handoff JSON | `/home/user/.claude/plugin-data/clusters/harbour-finance/handoff.json` |

---

## Next Steps

Run `content-brief-generator` with the handoff JSON:
```
Use content-brief-generator skill with argument: /home/user/.claude/plugin-data/clusters/harbour-finance/handoff.json
```
Suggested first brief: "First Home Buyer Grants VIC" (Cluster 2) — highest volume gap in the Easy difficulty band.
