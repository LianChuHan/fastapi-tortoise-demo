import os, sys

DIR_PATH = os.path.dirname(os.path.realpath(__file__))

TEMPLATE_DIR = os.path.join(DIR_PATH, 'template')
DB_MODELS_DIR = os.path.join(DIR_PATH, 'db_models')
MODELS_DIR = os.path.join(DB_MODELS_DIR, 'models')
STATIC_DIR = os.path.join(TEMPLATE_DIR, 'static')


async def project_sys_path_func():
    sys.path.insert(0, DIR_PATH)
