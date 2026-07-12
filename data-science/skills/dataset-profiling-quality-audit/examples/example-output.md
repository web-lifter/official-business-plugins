# Dataset Profiling & Quality Audit

**Dataset:** `customers_export_2026-03.csv` -- CRM export from a Brisbane-based retail chain
**Rows:** 14,832
**Columns:** 12
**File Size:** 2.4 MB
**Encoding:** UTF-8 (with BOM)

---

## Structural Profile

| Column | Type Detected | Non-Null | Null % | Unique | Sample Values |
|--------|--------------|----------|--------|--------|---------------|
| customer_id | INTEGER | 14,832 | 0.0% | 14,832 | 10001, 10002, 10003 |
| first_name | STRING | 14,790 | 0.3% | 8,412 | Sarah, James, Wei |
| last_name | STRING | 14,801 | 0.2% | 11,203 | O'Brien, Smith, Nguyen |
| email | STRING | 13,104 | 11.7% | 13,089 | s.obrien@gmail.com |
| phone | STRING | 11,246 | 24.2% | 11,198 | 0412 345 678, +61 7 3214 5678 |
| date_of_birth | STRING* | 12,567 | 15.3% | 9,841 | 15/03/1988, 1990-07-22, Mar 5 1975 |
| postcode | STRING* | 14,501 | 2.2% | 1,847 | 4000, 2000, 3121, NSW |
| state | STRING | 14,612 | 1.5% | 14 | QLD, Qld, Queensland, nsw |
| signup_date | STRING* | 14,832 | 0.0% | 1,203 | 2024-01-15, 15/01/2024 |
| total_spend | STRING* | 14,710 | 0.8% | 8,934 | $1,234.56, 892.3, 0 |
| loyalty_tier | STRING | 14,832 | 0.0% | 5 | Gold, Silver, Bronze, gold, N/A |
| notes | STRING | 3,218 | 78.3% | 3,102 | "VIP - handle with care", "prefers email" |

*Columns marked with `*` have mixed formats or type inconsistencies.

---

## Quality Scorecard

| Dimension | Score | Issues Found |
|-----------|-------|-------------|
| **Completeness** | 6/10 | `email` missing 11.7%, `phone` missing 24.2%, `date_of_birth` missing 15.3% |
| **Uniqueness** | 7/10 | 15 duplicate `email` addresses, `customer_id` is unique (good) |
| **Consistency** | 3/10 | `state` has 14 variants for 8 states, `date_of_birth` in 3+ date formats, `loyalty_tier` case inconsistencies |
| **Validity** | 5/10 | 237 postcodes are non-numeric (e.g., "NSW"), 48 emails fail regex, `total_spend` has currency symbols |
| **Timeliness** | 8/10 | Data is from current month export, `signup_date` range is 2019-2026 |
| **Overall** | 5.8/10 | Requires cleaning before use in analytics or migration |

---

## Issue Details

### 1. Date Format Inconsistency (Critical)

`date_of_birth` contains at least 3 distinct formats:

| Format | Example | Count | % |
|--------|---------|-------|---|
| DD/MM/YYYY | 15/03/1988 | 8,234 | 65.5% |
| YYYY-MM-DD | 1990-07-22 | 3,891 | 31.0% |
| Mon D YYYY | Mar 5 1975 | 442 | 3.5% |

`signup_date` has 2 formats: `YYYY-MM-DD` (72%) and `DD/MM/YYYY` (28%).

**Risk:** Ambiguous dates like `01/02/2024` could be 1 Feb or 2 Jan depending on interpretation.

### 2. State Normalisation (High)

The `state` column has 14 distinct values representing 8 Australian states/territories:

```
QLD (5,112), Qld (892), Queensland (234), qld (45)
NSW (3,401), nsw (112), New South Wales (89)
VIC (2,890), Vic (201)
WA (987), SA (612), TAS (198), ACT (156), NT (103)
```

### 3. Duplicate Emails (Medium)

