from unchat import secrets

import sqlalchemy as db
import bcrypt
import unchat.chat_message_pb2 as chat


class DBConnector:

    def __init__(self):
        self.cursor = db.create_engine(secrets.conn)

    def get_user_by_id(self, user_id: str):
        sql_statement = "SELECT * FROM Users WHERE user_id = %s"
        prepared_statements = (user_id,)
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        user = db_query.fetchone()
        return user

    def get_user_by_name(self, user_name: str):
        sql_statement = "SELECT * FROM Users WHERE user_name = %(name)s"
        prepared_statements = {"name": user_name}
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        user = db_query.fetchone()
        return user

    def insert_user(self, user: chat.UserLogin) -> bool:
        sql_statement = "INSERT INTO Users (user_id, user_name, password) VALUES (%s, %s, %s)"
        # user_id
        user_name = user.userName
        password = self.hash_password(user.password)
        # rest is default or set later on

        prepared_statements = ("user_id", user_name, password)
        try:
            test = self.cursor.execute(sql_statement, prepared_statements)
            print(test)
            return True
        except Exception:
            return False

    def get_password_by_user_id(self, user_id: str):
        sql_statement = "SELECT password FROM Users WHERE user_id = %s"
        prepared_statements = (user_id,)
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        password_list = db_query.fetchone()
        return password_list[0]

    def get_password_by_user_name(self, user_name: str):
        sql_statement = "SELECT password FROM Users WHERE user_name = %s"
        prepared_statements = (user_name,)
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        password_list = db_query.fetchone()
        return password_list[0]

    def hash_password(self, password: str):
        bytes_password = bytes(password, "utf-8")
        hashed_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
        return hashed_password

    def compare_passwords(self, given_password: str, user_name: str):
        hashed_user_password = bytes(self.get_password_by_user_name(user_name), "utf-8")
        bytes_given_password = bytes(given_password, "utf-8")

        is_password_equal = bcrypt.checkpw(bytes_given_password, hashed_user_password)
        return is_password_equal
