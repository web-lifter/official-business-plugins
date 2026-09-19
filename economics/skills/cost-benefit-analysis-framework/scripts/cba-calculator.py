#!/usr/bin/env python3
"""
cba-calculator.py — Cost-Benefit Analysis calculation engine.

Reads a JSON deck of options with year-by-year signed cashflows and a discount
rate; emits NPV, IRR, payback, discounted payback, profitability index, and
net-flow ratio per option. Gross benefit-cost ratio requires separate gross streams.

Input schema (see SKILL.md Phase 2):

    {
      "discount_rate": 0.10,
      "currency": "AUD",
      "horizon_years": 5,
      "options": [
        {"name": "Build", "cashflows": [-250000, -40000, 80000, 120000, 160000, 180000]},
        ...
      ]
    }

Output schema:

    {
      "discount_rate": 0.10,
      "currency": "AUD",
      "results": [
        {
          "name": "Build",
          "npv": ...,
          "irr": ... | null,
          "payback_years": ... | null,
          "discounted_payback_years": ... | null,
          "profitability_index": ... | null,
          "benefit_cost_ratio": ... | null,
          "total_nominal_cost": ...,
          "total_nominal_benefit": ...,
          "notes": [...]
        },
        ...
      ]
    }
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


def npv(rate: float, cashflows: list[float]) -> float:
    return sum(cf / (1.0 + rate) ** t for t, cf in enumerate(cashflows))


def irr(cashflows: list[float], guess: float = 0.1) -> float | None:
    """Find one IRR in [-0.99, 10]; None is inconclusive outside this bracket."""
    has_positive = any(cf > 0 for cf in cashflows)
    has_negative = any(cf < 0 for cf in cashflows)
    if not (has_positive and has_negative):
        return None

    lo, hi = -0.99, 10.0
    f_lo = npv(lo, cashflows)
    f_hi = npv(hi, cashflows)
    if f_lo == 0:
        return lo
    if f_hi == 0:
        return hi
    if f_lo * f_hi > 0:
        return None

    for _ in range(200):
        mid = (lo + hi) / 2.0
        f_mid = npv(mid, cashflows)
        if abs(f_mid) < 1e-6:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
            f_hi = f_mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo + hi) / 2.0


def payback(cashflows: list[float]) -> float | None:
    if cashflows and cashflows[0] >= 0:
        return 0.0
    cum = 0.0
    for t, cf in enumerate(cashflows):
        prev = cum
        cum += cf
        if prev < 0 and cum >= 0:
            return t - 1 + (-prev / cf) if cf != 0 else float(t)
    return None


def discounted_payback(rate: float, cashflows: list[float]) -> float | None:
    if cashflows and cashflows[0] >= 0:
        return 0.0
    cum = 0.0
    for t, cf in enumerate(cashflows):
        prev = cum
        cum += cf / (1.0 + rate) ** t
        if prev < 0 and cum >= 0:
            step = cum - prev
            return t - 1 + (-prev / step) if step != 0 else float(t)
    return None


def pv_split(rate: float, cashflows: list[float]) -> tuple[float, float]:
    pv_cost = 0.0
    pv_benefit = 0.0
    for t, cf in enumerate(cashflows):
        pv = cf / (1.0 + rate) ** t
        if cf < 0:
            pv_cost += -pv
        else:
            pv_benefit += pv
    return pv_cost, pv_benefit


def evaluate_option(name: str, cashflows: list[float], rate: float) -> dict:
    if not math.isfinite(rate) or rate <= -1:
        raise ValueError("discount rate must be finite and greater than -1")
    if not cashflows or not all(math.isfinite(cf) for cf in cashflows):
        raise ValueError("cashflows must contain finite numbers")
    notes: list[str] = []

    v_npv = npv(rate, cashflows)
    v_irr = irr(cashflows)
    if v_irr is None:
        notes.append("IRR not resolved by the finite bracket; it may be absent or non-unique. Do not infer no sign changes.")

    v_payback = payback(cashflows)
    if v_payback is None:
        notes.append("Payback never reached within horizon (cumulative cashflow stays negative).")

    v_dpayback = discounted_payback(rate, cashflows)
    if v_dpayback is None and v_payback is not None:
        notes.append("Discounted payback never reached within horizon.")

    pv_cost, pv_benefit = pv_split(rate, cashflows)
    net_flow_ratio = (pv_benefit / pv_cost) if pv_cost > 0 else None
    initial_outlay = -cashflows[0] if cashflows[0] < 0 else 0
    pi = (v_npv + initial_outlay) / initial_outlay if initial_outlay else None
    bcr = None
    notes.append("Gross benefit-cost ratio requires separate benefit and cost streams; signed net cashflows alone are insufficient. net_flow_ratio is a different measure.")

    total_cost = sum(-cf for cf in cashflows if cf < 0)
    total_benefit = sum(cf for cf in cashflows if cf > 0)

    return {
        "name": name,
        "npv": round(v_npv, 2),
        "irr": round(v_irr, 6) if v_irr is not None else None,
        "payback_years": round(v_payback, 3) if v_payback is not None else None,
        "discounted_payback_years": round(v_dpayback, 3) if v_dpayback is not None else None,
        "profitability_index": round(pi, 4) if pi is not None else None,
        "benefit_cost_ratio": bcr,
        "net_flow_ratio": round(net_flow_ratio, 4) if net_flow_ratio is not None else None,
        "total_nominal_cost": round(total_cost, 2),
        "total_nominal_benefit": round(total_benefit, 2),
        "notes": notes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Cost-Benefit Analysis calculator.")
    parser.add_argument("--input", required=True, help="Path to input JSON deck.")
    parser.add_argument("--output", required=True, help="Path to write output JSON results.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        print(f"error=target-not-found path={input_path}", file=sys.stderr)
        return 2

    try:
        deck = json.loads(input_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"error=invalid-json detail={exc}", file=sys.stderr)
        return 2

    if not isinstance(deck, dict):
        print("error=invalid-input detail=deck must be an object", file=sys.stderr)
        return 2
    rate = deck.get("discount_rate")
    options = deck.get("options")
    if rate is None or not isinstance(options, list) or not options:
        print("error=empty-argument detail=discount_rate or options missing", file=sys.stderr)
        return 2

    try:
        results = [
            evaluate_option(opt["name"], [float(cf) for cf in opt["cashflows"]], float(rate))
            for opt in options
        ]
    except (KeyError, TypeError, ValueError, OverflowError, ZeroDivisionError) as exc:
        print(f"error=invalid-option detail={exc}", file=sys.stderr)
        return 2

    payload = {
        "discount_rate": rate,
        "currency": deck.get("currency", "AUD"),
        "horizon_years": deck.get("horizon_years"),
        "results": results,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, allow_nan=False), encoding="utf-8")
    print(json.dumps(payload, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
