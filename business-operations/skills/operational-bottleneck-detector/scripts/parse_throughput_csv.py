#!/usr/bin/env python3
"""
parse_throughput_csv.py — reads a CSV with columns:
  stage, started_at, completed_at, wip
and prints summary stats (cycle time per stage, WIP, throughput) as JSON.

Usage:
  python3 parse_throughput_csv.py <path_to_csv>
"""

import csv
import json
import sys
from datetime import datetime


def parse_dt(value):
    """Parse ISO 8601 or common date/datetime strings."""
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(value.strip(), fmt)
        except ValueError:
            continue
    return None


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: parse_throughput_csv.py <path_to_csv>"}))
        sys.exit(1)

    path = sys.argv[1]

    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {path}"}))
        sys.exit(1)

    # Group rows by stage
    stages = {}
    for row in rows:
        stage = row.get("stage", "").strip()
        if not stage:
            continue
        started = parse_dt(row.get("started_at", ""))
        completed = parse_dt(row.get("completed_at", ""))
        try:
            wip = float(row.get("wip", 0))
        except (ValueError, TypeError):
            wip = 0.0

        if stage not in stages:
            stages[stage] = {"cycle_times_hours": [], "wip_values": []}

        if started and completed and completed > started:
            ct_hours = (completed - started).total_seconds() / 3600
            stages[stage]["cycle_times_hours"].append(ct_hours)

        if wip > 0:
            stages[stage]["wip_values"].append(wip)

    # Compute stats per stage
    results = {}
    for stage, data in stages.items():
        cts = data["cycle_times_hours"]
        wips = data["wip_values"]

        if cts:
            mean_ct = sum(cts) / len(cts)
            sorted_cts = sorted(cts)
            median_ct = sorted_cts[len(sorted_cts) // 2]
            p90_idx = int(len(sorted_cts) * 0.9)
            p90_ct = sorted_cts[min(p90_idx, len(sorted_cts) - 1)]
            throughput_per_day = len(cts) / max(
                (max(cts) / 24), 1
            )  # rough: completions / total span in days
        else:
            mean_ct = median_ct = p90_ct = throughput_per_day = None

        avg_wip = sum(wips) / len(wips) if wips else None

        # Little's Law check: WIP = Throughput * CycleTime
        littles_law_wip = None
        if throughput_per_day is not None and mean_ct is not None:
            littles_law_wip = round(throughput_per_day * (mean_ct / 24), 2)

        results[stage] = {
            "sample_count": len(cts),
            "mean_cycle_time_hours": round(mean_ct, 2) if mean_ct is not None else None,
            "median_cycle_time_hours": round(median_ct, 2) if median_ct is not None else None,
            "p90_cycle_time_hours": round(p90_ct, 2) if p90_ct is not None else None,
            "avg_wip": round(avg_wip, 2) if avg_wip is not None else None,
            "estimated_throughput_per_day": round(throughput_per_day, 2) if throughput_per_day is not None else None,
            "littles_law_expected_wip": littles_law_wip,
        }

    print(json.dumps({"stages": results, "total_rows": len(rows)}, indent=2))


if __name__ == "__main__":
    main()
