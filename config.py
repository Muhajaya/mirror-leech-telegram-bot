import os
import json

def getenv(key, default=None, cast=str):
    val = os.getenv(key, default)
    if val is None:
        return None
    try:
        if cast == bool:
            return str(val).lower() in ["1", "true", "yes", "on"]
        if cast == int:
            return int(val)
        if cast == list:
            return json.loads(val)
        if cast == dict:
            return json.loads(val)
        return cast(val)
    except Exception:
        return default

# REQUIRED CONFIG
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = getenv("OWNER_ID", 0, int)
TELEGRAM_API = getenv("TELEGRAM_API", 0, int)
TELEGRAM_HASH = getenv("TELEGRAM_HASH", "")

# OPTIONAL CONFIG
TG_PROXY = getenv("TG_PROXY", {}, dict)
USER_SESSION_STRING = getenv("USER_SESSION_STRING", "")
CMD_SUFFIX = getenv("CMD_SUFFIX", "")
AUTHORIZED_CHATS = getenv("AUTHORIZED_CHATS", "")
SUDO_USERS = getenv("SUDO_USERS", "")
DATABASE_URL = getenv("DATABASE_URL", "")
STATUS_LIMIT = getenv("STATUS_LIMIT", 4, int)
DEFAULT_UPLOAD = getenv("DEFAULT_UPLOAD", "rc")
STATUS_UPDATE_INTERVAL = getenv("STATUS_UPDATE_INTERVAL", 15, int)
FILELION_API = getenv("FILELION_API", "")
STREAMWISH_API = getenv("STREAMWISH_API", "")
EXCLUDED_EXTENSIONS = getenv("EXCLUDED_EXTENSIONS", "")
INCOMPLETE_TASK_NOTIFIER = getenv("INCOMPLETE_TASK_NOTIFIER", False, bool)
YT_DLP_OPTIONS = getenv("YT_DLP_OPTIONS", "")
USE_SERVICE_ACCOUNTS = getenv("USE_SERVICE_ACCOUNTS", False, bool)
NAME_SUBSTITUTE = getenv("NAME_SUBSTITUTE", "")
FFMPEG_CMDS = getenv("FFMPEG_CMDS", {}, dict)
UPLOAD_PATHS = getenv("UPLOAD_PATHS", {}, dict)

# GDrive Tools
GDRIVE_ID = getenv("GDRIVE_ID", "")
IS_TEAM_DRIVE = getenv("IS_TEAM_DRIVE", False, bool)
STOP_DUPLICATE = getenv("STOP_DUPLICATE", False, bool)
INDEX_URL = getenv("INDEX_URL", "")

# Rclone
RCLONE_PATH = getenv("RCLONE_PATH", "")
RCLONE_FLAGS = getenv("RCLONE_FLAGS", "")
RCLONE_SERVE_URL = getenv("RCLONE_SERVE_URL", "")
RCLONE_SERVE_PORT = getenv("RCLONE_SERVE_PORT", 0, int)
RCLONE_SERVE_USER = getenv("RCLONE_SERVE_USER", "")
RCLONE_SERVE_PASS = getenv("RCLONE_SERVE_PASS", "")

# JDownloader
JD_EMAIL = getenv("JD_EMAIL", "")
JD_PASS = getenv("JD_PASS", "")

# Sabnzbd
USENET_SERVERS = getenv("USENET_SERVERS", [], list)

# Nzb search
HYDRA_IP = getenv("HYDRA_IP", "")
HYDRA_API_KEY = getenv("HYDRA_API_KEY", "")

# Update
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

# Leech
LEECH_SPLIT_SIZE = getenv("LEECH_SPLIT_SIZE", 0, int)
AS_DOCUMENT = getenv("AS_DOCUMENT", False, bool)
EQUAL_SPLITS = getenv("EQUAL_SPLITS", False, bool)
MEDIA_GROUP = getenv("MEDIA_GROUP", False, bool)
USER_TRANSMISSION = getenv("USER_TRANSMISSION", False, bool)
HYBRID_LEECH = getenv("HYBRID_LEECH", False, bool)
LEECH_FILENAME_PREFIX = getenv("LEECH_FILENAME_PREFIX", "")
LEECH_DUMP_CHAT = getenv("LEECH_DUMP_CHAT", "")
THUMBNAIL_LAYOUT = getenv("THUMBNAIL_LAYOUT", "")

# qBittorrent/Aria2c
TORRENT_TIMEOUT = getenv("TORRENT_TIMEOUT", 0, int)
BASE_URL = getenv("BASE_URL", "")
BASE_URL_PORT = getenv("BASE_URL_PORT", 0, int)
WEB_PINCODE = getenv("WEB_PINCODE", False, bool)

# Queueing system
QUEUE_ALL = getenv("QUEUE_ALL", 0, int)
QUEUE_DOWNLOAD = getenv("QUEUE_DOWNLOAD", 0, int)
QUEUE_UPLOAD = getenv("QUEUE_UPLOAD", 0, int)

# RSS
RSS_DELAY = getenv("RSS_DELAY", 600, int)
RSS_CHAT = getenv("RSS_CHAT", "")
RSS_SIZE_LIMIT = getenv("RSS_SIZE_LIMIT", 0, int)

# Torrent Search
SEARCH_API_LINK = getenv("SEARCH_API_LINK", "")
SEARCH_LIMIT = getenv("SEARCH_LIMIT", 0, int)
SEARCH_PLUGINS = getenv("SEARCH_PLUGINS", [], list)
