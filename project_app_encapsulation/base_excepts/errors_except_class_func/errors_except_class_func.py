from fastapi import Request
from project_app_encapsulation.base_excepts.errors_except_class.errors_except_class import ErrorsExceptClass
from fastapi.responses import ORJSONResponse


async def errors_except_class_func(request: Request, exc: ErrorsExceptClass):
    response = ORJSONResponse(content={"message": exc.message, "status_code": exc.status_code})
    return response
