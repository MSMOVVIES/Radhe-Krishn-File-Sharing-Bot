#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>‣ ᴍʏ ɴᴀᴍᴇ : ᴘᴇʀᴍᴀɴᴇɴᴛ\n‣ ᴅᴀᴛᴀʙᴀꜱᴇ : ᴄʟᴏᴜᴅ\n‣ ꜱᴇʀᴠᴇʀ : ʙᴏꜱꜱ ʜᴏᴍᴇ\n‣ ᴄʀᴇᴀᴛᴏʀ: <a href='https://t.me/MS_Contact_RoBot'>ᴍs_ʜᴀᴄᴋᴇʀ</a>\n‣ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/MS_Movvies'>ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ</a>\n‣ вᴜɪʟᴅ ѕᴛᴀᴛᴜѕ: v2.7.1 [ ѕᴛᴀʙʟᴇ ]</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔙 ʙᴀᴄᴋ 🔙", callback_data = "start")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
