from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, validator

from src.plugin_create import PluginCreate
from src.plugin_filter import PluginFilter


class What(BaseModel):
    project: str
    content: str
    priority: Optional[int] = 1
    due: Optional[str] = None
    plugin: Optional[PluginCreate] = None

    @ validator('priority')
    def priority_validator(cls, v):
        if v not in range(1, 5):
            raise ValueError('priority must be in range 1-4')
        return v


class Task(BaseModel):
    what: What
    when: Optional[List[PluginFilter]] = []

    def check(self):
        for plugin in self.when:
            if not plugin.apply():
                return False

        return True

    def get_params(self):
        return {
            'project': self.what.project,
            'content': self.what.content,
            'due': {'string': self.what.due}
        }


class Config(BaseModel):
    tasks: List[Task]
    version: int
