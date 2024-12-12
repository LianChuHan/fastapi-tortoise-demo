from tortoise.contrib.pydantic import pydantic_model_creator,pydantic_queryset_creator
from db_models.models.user_info_model  import UserInfo


class UserInfoPydantic(pydantic_model_creator(UserInfo)):
    pass
