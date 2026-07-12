#!/usr/bin/env python3
"""
introspect-schema.py

Extract table and column definitions from SQL files or a live PostgreSQL database.
Outputs a JSON summary to stdout suitable for the data-dictionary-generator skill.

Usage:
    python introspect-schema.py --sql-file schema.sql
    python introspect-schema.py --sql-file migrations/*.sql
    python introspect-schema.py --connection-string "postgresql://user:pass@host:5432/db"
"""

import argparse
import json
import re
import sys
from pathlib import Path


def parse_sql_file(file_path: str) -> list[dict]:
    """Parse CREATE TABLE statements from a SQL file and extract schema info."""
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        return []

    sql = path.read_text(encoding="utf-8")
    tables = []

    # Match CREATE TABLE statements (handles IF NOT EXISTS and schema-qualified names)
    create_pattern = re.compile(
        r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?"
        r"(?:\"?(\w+)\"?\.)?\"?(\w+)\"?\s*\((.*?)\);",
        re.IGNORECASE | re.DOTALL,
    )

    for match in create_pattern.finditer(sql):
        schema_name = match.group(1) or "public"
        table_name = match.group(2)
        body = match.group(3)

        columns = []
        constraints = []

        for line in body.split(","):
            line = line.strip()
            if not line:
                continue

            # Skip table-level constraints
            upper = line.upper().lstrip()
            if upper.startswith(("PRIMARY KEY", "FOREIGN KEY", "UNIQUE", "CHECK", "CONSTRAINT", "EXCLUDE")):
                constraints.append(parse_table_constraint(line))
                continue

            col = parse_column_definition(line)
            if col:
                columns.append(col)

        tables.append({
            "schema": schema_name,
            "table_name": table_name,
            "columns": columns,
            "constraints": constraints,
        })

    # Parse standalone ALTER TABLE ... ADD CONSTRAINT / ADD FOREIGN KEY
    alter_pattern = re.compile(
        r"ALTER\s+TABLE\s+(?:ONLY\s+)?(?:\"?(\w+)\"?\.)?\"?(\w+)\"?\s+"
        r"ADD\s+(?:CONSTRAINT\s+\"?\w+\"?\s+)?(FOREIGN\s+KEY|PRIMARY\s+KEY|UNIQUE)\s*\((.+?)\)"
        r"(?:\s+REFERENCES\s+(?:\"?(\w+)\"?\.)?\"?(\w+)\"?\s*\((.+?)\)"
        r"(?:\s+ON\s+DELETE\s+(\w+(?:\s+\w+)?))?(?:\s+ON\s+UPDATE\s+(\w+(?:\s+\w+)?))?)?",
        re.IGNORECASE,
    )

    for match in alter_pattern.finditer(sql):
        table_name = match.group(2)
        constraint_type = match.group(3).upper().replace("  ", " ")
        local_columns = match.group(4).strip()
        foreign_table = match.group(6)
        foreign_columns = match.group(7)
        on_delete = match.group(8)

        constraint = {
            "type": constraint_type.replace("FOREIGN KEY", "FK").replace("PRIMARY KEY", "PK"),
            "columns": local_columns,
        }
        if foreign_table:
            constraint["references_table"] = foreign_table
            constraint["references_columns"] = foreign_columns.strip() if foreign_columns else None
        if on_delete:
            constraint["on_delete"] = on_delete.strip()

        # Attach to existing table if found
        for t in tables:
            if t["table_name"] == table_name:
                t["constraints"].append(constraint)
                break

    return tables


def parse_column_definition(line: str) -> dict | None:
    """Parse a single column definition line from a CREATE TABLE body."""
    col_pattern = re.compile(
        r"^\"?(\w+)\"?\s+([\w\s\(\),]+?)(?:\s+(NOT\s+NULL|NULL))?"
        r"(?:\s+DEFAULT\s+(.+?))?(?:\s+(PRIMARY\s+KEY))?"
        r"(?:\s+(UNIQUE))?"
        r"(?:\s+REFERENCES\s+(?:\"?(\w+)\"?\.)?\"?(\w+)\"?\s*\(\"?(\w+)\"?\)"
        r"(?:\s+ON\s+DELETE\s+(\w+(?:\s+\w+)?))?)?\s*$",
        re.IGNORECASE,
    )

    match = col_pattern.match(line.strip().rstrip(","))
    if not match:
        return None

    col_name = match.group(1)
    raw_type = match.group(2).strip()
    nullable_flag = match.group(3)
    default_val = match.group(4)
    is_pk = match.group(5) is not None
    is_unique = match.group(6) is not None
    ref_table = match.group(8)
    ref_column = match.group(9)
    on_delete = match.group(10)

    is_nullable = True
    if nullable_flag and "NOT" in nullable_flag.upper():
        is_nullable = False

    col = {
        "column_name": col_name,
        "data_type": raw_type,
        "is_nullable": is_nullable,
    }
    if default_val:
        col["default"] = default_val.strip()
    if is_pk:
        col["is_primary_key"] = True
    if is_unique:
        col["is_unique"] = True
    if ref_table:
        col["references"] = {
            "table": ref_table,
            "column": ref_column,
        }
        if on_delete:
            col["references"]["on_delete"] = on_delete.strip()

    return col


