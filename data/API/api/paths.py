"""
paths.py

プロジェクト全体で共通利用する Path 定義

このファイル以外では絶対パスを書かず、
必ず paths.py から import して利用する

例:
    from paths import (
        CHROMA_DIR,
        API_DIR,
        JSON_DOCS_DIR,
        MD_DOCS_DIR,
    )

保存場所：
	osnw: 192.168.50.2/data/CONFIG/atlxus/API/api/paths.py
	atlxus: 192.168.50.50/data/API/api/paths.py
"""
from pathlib import Path

# =========================================================
# ROOT
# =========================================================
ROOT = Path("/")

DATA_DIR = ROOT / "data"
HOME = ROOT / "home"
MNT = ROOT / "mnt"

# =========================================================
# osnw:		osnw
# 	192.168.50.2
# 	100.97.153.20
#	osnw.tailb112a4.ts.net
# =========================================================

# =========================================================
# CONFIG
#   /data/CONFIG
# =========================================================
CONFIG = DATA_DIR / "CONFIG"

# =========================================================
# Devices
# 	/data/CONFIG/
# =========================================================
CONF_OSNW = CONFIG / "osnw"
CONF_ATLXUS = CONFIG / "atlxus"
CONF_VKALI = CONFIG / "vkali"
CONF_ALX = CONFIG / "vm"

# =========================================================
# ROOT HOME
# =========================================================
HOME_OSNW = ROOT / "home" / "osnw"
HOME_ATLXUS = ROOT / "home" / "atlxus"

# =========================================================
# atlxus: 	atlxus-ai
# 	192.168.50.50
# 	100.67.241.92
# 	atlxus-ai.tailb112a4.ts.net
# =========================================================

# =========================================================
# MNT NVME
# 	/mnt/nvme/
# # =========================================================
NVME = MNT / "nvme"
RAG_DIR = NVME / "rag"
DOCKER_DIR = NVME / "docker"

# =========================================================
# RAG_DIR
# 	/mnt/nvme/rag
# =========================================================
CHROMA_DIR = RAG_DIR / "chroma"
DB_DIR = RAG_DIR / "db"
RAG_DOCS_DIR = RAG_DIR / "docs"
JSON_DIR = RAG_DIR / "json"
LOGDB_DIR = RAG_DIR / "logdb"
MODELS_DIR = RAG_DIR / "models"
OLLAMA_DIR = RAG_DIR / "ollama-home"

#QUERY_LOG_DB = LOGDB_DIR / "query_log.db"     # クエリ分類ログ（追加）

# =========================================================
# NVME モデル ディレクトリ
# 	/mnt/nvme/rag/models
# =========================================================
BLOBS_DIR = MODELS_DIR / "blobs"

#MODEL_CACHE = NVME / "models"                  # ローカルモデルキャッシュ（追加）
#EMBED_CACHE = NVME / "embed_cache"             # Embedding キャッシュ（追加）

# =========================================================
# DATA_DIR
# 	/data
# =========================================================
AI_DIR = DATA_DIR / "AI"
API_ROOT_DIR = DATA_DIR / "API"
EXPORT = DATA_DIR / "export"
IMPORT = DATA_DIR / "import"

# =========================================================
# AI_DIR	※ ナレッジ倉庫
# 	/data/AI
# =========================================================
JSON_DOCS_DIR = AI_DIR / "json_docs"
MD_DOCS_DIR = AI_DIR / "md_docs"
LOGS_DIR = AI_DIR / "logs"

# =========================================================
# API_ROOT_DIR
# 	/data/API
# =========================================================
API_DIR = API_ROOT_DIR / "api"
MCP_DIR = API_ROOT_DIR / "mcp"
SCRIPTS_DIR = API_ROOT_DIR / "scripts"
WEBUI_DIR = API_ROOT_DIR / "webui"

#BUILD_OUT    = AI_DIR / "build_output"         # ビルドスクリプト出力先（追加）
#CHUNK_DIR    = AI_DIR / "chunks"               # チャンク分割後ドキュメント（追加）

