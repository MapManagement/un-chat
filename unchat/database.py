from unchat import secrets

import sqlalchemy as db
import bcrypt
import unchat.chat_message_pb2 as chat


class DBConnector:

    def __init__(self):
        self.cursor = db.create_engine(secrets.conn)

    def get_user_by_id(self, user_id: int):
        sql_statement = "SELECT * FROM Users WHERE user_id = %s"
        prepared_statements = (int(user_id),)
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        user = db_query.fetchone()
        return user

    def get_user_by_name(self, user_name: str):
        sql_statement = "SELECT * FROM Users WHERE user_name = %s"
        prepared_statements = (user_name,)
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        user = db_query.fetchone()
        return user

    def insert_user(self, user: chat.UserLogin) -> bool:
        sql_statement = "INSERT INTO Users (user_name, password) VALUES (%s, %s)"
        user_name = user.userName
        password = self.hash_password(user.password)
        # rest is default or set later on

        prepared_statements = (user_name, password)
        try:
            self.cursor.execute(sql_statement, prepared_statements)
            return True
        except Exception:
            return False

    def update_user(self, new_user: chat.User):
        sql_statement_insert = "UPDATE Users SET user_name = %s, status = %s, biography = %s, " \
                               "path_profile_picture = %s WHERE user_id = %s"

        user_id = new_user.userID
        user_name = new_user.userName
        user_status = new_user.status
        user_biography = new_user.biography
        user_picture = new_user.profilePictureDir

        prepared_statements_insert = (user_name, user_status, user_biography, user_picture, user_id)
        self.cursor.execute(sql_statement_insert, prepared_statements_insert)

        user = self.get_user_by_id(user_id)
        return user

    def get_password_by_user_id(self, user_id: int):
        sql_statement = "SELECT password FROM Users WHERE user_id = %s"
        prepared_statements = (int(user_id),)
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        password_list = db_query.fetchone()
        return password_list[0]

    def get_password_by_user_name(self, user_name: str):
        sql_statement = "SELECT password FROM Users WHERE user_name = %s"
        prepared_statements = (user_name,)
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        password_list = db_query.fetchone()
        if password_list is not None:
            return password_list[0]
        else:
            return None

    def hash_password(self, password: str):
        bytes_password = bytes(password, "utf-8")
        hashed_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
        return hashed_password

    def compare_passwords(self, given_password: str, user_name: str):
        password_by_user_name = self.get_password_by_user_name(user_name)
        if password_by_user_name is not None:
            hashed_user_password = bytes(self.get_password_by_user_name(user_name), "utf-8")
            bytes_given_password = bytes(given_password, "utf-8")

            is_password_equal = bcrypt.checkpw(bytes_given_password, hashed_user_password)
            return is_password_equal
        else:
            return False

    def get_chats_by_sender_id(self, sender_id: int):
        sql_statement = "SELECT * FROM Chats WHERE sender_id = %s"
        prepared_statements = (int(sender_id),)
        db_query = self.cursor.execute(sql_statement, prepared_statements)
        chats = db_query.fetchall()
        print(chats)
        return chats

    def insert_chat(self, message: chat.ChatMessage):
        sender_id = message.senderID
        recipient_id = message.recipientID
        message_text = message.messageText
        chat_history_table_name = f"History{sender_id}_{recipient_id}"

        # insert new chat into sender-recipient form
        sql_statement_chat = "INSERT INTO Chats (sender_id, recipient_id, chat_history_table) VALUES (%s, %s, %s)"
        prepared_statements_chat = (int(sender_id), int(recipient_id), chat_history_table_name)
        self.cursor.execute(sql_statement_chat, prepared_statements_chat)

        # insert new chat also into recipient-sender form
        sql_statement_chat = "INSERT INTO Chats (sender_id, recipient_id, chat_history_table) VALUES (%s, %s, %s)"
        prepared_statements_chat = (int(recipient_id), int(sender_id), chat_history_table_name)
        self.cursor.execute(sql_statement_chat, prepared_statements_chat)

        self.create_new_history_table(chat_history_table_name)
        sql_statement_history = f"INSERT INTO {chat_history_table_name} (sender_id, message_text) VALUES (%s, %s)"
        prepared_statements_history = (int(sender_id), message_text)
        self.cursor.execute(sql_statement_history, prepared_statements_history)

    def get_history_by_chat_id(self, chat_id: int):
        sql_statement_chat_name = "SELECT chat_history_table FROM Chats WHERE chat_id = %s"
        prepared_statements_chat_name = (int(chat_id),)
        db_query_chat_name = self.cursor.execute(sql_statement_chat_name, prepared_statements_chat_name)
        chat_name = db_query_chat_name.fetchone()[0]
        print(chat_name)

        sql_statement_history = "SELECT * FROM %s"
        prepared_statements_history = (chat_name,)
        db_query_history = self.cursor.execute(sql_statement_history, prepared_statements_history)
        history = db_query_history.fetchall()
        print(history)
        return history

    def insert_new_message(self, message: chat.ChatMessage):
        sender_id = message.senderID
        recipient_id = message.recipientID
        message_text = message.messageText
        if int(sender_id) < int(recipient_id):
            chat_history_table_name = f"History{sender_id}_{recipient_id}"
        else:
            chat_history_table_name = f"History{recipient_id}_{sender_id}"

        sql_statement_chat_name = "SELECT chat_history_table FROM Chats WHERE (sender_id = %s AND recipient_id = %s)" \
                                  "OR (sender_id = %s AND recipient_id = %s)"
        prepared_statements_chat_name = (int(sender_id), int(recipient_id), int(recipient_id), int(sender_id))
        db_query_chat_name = self.cursor.execute(sql_statement_chat_name, prepared_statements_chat_name)
        chat_name = db_query_chat_name.fetchone()

        if chat_name is None:
            self.insert_chat(message)

        sql_statement_insert_message = f"INSERT INTO {chat_history_table_name} (sender_id, message_text) " \
                                       "VALUES (%s, %s)"
        prepared_statements_insert_message = (int(sender_id), message_text)
        self.cursor.execute(sql_statement_insert_message, prepared_statements_insert_message)

    def create_new_history_table(self, table_name: str):
        sql_statement_history_table = "CREATE TABLE {} (" \
                                      "message_id MEDIUMINT NOT NULL PRIMARY KEY AUTO_INCREMENT," \
                                      "sender_id MEDIUMINT NOT NULL," \
                                      "message_text VARCHAR(511) NOT NULL," \
                                      "sent_datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP()," \
                                      "FOREIGN KEY (sender_id) REFERENCES Users(user_id)" \
                                      ")".format(table_name)
        self.cursor.execute(sql_statement_history_table)

    def get_known_users(self, user: chat.User):
        sql_statement_chats = "SELECT * FROM Chats WHERE sender_id = %s"
        prepared_statements_chats = (int(user.userID),)
        db_query_chats = self.cursor.execute(sql_statement_chats, prepared_statements_chats)
        known_chats = db_query_chats.fetchall()

        users = []
        sql_statement_users = "SELECT * FROM Users WHERE user_id = %s"
        for known_chat in known_chats:
            prepared_statements_users = (int(known_chat[2]),)
            db_query_user = self.cursor.execute(sql_statement_users, prepared_statements_users)
            known_user = db_query_user.fetchone()
            users.append(known_user)
        return users

    def get_old_message_by_user_id(self, user_chat: chat.Chat):
        sender_id = user_chat.senderID
        recipient_id = user_chat.recipientID

        if int(sender_id) < int(recipient_id):
            chat_history_table_name = f"History{sender_id}_{recipient_id}"
        else:
            chat_history_table_name = f"History{recipient_id}_{sender_id}"

        sql_statement = f"SELECT * FROM {chat_history_table_name}"
        db_query = self.cursor.execute(sql_statement)
        old_messages = db_query.fetchall()
        return old_messages
