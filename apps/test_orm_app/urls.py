from fastapi import APIRouter
from apps.test_orm_app.views.operator_orm_views import  (bulk_create_db_api,query_orm_data_api,query_orm_id_api,query_orm_foreign_key_api,
                                                         query_orm_foreign_key_data_api,query_orm_model_test_api,create_orm_model_test_api,add_circle_of_friends_api)
from base_class.base_api_router import BaseApiRouter
test_orm_app=BaseApiRouter()



test_orm_app.add_api_route(path="/bulk_create_db_api",methods=["GET"],endpoint=bulk_create_db_api,summary="批量添加",description="批量添加...",tags=["ORM_OPERATOR增删改查"])
test_orm_app.add_api_route(path="/query_orm_data_api",methods=["GET"],endpoint=query_orm_data_api,summary="查询所有",description="查询所有...",tags=["ORM_OPERATOR增删改查"])
test_orm_app.add_api_route(path="/query_orm_id_api/{id}",methods=["GET"],endpoint=query_orm_id_api,summary="ID查询单个",description="ID查询单个...",tags=["ORM_OPERATOR增删改查"])
test_orm_app.add_api_route(path="/query_orm_foreign_key_api",methods=["GET"],endpoint=query_orm_foreign_key_api,summary="查询用户所有的详情",description="外键查询...",tags=["ORM_OPERATOR增删改查"])
test_orm_app.add_api_route(path="/query_orm_foreign_key_data_api",methods=["GET"],endpoint=query_orm_foreign_key_data_api,summary="查询用户所有的朋友圈",description="外键查询...",tags=["ORM_OPERATOR增删改查"])
test_orm_app.add_api_route(path="/query_orm_model_test_api",methods=["GET"],endpoint=query_orm_model_test_api,summary="tortoise-orm的pydantic使用",description="tortoise-orm的pydantic使用...",tags=["ORM_OPERATOR增删改查"])
test_orm_app.add_api_route(path="/create_orm_model_test_api",methods=["GET"],endpoint=create_orm_model_test_api,summary="添加tortoise-orm的pydantic使用",description="添加tortoise-orm的pydantic使用...",tags=["ORM_OPERATOR增删改查"])
test_orm_app.add_api_route(path="/add_circle_of_friends_api",methods=["POST"],endpoint=add_circle_of_friends_api,summary="添加一条朋友圈",description="添加一条朋友圈...",tags=["ORM_OPERATOR增删改查"])
