from app.models.bookmark import Bookmark
from app.models.user import User


class BookmarkRepository:
    @staticmethod
    async def toggle_bookmark(user: User, quote_id: int):
        # 이미 북마크가 되어 있는지 확인
        existing = await Bookmark.get_or_none(user=user, quote_id=quote_id)
        if existing:
            await existing.delete()
            return {"status": "unbookmarked"}

        # 새로 북마크 추가
        await Bookmark.create(user=user, quote_id=quote_id)
        return {"status": "bookmarked"}

    @staticmethod
    async def get_user_bookmarks(user_id: int):
        return await Bookmark.filter(user_id=user_id).prefetch_related("quote_id").all()
