from tortoise import fields, models


class Bookmark(models.Model):
    id = fields.IntField(pk=True)
    # ERD의 bookmarks -> users (N:1)
    user = fields.ForeignKeyField('models.User', related_name='bookmarks')
    # ERD의 bookmarks -> quotes (N:1)
    quote = fields.ForeignKeyField('models.Quote', related_name='bookmarked_by')
    # ERD의 created_at 필드
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "bookmarks"