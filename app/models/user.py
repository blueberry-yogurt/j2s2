from tortoise import models, fields


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=64)
    password_hash = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"
