from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "811052"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ed")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","GJ516 MUSIC BOT")
BOT_USERNAME = getenv("BOT_USERNAME", "GJ516_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ADVENTURE_FAMILY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/9e632a66fd1f214ec1895.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/fe5fdab83c2c3300866e3.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "185646905").split()))
