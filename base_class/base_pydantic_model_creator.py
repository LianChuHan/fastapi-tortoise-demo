from tortoise.contrib.pydantic import pydantic_model_creator
from functools  import partial
base_pydantic_model_creator=partial(pydantic_model_creator,exclude_readonly=("id","create_datetime","update_datetime"))