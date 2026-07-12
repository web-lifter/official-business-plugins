#!/usr/bin/env python3
"""cvp-calc.py — Cost-Volume-Profit + break-even calculator.

Pure stdlib. Reads inputs from CLI args.

Usage:
  python cvp-calc.py --fixed 480000 --variable_per_unit 28 --price 55 \
                     --target_profit 100000

Outputs:
  - Contribution margin per unit + ratio
  - Break-even (units + AUD)
  - Required units to hit target profit
  - Sensitivity to ±10% price / ±10% variable / ±10% fixed
"""
from __future__ import annotations

import argparse
import sys


def compute(fixed: float, variable_per_unit: float, price: float, target_profit: float = 0) -> dict:
    cm_per_unit = price - variable_per_unit
    cm_ratio = cm_per_unit / price if price else 0
    if cm_per_unit <= 0:
        return {"error": "Contribution margin <= 0; cannot break even at this price/cost mix."}
    break_even_units = fixed / cm_per_unit
    break_even_aud = break_even_units * price
    target_units = (fixed + target_profit) / cm_per_unit
    return {
        "cm_per_unit": round(cm_per_unit, 2),
        "cm_ratio": round(cm_ratio, 4),
        "break_even_units": round(break_even_units, 1),
        "break_even_aud": round(break_even_aud, 2),
        "target_units": round(target_units, 1),
    }


def sensitivity(fixed: float, var: float, price: float, target_profit: float) -> dict:
    base = compute(fixed, var, price, target_profit)
    if "error" in base:
        return {"error": base["error"]}
    return {
        "base": base,
        "price_-10": compute(fixed, var, price * 0.9, target_profit),
        "price_+10": compute(fixed, var, price * 1.1, target_profit),
        "variable_-10": compute(fixed, var * 0.9, price, target_profit),
        "variable_+10": compute(fixed, var * 1.1, price, target_profit),
        "fixed_-10": compute(fixed * 0.9, var, price, target_profit),
        "fixed_+10": compute(fixed * 1.1, var, price, target_profit),
    }


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--fixed", type=float, required=True)
    p.add_argument("--variable_per_unit", type=float, required=True)
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--target_profit", type=float, default=0)
    a = p.parse_args(argv)
    base = compute(a.fixed, a.variable_per_unit, a.price, a.target_profit)
    if "error" in base:
        print(f"ERROR: {base['error']}", file=sys.stderr)
        return 1
    print(f"Contribution margin/unit: ${base['cm_per_unit']:>10,.2f}")
    print(f"Contribution margin ratio:  {base['cm_ratio'] * 100:>6.1f}%")
    print(f"Break-even units:          {base['break_even_units']:>10,.0f}")
    print(f"Break-even AUD:            ${base['break_even_aud']:>10,.0f}")
    print(f"Units to hit target:       {base['target_units']:>10,.0f}")
    sens = sensitivity(a.fixed, a.variable_per_unit, a.price, a.target_profit)
    print("\nSensitivity (break-even units):")
    for label in ("price_-10", "price_+10", "variable_-10", "variable_+10", "fixed_-10", "fixed_+10"):
        v = sens[label]
        if isinstance(v, dict) and "break_even_units" in v:
            print(f"  {label}: {v['break_even_units']:>10,.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
