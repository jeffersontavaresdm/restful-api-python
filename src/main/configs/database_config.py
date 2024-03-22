import psycopg2


def database_connect() -> tuple:
    connection = psycopg2.connect(
        dbname="testdb",
        user="testdb",
        password="testdb",
        host="localhost",
        port="5432"
    )

    cursor = connection.cursor()

    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()
