from fastapi import Query, Path
from fastapi.responses import  HTMLResponse
from apps.test_app.schemas.test_app_schemas import Sex


async def test_app_params_api(str_key: str = Query(..., description="随便一个值嗷")):
    return HTMLResponse(content=f"您传递的值是{str_key}")


async def test_app_params_many_api(name: str = Query(..., description="姓名"),
                                   age: int = Query(..., description="年龄"),
                                   sex: Sex = Query(Sex.人妖, description="性别 1男|2女|3人妖")
                                   ):
    return  HTMLResponse(content=f"大家好 我是{name},性别{sex.name},今年{age}岁,从小我的妈妈告诉我，农村的孩子早当家")


async  def test_app_params_path_api(id:int=Path(...,description="请输入编号"),name:str=Query(...,description="请输入您的名称")):
    return HTMLResponse(content=f"编号:{id},姓名{name}\n验证错误，别瞎猜呀!!!")
