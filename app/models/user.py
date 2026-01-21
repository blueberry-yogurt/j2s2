from tortoise import fields
from tortoise.models import Model
from datetime import datetime

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    password_hash = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(default=datetime.utcnow)

    class Meta:
        table = "users"
