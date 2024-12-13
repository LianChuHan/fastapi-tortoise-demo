from tortoise.contrib.pydantic import pydantic_model_creator
from functools  import partial
base_pydantic_model_creator=partial(pydantic_model_creator,exclude=("id","create_datetime","update_datetime","is_del"))