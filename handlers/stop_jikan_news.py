from handlers.jikan_send import jikan_stop_send

async def stop_jikan_news(update, context):
    context.chat_data["stop_jikan_news"] = True
    await jikan_stop_send()  # Остановить отправку
    await update.message.reply_text("Новости Jikan остановлены.")


# async def stop_jikan_news(update, context):
#     context.chat_data["stop_jikan_news"] = True
#     await update.message.reply_text("Новости Jikan остановлены.")

