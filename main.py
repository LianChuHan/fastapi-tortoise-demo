import asyncio
from create_base_app import create_app



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(create_app())
        print("启动Fast-API服务")
    except Exception as err:
        print(err)
        print("停止服务")
    finally:
        loop.close()

