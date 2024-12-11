from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from db_models.models.user_model import User


class UserPydantic(pydantic_model_creator(User)):
    pass
