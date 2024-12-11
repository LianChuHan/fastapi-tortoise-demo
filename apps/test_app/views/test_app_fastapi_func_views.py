import json
import os.path
import time
from typing import List
from project_app_encapsulation.base_excepts.errors_except_class.errors_except_class import ErrorsExceptClass
from fastapi import Query, Depends, BackgroundTasks, Path, Body, File, UploadFile
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, Response, RedirectResponse, StreamingResponse, FileResponse
from apps.test_app.schemas.test_app_schemas import UnionQueryValueApi
from apps.test_app.schemas.test_app_schemas import Likes
from project_sys_path import STATIC_DIR
from fastapi.security import  HTTPBasicCredentials,HTTPBasic
security = HTTPBasic()

async def test_app_depends_api_depends(name: str = Query(..., description="姓名"),
                                       age: int = Query(..., gt=18, le=100, description="年龄")):
    try:
        req_data = {"name": name, "age": age}
        json.dumps(req_data)
    except Exception as err:
        return HTMLResponse(content="<h1 style=‘color:pink’>数据错误，返回不出来嗷<h1>")
    return  HTMLResponse(content=req_data)


async def test_app_depends_api(req_data: dict = Depends(test_app_depends_api_depends)):
    return HTMLResponse(content=f"接收参数为{req_data}")

async def test_app_base_model_args_api(name: str = Query(..., max_length=10, min_length=1, description="姓名"),
                                       age: int = Query(18, ge=18, le=100, description="年龄")):
    return HTMLResponse(content=f"姓名:{name},年龄:{age}")


async def test_app_list_query_value_api(
        likes: List[Likes] = Query(..., max_length=4, min_length=1,
                                   description="请选择你的爱好：1 唱|2 跳|3 Rap|4 篮球")):
    return HTMLResponse(content=f"您的爱好是:{[like.name for like in likes]}")


async def test_app_request_obj_api(request: Request):
    method = request.method
    url = request.url
    cookies = request.cookies
    headers = request.headers
    path_params = request.path_params
    query_params = request.query_params
    response = HTMLResponse(
        content=f'''method:{method}\nurl:{url}\ncookies:{cookies}\nheaders:{dict(headers)}\npath_params:{path_params}\nquery_params:{query_params}''')
    return response


async def test_app_response_obj_api():
    response = Response(
        content='''{"message":"这是响应你的数据嗷~"}''',
        media_type="application/json",
        headers={"test_header": "test_headers"}
    )
    return response


def back_task_func():
    for i in range(5):
        time.sleep(0.5)
        print(f"执行一个后台任务--->{i}")


async def test_app_back_task_api(back_task: BackgroundTasks):
    message = "添加一个后台任务"
    back_task.add_task(func=back_task_func)
    return HTMLResponse(content=message)


async def test_app_upload_load_file(file: UploadFile = File(..., description="上传文件名称")):
    filename = file.filename
    file_size = file.size
    file_data = await file.read()
    print(file_data)
    return HTMLResponse(content=f"上传文件:{filename}\n文件大小:{file_size}")


async def test_app_self_exception_response_api():
    raise ErrorsExceptClass(message="自定错误", status_code=301)


async def test_app_red_url_api():
    response = RedirectResponse(url="http://www.baidu.com")
    return response


async def test_app_return_bytes_response_func():
    for i in range(10):
        time.sleep(0.2)
        message = f"这是{i}"
        yield message.encode(encoding="utf-8")


async def test_app_return_bytes_response_api(request: Request):
    return StreamingResponse(test_app_return_bytes_response_func())


async def test_app_return_bytes_file_api(file_name=Query(...,description="请输入您要下载的文件名称",min_length=1,max_length=256)):
    resource = FileResponse(filename="这是送你的一个图片.png", path=os.path.join(STATIC_DIR,file_name))
    return resource


async def test_app_http_basic_cre_api(credentials: HTTPBasicCredentials = Depends(security)):
    return HTMLResponse(content={f"您输入的账号是:{credentials.username}\n您输入的密码是:{credentials.password}"})
