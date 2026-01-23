from app.models.bookmark import Bookmark
from app.models.user import User
from app.models.quote import Quote


class BookmarkRepository:
    @staticmethod
    async def toggle_bookmark(user: User, quote_id: int):
        # 이미 북마크가 되어 있는지 확인
        existing = await Bookmark.get_or_none(user=user, quote_id=quote_id)
        if existing:
            await existing.delete()
            return {"status": "unbookmarked"}
        users = await User.get_or_none(id = user.id)
        quote = await Quote.get_or_none(id=quote_id)
        # 새로 북마크 추가
        await Bookmark.create(user=users, quote=quote)
        return {"status": "bookmarked"}

    @staticmethod
    async def get_user_bookmarks(user_id: int):
        bookmarks = await (
            Bookmark.filter(user_id=user_id).prefetch_related("quote").all()
        )

        return [
            {
                "id": b.id,
                "quote_author": b.quote.author,
                "quote_content": b.quote.content,
                "created_at": b.created_at,
            }
            for b in bookmarks
        ]