15 email addresses appear more than once with different `customer_id` values. These likely represent:
- Household members sharing an email (8 cases -- different names)
- Genuine duplicate customer records (7 cases -- same name, different signup dates)

### 4. Invalid Postcodes (Medium)

237 rows have non-numeric postcodes. Breakdown:
- State abbreviations entered in postcode field: 189 rows
- Suburb names: 31 rows
- Empty strings (not null): 17 rows

### 5. Currency Symbols in Spend (Low)

`total_spend` contains `$` prefix in 62% of rows and comma-separated thousands in 34%. The column is stored as string, not numeric.

---

## Prioritised Cleaning Recommendations

### Priority 1: Standardise dates

```python
import pandas as pd

def parse_mixed_date(val):
    """Parse date strings in DD/MM/YYYY, YYYY-MM-DD, or Mon D YYYY format."""
    if pd.isna(val):
        return None
    for fmt in ('%d/%m/%Y', '%Y-%m-%d', '%b %d %Y', '%b %-d %Y'):
        try:
            return pd.to_datetime(val, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT

df['date_of_birth'] = df['date_of_birth'].apply(parse_mixed_date)
df['signup_date'] = df['signup_date'].apply(parse_mixed_date)
```

### Priority 2: Normalise state values

```python
STATE_MAP = {
    'qld': 'QLD', 'queensland': 'QLD',
    'nsw': 'NSW', 'new south wales': 'NSW',
    'vic': 'VIC', 'victoria': 'VIC',
    'wa': 'WA',  'western australia': 'WA',
    'sa': 'SA',  'south australia': 'SA',
    'tas': 'TAS', 'tasmania': 'TAS',
    'act': 'ACT', 'australian capital territory': 'ACT',
    'nt': 'NT',  'northern territory': 'NT',
}

df['state'] = df['state'].str.strip().str.lower().map(STATE_MAP).fillna(df['state'])
```

### Priority 3: Clean total_spend to numeric

```python
df['total_spend'] = (
    df['total_spend']
    .str.replace(r'[$,]', '', regex=True)
    .str.strip()
    .pipe(pd.to_numeric, errors='coerce')
)
```

### Priority 4: Normalise loyalty tier

```python
df['loyalty_tier'] = df['loyalty_tier'].str.strip().str.title()
df.loc[df['loyalty_tier'].isin(['N/A', 'Na', 'None', '']), 'loyalty_tier'] = None
```

### Priority 5: Validate and fix postcodes

```python
# Extract numeric postcodes; flag non-numeric for manual review
df['postcode_clean'] = df['postcode'].str.extract(r'^(\d{4})$')[0]
flagged = df[df['postcode_clean'].isna() & df['postcode'].notna()]
# -> 237 rows flagged for manual review or cross-reference with state
```

### Priority 6: Deduplicate email records

```python
# Identify and flag duplicates for manual review
dupes = df[df.duplicated(subset='email', keep=False) & df['email'].notna()]
dupes_sorted = dupes.sort_values(['email', 'signup_date'])
# -> Export 15 duplicate groups (30 rows) to 'duplicates_review.csv'
dupes_sorted.to_csv('duplicates_review.csv', index=False)
```

---

## Post-Cleaning Validation Checks

After applying fixes, verify:

- [ ] `date_of_birth` -- all values parse as valid dates, no future dates, no ages > 120
- [ ] `signup_date` -- all values parse, all within range 2019-01-01 to 2026-03-31
- [ ] `state` -- exactly 8 unique values matching Australian state/territory abbreviations
- [ ] `postcode` -- all 4-digit numeric strings, cross-validated against state
- [ ] `total_spend` -- all numeric, no negatives, reasonable range (0 to 500,000)
- [ ] `loyalty_tier` -- exactly 4 valid values: Bronze, Silver, Gold, Platinum (plus nulls)
- [ ] `email` -- no remaining duplicates (after merge/dedup decision)
