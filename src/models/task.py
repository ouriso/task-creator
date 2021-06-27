from typing import Dict, List, Optional

from pydantic import BaseModel

from .plugin_filter import PluginFilter
from .what import What


class Task(BaseModel):
    what: What
    when: Optional[List[PluginFilter]] = []
    disabled: Optional[bool] = False

    def should_create(self) -> bool:
        if self.disabled:
            return False

        for plugin in self.when:
            if not plugin.apply():
                return False

        return True

    def get_params(self) -> Dict[str, any]:
        params = {
            'project': self.what.project,
        }

        if self.what.content:
            params['content'] = self.what.content

        if self.what.due:
            params['due'] = {'string': self.what.due}

        if self.what.plugin:
            params.update(self.what.plugin.apply())

        return params
