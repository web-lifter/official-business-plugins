# Internal Linking Planner — Reference Framework

## Hub-and-Spoke Model

### Structure

```
Homepage
├── Hub Page A (Cluster A Pillar)
│   ├── Spoke A1
│   ├── Spoke A2
│   └── Spoke A3
├── Hub Page B (Cluster B Pillar)
│   ├── Spoke B1
│   └── Spoke B2
└── Hub Page C (Cluster C Pillar)
    ├── Spoke C1
    ├── Spoke C2
    └── Spoke C3
```

### Definitions

- **Hub (Pillar) page:** Covers the parent topic comprehensively. Broad, high-volume keyword. Links to all spoke pages. Receives the most internal links.
- **Spoke page:** Covers a specific sub-topic or attribute. Long-tail keyword. Links back to the hub. May link to closely related spokes.
- **Cross-cluster link:** Hub-to-hub links connecting adjacent topic clusters. Used sparingly for genuinely related parent topics.
- **Standalone page:** A page that doesn't fit neatly into a cluster (e.g. About, Contact, Privacy Policy). Not part of the cluster topology.

### Why It Works for SEO

1. Topical authority signalling: a hub receiving spoke links tells search engines the hub page is the authority on the cluster topic
2. Equity distribution: the hub passes PageRank to all spokes, ensuring cluster members get discovered and ranked
3. User experience: readers can navigate from a specific sub-topic to the comprehensive guide naturally

---

## Anchor-Text Best Practice

### The Right Anchor Text

- **Descriptive:** tells the reader what they'll find on the target page
- **Varied:** don't use the exact same anchor for every link to the same target
- **Natural:** fits the surrounding sentence grammatically without feeling inserted

### Anchor Distribution for a Target Page

| Anchor Type | Recommended Share of Total Links |
|---|---|
| Primary keyword (exact) | 1 link maximum across whole site |
| Keyword variants / synonyms | 30–40% of inbound internal links |
| Descriptive phrase (not keyword) | 30–40% |
| Partial keyword + context | 20–30% |
| Branded or navigational | < 10% |

### Anchors to Avoid

- "click here" / "read more" / "here" / "this article" — no topical signal
- Exact-match keyword repeated on every link — triggers over-optimisation signals
- Truncated URLs as anchors

---

## Link-Depth Principle

### The 3-Click Rule

Every page that has:
- External backlinks pointing to it, OR
- Commercial or conversion value (product pages, service pages, contact page)

…should be reachable from the homepage in 3 clicks or fewer.

**Why:** Google's crawl budget is finite. Pages buried 4–6 clicks from the homepage may be crawled less frequently, and link equity from the homepage diminishes with each additional hop.

### Link Depth by Page Type

| Page Type | Target Click Depth | Rationale |
|---|---|---|
| Homepage | 0 | Entry point |
| Category / Hub pages | 1–2 | Core SEO value |
| Product / Service pages | 2–3 | Conversion pages |
| Blog posts / Guides (high value) | 2–3 | Earns links; topical authority |
| Blog posts (supporting content) | 3–4 | Acceptable for spokes |
| Tag / Archive pages | 3–5 | Low priority |
| Utility pages (About, Contact) | 1–2 | Trust signals |

---

## PageRank Flow Intuition

PageRank distributes a page's authority equally among all outgoing links. Key implications:

1. **Fewer outbound links = more equity per link.** A page with 5 outbound links passes more equity per link than one with 50.
2. **Navigation links dilute equity.** If the header navigation links to 30 pages on every page, those links pass very little equity each.
3. **High-authority hub pages are the most valuable linkers.** A single contextual link from a well-linked hub page is worth more than 10 links from thin spoke pages.
4. **Orphan pages receive zero internal equity.** A page with no internal links cannot benefit from the site's PageRank flow, no matter how good its content is.

### Practical Rules

- Use contextual body links (within article content) for equity passing — these are more valuable than header/footer links
- Don't link from low-quality or thin pages to high-value pages expecting equity to flow
- Consolidate or redirect thin pages rather than linking to them extensively

---

## Orphan Page Definition

An orphan page is a page that:
- Is in the sitemap (crawlable, indexable) **but** receives no internal links from other pages, OR
- Receives internal links **but** is not in the sitemap (may be accidentally excluded from indexing)

### Orphan Detection Method

1. Pull all URLs from sitemap → set S
2. Pull all URLs that are targets of internal links on the site → set L
3. Orphans in sitemap = S − L (pages in sitemap but not linked to internally)
4. Linked-but-excluded = L − S (linked to but not in sitemap — check index status)

### Orphan Remediation Priority

| Page Type | Priority | Action |
|---|---|---|
| Has external backlinks | Critical | Add internal links immediately |
| Has conversion value | High | Add to nearest hub as spoke |
| Thin / low quality | Medium | Evaluate: update + add links, or 301 redirect |
| Duplicate / near-duplicate | Low | Consolidate with canonical |

---

## Key References

- Google Search Central: Internal Linking Best Practices
- HubSpot: Topic Cluster Model (original hub-and-spoke SEO framework)
- Screaming Frog SEO Spider: internal link matrix export
- Ahrefs Site Audit: orphan page and link-depth reports
