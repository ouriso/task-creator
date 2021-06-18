import requests
from src.api_yandex import YandexApi
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv('YANDEX_CLIENT_ID')
ACCESS_TOKEN = os.getenv('YANDEX_TOKEN')
APP_PATH = '/Приложения/Task Creator'
CONFIG_NAME = 'config.json'

yandex_api = YandexApi(CLIENT_ID, ACCESS_TOKEN)


def get_config():
    href = yandex_api.get_disk_download(f'{APP_PATH}/{CONFIG_NAME}')['href']
    config = requests.get(href)
    config.encoding = 'utf-8'
    return config.json()
