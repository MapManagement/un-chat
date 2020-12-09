from concurrent import futures
from unchat import database
from google.protobuf.timestamp_pb2 import Timestamp

import grpc
import datetime
import time

import unchat.chat_message_pb2_grpc as rpc
import unchat.chat_message_pb2 as chat


class ChatServer(rpc.ChatMessagesServicer):

    def __init__(self):
        self.chats = []
        self.db_connection = database.DBConnector()

    def SendMessage(self, request, context):
        print(f"Incoming Message {request} \n")
        self.chats.append(request)
        self.db_connection.insert_new_message(request)
        return chat.RequestSuccess(receivedRequest=True)

    def ChatStream(self, request, context):
        last_index = 0
        while True:
            while len(self.chats) > last_index:
                print(self.chats)
                message = self.chats[last_index]
                last_index += 1
                print(f"M: {message}")
                print(f"R: {request}")
                if message.recipientID == request.userID or message.senderID == request.userID:
                    yield message

    def SendUserInformation(self, request, context):
        print(f"New Login: {request}\n")
        try:
            database_user = self.db_connection.get_user_by_name(request.userName)
            if request.isUserUpdate:
                database_user = self.db_connection.update_user(request)
            timestamp_object = Timestamp(seconds=int(database_user[3].timestamp()))
            proto_user_information = chat.User(
                userID=str(database_user[0]),
                userName=database_user[1],
                signUpDate=timestamp_object,
                status=database_user[4],
                biography=database_user[5],
                profilePictureDir=database_user[6]
            )
            return proto_user_information
        except Exception as ex:
            print(ex)
            return chat.User()

    def CheckUserLogin(self, request, context):
        print(f"CheckLogin: {context.peer()}")
        user_password = str(request.password)

        passwords_equal = self.db_connection.compare_passwords(user_password, request.userName)
        return chat.RequestSuccess(receivedRequest=passwords_equal)

    def SendUserRegistration(self, request, context):
        print(f"New Registration: {request}\n")
        user_password = str(request.password)
        user_name = str(request.userName)
        user = chat.UserLogin(userName=user_name, password=user_password)
        success = self.db_connection.insert_user(user)
        return chat.RequestSuccess(receivedRequest=success)

    def GetKnownUsers(self, request, context):
        users = chat.UserArray()
        tuple_users = self.db_connection.get_known_users(request)
        for user in tuple_users:
            timestamp_object = Timestamp(seconds=int(user[3].timestamp()))
            new_user = chat.User(
                userID=str(user[0]),
                userName=user[1],
                signUpDate=timestamp_object,
                status=user[4],
                biography=user[5],
                profilePictureDir="pack://application:,,,/client-application/Resources/default_profile_picture.png"
            )
            users.user.append(new_user)
        return users

    def LoadOldMessages(self, request, context):
        messages = self.db_connection.get_old_messages_by_user_id(request)
        i = 0
        for message in messages:
            user_name = self.db_connection.get_user_by_id(message[1])[1]
            timestamp_object = Timestamp(seconds=int(message[3].timestamp()))
            chat_message = chat.ChatMessage(
                senderID=str(message[1]),

                messageText=message[2],
                userName=user_name,
                sentAt=timestamp_object
            )
            yield chat_message

            if i == len(messages)-1 or len(messages) == 0:
                if context.is_active():
                    context.cancel()
                    return
            i += 1


def get_server_credentials():
    with open("../server-key.pem", "rb") as file_key:
        private_key = file_key.read()
    with open("../server.pem", "rb") as file_cert:
        certificate = file_cert.read()
    credentials = grpc.ssl_server_credentials(((private_key, certificate),))
    return credentials


if __name__ == "__main__":
    print("Starting chat server...\n")
    port = 32002
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    rpc.add_ChatMessagesServicer_to_server(ChatServer(), server)
    server.add_secure_port(f'0.0.0.0:{port}', get_server_credentials())
    # server.add_insecure_port(f'0.0.0.0:{port}')
    server.start()
    server.wait_for_termination()
