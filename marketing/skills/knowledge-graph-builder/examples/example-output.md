# Knowledge Graph: Apex Strategy Partners

**Business:** Apex Strategy Partners - Management Consulting
**Domain:** Professional services consulting (strategy, operations, digital transformation)
**Location:** Melbourne, VIC
**Date:** 2026-04-04

---

## 1. Node Types

| Node Type | Count | Key Properties |
|---|---|---|
| Consultant | 14 | name, role, seniority, dayRate, specialisations[], startDate |
| Client | 9 | name, industry, abn, contractValue, status |
| Project | 17 | name, type, startDate, endDate, budget, status, methodology |
| Skill | 22 | name, category, demandLevel |
| Industry | 6 | name, sectorCode, activeClientCount |

---

## 2. Edge Types

| Edge | From | To | Properties |
|---|---|---|---|
| `ASSIGNED_TO` | Consultant | Project | role, allocation%, startDate, endDate |
| `CONTRACTED_BY` | Project | Client | contractId, signedDate, value |
| `HAS_SKILL` | Consultant | Skill | proficiencyLevel (1-5), certified (bool) |
| `REQUIRES_SKILL` | Project | Skill | importance (critical/preferred), minLevel |
| `OPERATES_IN` | Client | Industry | isPrimary (bool) |
| `REFERRED_BY` | Client | Client | referralDate, referralFee |
| `MANAGES` | Consultant | Consultant | since, reportingLine |
| `DELIVERED_FOR` | Consultant | Client | projectCount, totalBilledHours, npsScore |

---

## 3. Graph Statistics

| Metric | Value |
|---|---|
| Total nodes | 68 |
| Total edges | 143 |
| Avg. degree (Consultant) | 8.2 |
| Most connected node | "Digital Transformation" (Skill) -- 11 edges |
| Orphan nodes | 0 |
| Clusters (Louvain) | 3 (Strategy, Operations, Digital) |

---

## 4. Sample Subgraph: Project Staffing

```
[Sarah Chen]---ASSIGNED_TO{role:"Lead", allocation:80%}--->[Digital Roadmap - ANZ Bank]
[Sarah Chen]---HAS_SKILL{level:5, certified:true}-------->[Digital Transformation]
[James Okonkwo]---ASSIGNED_TO{role:"Analyst", allocation:100%}--->[Digital Roadmap - ANZ Bank]
[Digital Roadmap - ANZ Bank]---CONTRACTED_BY{value:$485K}--->[ANZ Bank]
[Digital Roadmap - ANZ Bank]---REQUIRES_SKILL{importance:"critical"}--->[Digital Transformation]
[Digital Roadmap - ANZ Bank]---REQUIRES_SKILL{importance:"preferred"}--->[Change Management]
[ANZ Bank]---OPERATES_IN{isPrimary:true}--->[Financial Services]
[ANZ Bank]---REFERRED_BY{date:"2025-11-02"}--->[Telstra]
```

---

## 5. JSON-LD Representation

```json
{
  "@context": {
    "@vocab": "https://apexstrategy.com.au/ontology/",
    "schema": "https://schema.org/",
    "name": "schema:name",
    "skills": { "@id": "hasSkill", "@container": "@set" }
  },
  "@graph": [
    {
      "@type": "Consultant",
      "@id": "urn:apex:consultant:sarah-chen",
      "name": "Sarah Chen",
      "role": "Principal Consultant",
      "seniority": "Senior",
      "dayRate": { "@value": "2800", "currency": "AUD" },
      "skills": [
        {
          "@type": "SkillAssignment",
          "skill": { "@id": "urn:apex:skill:digital-transformation" },
          "proficiencyLevel": 5,
          "certified": true
        },
        {
          "@type": "SkillAssignment",
          "skill": { "@id": "urn:apex:skill:stakeholder-management" },
          "proficiencyLevel": 4,
          "certified": false
        }
      ]
    },
    {
      "@type": "Project",
      "@id": "urn:apex:project:anz-digital-roadmap",
      "name": "Digital Roadmap - ANZ Bank",
      "methodology": "Agile Discovery",
      "budget": 485000,
      "status": "active",
      "startDate": "2026-02-10",
      "endDate": "2026-07-31",
      "contractedBy": { "@id": "urn:apex:client:anz-bank" },
      "requiredSkills": [
        { "skill": { "@id": "urn:apex:skill:digital-transformation" }, "importance": "critical" }
      ],
      "assignments": [
        { "consultant": { "@id": "urn:apex:consultant:sarah-chen" }, "role": "Lead", "allocation": 0.8 },
        { "consultant": { "@id": "urn:apex:consultant:james-okonkwo" }, "role": "Analyst", "allocation": 1.0 }
      ]
    },
    {
      "@type": "Client",
      "@id": "urn:apex:client:anz-bank",
      "name": "ANZ Bank",
      "industry": { "@id": "urn:apex:industry:financial-services" },
      "abn": "11 005 357 522",
      "contractValue": 485000,
      "status": "active"
    }
  ]
}
```

