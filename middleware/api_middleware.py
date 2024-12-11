from fastapi.requests import Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware


class ApiBaseMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, assigned_number):
        super().__init__(app)
        self.assigned_number = assigned_number

    async def dispatch(self,request: Request, call_next):
        print("请求中间件执行.......")
        response: Response = await call_next(request)
        return response
