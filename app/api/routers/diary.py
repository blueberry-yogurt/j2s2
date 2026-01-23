from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from app.core.deps import get_current_user
from app.models.user import User
from app.repositories.diary_repo import DiaryRepository
from app.schemas.diary import (
    DiaryCreate,
    DiaryResponse,
    DiaryUpdate,
)  # schemas는 별도 정의 필요
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

router = APIRouter()


@router.post("/", response_model=DiaryResponse, status_code=status.HTTP_201_CREATED)
async def create_diary(
    diary_in: DiaryCreate, current_user: User = Depends(get_current_user)
):
    return await DiaryRepository.create(current_user, **diary_in.dict())


@router.get("/", response_model=List[DiaryResponse])
async def read_diaries(
    q: Optional[str] = None, current_user: User = Depends(get_current_user)
):
    # 검색어(q)를 받아 최신순으로 정렬된 목록 반환
    return await DiaryRepository.list_diaries(current_user.id, keyword=q)


@router.put("/{diary_id}", response_model=DiaryResponse)
async def update_diary(
    diary_id: int, diary_in: DiaryUpdate, current_user: User = Depends(get_current_user)
):
    diary = await DiaryRepository.get_by_id(diary_id)

    if not diary or diary.user_id != current_user.id:
        raise HTTPException(
            status_code=404, detail="일기를 찾을 수 없거나 권한이 없습니다."
        )
    return await DiaryRepository.update(diary, **diary_in.model_dump())


@router.delete("/{diary_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_diary(diary_id: int, current_user: User = Depends(get_current_user)):
    diary = await DiaryRepository.get_by_id(diary_id)
    if not diary or diary.user_id != current_user.id:
        raise HTTPException(
            status_code=404, detail="일기를 찾을 수 없거나 권한이 없습니다."
        )

    await DiaryRepository.delete(diary)
    return None


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, "CHANGE_ME_SUPER_SECRET", algorithms=["HS256"])
        username: str | None = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = await User.get_or_none(username=username)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return user
