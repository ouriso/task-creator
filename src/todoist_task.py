import os

from dotenv import load_dotenv
from todoist.api import TodoistAPI

load_dotenv()

TODOIST_TOKEN = os.getenv('TODOIST_TOKEN')

api = TodoistAPI(TODOIST_TOKEN)
api.sync()


def get_project_id(project: str):
    projects = api.projects.all(filt=(lambda x: x['name'] == project))
    id = projects[0]['id'] if len(projects) > 0 else None

    return id


def create_task(project: str, content: str, due: str) -> None:
    project_id = get_project_id(project)

    api.items.add(content, project_id=project_id, due=due)


def commit() -> None:
    api.commit()
