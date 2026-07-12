# Backlink Audit — Reference Framework

## SEO Backlink Quality Signals

### Referring-Domain Authority Distribution

Authority banding (Ahrefs DR / Moz DA scale 0–100):

| Band | Label | Interpretation |
|---|---|---|
| 0–20 | Low authority | Minimal equity value; common in spam profiles |
| 21–40 | Below average | Small sites, local directories; some value |
| 41–60 | Average | Established niche sites; solid equity |
| 61–80 | High authority | Major niche publications, large brands |
| 81–100 | Elite | Wikipedia, BBC, major news; high value |

Healthy profile benchmark:
- > 30% of referring domains in the 41+ band
- < 10% of referring domains at 0–10 (very low authority)
- Authority distribution should be roughly bell-curved, not bottom-heavy

---

## Anchor-Text Diversity Framework

### Anchor-Text Taxonomy

| Type | Definition | Healthy Share |
|---|---|---|
| Branded | Brand name, domain name, or brand variant | 40–60% |
| Exact-match | Primary target keyword verbatim | < 5% (natural sites) / < 20% (aggressive) |
| Partial-match | Keyword variant or synonym | 10–20% |
| Generic | "click here", "here", "read more", "visit", "website" | 5–15% |
| Naked URL | Raw URL as anchor | 10–25% |
| Other / image | Image alt text, empty, miscellaneous | < 10% |

### Over-Optimisation Flags

- Exact-match anchor > 20% → Penguin-pattern risk; flag for review
- Exact-match anchor > 30% → Strong over-optimisation signal
- Generic + naked < 10% combined → Unusually editorial; may indicate purchased links
- Zero branded anchors on a named brand → Suspect profile

---

## Follow / Nofollow Split

| Signal | Interpretation |
|---|---|
| > 90% follow | Possible link scheme; natural profiles include nofollow |
| 60–80% follow | Normal for editorial content |
| < 40% follow | Heavy social/UGC sourcing; low equity value overall |

---

## Link Velocity

- **Normal organic growth**: slow, steady increase over months/years
- **Velocity spike**: > 2× average monthly new links in a single month
  - Investigate: press release, viral content, or link scheme
- **Sudden drop**: > 50% loss of referring domains in 30 days
  - Investigate: penalty, domain change, mass deindex of linking site
- **Steady decline with no gains**: profile erosion; link-building investment needed

---

## Topical Relevance

- Links from topically relevant domains carry higher equity than off-topic links
- Relevance signals: TLD pattern (e.g., `.edu`, `.gov`), domain name keywords, anchor context
- Off-topic > 70% of profile → possible link network or irrelevant link buying

---

## Toxicity Indicators (PBN / Spam Footprints)

Score each referring domain on the following indicators (0 = absent, 1 = present):

| Indicator | Score |
|---|---|
| Moz spam score ≥ 60 | 1 |
| DR/DA < 5 with > 1,000 outbound links | 1 |
| Exact-match keyword domain pointing to money page | 1 |
| Thin / auto-generated content on linking page | 1 |
| Link from footer or sitewide link | 1 |
| Hosting on same IP range as > 10 other linking domains | 1 |
| Sudden acquisition (first seen within 7 days of link) | 1 |
| Casino / pharma / adult content category | 1 |
| Site indexed but no organic traffic (SEMrush/Ahrefs) | 1 |

**Composite score thresholds:**
- 0–2: Clean
- 3–5: Watch list
- 6–9: Toxic — recommend disavow

---

## Google Disavow File Format

```
# Disavow file for example.com — generated YYYY-MM-DD
# Toxic domains (score 6+)
domain:spam-site.com
domain:link-farm-network.net
# Specific toxic URLs (use sparingly; domain-level preferred)
https://thin-content-site.com/bad-page/
```

Submit via: https://search.google.com/search-console/disavow-links

**Rules:**
- Use `domain:` prefix to disavow all links from a domain
- Only URL-level entries if domain has mix of good and bad links
- Disavow files are cumulative — always include all previously disavowed entries
- Google processes disavow files within weeks, not days

---

## Manual Action Recovery Checklist

If the user reports a manual action for unnatural links:
1. Pull full backlink profile (paid tool recommended)
2. Document all outreach attempts (date, method, response)
3. Build disavow file for all toxic and unresponsive domains
4. Submit reconsideration request with evidence of cleanup
5. Wait 2–4 weeks for Google reviewer to assess
6. If denied, repeat with broader disavow scope

---

## Key References

- Google Search Central: Link Schemes Policy
- Google Disavow Tool Documentation
- Moz Spam Score methodology
- Ahrefs Domain Rating methodology
