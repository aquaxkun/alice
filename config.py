import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 20201467
API_HASH = "5aec6e31f6522645ae31653500a3038e"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7427145769:AAHlPocCpn0h-ZRvIQuS582jAqmfWBYCOVg"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://aquaxkun1:aquaxkun1@cluster0.j1ogv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0""

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002361677751

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7842550519

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/ShadowArmy47"
SUPPORT_GROUP = "https://t.me/ShadowArmy47"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQE0P_sAfsnXsiSLEuxMrgTCWj98h22VNNnPGRsaAM4Feco_Rsfx9FDxQ6qFj9bVY7qne8Ed-F2hjnFIndzLBZI2I7aPzMc9gFhGa4mYesj62UztbJYqTVnMfX_1u1R0I76QdNgSOebmOlWx52JJEkhACzODRPCfpbq9TeDtl1IAi2eS2nbU7JNiU_HcNzzMbgaCVlZ1A-UPlWs0R0B3lAgYuID9-BvhMs1XvlVuZvoR4bV74m-moJOnA9K5ZY4OtarQNUMoPOu7g72flT3JjCN2Kqn16LvylZOi7snun28qTYHVdtdd8hU7OndJ9rl0E1hoclB2N2E423TGs5hyG5twO-jIRAAAAAHTc9L3AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"

PING_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
STATS_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
STREAM_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/bba2cb7344239937d89cf-cc08c2480c9c428cd2.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
