from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# 일기 생성 시 받을 데이터
class DiaryCreate(BaseModel):
    title: str
    content: str


# 일기 수정 시 받을 데이터
class DiaryUpdate(BaseModel):
    title: Optional[str]
    content: Optional[str]


# API 응답으로 내보낼 데이터 형식
class DiaryResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True
