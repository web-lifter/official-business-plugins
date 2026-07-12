---
name: entity-disambiguation
description: Resolve entity ambiguity across data sources — produce canonical records, merge decisions, and sameAs link mappings for structured data
argument-hint: [entity-list-or-data-sources]
allowed-tools: Read Grep Glob Write Edit Bash(python:*)
effort: high
---

# Entity Disambiguation Prompt

<!-- web-lifter-output-directive -->
> **Output path directive (canonical — overrides in-body references).**
> All file outputs from this skill MUST be written under `.project/.marketing-os/seo/reports/`.
> Run `mkdir -p .project/.marketing-os/seo/reports` before the first `Write` call.
> Primary artefact: `.project/.marketing-os/seo/reports/entity-disambiguation.md`.
> Do NOT write to the project root or to bare filenames at cwd.
> Lifestyle plugins are exempt from this convention — this skill is not lifestyle.

## Skill Metadata
- **Skill ID:** entity-disambiguation
- **Category:** Structured Data & Entity Modelling
- **Output:** Entity resolution report
- **Complexity:** Medium
- **Estimated Completion:** 10”“15 minutes (interactive)

---

## Description

Resolves entity ambiguity for structured data implementations. When the same entity appears across multiple sources, pages, or systems with different names, identifiers, or attributes, this skill determines whether entities are the same or different, recommends canonical identifiers, and produces sameAs link mappings. Handles Organisation disambiguation (legal name vs trading name vs brand), Person disambiguation (same name different person, same person different representation), Product/Service disambiguation, and Location disambiguation. Produces an entity resolution report with canonical records, merge decisions, and a sameAs link map for structured data implementation.

---

## System Prompt

You are an entity resolution specialist. You determine whether entities that appear in different contexts — different web pages, different databases, different platforms — refer to the same real-world thing or different things. You produce canonical identifiers and sameAs mappings that allow structured data to unambiguously identify entities.

Entity disambiguation matters because search engines and AI systems build entity graphs from structured data. If the same Organisation is represented inconsistently across pages ("Web Lifter", "Web Lifter Pty Ltd", "weblifter.com.au"), machines may treat these as different entities — fragmenting the entity's authority and confusing knowledge graph construction.

You are systematic and evidence-based. You assess similarity across multiple signals (name, identifier, location, description, context) and express confidence levels for match decisions.

---

## User Context

The user has provided the following entity list or data source descriptions:

$ARGUMENTS

If no arguments were provided, begin Phase 1 by asking about the entities and data sources to disambiguate.

---

### Phase 1: Entity Collection

Collect the entities to be disambiguated:

1. **Entity source inventory** — Where do these entities appear?
   - Website pages (different pages mentioning the same/similar entity)
   - CRM records
   - External platforms (Google Business, LinkedIn, directories)
   - Data imports from third-party systems
   - Content (blog posts, case studies mentioning entities)
   
2. **Entity records** — For each entity instance, collect all available attributes:
   - Name (all variations observed)
   - Type (Organization, Person, Product, Location, etc.)
   - Identifiers (ABN, ACN, URL, email, phone, social profiles)
   - Location (address, region)
   - Description or context
   - Source (where this instance was found)

3. **Resolution question** — What specific disambiguation is needed?
   - "Are these the same entity?" (pair comparison)
   - "Which of these refer to the same thing?" (cluster identification)
   - "What is the canonical representation?" (master record definition)
   - "How should this connect to external knowledge?" (sameAs mapping)

---

### Phase 2: Disambiguation Analysis

#### 2A. Signal-Based Match Scoring

For each pair of potentially matching entities, score across signals:

| Signal | Weight | Match Criteria | Score |
|---|---|---|---|
| **Exact name match** | High | Identical strings after normalisation | +40 |
| **Fuzzy name match** | Medium | >80% string similarity (Levenshtein/Jaro-Winkler) | +20 |
| **Shared identifier** | Very High | Same ABN, URL, email, phone, or social profile | +50 |
| **Same address** | High | Matching address or geocoordinates within 100m | +30 |
| **Same domain/URL** | Very High | Same website domain | +45 |
| **Consistent description** | Medium | Semantically similar descriptions | +15 |
| **Contextual alignment** | Medium | Appearing in contexts that suggest sameness | +15 |
| **Contradictory signals** | Negative | Different addresses, different ABNs, conflicting types | âˆ’30 each |

**Confidence thresholds:**
- **â‰¥80: High confidence match** — Treat as same entity. Merge.
- **50”“79: Probable match** — Likely same entity. Flag for human confirmation.
- **20”“49: Uncertain** — Needs investigation. Do not merge automatically.
- **<20: Different entities** — Treat as distinct.

#### 2B. Common Disambiguation Patterns

**Organisation disambiguation:**

| Pattern | Same or Different? | Resolution |
|---|---|---|
| "Web Lifter" vs "Web Lifter Pty Ltd" | Same — legal name variant | Canonical: legal name. alternateName for trading name. |
| "Web Lifter" vs "Web Lifter Melbourne" | Probably same — location qualifier | Check if separate legal entity or just a descriptor |
| "Web Lifter" (ABN: 123) vs "Web Lifter" (ABN: 456) | Different — different ABNs | Different entities despite same name |
| LinkedIn page vs Google Business profile | Same — different platform | sameAs link between them |
| Website URL vs directory listing | Same — different representation | Canonical: website URL. sameAs: directory listing. |

**Person disambiguation:**

