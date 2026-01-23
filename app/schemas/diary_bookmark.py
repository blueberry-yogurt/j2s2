from pydantic import BaseModel
from datetime import datetime


class DiaryBookmarkCreate(BaseModel):
    diary_id: int


class DiaryBookmarkResponse(BaseModel):
    id: int
    diary_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class DiaryBookmarkResponses(BaseModel):
    id: int
    diary_title: str
    diary_content : str
    created_at: datetime

    class Config:
        from_attributes = True