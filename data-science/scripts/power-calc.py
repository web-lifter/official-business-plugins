#!/usr/bin/env python3
"""power-calc.py — Sample-size calculation for proportion-based A/B tests.

Pure stdlib (uses math). Implements the standard formula for two-proportion z-test
(Wald approximation), which is fine for most product A/B tests where p, MDE are typical.

Usage:
  python power-calc.py --baseline 0.05 --mde 0.005 --alpha 0.05 --power 0.8 --two_sided

Outputs sample size per group + total.

For more exotic test types (ratio, continuous, sequential), use a proper stats library.
"""
from __future__ import annotations

import argparse
import math
from statistics import NormalDist
import sys


def z_score(p: float) -> float:
    """Inverse standard-normal CDF for a finite probability in (0, 1)."""
    if not math.isfinite(p) or not 0 < p < 1:
        raise ValueError("probability must be finite and strictly between 0 and 1")
    return NormalDist().inv_cdf(p)


def sample_size_proportions(baseline: float, mde: float, alpha: float, power: float, two_sided: bool) -> int:
    """Two-proportion z-test sample size per group."""
    if not all(math.isfinite(v) for v in (baseline, mde, alpha, power)):
        raise ValueError("inputs must be finite")
    if not 0 < baseline < 1 or not 0 < mde <= 1 - baseline:
        raise ValueError("baseline must be in (0,1); MDE must be positive and baseline + MDE <= 1")
    if not 0 < alpha < 0.5 or not 0.5 < power < 1:
        raise ValueError("alpha must be in (0,0.5) and power in (0.5,1)")
    p1 = baseline
    p2 = baseline + mde
    pbar = (p1 + p2) / 2
    z_alpha = z_score(1 - alpha / 2) if two_sided else z_score(1 - alpha)
    z_beta = z_score(power)
    numerator = (z_alpha * math.sqrt(2 * pbar * (1 - pbar)) +
                 z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    n = numerator / (mde ** 2)
    return math.ceil(n)


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--baseline", type=float, required=True, help="Baseline conversion rate (0.0–1.0)")
    p.add_argument("--mde", type=float, required=True, help="Minimum detectable effect, absolute (e.g. 0.005)")
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--power", type=float, default=0.8)
    p.add_argument("--two_sided", action="store_true")
    a = p.parse_args(argv)

    try:
        n_per_group = sample_size_proportions(a.baseline, a.mde, a.alpha, a.power, a.two_sided)
    except ValueError as exc:
        p.error(str(exc))
    print(f"Baseline:           {a.baseline:.4f}")
    print(f"MDE (absolute):     {a.mde:.4f}")
    print(f"Treatment expected: {a.baseline + a.mde:.4f}")
    print(f"Alpha:              {a.alpha}")
    print(f"Power:              {a.power}")
    print(f"Two-sided:          {a.two_sided}")
    print(f"Sample per group:   {n_per_group:,}")
    print(f"Total sample:       {2 * n_per_group:,}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
