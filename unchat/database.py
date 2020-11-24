import pymysql.cursors
import bcrypt
import unchat.chat_message_pb2 as chat


class DBConnector:

    def __init__(self):
        self.connection = pymysql.connect(host="abc", user="abc", password="abc", db="Users", charset="utf8mb4")
        self.cursor = self.connection.cursor()

    def get_user_by_id(self, user_id: str):
        sql_statement = "SELECT * FROM Users WHERE user_id = %(id)"
        prepared_statements = {"id": user_id}
        self.cursor().execute(sql_statement, prepared_statements)
        user_list = self.cursor.fetchone()
        return user_list[0]

    def get_user_by_name(self, user_name: str):
        sql_statement = "SELECT * FROM Users WHERE user_name = %(name)"
        prepared_statements = {"name": user_name}
        self.cursor().execute(sql_statement, prepared_statements)
        user_list = self.cursor.fetchone()
        return user_list[0]

    def insert_user(self, user: chat.UserLogin) -> bool:
        sql_statement = "INSERT INTO Users" \
                        "(user_id, user_name, password)" \
                        "VALUES" \
                        "(%(id), %(name), %(password))"
        # user_id
        user_name = user.username
        password = self.hash_password(user.password)
        # rest is default or set later on

        prepared_statements = {"id": "user_id", "name": user_name, "password": password}
        try:
            self.cursor().execute(sql_statement, prepared_statements)
            return True
        except Exception:
            return False

    def get_password_by_user_id(self, user_id: str):
        sql_statement = "SELECT password FROM Users WHERE user_id = %(id)"
        prepared_statements = {"id": user_id}
        self.cursor().execute(sql_statement, prepared_statements)
        password_list = self.cursor.fetchone()
        return password_list[0]

    def get_password_by_user_name(self, user_name: str):
        sql_statement = "SELECT password FROM Users WHERE user_name = %(name)"
        prepared_statements = {"name": user_name}
        self.cursor().execute(sql_statement, prepared_statements)
        password_list = self.cursor.fetchone()
        return password_list[0]

    def hash_password(self, password: str):
        bytes_password = bytes(password, "utf-8")
        hashed_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
        return hashed_password

    def compare_passwords(self, given_password: str, user_name: str):
        hashed_user_password = self.get_password_by_user_name(user_name)
        bytes_given_password = bytes(given_password, "utf-8")

        is_password_equal = bcrypt.checkpw(bytes_given_password, hashed_user_password)
        return is_password_equal
