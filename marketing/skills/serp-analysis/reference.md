# SERP Analysis — Reference

## SERP Feature Taxonomy

The following features may appear on a Google SERP. Detection is via SerpAPI response fields.

| Feature | SerpAPI Field | Description | Rankability for New Sites |
|---|---|---|---|
| **Featured Snippet** | `answer_box` / `featured_snippet` | Direct answer box above organic results. Pulled from an existing top-10 result. | High — captured by optimising an existing page, not requiring high authority |
| **People Also Ask (PAA)** | `related_questions` | Expandable Q&A boxes. Each answer is pulled from a ranked page. | High — FAQ schema + direct Q&A format improves chances |
| **Local Pack** | `local_results` | Map + 3 business listings. Triggered by local intent. | Medium — requires Google Business Profile + local SEO |
| **Image Pack** | `images_results` | Horizontal image strip inline. Triggered by visual queries. | Medium — requires image optimisation + alt text |
| **Video Pack** | `videos_results` | Horizontal video carousel. | Low-Medium — requires YouTube presence |
| **Knowledge Panel** | `knowledge_graph` | Right-side entity box. Typically for brands, people, places. | Low — editorial, not rankable |
| **Shopping / PLAs** | `shopping_results` | Product listing ads (paid). | N/A — paid feature |
| **Top Stories** | `top_stories` | News carousel. Requires Google News inclusion. | Low for non-publishers |
| **Reviews / Star Ratings** | `reviews` attribute in organic | Star ratings in organic results. Requires Review schema. | High — add Review schema to eligible pages |
| **Sitelinks** | `sitelinks` | Sub-links under a brand result. Typically for branded queries. | Low — granted algorithmically |
| **AI Overview** | `ai_overview` | Generative AI summary above organic results. Sources cited. | Medium — cited sources tend to be top-10 pages with clear direct answers |
| **Answer Box** | `answer_box` | Simple factual answer (calculator, definition, conversion). | Low — requires being the definitional source |

---

## Backlinko Search Intent Matrix

### Primary Intents

| Intent | Description | SERP Signals |
|---|---|---|
| **Informational** | User wants to learn | Articles, guides, Wikipedia, Q&A sites dominate |
| **Navigational** | User wants to reach a site | Brand result #1, sitelinks |
| **Commercial** | User is researching before buying | Comparison posts, reviews, "best X" lists, aggregators |
| **Transactional** | User is ready to convert | eCommerce PLPs/PDPs, service landing pages, Local Pack |

### Sub-Intent Matrix

| Sub-Intent | Parent Intent | Trigger Phrases | Typical Result Format |
|---|---|---|---|
| How-to | Informational | "how to", "how do I" | List-based article, video |
| Definition | Informational | "what is", "define", "meaning" | Featured Snippet, Wikipedia |
| Guide | Informational | "guide", "tutorial", "explained" | Long-form article |
| Example | Informational | "example", "template", "sample" | Article with lists |
| Best | Commercial | "best", "top", "leading" | Listicle, roundup |
| Compare | Commercial | "vs", "versus", "difference between" | Comparison article, table |
| Review | Commercial | "review", "is it worth it", "pros cons" | Review article |
| Buy | Transactional | "buy", "price", "shop", "discount" | PLP, PDP, Shopping ads |
| Hire | Transactional | "hire", "near me", "find a", "book" | Local Pack, service pages |
| Navigational/Brand | Navigational | Brand name primary | Sitelinks SERP |

---

## SERP Volatility Scoring

Volatility indicates how often the ranking order changes. High volatility = opportunity for newcomers.

| Rating | Signals |
|---|---|
| **High** | >6 different root domains in top 10; mix of high and low DR sites; fresh content (<6 months) in top 5 |
| **Medium** | 4–6 domains; moderate authority range; results relatively stable |
| **Low** | <4 domains; dominated by DR 70+ authoritative sites; results appear static |

High volatility SERPs reward fresh, comprehensive content. Low volatility SERPs require authority-building (links) before ranking is achievable.

---

## Content Format Classification

Use these labels when categorising organic results:

| Format | Description | Word Count Signal |
|---|---|---|
| `Article` | General editorial content, typically informational | 800–2,500 words |
| `Guide` | Comprehensive long-form tutorial or explainer | 2,000–5,000 words |
| `Listicle` | "10 best X" or numbered list format | 1,500–3,000 words |
| `Product Page` | eCommerce product detail page | 300–1,000 words |
| `Category Page` | eCommerce product listing page | 500–1,500 words |
| `Forum / UGC` | Reddit, Quora, community answers | Variable |
| `Video` | YouTube or embedded video page | Short text, primary video content |
| `Tool / Calculator` | Interactive utility with supporting content | 500+ words around tool |
| `News` | Time-sensitive news article | 300–1,200 words |
| `Local Landing Page` | Geographically targeted service page | 600–1,500 words |

---

## Featured Snippet Optimisation Rules

To maximise Featured Snippet capture probability:

1. **Provide a direct answer in ≤ 40 words** immediately following the target H2.
2. **Use the question as the H2** (or a close variant).
3. **Follow the answer with supporting detail** — the snippet takes the short answer, the page keeps the user.
4. **For "how to" snippets:** use a numbered list (Google pulls numbered steps).
5. **For "what is" snippets:** use a one-sentence definition, then expand.
6. **For comparison snippets:** use a table — Google often renders table snippets.
7. **The page must already rank in the top 10** — featured snippets are pulled from ranked results.

---

## AI Overview Signals (Current)

- AI Overviews appear more frequently for informational and "how to" queries in Australia (en-AU).
- Sources cited tend to be top-3 organic results with clear, structured answers.
- Pages cited in AI Overviews typically have: FAQ schema, short direct answers, authoritative domain signals.
- Optimising for AI Overview citation: same principles as Featured Snippet, plus breadth of topic coverage on the page.
- Monitor: AI Overview presence is volatile — it may appear/disappear for the same query on different days.
