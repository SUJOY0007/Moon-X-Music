import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAx0CZD3aQwACJD1jJ-k4Y3XA0H9cEU6QHfPxyNZjhwAC6BYAAv2LEEra9hZZ9LdRQCkE")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" *ʜᴇʟʟᴏ  {message.from_user.mention()}  !* 
    ━━━━━━━ *GJ516* ━━━━━━━ 
   ✦ [{bn}](t.me/{bu}) 🥀, is a telegram music bot which Can help play your favourite Song in your group.
   ✦ All of my command can be used with my command handlers : ( / . • $ ^ ~ + * ? )
   ✦ Managed 🖤 by Jay🥀 
    ━━━━━━━ *GJ516* ━━━━━━━  
    [Frist add me in group then see my power.](https://t.me/{bu}?startgroup=true)**""",
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

