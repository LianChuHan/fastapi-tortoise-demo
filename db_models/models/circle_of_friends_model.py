from db_models.base_model import BaseOrmModel
from tortoise import fields
from typing import Text
from tortoise.contrib.pydantic import pydantic_model_creator


class CircleOfFriends(BaseOrmModel):
    title: str = fields.CharField(max_length=100, description="标题")
    describe: Text = fields.TextField(description="详情")
    user = fields.ForeignKeyField(related_name="circle_of_friends", null=True, model_name="models.User")

    class Meta:
        table = "circle_of_friends"


