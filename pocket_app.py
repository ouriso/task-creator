import os
from typing import Dict
import random

from dotenv import load_dotenv

from src.api_pocket import PocketApi


load_dotenv()


CONSUMER_KEY = os.getenv('POCKET_CONSUMER_KEY')
ACCESS_TOKEN = os.getenv('POCKET_TOKEN')


pocket_api = PocketApi(CONSUMER_KEY, ACCESS_TOKEN)


def random_to_read_item() -> Dict:
    to_read = pocket_api.get()
    if len(to_read) == 0:
        return {}
    item = random.choice(list(to_read.items()))
    item_data = {
        'item_id': item[0],
        'item_title': item[1].get('resolved_title'),
        'item_url': item[1].get('resolved_url')
    }
    return item_data
