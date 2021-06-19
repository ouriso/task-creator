import os

from dotenv import load_dotenv

from src.api_yandex import YandexApi

load_dotenv()

CLIENT_ID = os.getenv('YANDEX_CLIENT_ID')

yandex_api = YandexApi(CLIENT_ID)

yandex_api.redirect_to_auth()
