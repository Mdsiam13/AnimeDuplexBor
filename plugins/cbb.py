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
            text = f"<b>○ Creator : This Person</a>\n○ Contact Me : <a href='https://www.facebook.com/profile.php?id=100092142554892&mibextid=ZbWKwL'>Fecbook</a>\n○ Follow Us : <a href='https://instagram.com/anime_onec?igshid=MzNlNGNkZWQ4Mg=='>Instragram</a>\n○ Channel : @Anime_Duplex\n○ Chat Group : @AnimeDuplex_Chat</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
