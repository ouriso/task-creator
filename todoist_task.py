import os

from dotenv import load_dotenv
from pocket_app import random_to_read_item
from todoist import TodoistAPI

load_dotenv()

TODOIST_TOKEN = os.getenv('TODOIST_TOKEN')
PROJECT_NAME = os.getenv('PROJECT_NAME')

api = TodoistAPI(TODOIST_TOKEN)
api.sync()


def create_to_read_task(project_id=None) -> None:
    item = random_to_read_item()
    title = item.get('item_title')
    url = item.get('item_url')
    task = f'[Читать: {title}]({url})'
    # print(item)
    item = api.items.add(task, project_id=project_id)
    api.commit()
    # print(item)


if __name__ == '__main__':
    projects = api.projects.all(filt=(lambda x: x['name'] == PROJECT_NAME))
    id = projects[0]['id'] if len(projects) > 0 else None
    # if id is not None:
    #     print(id)
    create_to_read_task(id)
