from app.models.diary_bookmark import DiaryBookmark


class DiaryBookmarkRepository:
    @staticmethod
    async def toggle_bookmark(user, diary_id: int):
        existing = await DiaryBookmark.get_or_none(user=user, diary_id=diary_id)
        if existing:
            await existing.delete()
            return {"status": "unbookmarked"}
        await DiaryBookmark.create(user=user, diary_id=diary_id)
        return {"status": "bookmarked"}

    @staticmethod
    async def get_user_bookmarks(user_id: int):
        diary = await DiaryBookmark.filter(user=user_id).prefetch_related("diary").all()
        return [
            {
                "id": b.id,
                "diary_title": b.diary.title,
                "diary_content": b.diary.content,
                "created_at": b.created_at,
            }
            for b in diary
        ]
