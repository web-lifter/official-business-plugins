## Dataset Quality Audit — [Dataset Name]

### 1. Dataset Overview

- **Source:** {{where the dataset came from}}
- **Format:** {{CSV / database table / API / JSON}}
- **Row Count:** {{total rows}}
- **Column Count:** {{total columns}}
- **Date Range:** {{earliest to latest record}}
- **Intended Use:** {{what this data will be used for}}
- **Primary Key:** {{column(s) that uniquely identify a row}}

<!-- Context determines severity: a 15% missing rate is critical for a model target variable but irrelevant for an unused field. -->

---

### 2. Structural Profile

**Schema Assessment:**

| Column | Declared Type | Actual Type | Nulls | Unique | Sample Values |
|--------|-------------|-------------|-------|--------|--------------|
| {{column}} | {{declared}} | {{observed}} | {{count (%)}} | {{count}} | {{3-5 examples}} |

**Relationship Assessment:**
- **Primary keys:** {{columns, uniqueness confirmed Y/N}}
- **Foreign keys:** {{relationships identified, referential integrity status}}
- **Duplicate rows:** {{count of exact duplicates, count of near-duplicates}}
- **Row completeness:** {{% of rows with no nulls across all columns}}

<!-- Structural fixes come before content fixes. Assess schema integrity first. -->

---

### 3. Content Quality Assessment

**Dimension: Completeness**
- {{column}}: {{null_count}} nulls ({{%}}) — Severity: {{High/Medium/Low}}
- Sentinel values detected: {{e.g. "N/A", 0, -1, "1900-01-01" masquerading as real data}}

**Dimension: Accuracy**
- {{column}}: {{count}} values outside expected range [{{min}}–{{max}}]
- Cross-field validation: {{inconsistencies between related columns}}

**Dimension: Consistency**
- {{column}}: {{count}} format variations (e.g. "AU" vs "Australia" vs "aus")
- Date formats: {{mixed formats found}}
- Case inconsistencies: {{examples}}

**Dimension: Timeliness**
- Most recent record: {{date}}
- Expected freshness: {{requirement}}
- Gap assessment: {{any missing time periods}}

**Dimension: Uniqueness**
- Exact duplicates: {{count}} rows
- Near-duplicates: {{count}} rows (based on {{matching criteria}})

<!-- Distinguish between data errors and data features. Nulls in cancelled_at are not missing data. -->

---

### 4. Quality Scorecard

| Dimension | Score (0-100) | Weight | Weighted Score | Status |
|-----------|--------------|--------|---------------|--------|
| Completeness | {{score}} | {{weight}} | {{weighted}} | Pass / Warn / Fail |
| Accuracy | {{score}} | {{weight}} | {{weighted}} | Pass / Warn / Fail |
| Consistency | {{score}} | {{weight}} | {{weighted}} | Pass / Warn / Fail |
| Timeliness | {{score}} | {{weight}} | {{weighted}} | Pass / Warn / Fail |
| Uniqueness | {{score}} | {{weight}} | {{weighted}} | Pass / Warn / Fail |
| **Overall** | | | **{{total}}** | **{{verdict}}** |

**Fitness for Intended Use:** {{Fit / Fit with caveats / Not fit without cleaning}}

---

### 5. Cleaning Recommendations (Prioritised)

**Priority 1 (Critical) — Must fix before use:**

1. **{{Issue title}}**
   - Impact: {{what goes wrong if not fixed}}
   - Records affected: {{count (%)}}
   - Python:
   ```python
   # {{description}}
   df['{{column}}'] = df['{{column}}'].{{operation}}
   ```
   - SQL:
   ```sql
   -- {{description}}
   UPDATE {{table}} SET {{column}} = {{fix}} WHERE {{condition}};
   ```

**Priority 2 (Important) — Should fix for reliable analysis:**

2. **{{Issue title}}**
   - Impact: {{effect on analysis}}
   - Records affected: {{count (%)}}
   - Recommendation: {{approach with code}}

**Priority 3 (Minor) — Fix if time permits:**

3. **{{Issue title}}**
   - Impact: {{minor effect}}
   - Recommendation: {{approach}}

<!-- Every recommendation includes implementation code in Python and SQL. -->

---

### 6. Cleaning Pipeline Design

Execute in this order (sequence matters):

| Step | Operation | Input | Output | Rationale |
|------|-----------|-------|--------|-----------|
| 1 | {{Structural fix — e.g. type casting}} | Raw data | Typed data | {{why first}} |
| 2 | {{Deduplication}} | Typed data | Unique data | {{before aggregation}} |
| 3 | {{Sentinel value handling}} | Unique data | Cleaned nulls | {{unmask fake values}} |
| 4 | {{Format standardisation}} | Cleaned nulls | Consistent data | {{after nulls handled}} |
| 5 | {{Outlier handling}} | Consistent data | Validated data | {{context-dependent}} |
| 6 | {{Imputation (if needed)}} | Validated data | Complete data | {{state bias introduced}} |

<!-- Order matters: structural fixes before content fixes, deduplication before aggregation. -->
<!-- Every imputation step must state the assumption and bias introduced. -->

---

### 7. Monitoring Recommendations

Checks to run on future data loads to prevent recurrence:

| Check | Frequency | Threshold | Action on Failure |
|-------|-----------|-----------|-------------------|
| Null rate on {{column}} | Every load | < {{%}} | Block load + alert |
| Row count deviation | Every load | +/- {{%}} from average | Alert for review |
| Schema change detection | Every load | Column mismatch | Block load + alert |
| Value range for {{column}} | Every load | [{{min}}, {{max}}] | Flag outliers |
| Duplicate rate | Every load | < {{%}} | Alert if exceeds |
| Freshness | Daily | < {{hours}} old | Alert if stale |

<!-- Monitoring prevents quality regressions. Automate these checks in the data pipeline. -->
