from tortoise import models, fields

# 명언 번호, 제목, 내용 추가
class Saying(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200)
    content = fields.TextField()