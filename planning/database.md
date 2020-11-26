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

| Column Name             | Data Type    | Primary Key | Not Null | Default* |
|:-----------------------:|:------------:|:-----------:|:--------:|:--------:|
| user_id                 | MEDIUMINT  | Yes         | Yes      | No       |
| user_name               | VARCHAR(32)  | No          | Yes      | No       |
| password                | VARCHAR(64)  | No          | Yes      | No       |
| created_at              | DATETIME     | No          | Yes      | Yes      |
| status                  | VARCHAR(32)  | No          | No       | Yes      |
| biography               | VARCHAR(128) | No          | No       | No       |
| path_profile_picture    | VARCHAR(256) | No          | Yes      | Yes      |

*Default means following values:  
- CreatedAt: Datetime when clicking on submit button
- Status: Something like "Using UnChat"
- PathProfilePicture: Path to default profile picture

## "Chats" Table
One user is able wo write with several different users and therefore I want to save the
chat history and also the already "started" chats within my database. Saving it in the
``Users`` table is not the best idea if I want to keep it simple and not that complex,
so I created another table and named it ``Chats``. It only contains the ``sender_id``, the
``recipient_id`` and the datetime of the last message, respectively ``last_message_datetime``.
The whole chat also receives a ``chat_id``.

| Column Name           | Data Type     | Primary Key | Not Null | Default* |
|:---------------------:|:-------------:|:-----------:|:--------:|:--------:|
| chat_id               | MEDIUMINT     | Yes         | Yes      | Yes      |
| sender_id             | MEDIUMINT     | No          | Yes      | No       |
| recipient_id          | MEDIUMINT     | No          | Yes      | No       |
| last_message_datetime | DATETIME      | No          | Yes      | Yes      |
| chat_history_table    | VARCHAR(127)  | No          | Yes      | No       |

## "ChatHistories" Table
To keep it even simpler, I decided to create another table: ``ChatHistories``. In contrast
to the other two tables, this one is only a blueprint and as soon as somebody starts a new
chat, a new table will be created for the concerned users. Everytime a user sends a message,
it will be stored within this newly created table. Of course, I will work on a proper
encryption to increase the security. Probably, the table will look like this:

 Column Name    | Data Type    | Primary Key | Not Null | Default* |
|:-------------:|:------------:|:-----------:|:--------:|:--------:|
| message_id    | MEDIUMINT    | Yes         | Yes      | Yes      |
| sender_id     | MEDIUMINT    | No          | Yes      | No       |
| message_text  | VARCHAR(511) | No          | Yes      | No       |
| sent_datetime | DATETIME     | No          | Yes      | Yes      |