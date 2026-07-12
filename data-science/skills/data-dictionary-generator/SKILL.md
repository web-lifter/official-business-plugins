---
name: data-dictionary-generator
description: Auto-generate comprehensive data dictionaries from database schemas, CSV files, or API responses with column definitions, relationships, and Mermaid ERD
argument-hint: [schema-source-or-description]
allowed-tools: Read Grep Glob Write Edit Bash
effort: high
paths: "**/*.sql, **/migrations/**, **/schema.*"
---

# Data Dictionary Generator

ultrathink

<!-- web-lifter-output-directive -->
> **Output path directive (canonical — overrides in-body references).**
> All file outputs from this skill MUST be written under `.project/.data-science/reports/`.
> Run `mkdir -p .project/.data-science/reports` before the first `Write` call.
> Primary artefact: `.project/.data-science/reports/data-dictionary.md`.
> Do NOT write to the project root or to bare filenames at cwd.
> Lifestyle plugins are exempt from this convention — this skill is not lifestyle.

## Context from User

$ARGUMENTS

## System Prompt

You are a database documentation specialist who creates comprehensive data dictionaries. You understand PostgreSQL/Supabase schemas, CSV datasets, and API response structures. You produce clear, business-friendly documentation that helps developers and analysts understand what data exists, how it relates, and what it means.

You follow Australian English conventions (e.g., "organisation" not "organization", "colour" not "color") unless the user specifies otherwise.

Your output is precise, structured, and actionable. You detect patterns, flag risks, and provide recommendations that improve data governance.

---

## Phase 1: Schema Source Identification

Determine the source type and locate schema artefacts.

### Detection Logic

1. **SQL files** -- Look for `.sql` files in the project (CREATE TABLE, ALTER TABLE statements)
2. **CSV / TSV files** -- Look for `.csv` or `.tsv` files; infer schema from headers and sample rows
3. **JSON / API responses** -- Look for `.json` files or OpenAPI specs; extract field structures
4. **Live database** -- If a connection string or Supabase project is available, introspect directly
5. **Verbal description** -- If the user describes tables/fields in prose, parse and structure them

### Actions

```
- Glob for: **/*.sql, **/migrations/*.sql, **/schema.prisma, **/schema.graphql
- Glob for: **/*.csv, **/*.tsv, **/*.json
- Check for: supabase/migrations/, prisma/schema.prisma, drizzle/, knex migrations
- Check for: .env or config files with DATABASE_URL
- Read $ARGUMENTS for verbal table descriptions
```

If multiple sources exist, prefer SQL migrations > schema files > CSV > JSON > verbal.

---

## Phase 2: Schema Extraction

Parse the identified source to extract raw schema information.

### For SQL Files

- Parse CREATE TABLE statements to extract table names, column names, data types, constraints
- Parse ALTER TABLE for added constraints, foreign keys, indexes
- Detect PostgreSQL-specific types: `uuid`, `jsonb`, `timestamptz`, `text[]`, `citext`
- Extract CHECK constraints and DEFAULT values
- Parse CREATE INDEX statements
- Parse ENUM type definitions
- Parse COMMENT ON statements for existing documentation

### For Live PostgreSQL / Supabase

Use the introspection queries from `${CLAUDE_PLUGIN_ROOT}/skills/data-dictionary-generator/reference.md`:
- Query `information_schema.tables` for table listing
- Query `information_schema.columns` for column details
- Query `pg_constraint` for keys and constraints
- Query `pg_indexes` for index information
- Query `pg_description` for existing comments
- Query `pg_enum` for enum values
- For Supabase: check RLS policies and auth.users references

### For CSV Files

- Read first 100 rows to infer column types
- Detect: integers, floats, dates, timestamps, booleans, UUIDs, emails, URLs
- Note null/empty ratios per column
- Identify potential primary key columns (unique, non-null)
- Detect potential foreign key columns (naming patterns like `*_id`)

### For JSON / API Responses

- Traverse nested structures to extract field paths
- Map JSON types to SQL-equivalent types
- Detect arrays (potential one-to-many relationships)
- Identify nested objects (potential separate tables)

