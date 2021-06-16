<<<<<<< HEAD
import requests
import logging
import webbrowser

=======
import logging
import webbrowser

import requests

>>>>>>> Add pocket oauth script

class PocketApi:
    URL = 'https://getpocket.com'
    VERSION = 'v3'
    HEADERS = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Accept': 'application/json'
    }

    def __init__(self, consumer_key, token=None) -> None:
        self.CONSUMER_KEY = consumer_key
        self.TOKEN = token

    def url(self, path: str):
        return f'{self.URL}/{self.VERSION}/{path}'

    def request(self, url: str, data: dict = {},
                method: callable = requests.get):
        response = method(url, json=data, headers=self.HEADERS)

        if response.status_code != 200:
            logging.error(
                (f'Wrong status code {response.status_code}\n',
                 f'Response: {response}'),
                exc_info=True
            )

        return response

    def ouath_request(self):
        url = self.url('oauth/request')

        response = self.request(url, {
            'consumer_key': self.CONSUMER_KEY,
            'redirect_uri': 'task-creator:authorizationFinished'
        }, requests.post)

        return response.json()['code']

    def ouath_authorize(self, code):
        url = self.url('oauth/authorize')

        response = self.request(url, {
            'consumer_key': self.CONSUMER_KEY,
            'code': code
        }, requests.post)

        return response.json()

    def redirect_to_auth(self, code: str):
        webbrowser.open_new_tab(
            f'{self.URL}/auth/authorize?request_token={code}')
