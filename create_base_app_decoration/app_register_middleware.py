from middleware.api_middleware import ApiBaseMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware


async def app_register_middleware(app):
    app.add_middleware(middleware_class=ApiBaseMiddleware, assigned_number=1)
    # 请求中必须包含 Host 字段，为防止 HTTP 主机报头攻击，并且添加中间件的时候，还可以指定一个 allowed_hosts，那么它是干什么的呢？
    # 假设我们有服务 a.example.com, b.example.com, c.example.com
    # 但我们不希望用户访问 c.example.com，就可以像下面这么设置，如果指定为 ["*"]，或者不指定 allow_hosts，则表示无限制
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])
    # 如果用户的请求头的 Accept-Encoding 字段包含 gzip，那么 FastAPI 会使用 GZip 算法压缩
    # minimum_size=1000 表示当大小不超过 1000 字节的时候就不压缩了
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(
        CORSMiddleware,
        # 允许跨域的源列表，例如 ["http://www.example.org"] 等等，["*"] 表示允许任何源
        allow_origins=["*"],
        # 跨域请求是否支持 cookie，默认是 False，如果为 True，allow_origins 必须为具体的源，不可以是 ["*"]
        allow_credentials=False,
        # 允许跨域请求的 HTTP 方法列表，默认是 ["GET"]
        allow_methods=["*"],
        # 允许跨域请求的 HTTP 请求头列表，默认是 []，可以使用 ["*"] 表示允许所有的请求头
        # 当然 Accept、Accept-Language、Content-Language 以及 Content-Type 总之被允许的
        allow_headers=["*"],
        # 可以被浏览器访问的响应头, 默认是 []，一般很少指定
        # expose_headers=["*"]
        # 设定浏览器缓存 CORS 响应的最长时间，单位是秒。默认为 600，一般也很少指定
        # max_age=1000
    )
