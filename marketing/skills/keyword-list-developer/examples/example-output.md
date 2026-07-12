# Keyword Master List — Harbour Finance (Melbourne Mortgage Broker)

**Market / Locale:** en-AU
**Volume Floor:** 50 searches/month
**Maximum List Size:** 500
**Include Branded:** Yes (segregated)
**Research Date:** 15/05/2026
**CSV saved to:** `/home/user/.claude/plugin-data/keywords/harbour-finance-master.csv`

---

## Summary

| Metric | Value |
|---|---|
| Total keywords in master list | 347 |
| Raw candidates (pre-filter) | 1,842 |
| Removed (volume < 50/month) | 891 |
| Removed (off-topic) | 73 |
| Removed (duplicates) | 531 |
| Sources used | serpapi-related, serpapi-paa, dataforseo-suggest, dataforseo-site, dataforseo-volume, gsc-top-queries, competitor-ratecity.com.au, competitor-loans.com.au, llm-semantic |

### By Intent

| Intent | Count | % of Total |
|---|---|---|
| Informational | 89 | 26% |
| Commercial | 142 | 41% |
| Transactional | 98 | 28% |
| Navigational (incl. branded) | 18 | 5% |

### By Difficulty Band

| Band | Count |
|---|---|
| Easy (0–30) | 68 |
| Medium (31–60) | 187 |
| Hard (61+) | 79 |
| Unknown / Estimated | 13 |

---

## Top 10 by Volume

| # | Keyword | Volume | Difficulty | Intent | Parent Topic | Current URL |
|---|---|---|---|---|---|---|
| 1 | mortgage broker melbourne | 9,900 | 72 | Transactional | mortgage broker melbourne | /melbourne |
| 2 | home loan comparison australia | 8,100 | 68 | Commercial | home loan comparison | |
| 3 | best mortgage broker melbourne | 6,600 | 65 | Commercial | mortgage broker melbourne | |
| 4 | refinance home loan australia | 5,400 | 61 | Transactional | refinance home loan | |
| 5 | mortgage broker fees australia | 4,400 | 44 | Informational | mortgage broker fees | |
| 6 | first home buyer loan australia | 4,000 | 58 | Commercial | first home buyer loan | |
| 7 | how to get a home loan australia | 3,600 | 35 | Informational | how to get a home loan | /guides/how-to-get-a-home-loan |
| 8 | investment property loan australia | 3,200 | 55 | Commercial | investment property loan | |
| 9 | low deposit home loan australia | 2,900 | 42 | Commercial | low deposit home loan | |
| 10 | mortgage broker vs bank australia | 2,400 | 31 | Informational | mortgage broker vs bank | |

---

## Top 10 Quick Wins (Volume ≥ 50, Difficulty ≤ 30)

| # | Keyword | Volume | Difficulty | Intent | Parent Topic |
|---|---|---|---|---|---|
| 1 | mortgage broker vs bank australia | 2,400 | 31 | Informational | mortgage broker vs bank |
| 2 | what does a mortgage broker do | 1,900 | 27 | Informational | what does a mortgage broker do |
| 3 | do mortgage brokers charge fees australia | 1,600 | 24 | Informational | mortgage broker fees |
| 4 | first home buyer grants victoria 2026 | 1,400 | 19 | Informational | first home buyer grants victoria |
| 5 | how long does home loan approval take | 1,100 | 22 | Informational | how to get a home loan |
| 6 | offset account vs redraw australia | 880 | 18 | Informational | offset account vs redraw |
| 7 | lenders mortgage insurance explained | 740 | 21 | Informational | lenders mortgage insurance |
| 8 | mortgage broker inner north melbourne | 390 | 14 | Transactional | mortgage broker melbourne |
| 9 | construction loan requirements australia | 320 | 28 | Informational | construction loan |
| 10 | smsf property loan australia | 270 | 25 | Commercial | smsf property loan |

---

## Selected Cluster Previews

### mortgage broker melbourne (41,200 total volume, 38 keywords)

Top keywords: mortgage broker melbourne (9,900), best mortgage broker melbourne (6,600), independent mortgage broker melbourne (1,200), mortgage broker south yarra (380), mortgage broker richmond melbourne (290), fee-free mortgage broker melbourne (210) …

### home loan informational (18,400 total volume, 54 keywords)

Top keywords: how to get a home loan australia (3,600), mortgage broker fees australia (4,400), what does a mortgage broker do (1,900), how long does home loan approval take (1,100), offset account vs redraw australia (880) …

### first home buyer (12,800 total volume, 29 keywords)

Top keywords: first home buyer loan australia (4,000), first home buyer grants victoria 2026 (1,400), first home owner grant requirements vic (890), stamp duty concession first home buyer vic (760) …

### refinance (9,600 total volume, 22 keywords)

Top keywords: refinance home loan australia (5,400), should i refinance my home loan (1,100), best time to refinance home loan australia (880), refinance cash out australia (620) …

---

## Data Quality Notes

**Estimated volume records:** 13 keywords (LLM-semantic expansion — marked `-1` in CSV; manually verify before prioritising)
- "mortgage broker outer eastern suburbs melbourne" — estimated ~80/month
- "smsf limited recourse borrowing arrangement broker" — estimated ~60/month

**Off-topic exclusions:** 73 removed
- "mortgage calculator" variants (14) — high volume but pure tool/navigational, no content opportunity for broker
- US-locale mortgage terms (31) — locale mismatch, AU volumes < 50
- "mortgage meaning" (1) — definition query, outside broker's content scope
- Other off-topic: finance unrelated to property (27)

**Missing difficulty:** 13 keywords (LLM-semantic expansion rows; `-1` in CSV)

**Missing SERP features:** 297 keywords (sampled top 50 only; full SERP feature data available via `serp-analysis` for priority terms)

**GSC data:** Connected — 127 keywords contributed from GSC top queries (last 3 months, impressions ≥ 100)

**Competitor extraction:** ratecity.com.au (112 keywords), loans.com.au (94 keywords) — significant overlap with DataForSEO data; 86 net-new keywords from competitor extraction

---

## Handoff Note

Master list ready. Run `keyword-clustering-and-mapping` with:

```bash
keyword-cluster run \
  --keywords /home/user/.claude/plugin-data/keywords/harbour-finance-master.csv \
  --pages pages.csv \
  --method kmeans \
  --auto-k silhouette \
  --output /home/user/.claude/plugin-data/clusters/harbour-finance/
```

Or use the `keyword-clustering-and-mapping` skill which will handle method selection interactively.

**Recommendation:** Given 347 keywords across identifiable informational, commercial, and local intent clusters, `kmeans` with 12–15 target clusters is the suggested starting point. Consider `hdbscan` if you want the package to determine cluster count automatically.
