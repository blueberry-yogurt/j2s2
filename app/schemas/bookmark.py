from pydantic import BaseModel
from datetime import datetime


class BookmarkCreate(BaseModel):
    quote_id: int


class BookmarkResponse(BaseModel):
    id: int
    # quote_id: int
    created_at: datetime

    class Config:
        from_attributes = True
