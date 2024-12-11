from  fastapi import Request
from fastapi.exceptions import StarletteHTTPException
from fastapi.responses import HTMLResponse


async  def create_html_text(image_path):
    html_text = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>您的页面去火星了。。。。。</title>
        <style>
            body {{
                background-image: url('{image_path}'); /* 替换为你的图片路径 */
                background-size: contain; /* 确保整个图片都能显示 */
                background-repeat: no-repeat; /* 防止背景图片重复 */
                background-position: center center; /* 背景图片居中 */
                height: 100vh; /* 设置页面高度为视口高度 */
                margin: 0; /* 去除默认外边距 */
                display: flex; /* 使用Flexbox布局 */
                justify-content: center; /* 水平居中 */
                align-items: center; /* 垂直居中 */
            }}
            h1 {{
                text-align: center; /* 居中文本 */
                color: pink; /* 文本颜色 */
                font-size: 2em; /* 可选：调整字体大小 */
                margin: 0; /* 去除默认外边距 */
                padding: 20px; /* 可选：添加内边距 */
                background: rgba(0, 0, 0, 0.5); /* 可选：添加半透明背景以提高可读性 */
                border-radius: 10px; /* 可选：添加圆角 */
            }}
            .background-example {{
                display: none; /* 隐藏不必要的div */
            }}
        </style>
    </head>
    <body>
        <h1>您的页面去火星了。。。。。。</h1>
        <div class="background-example"></div>
    </body>
    </html>
    """

    return html_text

async def not_found_err_func(request:Request,ext:StarletteHTTPException):
    resource=HTMLResponse(
        content=await  create_html_text(image_path=request.url_for("static",path='404.gif'))
    )
    return resource


