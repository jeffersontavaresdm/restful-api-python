from src.main.exceptions.base.not_found_exception import NotFoundException


class UserNotFoundException(NotFoundException):
    def __init__(self, message: str = "user.not.found"):
        self.message = message
        super().__init__(message)
