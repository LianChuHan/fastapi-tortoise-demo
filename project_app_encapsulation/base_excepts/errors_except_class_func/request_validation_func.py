from  fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import HTMLResponse
async  def create_html_text(image_path,err_info,err_body):
    html_text = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>哥们？？？？你参数错了你晓得不？？？？？。。。。。。</title>
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
                flex-direction: column; /* 垂直排列 */
                text-align: center; /* 将文本居中 */
                color: white; /* 设置文本颜色为白色 */
            }}
            h1 {{
                color: rgb(255, 128, 128); /* 标题颜色 */
                font-size: 2em; /* 标题字体大小 */
                margin-bottom: 20px; /* 标题与正文的间距 */
            }}
            h4 {{
                color: red; /* 详情标题颜色 */
            }}
            .content {{
                font-size: 1.2em; /* 正文字体大小 */
                max-width: 600px; /* 限制正文宽度 */
                margin-top: 20px; /* 正文与标题之间的间距 */
            }}
        </style>
    </head>
    <body>
        <h1>哥们？？？？你参数错了你晓得不？？？？？。。。。。。</h1>
        <div class="content">
            <h4>详情</h4>
            <div>{err_info}</div>
            <h4>数据</h4>
            <div>{err_body}</div>
        </div>
    </body>
    </html>
    """
    return html_text

async def request_validation_func(request:Request,ext:RequestValidationError):
    err_info=ext.errors()
    err_info=err_info if err_info else ""
    err_body=ext.body
    err_body=err_body if err_body else ""

    return HTMLResponse(
        status_code=422,
        content=await create_html_text(image_path=request.url_for("static",path='10.png'),err_info=err_info,err_body=err_body)
    )