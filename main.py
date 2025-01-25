from telegram import InlineKeyboardButton, InlineKeyboardMarkup,Update
from telegram.ext import Updater, CommandHandler,CallbackQueryHandler,CallbackContext
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


def query(update:Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    print(f"callbackdata: {data}")


TOKEN = os.getenv("TOKEN")

updater = Updater(TOKEN) 

dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))

dispatcher.add_handler(CallbackQueryHandler(callback=query))

updater.start_polling()
updater.idle()