from fastapi import APIRouter

from apps.test_app.views.test_app_fastapi_func_views import (test_app_depends_api, test_app_base_model_args_api, \
                                                             test_app_list_query_value_api, test_app_request_obj_api, test_app_response_obj_api, test_app_back_task_api,
                                                             test_app_upload_load_file, test_app_self_exception_response_api, test_app_red_url_api,
                                                             test_app_return_bytes_response_api, test_app_return_bytes_file_api, test_app_http_basic_cre_api
                                                             )

from apps.test_app.views.test_app_params_views import test_app_params_api, test_app_params_many_api, \
    test_app_params_path_api
from apps.test_app.views.test_app_path_views import test_app_api, test_app_path_api, test_app_enum_api, \
    test_app_path_path_api
from apps.test_app.views.test_app_req_body_views import test_app_req_body_api, test_app_request_body_api
from apps.test_app.views.test_app_form_view import  test_app_form_api,test_app_request_form_api,test_app_form_one_api
from base_class.base_api_router import BaseApiRouter
test_app=BaseApiRouter()



test_app.add_api_route(path="/test_app_api",methods=["GET"],endpoint=test_app_api,summary="路由参数普通的接口",description="路由参数普通的接口...",tags=["路由参数ParamsAPI"])
test_app.add_api_route(path="/test_app_path_api/{id}",methods=["GET"],endpoint=test_app_path_api,summary="路由参数接口",description="路由参数接口...",tags=["路由参数ParamsAPI"])
test_app.add_api_route(path="/test_app_enum_api/{sex}",methods=["GET"],endpoint=test_app_enum_api,summary="路由枚举参数接口",description="路由枚举参数接口...",tags=["路由参数ParamsAPI"])
test_app.add_api_route(path="/test_app_path_path_api/{path:path}",methods=["GET"],endpoint=test_app_path_path_api,summary="路径路由参数接口",description="路径路由参数接口...",tags=["路由参数ParamsAPI"])

test_app.add_api_route(path="/test_app_params_path_api/{id}",methods=["GET"],endpoint=test_app_params_path_api,summary="查询参数路由参数接口",description="查询参数路由参数接口...",tags=["路由参数ParamsAPI","查询参数QueryAPI"])

test_app.add_api_route(path="/test_app_params_api",methods=["GET"],endpoint=test_app_params_api,summary="查询参数普通接口",description="查询参数普通接口...",tags=["查询参数QueryAPI"])
test_app.add_api_route(path="/test_app_params_many_api",methods=["GET"],endpoint=test_app_params_many_api,summary="查询多个参数普通接口",description="查询多个参数普通接口...",tags=["查询参数QueryAPI"])


test_app.add_api_route(path="/test_app_depends_api",methods=["GET"],endpoint=test_app_depends_api,summary="Depends请求预处理接口",description="Depends请求预处理接口...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_base_model_args_api",methods=["GET"],endpoint=test_app_base_model_args_api,summary="BaseModel限制参数接口",description="BaseModel限制参数接口...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_list_query_value_api",methods=["GET"],endpoint=test_app_list_query_value_api,summary="List类型请求参数接口",description="List类型请求参数接口...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_request_obj_api",methods=["GET"],endpoint=test_app_request_obj_api,summary="Request对象属性接口",description="Request对象属性接口...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_response_obj_api",methods=["GET"],endpoint=test_app_response_obj_api,summary="Response对象属性接口",description="Response对象属性接口...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_back_task_api",methods=["GET"],endpoint=test_app_back_task_api,summary="添加后台任务接口",description="添加后台任务接口...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_upload_load_file",methods=["POST"],endpoint=test_app_upload_load_file,summary="上传File文件",description="上传File文件...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_self_exception_response_api",methods=["GET"],endpoint=test_app_self_exception_response_api,summary="自定义错误返回",description="自定义错误返回...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_red_url_api",methods=["GET"],endpoint=test_app_red_url_api,summary="跳转url",description="跳转url...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_return_bytes_response_api",methods=["GET"],endpoint=test_app_return_bytes_response_api,summary="流响应",description="流响应...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_return_bytes_file_api",methods=["GET"],endpoint=test_app_return_bytes_file_api,summary="响应文件",description="响应文件...",tags=["FastApi小技巧"])
test_app.add_api_route(path="/test_app_http_basic_cre_api",methods=["GET"],endpoint=test_app_http_basic_cre_api,summary="浏览器登录校验",description="浏览器登录校验...",tags=["FastApi小技巧"])


test_app.add_api_route(path="/test_app_req_body_api",methods=["POST"],endpoint=test_app_req_body_api,summary="基本请求体接口",description="基本请求体接口...",tags=["请求体Body处理"])
test_app.add_api_route(path="/test_app_request_body_api",methods=["POST"],endpoint=test_app_request_body_api,summary="Request中body对象获取",description="Request中body对象获取...",tags=["请求体Body处理"])

test_app.add_api_route(path="/test_app_form_api",methods=["POST"],endpoint=test_app_form_api,summary="FormData参数接口",description="FormData参数接口...",tags=["FormData参数接口"])
test_app.add_api_route(path="/test_app_form_one_api",methods=["POST"],endpoint=test_app_form_one_api,summary="FormData单个参数接口",description="FormData单个参数接口...",tags=["FormData参数接口"])
test_app.add_api_route(path="/test_app_request_form_api",methods=["POST"],endpoint=test_app_request_form_api,summary="Request对象获取FormData参数接口",description="Request对象获取FormData参数接口...",tags=["FormData参数接口","FastApi小技巧"])




















