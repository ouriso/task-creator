import os

from dotenv import load_dotenv

from api_pocket import PocketApi

load_dotenv()

POCKET_CONSUMER_KEY = os.getenv('POCKET_CONSUMER_KEY')

pocket_api = PocketApi(POCKET_CONSUMER_KEY)

code = pocket_api.oauth_request()
pocket_api.redirect_to_auth(code)

input()

response = pocket_api.oauth_authorize(code)
print(response)