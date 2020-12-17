# MySQL Database
## "Users" Table
A user registration system needs a database for sure and so I thought about why not using
MySQL further on because of using it already every time I have worked with databases. It
contains every registered user and runs on the Raspberry Pi as well. Once a user opens up
the client program on his machine and he/she is connected to the same network the Raspberry
Pi is connected to, he has to login himself/herself. If he/she has no account yet, he/she
can easily create one just by providing a user name and a mail address. Everything else will
be done by the server instance and the provided data added to the database. Further logins
are now able as long as the user still knows the password and his user name.  
Following table shows the database structure:

| Column Name             | Data Type    | Key | Not Null | Default* | Unique |
|:-----------------------:|:------------:|:---:|:--------:|:--------:|:------:|
| user_id                 | MEDIUMINT    | PK  | Yes      | No       | Yes    |
| user_name               | VARCHAR(32)  |     | Yes      | No       | Yes    |
| password                | VARCHAR(64)  |     | Yes      | No       | No     |
| created_at              | DATETIME     |     | Yes      | No       | No     |
| status                  | VARCHAR(32)  |     | No       | Yes      | No     |
| biography               | VARCHAR(128) |     | No       | No       | No     |
| path_profile_picture    | VARCHAR(256) |     | Yes      | Yes      | No     |

*Default means following values:  
- Status: Something like "Using UnChat"
- PathProfilePicture: Path to default profile picture

## "Chats" Table
One user is able wo write with several different users and therefore I want to save the
chat history and also the already "started" chats within my database. Saving it in the
``Users`` table is not the best idea if I want to keep it simple and not that complex,
so I created another table and named it ``Chats``. It only contains the ``sender_id``, the
``recipient_id`` and the datetime of the last message, respectively ``last_message_datetime``.
The whole chat also receives a ``chat_id``.

| Column Name           | Data Type     | Key | Not Null | Default* |
|:---------------------:|:-------------:|:---:|:--------:|:--------:|
| chat_id               | MEDIUMINT     | PK  | Yes      | Yes      |
| sender_id             | MEDIUMINT     | FK  | Yes      | No       |
| recipient_id          | MEDIUMINT     | FK  | Yes      | No       |
| last_message_datetime | DATETIME      |     | Yes      | No       |
| chat_history_table    | VARCHAR(127)  |     | Yes      | No       |

## "ChatHistories" Table
To keep it even simpler, I decided to create another table: ``ChatHistories``. In contrast
to the other two tables, this one is only a blueprint and as soon as somebody starts a new
chat, a new table will be created for the concerned users. Everytime a user sends a message,
it will be stored within this newly created table. Of course, I will work on a proper
encryption to increase the security. Probably, the table will look like this:

 Column Name    | Data Type    | Key | Not Null | Default* |
|:-------------:|:------------:|:---:|:--------:|:--------:|
| message_id    | MEDIUMINT    | PK  | Yes      | Yes      |
| sender_id     | MEDIUMINT    | FK  | Yes      | No       |
| message_text  | VARCHAR(511) | No  | Yes      | No       |
| sent_datetime | DATETIME     | No  | Yes      | No       |