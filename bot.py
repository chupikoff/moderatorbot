from glob import glob
from random import choice
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings as settings

def greet_user(update, context):
    update.message.reply_text("Я живий")

def send_random_spb(update, context):
    random_spb_list = glob('opt/spb/*.mp3')
    spb_filename = choice(random_spb_list)
    chat_id = update.effective_chat.id
    context.bot.send_audio(chat_id=chat_id, audio=open(spb_filename, 'rb'))

def send_random_image(update, context):
    random_photos_list = glob('opt/images/*.jpg')
    pic_filename = choice(random_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(pic_filename, 'rb'))

def greet_user_after_message(update, context):
    # Проверяем ID пользователя
    if update.message.from_user.id == 211139051:  # change id
        update.message.reply_text("Це реплай користувачу @chupikoff")

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("image", send_random_image))
    dp.add_handler(CommandHandler("spb", send_random_spb))
    
    # Обробник повідомлень
    dp.add_handler(MessageHandler(Filters.text, greet_user_after_message))
    
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
