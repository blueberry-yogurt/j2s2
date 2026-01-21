from tortoise import field, Models

class Diary(models.Model):
    id = fields.IntField(pk=True)
    # User 모델과의 관계 설정 ForeignKey)
    user = fields.ForeignKeyField('models.User', related_name='diaries')
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "diaries"