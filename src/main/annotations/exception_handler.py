from src.main.exceptions.base.bad_request_exception import BadRequestException
from src.main.exceptions.base.base_exception import BaseCustomException
from src.main.exceptions.base.not_found_exception import NotFoundException
from src.main.response.response import APIResponse


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotFoundException as exception:
            return APIResponse.not_found_response(exception.message).to_json(), 404
        except BadRequestException as exception:
            return APIResponse.bad_request_response(exception.message).to_json(), 400
        except BaseCustomException as exception:
            return APIResponse.error_response(exception.message).to_json(), 500

    wrapper.__name__ = f"handled_{func.__name__}"
    return wrapper
