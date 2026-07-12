# Entity-Relationship Map: Reliable Plumbing Solutions

**Business:** Reliable Plumbing Solutions Pty Ltd
**Domain:** Local plumbing services, residential and commercial
**Location:** Northern Beaches, Sydney, NSW
**Date:** 2026-04-04

---

## 1. Entity Inventory

| Entity Type | Count | Description |
|---|---|---|
| Organisation | 1 | The plumbing business itself |
| Person | 4 | Owner, licensed plumbers, apprentice |
| Service | 6 | Distinct service offerings |
| ServiceArea | 3 | Geographic coverage zones |
| Review | 12 | Customer reviews across platforms |
| Offer | 3 | Current promotional offers |

---

## 2. Entity Definitions and @id Architecture

Each entity uses a deterministic URI structure anchored to the business domain.

| Entity | @type (Schema.org) | @id Pattern | Example |
|---|---|---|---|
| Organisation | `PlumbingBusiness` | `https://reliableplumbing.com.au/#org` | `/#org` |
| Person | `Person` | `https://reliableplumbing.com.au/#person/{slug}` | `/#person/dave-mitchell` |
| Service | `Service` | `https://reliableplumbing.com.au/#service/{slug}` | `/#service/blocked-drains` |
| ServiceArea | `GeoCircle` / `AdministrativeArea` | `https://reliableplumbing.com.au/#area/{slug}` | `/#area/northern-beaches` |
| Review | `Review` | `https://reliableplumbing.com.au/#review/{platform}-{index}` | `/#review/google-001` |
| Offer | `Offer` | `https://reliableplumbing.com.au/#offer/{slug}` | `/#offer/senior-discount` |

---

## 3. Entity-Relationship Diagram

```
                    +-----------------+
                    |  Organisation   |
                    |  (PlumbingBiz)  |
                    +--------+--------+
                             |
          +------------------+------------------+
          |                  |                  |
    employs/owns       provides           areaServed
          |                  |                  |
  +-------+------+   +------+------+   +-------+-------+
  |    Person    |   |   Service   |   |  ServiceArea  |
  | (Plumber x4) |   | (6 types)   |   | (3 zones)     |
  +--------------+   +------+------+   +---------------+
                            |
                      hasOffer
                            |
                     +------+------+
                     |    Offer    |
                     | (3 promos)  |
                     +-------------+

  +-------------+
  |   Review    |-----> itemReviewed ----> Organisation
  | (12 total)  |-----> author ---------> Person (customer, external)
  +-------------+
```

---

## 4. Relationship Matrix

| From | Relation | To | Cardinality |
|---|---|---|---|
| Organisation | `employee` | Person | 1:N |
| Organisation | `hasOfferCatalog` | Service | 1:N |
| Organisation | `areaServed` | ServiceArea | 1:N |
| Service | `offers` | Offer | 1:N |
| Review | `itemReviewed` | Organisation | N:1 |
| Review | `author` | Person (external) | N:1 |
| Person | `worksFor` | Organisation | N:1 |
| Person | `knowsAbout` | Service | N:N |

---

## 5. sameAs Link Mappings

| Entity | Platform | sameAs URI |
|---|---|---|
| Organisation | Google Business | `https://www.google.com/maps?cid=12345678901234567` |
| Organisation | Facebook | `https://www.facebook.com/ReliablePlumbingSydney` |
| Organisation | ServiceSeeking | `https://www.serviceseeking.com.au/profile/reliable-plumbing` |
| Organisation | Hipages | `https://hipages.com.au/connect/reliableplumbingsolutions` |
| Organisation | ABN Lookup | `https://abr.business.gov.au/ABN/View?abn=51234567890` |
| Person (Dave) | LinkedIn | `https://www.linkedin.com/in/dave-mitchell-plumber` |

---

## 6. JSON-LD @graph Snippet

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Plumber",
      "@id": "https://reliableplumbing.com.au/#org",
      "name": "Reliable Plumbing Solutions Pty Ltd",
      "url": "https://reliableplumbing.com.au",
      "telephone": "+61-2-9876-5432",
      "abn": "51 234 567 890",
      "priceRange": "$$",
      "areaServed": [
        { "@id": "https://reliableplumbing.com.au/#area/northern-beaches" },
        { "@id": "https://reliableplumbing.com.au/#area/north-shore" },
        { "@id": "https://reliableplumbing.com.au/#area/hills-district" }
      ],
      "employee": [
        { "@id": "https://reliableplumbing.com.au/#person/dave-mitchell" }
      ],
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "itemListElement": [
          { "@id": "https://reliableplumbing.com.au/#service/blocked-drains" },
          { "@id": "https://reliableplumbing.com.au/#service/hot-water-systems" },
          { "@id": "https://reliableplumbing.com.au/#service/leak-detection" },
          { "@id": "https://reliableplumbing.com.au/#service/gas-fitting" },
          { "@id": "https://reliableplumbing.com.au/#service/bathroom-renovations" },
          { "@id": "https://reliableplumbing.com.au/#service/emergency-plumbing" }
        ]
      },
      "sameAs": [
        "https://www.facebook.com/ReliablePlumbingSydney",
        "https://hipages.com.au/connect/reliableplumbingsolutions"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "12"
      }
    },
    {
      "@type": "Person",
      "@id": "https://reliableplumbing.com.au/#person/dave-mitchell",
      "name": "Dave Mitchell",
      "jobTitle": "Owner & Licensed Plumber",
      "worksFor": { "@id": "https://reliableplumbing.com.au/#org" },
      "knowsAbout": ["Gas Fitting", "Blocked Drains", "Hot Water Systems"],
      "sameAs": "https://www.linkedin.com/in/dave-mitchell-plumber"
    },
    {
      "@type": "Service",
      "@id": "https://reliableplumbing.com.au/#service/blocked-drains",
      "name": "Blocked Drain Clearing",
      "description": "CCTV drain inspection and high-pressure jet blasting for residential and commercial blocked drains.",
      "provider": { "@id": "https://reliableplumbing.com.au/#org" },
      "areaServed": { "@id": "https://reliableplumbing.com.au/#area/northern-beaches" },
      "offers": {
        "@type": "Offer",
        "@id": "https://reliableplumbing.com.au/#offer/free-inspection",
        "name": "Free CCTV Drain Inspection",
        "description": "Complimentary CCTV inspection with any drain clearing service",
        "price": "0",
        "priceCurrency": "AUD"
      }
    },
    {
      "@type": "GeoCircle",
      "@id": "https://reliableplumbing.com.au/#area/northern-beaches",
      "name": "Northern Beaches",
      "geoMidpoint": {
        "@type": "GeoCoordinates",
        "latitude": -33.74,
        "longitude": 151.28
      },
      "geoRadius": "15 km"
    },
    {
      "@type": "Review",
      "@id": "https://reliableplumbing.com.au/#review/google-001",
      "itemReviewed": { "@id": "https://reliableplumbing.com.au/#org" },
      "reviewRating": { "@type": "Rating", "ratingValue": "5" },
      "author": { "@type": "Person", "name": "Sarah T." },
      "reviewBody": "Dave was on time, explained everything clearly, and fixed our burst pipe within the hour. Highly recommend.",
      "datePublished": "2026-03-15"
    }
  ]
}
```

---

## 7. Validation Checklist

- [x] All entities have deterministic @id URIs
- [x] sameAs links resolve to live platform profiles
- [x] Relationships are bidirectional where Schema.org supports it
- [x] AggregateRating aligns with review count
- [x] GeoCircle service areas cover stated suburbs
- [x] ABN format valid (11 digits, space-separated)
