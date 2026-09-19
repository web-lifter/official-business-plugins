#!/usr/bin/env python3
"""Constant-period retention model; r always denotes retention, never churn."""
from __future__ import annotations
import argparse
import json
import math

def retention_model(retention: float, months: int = 12) -> dict:
    if not math.isfinite(retention) or not 0 <= retention <= 1:
        raise ValueError("retention must be finite and in [0,1]")
    if isinstance(months, bool) or not isinstance(months, int) or months < 0:
        raise ValueError("months must be a non-negative integer")
    return {"monthly_retention": retention, "monthly_churn": 1 - retention,
            "months": months, "cohort_remaining": retention ** months,
            "average_lifetime_months": 1 / (1 - retention) if retention < 1 else None,
            "assumption": "constant retention; initial paid period included; no expansion or discounting",
            "boundary_note": "unbounded model lifetime at r=1; use a finite planning horizon" if retention == 1 else None}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--retention", required=True, type=float)
    p.add_argument("--months", default=12, type=int)
    a = p.parse_args()
    try:
        print(json.dumps(retention_model(a.retention, a.months), indent=2, allow_nan=False))
    except ValueError as exc:
        p.error(str(exc))
