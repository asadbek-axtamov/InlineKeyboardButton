from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler
import os

like_count = 0
dislike_count = 0


def start(update, context):

    photo = open("image.png", "rb")

    keyboard = [
        [InlineKeyboardButton(f"👍 {like_count}", callback_data="like"), InlineKeyboardButton(f"👎 {dislike_count}", callback_data="dislike")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_photo(photo=photo, reply_markup=reply_markup)


TOKEN = os.getenv("TOKEN")

updater = Updater(TOKEN) 

dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()