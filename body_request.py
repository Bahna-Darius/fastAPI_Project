from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str      #required
    body: str       #required
    published: Optional[bool]       #Not required


