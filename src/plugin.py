from pydantic import BaseModel
from typing import Any, Dict


class Plugin(BaseModel):
    name: str
    params: Dict[str, Any]
    registry = {}

    def apply(self):
        plugin = self.registry[self.name]

        return plugin(**self.params)
