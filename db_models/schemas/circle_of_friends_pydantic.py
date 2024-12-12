from tortoise.contrib.pydantic import pydantic_model_creator
from db_models.models.circle_of_friends_model import CircleOfFriends


class CircleOfFriendsPydantic(pydantic_model_creator(CircleOfFriends)):
    pass

class OperatorCircleOfFriendsPydantic(pydantic_model_creator(CircleOfFriends,exclude=("id","create_datetime","update_datetime","is_del"))):
    pass
