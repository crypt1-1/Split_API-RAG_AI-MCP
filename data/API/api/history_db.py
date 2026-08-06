import sqlite3
import os

from paths import(
    database_directory-path"DB_DIR",
    config.py_directory-path"API_DIR,
    logs_database_directory-path"LOGS_DB"
)

from config import(
    API_DIR,
)


def search_history(query):

    if not DB_DIR, API_DIR:
        return []

    if not os.path.exists(API_DIR):
        return []

    conn = sqlite3.connect(LOGS_DB)
    cur = conn.cursor()

    cur.execute("""
        SELECT timestamp, command
        FROM history
        WHERE command LIKE ?
        ORDER BY timestamp DESC
        LIMIT 5
    """, (f"%{query}%",))

    rows = cur.fetchall()
    conn.close()

    return [
        f"{r[0]} {r[1]}"
        for r in rows
    ]
