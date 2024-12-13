from base_class.base_pydantic_model_creator import base_pydantic_model_creator
from db_models.models.circle_of_friends_model import CircleOfFriends


class CircleOfFriendsPydantic(base_pydantic_model_creator(CircleOfFriends,exclude=None)):
    pass

class OperatorCircleOfFriendsPydantic(base_pydantic_model_creator(CircleOfFriends)):
    pass
