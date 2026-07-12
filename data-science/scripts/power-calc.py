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
import sys


def z_score(p: float) -> float:
    """Approximate inverse normal CDF (Beasley-Springer-Moro). Pure-stdlib."""
    # Acceptable approximation in the (0.001, 0.999) range we care about.
    a = [
        -3.969683028665376e+01, 2.209460984245205e+02,
        -2.759285104469687e+02, 1.383577518672690e+02,
        -3.066479806614716e+01, 2.506628277459239e+00,
    ]
    b = [
        -5.447609879822406e+01, 1.615858368580409e+02,
        -1.556989798598866e+02, 6.680131188771972e+01,
        -1.328068155288572e+01,
    ]
    c = [
        -7.784894002430293e-03, -3.223964580411365e-01,
        -2.400758277161838e+00, -2.549732539343734e+00,
        4.374664141464968e+00, 2.938163982698783e+00,
    ]
    d = [
        7.784695709041462e-03, 3.224671290700398e-01,
        2.445134137142996e+00, 3.754408661907416e+00,
    ]
    plow = 0.02425
    phigh = 1 - plow
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
               ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    if p <= phigh:
        q = p - 0.5
        r = q * q
        return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / \
               (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)
    q = math.sqrt(-2 * math.log(1 - p))
    return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
           ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)


def sample_size_proportions(baseline: float, mde: float, alpha: float, power: float, two_sided: bool) -> int:
    """Two-proportion z-test sample size per group."""
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

    n_per_group = sample_size_proportions(a.baseline, a.mde, a.alpha, a.power, a.two_sided)
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
