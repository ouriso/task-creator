import logging
import os
from typing import Dict
import requests
import random

from dotenv import load_dotenv

load_dotenv()


HEADERS = {
    'Content-Type': 'application/json; charset=UTF-8',
    'X-Accept': 'application/json'
}
CONSUMER_KEY = os.getenv('POCKET_KEY_WIN')
ACCESS_TOKEN = os.getenv('POCKET_TOKEN')
GET_LIST_URL = 'https://getpocket.com/v3/get'


def get_list_to_read() -> Dict:
    response = requests.post(GET_LIST_URL, json={
        'consumer_key': CONSUMER_KEY,
        'access_token': ACCESS_TOKEN,
        'detailType': 'simple'
    }, headers=HEADERS)

    if response.status_code != 200:
        logging.error(
            (f'Wrong status code {response.status_code}\n',
            f'Response: {response}'),
            exc_info=True
        )
        return {}
    try:
        to_read_list = response.json()['list']
    except KeyError:
        logging.error(
            f'Response does not contains "list": {response}',
            exc_info=True
        )
    return to_read_list

def random_to_read_item() -> Dict:
    to_read = get_list_to_read()
    if len(to_read) == 0:
        return {}
    item = random.choice(list(to_read.items()))
    item_data = {
        'item_id': item[0],
        'item_title': item[1].get('resolved_title'),
        'item_url': item[1].get('resolved_url')
    }
    return item_data
