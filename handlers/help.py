from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "👋 *Список доступных команд:*\n\n"
        "/start - Начать общение с ботом\n"
        "/news <категория> <язык> - Получить новости по категории и языку (пример: `/news technology en`)\n"
        "/jikanstart <язык> - Получать новости про аниме с Jikan (пример: `/jikanstart ru`)\n"
        "/jikanstop - Остановить получение новостей про аниме с Jikan\n"
        "/categories - Просмотреть доступные категории новостей\n"
        "/languages - Просмотреть доступные языки перевода\n"
        "/startsending - Начать отправку новостей Jikan в Telegram-канал\n"
        "/stopsending - Остановить отправку новостей Jikan в Telegram-канал\n"
        "/changechannel <ID канала> - Изменить канал для отправки новостей (пример: `/change_channel @new_channel_id`)\n"
        "/help - Показать это сообщение"
    )

    await update.message.reply_text(help_text, parse_mode="Markdown")








# from telegram import Update
# from telegram.ext import ContextTypes
#
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     help_text = (
#         "👋 *Список доступных команд:*\n\n"
#         "/start - Начать общение с ботом\n"
#         "/news <категория> <язык> - Получить новости по категории и языку (пример: `/news technology en`)\n"
#         "/jikanstart <язык> - Получать новости про аниме с Jikan (пример: `/jikanstart ru`)\n"
#         "/jikanstop - Остановить получение новостей про аниме с Jikan\n"
#         "/categories - Просмотреть доступные категории новостей\n"
#         "/languages - Просмотреть доступные языки перевода\n"
#         "/help - Показать это сообщение"
#     )
#
#     await update.message.reply_text(help_text, parse_mode="Markdown")









# from telegram import Update
# from telegram.ext import ContextTypes
#
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     help_text = (
#         "👋 *Список доступных команд:*\n\n"
#         "/start - Начать общение с ботом\n"
#         "/news \\<категория\\> \\<язык\\> - Получить новости по категории и языку \\(пример: `/news technology en`\\)\n"
#         "/jikan\\_start \\<язык\\> - Получать новости про аниме с Jikan \\(пример: `/jikan_start ru`\\)\n"
#         "/jikan\\_stop - Остановить получение новостей про аниме с Jikan\n"
#         "/categories - Просмотреть доступные категории новостей\n"
#         "/languages - Просмотреть доступные языки перевода\n"
#         "/help - Показать это сообщение"
#     )
#
#     await update.message.reply_text(help_text, parse_mode="MarkdownV2")





# from telegram import Update
# from telegram.ext import ContextTypes
#
# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     help_text = (
#         "👋 *Список доступных команд:*\n"
#         "/start - Начать общение с ботом\n"
#         "/news <категория> <язык> - Получить новости по категории и языку (пример: /news technology en)\n"
#         "/start_jikan - Получать новости про аниме с jikan\n"
#         "/stop_jikan - Остановить получение новостей про аниме с jikan\n"
#         "/categories - Просмотреть доступные категории новостей\n"
#         "/languages - Просмотреть доступные языки перевода\n"
#         "/help - Показать это сообщение"
#     )
#     await update.message.reply_text(help_text, parse_mode="Markdown")
