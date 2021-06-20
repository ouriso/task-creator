
from src.get_config import get_config
from src.models.config import Config
from src.todoist_task import commit, create_task


def task(request=None, context=None):
    json = get_config()

    config = Config(**json)

    for task in config.tasks:
        if task.should_create():
            create_task(**task.get_params())

    commit()


if __name__ == '__main__':
    task()
