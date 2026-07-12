"""Smoke tests for plugin-level Python scripts in the business marketplace.

Covers:
- power-calc  (data-science)
- cvp-calc    (economics)

Each test invokes the script with a small valid input and asserts exit code and
an expected substring. Pure stdlib — no third-party deps.

Run from the repo root:

    python -m pytest tests/scripts/test_smoke.py -v
    python tests/scripts/test_smoke.py
"""
from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def run(script: str, *args: str) -> subprocess.CompletedProcess:
    cmd = [sys.executable, str(REPO_ROOT / script), *args]
    return subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=30)


class TestPowerCalc(unittest.TestCase):
    """data-science/scripts/power-calc.py"""

    SCRIPT = "data-science/scripts/power-calc.py"

    def test_standard_ab_test(self):
        r = run(self.SCRIPT, "--baseline", "0.05", "--mde", "0.005",
                "--alpha", "0.05", "--power", "0.8", "--two_sided")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Sample per group:", r.stdout)
        self.assertIn("Total sample:", r.stdout)

    def test_smaller_mde_needs_more_sample(self):
        r1 = run(self.SCRIPT, "--baseline", "0.10", "--mde", "0.01", "--two_sided")
        r2 = run(self.SCRIPT, "--baseline", "0.10", "--mde", "0.005", "--two_sided")

        def n_from(out):
            for line in out.splitlines():
                if "Total sample:" in line:
                    return int(line.split(":")[1].strip().replace(",", ""))
            return None
        self.assertGreater(n_from(r2.stdout), n_from(r1.stdout),
                           "smaller MDE should require more sample")


class TestCvpCalc(unittest.TestCase):
    """economics/scripts/cvp-calc.py"""

    SCRIPT = "economics/scripts/cvp-calc.py"

    def test_basic_break_even(self):
        r = run(self.SCRIPT, "--fixed", "100000", "--variable_per_unit", "20",
                "--price", "50", "--target_profit", "0")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("Break-even units:", r.stdout)
        self.assertIn("Sensitivity", r.stdout)

    def test_negative_margin_errors(self):
        r = run(self.SCRIPT, "--fixed", "100000", "--variable_per_unit", "60",
                "--price", "50", "--target_profit", "0")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("ERROR", r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
