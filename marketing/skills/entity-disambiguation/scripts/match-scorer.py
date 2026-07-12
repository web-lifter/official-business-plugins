#!/usr/bin/env python3
"""Score entity matches based on field similarity.

Compares two entity records (JSON) and computes similarity scores
using exact match, fuzzy string distance, and phonetic matching.

Usage:
    python match-scorer.py '{"name":"John Smith","email":"john@example.com"}' '{"name":"Jon Smith","email":"john@example.com"}'
    python match-scorer.py --file1 entity_a.json --file2 entity_b.json
"""

import argparse
import json
import sys
from pathlib import Path


def levenshtein_distance(s1: str, s2: str) -> int:
    """Compute Levenshtein edit distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            cost = 0 if c1 == c2 else 1
            curr.append(min(curr[j] + 1, prev[j + 1] + 1, prev[j] + cost))
        prev = curr
    return prev[-1]


def fuzzy_similarity(a: str, b: str) -> float:
    """Return normalized similarity 0.0-1.0 based on Levenshtein distance."""
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    max_len = max(len(a), len(b))
    dist = levenshtein_distance(a.lower(), b.lower())
    return round(1.0 - dist / max_len, 3)


def soundex(name: str) -> str:
    """Compute Soundex phonetic code for a string."""
    name = name.upper().strip()
    if not name:
        return "0000"
    name = "".join(c for c in name if c.isalpha())
    if not name:
        return "0000"
    mapping = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2", "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3", "L": "4", "M": "5", "N": "5", "R": "6",
    }
    code = [name[0]]
    prev = mapping.get(name[0], "0")
    for ch in name[1:]:
        digit = mapping.get(ch, "0")
        if digit != "0" and digit != prev:
            code.append(digit)
        prev = digit if digit != "0" else prev
    return "".join(code)[:4].ljust(4, "0")


def score_entities(entity_a: dict, entity_b: dict) -> dict:
    """Score similarity between two entity records."""
    all_keys = set(entity_a.keys()) | set(entity_b.keys())
    field_scores = {}
    total_weight = 0
    weighted_sum = 0.0

    for key in sorted(all_keys):
        val_a = str(entity_a.get(key, "")).strip()
        val_b = str(entity_b.get(key, "")).strip()

        exact = 1.0 if val_a.lower() == val_b.lower() else 0.0
        fuzzy = fuzzy_similarity(val_a, val_b)
        phonetic = 1.0 if soundex(val_a) == soundex(val_b) and val_a else 0.0

        combined = max(exact, fuzzy * 0.8 + phonetic * 0.2)
        field_scores[key] = {
            "exact": exact, "fuzzy": round(fuzzy, 3),
            "phonetic": phonetic, "combined": round(combined, 3),
        }
        total_weight += 1
        weighted_sum += combined

    overall = round(weighted_sum / total_weight, 3) if total_weight else 0.0
    confidence = "HIGH" if overall >= 0.85 else "MEDIUM" if overall >= 0.6 else "LOW"

    return {"field_scores": field_scores, "overall_score": overall, "confidence": confidence}


def load_entity(raw: str | None, file_path: str | None) -> dict:
    """Load entity from inline JSON or file."""
    if file_path:
        p = Path(file_path)
        if not p.exists():
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        return json.loads(p.read_text(encoding="utf-8"))
    if raw:
        return json.loads(raw)
    print("Error: Provide entity as JSON string or --file path.", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Score entity match similarity.")
    parser.add_argument("entity_a", nargs="?", help="First entity as JSON string")
    parser.add_argument("entity_b", nargs="?", help="Second entity as JSON string")
    parser.add_argument("--file1", help="Path to first entity JSON file")
    parser.add_argument("--file2", help="Path to second entity JSON file")
    args = parser.parse_args()

    a = load_entity(args.entity_a, args.file1)
    b = load_entity(args.entity_b, args.file2)
    result = score_entities(a, b)

    print(f"Overall Score: {result['overall_score']}  |  Confidence: {result['confidence']}\n")
    for field, scores in result["field_scores"].items():
        print(f"  {field}: exact={scores['exact']} fuzzy={scores['fuzzy']} "
              f"phonetic={scores['phonetic']} combined={scores['combined']}")


if __name__ == "__main__":
    main()
