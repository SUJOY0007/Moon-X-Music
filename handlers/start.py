import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("tg://openmessage?user_id=5564920980&message_id=53661")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** Hey {message.from_user.mention()} , ⚔️\n\n
๏ This is [{bn}](t.me/{bu}) ,  !
➻ 👑Official Account🖤
💟Wish Me On 25 July 🎂
⚡My Life My Rules💪
🎶Music ka Diwana💥
🕉️Mahadev Bhakt🕉️
♍I’m not Rich ßut I’m Royal 👑
༒︎Iɴsᴛᴀɢʀᴀᴍ ɪᴅ ༒︎k_i_n_g_o_f_d_e_v_i_l_s_0_0_7 ☠︎︎.

──────────────────
๏  All of my command can be used with My command handle : ( / . • $ ^ ~ + * ? )
➻ Made 🫶🏻 by : [𝐇𝐀𝐂𝐊𝐄𝐑❤️‍🔥](https://t.me/{me}) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ group me add kar re ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        "⚔️ Chal Channel ko support kar  ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "⚔️ Group Support ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 King owner ", url=f"https://t.me/{me}"
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

