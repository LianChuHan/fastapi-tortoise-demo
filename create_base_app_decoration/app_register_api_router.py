from fastapi.staticfiles import StaticFiles
from project_sys_path import STATIC_DIR
from apps.test_app.urls import test_app
from apps.test_orm_app.urls import test_orm_app
from fastapi.exceptions import StarletteHTTPException
from project_app_encapsulation.base_excepts.errors_except_class_func.errors_except_class_func import \
    errors_except_class_func, ErrorsExceptClass
from project_app_encapsulation.base_excepts.errors_except_class_func.not_found_err_func import not_found_err_func
from project_app_encapsulation.base_excepts.errors_except_class_func.request_validation_func import \
    request_validation_func
from fastapi.exceptions import RequestValidationError


async def app_register_api_router(app):
    app.mount(path="/static", app=StaticFiles(directory=STATIC_DIR), name="static")
    app.include_router(router=test_app, prefix="/test_app")
    app.include_router(router=test_orm_app, prefix="/test_orm_app")

    app.add_exception_handler(ErrorsExceptClass, errors_except_class_func)
    app.add_exception_handler(StarletteHTTPException, not_found_err_func)
    app.add_exception_handler(RequestValidationError, request_validation_func)
