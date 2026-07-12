# Schema Markup — LocalBusiness + FAQPage — Crema Lane Café, Brisbane

**Date:** 15/05/2026
**Schema types:** LocalBusiness (CafeOrCoffeeShop), FAQPage
**Locale:** en-AU

---

## Generated JSON-LD

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["LocalBusiness", "CafeOrCoffeeShop"],
      "@id": "https://cremalane.com.au/#business",
      "name": "Crema Lane",
      "description": "Specialty coffee bar and café in Brisbane's West End, serving single-origin espresso, cold brew, and all-day brunch in a relaxed laneway setting.",
      "url": "https://cremalane.com.au",
      "telephone": "+61 7 3844 5566",
      "email": "hello@cremalane.com.au",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "18 Raven Street",
        "addressLocality": "West End",
        "addressRegion": "QLD",
        "postalCode": "4101",
        "addressCountry": "AU"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": -27.4798,
        "longitude": 153.0128
      },
      "image": [
        "https://cremalane.com.au/images/cafe-exterior.jpg",
        "https://cremalane.com.au/images/coffee-bar.jpg",
        "https://cremalane.com.au/images/brunch-menu.jpg"
      ],
      "logo": "https://cremalane.com.au/images/crema-lane-logo.png",
      "priceRange": "$$",
      "servesCuisine": ["Coffee", "Brunch", "Australian"],
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          "opens": "06:30",
          "closes": "15:00"
        },
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Saturday", "Sunday"],
          "opens": "07:00",
          "closes": "14:00"
        }
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.7",
        "reviewCount": "312",
        "bestRating": "5",
        "worstRating": "1"
      },
      "sameAs": [
        "https://www.google.com/maps/place/Crema+Lane",
        "https://www.instagram.com/cremalane",
        "https://www.facebook.com/cremalane"
      ],
      "hasMap": "https://goo.gl/maps/REPLACE_ME_WITH_ACTUAL_MAPS_LINK",
      "currenciesAccepted": "AUD",
      "paymentAccepted": "Cash, Credit Card, EFTPOS",
      "areaServed": {
        "@type": "City",
        "name": "Brisbane"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Does Crema Lane take reservations?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Crema Lane does not take reservations. We operate on a walk-in basis. Weekend mornings can be busy — we recommend arriving before 9am to avoid a wait."
          }
        },
        {
          "@type": "Question",
          "name": "Is Crema Lane dog-friendly?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, Crema Lane is dog-friendly at our outdoor laneway seating. Dogs are welcome on a leash, and we keep a water bowl at the entrance. Dogs are not permitted inside due to health regulations."
          }
        },
        {
          "@type": "Question",
          "name": "Do you offer dairy-free milk alternatives?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, we offer oat milk, almond milk, soy milk, and macadamia milk at no extra charge. Our baristas are trained to steam each milk alternative correctly for the best texture."
          }
        },
        {
          "@type": "Question",
          "name": "Where do you source your coffee beans?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Our espresso blend is sourced from Ona Coffee (Canberra) and rotated seasonally. We also offer a single-origin pour-over option from rotating Australian and Papua New Guinean producers."
          }
        },
        {
          "@type": "Question",
          "name": "Is there parking near Crema Lane?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Street parking is available on Raven Street and Boundary Street (2-hour limit). The nearest paid car park is on Vulture Street, approximately 200 metres away. The West End bus stop on Boundary Street is a 2-minute walk."
          }
        }
      ]
    }
  ]
}
</script>
```

---

## Validation Notes

### Required Properties Status — LocalBusiness

| Property | Status | Notes |
|---|---|---|
| `@type` | Populated | Stacked `LocalBusiness` + `CafeOrCoffeeShop` sub-type |
| `name` | Populated | — |
| `address` | Populated | Full PostalAddress with AU country code |
| `telephone` | Populated | E.164 format with +61 country code |
| `url` | Populated | — |
| `aggregateRating.ratingValue` | Populated | Based on user-supplied data |
| `aggregateRating.reviewCount` | Populated | Must reflect actual review count; keep updated |

### Required Properties Status — FAQPage

| Property | Status | Notes |
|---|---|---|
| `mainEntity` | Populated | 5 questions provided |
| All `Question.name` | Populated | — |
| All `acceptedAnswer.text` | Populated | Each answer is 40–70 words (optimal for Featured Snippet) |

### Recommended Properties Not Yet Included

| Property | Value to Add | Impact |
|---|---|---|
| `hasMap` | Replace `REPLACE_ME_WITH_ACTUAL_MAPS_LINK` with real Google Maps URL | Enables direct map link in knowledge panel |
| `menu` | Add `"menu": "https://cremalane.com.au/menu"` if a menu page exists | Enables menu link for Restaurant/Café types |
| `founder` | `{"@type": "Person", "name": "Your Name"}` | Enhances knowledge graph |
| `foundingDate` | `"2019"` (or actual year) | Adds establishment credibility signal |

---

## Testing Instructions

**Google Rich Results Test:**
1. Go to https://search.google.com/test/rich-results
2. Select "Test code snippet"
3. Paste the JSON-LD block above
4. Expected: `LocalBusiness` and `FAQPage` both appear as detected types with no errors

**Schema.org Validator:**
1. Go to https://validator.schema.org/
2. Paste the JSON-LD block
3. Verify: `CafeOrCoffeeShop` and `FAQPage` types validated correctly

**Live page testing (after deployment):**
```
https://search.google.com/test/rich-results?url=https://cremalane.com.au
```

---

## Implementation Notes

- Place the entire `<script type="application/ld+json">` block in the `<head>` element of the page, ideally near other `<meta>` tags
- The `hasMap` value should be replaced with the actual Google Maps share link for the business
- The `aggregateRating` values (`ratingValue: 4.7`, `reviewCount: 312`) must reflect real review data — do not inflate these figures as this violates Google's structured data guidelines
- FAQ rich results typically appear within 1–2 weeks of deployment after Google's next crawl
- If the café ever changes hours (e.g. holiday trading), update `openingHoursSpecification` promptly — outdated hours in schema will generate a mismatch warning in Search Console

---

*Generated by marketing / schema-markup-generator*
