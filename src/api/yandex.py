import logging
import webbrowser
from urllib import parse

import requests


class YandexApi:
    URL = 'https://cloud-api.yandex.net'
    VERSION = 'v1'
    HEADERS = {
        'Accept': 'application/json'
    }

    def __init__(self, client_id: str, token=None) -> None:
        self.CLIENT_ID = client_id
        self.TOKEN = token

    def request(self, path: str, method: callable = requests.get):
        headers = {
            **self.HEADERS,
            'Authorization': f'OAuth {self.TOKEN}'
        }
        response = method(f'{self.URL}/{self.VERSION}/{path}', headers=headers)

        if response.status_code != 200:
            logging.error(
                (f'Wrong status code {response.status_code}\n',
                 f'Response: {response}'),
                exc_info=True
            )

        return response

    def get_disk_resources(self, path: str):
        query = {'path': path}

        response = self.request(f'disk/resources?{parse.urlencode(query)}')

        return response.json()

    def get_disk_download(self, path: str):
        query = {'path': path}

        response = self.request(
            f'disk/resources/download?{parse.urlencode(query)}')

        return response.json()

    def redirect_to_auth(self):
        webbrowser.open_new_tab(
            f'https://oauth.yandex.ru/authorize?response_type=token&client_id={self.CLIENT_ID}')