# =========================================================
# SCRIPTS_DIR
# 	/data/API/api/scripts
# =========================================================
BUILD_DIR = SCRIPTS_DIR / "build"
CONVERT_DIR = SCRIPTS_DIR / "convert"
QUERY_DIR = SCRIPTS_DIR / "query"
COLLECT = SCRIPTS_DIR / "collect"

# =========================================================
# API_DIR
# 	/data/API/api
# =========================================================
DATABASE_DIR = API_DIR / "database"
ROUTES_DIR = API_DIR / "routes"
SERVICES_DIR = API_DIR / "services"
UTILS_DIR = API_DIR / "utils"
# API_DIR / ["config.py", "paths.py", "query_classifier.py", "server.py"]

# =========================================================
# WEBUI_DIR
# 	/data/API/webui
# =========================================================
OPEN_WEBUI_DIR = WEBUI_DIR / "open-webui"
#OPEN_WEBUI_DIR / compose.yml

# =========================================================
# vkai:		vkali
# 	192.168.50.5
# 	100.85.254.111
# 	vkali.tailb112a4.ts.net
# =========================================================
WORKS_DIR = MNT / ”Workspace”
COLLECT_DIR = WORKS_DIR / "collector"
HISTORY_JSON_DIR = COLLECT_DIR / "history.json"
# COLLECT_DIR / "export_atuin.py"
# ALX_ROOT / "etc" / "periodic" / "hourly" / "sync_history.sh"

# =========================================================
# コモン	COMMON = CONFIG / "common"
# =========================================================

# =========================================================
# ユーティリティ
# =========================================================
def ensure_dirs(*dirs: Path) -> None:
    """指定したディレクトリが存在しなければ作成する。"""
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)


def resolve(base: Path, *parts: str) -> Path:
    """base に対して安全に相対パスを結合する。"""
    return base.joinpath(*parts)


def show_paths() -> None:
    """定義済みパス一覧を表示"""

    all_paths = {
        "DATA_DIR": DATA_DIR,
        "HOME": HOME,
        "MNT": MNT,

        "CONFIG": CONFIG,
        "CONF_OSNW": CONF_OSNW,
        "CONF_ATLXUS": CONF_ATLXUS,
        "CONF_VKALI": CONF_VKALI,

        "NVME": NVME,
        "RAG_DIR": RAG_DIR,
        "DOCKER_DIR": DOCKER_DIR,

        "CHROMA_DIR": CHROMA_DIR,
        "DB_DIR": DB_DIR,
        "RAG_DOCS_DIR": RAG_DOCS_DIR,
        "JSON_DIR": JSON_DIR,
        "LOGDB_DIR": LOGDB_DIR,
        "MODELS_DIR": MODELS_DIR,

        "AI_DIR": AI_DIR,
        "API_ROOT_DIR": API_ROOT_DIR,

        "JSON_DOCS_DIR": JSON_DOCS_DIR,
        "MD_DOCS_DIR": MD_DOCS_DIR,
        "LOGS_DIR": LOGS_DIR,

        "API_DIR": API_DIR,
        "MCP_DIR": MCP_DIR,
        "SCRIPTS_DIR": SCRIPTS_DIR,
        "WEBUI_DIR": WEBUI_DIR,

        "DATABASE_DIR": DATABASE_DIR,
        "ROUTES_DIR": ROUTES_DIR,
        "SERVICES_DIR": SERVICES_DIR,
        "UTILS_DIR": UTILS_DIR,

        "OPEN_WEBUI_DIR": OPEN_WEBUI_DIR,
    }

    width = max(len(name) for name in all_paths) + 2

    print("=== paths.py ===")
    for name, path in sorted(all_paths.items()):
        print(f"{name:<{width}} : {path}")

# スクリプト単体実行時の確認用
if __name__ == "__main__":
    show_paths()
