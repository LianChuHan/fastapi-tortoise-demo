from tortoise.contrib.fastapi import register_tortoise
from conf.tortoise_conf import DATABASE_CONFIG
from tortoise import Tortoise


async def app_register_tortoise_orm(app):
    Tortoise.init_models(models_paths=DATABASE_CONFIG)
    register_tortoise(
        app=app,
        config=DATABASE_CONFIG,
        generate_schemas=False,  # 如果数据库为空，则自动生成对应表单,生产环境不要开
        add_exception_handlers=False,  # 生产环境不要开，会泄露调试信息
    )
