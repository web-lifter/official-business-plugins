#!/usr/bin/env python3
"""Validate anomaly detection thresholds against historical data.

Reads a CSV of historical metric values and proposed thresholds,
then reports trigger counts and estimated false positive rates.

Usage:
    python validate-thresholds.py data.csv --upper 95.0 --lower 10.0
    python validate-thresholds.py data.csv --upper 95.0 --column cpu_usage
"""

import argparse
import csv
import sys
from pathlib import Path


def load_values(csv_path: str, column: str | None) -> list[float]:
    """Load numeric values from a CSV file."""
    values = []
    path = Path(csv_path)
    if not path.exists():
        print(f"Error: File not found: {csv_path}", file=sys.stderr)
        sys.exit(1)

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if column and column not in (reader.fieldnames or []):
            print(f"Error: Column '{column}' not found. Available: {reader.fieldnames}", file=sys.stderr)
            sys.exit(1)

        target_col = column or (reader.fieldnames[0] if reader.fieldnames else None)
        if not target_col:
            print("Error: CSV has no columns.", file=sys.stderr)
            sys.exit(1)

        for row_num, row in enumerate(reader, start=2):
            raw = row.get(target_col, "").strip()
            if raw == "":
                continue
            try:
                values.append(float(raw))
            except ValueError:
                print(f"Warning: Skipping non-numeric value on row {row_num}: '{raw}'", file=sys.stderr)

    if not values:
        print("Error: No valid numeric values found.", file=sys.stderr)
        sys.exit(1)

    return values


def validate(values: list[float], upper: float | None, lower: float | None) -> None:
    """Validate thresholds and print report."""
    total = len(values)
    mean = sum(values) / total
    sorted_vals = sorted(values)
    median = sorted_vals[total // 2]

    print(f"Dataset: {total} data points")
    print(f"Range:   {min(values):.2f} - {max(values):.2f}")
    print(f"Mean:    {mean:.2f}  |  Median: {median:.2f}")
    print("-" * 50)

    if upper is not None:
        breaches = sum(1 for v in values if v > upper)
        rate = breaches / total * 100
        print(f"Upper threshold ({upper}): {breaches} triggers ({rate:.1f}% of data)")
        if rate > 5:
            print("  WARNING: >5% trigger rate suggests threshold is too sensitive.")
        elif rate == 0:
            print("  NOTE: Zero triggers -- threshold may be too lenient.")

    if lower is not None:
        breaches = sum(1 for v in values if v < lower)
        rate = breaches / total * 100
        print(f"Lower threshold ({lower}): {breaches} triggers ({rate:.1f}% of data)")
        if rate > 5:
            print("  WARNING: >5% trigger rate suggests threshold is too sensitive.")
        elif rate == 0:
            print("  NOTE: Zero triggers -- threshold may be too lenient.")

    if upper is None and lower is None:
        print("No thresholds specified. Use --upper and/or --lower.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate anomaly detection thresholds.")
    parser.add_argument("csv_file", help="Path to CSV with historical metric values")
    parser.add_argument("--upper", type=float, default=None, help="Upper threshold value")
    parser.add_argument("--lower", type=float, default=None, help="Lower threshold value")
    parser.add_argument("--column", default=None, help="Column name to analyze (default: first column)")
    args = parser.parse_args()

    values = load_values(args.csv_file, args.column)
    validate(values, args.upper, args.lower)


if __name__ == "__main__":
    main()
