create_user_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)
);
"""

get_users_query = "SELECT id, name, email FROM users"

insert_user_query = "INSERT INTO users (name, email) VALUES (%s, %s)"

check_user_query = "SELECT id FROM users WHERE id = %s"

update_user_query = "UPDATE users SET name = %s, email = %s WHERE id = %s"

delete_user_query = "DELETE FROM users WHERE id = %s"
