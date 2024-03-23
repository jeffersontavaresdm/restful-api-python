from src.main.annotations.exception_handler import exception_handler
from src.resource.queries.user_queries import create_user_table_query
from src.main.annotations.open_close_connection import open_close_connection


@open_close_connection
@exception_handler
def create_user_table(connection, cursor):
    cursor.execute(create_user_table_query)
    connection.commit()
