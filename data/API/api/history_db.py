import sqlite3
import os

from paths import (DATABASE_DIR, API_DIR)

from config import API_DIR


def search_history(query):

    if not DATABASE_DIR, API_DIR:
        return []

    if not os.path.exists(LOG_DB_HISTORY):
        return []

    conn = sqlite3.connect(LOG_DB_HISTORY)
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
