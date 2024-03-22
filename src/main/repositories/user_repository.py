from src.resource.queries.user_queries import get_users_query, delete_user_query, update_user_query, check_user_query
from src.resource.queries.user_queries import insert_user_query
from src.main.annotations.open_close_connection import open_close_connection
from src.main.exceptions.user_not_found_exception import UserNotFoundException
from src.main.models.user import User, UserPayload


@open_close_connection
def create_user(connection, cursor, name, email):
    try:
        cursor.execute(insert_user_query, (name, email))
        connection.commit()
    except Exception as exception:
        print(exception)
        UserNotFoundException()


@open_close_connection
def get_users(_, cursor):
    cursor.execute(get_users_query)

    users = [User(*row) for row in cursor.fetchall()]

    return users


@open_close_connection
def update_user(connection, cursor, payload: UserPayload, user_id):
    try:
        cursor.execute(check_user_query, (user_id,))
        user_exists = cursor.fetchone()

        if user_exists:
            cursor.execute(update_user_query, (payload.name, payload.email, user_id))
            connection.commit()
        else:
            raise UserNotFoundException(f"User with id {user_id} was not found")
    except Exception as exception:
        print(exception)
        raise Exception("An error occurred when trying to update the user")


@open_close_connection
def delete_user(connection, cursor, user_id):
    try:
        cursor.execute(check_user_query, (user_id,))
        user_exists = cursor.fetchone()

        if user_exists:
            cursor.execute(delete_user_query, (user_id,))
            connection.commit()
        else:
            raise UserNotFoundException(f"User with id {user_id} was not found")
    except Exception as exception:
        print(exception)
        raise Exception("An error occurred when trying to delete the user")
