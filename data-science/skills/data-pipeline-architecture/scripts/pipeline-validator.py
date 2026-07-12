#!/usr/bin/env python3
"""Validate a data pipeline configuration for common issues.

Checks a YAML or JSON pipeline spec for missing error handling,
idempotency, monitoring, and other best-practice concerns.

Usage:
    python pipeline-validator.py pipeline.yaml
    python pipeline-validator.py pipeline.json
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def load_spec(path: str) -> dict:
    """Load pipeline spec from YAML or JSON."""
    filepath = Path(path)
    if not filepath.exists():
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)

    content = filepath.read_text(encoding="utf-8")
    if filepath.suffix in (".yaml", ".yml"):
        if not HAS_YAML:
            print("Error: PyYAML required for YAML files. Install with: pip install pyyaml", file=sys.stderr)
            sys.exit(1)
        return yaml.safe_load(content) or {}
    else:
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
            sys.exit(1)


def check_key_present(spec: dict, key: str, path: str = "") -> bool:
    """Recursively check if a key exists anywhere in the spec."""
    if key in spec:
        return True
    for v in spec.values():
        if isinstance(v, dict) and check_key_present(v, key, path):
            return True
        if isinstance(v, list):
            for item in v:
                if isinstance(item, dict) and check_key_present(item, key, path):
                    return True
    return False


def validate(spec: dict) -> list[dict]:
    """Run validation checks and return findings."""
    issues = []

    def add(severity: str, message: str, suggestion: str):
        issues.append({"severity": severity, "message": message, "suggestion": suggestion})

    # Check for error handling
    error_keywords = ["error_handling", "on_failure", "retry", "dead_letter", "catch", "fallback"]
    if not any(check_key_present(spec, kw) for kw in error_keywords):
        add("ERROR", "No error handling detected",
            "Add retry policies, dead-letter queues, or on_failure handlers to each step.")

    # Check for idempotency
    idem_keywords = ["idempotent", "idempotency_key", "dedup", "deduplication", "upsert"]
    if not any(check_key_present(spec, kw) for kw in idem_keywords):
        add("WARNING", "No idempotency configuration found",
            "Add idempotency keys or deduplication logic to prevent duplicate processing.")

    # Check for monitoring
    mon_keywords = ["monitoring", "alerting", "metrics", "logging", "observability", "health_check"]
    if not any(check_key_present(spec, kw) for kw in mon_keywords):
        add("WARNING", "No monitoring or alerting configured",
            "Add metrics collection, health checks, and alerting for pipeline failures.")

    # Check for schedule / trigger
    trigger_keywords = ["schedule", "trigger", "cron", "interval", "event_source"]
    if not any(check_key_present(spec, kw) for kw in trigger_keywords):
        add("INFO", "No schedule or trigger defined",
            "Define how the pipeline is triggered (cron, event, or manual).")

    # Check steps exist
    steps = spec.get("steps") or spec.get("stages") or spec.get("tasks")
    if not steps:
        add("ERROR", "No pipeline steps/stages/tasks found",
            "Define pipeline steps under a 'steps', 'stages', or 'tasks' key.")
    elif isinstance(steps, list):
        for i, step in enumerate(steps):
            if isinstance(step, dict):
                if not step.get("name") and not step.get("id"):
                    add("WARNING", f"Step {i} has no name or id", "Name each step for traceability.")
                if not any(k in step for k in ["timeout", "time_limit", "deadline"]):
                    add("INFO", f"Step '{step.get('name', i)}' has no timeout",
                        "Set timeouts to prevent hung steps from blocking the pipeline.")

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a data pipeline configuration.")
    parser.add_argument("spec_file", help="Path to pipeline spec (YAML or JSON)")
    args = parser.parse_args()

    spec = load_spec(args.spec_file)
    issues = validate(spec)

    if not issues:
        print("All checks passed. No issues found.")
        return

    severity_order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
    issues.sort(key=lambda x: severity_order.get(x["severity"], 9))

    print(f"Pipeline Validation: {len(issues)} issue(s) found\n")
    for issue in issues:
        print(f"  [{issue['severity']}] {issue['message']}")
        print(f"    -> {issue['suggestion']}\n")

    error_count = sum(1 for i in issues if i["severity"] == "ERROR")
    if error_count:
        sys.exit(1)


if __name__ == "__main__":
    main()
