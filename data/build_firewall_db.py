"""
scripts/build_firewall_db.py — ファイアウォールログ (CSV/iptables形式) を SQLite に取り込む
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from paths import FIREWALL_DB, LOG_DIR, ensure_dirs
from api.database.firewall_db import insert_firewall, _connect, _ensure_table

# 取り込み対象ログファイルのパターン（変更可）
DEFAULT_LOG_GLOB = "firewall*.log"


def _parse_iptables_line(line: str) -> dict | None:
    """
    iptables/nftables 形式の1行をパースする。
    例: ... SRC=1.2.3.4 DST=10.0.0.1 ... DPT=22 ... [BLOCK]
    """
    if not line.strip():
        return None

    def _extract(pattern: str, default: str | None = None) -> str | None:
        m = re.search(pattern, line)
        return m.group(1) if m else default

    src     = _extract(r"SRC=([\d.]+)")
    dst     = _extract(r"DST=([\d.]+)")
    dpt     = _extract(r"DPT=(\d+)")
    proto   = _extract(r"PROTO=(\w+)")
    action  = _extract(r"\[(BLOCK|ALLOW|DROP|REJECT)\]") or "BLOCK"
    rule_id = _extract(r"RULE=(\S+)")

    if not src:
        return None

    return {
        "src_ip":   src,
        "dst_ip":   dst,
        "dst_port": int(dpt) if dpt else None,
        "protocol": proto,
        "action":   action,
        "rule_id":  rule_id,
        "detail":   line.strip()[:300],
    }


def _parse_csv_row(row: dict) -> dict | None:
    """CSV 形式（列: src_ip, dst_ip, dst_port, protocol, action, rule_id, detail）"""
    src = row.get("src_ip", "").strip()
    if not src:
        return None
    return {
        "src_ip":   src,
        "dst_ip":   row.get("dst_ip"),
        "dst_port": int(row["dst_port"]) if row.get("dst_port", "").isdigit() else None,
        "protocol": row.get("protocol"),
        "action":   row.get("action", "BLOCK").upper(),
        "rule_id":  row.get("rule_id"),
        "detail":   row.get("detail"),
    }


def build_firewall_db(log_dir: Path = LOG_DIR, glob: str = DEFAULT_LOG_GLOB) -> None:
    """
    LOG_DIR 以下のファイアウォールログを FIREWALL_DB に取り込む。
    .csv → CSV パーサー、それ以外 → iptables 形式パーサー を使用する。
    """
    ensure_dirs(FIREWALL_DB.parent)

    log_files = list(log_dir.glob(glob))
    if not log_files:
        print(f"[WARN] ログファイルが見つかりません: {log_dir}/{glob}")
        return

    total = 0
    for lf in log_files:
        print(f"[INFO] 処理中: {lf}")
        count = 0

        if lf.suffix.lower() == ".csv":
            with lf.open(encoding="utf-8", errors="replace") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    parsed = _parse_csv_row(row)
                    if parsed:
                        insert_firewall(**parsed)
                        count += 1
        else:
            for line in lf.read_text(encoding="utf-8", errors="replace").splitlines():
                parsed = _parse_iptables_line(line)
                if parsed:
                    insert_firewall(**parsed)
                    count += 1

        print(f"  → {count} 件追加")
        total += count

    print(f"\n=== build_firewall_db 完了: 合計 {total} 件 ===")


if __name__ == "__main__":
    build_firewall_db()
