## Entity-Relationship Model — [Business Name]

### 1. Entity Inventory

| # | Entity | Schema.org Type | @id | Primary Page | Description |
|---|--------|----------------|-----|-------------|-------------|
| 1 | {{entity_name}} | {{e.g. Organization}} | `{{url}}/#{{fragment}}` | {{e.g. Homepage}} | {{brief description}} |
| 2 | {{entity_name}} | {{e.g. Person}} | `{{url}}/#{{fragment}}` | {{e.g. About}} | {{brief description}} |
| 3 | {{entity_name}} | {{e.g. Service}} | `{{url}}/#{{fragment}}` | {{e.g. Services}} | {{brief description}} |

<!-- List every entity in the business knowledge graph. -->
<!-- Entities exist independently of pages — the page is just a container. -->

---

### 2. @id Architecture

**Naming Convention:** `https://{{domain}}/{{page-path}}#{{entity-type-slug}}`

| Entity | @id | Notes |
|--------|-----|-------|
| Organization | `https://{{domain}}/#organization` | Defined on homepage, referenced everywhere |
| Website | `https://{{domain}}/#website` | Defined on homepage |
| {{Person}} | `https://{{domain}}/about#{{person-slug}}` | Defined on about page |
| {{Service}} | `https://{{domain}}/services/{{slug}}#service` | One per service page |

**Rules:**
- @id is a graph identifier (internal plumbing), not a navigable URL
- @id uses hash fragments; url does not
- Once assigned, an @id must never change (use redirects if domain changes)

---

### 3. Entity-Relationship Diagram

```
┌──────────────────────┐
│    Organization       │
│ {{business_name}}     │
└──────────┬───────────┘
           │
     ┌─────┼──────┐
     │     │      │
     ▼     ▼      ▼
┌────────┐ ┌────────┐ ┌────────┐
│ Person │ │Service │ │Location│
│{{name}}│ │{{name}}│ │{{name}}│
└────────┘ └────────┘ └────────┘
```

<!-- Show all entity relationships with direction and cardinality. -->
<!-- Use Schema.org property names on relationship lines (e.g. founder, provides, location). -->

---

### 4. Relationship Mapping Table

| Subject | Relationship (Property) | Object | Cardinality | Notes |
|---------|------------------------|--------|-------------|-------|
| Organization | `founder` | Person | 1:1 / 1:N | {{context}} |
| Organization | `hasOfferCatalog` | OfferCatalog | 1:1 | {{context}} |
| Organization | `makesOffer` | Offer | 1:N | {{context}} |
| Service | `provider` | Organization | N:1 | {{context}} |
| Person | `worksFor` | Organization | N:1 | {{context}} |
| Organization | `knowsAbout` | DefinedTerm | 1:N | Topical authority |

<!-- Use specific Schema.org properties. "related to" is never acceptable. -->

---

### 5. JSON-LD @graph Specification

**Homepage @graph (foundation):**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://{{domain}}/#organization",
      "name": "{{business_name}}",
      "url": "https://{{domain}}",
      "logo": "https://{{domain}}/logo.png",
      "sameAs": [
        "{{linkedin_url}}",
        "{{facebook_url}}"
      ],
      "knowsAbout": ["{{topic_1}}", "{{topic_2}}"],
      "founder": { "@id": "https://{{domain}}/about#{{person-slug}}" },
      "hasOfferCatalog": { "@id": "https://{{domain}}/services#catalog" }
    },
    {
      "@type": "WebSite",
      "@id": "https://{{domain}}/#website",
      "url": "https://{{domain}}",
      "name": "{{site_name}}",
      "publisher": { "@id": "https://{{domain}}/#organization" }
    }
  ]
}
```

**Per-page template (reference by @id, do not redefine):**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "{{PageType — e.g. Service}}",
      "@id": "https://{{domain}}/{{page-path}}#{{entity-slug}}",
      "name": "{{entity_name}}",
      "provider": { "@id": "https://{{domain}}/#organization" }
    },
    {
      "@type": "WebPage",
      "@id": "https://{{domain}}/{{page-path}}",
      "name": "{{page_title}}",
      "isPartOf": { "@id": "https://{{domain}}/#website" },
      "about": { "@id": "https://{{domain}}/{{page-path}}#{{entity-slug}}" }
    }
  ]
}
```

<!-- Always use @graph for multi-entity pages. Never use multiple script blocks. -->
<!-- Match JSON-LD to visible page content. Every structured data claim must be supported on-page. -->

---

### 6. sameAs Link Mappings

| Entity | Profile URL | Platform | Verified |
|--------|-----------|----------|----------|
| Organization | {{linkedin_url}} | LinkedIn | Yes / No |
| Organization | {{facebook_url}} | Facebook | Yes / No |
| Organization | {{google_maps_url}} | Google Business | Yes / No |
| Person | {{linkedin_url}} | LinkedIn | Yes / No |

<!-- sameAs links must be authoritative profiles you control. Not random mentions. -->
<!-- Bidirectional verification preferred where possible. -->

---

### 7. Implementation Notes

**Deployment Order:**
1. Homepage @graph (Organization + WebSite) — deploy first
2. About page @graph (Person entities with @id references)
3. Service pages (Service entities referencing Organization by @id)
4. Remaining pages (Blog posts, location pages, etc.)

**Validation Checklist:**
- [ ] Schema Markup Validator (schema.org/validator) — full vocabulary coverage
- [ ] Google Rich Results Test — Google-specific eligibility
- [ ] All @id references resolve to defined entities
- [ ] No duplicate entity definitions across pages (reference by @id, do not redefine)
- [ ] sameAs links point to live, verified profiles

**Common Errors to Avoid:**
- Redefining an entity's properties on multiple pages instead of referencing by @id
- Using @id and url interchangeably (they serve different purposes)
- Multiple `<script type="application/ld+json">` blocks instead of a single @graph
- Structured data claims not supported by visible page content
