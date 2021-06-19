
from src.get_config import get_config
from src.config_parser import Config
from src.todoist_task import commit, create_task

json = get_config()

config = Config(**json)

for task in config.tasks:
    if task.check():
        create_task(**task.get_content())

commit()