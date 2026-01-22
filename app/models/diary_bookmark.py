from tortoise import fields, models

class DiaryBookmark(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='diary_bookmark', on_delete=fields.CASCADE)
    diary = fields.ForeignKeyField('models.Diary', related_name='bookmarks', on_delete=fields.CASCADE)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "diary_bookmark"
        unique_together = (("user", "diary"),) # 중복 방지