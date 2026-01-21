from typing import List, Optional
from app.models.diary import Diary
from app.models.user import User

class DiaryRepository:
    @staticmethod
    async def create(user: User, title: str, content: str) -> Diary:
        return await Diary.create(title=title, content=content, user=user)

    @staticmethod
    async def get_by_id(diary_id: int) -> Optional[Diary]:
        return await Diary.get_or_none(id=diary_id)

    @staticmethod
    async def list_diaries(user_id: int, keyword: Optional[str] = None) -> List[Diary]:
        # 해당 사용자의 일기만 필터링
        query = Diary.filter(user_id=user_id)

        # 제목 검색
        if keyword:
            query = query.filter(title__icontains=keyword)

        # 최신순 정렬
        return await query.order_by("-created_at").all()

    @staticmethod
    async def update(diary: Diary, title: str, content: str) -> Diary:
        diary.title = title
        diary.content = content
        await diary.save()
        return diary

    @staticmethod
    async def delete(diary: Diary) -> None:
        await diary.delete()