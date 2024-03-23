from src.main.exceptions.base.base_exception import BaseCustomException


class NotFoundException(BaseCustomException):
    def __init__(self, message: str = "not.found"):
        self.message = message
        super().__init__(message)