def parse_table_constraint(line: str) -> dict:
    """Parse a table-level constraint line."""
    constraint = {"raw": line.strip().rstrip(",")}

    upper = line.upper().strip()
    if "PRIMARY KEY" in upper:
        constraint["type"] = "PK"
    elif "FOREIGN KEY" in upper:
        constraint["type"] = "FK"
    elif "UNIQUE" in upper:
        constraint["type"] = "UNIQUE"
    elif "CHECK" in upper:
        constraint["type"] = "CHECK"
    else:
        constraint["type"] = "OTHER"

    cols_match = re.search(r"\(([^)]+)\)", line)
    if cols_match:
        constraint["columns"] = cols_match.group(1).strip()

    return constraint


def introspect_live_database(connection_string: str) -> list[dict]:
    """Introspect a live PostgreSQL database using psycopg2."""
    try:
        import psycopg2
        import psycopg2.extras
    except ImportError:
        print(
            "Error: psycopg2 is not installed. Install it with:\n"
            "  pip install psycopg2-binary\n"
            "Or use --sql-file to parse a SQL file offline.",
            file=sys.stderr,
        )
        sys.exit(1)

    tables = []
    try:
        conn = psycopg2.connect(connection_string)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        # Get tables
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
            ORDER BY table_name
        """)
        table_rows = cur.fetchall()

        for trow in table_rows:
            tname = trow["table_name"]

            # Get columns
            cur.execute("""
                SELECT column_name, data_type, udt_name, is_nullable, column_default
                FROM information_schema.columns
                WHERE table_schema = 'public' AND table_name = %s
                ORDER BY ordinal_position
            """, (tname,))

            columns = []
            for crow in cur.fetchall():
                columns.append({
                    "column_name": crow["column_name"],
                    "data_type": crow["udt_name"] or crow["data_type"],
                    "is_nullable": crow["is_nullable"] == "YES",
                    "default": crow["column_default"],
                })

            # Get constraints
            cur.execute("""
                SELECT tc.constraint_type, kcu.column_name,
                       ccu.table_name AS foreign_table,
                       ccu.column_name AS foreign_column
                FROM information_schema.table_constraints tc
                JOIN information_schema.key_column_usage kcu
                    ON tc.constraint_name = kcu.constraint_name
                LEFT JOIN information_schema.constraint_column_usage ccu
                    ON ccu.constraint_name = tc.constraint_name
                WHERE tc.table_schema = 'public' AND tc.table_name = %s
            """, (tname,))

            constraints = []
            for crow in cur.fetchall():
                c = {
                    "type": crow["constraint_type"],
                    "columns": crow["column_name"],
                }
                if crow["foreign_table"]:
                    c["references_table"] = crow["foreign_table"]
                    c["references_columns"] = crow["foreign_column"]
                constraints.append(c)

            tables.append({
                "schema": "public",
                "table_name": tname,
                "columns": columns,
                "constraints": constraints,
            })

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error connecting to database: {e}", file=sys.stderr)
        sys.exit(1)

    return tables


def main():
    parser = argparse.ArgumentParser(
        description="Extract schema information from SQL files or a live PostgreSQL database.",
        epilog="Examples:\n"
               "  python introspect-schema.py --sql-file schema.sql\n"
               "  python introspect-schema.py --sql-file migrations/*.sql\n"
               '  python introspect-schema.py --connection-string "postgresql://user:pass@localhost:5432/mydb"',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--sql-file",
        nargs="+",
        help="Path(s) to .sql files to parse for CREATE TABLE statements",
    )
    parser.add_argument(
        "--connection-string",
        help="PostgreSQL connection string for live database introspection (requires psycopg2)",
    )

    args = parser.parse_args()

    if not args.sql_file and not args.connection_string:
        parser.error("Provide either --sql-file or --connection-string")

    tables = []

    if args.sql_file:
        for f in args.sql_file:
            tables.extend(parse_sql_file(f))

    if args.connection_string:
        tables.extend(introspect_live_database(args.connection_string))

    output = {
        "source": "sql_file" if args.sql_file else "live_database",
        "table_count": len(tables),
        "tables": tables,
    }

    json.dump(output, sys.stdout, indent=2, default=str)
    print()  # trailing newline


if __name__ == "__main__":
    main()
