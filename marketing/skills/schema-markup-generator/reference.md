# Schema Markup Generator — Reference: Schema.org Types Matrix

## Table of Contents

- [Article / BlogPosting / NewsArticle](#article--blogposting--newsarticle)
- [Product](#product)
- [FAQPage](#faqpage)
- [HowTo](#howto)
- [LocalBusiness](#localbusiness)
- [Recipe](#recipe)
- [Event](#event)
- [Organization](#organization)
- [Person](#person)
- [BreadcrumbList](#breadcrumblist)
- [Service](#service)
- [Review / AggregateRating](#review--aggregaterating)

## Google-Supported Rich Result Types

Types marked **Rich Result** are eligible for enhanced SERP display. Types marked **Semantic only** improve knowledge graph understanding but do not produce rich results.

---

## Article / BlogPosting / NewsArticle

**Rich Result:** Yes (Top Stories, author rich results)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `headline` | Yes | — |
| `image` | Yes (array of URLs) | — |
| `datePublished` | Yes | — |
| `dateModified` | — | Yes |
| `author` | Yes (`Person` or `Organization`) | — |
| `publisher` | — | Yes (`Organization`) |
| `description` | — | Yes |
| `mainEntityOfPage` | — | Yes (`WebPage` URL) |
| `url` | — | Yes |

**Notes:**
- `NewsArticle` for time-sensitive news; `BlogPosting` for blog posts; `Article` for general editorial
- `image` should be at least 1200px wide for AMP Top Stories
- `author` with a `Person` type and `sameAs` (linking to author's social or Wikipedia profile) improves E-E-A-T signals

---

## Product

**Rich Result:** Yes (Product snippets with price, availability, rating)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `name` | Yes | — |
| `image` | Yes | — |
| `description` | — | Yes |
| `sku` | — | Yes |
| `brand` | — | Yes (`Brand`) |
| `offers` | Yes (`Offer`) | — |
| `offers.price` | Yes | — |
| `offers.priceCurrency` | Yes (use `"AUD"`) | — |
| `offers.availability` | Yes | — |
| `offers.url` | — | Yes |
| `aggregateRating` | — | Yes (if ratings available) |
| `aggregateRating.ratingValue` | Required if AggRating | — |
| `aggregateRating.reviewCount` | Required if AggRating | — |
| `review` | — | Yes |

**Availability values:**
- `https://schema.org/InStock`
- `https://schema.org/OutOfStock`
- `https://schema.org/PreOrder`
- `https://schema.org/Discontinued`

---

## FAQPage

**Rich Result:** Yes (FAQ accordion in SERP)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `mainEntity` | Yes (array) | — |
| `mainEntity[].@type` | Yes (`Question`) | — |
| `mainEntity[].name` | Yes (the question) | — |
| `mainEntity[].acceptedAnswer` | Yes (`Answer`) | — |
| `mainEntity[].acceptedAnswer.text` | Yes | — |

**Notes:**
- Each answer should be at least 1 sentence; 40–60 words optimal for Featured Snippet
- Google typically displays 3–5 FAQ items in rich results even if more are marked up
- Do not use FAQPage for pages where users submit answers — that requires `QAPage`

---

## HowTo

**Rich Result:** Yes (step-by-step rich result with images)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `name` | Yes | — |
| `step` | Yes (array of `HowToStep`) | — |
| `step[].@type` | Yes | — |
| `step[].name` | Yes | — |
| `step[].text` | Yes | — |
| `step[].image` | — | Yes |
| `image` | — | Yes |
| `totalTime` | — | Yes (ISO 8601 duration, e.g. `PT30M`) |
| `estimatedCost` | — | Yes |
| `supply` | — | Yes (`HowToSupply`) |
| `tool` | — | Yes (`HowToTool`) |

---

## LocalBusiness

**Rich Result:** Yes (knowledge panel, map pack)
**Sub-types include:** Restaurant, MedicalBusiness, LegalService, FinancialService, HomeAndConstructionBusiness, AutoRepair, etc.

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `name` | Yes | — |
| `address` | Yes (`PostalAddress`) | — |
| `address.streetAddress` | Yes | — |
| `address.addressLocality` | Yes | — |
| `address.addressRegion` | Yes (AU state code, e.g. `VIC`) | — |
| `address.postalCode` | Yes | — |
| `address.addressCountry` | Yes (`AU`) | — |
| `telephone` | Yes | — |
| `url` | Yes | — |
| `openingHoursSpecification` | — | Yes |
| `geo` | — | Yes (`GeoCoordinates`) |
| `image` | — | Yes |
| `priceRange` | — | Yes |
| `servesCuisine` | — | Yes (for Restaurant) |
| `aggregateRating` | — | Yes |
| `sameAs` | — | Yes (Google Business Profile URL, Facebook, etc.) |

---

## Organization / Person

**Rich Result:** Semantic + knowledge panel
**Notes:** Use `Organization` for businesses, brands, and institutions; `Person` for individuals.

| Property (Organization) | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `name` | Yes | — |
| `url` | Yes | — |
| `logo` | — | Yes |
| `sameAs` | — | Yes (social profiles, Wikipedia) |
| `contactPoint` | — | Yes |
| `address` | — | Yes |

---

## BreadcrumbList

**Rich Result:** Yes (breadcrumb trail in SERP URL display)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `itemListElement` | Yes (array of `ListItem`) | — |
| `itemListElement[].@type` | Yes (`ListItem`) | — |
| `itemListElement[].position` | Yes (integer, starts at 1) | — |
| `itemListElement[].name` | Yes | — |
| `itemListElement[].item` | Yes (URL of the breadcrumb page) | — |

---

## Event

**Rich Result:** Yes (event rich results in search and Google Events)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `name` | Yes | — |
| `startDate` | Yes (ISO 8601) | — |
| `endDate` | — | Yes |
| `eventStatus` | — | Yes (`EventScheduled`, `EventCancelled`, `EventPostponed`) |
| `eventAttendanceMode` | — | Yes (`OnlineEventAttendanceMode`, `OfflineEventAttendanceMode`) |
| `location` | Yes (`Place` or `VirtualLocation`) | — |
| `organizer` | — | Yes (`Organization` or `Person`) |
| `image` | — | Yes |
| `offers` | — | Yes (if ticketed) |
| `description` | — | Yes |

---

## Recipe

**Rich Result:** Yes (recipe card with image, ratings, cook time)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `name` | Yes | — |
| `image` | Yes | — |
| `author` | Yes (`Person`) | — |
| `datePublished` | — | Yes |
| `description` | — | Yes |
| `prepTime` | — | Yes (ISO 8601) |
| `cookTime` | — | Yes (ISO 8601) |
| `totalTime` | — | Yes |
| `recipeYield` | — | Yes |
| `recipeIngredient` | Yes (array) | — |
| `recipeInstructions` | Yes (`HowToStep` array) | — |
| `aggregateRating` | — | Yes |
| `nutrition` | — | Yes |

---

## Review

**Rich Result:** Yes (review snippet — but only in aggregate or via third-party review sites)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `itemReviewed` | Yes | — |
| `reviewRating` | Yes (`Rating`) | — |
| `reviewRating.ratingValue` | Yes | — |
| `reviewRating.bestRating` | — | Yes |
| `author` | Yes (`Person`) | — |
| `reviewBody` | — | Yes |
| `datePublished` | — | Yes |

---

## Service

**Rich Result:** Semantic only (no standalone rich result; enhances knowledge panel)

| Property | Required | Recommended |
|---|---|---|
| `@type` | Yes | — |
| `name` | Yes | — |
| `provider` | — | Yes (`Organization`) |
| `serviceType` | — | Yes |
| `areaServed` | — | Yes (`City`, `State`, `Country`) |
| `description` | — | Yes |
| `offers` | — | Yes |

---

## JSON-LD @graph Pattern (Multi-Type Pages)

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      ...
    },
    {
      "@type": "FAQPage",
      ...
    }
  ]
}
</script>
```

Use `@graph` whenever two or more types apply to the same page. This is cleaner than two separate `<script>` tags (though both are valid).

---

## ISO 8601 Duration Quick Reference

| Duration | Format |
|---|---|
| 30 minutes | `PT30M` |
| 1 hour | `PT1H` |
| 1 hour 30 minutes | `PT1H30M` |
| 2 days | `P2D` |
| 1 week | `P1W` |

---

## Key References

- Google Rich Results documentation: https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- Schema.org full type hierarchy: https://schema.org/docs/full.html
- Google Rich Results Test: https://search.google.com/test/rich-results
- Schema Validator: https://validator.schema.org/
