import json
import time
from typing import Text, Any

from fastapi import Query, Depends, BackgroundTasks, Path, Body, Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, Response
from apps.test_app.schemas.test_app_schemas import Likes


async def test_app_form_api():
    return HTMLResponse(content=f"这是form-data参数接口")


async def test_app_form_one_api(title: str = Form(..., min_length=1, max_length=20, description="标题"),
                                info: Text = Form(..., description="详情")):
    return HTMLResponse(content=f"标题:{title}\n内容:{info}")


async def test_app_request_form_api(request: Request, req_form: Any = Form(..., description="Form请求参数")):
    request_form_data = await request.form()
    return HTMLResponse(content=request_form_data)
