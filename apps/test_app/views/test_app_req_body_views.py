from typing import Any

from fastapi import Body
from fastapi.requests import Request
from fastapi.responses import  HTMLResponse
from apps.test_app.schemas.test_app_schemas import TestAppReqBodyApiSchemas


async def test_app_req_body_api(req_body: TestAppReqBodyApiSchemas):
    req_body_ser = req_body.model_dump()
    name = req_body_ser.get("name")
    age = req_body_ser.get("age")
    sex_obj = req_body_ser.get("sex")
    return HTMLResponse(content=f"大家好!我是:{name}\n性别:{sex_obj.name}\n今年:{age}岁")


async def test_app_request_body_api(request: Request, request_body: Any=Body(...,description="请求体参数，随便输入~")):
    body = await  request.body()
    return HTMLResponse(content=body.decode("utf-8"))
