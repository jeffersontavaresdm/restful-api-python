from typing import List

from src.main.annotations.open_close_connection import open_close_connection
from src.main.exceptions.user_not_found_exception import UserNotFoundException
from src.main.models.user import User, UserPayload
from src.resource.queries.user_queries import get_users_query, delete_user_query, update_user_query, check_user_query, \
    get_user_by_id_query, get_user_by_name_query
from src.resource.queries.user_queries import insert_user_query


@open_close_connection
def create_user(connection, cursor, name, email):
    cursor.execute(insert_user_query, (name, email))
    connection.commit()


@open_close_connection
def get_users(_, cursor) -> List[User]:
    cursor.execute(get_users_query)
    users = [User(*row) for row in cursor.fetchall()]
    return users


@open_close_connection
def update_user(connection, cursor, payload: UserPayload, user_id):
    cursor.execute(check_user_query, (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute(update_user_query, (payload.name, payload.email, user_id))
        connection.commit()
    else:
        raise UserNotFoundException(f"User with id {user_id} was not found")


@open_close_connection
def delete_user(connection, cursor, user_id):
    cursor.execute(check_user_query, (user_id,))
    user_exists = cursor.fetchone()

    if user_exists:
        cursor.execute(delete_user_query, (user_id,))
        connection.commit()
    else:
        raise UserNotFoundException(f"User with id {user_id} was not found")


@open_close_connection
def get_user_by_id(_, cursor, user_id) -> User:
    cursor.execute(get_user_by_id_query, (user_id,))
    users = User(*cursor.fetchone())
    return users


@open_close_connection
def get_user_by_name(_, cursor, user_name) -> User:
    cursor.execute(get_user_by_name_query, (user_name,))
    users = User(*cursor.fetchone())
    return users
