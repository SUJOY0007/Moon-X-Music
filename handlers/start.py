import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEOnXRj0K3rOj2KzPQEII_mzUUJf65_0AACUAcAAjA5gFZaJKzDHxVmBC0E")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()} , ⚔️\n\n
๏ This is [{bn}](t.me/{bu}) ,
➻ 👑Official Account🖤
💟Wish Me On 15 August 🎂
⚡My Life My Rules💪
🎶Music ka Diwana💥
🕉️Mahadev Bhakt🕉️
♍I’m not Rich ßut I’m Royal 👑
🌹Loyal and trustable Boy👩‍❤️‍👨
☺️My Freinds are my World 💗.

──────────────────
๏  All of my command can be used with My command handle : ( / . • $ ^ ~ + * ? )
➻ Made 🫶🏻 by : [𝙈𝙊𝙊𝙉𝙎𝙃𝙄𝙉𝙀❤️‍🔥](https://t.me/MT_LEXTUS_XD) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚Add Me To Your Group✚  ", url=f"https://t.me/MOON_X_MUSIC_BOT?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "⚔️ Support My Channel  ", url=f"https://t.me/AASHIYANA_MERA"
                    ),
                    InlineKeyboardButton(
                        "⚔️ Support My Group ", url=f"https://t.me/COOKIE_WORLD"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 Real Owner ", url=f"https://t.me/MT_LEXTUS_XD"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"https://t.me/MT_LEXTUS_XD"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 Git repo", url="https://telegra.ph/file/089864f9401b686c645cb.mp4"
                    )]
            ]
       ),
    )