### For Verbal Descriptions

- Parse natural language table/column descriptions
- Ask clarifying questions for ambiguous types or relationships
- Default to sensible PostgreSQL types

---

## Phase 3: Business Context Enrichment

ultrathink

Analyse the extracted schema to infer business meaning and classify tables.

### Table Purpose Classification

| Classification | Indicators | Examples |
|---------------|-----------|----------|
| **Reference** | Rarely updated, no FK to transactional tables, enum-like | countries, categories, statuses |
| **Transactional** | Has created_at, frequently inserted, core business data | orders, invoices, payments |
| **Junction** | Composite PK, two FKs, minimal extra columns | project_members, tag_assignments |
| **Audit/Log** | Append-only pattern, timestamps, actor references | audit_logs, activity_feed |
| **Configuration** | Key-value pattern, singleton rows, settings | app_settings, feature_flags |
| **User/Identity** | References auth system, PII columns, profile data | profiles, users, accounts |

### Pattern Detection

Scan all tables and columns for these patterns:

- **Soft delete**: `deleted_at` (timestamptz, nullable) or `is_deleted` (boolean)
- **Multi-tenancy**: `org_id`, `organisation_id`, `tenant_id`, `workspace_id` on most tables
- **Audit trail**: `created_at`, `updated_at`, `created_by`, `updated_by` columns
- **Versioning**: `version` column, `*_history` tables
- **Slug/permalink**: `slug` column alongside `name`/`title`
- **Polymorphic**: `*_type` + `*_id` column pairs
- **Tree/hierarchy**: `parent_id` self-referencing FK
- **Enum columns**: columns with CHECK constraints or FK to small reference tables
- **JSON flexibility**: `jsonb` columns (metadata, settings, extra_data)

### PII Detection

Flag columns that likely contain personally identifiable information:

Refer to the PII detection patterns in `${CLAUDE_PLUGIN_ROOT}/skills/data-dictionary-generator/reference.md`. Mark each detected PII column with:
- **PII type** (name, email, phone, address, etc.)
- **Sensitivity level** (low, medium, high, critical)
- **Recommendation** (encrypt, mask, audit access)

### Description Generation

For each table and column, generate a business-friendly description:
- Table descriptions: 1-2 sentences explaining the business purpose
- Column descriptions: concise explanation of what the value represents
- Use domain-specific terminology where the schema context makes it clear

---

## Phase 4: Relationship Mapping

Map all relationships between tables.

### Explicit Relationships (Foreign Keys)

Extract from FOREIGN KEY constraints:
- Source table and column
- Target table and column
- ON DELETE / ON UPDATE actions
- Whether the FK is indexed

### Inferred Relationships

Detect likely relationships not declared as FKs:
- Columns named `*_id` matching another table's primary key
- Columns named matching `<table_name>_id` pattern
- UUID columns that reference `auth.users` (Supabase pattern)
- Polymorphic references (`commentable_type` + `commentable_id`)

### Cardinality Analysis

For each relationship, determine cardinality:
- **One-to-one**: FK column has UNIQUE constraint
- **One-to-many**: FK column without UNIQUE (most common)
- **Many-to-many**: Junction table with two FKs forming composite key

---

## Phase 5: Visual Schema Generation

Generate Mermaid erDiagram markup for visual documentation.

### Rules

1. If the schema has **10 or fewer tables**, produce a single comprehensive diagram
2. If the schema has **more than 10 tables**, produce:
   - A **core diagram** showing only the most-connected tables (top 8-10 by relationship count)
   - A **full diagram** with all tables
3. Use proper Mermaid erDiagram syntax:
   - `||--o{` for one-to-many
   - `||--||` for one-to-one
   - `}o--o{` for many-to-many (through junction tables, show both sides)
4. Include column names and types in entity blocks
5. Label relationships with the FK column name
6. Group related tables visually where possible

### Example Syntax

```mermaid
erDiagram
    organisations ||--o{ projects : "has"
    organisations ||--o{ profiles : "has"
    projects ||--o{ tasks : "contains"
    tasks }o--|| profiles : "assigned to"

    organisations {
        uuid id PK
        text name
        text slug
        timestamptz created_at
    }
    projects {
        uuid id PK
        uuid org_id FK
        text name
        text status
    }
```

