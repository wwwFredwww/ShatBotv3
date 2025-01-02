from flask import Flask
from threading import Thread

# Инициализация Flask-приложения
app = Flask('')

@app.route('/')
def home():
    return "I'm alive!"  # Текст, который будет виден при доступе к серверу

# Функция для запуска Flask-сервера
def run():
    app.run(host='0.0.0.0', port=8080)

# Функция для запуска Flask-сервера в отдельном потоке
def keep_alive():
    t = Thread(target=run)
    t.start()

