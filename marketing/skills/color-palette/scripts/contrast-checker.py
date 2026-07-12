#!/usr/bin/env python3
"""WCAG 2.2 contrast ratio checker.

Computes the WCAG 2.2 contrast ratio between two colours and reports
pass/fail status for normal text (AA + AAA) and large text (AA + AAA).

Implements the formal WCAG formula:
    contrast = (L1 + 0.05) / (L2 + 0.05)
where L1, L2 are relative luminance values per WCAG (sRGB-aware).

Usage:
    python contrast-checker.py "#0A2540" "#FFFFFF"
    python contrast-checker.py 0A2540 FFFFFF        # hash optional
    python contrast-checker.py --pairs pairs.txt    # batch mode

Exit codes:
    0  All pairs pass AA for normal text
    1  At least one pair fails AA for normal text
    2  Invalid input
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# WCAG 2.2 thresholds
AA_NORMAL = 4.5
AAA_NORMAL = 7.0
AA_LARGE = 3.0
AAA_LARGE = 4.5


def parse_hex(value: str) -> tuple[int, int, int]:
    """Parse a HEX colour string into an (R, G, B) tuple of 0–255 ints.

    Accepts: '#RRGGBB', 'RRGGBB', '#RGB', 'RGB' (case-insensitive).
    Raises ValueError for malformed input.
    """
    raw = value.strip().lstrip("#")
    if len(raw) == 3:
        raw = "".join(c * 2 for c in raw)
    if len(raw) != 6:
        raise ValueError(f"Invalid hex colour: {value!r}")
    try:
        return (
            int(raw[0:2], 16),
            int(raw[2:4], 16),
            int(raw[4:6], 16),
        )
    except ValueError as exc:
        raise ValueError(f"Invalid hex digits in: {value!r}") from exc


def linearise(channel_8bit: int) -> float:
    """Linearise an sRGB 0–255 channel value per WCAG."""
    c = channel_8bit / 255.0
    if c <= 0.03928:
        return c / 12.92
    return ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    """Compute WCAG relative luminance (0.0–1.0) from an (R, G, B) tuple."""
    r, g, b = (linearise(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(hex_a: str, hex_b: str) -> float:
    """Return the WCAG contrast ratio between two HEX colours.

    Result is always >= 1.0 (lighter colour goes on top in the formula).
    """
    la = relative_luminance(parse_hex(hex_a))
    lb = relative_luminance(parse_hex(hex_b))
    lighter, darker = max(la, lb), min(la, lb)
    return (lighter + 0.05) / (darker + 0.05)


def grade(ratio: float) -> dict[str, bool]:
    """Return a dict of WCAG pass/fail flags for a given ratio."""
    return {
        "aa_normal": ratio >= AA_NORMAL,
        "aaa_normal": ratio >= AAA_NORMAL,
        "aa_large": ratio >= AA_LARGE,
        "aaa_large": ratio >= AAA_LARGE,
    }


def format_check(passed: bool) -> str:
    return "PASS" if passed else "FAIL"


def report_pair(hex_a: str, hex_b: str) -> bool:
    """Print a report for a single colour pair. Return True if AA normal passes."""
    try:
        ratio = contrast_ratio(hex_a, hex_b)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return False

    g = grade(ratio)
    print(f"\n{hex_a}  vs  {hex_b}")
    print(f"  Contrast ratio: {ratio:.2f}:1")
    print(f"  AA  normal text  (>= 4.5): {format_check(g['aa_normal'])}")
    print(f"  AAA normal text  (>= 7.0): {format_check(g['aaa_normal'])}")
    print(f"  AA  large text   (>= 3.0): {format_check(g['aa_large'])}")
    print(f"  AAA large text   (>= 4.5): {format_check(g['aaa_large'])}")
    return g["aa_normal"]


def read_pairs_file(path: Path) -> list[tuple[str, str]]:
    """Read a pairs file. Each line: '#RRGGBB #RRGGBB' (whitespace-separated)."""
    pairs: list[tuple[str, str]] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") and len(line.split()) < 2:
            # Skip empty lines and comment-only lines (a single hex would also start with '#')
            if not line or line.startswith("//"):
                continue
        parts = line.split()
        if len(parts) >= 2:
            pairs.append((parts[0], parts[1]))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check WCAG 2.2 contrast ratio between two HEX colours.",
        epilog="Exit code 0 = all pairs pass AA normal text. Exit code 1 = one or more pairs fail.",
    )
    parser.add_argument("color_a", nargs="?", help="First colour (e.g. #0A2540)")
    parser.add_argument("color_b", nargs="?", help="Second colour (e.g. #FFFFFF)")
    parser.add_argument(
        "--pairs",
        type=Path,
        help="Path to a file with one HEX pair per line (whitespace-separated).",
    )
    args = parser.parse_args()

    if args.pairs:
        if not args.pairs.exists():
            print(f"ERROR: pairs file not found: {args.pairs}", file=sys.stderr)
            return 2
        pairs = read_pairs_file(args.pairs)
        if not pairs:
            print("ERROR: no valid pairs found in file", file=sys.stderr)
            return 2
        all_pass = True
        for a, b in pairs:
            if not report_pair(a, b):
                all_pass = False
        return 0 if all_pass else 1

    if not args.color_a or not args.color_b:
        parser.print_help(sys.stderr)
        return 2

    return 0 if report_pair(args.color_a, args.color_b) else 1


if __name__ == "__main__":
    sys.exit(main())
