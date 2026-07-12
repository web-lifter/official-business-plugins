# Local SEO Audit — Reference Framework

## NAP Consistency Check Methodology

### What is NAP?

NAP = Name, Address, Phone. The three data points that Google uses to verify and rank a local business. Consistent NAP across the web is a fundamental local ranking signal.

### Common NAP Variation Types

| Variation Type | Example | Impact |
|---|---|---|
| Business suffix | "Pty Ltd" vs "Pty. Ltd." | Low–Medium |
| Street type abbreviation | "St" vs "Street" | Low–Medium |
| Suite/unit format | "Level 2, 10 Collins St" vs "10 Collins Street, Level 2" | Medium |
| Phone format | "03 9800 1234" vs "(03) 9800 1234" vs "+61 3 9800 1234" | Low |
| Old address (post-move) | Previous premises still listed on citation sites | High |
| Business name variation | "Crema Lane Café" vs "Crema Lane Coffee" | High |
| Truncated name | "Crema Lane" vs "Crema Lane Specialty Coffee" | Medium |

### Canonical NAP Format (Recommended Australian Standard)

- **Name:** Trading name as registered with ASIC or commonly known (consistent across all platforms)
- **Address:** Full street address in Australia Post format — `[unit/level] [number] [Street Name] [Street Type], [Suburb] [STATE] [postcode]`
- **Phone:** National format: `(0X) XXXX XXXX` for landlines; `04XX XXX XXX` for mobiles

---

## Google Business Profile Completeness Checklist

Score 1 point for each item present and accurate. Total: 0–22.

| Category | Item | Points |
|---|---|---|
| Basic | Business name (canonical) | 1 |
| Basic | Primary category | 1 |
| Basic | Additional categories (at least 1) | 1 |
| Basic | Address | 1 |
| Basic | Phone number | 1 |
| Basic | Website URL | 1 |
| Basic | Business description (750 chars) | 1 |
| Hours | Primary hours | 1 |
| Hours | Holiday hours set | 1 |
| Hours | Special hours (if applicable) | 1 |
| Media | Photos (minimum 5) | 1 |
| Media | Logo uploaded | 1 |
| Media | Cover photo | 1 |
| Media | Interior/exterior photos | 1 |
| Services/Products | Services listed | 1 |
| Services/Products | Products listed (if applicable) | 1 |
| Posts | At least 1 post in last 30 days | 1 |
| Posts | At least 1 offer or event post | 1 |
| Q&A | Questions answered | 1 |
| Attributes | Relevant attributes set (accessibility, payment, etc.) | 1 |
| Reviews | Average rating ≥ 4.0 | 1 |
| Reviews | All reviews responded to | 1 |

**Scoring bands:**
- 18–22: Excellent
- 12–17: Good
- 6–11: Needs improvement
- 0–5: Critical gaps

---

## Australian Citation Directory Tiers

### Tier 1 — Must Have (highest authority and impact)

| Directory | URL | Notes |
|---|---|---|
| Google Business Profile | business.google.com | Essential; most impactful local ranking factor |
| Apple Maps | mapsconnect.apple.com | Important for iPhone/Safari users |
| Bing Places | bingplaces.com | Feeds Bing Maps and Cortana |
| Yelp Australia | yelp.com.au | High authority; strong review platform |
| Facebook | facebook.com | Social trust signal; review platform |

### Tier 2 — Strongly Recommended (Australian-specific)

| Directory | URL | Notes |
|---|---|---|
| Yellow Pages Australia | yellowpages.com.au | Long-standing AU directory; DA ~58 |
| True Local | truelocal.com.au | Australian local review directory |
| Hotfrog Australia | hotfrog.com.au | Global but has AU section; free listing |
| StartLocal | startlocal.com.au | AU-specific; good for local authority |
| AussieWeb | aussieweb.com.au | Australian business directory |
| White Pages Australia | whitepages.com.au | Phone and address verification authority |

