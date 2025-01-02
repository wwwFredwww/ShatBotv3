from deep_translator import GoogleTranslator
from utils.constants import AVAILABLE_LANGUAGES
from handlers.jikan_send import jikan_send, jikan_start_send, jikan_stop_send
import requests
import asyncio

async def start_jikan_news(update, context):
    args = context.args
    if len(args) < 1:
        available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
        await update.message.reply_text(
            f"Пожалуйста, укажите язык перевода. Пример: /jikanstart ru\n"
            f"Доступные языки: {available_langs}"
        )
        return

    language = args[0].lower()
    if language not in AVAILABLE_LANGUAGES:
        available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
        await update.message.reply_text(
            f"Неверный язык. Используйте один из следующих: {available_langs}"
        )
        return

    url = "https://api.jikan.moe/v4/top/anime"
    response = requests.get(url)

    if response.status_code != 200:
        await update.message.reply_text("Не удалось получить данные о аниме. Попробуйте позже.")
        return

    data = response.json()
    top_anime = data["data"]

    # Старт отправки в канал
    await jikan_start_send()

    for anime in top_anime:
        if context.chat_data.get("stop_jikan_news"):
            await jikan_stop_send()  # Остановить отправку
            await update.message.reply_text("Новости Jikan остановлены.")
            return

        title = anime["title"]
        translated_title = GoogleTranslator(source="en", target=language).translate(title)

        score = anime.get("score", "N/A")
        synopsis = anime.get("synopsis", "Описание недоступно")
        translated_synopsis = GoogleTranslator(source="en", target=language).translate(synopsis)
        trailer_url = anime.get("trailer", {}).get("url", "Трейлер недоступен")

        message = (
            f"🎥 *{translated_title}* (Рейтинг: {score})\n"
            f"📖 Описание: {translated_synopsis}"
            f"📺 [Трейлер]({trailer_url})"
        )

        await jikan_send(context, message)
        await asyncio.sleep(60)  # Пауза между отправкой сообщений

    context.chat_data["stop_jikan_news"] = False
    await update.message.reply_text("Все новости Jikan отправлены!")




# from deep_translator import GoogleTranslator
# from utils.constants import AVAILABLE_LANGUAGES
# import requests
# import asyncio
#
# async def start_jikan_news(update, context):
#     args = context.args
#     if len(args) < 1:
#         available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
#         await update.message.reply_text(
#             f"Пожалуйста, укажите язык перевода. Пример: /jikan_start ru\n"
#             f"Доступные языки: {available_langs}"
#         )
#         return
#
#     language = args[0].lower()
#     if language not in AVAILABLE_LANGUAGES:
#         available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
#         await update.message.reply_text(
#             f"Неверный язык. Используйте один из следующих: {available_langs}"
#         )
#         return
#
#     url = "https://api.jikan.moe/v4/top/anime"
#     response = requests.get(url)
#
#     if response.status_code != 200:
#         await update.message.reply_text("Не удалось получить данные о аниме. Попробуйте позже.")
#         return
#
#     data = response.json()
#     top_anime = data["data"]
#
#     current_index = context.chat_data.get("jikan_news_index", 0)
#
#     for index in range(current_index, len(top_anime)):
#         if context.chat_data.get("stop_jikan_news"):
#             context.chat_data["jikan_news_index"] = index
#             await update.message.reply_text("Новости Jikan остановлены. Для продолжения используйте команду снова.")
#             return
#
#         anime = top_anime[index]
#         title = anime["title"]
#         translated_title = GoogleTranslator(source="en", target=language).translate(title)
#
#         score = anime.get("score", "N/A")
#         synopsis = anime.get("synopsis", "Описание недоступно")
#         translated_synopsis = GoogleTranslator(source="en", target=language).translate(synopsis)
#
#         image_url = anime["images"]["jpg"]["image_url"]
#         trailer_url = anime.get("trailer", {}).get("url", "Трейлер недоступен")
#
#         message = (
#             f"🎥 *{translated_title}* (Рейтинг: {score})\n"
#             f"📖 Описание: {translated_synopsis}\n"
#             f"📺 [Трейлер]({trailer_url})"
#         )
#
#         if len(message) > 1024:
#             message_parts = [message[i:i+1024] for i in range(0, len(message), 1024)]
#             await context.bot.send_photo(
#                 chat_id=update.effective_chat.id,
#                 photo=image_url,
#                 caption=message_parts[0],
#                 parse_mode="Markdown"
#             )
#             for part in message_parts[1:]:
#                 await context.bot.send_message(
#                     chat_id=update.effective_chat.id,
#                     text=part,
#                     parse_mode="Markdown"
#                 )
#         else:
#             await context.bot.send_photo(
#                 chat_id=update.effective_chat.id,
#                 photo=image_url,
#                 caption=message,
#                 parse_mode="Markdown"
#             )
#
#         await asyncio.sleep(60)
#
#     context.chat_data["jikan_news_index"] = 0
#     context.chat_data["stop_jikan_news"] = False
#     await update.message.reply_text("Все новости Jikan отправлены!")



