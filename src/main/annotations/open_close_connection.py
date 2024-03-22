from functools import wraps

from src.main.configs.database_config import database_connect, close_connection


def open_close_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        connection, cursor = database_connect()
        result = func(connection, cursor, *args, **kwargs)
        close_connection(connection, cursor)
        return result

    return wrapper