### Tier 3 — Category-Specific (Australian niche directories)

| Category | Directories |
|---|---|
| Restaurants / Cafés | Zomato, OpenTable, TripAdvisor, Broadsheet |
| Trades / Home Services | hipages, ServiceSeeking, OneFlare |
| Health / Medical | HealthEngine, HotDoc, Healthdirect Provider Finder |
| Legal | LawAnswers, Lawyer.com.au, LawTap |
| Real Estate | realestate.com.au, domain.com.au (agent listings) |
| Automotive | CarExpert, carsales.com.au, AutoGuru |
| Education | Study.com.au, Course Finder, TAFEnow |
| Accounting / Finance | Adviser Ratings, XeroPartners (if applicable) |
| Hospitality | TripAdvisor, Booking.com, Expedia |

---

## Review Velocity Benchmarks (Australian Market)

| Business Category | Healthy Monthly Velocity | Competitive Velocity |
|---|---|---|
| Café / Restaurant | 10–30 reviews/month | 30+ reviews/month |
| Retail (general) | 3–10 reviews/month | 10+ reviews/month |
| Professional services (legal, accounting) | 1–3 reviews/month | 5+ reviews/month |
| Medical / Health | 2–8 reviews/month | 10+ reviews/month |
| Trades / Home Services | 3–10 reviews/month | 15+ reviews/month |
| B2B services | 0.5–2 reviews/month | 3+ reviews/month |

### Review Acquisition Best Practices (compliant with Google Guidelines)

- Ask all customers for a review post-service — in person, by SMS, or by email
- Provide a direct GBP review link (short URL from GBP dashboard)
- Do NOT offer incentives for reviews (against Google guidelines)
- Do NOT review-gate (pre-screening customers to only send happy ones)
- Respond to ALL reviews — positive and negative — within 48 hours

### Responding to Negative Reviews

1. Acknowledge the experience
2. Apologise sincerely (do not be defensive)
3. Offer to resolve offline (provide contact email or phone)
4. Keep responses under 100 words
5. Never argue publicly

---

## Local Pack (Map Pack) Ranking Factors

Google's local ranking algorithm uses three signals:

### 1. Relevance
- GBP category matches the search query
- Business description contains relevant keywords
- Services/products listed match what users search for
- Website content supports the business category

### 2. Proximity
- Physical distance from the searcher (or service area specified)
- Cannot be optimised directly — choosing a central location helps

### 3. Prominence
- Number and quality of reviews
- NAP consistency across citation directories
- Backlinks pointing to the website
- GBP activity (posts, photos, Q&A responses)
- Domain authority of the website

### Local Pack Optimisation Priority Order

1. Claim and verify GBP (if not done)
2. Complete GBP profile to 18+ out of 22 checklist items
3. Fix all Tier-1 NAP inconsistencies
4. Fix Tier-2 NAP inconsistencies
5. Build missing Tier-1 and Tier-2 citations
6. Implement review acquisition strategy
7. Respond to all outstanding reviews
8. Add Tier-3 category-specific citations
9. Optimise website landing page for local keywords
10. Implement LocalBusiness schema on website

---

## LocalBusiness Schema Quick Reference

Key properties for a local business page (see `schema-markup-generator` for full implementation):

```json
{
  "@type": "LocalBusiness",
  "name": "[Canonical Business Name]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Number Street Name]",
    "addressLocality": "[Suburb]",
    "addressRegion": "[STATE]",
    "postalCode": "[XXXX]",
    "addressCountry": "AU"
  },
  "telephone": "[canonical phone]",
  "url": "[website URL]"
}
```

Run `schema-markup-generator` with the verified NAP data from this audit for a full implementation.

---

## Key References

- Google Business Profile Help Centre
- Moz Local: Local SEO guide and citation building methodology
- BrightLocal: Local Consumer Review Survey (Australian data)
- Google Business Profile Guidelines: Prohibited and restricted content
