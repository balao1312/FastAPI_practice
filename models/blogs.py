from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class Blog(BaseModel):
    author: str
    title: str
    content: str
    m_time: datetime = None
    comments: Optional[list] = []
    likes: Optional[int] = 0

    @validator('m_time', pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.now()
