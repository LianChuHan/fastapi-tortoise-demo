from pydantic import BaseModel, Field
from fastapi import APIRouter
from typing import Optional,Union


# 定义成功响应的模型
class SuccessResponse(BaseModel):
    status_code: int = Field(2000, ge=2000, le=4000, description="成功响应状态码")
    message: str = Field("牛逼!!!兄弟你蒙对了!!!", description="成功响应文本")
    data: Optional[Union[dict,list]] = Field(None, description="成功响应JSON数据")


# 定义错误响应的模型
class ErrorResponse(BaseModel):
    status_code: int = Field(4000, ge=4000, description="失败响应状态码")
    message: str = Field("哥们？？？玩呢？？？", description="失败响应文本")
    data: Optional[Union[dict,list]] = Field(None, description="失败响应JSON数据")


class BaseApiRouter(APIRouter):
    def add_api_route(self, *args, **kwargs):
        kwargs.setdefault("responses", {
            200: {"model": SuccessResponse,
                  "description": "<h3>成功响应</h3>"
                  },
            422:{"model": ErrorResponse,
                  "description": "<h3>参数错误响应</h3>"
                  },
        })
        super().add_api_route(*args, **kwargs)
