from typing import Any, Dict, Union

from pydantic import BaseModel


class Plugin(BaseModel):
    name: str
    params: Dict[str, Any] = {}
    registry = {}

    def apply(self) -> Union[dict, bool]:
        plugin = self.registry[self.name]

        return plugin(**self.params)
