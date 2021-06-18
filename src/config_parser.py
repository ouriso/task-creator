from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, validator


class Plugin(BaseModel):
    name: str
    params: Dict[str, Any]


class What(BaseModel):
    content: str
    project: str
    priority: int
    due: str
    plugin: Optional[Plugin] = None

    @validator('priority')
    def priority_validator(cls, v):
        if v not in range(1, 5):
            raise ValueError('priority must be in range 1-4')
        return v


class Plugin1(BaseModel):
    name: str
    params: Dict[str, Any]


class When(BaseModel):
    days: List[str]
    plugins: Optional[List[Plugin1]] = None


class Task(BaseModel):
    what: What
    when: When


class Model(BaseModel):
    tasks: List[Task]
    version: int
