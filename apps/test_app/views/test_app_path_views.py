from apps.test_app.schemas.test_app_schemas import Sex
from fastapi import Path
from fastapi import Path
from fastapi.responses import  JSONResponse,HTMLResponse
from apps.test_app.schemas.test_app_schemas import Sex


async def test_app_api():
    response=JSONResponse(content={"message":"ok"})
    return response

async def test_app_path_api(id:int):
    return HTMLResponse(content=f"您的参数是{id}")


async def test_app_enum_api(sex:Sex=Path(...,description="性别 1男|2女|3人妖")):
    return HTMLResponse(content=f"您的参数是{sex.name}")


async def test_app_path_path_api(path:str=Path(...,description="你要访问的path")):
    return HTMLResponse(content=f"您的路由是{path}")



