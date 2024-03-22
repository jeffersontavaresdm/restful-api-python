class UserNotFoundException(Exception):

    def __init__(self, message: str = "user.not.found"):
        super().__init__(self, message)
