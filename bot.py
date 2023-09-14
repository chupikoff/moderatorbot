import sqlite3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import settings_testing as settings

# Функция для открытия подключения к базе данных
def open_db_connection():
    conn = sqlite3.connect('word_count.db')
    return conn

# Функция для создания таблицы (если ее нет)
def create_table():
    conn = open_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS word_count
                  (user_id INTEGER PRIMARY KEY, user_name TEXT, word_count INTEGER)''')
    conn.commit()
    conn.close()
def count_words(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.username
    
    # Разбиваем текст сообщения на слова и считаем их количество
    word_count = len(update.message.text.split())
    
    # Обновляем счетчик слов в базе данных
    current_word_count = get_word_count(user_id)
    update_word_count(user_id, user_name, current_word_count + word_count)
# Остальной код остается без изменений
def show_stats(update, context):
    conn = open_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, user_name, word_count FROM word_count")
    results = cursor.fetchall()
    conn.close()  # Закрываем соединение после использования
    
    stats_text = "Статистика пользователей:\n"
    for user_id, user_name, word_count in results:
        stats_text += f"{user_name} (ID: {user_id}): {word_count} слов\n"
    
    update.message.reply_text(stats_text)
def get_word_count(user_id):
    conn = open_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT word_count FROM word_count WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return result[0]
    else:
        return 0  # Возвращаем 0, если запись не найдена

def update_word_count(user_id, user_name, new_word_count):
    conn = open_db_connection()
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO word_count (user_id, user_name, word_count) VALUES (?, ?, ?)", (user_id, user_name, new_word_count))
    conn.commit()
    conn.close()
def main():
    create_table()  # Создаем таблицу (если ее нет)
    
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    
    # Добавляем обработчик сообщений для подсчета слов
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, count_words))
    
    # Добавляем обработчик команды /stats
    dp.add_handler(CommandHandler("stats", show_stats))
    
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()

