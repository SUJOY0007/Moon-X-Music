from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "14029829"))
API_HASH = getenv("API_HASH", "9643981b3fdc7c4c142481467274ad19")
BOT_TOKEN = getenv("BOT_TOKEN", "5833438026:AAGtn7_NXqFbDRvh8VMajWWACa06kBldY9k")
BOT_NAME = getenv("BOT_NAME","𝙈𝙊𝙊𝙉𝙎𝙃𝙄𝙉𝙀 𝙓 𝙈𝙐𝙎𝙄𝘾")
BOT_USERNAME = getenv("BOT_USERNAME", "@MOON_X_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@MT_LEXTUS_XD")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "@COOKIE_WORLD")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "@AASHIYANA_MERA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://telegra.ph//file/77ae3f1b2de8074ca51ff.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/691dfa4756d2a9ad7b9f4.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQCjZ1O6hggF3i6MApH06F0Ynvi8PEcyoznJ91jfGJOMWs_8P1JVt2P2sPQRDmwExz3q0qw77KQqBH26sQLw0zTSvrMeV-zf9YOYKh8Fac9vBoBn_HISOEEyQ0gzFEGiH6t7O5VVH48RJ09HKc_nOQqCAi-twWIjeR8HcBLv4I5LboE2MeiRhxDRBnREPimi5L3B21bC5mkC81uUdmBdzGal_5iQFY0au0KaH8C_pGHb8s-3B4VoSBrErp4mfIr7x0wep7NqyFtzdg6uqTNV09OFm4HGEpYQILS9AQEe1B2LsGarY38srKoM0-NcHMMlKrhYfGDMIR6sC9bcMhqAJwl7AAAAAV0qAisA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2058379497").split()))
