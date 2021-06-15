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
        if v == '%Y-%m-%d %H:%M:%S':
            return v
        elif v == '%Y-%m-%dT%H:%M:%SZ':
            return v
        return datetime.now()

class UpdateBlog(BaseModel):
    title: str
    content: str
    m_time: datetime = None

    @validator('m_time', pre=True, always=True)
    def set_ts_now(cls, v):
        if v == '%Y-%m-%d %H:%M:%S':
            return v
        elif v == '%Y-%m-%dT%H:%M:%SZ':
            return v
        return datetime.now()
