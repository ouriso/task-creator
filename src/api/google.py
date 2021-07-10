from datetime import date
import json
from typing import List
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


class GoogleApi:
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None

    def __init__(self, token: json = None, config: json = None) -> None:
        if token is not None:
            self.creds = Credentials.from_authorized_user_info(
                token, self.SCOPES)

        self.config = config

    def get_events(self, from_date: date = None, to_date: date = None
                   ) -> List[any]:
        """Возвращает список событий из календаря за указанный
        интервал времени

        Args:
            from_date (date, optional): Дата, начиная с которой
                производится фильтрация.
            to_date (date, optional): Дата, заканчивая которой
                производится фильтрация.

        Returns:
            List[any]: Список событий из календаря
        """
        service = self.build_service()
        events_result = service.events().list(
            calendarId='primary',
            timeMin=from_date, timeMax=to_date
        ).execute()
        events = events_result.get('items', [])

        return events

    def build_service(self):
        return build('calendar', 'v3', self.creds)

    def get_or_refresh_token(self):
        creds = self.creds
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        elif self.config:
            flow = InstalledAppFlow.from_client_config(
                self.config, self.SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        print(creds.to_json())
