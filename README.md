# 🤖 Task Creator
Automatically creates tasks depending on certain conditions

## Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Get tokens
For yandex token

```
python3 src/oauth_yandex.py
```

For pocket token

```
python3 src/oauth_pocket.py
```

Enviroment variables
```
POCKET_CONSUMER_KEY
POCKET_TOKEN
YANDEX_CLIENT_ID
YANDEX_TOKEN
TODOIST_TOKEN
```

## Tests
```
python -m unittest
```
