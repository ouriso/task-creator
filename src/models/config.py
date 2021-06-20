from typing import List

from pydantic import BaseModel

from .task import Task


class Config(BaseModel):
    tasks: List[Task]
    version: int
