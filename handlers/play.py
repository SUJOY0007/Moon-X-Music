import os
from os import path
from pyrogram import Client, filters
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT, SUPPORT_GROUP, CHANNEL_UPDATES
from helpers.filters import command
from helpers.decorators import errors
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(
    command(["play", "p", "fuck"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def play(_, message: Message):
    global que
    global useer

    await message.delete()

    programmer = await message.reply("🔄 Processing Query... Please Wait!")

    chumtiya = message.from_user.mention

    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Exportgabbar"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
                except:
                    await programmer.edit(
                        "Frist make me admin")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "assistant successful joined the chat, now you can play songs​.")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await programmer.edit(
                        f" Assistant is not, send /join Frist time to order the assistant join the chat .")
    try:
        await USER.get_chat(chid)
    except Exception as e:
        await programmer.edit(
            f" Assistant failed to this chat.\n\n reason : {e}")
        return
    
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"Duration Limit Exceeded\n\n•Allowed Duration: {DURATION_LIMIT} minutes (s)"
            )

        file_name = get_file_name(audio)
        title = file_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name))
            else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            title = "NaN"
            duration = "NaN"
            views = "NaN"

        if (dur / 60) > DURATION_LIMIT:
            await programmer.edit(
                f"Duration Limit Exceeded\n\n•Allowed Duration: {DURATION_LIMIT} minutes (s)"
            )
            return
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await programmer.edit(
                "Usage: /play [Music Name or \nYoutube Link or Reply to Audio] 🥀 "
            )
        await programmer.edit("🔎")
        query = message.text.split(None, 1)[1]
        # print(query)
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f"thumb{title}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(":")
            for i in range(len(dur_arr) - 1, -1, -1):
                dur += int(dur_arr[i]) * secmul
                secmul *= 60

        except Exception as e:
            await programmer.edit(
                "Not found, Try searching with the song name"
            )
            print(str(e))
            return

        if (dur / 60) > DURATION_LIMIT:
            await programmer.edit(
                f"Duration Limit Exceeded\n\n•Allowed Duration:  {DURATION_LIMIT} minutes (s)"
            )
            return
        file_path = await converter.convert(youtube.download(url))
    ACTV_CALLS = []
    chat_id = message.chat.id
    for x in callsmusic.pytgcalls.active_calls:
        ACTV_CALLS.append(int(x.chat_id))
    if int(chat_id) in ACTV_CALLS:
        position = await queues.put(chat_id, file=file_path)
        await message.reply_text(
            text=f"**⏳ Added to Queue at #{position} **\n💡**Title :**[{title[:65]}]({url})\n\n🕤**Duration :** `{duration}` **min**\n👤**Requested by​ : **{chumtiya}",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("📨 Channel", url=f"https://t.me/{CHANNEL_UPDATES}")
                ],
                [
                   InlineKeyboardButton("🗑️ Close Menu", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
    else:
        await callsmusic.pytgcalls.join_group_call(
                chat_id, 
                InputStream(
                    InputAudioStream(
                        file_path,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )

        await message.reply_text(
            text=f"**📡 Started Streaming **\n💡**Title​:** [{title[:65]}]({url})\n🕕 **Duration:** `{duration}` Min\n👤**Requested by​:** {chumtiya}\n⏯️**Playing in:**`{message.chat.title}`\n🎥 **Stream type:** YouTube music\n",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton("📨 Channel ", url=f"https://t.me/{CHANNEL_UPDATES}")
                ],
                [
                    InlineKeyboardButton("🗑️ Close Menu", callback_data="close_play")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

    return await programmer.delete()

@Client.on_callback_query(filters.regex("close_play"))
async def in_close_play(_, query: CallbackQuery):
    await query.message.delete()
