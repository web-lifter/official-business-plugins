#!/usr/bin/env python3
"""Calculate core unit economics metrics with health assessment.

Computes CAC, LTV, LTV:CAC ratio, payback period, and contribution margin
from revenue and cost inputs.

Usage:
    python unit-economics.py --arpu 100 --cogs 30 --cac 250 --churn 5
    python unit-economics.py --arpu 50 --cogs 15 --cac 120 --churn 3 --gross-margin-override 70
"""

import argparse
import sys


def calculate_unit_economics(arpu: float, cogs: float, cac: float,
                              monthly_churn: float, gross_margin_override: float | None) -> dict:
    """Calculate unit economics from inputs."""
    if monthly_churn <= 0:
        print("Error: Churn rate must be greater than 0.", file=sys.stderr)
        sys.exit(1)

    gross_margin_pct = gross_margin_override if gross_margin_override is not None else ((arpu - cogs) / arpu * 100)
    gross_profit = arpu * (gross_margin_pct / 100)
    avg_lifetime_months = 1 / (monthly_churn / 100)
    ltv = gross_profit * avg_lifetime_months
    ltv_cac_ratio = ltv / cac if cac > 0 else float("inf")
    payback_months = cac / gross_profit if gross_profit > 0 else float("inf")
    contribution_margin = gross_profit - (cac / avg_lifetime_months)

    return {
        "arpu": arpu,
        "cogs": cogs,
        "gross_margin_pct": round(gross_margin_pct, 1),
        "gross_profit": round(gross_profit, 2),
        "cac": cac,
        "monthly_churn_pct": monthly_churn,
        "avg_lifetime_months": round(avg_lifetime_months, 1),
        "ltv": round(ltv, 2),
        "ltv_cac_ratio": round(ltv_cac_ratio, 2),
        "payback_months": round(payback_months, 1),
        "contribution_margin": round(contribution_margin, 2),
    }


def assess_health(metrics: dict) -> list[str]:
    """Return health assessment notes."""
    notes = []
    ratio = metrics["ltv_cac_ratio"]
    if ratio >= 3:
        notes.append(f"LTV:CAC = {ratio}x -- HEALTHY (target is 3x+)")
    elif ratio >= 1:
        notes.append(f"LTV:CAC = {ratio}x -- MARGINAL (below 3x target, optimize CAC or retention)")
    else:
        notes.append(f"LTV:CAC = {ratio}x -- UNSUSTAINABLE (spending more to acquire than customer is worth)")

    payback = metrics["payback_months"]
    if payback <= 12:
        notes.append(f"Payback = {payback} months -- GOOD (under 12 months)")
    elif payback <= 18:
        notes.append(f"Payback = {payback} months -- ACCEPTABLE (12-18 month range)")
    else:
        notes.append(f"Payback = {payback} months -- SLOW (over 18 months, cash flow risk)")

    if metrics["monthly_churn_pct"] > 5:
        notes.append(f"Monthly churn = {metrics['monthly_churn_pct']}% -- HIGH (target <5% monthly)")

    if metrics["contribution_margin"] < 0:
        notes.append(f"Contribution margin = ${metrics['contribution_margin']} -- NEGATIVE (unprofitable per unit)")

    return notes


def print_report(metrics: dict) -> None:
    """Print formatted report."""
    print("=" * 55)
    print("  UNIT ECONOMICS SUMMARY")
    print("=" * 55)
    print()
    print(f"  Revenue (ARPU/mo):       ${metrics['arpu']:>10,.2f}")
    print(f"  COGS per unit:           ${metrics['cogs']:>10,.2f}")
    print(f"  Gross margin:            {metrics['gross_margin_pct']:>10.1f}%")
    print(f"  Gross profit/mo:         ${metrics['gross_profit']:>10,.2f}")
    print()
    print(f"  CAC:                     ${metrics['cac']:>10,.2f}")
    print(f"  Monthly churn:           {metrics['monthly_churn_pct']:>10.1f}%")
    print(f"  Avg lifetime:            {metrics['avg_lifetime_months']:>10.1f} months")
    print()
    print(f"  LTV:                     ${metrics['ltv']:>10,.2f}")
    print(f"  LTV:CAC ratio:           {metrics['ltv_cac_ratio']:>10.1f}x")
    print(f"  Payback period:          {metrics['payback_months']:>10.1f} months")
    print(f"  Contribution margin/mo:  ${metrics['contribution_margin']:>10,.2f}")
    print()
    print("-" * 55)
    print("  HEALTH ASSESSMENT")
    print("-" * 55)
    for note in assess_health(metrics):
        print(f"  {note}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate unit economics metrics.")
    parser.add_argument("--arpu", type=float, required=True, help="Average revenue per user per month")
    parser.add_argument("--cogs", type=float, required=True, help="Cost of goods sold per user per month")
    parser.add_argument("--cac", type=float, required=True, help="Customer acquisition cost")
    parser.add_argument("--churn", type=float, required=True, help="Monthly churn rate (percent)")
    parser.add_argument("--gross-margin-override", type=float, default=None,
                        help="Override gross margin percent instead of computing from ARPU/COGS")
    args = parser.parse_args()

    metrics = calculate_unit_economics(args.arpu, args.cogs, args.cac, args.churn, args.gross_margin_override)
    print_report(metrics)


if __name__ == "__main__":
    main()
