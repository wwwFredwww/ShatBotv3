from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from backgraund import keep_alive  # Импортируем функцию для запуска Flask-сервера

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот, готовый работать круглосуточно. Чем могу помочь?")

# Основная функция для запуска бота
def main():
    # Запуск Flask-сервера для "оживления" бота
    keep_alive()

    # Токен вашего бота
    token = "7673040365:AAEWfwnvbxAJPQuYfyIbj8APj0Vnqq-H_ho"  # Замените на ваш токен от BotFather

    # Создание приложения (аналог Updater)
    app = ApplicationBuilder().token(token).build()

    # Обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()

