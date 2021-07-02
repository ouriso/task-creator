from src.get_config import get_config
from src.models.config import Config
from src.todoist_task import commit, create_task


def task(request=None, context=None, dry_run=False):
    json = get_config()

    config = Config(**json)

    for task in config.tasks:
        if not task.should_create():
            continue

        params = task.get_params()
        if params.get('content'):
            if dry_run:
                print(params)
            else:
                create_task(**params)

    if not dry_run:
        commit()


if __name__ == '__main__':
    task()
