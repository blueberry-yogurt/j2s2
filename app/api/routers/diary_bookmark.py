from fastapi import APIRouter, Depends, status
from typing import List
from app.core.deps import get_current_user
from app.models.user import User
from app.repositories.diary_bookmark import DiaryBookmarkRepository
from app.schemas.diary_bookmark import DiaryBookmarkCreate, DiaryBookmarkResponse

router = APIRouter(prefix="/diary", tags=["diary bookmark"])

@router.post("/", status_code=status.HTTP_201_CREATED)
async def toggle_diary_bookmark(
        bookmark_id: DiaryBookmarkCreate,
        current_user: User = Depends(get_current_user)
):
    return await DiaryBookmarkRepository.toggle_bookmark(
        user=current_user,
        diary_id=bookmark_id.diary_id
    )

@router.get("/", response_model=List[DiaryBookmarkResponse])
async def get_my_diary_bookmarks(current_user: User = Depends(get_current_user)):
    return await DiaryBookmarkRepository.get_user_bookmarks(current_user.id)