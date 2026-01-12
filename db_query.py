from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, List

from db import DEFAULT_DB_PATH


def connect(db_path: str) -> sqlite3.Connection:
    if not Path(db_path).exists():
        raise SystemExit(f"Database not found: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def row_to_dict(row: sqlite3.Row) -> Dict[str, Any]:
    item = dict(row)
    if "data_json" in item:
        try:
            item["data_json"] = json.loads(item["data_json"])
        except json.JSONDecodeError:
            pass
    return item


def print_rows(rows: List[sqlite3.Row]) -> None:
    payload = [row_to_dict(row) for row in rows]
    print(json.dumps(payload, ensure_ascii=True, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="Query stored extraction results.")
    parser.add_argument(
        "--db",
        type=str,
        default=str(DEFAULT_DB_PATH),
        help="Path to SQLite database created by main.py",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--scene-id", type=str, help="Lookup a single scene_id")
    group.add_argument(
        "--json-path",
        type=str,
        help="SQLite JSON path for filtering (e.g. $.comprehension_layer.emotional_state.felt_emotion)",
    )
    group.add_argument("--sql", type=str, help="Run a custom SELECT query")
    parser.add_argument("--equals", type=str, help="Match value for --json-path")
    parser.add_argument("--like", type=str, help="LIKE pattern for --json-path")
    parser.add_argument("--limit", type=int, default=25, help="Limit for --json-path queries")
    args = parser.parse_args()

    with connect(args.db) as conn:
        if args.scene_id:
            row = conn.execute(
                "SELECT data_json FROM scenes WHERE scene_id = ?",
                (args.scene_id,),
            ).fetchone()
            if not row:
                print("No results.")
                return
            data = json.loads(row["data_json"])
            print(json.dumps(data, ensure_ascii=True, indent=2))
            return

        if args.json_path:
            if not args.equals and not args.like:
                parser.error("--json-path requires --equals or --like")
            if args.equals:
                rows = conn.execute(
                    """
                    SELECT scene_id, data_json
                    FROM scenes
                    WHERE json_extract(data_json, ?) = ?
                    ORDER BY scene_id
                    LIMIT ?
                    """,
                    (args.json_path, args.equals, args.limit),
                ).fetchall()
            else:
                rows = conn.execute(
                    """
                    SELECT scene_id, data_json
                    FROM scenes
                    WHERE json_extract(data_json, ?) LIKE ?
                    ORDER BY scene_id
                    LIMIT ?
                    """,
                    (args.json_path, args.like, args.limit),
                ).fetchall()
            print_rows(rows)
            return

        sql = args.sql.strip()
        lowered = sql.lstrip().lower()
        if not (lowered.startswith("select") or lowered.startswith("with")):
            raise SystemExit("Only SELECT/WITH queries are allowed.")
        rows = conn.execute(sql).fetchall()
        print_rows(rows)


if __name__ == "__main__":
    main()
