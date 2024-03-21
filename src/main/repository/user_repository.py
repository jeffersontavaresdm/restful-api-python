from queries.get_users_query import get_users_query
from src.main.configs.database_config import database_connect, close_connection
from src.main.models.user import User


def create(body):
    pass


def get_users():
    connection, cursor = database_connect()

    cursor.execute(get_users_query)

    users = [User(*row) for row in cursor.fetchall()]

    close_connection(connection, cursor)

    return users
