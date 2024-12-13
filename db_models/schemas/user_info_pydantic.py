from base_class.base_pydantic_model_creator import base_pydantic_model_creator
from db_models.models.user_info_model  import UserInfo


class UserInfoPydantic(base_pydantic_model_creator(UserInfo,exclude=None)):
    pass


class OperatorUserInfoPydantic(base_pydantic_model_creator(UserInfo)):
    pass
