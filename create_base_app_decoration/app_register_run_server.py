from uvicorn.config import Config
from uvicorn.server import Server


async def app_register_run_server(app):
    config = Config(app, host="0", port=8080, reload=True, workers=4)
    server = Server(config)
    await server.serve()
