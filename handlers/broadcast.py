import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as GJ516
from config import SUDO_USERS

@Client.on_message(filters.command(["broadcast", "gcast"]))
async def broadcast(_, message: Message):
    await message.delete()
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`starting broardcast...`")
        if not message.reply_to_message:
            await wtf.edit("**__reply to a message to broadcast__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in GJ516.iter_dialogs():
            try:
                await GJ516.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Broadcasted...` \n\n**broadcasted to  :** `{sent}` **chats** \n**faild in :** `{failed}` **chats**")
                await asyncio.sleep(0.3)
            except:
                failed=failed+1
        await message.reply_text(f"**Broadcasted successfully ** \n\n**broadcasted to :** `{sent}` **chats** \n**failed in​ :** `{failed}` **chats**")
