#!/usr/bin/env python3
"""Calculate TAM/SAM/SOM from market inputs.

Takes total market size, serviceable percentage, and obtainable
percentage to compute TAM, SAM, SOM with confidence ranges.

Usage:
    python tam-calculator.py --tam-value 10000000000 --sam-pct 15 --som-pct 5
    python tam-calculator.py --tam-value 500000000 --sam-pct 30 --som-pct 8 --confidence-band 20
"""

import argparse
import sys


def format_currency(value: float) -> str:
    """Format large numbers with appropriate suffix."""
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.1f}B"
    if value >= 1_000_000:
        return f"${value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"${value / 1_000:.1f}K"
    return f"${value:,.0f}"


def calculate(tam_value: float, sam_pct: float, som_pct: float,
              confidence_band: float) -> dict:
    """Calculate TAM, SAM, SOM with confidence ranges."""
    sam_value = tam_value * (sam_pct / 100)
    som_value = sam_value * (som_pct / 100)

    band = confidence_band / 100
    return {
        "tam": {"value": tam_value, "low": tam_value * (1 - band), "high": tam_value * (1 + band)},
        "sam": {"value": sam_value, "low": sam_value * (1 - band), "high": sam_value * (1 + band),
                "pct_of_tam": sam_pct},
        "som": {"value": som_value, "low": som_value * (1 - band), "high": som_value * (1 + band),
                "pct_of_sam": som_pct, "pct_of_tam": round(som_value / tam_value * 100, 2)},
    }


def print_report(result: dict, confidence_band: float) -> None:
    """Print formatted summary."""
    print("=" * 55)
    print("  MARKET SIZING SUMMARY")
    print("=" * 55)
    print()

    for label, key in [("TAM (Total Addressable Market)", "tam"),
                       ("SAM (Serviceable Addressable Market)", "sam"),
                       ("SOM (Serviceable Obtainable Market)", "som")]:
        data = result[key]
        print(f"  {label}")
        print(f"    Estimate:  {format_currency(data['value'])}")
        print(f"    Range:     {format_currency(data['low'])} - {format_currency(data['high'])} "
              f"(+/-{confidence_band:.0f}%)")
        if "pct_of_tam" in data and key == "sam":
            print(f"    Share:     {data['pct_of_tam']}% of TAM")
        if key == "som":
            print(f"    Share:     {data['pct_of_sam']}% of SAM, {data['pct_of_tam']}% of TAM")
        print()

    print("-" * 55)
    ratio = result["som"]["value"] / result["tam"]["value"] * 100 if result["tam"]["value"] else 0
    if ratio > 10:
        print("  NOTE: SOM > 10% of TAM is aggressive. Validate assumptions.")
    elif ratio < 0.5:
        print("  NOTE: SOM < 0.5% of TAM. Consider whether SAM is too broad.")
    else:
        print("  Market capture ratio looks reasonable.")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate TAM/SAM/SOM.")
    parser.add_argument("--tam-value", type=float, required=True, help="Total Addressable Market in dollars")
    parser.add_argument("--sam-pct", type=float, required=True, help="SAM as percentage of TAM")
    parser.add_argument("--som-pct", type=float, required=True, help="SOM as percentage of SAM")
    parser.add_argument("--confidence-band", type=float, default=15.0, help="Confidence band +/- percent (default: 15)")
    args = parser.parse_args()

    if args.tam_value <= 0:
        print("Error: TAM value must be positive.", file=sys.stderr)
        sys.exit(1)
    if not (0 < args.sam_pct <= 100) or not (0 < args.som_pct <= 100):
        print("Error: Percentages must be between 0 and 100.", file=sys.stderr)
        sys.exit(1)

    result = calculate(args.tam_value, args.sam_pct, args.som_pct, args.confidence_band)
    print_report(result, args.confidence_band)


if __name__ == "__main__":
    main()
