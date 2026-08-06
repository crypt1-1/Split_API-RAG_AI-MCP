import sqlite3
import os

from config import LOG_DB_FIREWALL


def search_firewall(query):

    if not LOG_DB_FIREWALL:
        return []

    if not os.path.exists(LOG_DB_FIREWALL):
        return []

    conn = sqlite3.connect(LOG_DB_FIREWALL)
    cur = conn.cursor()

    cur.execute("""
        SELECT raw
        FROM firewall
        WHERE raw LIKE ?
        ORDER BY id DESC
        LIMIT 10
    """, (f"%{query}%",))

    rows = cur.fetchall()

    conn.close()

    return [
        r[0]
        for r in rows
    ]
