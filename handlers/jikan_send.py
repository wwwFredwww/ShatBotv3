import logging
from telegram.ext import ContextTypes
from telegram.error import TelegramError

# Глобальная переменная для состояния
sending_enabled = False
channel_id = "@jikananime"  # Укажите корректное имя канала (например, @jikananime)

# Функция для отправки новости
async def jikan_send(context: ContextTypes.DEFAULT_TYPE, news_message: str):
    if sending_enabled:
        try:
            await context.bot.send_message(chat_id=channel_id, text=news_message)
            logging.info(f"Message sent to {channel_id}: {news_message}")
        except TelegramError as e:
            logging.error(f"Error sending message: {e}")

# Функция для начала отправки новостей
async def jikan_start_send():
    global sending_enabled
    sending_enabled = True
    logging.info("Started sending news.")

# Функция для остановки отправки новостей
async def jikan_stop_send():
    global sending_enabled
    sending_enabled = False
    logging.info("Stopped sending news.")

# Функция для изменения канала
async def change_channel(new_channel_id: str):
    global channel_id
    channel_id = new_channel_id
    logging.info(f"Channel changed to {channel_id}")


# import logging
# from telegram import Bot
# from telegram.error import TelegramError
#
# # Инициализация бота с токеном
# TOKEN = "7673040365:AAEWfwnvbxAJPQuYfyIbj8APj0Vnqq-H_ho"
# bot = Bot(token=TOKEN)
#
# # Глобальная переменная для хранения состояния отправки сообщений
# sending_enabled = False
# channel_id = "https://t.me/jikananime"  # Изначальный адрес, который можно будет менять
#
# # Функция для отправки новости
# async def jikan_send(news_message: str):
#     if sending_enabled:
#         try:
#             await bot.send_message(chat_id=channel_id, text=news_message)
#             logging.info(f"Message sent to {channel_id}: {news_message}")
#         except TelegramError as e:
#             logging.error(f"Error sending message: {e}")
#
# # Функция для начала отправки новостей
# async def jikan_start_send():
#     global sending_enabled
#     sending_enabled = True
#     logging.info("Started sending news.")
#
# # Функция для остановки отправки новостей
# async def jikan_stop_send():
#     global sending_enabled
#     sending_enabled = False
#     logging.info("Stopped sending news.")
#
# # Функция для изменения канала
# async def change_channel(new_channel_id: str):
#     global channel_id
#     channel_id = new_channel_id
#     logging.info(f"Channel changed to {channel_id}")
