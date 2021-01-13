from unchat import secrets

import sqlalchemy as db


# you have to define the connector for your own database
cursor = db.create_engine(secrets.conn)


def main():
    create_users_table()
    create_chats_table()
    create_histories_table()
    print("Finished!")
    input("Press Enter to close this window...")


def create_users_table():
    sql_statement = "CREATE TABLE Users (" \
                    "user_id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "user_name VARCHAR(32) NOT NULL," \
                    "password VARCHAR(255) NOT NULL," \
                    "created_at DATETIME NOT NULL," \
                    "status VARCHAR(32) DEFAULT 'Using UnChat'," \
                    "biography VARCHAR(128)," \
                    "path_profile_picture VARCHAR(256) NOT NULL DEFAULT 'UnChat.png'," \
                    "is_online TINYINT(1) NOT NULL," \
                    "PRIMARY KEY (user_id)," \
                    "UNIQUE (user_name)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created Users table successfully!")


# only a blueprint since history tables are created automatically
def create_chats_table():
    sql_statement = "CREATE TABLE Chats (" \
                    "chat_id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "sender_id MEDIUMINT(9) NOT NULL," \
                    "recipient_id MEDIUMINT(9) NOT NULL," \
                    "last_message_datetime DATETIME NOT NULL," \
                    "chat_history_table VARCHAR(127) NOT NULL," \
                    "PRIMARY KEY (chat_id)," \
                    "FOREIGN KEY (sender_id) REFERENCES Users(user_id)," \
                    "FOREIGN KEY (recipient_id) REFERENCES Users(user_id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created Chats table successfully!")


def create_histories_table():
    sql_statement = "CREATE TABLE ChatHistories (" \
                    "message_id MEDIUMINT(9) NOT NULL AUTO_INCREMENT," \
                    "sender_id MEDIUMINT(9) NOT NULL," \
                    "message_text VARCHAR(511) NOT NULL," \
                    "sent_datetime DATETIME NOT NULL," \
                    "PRIMARY KEY (message_id)," \
                    "FOREIGN KEY (sender_id) REFERENCES Users(user_id)" \
                    ")"
    cursor.execute(sql_statement)
    print("Created ChatHistories table (blueprint) successfully!")


if __name__ == '__main__':
    main()
