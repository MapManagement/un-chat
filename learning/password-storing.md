# Storing Passwords
## User Database
As you should already know, my server also hosts a MySQL database which stores all registered users and
chat histories. Talking about registered users, all of them need a password for their account so nobody but
they can authenticate as the profile they created. For that reason besides saving general information like
a user name or a profile picture I also have to store the corresponding password. In terms of security it is
common sense to encrypt these with so called **hashing functions** for cryptography. That is the way I chose too
and this section explains what, how and why I did the things I did for UnChat.

## Saving Process
I wanted to show what happens in the code behind when a new user decides to register himself/herself.
Following steps describe the different processes on a client and the server:
1. user enters name and password, submits credentials
2. credentials will be sent to server (how is not defined yet)
3. server receives credentials  
    1. creates new user out of it and saves it in database  
    2. password is hashed + salted and eventually saved in database  
    3. server acknowledges new registered user via sending response  
4. user has to login with newly created profile credentials
5. credentials will be sent to server
6. password is hashed and salted
7. server checks whether entered password matches entered user name
8. server sends response and user is logged in

## Hashing Passwords
As soon as the user submits his/her credentials and the server received them, the password will be hashed.
But what does "hash" even mean? The entered password is put into a so called **"hashing function"**. This
function turns the given password into a character string of a set amount of characters. A hashing function
is not always a cryptographic one, it is originated in mathematics.  As of today there are several hashing
functions especially for the cryptography like MD5, SHA1, SH256 or bcrypt. Cryptographic hashing functions
have to fulfill following conditions:
- Definiteness: the same character string has to result in the same hash-value
- Reversibility: the resulting hash-value should not be reversible meaning that the character string leads
to a hash-value but the has value does not lead to the original character string
- Collision: different character strings should not result in the same hash-value  

The last point is one of the weaknesses of older hashing algorithms since they turned a arbitrary long
character string into a hash-value of a set length. Newer ones instead  extend their length whenever the
given string is longer too, e.g. SHA256.  
You do hash passwords because of the risk of data breaches. Even if somebody has access to thousands of
user profiles and their passwords, the person does not know the plaintext password. Only the hash-value
of it is breached and can be stolen.

## Salting Passwords
It is known that most humans tend to use simple and the same passwords across multiple platforms. Even
hashing function cannot do anything about it they simply just convert the given password in a hash-value.
Same passwords lead to the same hash-values or you could not login yourself anymore after registering. So
how could you increase the security without any disadvantages? **Password salting** is the solution but
how does it work and what is it? After hashing your entered password a so called **"password salt"** is
added to the resulting hash-value. A password salt is a random bit of data and increases the security
by a lot since same passwords will not lead to same hash-values as long as each registered user has its
own salt. Attacking methods like **dictionary attacks** or **rainbow tables** lose their effectiveness
if you do so. More about it in the [weaknesses](##Weaknesses) chapter.

## Weaknesses
### Brute Force
One of the methods which will probably work forever if you want to crack passwords, is brute force. You just
try every possibility until you found the right value. The better modern machines get, the faster they are
able to find the right password but scalable methods of encrypting passwords do already exist. They can be
adjusted to the performance newer machines have. The golden rule remains, longer passwords are harder to crack.
### Dictionary Attacks
Nowadays, there are tables which contain common passwords or character combinations. Most often they are
extended whenever any site is a victim of a **data breach**. Large amounts of data stored within a database
is stolen or publicly available and then added to existing tables. It removes the randomness of brute force
to a certain extent. You can now minimize the number of passwords you want to try and the possibility of
cracking a password rises immediately. That is why salting is important, adds a kind of randomness even to
weak and common passwords.
### Rainbow Tables
Rainbow tables are a extended version of dictionary attacks so to say. They do not only contain common
passwords, they also contain their corresponding hash-value. Salting decreases the chance of getting attacked
by this method too.
