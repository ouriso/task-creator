from typing import Dict, List, Optional

from pydantic import BaseModel, validator

from .plugin_filter import PluginFilter
from .what import What


class Task(BaseModel):
    what: What
    when: Optional[List[PluginFilter]] = []
    disabled: Optional[bool] = False

    @validator('when', pre=True)
    def parse_when(cls, v):
        if not isinstance(v, dict):
            return v
        parsed_data = []
        for key, value in v.items():
            plugin_data = {
                "name": key,
                "params": {
                    "days": value
                }
            }
            parsed_data.append(PluginFilter(**plugin_data))
        return parsed_data

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
