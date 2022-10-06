import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAx0CZD3aQwACJ_hjPkS4Komyh2BnI4s_NUdAdzYSpwAClgAD5KDOB-VgUnOaX5eTKgQ")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**Hey {message.from_user.mention()},🖤**\n   **This is [{bn}](t.me/{bu}), ** 🥀\n **A powerfull music player bot with some awesome and useful features.**\n\n**All of my commands are (/ . • $ ^ ~ + * ?).\n\nManaged 🖤 by: Jay🥀**"""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✚ Add me to your Group", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "📨 Channel ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        "📨 Support ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        "👤 Bot Owner ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "👨‍💻 Developer ", url=f"https://t.me/export_gabbar"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "💡 Git repo", url="https://github.com/MrProgrammer72/GJ516VCBOT"
                    )]
            ]
       ),
    )

