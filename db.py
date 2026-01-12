import json
import sqlite3
from pathlib import Path
from typing import Any, Dict, Optional, Union

DEFAULT_DB_PATH = Path(__file__).resolve().parent / "eqbench.db"


def init_db(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS scenes (
            scene_id TEXT PRIMARY KEY,
            data_json TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at TEXT NOT NULL DEFAULT (datetime('now'))
        );
        """
    )


def store_scene(
    result: Dict[str, Any],
    db_path: Union[str, Path] = DEFAULT_DB_PATH,
    scene_id: Optional[str] = None,
) -> None:
    if scene_id is None:
        scene_id = result.get("scene_id")
    if not scene_id:
        raise ValueError("scene_id is required (pass --scene-id or include it in the output)")

    data_json = json.dumps(result, ensure_ascii=True, separators=(",", ":"))
    db_path = str(db_path)

    with sqlite3.connect(db_path) as conn:
        init_db(conn)
        conn.execute(
            """
            INSERT INTO scenes (scene_id, data_json)
            VALUES (?, ?)
            ON CONFLICT(scene_id) DO UPDATE SET
                data_json = excluded.data_json,
                updated_at = datetime('now')
            """,
            (scene_id, data_json),
        )
