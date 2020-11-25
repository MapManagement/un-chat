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

    def SendMessage(self, request, context):
        print(f"Incoming Message {request} \n")
        print(context.peer_identity_key())
        self.chats.append(request)
        return chat.RequestSuccess

    def ChatStream(self, request, context):
        last_index = 0
        while True:
            while len(self.chats) > last_index:
                message = self.chats[last_index]
                last_index += 1
                print(type(message))
                print(message)
                if message.recipientID == request.userID:
                    yield message

    def SendUserInformation(self, request, context):
        print(f"New Login: {request}\n")
        db_connection = database.DBConnector()
        try:
            database_user = db_connection.get_user_by_name(request.userName)
            timestamp_object = Timestamp(seconds=int(database_user[3].timestamp()))
            proto_user_information = chat.UserInformation(
                userID=str(database_user[0]),
                signUpDate=timestamp_object,
                status=database_user[4],
                biography=database_user[5],
                profilePictureDir=database_user[6]
            )
            return proto_user_information
        except Exception as ex:
            print(ex)
            return chat.UserInformation()

    def CheckUserLogin(self, request, context):
        db_connection = database.DBConnector()
        user_password = str(request.password)

        passwords_equal = db_connection.compare_passwords(user_password, request.userName)
        return chat.RequestSuccess(receivedRequest=passwords_equal)

    def SendUserRegistration(self, request, context):
        print(f"New Registration: {request}\n")
        db_connection = database.DBConnector()
        user_password = str(request.password)
        user_name = str(request.userName)
        user = chat.UserLogin(userName=user_name, password=user_password)
        success = db_connection.insert_user(user)
        return chat.RequestSuccess(receivedRequest=success)


if __name__ == "__main__":
    print("Starting chat server...\n")
    port = 32002
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    rpc.add_ChatMessagesServicer_to_server(ChatServer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()
