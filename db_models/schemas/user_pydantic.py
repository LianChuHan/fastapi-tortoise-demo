from base_class.base_pydantic_model_creator import base_pydantic_model_creator
from db_models.models.user_model import User


class UserPydantic(base_pydantic_model_creator(User,exclude=None)):
    pass
class OperatorUserPydantic(base_pydantic_model_creator(User)):
    pass
