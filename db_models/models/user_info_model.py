from tortoise import fields
from db_models.base_model import BaseOrmModel
from tortoise.contrib.pydantic import pydantic_model_creator


class UserInfo(BaseOrmModel):
    remark: str = fields.CharField(max_length=26, description="备注", null=True)
    user = fields.ForeignKeyField(
        model_name="models.User",  # 确保正确的 app_label.Model 格式
        related_name="user_info",
        null=True,
    )

    class Meta:
        table = "user_info"
