from tortoise import fields
from tortoise.models import Model
from datetime import datetime

class Quote(Model):
    id = fields.IntField(pk=True)
    content = fields.TextField()
    author = fields.CharField(max_length=50, null=True)
    created_at = fields.DatetimeField(default=datetime.utcnow)

    class Meta:
        table = "quotes"
