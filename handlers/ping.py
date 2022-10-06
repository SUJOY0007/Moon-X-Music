import os
import asyncio
import time
from datetime import datetime

import psutil

from handlers import StartTime
from helpers.filters import command
from telegram.utils.helpers import escape_markdown, mention_html
from config import BOT_USERNAME, SUPPORT_GROUP, CHANNEL_UPDATES, PING_IMG, BOT_NAME
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


@Client.on_message(command(["ping", "repo", "gabbar", "alive"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.delete()
    boottime = time.time()
    bot_uptime = escape_markdown(get_readable_time((time.time() - StartTime)))
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await message.reply_sticker("CAACAgUAAx0CZD3aQwACJ_RjPkP-o8j8W0cchyTkG24G-LyMlgAC9wQAAgjiQFZpD9oahx09sioE")
    jay = await message.reply_photo(
        photo=f"{PING_IMG}",
        caption=" Pinging...⚡ ",
    )
    await jay.edit_text(
        f"""<b> pong ping ! ⚡</b>\n  🏓 `{resp} ms`\n\n<b><u>{BOT_NAME} system stats:</u></b>\n\n✨ Uptime : {bot_uptime}\n🔮 Cpu : {cpu}%\n💫 Disk : {disk}%\n❤️ Ram : {mem}\n\n||ᴍᴀᴅᴇ 🖤 ʙʏ [ᴇxᴘᴏʀᴛ ɢᴀʙʙᴀʀ🥀](https://t.me/export_gabbar)||""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📨 Support ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "📨 Channel ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "💡Git repo ", url="https://te.legra.ph/file/db7c6b18567b5e81165ad.mp4"
                    )
                ]
            ]
        ),
    )
