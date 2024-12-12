from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from project_sys_path import project_sys_path_func, STATIC_DIR
from apps.test_app.urls import test_app
from apps.test_orm_app.urls import test_orm_app
from uvicorn.config import Config
from uvicorn.server import Server
from fastapi.exceptions import StarletteHTTPException
from project_app_encapsulation.base_excepts.errors_except_class_func.errors_except_class_func import \
    errors_except_class_func, ErrorsExceptClass
from project_app_encapsulation.base_excepts.errors_except_class_func.not_found_err_func import not_found_err_func
from project_app_encapsulation.base_excepts.errors_except_class_func.request_validation_func import \
    request_validation_func
from middleware.api_middleware import ApiBaseMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from tortoise.contrib.fastapi import register_tortoise
from conf.tortoise_conf import DATABASE_CONFIG
from fastapi.exceptions import RequestValidationError

PROJECT_APP = None


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
    global PROJECT_APP
    PROJECT_APP = app
    register_tortoise(
        app=app,
        config=DATABASE_CONFIG,
        generate_schemas=True,  # 如果数据库为空，则自动生成对应表单,生产环境不要开
        add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
    )
    app.add_middleware(middleware_class=ApiBaseMiddleware, assigned_number=1)
    # 请求中必须包含 Host 字段，为防止 HTTP 主机报头攻击，并且添加中间件的时候，还可以指定一个 allowed_hosts，那么它是干什么的呢？
    # 假设我们有服务 a.example.com, b.example.com, c.example.com
    # 但我们不希望用户访问 c.example.com，就可以像下面这么设置，如果指定为 ["*"]，或者不指定 allow_hosts，则表示无限制
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
    # 如果用户的请求头的 Accept-Encoding 字段包含 gzip，那么 FastAPI 会使用 GZip 算法压缩
    # minimum_size=1000 表示当大小不超过 1000 字节的时候就不压缩了
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(
        CORSMiddleware,
        # 允许跨域的源列表，例如 ["http://www.example.org"] 等等，["*"] 表示允许任何源
        allow_origins=["*"],
        # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
        allow_credentials=False,
        # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
        allow_methods=["*"],
        # 允许跨域请求的 HTTP 请求头列表，默认是 []，可以使用 ["*"] 表示允许所有的请求头
        # 当然 Accept、Accept-Language、Content-Language 以及 Content-Type 总之被允许的
        allow_headers=["*"],
        # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
        # expose_headers=["*"]
        # 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600，一般也很少指定
        # max_age=1000
    )
    app.mount(path="/static", app=StaticFiles(directory=STATIC_DIR), name="static")
    app.include_router(router=test_app, prefix="/test_app")
    app.include_router(router=test_orm_app, prefix="/test_orm_app")

    app.add_exception_handler(ErrorsExceptClass, errors_except_class_func)
    app.add_exception_handler(StarletteHTTPException, not_found_err_func)
    app.add_exception_handler(RequestValidationError, request_validation_func)
    config = Config(app, host="0", port=8080, reload=True,workers=4)
    server = Server(config)
    await server.serve()
