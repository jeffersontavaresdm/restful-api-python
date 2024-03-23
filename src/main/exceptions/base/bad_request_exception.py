from src.main.exceptions.base.base_exception import BaseCustomException


class BadRequestException(BaseCustomException):
    def __init__(self, message: str = "bad.request"):
        super().__init__(message)
