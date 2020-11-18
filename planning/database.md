# MySQL Database
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
| UserID                  | VARCHAR(16)  | Yes         | Yes      | No       |
| UserName                | VARCHAR(32)  | No          | Yes      | No       |
| Password                | VARCHAR(64)  | No          | Yes      | No       |
| CreatedAt               | DATETIME     | No          | Yes      | Yes      |
| Status                  | VARCHAR(20)  | No          | No       | Yes      |
| Biography               | VARCHAR(128) | No          | No       | No       |
| PathProfilePicture      | VARCHAR(256) | No          | Yes      | Yes      |

*Default means following values:  
- CreatedAt: Datetime when clicking on submit button
- Status: Something like "Using UnChat"
- PathProfilePicture: Path to default profile picture
