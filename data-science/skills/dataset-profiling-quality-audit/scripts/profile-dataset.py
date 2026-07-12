#!/usr/bin/env python3
"""Profile a CSV dataset and output a markdown quality summary.

Analyzes row count, column types, missing values, unique counts,
and basic statistics for numeric columns.

Usage:
    python profile-dataset.py data.csv
    python profile-dataset.py data.csv --output report.md
"""

import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path


def detect_type(values: list[str]) -> str:
    """Heuristically detect column type from sample values."""
    non_empty = [v for v in values if v.strip()]
    if not non_empty:
        return "empty"

    int_count = float_count = bool_count = 0
    for v in non_empty:
        if v.lower() in ("true", "false", "yes", "no", "0", "1"):
            bool_count += 1
        try:
            int(v)
            int_count += 1
            continue
        except ValueError:
            pass
        try:
            float(v)
            float_count += 1
        except ValueError:
            pass

    total = len(non_empty)
    if int_count == total:
        return "integer"
    if (int_count + float_count) == total:
        return "numeric"
    if bool_count > total * 0.8:
        return "boolean"
    return "text"


def numeric_stats(values: list[str]) -> dict:
    """Compute basic stats for numeric values."""
    nums = []
    for v in values:
        try:
            nums.append(float(v))
        except (ValueError, TypeError):
            pass
    if not nums:
        return {}
    nums.sort()
    n = len(nums)
    mean = sum(nums) / n
    median = nums[n // 2] if n % 2 else (nums[n // 2 - 1] + nums[n // 2]) / 2
    return {"min": nums[0], "max": nums[-1], "mean": round(mean, 2), "median": round(median, 2)}


def profile(csv_path: str) -> str:
    """Profile the dataset and return a markdown report."""
    path = Path(csv_path)
    if not path.exists():
        print(f"Error: File not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    columns: dict[str, list[str]] = defaultdict(list)
    row_count = 0

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames or []
        if not headers:
            print("Error: CSV has no headers.", file=sys.stderr)
            sys.exit(1)

        for row in reader:
            row_count += 1
            for h in headers:
                columns[h].append(row.get(h, ""))

    lines = [
        f"# Dataset Profile: {path.name}",
        "",
        f"- **Rows**: {row_count:,}",
        f"- **Columns**: {len(headers)}",
        f"- **File size**: {path.stat().st_size:,} bytes",
        "",
        "## Column Summary",
        "",
        "| Column | Type | Missing | Missing % | Unique | Sample Values |",
        "|--------|------|---------|-----------|--------|---------------|",
    ]

    for h in headers:
        vals = columns[h]
        missing = sum(1 for v in vals if v.strip() == "")
        missing_pct = round(missing / row_count * 100, 1) if row_count else 0
        unique = len(set(v for v in vals if v.strip()))
        col_type = detect_type(vals)
        non_empty = [v for v in vals if v.strip()]
        samples = ", ".join(non_empty[:3])
        if len(samples) > 40:
            samples = samples[:37] + "..."
        lines.append(f"| {h} | {col_type} | {missing} | {missing_pct}% | {unique} | {samples} |")

    # Numeric details
    numeric_cols = [h for h in headers if detect_type(columns[h]) in ("integer", "numeric")]
    if numeric_cols:
        lines.extend(["", "## Numeric Statistics", ""])
        lines.append("| Column | Min | Max | Mean | Median |")
        lines.append("|--------|-----|-----|------|--------|")
        for h in numeric_cols:
            stats = numeric_stats(columns[h])
            if stats:
                lines.append(f"| {h} | {stats['min']} | {stats['max']} | {stats['mean']} | {stats['median']} |")

    # Quality flags
    quality_issues = []
    for h in headers:
        vals = columns[h]
        missing_pct = sum(1 for v in vals if v.strip() == "") / row_count * 100 if row_count else 0
        if missing_pct > 50:
            quality_issues.append(f"- **{h}**: {missing_pct:.0f}% missing values -- consider dropping or imputing")
        if len(set(vals)) == 1:
            quality_issues.append(f"- **{h}**: constant value -- provides no analytical signal")

    if quality_issues:
        lines.extend(["", "## Quality Flags", ""])
        lines.extend(quality_issues)

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Profile a CSV dataset.")
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("--output", default=None, help="Output markdown file (default: stdout)")
    args = parser.parse_args()

    report = profile(args.csv_file)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Report written to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
