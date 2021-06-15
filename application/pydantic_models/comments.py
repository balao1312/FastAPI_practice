# not used yet

from pydantic import BaseModel
from datetime import datetime


class Comments(BaseModel):
    author: str
    content: str
    m_time: datetime
