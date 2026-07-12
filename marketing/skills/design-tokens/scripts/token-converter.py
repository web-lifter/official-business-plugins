#!/usr/bin/env python3
"""Design token format converter.

Converts a token set between formats:
  - W3C Design Tokens JSON (with $value/$type)
  - CSS variables
  - Tailwind v4 @theme block
  - Style Dictionary source JSON (legacy `value` field)

Usage:
    python token-converter.py --in tokens.json --out app.css --format tailwind
    python token-converter.py --in tokens.json --out tokens.css --format css
    python token-converter.py --in tokens.json --out sd.json   --format style-dictionary
    python token-converter.py --in sd.json     --out tokens.json --format w3c

Detected automatically:
  - Input format inferred from file extension and content shape
  - Output format must be specified via --format

Exit codes:
    0  Success
    1  Conversion error
    2  Invalid input
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Token model
# ---------------------------------------------------------------------------

class Token:
    """A single design token: a leaf in the token tree."""

    def __init__(self, path: list[str], value: Any, type_: str | None = None) -> None:
        self.path = path  # e.g. ["color", "brand", "primary"]
        self.value = value
        self.type = type_

    @property
    def dot_name(self) -> str:
        return ".".join(self.path)

    @property
    def kebab_name(self) -> str:
        return "-".join(self.path)

    def __repr__(self) -> str:
        return f"Token({self.dot_name}={self.value!r})"


# ---------------------------------------------------------------------------
# Parsers (input → list[Token])
# ---------------------------------------------------------------------------

def parse_w3c_json(data: dict[str, Any]) -> list[Token]:
    """Parse a W3C Design Tokens spec JSON document."""
    tokens: list[Token] = []

    def walk(node: Any, path: list[str], inherited_type: str | None) -> None:
        if not isinstance(node, dict):
            return

        # Determine the current type ($type set on this group cascades down)
        current_type = node.get("$type", inherited_type)

        # Detect leaf token (has $value)
        if "$value" in node:
            tokens.append(Token(path=path, value=node["$value"], type_=current_type))
            return

        # Recurse into child groups
        for key, child in node.items():
            if key.startswith("$"):
                continue
            walk(child, path + [key], current_type)

    walk(data, [], None)
    return tokens


def parse_style_dictionary(data: dict[str, Any]) -> list[Token]:
    """Parse a Style Dictionary source file (uses `value` instead of `$value`)."""
    tokens: list[Token] = []

    def walk(node: Any, path: list[str]) -> None:
        if not isinstance(node, dict):
            return
        if "value" in node:
            tokens.append(Token(path=path, value=node["value"]))
            return
        for key, child in node.items():
            walk(child, path + [key])

    walk(data, [])
    return tokens


def parse_input(path: Path) -> list[Token]:
    """Auto-detect input format and parse."""
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    raw = path.read_text(encoding="utf-8")

    # JSON inputs
    if path.suffix == ".json":
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON in {path}: {exc}") from exc

        # Detect W3C vs Style Dictionary by checking for $value anywhere
        if _has_dollar_value(data):
            return parse_w3c_json(data)
        return parse_style_dictionary(data)

    raise ValueError(f"Unsupported input file extension: {path.suffix}")


def _has_dollar_value(node: Any) -> bool:
    """Recursively check if a JSON tree contains any '$value' key."""
    if isinstance(node, dict):
        if "$value" in node:
            return True
        return any(_has_dollar_value(v) for v in node.values())
    if isinstance(node, list):
        return any(_has_dollar_value(v) for v in node)
    return False


# ---------------------------------------------------------------------------
# Emitters (list[Token] → string)
# ---------------------------------------------------------------------------

def _resolve_reference(value: Any) -> str:
    """If the value is a token reference like '{color.brand.primary}', convert
    to a CSS var() reference. Otherwise, return as-is.
    """
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        ref = value[1:-1].replace(".", "-")
        return f"var(--{ref})"
    return str(value)


def _format_value_for_css(value: Any, type_: str | None) -> str:
    """Format a token value as a CSS string."""
    if isinstance(value, dict):
        # Composite token (e.g. shadow). Best-effort serialisation.
        if type_ == "shadow":
            return f"{value.get('offsetX', '0')} {value.get('offsetY', '0')} {value.get('blur', '0')} {value.get('spread', '0')} {value.get('color', '#000')}"
        return json.dumps(value)
    if isinstance(value, (int, float)):
        return str(value)
    return _resolve_reference(value)


def emit_css(tokens: list[Token]) -> str:
    """Emit a `:root { ... }` block of CSS variables."""
    lines = [":root {"]
    for token in tokens:
        var_name = "--" + token.kebab_name
        lines.append(f"  {var_name}: {_format_value_for_css(token.value, token.type)};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def emit_tailwind_v4(tokens: list[Token]) -> str:
    """Emit a Tailwind v4 `@theme {}` block."""
    lines = ['@import "tailwindcss";', "", "@theme {"]
    for token in tokens:
        var_name = "--" + token.kebab_name
        lines.append(f"  {var_name}: {_format_value_for_css(token.value, token.type)};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def emit_style_dictionary(tokens: list[Token]) -> str:
    """Emit a Style Dictionary source JSON document."""
    root: dict[str, Any] = {}
    for token in tokens:
        node = root
        for segment in token.path[:-1]:
            node = node.setdefault(segment, {})
        leaf_key = token.path[-1]
        node[leaf_key] = {"value": token.value}
    return json.dumps(root, indent=2) + "\n"


def emit_w3c_json(tokens: list[Token]) -> str:
    """Emit a W3C Design Tokens spec JSON document."""
    root: dict[str, Any] = {}
    for token in tokens:
        node = root
        for segment in token.path[:-1]:
            node = node.setdefault(segment, {})
        leaf_key = token.path[-1]
        leaf: dict[str, Any] = {"$value": token.value}
        if token.type:
            leaf["$type"] = token.type
        node[leaf_key] = leaf
    return json.dumps(root, indent=2) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

EMITTERS = {
    "css": emit_css,
    "tailwind": emit_tailwind_v4,
    "style-dictionary": emit_style_dictionary,
    "w3c": emit_w3c_json,
}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert design tokens between W3C JSON, CSS, Tailwind v4, and Style Dictionary.",
    )
    parser.add_argument("--in", dest="input_path", type=Path, required=True, help="Input file path")
    parser.add_argument("--out", dest="output_path", type=Path, required=True, help="Output file path")
    parser.add_argument(
        "--format",
        choices=sorted(EMITTERS.keys()),
        required=True,
        help="Target format",
    )
    args = parser.parse_args()

    try:
        tokens = parse_input(args.input_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if not tokens:
        print(f"ERROR: no tokens found in {args.input_path}", file=sys.stderr)
        return 2

    try:
        output = EMITTERS[args.format](tokens)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: emit failed: {exc}", file=sys.stderr)
        return 1

    args.output_path.write_text(output, encoding="utf-8")
    print(f"Wrote {len(tokens)} tokens -> {args.output_path} ({args.format})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
