# Entity Relationship Mapper -- Reference

Supplementary reference material for the entity-relationship-mapper skill. Use alongside SKILL.md for Schema.org property tables, @id conventions, sameAs sources, JSON-LD templates, and ERD notation.

---

## Table of Contents

- [Schema.org Relationship Property Reference](#schemaorg-relationship-property-reference)
- [@id Convention Rules and Examples](#id-convention-rules-and-examples)
- [sameAs Link Sources by Entity Type](#sameas-link-sources-by-entity-type)
- [JSON-LD @graph Template](#json-ld-graph-template)
- [Common Entity Type Mappings](#common-entity-type-mappings)
- [ERD Notation Guide for Text-Based Diagrams](#erd-notation-guide-for-text-based-diagrams)

---

## Schema.org Relationship Property Reference

Complete reference of relationship properties used in entity-relationship mapping. Each entry includes the forward property, its domain (subject type), range (object type), and a usage example.

| Property | Domain (From) | Range (To) | Direction | Usage Example |
|---|---|---|---|---|
| `publisher` | CreativeWork, WebSite | Organization, Person | CreativeWork -> Organization | `"publisher": {"@id": "https://example.com/#organization"}` |
| `author` | CreativeWork | Organization, Person | CreativeWork -> Person | `"author": {"@id": "https://example.com/about/#person-jane"}` |
| `creator` | CreativeWork | Organization, Person | CreativeWork -> Person/Org | `"creator": {"@id": "https://example.com/#organization"}` |
| `employee` | Organization | Person | Organization -> Person | `"employee": [{"@id": "https://example.com/about/#person-jane"}]` |
| `worksFor` | Person | Organization | Person -> Organization | `"worksFor": {"@id": "https://example.com/#organization"}` |
| `founder` | Organization | Person | Organization -> Person | `"founder": {"@id": "https://example.com/about/#person-john"}` |
| `member` | Organization | Organization, Person | Organization -> Person | `"member": [{"@id": "https://example.com/about/#person-jane"}]` |
| `memberOf` | Person, Organization | Organization | Person -> Organization | `"memberOf": {"@id": "https://example.com/#organization"}` |
| `parentOrganization` | Organization | Organization | Child -> Parent | `"parentOrganization": {"@id": "https://example.com/#organization"}` |
| `subOrganization` | Organization | Organization | Parent -> Child | `"subOrganization": [{"@id": "https://example.com/#org-subsidiary"}]` |
| `department` | Organization | Organization | Organization -> Department | `"department": [{"@id": "https://example.com/#dept-engineering"}]` |
| `provider` | Service, CreativeWork | Organization, Person | Service -> Organization | `"provider": {"@id": "https://example.com/#organization"}` |
| `offers` | Product, Service, Event | Offer | Entity -> Offer | `"offers": {"@type": "Offer", "price": "500", ...}` |
| `brand` | Product, Organization | Brand | Product -> Brand | `"brand": {"@id": "https://example.com/#brand"}` |
| `manufacturer` | Product | Organization | Product -> Organization | `"manufacturer": {"@id": "https://example.com/#organization"}` |
| `isPartOf` | WebPage, CreativeWork | WebSite, CreativeWork | Page -> Site | `"isPartOf": {"@id": "https://example.com/#website"}` |
| `hasPart` | CreativeWork, WebSite | CreativeWork, WebPage | Site -> Page | `"hasPart": [{"@id": "https://example.com/blog/#webpage"}]` |
| `mainEntity` | WebPage | Thing | Page -> Entity | `"mainEntity": {"@id": "https://example.com/services/seo/#service"}` |
| `mainEntityOfPage` | Thing | WebPage | Entity -> Page | `"mainEntityOfPage": {"@id": "https://example.com/services/seo/#webpage"}` |
| `about` | WebPage, CreativeWork | Thing | Page -> Entity | `"about": {"@id": "https://example.com/#organization"}` |
| `sameAs` | Thing | URL | Entity -> External URL | `"sameAs": ["https://linkedin.com/company/example"]` |
| `image` | Thing | ImageObject, URL | Entity -> Image | `"image": {"@id": "https://example.com/#logo"}` |
| `logo` | Organization, Brand | ImageObject, URL | Organization -> Logo | `"logo": {"@id": "https://example.com/#logo"}` |
| `address` | Organization, LocalBusiness, Person | PostalAddress | Entity -> Address | `"address": {"@type": "PostalAddress", ...}` |
| `geo` | Place, LocalBusiness | GeoCoordinates | Location -> Coordinates | `"geo": {"@type": "GeoCoordinates", "latitude": "-33.87", ...}` |
| `areaServed` | Organization, Service | Place, GeoShape, Text | Service -> Area | `"areaServed": {"@type": "City", "name": "Sydney"}` |
| `knowsAbout` | Organization, Person | Text, Thing, URL | Entity -> Topic | `"knowsAbout": ["SEO", "Web Development"]` |
| `hasOfferCatalog` | Organization, Service | OfferCatalog | Organization -> Catalog | `"hasOfferCatalog": {"@type": "OfferCatalog", ...}` |
| `itemReviewed` | Review | Thing | Review -> Entity | `"itemReviewed": {"@id": "https://example.com/#organization"}` |
| `contactPoint` | Organization | ContactPoint | Organization -> Contact | `"contactPoint": {"@type": "ContactPoint", ...}` |
| `location` | Event, Organization | Place, PostalAddress | Event -> Place | `"location": {"@type": "Place", "name": "Sydney Office", ...}` |
| `organizer` | Event | Organization, Person | Event -> Organization | `"organizer": {"@id": "https://example.com/#organization"}` |
| `performer` | Event | Organization, Person | Event -> Person | `"performer": {"@id": "https://example.com/about/#person-jane"}` |
| `identifier` | Thing | PropertyValue, Text, URL | Entity -> ID | `"identifier": {"@type": "PropertyValue", "name": "ABN", ...}` |

### Bidirectional Relationship Pairs

When modelling relationships, apply both directions where applicable:

| Forward | Inverse | Notes |
|---|---|---|
| `employee` | `worksFor` | Organization lists employees; Person references employer |
| `founder` | (use `worksFor` + `jobTitle`) | Organization names founder; Person states role |
| `parentOrganization` | `subOrganization` | Child references parent; parent lists children |
| `publisher` | (no standard inverse) | WebSite/Article references publisher |
| `author` | (no standard inverse) | Article references author; use `author` on CreativeWork |
| `mainEntity` | `mainEntityOfPage` | Page references its main entity; entity references its page |
| `isPartOf` | `hasPart` | Page is part of site; site has pages |
| `provider` | (no standard inverse) | Service references provider |
| `memberOf` | `member` | Person references org; org lists members |

---

## @id Convention Rules and Examples

### URL Structure Rules

1. **Root pattern:** `{canonical_page_url}#{type-qualifier}`
2. **Hash fragment format:** lowercase, hyphenated: `#organization`, `#person-jane-doe`, `#service-web-dev`
3. **Uniqueness:** Every entity gets exactly one @id, used identically across all pages
4. **Stability:** @ids must not change when page content is updated -- they are permanent identifiers
5. **Canonical URL:** Use the page URL where the entity is most fully described

### @id Examples by Type

| Entity Type | @id Pattern | Example |
|---|---|---|
| Organization | `https://domain.com/#organization` | `https://acme.com.au/#organization` |
| WebSite | `https://domain.com/#website` | `https://acme.com.au/#website` |
| Person | `https://domain.com/about/#person-{slug}` | `https://acme.com.au/about/#person-jane-smith` |
| Service | `https://domain.com/services/{slug}/#{service}` | `https://acme.com.au/services/web-development/#service` |
| Product | `https://domain.com/products/{slug}/#{product}` | `https://acme.com.au/products/analytics-pro/#product` |
| LocalBusiness | `https://domain.com/locations/{slug}/#{location}` | `https://acme.com.au/locations/sydney-cbd/#location` |
| BlogPosting | `https://domain.com/blog/{slug}/#{article}` | `https://acme.com.au/blog/seo-guide-2025/#article` |
| WebPage | `https://domain.com/{path}/#{webpage}` | `https://acme.com.au/contact/#webpage` |
| ImageObject (logo) | `https://domain.com/#logo` | `https://acme.com.au/#logo` |
| Brand | `https://domain.com/#brand` | `https://acme.com.au/#brand` |
| Event | `https://domain.com/events/{slug}/#{event}` | `https://acme.com.au/events/launch-2025/#event` |
| FAQPage | `https://domain.com/faq/#{faqpage}` | `https://acme.com.au/faq/#faqpage` |
| ContactPage | `https://domain.com/contact/#{webpage}` | `https://acme.com.au/contact/#webpage` |
| Review | `https://domain.com/reviews/#{review-slug}` | `https://acme.com.au/reviews/#review-jane-smith` |

### @id vs url

| Property | Purpose | Has hash fragment | Example |
|---|---|---|---|
| `@id` | Graph identifier -- internal plumbing for connecting entities | Yes (`#fragment`) | `https://acme.com.au/about/#person-jane` |
| `url` | Human-facing web address a user visits | No | `https://acme.com.au/about/` |

These may share the same base URL but serve fundamentally different purposes. `@id` is for machines traversing the graph; `url` is for humans visiting pages.

### Multi-Location @id Conventions

```
Parent org:     https://acme.com.au/#organization
Sydney office:  https://acme.com.au/locations/sydney/#location
Melbourne:      https://acme.com.au/locations/melbourne/#location
Brisbane:       https://acme.com.au/locations/brisbane/#location
```

Each location uses `parentOrganization` to reference the parent `#organization`.

---

## sameAs Link Sources by Entity Type

### Organisations

| Source | URL Pattern | Priority | Notes |
|---|---|---|---|
| ABN Lookup | `https://abr.business.gov.au/ABN/View?abn={ABN}` | High (AU) | Authoritative for Australian businesses |
| LinkedIn Company | `https://www.linkedin.com/company/{slug}` | High | Most widely recognised business profile |
| Google Business Profile | `https://maps.google.com/?cid={CID}` | High | Use the Place URL or CID-based URL |
| Facebook Page | `https://www.facebook.com/{slug}` | Medium | If actively maintained |
| Crunchbase | `https://www.crunchbase.com/organization/{slug}` | Medium | For tech/startup companies |
| Wikipedia | `https://en.wikipedia.org/wiki/{title}` | High | If article exists |
| Wikidata | `https://www.wikidata.org/wiki/{QID}` | High | Machine-readable; preferred by knowledge graphs |
| Twitter/X | `https://twitter.com/{handle}` | Medium | If actively maintained |
| YouTube Channel | `https://www.youtube.com/@{handle}` | Low | If publishing video content |
| GitHub Org | `https://github.com/{org}` | Medium | For tech companies |
| Apple Maps | `https://maps.apple.com/?address={encoded}` | Low | Less commonly used for sameAs |
| Industry directories | Varies by industry | Medium | Real estate: domain.com.au; legal: lawsociety; medical: AHPRA |

### People

| Source | URL Pattern | Priority | Notes |
|---|---|---|---|
| LinkedIn Profile | `https://www.linkedin.com/in/{slug}` | High | Most authoritative professional profile |
| Twitter/X | `https://twitter.com/{handle}` | Medium | Public thought leadership |
| GitHub | `https://github.com/{username}` | Medium | For technical people |
| Personal website | `https://janedoe.com` | High | Authoritative if the person controls it |
| Google Scholar | `https://scholar.google.com/citations?user={ID}` | Medium | For academics/researchers |
| Wikidata | `https://www.wikidata.org/wiki/{QID}` | High | If notable enough for Wikidata entry |
| ORCID | `https://orcid.org/{ID}` | Medium | For researchers |
| Gravatar | `https://gravatar.com/{hash}` | Low | Email-linked identity |

### Locations (LocalBusiness)

| Source | URL Pattern | Priority | Notes |
|---|---|---|---|
| Google Maps/Places | `https://maps.google.com/?cid={CID}` | High | Primary local listing |
| Apple Maps | `https://maps.apple.com/?address={encoded}` | Medium | Apple ecosystem presence |
| Yelp | `https://www.yelp.com/biz/{slug}` | Medium | If listed and has reviews |
| TripAdvisor | `https://www.tripadvisor.com/{path}` | Medium | For hospitality/tourism businesses |
| OpenStreetMap | `https://www.openstreetmap.org/node/{ID}` | Low | Open data; less commonly referenced |
| Foursquare | `https://foursquare.com/v/{slug}/{ID}` | Low | Declining relevance |
| Zomato | `https://www.zomato.com/{city}/{slug}` | Medium | For restaurants (AU/NZ) |
| Yellow Pages AU | `https://www.yellowpages.com.au/{path}` | Low | Legacy directory |

### Products

| Source | URL Pattern | Priority | Notes |
|---|---|---|---|
| G2 | `https://www.g2.com/products/{slug}` | High | For SaaS products |
| Capterra | `https://www.capterra.com/p/{ID}/{slug}` | Medium | For software products |
| Product Hunt | `https://www.producthunt.com/products/{slug}` | Medium | For launched tech products |
| Amazon | `https://www.amazon.com.au/dp/{ASIN}` | High | For physical products sold on Amazon |
| App Store | `https://apps.apple.com/au/app/{slug}/id{ID}` | High | For iOS apps |
| Google Play | `https://play.google.com/store/apps/details?id={package}` | High | For Android apps |
| Wikipedia | `https://en.wikipedia.org/wiki/{title}` | High | If product has its own article |

---

## JSON-LD @graph Template

Complete multi-entity example showing a business with people, services, a location, and content.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://acme.com.au/#organization",
      "name": "Acme Digital",
      "legalName": "Acme Digital Pty Ltd",
      "url": "https://acme.com.au",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://acme.com.au/#logo",
        "url": "https://acme.com.au/images/logo.png",
        "width": "600",
        "height": "60",
        "caption": "Acme Digital logo"
      },
      "image": { "@id": "https://acme.com.au/#logo" },
      "description": "Acme Digital is a Sydney-based agency specialising in web development and SEO for small businesses.",
      "foundingDate": "2020",
      "founder": { "@id": "https://acme.com.au/about/#person-john-smith" },
      "employee": [
        { "@id": "https://acme.com.au/about/#person-john-smith" },
        { "@id": "https://acme.com.au/about/#person-jane-doe" }
      ],
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "123 George Street",
        "addressLocality": "Sydney",
        "addressRegion": "NSW",
        "postalCode": "2000",
        "addressCountry": "AU"
      },
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+61 2 9000 1234",
        "contactType": "customer service",
        "email": "hello@acme.com.au"
      },
      "identifier": {
        "@type": "PropertyValue",
        "name": "ABN",
        "value": "12 345 678 901"
      },
      "sameAs": [
        "https://www.linkedin.com/company/acme-digital-au",
        "https://www.facebook.com/acmedigitalau",
        "https://twitter.com/acmedigitalau",
        "https://abr.business.gov.au/ABN/View?abn=12345678901"
      ],
      "knowsAbout": [
        "Web Development",
        "Search Engine Optimization",
        "Digital Marketing",
        "E-commerce"
      ],
      "areaServed": {
        "@type": "Country",
        "name": "Australia"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://acme.com.au/#website",
      "name": "Acme Digital",
      "url": "https://acme.com.au",
      "publisher": { "@id": "https://acme.com.au/#organization" },
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": "https://acme.com.au/search?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
      }
    },
    {
      "@type": "WebPage",
      "@id": "https://acme.com.au/#webpage",
      "url": "https://acme.com.au",
      "name": "Acme Digital - Web Development & SEO Agency Sydney",
      "description": "Sydney-based web development and SEO agency helping small businesses grow online.",
      "isPartOf": { "@id": "https://acme.com.au/#website" },
      "about": { "@id": "https://acme.com.au/#organization" }
    },
    {
      "@type": "Person",
      "@id": "https://acme.com.au/about/#person-john-smith",
      "name": "John Smith",
      "jobTitle": "Founder & Managing Director",
      "url": "https://acme.com.au/about/",
      "image": "https://acme.com.au/images/team/john-smith.jpg",
      "worksFor": { "@id": "https://acme.com.au/#organization" },
      "sameAs": [
        "https://www.linkedin.com/in/johnsmith-acme",
        "https://twitter.com/johnsmith_dev"
      ],
      "knowsAbout": ["Web Development", "Business Strategy", "SEO"]
    },
    {
      "@type": "Person",
      "@id": "https://acme.com.au/about/#person-jane-doe",
      "name": "Jane Doe",
      "jobTitle": "Head of SEO",
      "url": "https://acme.com.au/about/",
      "image": "https://acme.com.au/images/team/jane-doe.jpg",
      "worksFor": { "@id": "https://acme.com.au/#organization" },
      "sameAs": [
        "https://www.linkedin.com/in/janedoe-seo"
      ],
      "knowsAbout": ["SEO", "Content Strategy", "Analytics"]
    },
    {
      "@type": "Service",
      "@id": "https://acme.com.au/services/web-development/#service",
      "name": "Web Development",
      "description": "Custom website design and development for small businesses using modern frameworks.",
      "url": "https://acme.com.au/services/web-development/",
      "provider": { "@id": "https://acme.com.au/#organization" },
      "areaServed": {
        "@type": "Country",
        "name": "Australia"
      },
      "offers": {
        "@type": "Offer",
        "priceCurrency": "AUD",
        "price": "5000",
        "priceSpecification": {
          "@type": "PriceSpecification",
          "priceCurrency": "AUD",
          "price": "5000",
          "unitText": "starting from"
        }
      }
    },
    {
      "@type": "Service",
      "@id": "https://acme.com.au/services/seo/#service",
      "name": "SEO Services",
      "description": "Search engine optimisation to improve organic visibility and drive qualified traffic.",
      "url": "https://acme.com.au/services/seo/",
      "provider": { "@id": "https://acme.com.au/#organization" },
      "areaServed": {
        "@type": "Country",
        "name": "Australia"
      }
    },
    {
      "@type": "BlogPosting",
      "@id": "https://acme.com.au/blog/seo-guide-2025/#article",
      "headline": "The Complete SEO Guide for Australian Small Businesses in 2025",
      "url": "https://acme.com.au/blog/seo-guide-2025/",
      "datePublished": "2025-03-15",
      "dateModified": "2025-03-20",
      "author": { "@id": "https://acme.com.au/about/#person-jane-doe" },
      "publisher": { "@id": "https://acme.com.au/#organization" },
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://acme.com.au/blog/seo-guide-2025/#webpage"
      },
      "image": "https://acme.com.au/images/blog/seo-guide-2025.jpg",
      "description": "A comprehensive guide to SEO strategy for Australian small businesses.",
      "articleSection": "SEO"
    }
  ]
}
```

---

## Common Entity Type Mappings

Quick lookup from business domain concepts to the correct Schema.org type.

| Business Domain Concept | Schema.org Type | Notes |
|---|---|---|
| The company / business | `Organization` | Use `LocalBusiness` subtype if customers visit a physical location |
| Registered company | `Corporation` | When legal structure matters |
| Agency / consultancy | `ProfessionalService` | Subtype of `LocalBusiness`; use if location-based |
| Shop / retail store | `Store` | Subtype of `LocalBusiness` |
| Restaurant / cafe | `Restaurant`, `CafeOrCoffeeShop` | Subtypes of `FoodEstablishment` |
| Medical practice | `MedicalBusiness` or subtype | `Physician`, `Dentist`, `Optician`, etc. |
| Legal practice | `LegalService` | Subtype of `LocalBusiness` |
| Accounting firm | `AccountingService` | Subtype of `FinancialService` |
| Real estate agency | `RealEstateAgent` | Subtype of `LocalBusiness` |
| Team member / staff | `Person` | Link to Organization via `worksFor` / `employee` |
| A service the business sells | `Service` | Can nest `Offer` for pricing |
| A physical product | `Product` | Can nest `Offer` for pricing |
| A SaaS product / app | `SoftwareApplication` | Use `applicationCategory`, `operatingSystem` |
| A digital download | `DigitalDocument` or `Product` | `Product` if sold commercially |
| An online course | `Course` | With `CourseInstance` for scheduled offerings |
| A blog post | `BlogPosting` | Subtype of `Article` |
| A technical article | `TechArticle` | Subtype of `Article` |
| A case study | `Article` or `CreativeWork` | No specific case study type exists |
| A how-to guide | `HowTo` | With `HowToStep` children |
| A FAQ page | `FAQPage` | With `Question` + `Answer` children |
| An event | `Event` | Subtypes: `BusinessEvent`, `EducationEvent`, `SocialEvent` |
| A webinar | `Event` with `eventAttendanceMode: OnlineEventAttendanceMode` | Use `VirtualLocation` |
| A podcast episode | `PodcastEpisode` | Part of `PodcastSeries` |
| A video | `VideoObject` | Can be embedded in `Article` or standalone |
| A review / testimonial | `Review` | Link to reviewed entity via `itemReviewed` |
| An award | `Award` or text in `award` property | No dedicated Award type |
| A brand name | `Brand` | Distinct from the Organization if brand name differs from legal name |
| A job posting | `JobPosting` | With `hiringOrganization` linking to Organization |
| An office / branch | `LocalBusiness` (subtype) | Use `parentOrganization` to link to parent |
| A geographic service area | `GeoShape`, `AdministrativeArea`, `City`, `State`, `Country` | Use in `areaServed` property |
| A price / offer | `Offer` | Nest within `Product` or `Service` |
| A price range / bundle | `AggregateOffer` | When multiple price points exist |
| A product catalogue | `OfferCatalog` | Use `hasOfferCatalog` on Organization |
| A logo | `ImageObject` | Reference from Organization via `logo` and `image` |
| A contact method | `ContactPoint` | Nest in Organization; specify `contactType` |
| A postal address | `PostalAddress` | Nest in Organization or LocalBusiness via `address` |
| GPS coordinates | `GeoCoordinates` | Nest in Place or LocalBusiness via `geo` |
| Opening hours | `OpeningHoursSpecification` | Use on `LocalBusiness` via `openingHoursSpecification` |
| An Australian Business Number | `PropertyValue` | `"name": "ABN", "value": "12 345 678 901"` via `identifier` |

---

## ERD Notation Guide for Text-Based Diagrams

Since JSON-LD entity graphs are described in documentation and code, not visual tools, use this text-based notation for drawing entity-relationship diagrams in markdown, comments, and architecture docs.

### Entity Boxes

```
┌──────────────────┐
│ EntityType       │
│ #id-fragment     │
├──────────────────┤
│ name: value      │
│ property: value  │
└──────────────────┘
```

Simplified (no properties):

```
┌──────────────┐
│ Organization │
│ #organization│
└──────────────┘
```

### Relationship Lines

| Symbol | Meaning |
|---|---|
| `──▶` | Directed relationship (arrow points to target) |
| `◀──▶` | Bidirectional relationship |
| `──` | Undirected / association |
| `──┤` | One side of relationship |
| `├──` | Other side of relationship |

### Cardinality Notation

| Symbol | Meaning | Example |
|---|---|---|
| `1──▶1` | One-to-one | Organization `1──▶1` WebSite |
| `1──▶*` | One-to-many | Organization `1──▶*` Person (employees) |
| `*──▶1` | Many-to-one | BlogPosting `*──▶1` Person (author) |
| `*──▶*` | Many-to-many | Person `*──▶*` Organization (memberOf) |

### Labelled Relationships

Write the property name on or near the line:

```
┌──────────┐  employee   ┌──────────┐
│ Org      │────────────▶│ Person   │
│ #org     │◀────────────│ #person  │
└──────────┘  worksFor   └──────────┘
```

### Full Diagram Example

```
                         ┌──────────────┐
                         │  WebSite     │
                         │  #website    │
                         └──────┬───────┘
                                │ publisher (1:1)
                                ▼
