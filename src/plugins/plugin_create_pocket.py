import os
from typing import Dict
import random

from dotenv import load_dotenv

from ..api.pocket import PocketApi


load_dotenv()


CONSUMER_KEY = os.getenv('POCKET_CONSUMER_KEY')
ACCESS_TOKEN = os.getenv('POCKET_TOKEN')


pocket_api = PocketApi(CONSUMER_KEY, ACCESS_TOKEN)


def plugin_create_pocket() -> Dict:
    to_read = pocket_api.get()
    if len(to_read) == 0:
        return None

    item = random.choice(list(to_read.items()))

    id = item[0]
    title = item[1].get('resolved_title')
    url = item[1].get('resolved_url')

    return {
        'content':  f'[Читать: {title}]({url}) ({id})'
    }
