## Entity Disambiguation Report — [Project/Business Name]

### 1. Entity Inventory

| # | Entity Name | Source | Type | Identifiers | Notes |
|---|------------|--------|------|-------------|-------|
| 1 | {{entity_name}} | {{source — e.g. website, CRM, listing}} | Organization / Person / Place | {{ABN, email, URL, etc.}} | {{initial notes}} |

<!-- Collect all entity instances across all sources before analysis. -->
<!-- Include every variant, alias, and reference found. -->

---

### 2. Disambiguation Analysis

**Cluster: {{entity_group_label}}**

Entities under consideration:
- Instance A: "{{name_variant_1}}" from {{source_1}}
- Instance B: "{{name_variant_2}}" from {{source_2}}

| Signal | Instance A | Instance B | Match? | Weight |
|--------|-----------|-----------|--------|--------|
| Name | {{value}} | {{value}} | Exact / Partial / No | High / Medium / Low |
| ABN / Tax ID | {{value}} | {{value}} | Yes / No / N/A | Very High |
| Address | {{value}} | {{value}} | Match / Partial / No | High |
| Phone | {{value}} | {{value}} | Match / No / N/A | High |
| Email domain | {{value}} | {{value}} | Match / No / N/A | Medium |
| Website | {{value}} | {{value}} | Match / No / N/A | High |

**Decision:** MERGE / KEEP SEPARATE / INVESTIGATE FURTHER
**Confidence:** {{0-100}}%
**Reasoning:** {{2-3 sentences explaining the decision with evidence}}

<!-- Repeat for each cluster of potentially matching entities. -->
<!-- Never merge without at least two matching signals. -->

---

### 3. Match Scoring Results

| Cluster | Instances | Decision | Confidence | Key Evidence |
|---------|-----------|----------|------------|-------------|
| {{label}} | A, B | Merge | {{%}} | {{primary evidence}} |
| {{label}} | C, D | Keep Separate | {{%}} | {{differentiating evidence}} |
| {{label}} | E, F, G | Merge (E+F), Separate (G) | {{%}} | {{reasoning summary}} |

**Score Distribution:**
- High confidence (>80%): {{count}} clusters
- Medium confidence (50-80%): {{count}} clusters
- Low confidence (<50%): {{count}} clusters — flagged for manual review

---

### 4. Canonical Records

For each resolved entity, the authoritative representation:

**Entity: {{canonical_name}}**
- **@id:** `{{canonical_id — e.g. https://example.com/#org}}`
- **Type:** {{Schema.org type — Organization, Person, LocalBusiness}}
- **Name:** {{canonical name}}
- **legalName:** {{registered legal name, if different}}
- **alternateName:** [{{variant_1}}, {{variant_2}}]
- **Identifiers:** {{ABN, registration numbers}}
- **URL:** {{canonical URL}}
- **Merged from:** {{list of source instances that resolved to this record}}

<!-- The canonical record is the single source of truth for this entity going forward. -->
<!-- @id must be stable — once assigned, it should not change. -->

---

### 5. sameAs Link Mappings

| Canonical Entity | @id | sameAs Links | Validation Status |
|-----------------|-----|-------------|-------------------|
| {{entity_name}} | `{{@id}}` | `{{wikidata_url}}`, `{{linkedin_url}}`, `{{google_maps_url}}` | Verified / Pending |

```json
{
  "@type": "Organization",
  "@id": "{{canonical_id}}",
  "name": "{{canonical_name}}",
  "sameAs": [
    "{{external_profile_url_1}}",
    "{{external_profile_url_2}}"
  ]
}
```

<!-- sameAs is a strong claim: this entity IS that entity. Only use when confidence >= 80%. -->
<!-- Wikidata (QID) is the preferred universal disambiguation target. -->

---

### 6. Confidence Summary

| Category | Count | Action |
|----------|-------|--------|
| Confirmed merges (>80% confidence) | {{count}} | Implement as canonical records |
| Probable merges (50-80%) | {{count}} | Flag for manual review before merging |
| Confirmed separates (>80% confidence) | {{count}} | Maintain as distinct entities |
| Unresolved (<50% confidence) | {{count}} | Requires additional data collection |

---

### 7. Unresolved Entities

| Entity | Issue | Missing Evidence | Recommended Action |
|--------|-------|-----------------|-------------------|
| {{entity_name}} | {{why it could not be resolved}} | {{what data would resolve it}} | {{next step}} |

<!-- Entities that cannot be confidently resolved should remain separate until evidence is available. -->
<!-- Merging without evidence creates worse problems than keeping entities separate. -->

**Monitoring for Future Disambiguation:**
- New content published: Re-check entity references for new matching signals
- Business acquisitions or rebrands: Update canonical records and sameAs mappings
- New external profiles created: Add to sameAs link mappings
