from deep_translator import GoogleTranslator
from services.news_service import get_latest_news
from utils.constants import CATEGORIES, AVAILABLE_LANGUAGES
import requests

async def news(update, context):
    args = context.args
    if len(args) < 2:
        available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
        await update.message.reply_text(
            f"Пожалуйста, укажите категорию и язык перевода. Пример: /news business ru\n"
            f"Доступные языки: {available_langs}"
        )
        return

    category = args[0].lower()
    language = args[1].lower()

    # Проверка языка
    if language not in AVAILABLE_LANGUAGES:
        available_langs = ', '.join(f"{key} ({value})" for key, value in AVAILABLE_LANGUAGES.items())
        await update.message.reply_text(
            f"Неверный язык. Используйте один из следующих: {available_langs}"
        )
        return

    # Проверка категории
    if category not in CATEGORIES:
        await update.message.reply_text(
            f"Неверная категория. Используйте одну из следующих: {', '.join(CATEGORIES)}"
        )
        return

    if category in ["business", "entertainment", "general", "health", "science", "sports", "technology"]:
        # Используем ваш `get_latest_news` для стандартных категорий
        news_list = get_latest_news(category)

        if not news_list:
            await update.message.reply_text("Новости не найдены. Попробуйте позже.")
            return

        for news_item in news_list:
            title = news_item.get("title", "Без заголовка")
            translated_title = GoogleTranslator(source="en", target=language).translate(title)

            url = news_item.get("url", "Ссылка недоступна")
            image_url = news_item.get("image", None)

            # Формируем текст сообщения
            message = (
                f"📰 *{translated_title}*\n\n"
                f"🔗 [Читать подробнее]({url})"
            )

            if image_url:
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=image_url,
                    caption=message,
                    parse_mode="Markdown"
                )
            else:
                await update.message.reply_text(message, parse_mode="Markdown")


    elif category == "jikan_anime":
        # Логика для Jikan API
        url = "https://api.jikan.moe/v4/top/anime"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            top_anime = data["data"][:5]  # Топ-5 аниме

            for anime in top_anime:
                title = anime["title"]
                translated_title = GoogleTranslator(source="en", target=language).translate(title)

                score = anime.get("score", "N/A")
                synopsis = anime.get("synopsis", "Описание недоступно")
                translated_synopsis = GoogleTranslator(source="en", target=language).translate(synopsis)

                image_url = anime["images"]["jpg"]["image_url"]
                trailer_url = anime.get("trailer", {}).get("url", "Трейлер недоступен")

                # Формируем текст сообщения
                message = (
                    f"🎥 *{translated_title}* (Рейтинг: {score})\n"
                    f"📖 Описание: {translated_synopsis}\n"
                    f"📺 [Трейлер]({trailer_url})"
                )

                if len(message) > 1024:
                    message_parts = [message[i:i+1024] for i in range(0, len(message), 1024)]
                    await context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=image_url,
                        caption=message_parts[0],
                        parse_mode="Markdown"
                    )
                    for part in message_parts[1:]:
                        await context.bot.send_message(
                            chat_id=update.effective_chat.id,
                            text=part,
                            parse_mode="Markdown"
                        )
                else:
                    await context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=image_url,
                        caption=message,
                        parse_mode="Markdown"
                    )
        else:
            await update.message.reply_text("Не удалось получить данные о аниме. Попробуйте позже.")

    else:
        await update.message.reply_text(f"Вы выбрали категорию: {category}. Пока она не поддерживается.")

