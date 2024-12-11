from tortoise import fields
from db_models.base_model import BaseOrmModel


class User(BaseOrmModel):
    username = fields.CharField(unique=True, max_length=16, description="用户名")
    password = fields.CharField(max_length=16, null=True, description="密码")
    class Meta:
        table = "user"


