from tortoise import models, fields

# 명언 번호, 제목, 내용 추가
class Quote(models.Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=255, null=True)

    class Meta:
        table = "quotes"