┌──────────┐  employee  ┌──────────────┐  parentOrg  ┌──────────────┐
│ Person   │◀──────────▶│ Organization │◀───────────▶│ LocalBusiness│
│ #person  │  worksFor  │ #organization│  subOrg     │ #location    │
└────┬─────┘            └──────┬───────┘             └──────┬───────┘
     │ author (*.1)            │ provider (1.*)             │ address (1:1)
     ▼                         ▼                            ▼
┌──────────┐            ┌──────────────┐             ┌──────────────┐
│ Article  │            │   Service    │             │ PostalAddress │
│ #article │            │   #service   │             │              │
└──────────┘            └──────┬───────┘             └──────────────┘
                               │ offers (1:*)
                               ▼
                        ┌──────────────┐
                        │    Offer     │
                        │              │
                        └──────────────┘
```

### Notation for Page-Entity Relationships

Use dashed lines or a different marker to distinguish page containers from entity relationships:

```
┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐
  Homepage (/)
│                       │
  Contains:
│  - Organization #org  │
│  - WebSite #website   │
   - WebPage #webpage
└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘

┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐
  About Page (/about/)
│                       │
  Contains:
│  - Person #person-*   │
│  - WebPage #webpage   │
   References:
│  - Organization #org  │
└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘

┌─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┐
  Service Page
│ (/services/seo/)      │
  Contains:
│  - Service #service   │
│  - WebPage #webpage   │
   References:
│  - Organization #org  │
└─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┘
```

### Tips for Text-Based ERDs

- Keep diagrams under 80 characters wide for readability in code and markdown
- Use the `#fragment` from the @id inside each entity box so diagrams map directly to JSON-LD
- Show the most important relationships; do not try to diagram every property
- Group related entities spatially (org + people on one side, content on another)
- Use a legend at the bottom if your diagram uses custom notation
- For complex graphs (10+ entities), split into multiple focused diagrams rather than one dense diagram
