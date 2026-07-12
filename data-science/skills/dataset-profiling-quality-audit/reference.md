# Dataset Profiling Quality Audit -- Reference

Supplementary reference material for the dataset-profiling-quality-audit skill. Use alongside SKILL.md for scoring rubrics, detection methods, code templates, and the quality scorecard format.

---

## Table of Contents

- [Quality Dimension Scoring Rubrics](#quality-dimension-scoring-rubrics)
- [Missingness Classification Guide](#missingness-classification-guide)
- [Common Type Mismatch Patterns](#common-type-mismatch-patterns)
- [Outlier Detection Methods Reference](#outlier-detection-methods-reference)
- [Data Cleaning Operation Templates](#data-cleaning-operation-templates)
- [Quality Scorecard Template](#quality-scorecard-template)

---

## Quality Dimension Scoring Rubrics

### Completeness (0--100)

Measures how much expected data is actually present.

| Score Range | Rating | Criteria |
|---|---|---|
| 90--100 | Excellent | <2% missing across all fields; no required field has nulls; no sentinel values masquerading as data |
| 75--89 | Good | <5% missing on most fields; required fields complete; a few optional fields have moderate gaps |
| 50--74 | Acceptable | 5--15% missing on some fields; some required fields have gaps; sentinel values detected but limited |
| 25--49 | Poor | 15--30% missing on multiple fields; required fields have significant gaps; widespread sentinel values |
| 0--24 | Critical | >30% missing on key fields; required fields routinely null; dataset unreliable for intended use |

**Calculation:**

```python
def score_completeness(df: pd.DataFrame, required_fields: list[str]) -> float:
    total_cells = df.shape[0] * df.shape[1]
    non_null_cells = df.notna().sum().sum()
    base_score = (non_null_cells / total_cells) * 100

    # Penalise required field nulls more heavily
    required_penalty = 0
    for field in required_fields:
        if field in df.columns:
            null_pct = df[field].isna().mean()
            required_penalty += null_pct * 20  # Up to 20 points penalty per required field

    return max(0, min(100, base_score - required_penalty))
```

### Validity (0--100)

Measures whether values conform to expected formats, ranges, and domains.

| Score Range | Rating | Criteria |
|---|---|---|
| 90--100 | Excellent | >98% of values pass format, range, and domain checks; cross-field rules hold |
| 75--89 | Good | >95% pass; a few fields have minor format inconsistencies; cross-field rules mostly hold |
| 50--74 | Acceptable | >85% pass; some fields have significant format issues; a few cross-field violations |
| 25--49 | Poor | >70% pass; multiple fields fail format checks; frequent cross-field violations |
| 0--24 | Critical | <70% pass; widespread type mismatches; business rules routinely violated |

**Calculation:**

```python
def score_validity(df: pd.DataFrame, validation_rules: dict) -> float:
    """
    validation_rules format:
    {
        "email": {"regex": r"^[\w\.\+\-]+@[\w\-]+\.[\w\.\-]+$"},
        "age": {"min": 0, "max": 120},
        "status": {"values": ["active", "inactive", "pending"]},
    }
    """
    total_checks = 0
    passed_checks = 0

    for field, rules in validation_rules.items():
        if field not in df.columns:
            continue
        non_null = df[field].dropna()
        total_checks += len(non_null)

        if "regex" in rules:
            passed_checks += non_null.astype(str).str.match(rules["regex"]).sum()
        elif "min" in rules and "max" in rules:
            numeric = pd.to_numeric(non_null, errors="coerce")
            passed_checks += ((numeric >= rules["min"]) & (numeric <= rules["max"])).sum()
        elif "values" in rules:
            passed_checks += non_null.isin(rules["values"]).sum()

    return (passed_checks / max(total_checks, 1)) * 100
```

### Consistency (0--100)

Measures whether the same concept is represented the same way throughout the dataset.

| Score Range | Rating | Criteria |
|---|---|---|
| 90--100 | Excellent | Uniform formats, casing, and encoding; cross-table references match; no unit mixing |
| 75--89 | Good | Minor casing or format variations in 1--2 fields; cross-table references mostly match |
| 50--74 | Acceptable | Multiple fields have format inconsistencies; some cross-table mismatches; mixed encodings present |
| 25--49 | Poor | Widespread format mixing; date columns have 3+ formats; categorical fields have many variant spellings |
| 0--24 | Critical | No consistent formatting across fields; cross-table joins unreliable; mixed units without indicators |

### Uniqueness (0--100)

Measures whether records and keys are appropriately unique.

| Score Range | Rating | Criteria |
|---|---|---|
| 90--100 | Excellent | No exact duplicates; primary keys unique; business keys unique where expected |
| 75--89 | Good | <1% exact duplicates; primary keys unique; a few business key near-duplicates |
| 50--74 | Acceptable | 1--5% duplicates; primary keys unique but business keys have issues; near-duplicates detected |
| 25--49 | Poor | 5--15% duplicates; some primary key violations; deduplication required before use |
| 0--24 | Critical | >15% duplicates; primary key violations; data reliability severely compromised |

### Timeliness (0--100)

Measures whether data is sufficiently current for its intended use.

| Score Range | Rating | Criteria |
|---|---|---|
| 90--100 | Excellent | Data current within SLA; no gaps in expected update frequency; full temporal coverage |
| 75--89 | Good | Data within 1.5x SLA; minor gaps in update frequency; adequate temporal coverage |
| 50--74 | Acceptable | Data within 2x SLA; some gaps; temporal coverage missing recent periods |
| 25--49 | Poor | Data significantly stale; frequent gaps; temporal coverage inadequate for analysis |
| 0--24 | Critical | Data severely outdated; large temporal gaps; insufficient for any time-sensitive analysis |

### Accuracy (0--100)

Measures whether data values correctly represent real-world entities and events. Hardest to assess without a ground truth source.

| Score Range | Rating | Criteria |
|---|---|---|
| 90--100 | Excellent | Cross-validated against external sources; business rules hold; no suspicious patterns |
| 75--89 | Good | Spot checks against source systems pass; minor discrepancies in derived fields |
| 50--74 | Acceptable | Some fields diverge from source; aggregations show unexplained variance; sampling reveals errors |
| 25--49 | Poor | Frequent mismatches with source systems; calculated fields incorrect; aggregations unreliable |
| 0--24 | Critical | Data does not reflect reality; widespread errors; not fit for decision-making |

---

## Missingness Classification Guide

### MCAR -- Missing Completely At Random

The probability of a value being missing is unrelated to both the missing value itself and any other observed variable.

**Detection methods:**

```python
# Little's MCAR test (approximate with chi-squared approach)
from scipy import stats

def test_mcar_approximate(df: pd.DataFrame, column: str, group_column: str) -> dict:
    """Test if missingness in column is independent of group_column."""
    contingency = pd.crosstab(
        df[group_column].fillna("__UNKNOWN__"),
        df[column].isna().map({True: "missing", False: "present"})
    )
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency)
    return {
        "test": "chi-squared independence",
        "chi2": round(chi2, 4),
        "p_value": round(p_value, 4),
        "is_mcar": p_value > 0.05,  # Fail to reject null = consistent with MCAR
        "interpretation": (
            "Missingness appears random (MCAR)" if p_value > 0.05
            else f"Missingness is associated with {group_column} (not MCAR)"
        )
    }

# Visual check: compare distributions of other variables
# between rows where target column is missing vs present
def compare_missing_vs_present(df: pd.DataFrame, target_col: str, compare_cols: list[str]):
    missing_mask = df[target_col].isna()
    results = {}
    for col in compare_cols:
        if df[col].dtype in ["float64", "int64"]:
            present_mean = df.loc[~missing_mask, col].mean()
            missing_mean = df.loc[missing_mask, col].mean()
            t_stat, p_val = stats.ttest_ind(
                df.loc[~missing_mask, col].dropna(),
                df.loc[missing_mask, col].dropna(),
                equal_var=False
            )
            results[col] = {
                "present_mean": round(present_mean, 2),
                "missing_mean": round(missing_mean, 2),
                "p_value": round(p_val, 4),
                "significant_difference": p_val < 0.05
            }
    return results
```

**Treatment strategies:**
- Listwise deletion (drop rows) -- safe when missingness is low (<5%)
- Mean/median imputation -- simple, reduces variance
- Random imputation from observed distribution -- preserves distribution shape

### MAR -- Missing At Random

The probability of a value being missing depends on other observed variables but not on the missing value itself.

**Detection clues:**
- Missing values concentrated in specific segments (e.g., younger respondents skip income question)
- Missingness rate differs significantly across categories of another variable
- Logistic regression predicting missingness achieves above-chance accuracy using observed variables

```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

def detect_mar(df: pd.DataFrame, target_col: str, predictor_cols: list[str]) -> dict:
    """Test if missingness can be predicted from other variables (MAR indicator)."""
    y = df[target_col].isna().astype(int)
    X = df[predictor_cols].copy()

    # Encode categoricals and fill NAs in predictors
    for col in X.columns:
        if X[col].dtype == "object":
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].fillna("__MISSING__"))
        else:
            X[col] = X[col].fillna(X[col].median())

    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X, y)
    accuracy = model.score(X, y)
    baseline = 1 - y.mean()  # Majority class baseline

    return {
        "target_column": target_col,
        "model_accuracy": round(accuracy, 4),
        "baseline_accuracy": round(baseline, 4),
        "accuracy_lift": round(accuracy - baseline, 4),
        "likely_mar": accuracy - baseline > 0.05,
        "top_predictors": dict(zip(predictor_cols, model.coef_[0].round(4)))
    }
```

**Treatment strategies:**
- Multiple imputation (MICE) -- gold standard for MAR
- Imputation using correlated variables (regression, kNN)
- Conditional mean/median by segment

```python
# Multiple imputation with IterativeImputer (sklearn MICE equivalent)
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

def impute_mar(df: pd.DataFrame, numeric_cols: list[str]) -> pd.DataFrame:
    """Multiple imputation for MAR data using MICE-style approach."""
    imputer = IterativeImputer(
        max_iter=10,
        random_state=42,
        sample_posterior=True  # Adds appropriate randomness
    )
    df[numeric_cols] = imputer.fit_transform(df[numeric_cols])
    return df
```

### MNAR -- Missing Not At Random

The probability of a value being missing depends on the missing value itself.

**Detection clues:**
- Domain knowledge suggests self-censoring (high earners skip income, dissatisfied customers skip NPS)
- After accounting for all observed variables, missingness pattern still unexplained
- Truncation patterns (values missing above or below a threshold)

**Detection approach:**

```python
def detect_mnar_indicators(df: pd.DataFrame, target_col: str) -> dict:
    """Heuristic indicators that missingness may be MNAR."""
    indicators = {}
    non_null = df[target_col].dropna()

    # Check for truncation: is the distribution of observed values suspiciously
    # bounded compared to what domain knowledge suggests?
    indicators["observed_min"] = non_null.min()
    indicators["observed_max"] = non_null.max()
    indicators["observed_skew"] = round(non_null.skew(), 3)

    # High skew + high missingness often indicates MNAR
    # (extreme values are missing, compressing the observed distribution)
    missing_rate = df[target_col].isna().mean()
    indicators["missing_rate"] = round(missing_rate, 4)
    indicators["skew_concern"] = abs(non_null.skew()) > 1.5 and missing_rate > 0.1

    return indicators
```

**Treatment strategies (limited -- MNAR cannot be fully corrected from observed data):**
- Sensitivity analysis: run analysis with different assumptions about missing values
- Bounds analysis: compute best-case and worst-case results
- Pattern-mixture models (advanced statistical technique)
- Document the bias and its likely direction; do not impute and pretend the problem is solved

---

## Common Type Mismatch Patterns

| Expected Type | Actual Pattern | Detection Query (PostgreSQL) | Fix |
|---|---|---|---|
| INTEGER | Contains decimal values (`"10.5"`) | `SELECT * FROM t WHERE col::TEXT LIKE '%.%'` | `ROUND(col)` or change type to NUMERIC |
| INTEGER | Contains text (`"N/A"`, `"none"`, `""`) | `SELECT * FROM t WHERE col !~ '^\d+$'` | Replace sentinels with NULL, then cast |
| NUMERIC | Formatted with commas (`"1,234.56"`) | `SELECT * FROM t WHERE col::TEXT LIKE '%,%'` | `REPLACE(col, ',', '')::NUMERIC` |
| NUMERIC | Currency symbols (`"$100"`, `"USD 50"`) | `SELECT * FROM t WHERE col::TEXT ~ '[^0-9.\-]'` | `REGEXP_REPLACE(col, '[^0-9.\-]', '', 'g')::NUMERIC` |
| DATE | Mixed formats (`2024-01-15`, `15/01/2024`) | `SELECT col, COUNT(*) FROM t GROUP BY LENGTH(col)` | Detect format per row, parse with `TO_DATE()` |
| DATE | Excel serial numbers (`45678`) | `SELECT * FROM t WHERE col ~ '^\d{5}$'` | `DATE '1899-12-30' + col::INT` |
| DATE | Unix timestamps (`1705276800`) | `SELECT * FROM t WHERE col ~ '^\d{10}$'` | `TO_TIMESTAMP(col::BIGINT)` |
| BOOLEAN | String representations (`"yes"`, `"Y"`, `"1"`, `"true"`) | `SELECT DISTINCT col FROM t` | `CASE WHEN LOWER(col) IN ('yes','y','1','true','t') THEN TRUE ... END` |
| EMAIL | Missing @ or domain | `SELECT * FROM t WHERE col NOT LIKE '%@%.%'` | Flag for manual review or enrichment |
| PHONE | Mixed formats (`+61 400 123 456`, `0400123456`) | `SELECT * FROM t WHERE LENGTH(REGEXP_REPLACE(col, '\D', '', 'g')) NOT BETWEEN 9 AND 15` | `REGEXP_REPLACE(col, '\D', '', 'g')` then format consistently |
| POSTCODE (AU) | Wrong length or non-numeric | `SELECT * FROM t WHERE col !~ '^\d{4}$'` | Validate against AU postcode reference; flag invalid |
| JSON in TEXT | JSON string stored as TEXT | `SELECT * FROM t WHERE col::TEXT LIKE '{%' OR col::TEXT LIKE '[%'` | `col::JSONB` after validation |

**pandas detection:**

```python
def detect_type_mismatches(df: pd.DataFrame) -> dict:
    """Detect columns where actual content does not match the declared dtype."""
    issues = {}
    for col in df.columns:
        if df[col].dtype == "object":
            non_null = df[col].dropna()
            if len(non_null) == 0:
                continue

            # Check if all values are numeric
            numeric_pct = pd.to_numeric(non_null, errors="coerce").notna().mean()
            if numeric_pct > 0.8:
                issues[col] = {
                    "declared": "object",
                    "likely": "numeric",
                    "numeric_pct": round(numeric_pct, 3),
                    "non_numeric_samples": non_null[
                        pd.to_numeric(non_null, errors="coerce").isna()
                    ].head(5).tolist()
                }

            # Check if all values are dates
            date_pct = pd.to_datetime(non_null, errors="coerce", format="mixed").notna().mean()
            if date_pct > 0.8 and col not in issues:
                issues[col] = {
                    "declared": "object",
                    "likely": "datetime",
                    "date_pct": round(date_pct, 3)
                }

            # Check if boolean-like
            bool_values = {"true", "false", "yes", "no", "y", "n", "1", "0", "t", "f"}
            bool_pct = non_null.str.lower().isin(bool_values).mean()
            if bool_pct > 0.9 and col not in issues:
                issues[col] = {
                    "declared": "object",
                    "likely": "boolean",
                    "bool_pct": round(bool_pct, 3)
                }

    return issues
```

---

## Outlier Detection Methods Reference

### IQR Method

Robust general-purpose method. Works well for skewed distributions.

```python
def detect_outliers_iqr(series: pd.Series, multiplier: float = 1.5) -> pd.Series:
    """Flag outliers using the IQR method. Returns boolean mask."""
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    return (series < lower_bound) | (series > upper_bound)

# Usage
outlier_mask = detect_outliers_iqr(df["amount"])
print(f"Outliers: {outlier_mask.sum()} ({outlier_mask.mean():.1%})")
print(f"Bounds: [{df['amount'].quantile(0.25) - 1.5 * (df['amount'].quantile(0.75) - df['amount'].quantile(0.25)):.2f}, "
      f"{df['amount'].quantile(0.75) + 1.5 * (df['amount'].quantile(0.75) - df['amount'].quantile(0.25)):.2f}]")
```

**SQL equivalent:**

```sql
WITH stats AS (
  SELECT
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS q1,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) AS q3
  FROM payments
)
SELECT p.*,
  CASE
    WHEN p.amount < s.q1 - 1.5 * (s.q3 - s.q1) THEN 'low_outlier'
    WHEN p.amount > s.q3 + 1.5 * (s.q3 - s.q1) THEN 'high_outlier'
    ELSE 'normal'
  END AS outlier_flag
FROM payments p
CROSS JOIN stats s;
```

### Z-Score Method

Best for normally distributed data. Sensitive to extreme outliers shifting the mean.

```python
import numpy as np

def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Flag outliers using Z-score. Returns boolean mask."""
    mean = series.mean()
    std = series.std()
    z_scores = (series - mean) / std
    return z_scores.abs() > threshold

# Usage
outlier_mask = detect_outliers_zscore(df["amount"], threshold=3.0)
```

**SQL equivalent:**

```sql
WITH stats AS (
  SELECT AVG(amount) AS mean_val, STDDEV(amount) AS std_val
  FROM payments
)
SELECT p.*,
  ABS((p.amount - s.mean_val) / NULLIF(s.std_val, 0)) AS z_score,
  CASE
    WHEN ABS((p.amount - s.mean_val) / NULLIF(s.std_val, 0)) > 3 THEN 'outlier'
    ELSE 'normal'
  END AS outlier_flag
FROM payments p
CROSS JOIN stats s;
```

### Modified Z-Score Method

Uses median and MAD (Median Absolute Deviation) instead of mean and standard deviation. Robust to existing outliers.

```python
def detect_outliers_modified_zscore(series: pd.Series, threshold: float = 3.5) -> pd.Series:
    """Flag outliers using modified Z-score (Iglewicz and Hoaglin method)."""
    median = series.median()
    mad = (series - median).abs().median()
    # 0.6745 is the 0.75th quantile of the standard normal distribution
    modified_z = 0.6745 * (series - median) / max(mad, 1e-10)
    return modified_z.abs() > threshold

# Usage
outlier_mask = detect_outliers_modified_zscore(df["amount"], threshold=3.5)
```

**SQL equivalent:**

```sql
WITH base AS (
  SELECT
    amount,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) OVER () AS median_val
  FROM payments
),
mad_calc AS (
  SELECT
    amount,
    median_val,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY ABS(amount - median_val)) OVER () AS mad
  FROM base
)
SELECT
  amount,
  0.6745 * (amount - median_val) / GREATEST(mad, 0.0001) AS modified_z_score,
  CASE
    WHEN ABS(0.6745 * (amount - median_val) / GREATEST(mad, 0.0001)) > 3.5 THEN 'outlier'
    ELSE 'normal'
  END AS outlier_flag
FROM mad_calc;
```

### Comparison Table

| Method | Robustness | Assumption | Threshold | Best For |
|---|---|---|---|---|
| IQR | High | None (non-parametric) | 1.5x (standard), 3x (extreme) | General purpose; skewed data |
| Z-Score | Low | Normal distribution | 2.5 (strict), 3.0 (standard) | Known normal distributions |
| Modified Z-Score | High | None | 3.5 (Iglewicz-Hoaglin) | Small samples; contaminated data |
| Percentile | Medium | None | 1st/99th or 0.5th/99.5th | Any distribution; simple threshold |

---

## Data Cleaning Operation Templates

### Sentinel Value Replacement

```python
def replace_sentinels(df: pd.DataFrame, rules: dict = None) -> pd.DataFrame:
    """Replace common sentinel values with proper NaN/None.

    Default rules handle the most common patterns. Override with custom rules dict.
    """
    default_rules = {
        "string": ["N/A", "n/a", "NA", "na", "NULL", "null", "None", "none",
                    "-", "--", ".", "...", "TBD", "tbd", "unknown", "UNKNOWN",
                    "not available", "not applicable", "#N/A", "#REF!", "#VALUE!"],
        "numeric": [0, -1, -999, 999999, 9999999],
        "date": ["1900-01-01", "1970-01-01", "0000-00-00", "9999-12-31"]
    }
    rules = rules or default_rules

    df = df.copy()

    for col in df.columns:
        # Replace empty strings and whitespace-only strings
        if df[col].dtype == "object":
            df[col] = df[col].str.strip()
            df[col] = df[col].replace("", np.nan)
            df[col] = df[col].replace(rules["string"], np.nan)

    return df
```

### Standardise Categorical Values

```python
def standardise_categories(
    series: pd.Series,
    mapping: dict = None,
    case: str = "lower"
) -> pd.Series:
    """Standardise categorical values with optional explicit mapping.

    If no mapping provided, normalises whitespace and applies casing.
    """
    result = series.copy()

    # Normalise whitespace and casing
    if result.dtype == "object":
        result = result.str.strip()
        result = result.str.replace(r'\s+', ' ', regex=True)

        if case == "lower":
            result = result.str.lower()
        elif case == "upper":
            result = result.str.upper()
        elif case == "title":
            result = result.str.title()

    # Apply explicit mapping if provided
    if mapping:
        result = result.replace(mapping)

    return result

# Example usage
status_mapping = {
    "active": "active",
    "act": "active",
    "a": "active",
    "inactive": "inactive",
    "inact": "inactive",
    "i": "inactive",
    "cancelled": "cancelled",
    "canceled": "cancelled",
    "cancel": "cancelled",
}
df["status"] = standardise_categories(df["status"], mapping=status_mapping)
```

### Deduplicate Records

```python
def deduplicate(
    df: pd.DataFrame,
    subset: list[str] = None,
    keep: str = "last",
    sort_by: str = None,
    sort_ascending: bool = False
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Remove duplicates, returning cleaned df and removed duplicates for audit.

    Args:
        subset: columns to check for duplicates (None = all columns)
        keep: 'first', 'last', or False (drop all duplicates)
        sort_by: sort before deduplication (e.g., sort by updated_at to keep latest)
    """
    if sort_by and sort_by in df.columns:
        df = df.sort_values(sort_by, ascending=sort_ascending)

    duplicates_mask = df.duplicated(subset=subset, keep=keep)
    removed = df[duplicates_mask].copy()
    cleaned = df[~duplicates_mask].copy()

    return cleaned, removed

# Usage
cleaned_df, removed_df = deduplicate(
    df,
    subset=["email", "order_id"],
    keep="last",
    sort_by="updated_at"
)
print(f"Removed {len(removed_df)} duplicates ({len(removed_df)/len(df):.1%})")
```

### Fix Date Format Inconsistencies

```python
def parse_mixed_dates(series: pd.Series) -> pd.Series:
    """Parse dates from mixed formats into consistent datetime."""
    # Try pandas mixed format parsing first
    result = pd.to_datetime(series, errors="coerce", format="mixed", dayfirst=True)

    # For values that failed, try common explicit formats
    failed_mask = result.isna() & series.notna()
    if failed_mask.any():
        formats_to_try = [
            "%d/%m/%Y", "%m/%d/%Y", "%Y-%m-%d",
            "%d-%m-%Y", "%d %b %Y", "%B %d, %Y",
            "%Y%m%d", "%d.%m.%Y"
        ]
        for fmt in formats_to_try:
            still_failed = result.isna() & series.notna()
            if not still_failed.any():
                break
            result[still_failed] = pd.to_datetime(
                series[still_failed], format=fmt, errors="coerce"
            )

    return result
```

### Normalise Phone Numbers

```python
import re

def normalise_phone_au(phone: str) -> str | None:
    """Normalise Australian phone numbers to +61 format."""
    if pd.isna(phone) or not phone:
        return None

    # Strip all non-digits
    digits = re.sub(r'\D', '', str(phone))

    # Handle +61 prefix (already international)
    if digits.startswith("61") and len(digits) == 11:
        return f"+61 {digits[2:5]} {digits[5:8]} {digits[8:]}"

    # Handle 04xx (mobile) or 0x (landline)
    if digits.startswith("0") and len(digits) == 10:
        return f"+61 {digits[1:4]} {digits[4:7]} {digits[7:]}"

    # Handle without leading zero (9 digits)
    if len(digits) == 9:
        return f"+61 {digits[0:3]} {digits[3:6]} {digits[6:]}"

    return None  # Cannot parse -- return None for manual review

# Apply to column
df["phone_normalised"] = df["phone"].apply(normalise_phone_au)
```

---

## Quality Scorecard Template

Copy and fill this template for each dataset audit.

```markdown
## Dataset Quality Scorecard -- [Dataset Name]

**Audit date:** [YYYY-MM-DD]
**Dataset:** [Name / description]
**Source:** [System or file origin]
**Volume:** [Row count] rows x [Column count] columns
**Date range:** [Earliest record] to [Latest record]
**Intended use:** [What the data will be used for]
**Audited by:** [Name or system]

---

### Overall Quality Score: [X]/100

| Dimension    | Score  | Status | Weight | Key Finding |
|-------------|--------|--------|--------|-------------|
| Completeness | [X]/100 | [Pass/Warn/Fail] | [%] | [One-line summary of worst completeness issue] |
| Validity     | [X]/100 | [Pass/Warn/Fail] | [%] | [One-line summary of worst validity issue] |
| Consistency  | [X]/100 | [Pass/Warn/Fail] | [%] | [One-line summary of worst consistency issue] |
| Uniqueness   | [X]/100 | [Pass/Warn/Fail] | [%] | [One-line summary of worst uniqueness issue] |
| Timeliness   | [X]/100 | [Pass/Warn/Fail] | [%] | [One-line summary of worst timeliness issue] |
| Accuracy     | [X]/100 | [Pass/Warn/Fail] | [%] | [One-line summary of worst accuracy issue] |

**Status thresholds:** Pass = 80+, Warn = 50-79, Fail = <50

### Fitness for Intended Use

**Verdict:** [Ready / Usable with caveats / Not ready]

**Rationale:** [2-3 sentences explaining why the data is or is not fit for the stated use, referencing the most impactful findings.]

### Critical Issues (fix before use)

1. [Issue description] -- [X records affected] -- [Dimension]
2. [Issue description] -- [X records affected] -- [Dimension]

### High Priority Issues (fix before analysis)

1. [Issue description] -- [X records affected] -- [Dimension]
2. [Issue description] -- [X records affected] -- [Dimension]

### Medium Priority Issues (fix for quality)

1. [Issue description] -- [X records affected] -- [Dimension]

### Low Priority Issues (improve when possible)

1. [Issue description] -- [X records affected] -- [Dimension]

---

### Field-Level Summary

| Field | Type | Non-Null % | Unique % | Top Issue | Severity |
|-------|------|-----------|----------|-----------|----------|
| [field_name] | [type] | [X%] | [X%] | [Issue or "Clean"] | [Critical/High/Medium/Low/None] |

---

### Recommended Next Steps

1. [ ] [First action to take with estimated effort]
2. [ ] [Second action to take with estimated effort]
3. [ ] [Third action to take with estimated effort]
```
