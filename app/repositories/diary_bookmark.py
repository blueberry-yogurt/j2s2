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