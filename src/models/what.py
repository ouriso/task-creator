from typing import Optional

from pydantic import BaseModel, validator

from .plugin_create import PluginCreate


class What(BaseModel):
    project: str
    content: Optional[str]
    priority: Optional[int] = 1
    due: Optional[str] = None
    plugin: Optional[PluginCreate] = None

    @validator('priority')
    def priority_validator(cls, v):
        if v not in range(1, 5):
            raise ValueError('priority must be in range 1-4')
        return v
