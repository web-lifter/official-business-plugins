## Knowledge Graph Specification — [Business Name]

### 1. Domain Model

- **Domain:** {{business domain or industry}}
- **Scope:** {{what the graph covers — e.g. company structure, services, content topics}}
- **Primary Use Cases:**
  1. {{e.g. Generate JSON-LD structured data for website pages}}
  2. {{e.g. Power AI agent context with entity relationships}}
  3. {{e.g. Drive internal knowledge base and search}}
- **Target Environment:** JSON-LD / PostgreSQL / Neo4j / Hybrid
- **Entity Count:** {{estimated total nodes}}
- **Relationship Density:** {{estimated edges per node}}

<!-- Start small. A 10-entity graph with good relationships is more valuable than 200 entities with broken links. -->

---

### 2. Node Types

For each entity class:

**Node: {{EntityTypeName}}**
- **Schema.org Type:** {{e.g. Organization, Person, Service, Article}}
- **@id Pattern:** `https://{{domain}}/{{path}}#{{slug}}`
- **Required Properties:**

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `name` | Text | {{description}} | {{example value}} |
| `@id` | URL | Canonical identifier | {{example}} |
| `url` | URL | Human-facing page | {{example}} |

- **Optional Properties:**

| Property | Type | Description |
|----------|------|-------------|
| {{property}} | {{type}} | {{description}} |

- **Constraints:** {{validation rules — e.g. name is required, url must be unique}}

<!-- Repeat for each node type. Use Schema.org types wherever they exist. -->
<!-- For domain-specific concepts without Schema.org mapping, use custom properties and document the gap. -->

---

### 3. Edge Types

For each relationship type:

**Edge: {{relationship_name}}**
- **Schema.org Property:** {{e.g. founder, provider, worksFor}}
- **Source Node:** {{NodeType}}
- **Target Node:** {{NodeType}}
- **Cardinality:** 1:1 / 1:N / N:M
- **Required:** Yes / No
- **Description:** {{what this relationship means in the domain}}

| Relationship | Source | Target | Cardinality | Example |
|-------------|--------|--------|-------------|---------|
| `founder` | Organization | Person | 1:N | Acme Inc --founder--> Jane Doe |
| `provider` | Service | Organization | N:1 | Web Design --provider--> Acme Inc |
| `worksFor` | Person | Organization | N:1 | Jane Doe --worksFor--> Acme Inc |
| `about` | Article | DefinedTerm | N:M | Blog Post --about--> SEO |

<!-- Relationships must be typed and specific. "related to" is never acceptable. -->
<!-- Every entity must have at least one relationship — no orphan nodes. -->

---

### 4. Graph Schema

```
[Organization] ──founder──> [Person]
       │                       │
       ├──provides──> [Service] │
       │                       │
       ├──location──> [Place]  ├──worksFor──> [Organization]
       │                       │
       └──about──> [DefinedTerm]
                       ▲
                       │
              [Article]──about──┘
```

<!-- Visual representation of the complete graph structure. -->
<!-- Show all node types and edge types in a single connected diagram. -->

---

### 5. Implementation Specification

**Option A: JSON-LD @graph (for structured data / SEO)**

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "{{NodeType}}",
      "@id": "{{canonical_id}}",
      "name": "{{name}}",
      "{{relationship}}": { "@id": "{{related_entity_id}}" }
    }
  ]
}
```

**Option B: PostgreSQL (for application data)**

```sql
-- Node storage
CREATE TABLE IF NOT EXISTS entities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  entity_type TEXT NOT NULL,
  schema_type TEXT NOT NULL,  -- Schema.org type
  canonical_id TEXT UNIQUE NOT NULL,  -- @id
  name TEXT NOT NULL,
  properties JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Edge storage
CREATE TABLE IF NOT EXISTS relationships (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  source_id UUID REFERENCES entities(id),
  target_id UUID REFERENCES entities(id),
  relationship_type TEXT NOT NULL,  -- Schema.org property
  properties JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX idx_rel_source ON relationships(source_id);
CREATE INDEX idx_rel_target ON relationships(target_id);
CREATE INDEX idx_rel_type ON relationships(relationship_type);
```

**Option C: Neo4j Cypher (for graph-native storage)**

```cypher
// Create node
CREATE (n:{{NodeType}} {
  canonicalId: '{{id}}',
  name: '{{name}}'
})

// Create relationship
MATCH (a:{{SourceType}} {canonicalId: '{{source_id}}'})
MATCH (b:{{TargetType}} {canonicalId: '{{target_id}}'})
CREATE (a)-[:{{RELATIONSHIP_TYPE}}]->(b)
```

---

### 6. Quality Rules

| Rule | Check | Frequency | Action on Failure |
|------|-------|-----------|-------------------|
| No orphan nodes | Every entity has >= 1 relationship | On update | Flag for review |
| @id uniqueness | No duplicate canonical IDs | On insert | Reject duplicate |
| Required properties | All required fields populated | On insert/update | Reject incomplete |
| Relationship validity | Source and target nodes exist | On insert | Reject broken link |
| External link health | sameAs URLs return 200 | Weekly | Flag broken links |
| Schema.org compliance | All types and properties valid | On update | Warn on non-standard |

---

### 7. Maintenance Protocol

**Adding New Entities:**
1. Determine Schema.org type and assign @id following naming convention
2. Define required and optional properties
3. Create at least one relationship to an existing entity
4. Validate with quality rules before inserting

**Updating Existing Entities:**
1. Never change an entity's @id (use redirects if needed)
2. Update properties and relationships as needed
3. Re-validate sameAs links after updates

**Expanding the Graph:**
- Add new node types when the domain requires them
- Add new edge types for newly identified relationships
- Periodically review Schema.org for new types that better fit existing entities

**Review Cadence:**
- **Monthly:** Check for broken sameAs links and stale properties
- **Quarterly:** Review graph completeness against domain model
- **On content change:** Update entities when new content, services, or team members are added
