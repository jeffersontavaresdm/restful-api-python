from queries.user_queries import get_users_query
from queries.user_queries import insert_user_query
from src.main.annotations.open_close_connection import open_close_connection
from src.main.models.user import User


@open_close_connection
def insert_user(connection, cursor, name, email):
    cursor.execute(insert_user_query, (name, email))
    connection.commit()


@open_close_connection
def get_users(_, cursor):
    cursor.execute(get_users_query)

    users = [User(*row) for row in cursor.fetchall()]

    return users
