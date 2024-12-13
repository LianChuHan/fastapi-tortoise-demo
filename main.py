import asyncio
from create_base_app import create_app
import uvloop


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_running_loop()
    try:
        loop.run_until_complete(create_app())
        print("启动Fast-API服务")
    except Exception as err:
        print(err)
        print("停止服务")
    finally:
        loop.close()

