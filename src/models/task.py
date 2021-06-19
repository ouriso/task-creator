from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, validator

from .plugin_filter import PluginFilter
from .what import What


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
