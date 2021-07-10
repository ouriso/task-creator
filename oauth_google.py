"""Для подключения гуглового календаря:
    инструкция: https://developers.google.com/calendar/api/quickstart/python
    1. Создать проект в гугл-консоли
    2. Подключить к нему API календаря с разрешением читать все эвенты
    3. Во вкладке credentials создать реквизиты для входа для
       десктопного приложения.
    4. Добавить свой аккаунт в список тестировщиков в реквизитах
    5. Скачать json-файл с секретами либо скопировать инфу из командной
       строки и сохранить как json-string в переменные окружения или
       .env файл. Имя переменной GOOGLE_CONFIG
    """
import json
import os

from dotenv import load_dotenv
from src.api.google import GoogleApi

load_dotenv()

GOOGLE_CONFIG = os.getenv('GOOGLE_CONFIG')

google_api = GoogleApi(config=json.loads(GOOGLE_CONFIG))

google_api.get_or_refresh_token()
