from fastapi import FastAPI
from project_sys_path import project_sys_path_func
from create_base_app_decoration.app_register_tortoise_orm import app_register_tortoise_orm
from create_base_app_decoration.app_register_middleware import app_register_middleware
from create_base_app_decoration.app_register_api_router import app_register_api_router
from create_base_app_decoration.app_register_run_server import app_register_run_server


async def create_app():
    await project_sys_path_func()
    app = FastAPI(
        title="这是一个简单的不能再简单demo。。。。。",
        docs_url="/desc",
        redoc_url="/re_desc",
        openapi_url="/文档看板",
        version="第无数个版本了.........",
        swagger_ui_parameters={"syntaxHighlight.theme": "github", "docExpansion": "none"}
    )
    await app_register_tortoise_orm(app)
    await app_register_middleware(app)
    await app_register_api_router(app)
    # 启动服务
    await app_register_run_server(app)
