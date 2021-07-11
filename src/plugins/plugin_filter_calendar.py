from datetime import date, timedelta
import json
import os
from src.api.google import GoogleApi
from dotenv import load_dotenv

load_dotenv()

GOOGLE_TOKEN = json.loads(os.getenv('GOOGLE_TOKEN'))


def plugin_filter_calendar(summary: str) -> bool:
    today = date.today()
    start = str(today) + 'T00:00:00Z'
    end = str(today + timedelta(days=1)) + 'T00:00:00Z'

    google_api = GoogleApi(token=GOOGLE_TOKEN)

    events = google_api.get_events(from_date=start, to_date=end)

    for event in events:
        if summary == event['summary']:
            return True

    return False
