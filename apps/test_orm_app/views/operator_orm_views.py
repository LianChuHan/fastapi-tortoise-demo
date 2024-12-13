import json
import os.path
import time
from typing import List

from starlette.responses import JSONResponse

from project_app_encapsulation.base_excepts.errors_except_class.errors_except_class import ErrorsExceptClass
from fastapi import Query, Depends, BackgroundTasks, Path, Body, File, UploadFile,Form
from fastapi.requests import Request
from fastapi.responses import HTMLResponse, Response, RedirectResponse, StreamingResponse, FileResponse
from apps.test_app.schemas.test_app_schemas import UnionQueryValueApi
from apps.test_app.schemas.test_app_schemas import Likes
from project_sys_path import STATIC_DIR
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from db_models.models.user_model import User
from db_models.models.user_info_model import UserInfo
from db_models.models.circle_of_friends_model import CircleOfFriends
from db_models.schemas.user_pydantic import UserPydantic
from db_models.schemas.user_info_pydantic import UserInfoPydantic
from db_models.schemas.circle_of_friends_pydantic import CircleOfFriendsPydantic,OperatorCircleOfFriendsPydantic
import random


async def bulk_create_db_api():
    bulk_data_lis = [
        {"username": f"张{random.randint(1, 100)}", "password": "123456"},
        {"username": f"李{random.randint(1, 100)}", "password": "123456"},
        {"username": f"王{random.randint(1, 100)}", "password": "123456"}]
    bulk_db_info = await User.bulk_create(
        [User(**create_data) for create_data in bulk_data_lis]
    )

    return HTMLResponse(content="插入成功")


async def query_orm_data_api():
    user_data = await User.all()
    ser_lis = []
    for user_obj in user_data:
        user_pydantic_base_model = await  UserPydantic.from_tortoise_orm(user_obj)
        user_dict = user_pydantic_base_model.model_dump_json()
        ser_lis.append(user_dict)
    return HTMLResponse(content=f"{ser_lis}")


async def query_orm_id_api(id: int = Path(..., description="用户id")):
    # user_obj = await  User.get(id=id)
    user_obj = await  User.filter(id=id)
    if not user_obj:
        return HTMLResponse(content="查无此人")
    user_pydantic_model = await  UserPydantic.from_tortoise_orm(user_obj)
    return HTMLResponse(content=user_pydantic_model.model_dump_json())


async def query_orm_foreign_key_api():
    user_data = await User.all()
    user_dic = {}
    for user in user_data:
        username = user.username
        user_info_lis = await user.user_info
        user_info_info = []
        for user_info_obj in user_info_lis:
            user_info_pydantic = await UserInfoPydantic.from_tortoise_orm(user_info_obj)
            user_info_info.append(user_info_pydantic.model_dump_json())
        user_dic.setdefault(username, user_info_info)
    return JSONResponse(content=user_dic)


async def query_orm_foreign_key_data_api():
    response_json = {}
    user_data = await User.all()
    for user in user_data:
        username = user.username
        circle_of_friends_data = await user.circle_of_friends
        circle_of_friends_lis = []
        for circle_of_friends in circle_of_friends_data:
            circle_of_friends_pydantic = await  CircleOfFriendsPydantic.from_tortoise_orm(circle_of_friends)
            circle_of_friends_lis.append(circle_of_friends_pydantic.model_dump_json())
        response_json.setdefault(username, circle_of_friends_lis)
    return JSONResponse(content=response_json)


async def query_orm_model_test_api():
    data_pydantic_obj = await UserPydantic.from_queryset_single(User.first())
    data_pydantic_obj_many_lis = await UserPydantic.from_queryset(User.filter())
    print(data_pydantic_obj.model_dump())
    for   data_pydantic_obj_many in data_pydantic_obj_many_lis:
        print(data_pydantic_obj_many.model_dump())

    return HTMLResponse(content="ok")
async def add_circle_of_friends_api(add_data:OperatorCircleOfFriendsPydantic=Form(...,description="添加朋友圈")):
    user_data=await User.all()
    user_obj=random.choice(user_data)
    add_obj=await CircleOfFriends.create(**add_data.model_dump(),user_id=user_obj.id)
    print(add_obj)
    add_obj_pydantic=await OperatorCircleOfFriendsPydantic.from_tortoise_orm(add_obj)
    add_obj_json=add_obj_pydantic.model_dump_json()
    return HTMLResponse(content={**add_obj_json,"username":add_obj_json.username})

async def create_orm_model_test_api():

    return HTMLResponse(content="点了一下啥也没干~~")
