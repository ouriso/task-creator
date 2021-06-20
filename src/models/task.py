from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, validator

from .plugin_filter import PluginFilter
from .what import What


class Task(BaseModel):
    what: What
    when: Optional[List[PluginFilter]] = []

    def should_create(self):
        for plugin in self.when:
            if not plugin.apply():
                return False

        return True

    def get_params(self):
        params = {
            'project': self.what.project,
        }

        if (self.what.content):
            params['content'] = self.what.content

        if (self.what.due):
            params['due'] = {'string': self.what.due}

        if self.what.plugin:
            params = {
                **self.what.plugin.apply(),
                **params
            }

        return params