---

## 6. PostgreSQL JSONB Implementation

```sql
-- Nodes table with JSONB properties
CREATE TABLE kg_nodes (
    id          TEXT PRIMARY KEY,           -- e.g. 'consultant:sarah-chen'
    node_type   TEXT NOT NULL,              -- 'Consultant', 'Client', 'Project', etc.
    properties  JSONB NOT NULL DEFAULT '{}',
    created_at  TIMESTAMPTZ DEFAULT now(),
    updated_at  TIMESTAMPTZ DEFAULT now()
);

-- Edges table with JSONB properties
CREATE TABLE kg_edges (
    id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    edge_type   TEXT NOT NULL,              -- 'ASSIGNED_TO', 'HAS_SKILL', etc.
    from_id     TEXT NOT NULL REFERENCES kg_nodes(id),
    to_id       TEXT NOT NULL REFERENCES kg_nodes(id),
    properties  JSONB NOT NULL DEFAULT '{}',
    created_at  TIMESTAMPTZ DEFAULT now(),
    UNIQUE (edge_type, from_id, to_id)
);

-- Indexes for common traversal patterns
CREATE INDEX idx_edges_from   ON kg_edges (from_id, edge_type);
CREATE INDEX idx_edges_to     ON kg_edges (to_id, edge_type);
CREATE INDEX idx_nodes_type   ON kg_nodes (node_type);
CREATE INDEX idx_nodes_props  ON kg_nodes USING GIN (properties);

-- Example: Find all consultants on a project with their skills
SELECT
    c.properties->>'name'           AS consultant_name,
    a.properties->>'role'           AS project_role,
    (a.properties->>'allocation')::NUMERIC * 100 AS allocation_pct,
    json_agg(s.properties->>'name') AS skills
FROM kg_nodes p
JOIN kg_edges a  ON a.to_id = p.id AND a.edge_type = 'ASSIGNED_TO'
JOIN kg_nodes c  ON c.id = a.from_id
LEFT JOIN kg_edges hs ON hs.from_id = c.id AND hs.edge_type = 'HAS_SKILL'
LEFT JOIN kg_nodes s  ON s.id = hs.to_id
WHERE p.id = 'project:anz-digital-roadmap'
GROUP BY c.id, c.properties, a.properties;

-- Result:
-- consultant_name | project_role | allocation_pct | skills
-- Sarah Chen      | Lead         | 80             | ["Digital Transformation","Stakeholder Management"]
-- James Okonkwo   | Analyst      | 100            | ["Data Analysis","Business Process Mapping"]
```

---

## 7. Key Insights from Graph Analysis

| Insight | Detail | Action |
|---|---|---|
| Skill concentration risk | 1 of 14 consultants holds sole "critical" rating in Cloud Architecture | Cross-train a second consultant to reduce key-person dependency |
| Revenue clustering | 62% of project value comes from Financial Services sector | Diversify pipeline into Healthcare and Government verticals |
| Referral chain | Telstra referred ANZ Bank, who referred Suncorp -- 3-node referral chain generating $1.2M | Formalise referral program with incentive structure |
| Utilisation gap | 3 consultants below 60% allocation in current quarter | Review bench strategy and consider short-term contract placements |
