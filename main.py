from telegram.ext import ApplicationBuilder, CommandHandler
from utils.keep_alive import keep_alive
from handlers.start_jikan_news import start_jikan_news
from handlers.stop_jikan_news import stop_jikan_news
from handlers.start import start
from handlers.languages import languages
from handlers.categories import categories
from handlers.news import news
from handlers.help import help_command
from handlers.jikan_send import jikan_send, jikan_start_send, jikan_stop_send, change_channel

TOKEN = "7673040365:AAEWfwnvbxAJPQuYfyIbj8APj0Vnqq-H_ho"


async def start_jikan_sending(update, context):
    """Команда для запуска отправки новостей в канал."""
    await jikan_start_send()
    await update.message.reply_text("Отправка новостей Jikan в канал запущена.")


async def stop_jikan_sending(update, context):
    """Команда для остановки отправки новостей в канал."""
    await jikan_stop_send()
    await update.message.reply_text("Отправка новостей Jikan в канал остановлена.")


async def change_jikan_channel(update, context):
    """Команда для смены канала отправки новостей."""
    if not context.args:
        await update.message.reply_text("Пожалуйста, укажите ID нового канала. Пример: /change_channel @new_channel_id")
        return

    new_channel_id = context.args[0]
    await change_channel(new_channel_id)
    await update.message.reply_text(f"Канал изменен на {new_channel_id}")


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("languages", languages))
    app.add_handler(CommandHandler("categories", categories))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("jikanstart", start_jikan_news))
    app.add_handler(CommandHandler("jikanstop", stop_jikan_news))
    app.add_handler(CommandHandler("help", help_command))

    # Обработчики для отправки в канал
    app.add_handler(CommandHandler("startsending", start_jikan_sending))
    app.add_handler(CommandHandler("stopsending", stop_jikan_sending))
    app.add_handler(CommandHandler("changechannel", change_jikan_channel))

    # Запуск бота
    keep_alive()
    app.run_polling()


if __name__ == "__main__":
    main()




# from telegram.ext import ApplicationBuilder, CommandHandler
#
# from utils.keep_alive import keep_alive
# from handlers.start_jikan_news import start_jikan_news
# from handlers.stop_jikan_news import stop_jikan_news
# from handlers.start import start
# from handlers.languages import languages
# from handlers.categories import categories
# from handlers.news import news
# from handlers.help import help_command
#
# TOKEN = "7673040365:AAEWfwnvbxAJPQuYfyIbj8APj0Vnqq-H_ho"
#
# def main():
#     app = ApplicationBuilder().token(TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("languages", languages))
#     app.add_handler(CommandHandler("categories", categories))
#     app.add_handler(CommandHandler("news", news))
#     app.add_handler(CommandHandler("jikanstart", start_jikan_news))
#     app.add_handler(CommandHandler("jikanstop", stop_jikan_news))
#     app.add_handler(CommandHandler("help", help_command))
#
#     keep_alive()
#     app.run_polling()
#
# if __name__ == "__main__":
#     main()








# from telegram.ext import ApplicationBuilder, CommandHandler
# from utils.keep_alive import keep_alive
# from handlers.start_jikan_news import start_jikan_news
# from handlers.stop_jikan_news import stop_jikan_news
# from handlers.start import start
# from handlers.languages import languages
# from handlers.categories import categories
# from handlers.news import news
# from handlers.help import help_command
#
# TOKEN = "7673040365:AAEWfwnvbxAJPQuYfyIbj8APj0Vnqq-H_ho"
#
# def main():
#     app = ApplicationBuilder().token(TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("languages", languages))
#     app.add_handler(CommandHandler("categories", categories))
#     app.add_handler(CommandHandler("news", news))
#     app.add_handler(CommandHandler("startjikan", start_jikan_news))
#     app.add_handler(CommandHandler("stopjikan", stop_jikan_news))
#     app.add_handler(CommandHandler("help", help_command))
#
#     keep_alive()
#     app.run_polling()
#
# if __name__ == "__main__":
#     main()

