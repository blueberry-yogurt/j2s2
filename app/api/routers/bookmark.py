from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.core.deps import get_current_user
from app.models.user import User

from app.repositories.bookmark_repo import BookmarkRepository
from app.schemas.bookmark import BookmarkCreate, BookmarkResponse, BookmarkResponses

router = APIRouter(prefix="/bookmark", tags=["bookmark"])


@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def toggle_quote_bookmark(
    bookmark_in: BookmarkCreate, current_user: User = Depends(get_current_user)
):
    """
    명언 북마크 토글:
    이미 북마크가 되어 있으면 해제, 없으면 추가합니다.
    """
    # BookmarkRepository에 정의한 toggle 로직 호출
    result = await BookmarkRepository.toggle_bookmark(
        user=current_user,
        quote_id = bookmark_in.quote_id
    )
    return result


@router.get("/", response_model=List[BookmarkResponses])
async def read_my_bookmarks(current_user: User = Depends(get_current_user)):
    """
    현재 로그인한 사용자가 북마크한 모든 명언 목록을 가져옵니다.
    """
    bookmarks = await BookmarkRepository.get_user_bookmarks(current_user.id)
    print(bookmarks)
    return bookmarks
