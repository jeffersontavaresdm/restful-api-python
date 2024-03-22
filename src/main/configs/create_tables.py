from queries.user_queries import create_user_table_query
from src.main.annotations.open_close_connection import open_close_connection


@open_close_connection
def create_user_table(connection, cursor):
    try:
        cursor.execute(create_user_table_query)
        connection.commit()
    except Exception as exception:
        print(exception)
