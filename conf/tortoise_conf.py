import os

from project_sys_path import MODELS_DIR, DIR_PATH
from pathlib import Path

separator = os.sep


def get_model_path_lis():
    models_path_lis = []
    all_mode_file = os.listdir(MODELS_DIR)
    abs_path_lis = MODELS_DIR.split(DIR_PATH)
    abs_path_st = abs_path_lis[1].replace(separator, ".")
    if abs_path_st.startswith("."):
        abs_path_st = abs_path_st[1:]
    for file_name in all_mode_file:
        file_name_lis = file_name.split(".")
        new_file_name = file_name_lis[0]
        print(new_file_name)
        if new_file_name in ["__init___","__pycache__"]:
            continue
        models_path_lis.append(abs_path_st + "." + new_file_name)
    return models_path_lis

MODELS_PATH_LIS=get_model_path_lis()
print(MODELS_PATH_LIS)
DATABASE_CONFIG = {
    "connections": {
        "default": "mysql://root:123456@127.0.0.1:3306/fast_api_db",  # 替换为你的数据库连接字符串
    },
    "apps": {
        "models": {
            "models": MODELS_PATH_LIS,  # 你的模型所在的模块
            "default_connection": "default",
        }
    },
}
