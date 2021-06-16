import logging
import webbrowser

import requests


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

    def request(self, path: str, data: dict,
                method: callable = requests.post):
        response = method(f'{self.URL}/{self.VERSION}/{path}',
                          json=data, headers=self.HEADERS)

        if response.status_code != 200:
            logging.error(
                (f'Wrong status code {response.status_code}\n',
                 f'Response: {response}'),
                exc_info=True
            )

        return response

    def get(self):
        response = self.request('get', {
            'consumer_key': self.CONSUMER_KEY,
            'access_token': self.TOKEN,
            'detailType': 'simple'
        })

        return response.json()['list']

    def oauth_request(self):
        response = self.request('oauth/request', {
            'consumer_key': self.CONSUMER_KEY,
            'redirect_uri': 'task-creator:authorizationFinished'
        })

        return response.json()['code']

    def oauth_authorize(self, code):
        response = self.request('oauth/authorize', {
            'consumer_key': self.CONSUMER_KEY,
            'code': code
        })

        return response.json()

    def redirect_to_auth(self, code: str):
        webbrowser.open_new_tab(
            f'{self.URL}/auth/authorize?request_token={code}')
