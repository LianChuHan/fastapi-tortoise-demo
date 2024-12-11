

class ErrorsExceptClass(Exception):
    def __init__(self,status_code,message="操作有误"):
        self.status_code = status_code
        self.message = message