# -----------------------------------------------------------------------------
# async def start_jikan_news(update, context):
#     args = context.args
#     if len(args) < 2:
#         available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
#         await update.message.reply_text(
#             f"Пожалуйста, укажите категорию и язык перевода. Пример: /start jikan news jikan_anime ru\n"
#             f"Доступные языки: {available_langs}"
#         )
#         return
#
#     category = args[0].lower()
#     language = args[1].lower()
#
#     # Проверка языка
#     if language not in AVAILABLE_LANGUAGES:
#         available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
#         await update.message.reply_text(
#             f"Неверный язык. Используйте один из следующих: {available_langs}"
#         )
#         return
#
#     # Проверка категории
#     if category not in CATEGORIES:
#         await update.message.reply_text(
#             f"Неверная категория. Используйте одну из следующих: {', '.join(CATEGORIES)}"
#         )
#         return
#
#     # Получаем данные из Jikan API
#     url = "https://api.jikan.moe/v4/top/anime"
#     response = requests.get(url)
#
#     if response.status_code != 200:
#         await update.message.reply_text("Не удалось получить данные о аниме. Попробуйте позже.")
#         return
#
#     data = response.json()
#     top_anime = data["data"]  # Все доступные аниме
#     start_index = context.chat_data.get("start_index", 0)  # Начальный индекс (прогресс)
#
#     for i in range(start_index, len(top_anime)):
#         if context.chat_data.get("stop_jikan_news", False):
#             context.chat_data["start_index"] = i
#             await update.message.reply_text("Новости остановлены. Введите /start jikan news, чтобы продолжить.")
#             return
#
#         anime = top_anime[i]
#         title = anime["title"]
#         translated_title = GoogleTranslator(source="en", target=language).translate(title)
#
#         score = anime.get("score", "N/A")
#         synopsis = anime.get("synopsis", "Описание недоступно")
#         translated_synopsis = GoogleTranslator(source="en", target=language).translate(synopsis)
#
#         image_url = anime["images"]["jpg"]["image_url"]
#         trailer_url = anime.get("trailer", {}).get("url", "Трейлер недоступен")
#
#         # Формируем текст сообщения
#         message = (
#             f"🎥 *{translated_title}* (Рейтинг: {score})\n"
#             f"📖 Описание: {translated_synopsis}\n"
#             f"📺 [Трейлер]({trailer_url})"
#         )
#
#         await context.bot.send_photo(
#             chat_id=update.effective_chat.id,
#             photo=image_url,
#             caption=message[:1024],  # Обрезаем текст, если он длиннее 1024 символов
#             parse_mode="Markdown"
#         )
#
#         await asyncio.sleep(60)  # Пауза 1 минута
#
#     context.chat_data["start_index"] = 0  # Сбрасываем индекс после завершения
#     await update.message.reply_text("Все новости отправлены!")
# ------------------------------------------------------------------------

# async def start_jikan_news(update, context):
#     args = context.args
#     if len(args) < 2:
#         available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
#         await update.message.reply_text(
#             f"Пожалуйста, укажите категорию и язык перевода. Пример: /news business ru\n"
#             f"Доступные языки: {available_langs}"
#         )
#         return
#
#     category = args[0].lower()
#     language = args[1].lower()
#
#     # Проверка языка
#     if language not in AVAILABLE_LANGUAGES:
#         available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
#         await update.message.reply_text(
#             f"Неверный язык. Используйте один из следующих: {available_langs}"
#         )
#         return
#
#     # Проверка категории
#     if category not in CATEGORIES:
#         await update.message.reply_text(
#             f"Неверная категория. Используйте одну из следующих: {', '.join(CATEGORIES)}"
#         )
#         return
#
#
#     elif category == "jikan_anime":
#         # Логика для Jikan API
#         url = "https://api.jikan.moe/v4/top/anime"
#         response = requests.get(url)
#
#         if response.status_code == 200:
#             data = response.json()
#             top_anime = data["data"][:5]  # Топ-5 аниме
#
#             for anime in top_anime:
#                 title = anime["title"]
#                 translated_title = GoogleTranslator(source="en", target=language).translate(title)
#
#                 score = anime.get("score", "N/A")
#                 synopsis = anime.get("synopsis", "Описание недоступно")
#                 translated_synopsis = GoogleTranslator(source="en", target=language).translate(synopsis)
#
#                 image_url = anime["images"]["jpg"]["image_url"]
#                 trailer_url = anime.get("trailer", {}).get("url", "Трейлер недоступен")
#
#                 # Формируем текст сообщения
#                 message = (
#                     f"🎥 *{translated_title}* (Рейтинг: {score})\n"
#                     f"📖 Описание: {translated_synopsis}\n"
#                     f"📺 [Трейлер]({trailer_url})"
#                 )
#
#                 if len(message) > 1024:
#                     message_parts = [message[i:i+1024] for i in range(0, len(message), 1024)]
#                     await context.bot.send_photo(
#                         chat_id=update.effective_chat.id,
#                         photo=image_url,
#                         caption=message_parts[0],
#                         parse_mode="Markdown"
#                     )
#                     for part in message_parts[1:]:
#                         await context.bot.send_message(
#                             chat_id=update.effective_chat.id,
#                             text=part,
#                             parse_mode="Markdown"
#                         )
#                 else:
#                     await context.bot.send_photo(
#                         chat_id=update.effective_chat.id,
#                         photo=image_url,
#                         caption=message,
#                         parse_mode="Markdown"
#                     )
#         else:
#             await update.message.reply_text("Не удалось получить данные о аниме. Попробуйте позже.")
#
#     else:
#         await update.message.reply_text(f"Вы выбрали категорию: {category}. Пока она не поддерживается.")
