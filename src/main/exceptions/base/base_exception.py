class BaseCustomException(Exception):
    message: str

    def __init__(self, message: str = "not.found"):
        self.message = message
        super().__init__(self, message)
