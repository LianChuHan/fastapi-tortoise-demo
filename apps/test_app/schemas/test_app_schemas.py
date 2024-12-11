from pydantic import BaseModel, Field
from typing import Optional
from base_class.base_enum import BaseEnum
from fastapi import Query


class Sex(str, BaseEnum):
    男 = 1
    女 = 2
    人妖 = 3


class Likes(str, BaseEnum):
    唱 = 1
    跳 = 2
    Rap = 3
    篮球 = 4


class TestAppReqBodyApiSchemas(BaseModel):
    name: str = Field(..., min_length=1, max_length=6, description="请输入姓名")
    age: int = Field(..., ge=18, le=100, description="请输入年龄")
    sex: Sex = Field(Sex.人妖, description="请输入年龄性别 1男|2女|3人妖")

class TestAppReqBodyApiSchemas(BaseModel):
    name: str = Field(..., min_length=1, max_length=6, description="请输入姓名")
    age: int = Field(..., ge=18, le=100, description="请输入年龄")
    sex: Sex = Field(Sex.人妖, description="请输入年龄性别 1男|2女|3人妖")

class UnionQueryValueApi(BaseModel):
    title:str=Field(...,min_length=1,max_length=20,description="标题")
    info:str=Field(...,min_length=1,max_length=512,description="详情")