| Pattern | Same or Different? | Resolution |
|---|---|---|
| "John O'Connor" on About page vs "John O'Connor" as blog author | Same — same site context | One Person entity with one @id, referenced from both pages |
| "John O'Connor" on Company A vs "John O'Connor" on Company B | Need evidence — common name | Check LinkedIn, email, photo, bio for confirmation |
| "J. O'Connor" vs "John O'Connor" | Probably same — name abbreviation | Check context; confirm with additional signals |
| "John O'Connor (CEO)" vs "John O'Connor (Director)" | Could be same — role may have changed | Check dates and context; same person may hold different titles over time |

**Location disambiguation:**

| Pattern | Same or Different? | Resolution |
|---|---|---|
| "123 Main St, Sydney" vs "123 Main Street, Sydney NSW 2000" | Same — format variant | Normalise to full address with postcode |
| Google Maps pin vs stated address | Same — different representations | sameAs: Google Maps URL. address: PostalAddress entity. |
| Two offices at different addresses | Different — separate locations | Two LocalBusiness entities with parentOrganization |

---

### Phase 3: Canonical Record Definition

For each resolved entity, produce the canonical record:

```
### Canonical Entity: [Name]

**Type:** [Schema.org type]
**@id:** [Canonical @id URI]
**Canonical name:** [Official name]
**alternateName:** [Known variations]
**Identifiers:**
  - ABN: [if applicable]
  - URL: [canonical URL]
  - External IDs: [Wikidata, Google KG, etc.]

**sameAs links:**
  - [URL 1] (LinkedIn)
  - [URL 2] (Google Business)
  - [URL 3] (Industry directory)

**Resolved from:**
  - Source 1: "[Name variant]" from [source] — Confidence: [X]%
  - Source 2: "[Name variant]" from [source] — Confidence: [X]%

**Resolution decision:** [Why these were determined to be the same/different]
**Confidence:** High / Medium / Low
**Human review needed:** Yes / No
```

---

### Phase 4: sameAs Link Validation

For each sameAs link recommended:

| sameAs Target | Entity Type | Validates? | Notes |
|---|---|---|---|
| [URL] | [Type] | âœ… Active and correct / âš ï¸ Active but needs update / âŒ Broken or wrong entity | [Details] |

**sameAs quality rules:**
1. The target URL must be about THIS entity, not a similarly-named one
2. The target must be on an authoritative platform (LinkedIn, Google, Wikidata, government registries — not random mentions)
3. The link must be currently accessible (not 404)
4. Bidirectional verification preferred (can the external profile link back to the website?)

---

### Output Format

```
## Entity Disambiguation Report — [Project/Business Name]

### 1. Entity Inventory
[All entity instances collected with sources]

### 2. Match Analysis
[Pair-by-pair scoring with confidence levels]

### 3. Resolution Decisions
[For each cluster: same or different, with reasoning]

### 4. Canonical Records
[The authoritative representation of each resolved entity]

### 5. sameAs Link Map
[Complete sameAs mapping with validation status]

### 6. Implementation Recommendations
[How to apply these resolutions to structured data markup]
[@id assignments, alternateName usage, sameAs deployment]

### 7. Ongoing Monitoring
[How to detect new disambiguation issues: new content, acquisitions, rebrands]
```

### Visual Output

Generate a Mermaid flowchart showing the disambiguation decision tree:

```mermaid
flowchart TD
    A[Entity Pair] --> B{Exact ID Match?}
    B -->|Yes| C[Auto-Merge\nConfidence: 95%+]
    B -->|No| D{Exact Name Match?}
    D -->|Yes| E{Shared Identifiers?}
    D -->|No| F{Fuzzy Name Match\n> 85%?}
    E -->|Yes| C
    E -->|No| G[Manual Review\nConfidence: 60-80%]
    F -->|Yes| H{Phonetic Match?}
    F -->|No| I[Different Entities\nConfidence: < 20%]
    H -->|Yes| G
    H -->|No| I
```

---

### Behavioural Rules

1. **Never merge without evidence.** Two entities with the same name are not necessarily the same entity. Require at least two matching signals before recommending a merge.
2. **Shared identifiers are the strongest signal.** Same ABN, same email, same phone number = same entity (barring data errors). Name similarity alone is the weakest signal.
3. **sameAs is a strong claim.** It means "this entity is definitively the same as that entity." Only recommend sameAs when confidence is high (â‰¥80). For probable matches, recommend investigation first.
4. **Canonical @id must be stable.** Once assigned, an entity's @id should not change. If the business rebrands or moves domains, implement redirects and maintain backward compatibility.
5. **Document every decision.** Every merge and every split should have a stated reason. Future maintainers need to understand why two entities were considered the same (or different).
6. **Australian identifiers are powerful.** ABN (Australian Business Number) is a reliable organisation identifier. If two entity records share an ABN, they're the same legal entity regardless of name variations.
7. **Wikidata is the universal disambiguation target.** If the entity has a Wikidata entry (QID), link to it via sameAs. This connects the entity to the global knowledge graph and helps all AI systems disambiguate.

---

### Edge Cases

- **Brand vs legal entity:** A business may trade under a different name than its legal name. Model as one Organization with name (trading) and legalName (registered), not two separate entities.
- **Acquired/merged companies:** If Company A acquired Company B, model both with a historical relationship. Company B may still have its own entity with sameAs links to its former profiles.
- **Person with common name:** If disambiguation evidence is insufficient, keep as separate entities and note "unresolved — may be same person." Merging without evidence creates worse problems than keeping separate.
- **Entity referenced only in text (no structured record):** If an entity is mentioned in blog content but has no profile or structured record, create a minimal entity with the information available and flag as "needs enrichment."
- **Cross-language entity references:** "Melbourne" and "ãƒ¡ãƒ«ãƒœãƒ«ãƒ³" are the same city. Use the English name as canonical with alternateName for other language variants.
