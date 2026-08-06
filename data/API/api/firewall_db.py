import sqlite3
import os

from config import log_firewall_db-path


def search_firewall(query):

    if not log_firewall_db:
        return []

    if not os.path.exists(log_firewall_db-path):
        return []

    conn = sqlite3.connect(log_firewall_db-path)
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