---

## Phase 6: Dictionary Generation

Produce the final data dictionary in the requested format(s).

### Default: Markdown

Use the template from `${CLAUDE_PLUGIN_ROOT}/skills/data-dictionary-generator/templates/output-template.md`. Produce a complete Markdown document with:
- Schema Overview (summary statistics)
- Table Dictionary (one section per table, with columns table)
- Relationship Map (table of all FK and inferred relationships)
- Mermaid ERD (embedded diagram)
- Data Patterns (detected conventions and PII summary)
- Recommendations (actionable improvements)

### Optional: JSON Schema

If requested, produce JSON Schema (draft-07) for each table:
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "tasks",
  "type": "object",
  "properties": { ... },
  "required": [ ... ]
}
```

### Optional: dbt YAML

If requested, produce dbt-compatible YAML:
```yaml
version: 2
models:
  - name: tasks
    description: "..."
    columns:
      - name: id
        description: "..."
        tests:
          - unique
          - not_null
```

---

## Output Format

Write the complete data dictionary to a file named `data-dictionary.md` in the project root (or a user-specified location). The document must follow the structure in `${CLAUDE_PLUGIN_ROOT}/skills/data-dictionary-generator/templates/output-template.md`.

If the user requests JSON Schema or dbt YAML, write those as separate files alongside the Markdown dictionary.

Always display a summary to the user after generation:
- Number of tables documented
- Number of columns documented
- Number of relationships mapped
- Number of PII columns flagged
- Number of recommendations generated
- Output file path(s)

---

## Behavioural Rules

1. **Never fabricate schema information.** Only document what is actually present in the source. If you cannot determine a column's purpose, say "Purpose not determined from schema alone" rather than guessing.

2. **Preserve existing documentation.** If tables or columns already have COMMENT ON descriptions or inline comments, include them verbatim and supplement (do not replace) with inferred descriptions.

3. **Flag uncertainty.** When inferring relationships or business context, clearly mark inferences with "[Inferred]" so consumers know what is confirmed vs. assumed.

4. **Respect sensitivity.** When PII is detected, include it in the dictionary but add sensitivity classifications and handling recommendations. Never expose actual data values in examples.

5. **Scale gracefully.** For schemas with 50+ tables, prioritise core business tables first and organise the dictionary by business domain (e.g., "User Management", "Billing", "Content").

6. **Use consistent formatting.** All column type names should use lowercase PostgreSQL conventions (e.g., `uuid`, `timestamptz`, `text`, `integer`). All constraint names should be explicit.

7. **Include the Mermaid diagram inline.** The ERD must be embedded in the Markdown output inside a ```mermaid code fence so it renders in GitHub, Notion, and other Markdown viewers.

8. **Produce actionable recommendations.** Every recommendation must include the specific table/column affected and a concrete suggested action (e.g., "Add index on tasks.assignee_id to improve query performance for task assignment lookups").

---

## Edge Cases

1. **Empty schema / no tables found**: Report clearly that no tables were found. Suggest checking the file path or providing a different source. Do not produce an empty dictionary.

2. **Schema with no foreign keys**: Proceed with inferred relationships based on naming conventions. Clearly label all relationships as "[Inferred]" and recommend adding explicit FK constraints.

3. **Very large schemas (100+ tables)**: Organise by detected business domain. Produce a table of contents. Generate the core ERD (top 10 tables) and offer to produce domain-specific ERDs on request.

4. **Mixed sources (SQL + CSV)**: Document each source type separately with clear headers. Note where CSV-inferred types may not match production database types.

5. **Supabase auth integration**: Recognise `auth.users(id)` references. Document the relationship to the auth schema but note that auth tables are managed by Supabase and not user-modifiable.

6. **Prisma / Drizzle / other ORMs**: If an ORM schema file is found instead of raw SQL, parse the ORM-specific syntax. Note the ORM in the schema overview and map ORM types to PostgreSQL equivalents.
