from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "14029829"))
API_HASH = getenv("API_HASH", "9643981b3fdc7c4c142481467274ad19")
BOT_TOKEN = getenv("BOT_TOKEN", "5983114890:AAEC0qcFZ7thl8mH26XNEZeqZap6dfhxqgk")
BOT_NAME = getenv("BOT_NAME","𝙈𝙊𝙊𝙉𝙎𝙃𝙄𝙉𝙀 𝙓 𝙈𝙐𝙎𝙄𝘾")
BOT_USERNAME = getenv("BOT_USERNAME", "@MOON_X_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@MT_LEXTUS_XD")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "@COOKIE_WORLD")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "@AASHIYANA_MERA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph//file/77ae3f1b2de8074ca51ff.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/691dfa4756d2a9ad7b9f4.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQBja2sCz5xBPXK26PIy_bi8ho34xaGIQRGE9oQcS5dTLHVSuLX29D8jgH20x4Fw0AcEV8Kc0XhxfvMFNjpLgSFvMXtZLMa_ajXltPME5f39Jr-PSxpeMdTiUPoGhgLx1N43U_4Jsml2fLbZBnlXG3p0DrF_sAiYhXic62tFKHJWsZ3CrN_6pO5rj7dGEPFHh4-qHjE87YR-X_rO5g6z7VBaHCMjFNTC_m3U-MoNXDuyW0Da7brXxrecC0eNXHL8FS36ZIANbSkShijUK6tfPfcwwx1BhsZE27s2WgNgi6YIe5QE9hJo94TkkPu9AzbSMXLSP7Rt_oo2KaQJv0m0Ul1hAAAAAV0qAisA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2058379497").split()))
