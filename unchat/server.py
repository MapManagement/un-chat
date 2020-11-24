from concurrent import futures
from unchat import database

import grpc

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

    def SendUserLogin(self, request, context):
            print(f"New Login: {request}\n")
            db_connection = database.DBConnector()
            user_passsword = str(request.password)
            try:
                if db_connection.compare_passwords(user_passsword, request.userName):
                    database_user = db_connection.get_user_by_name(request.userName)
                    proto_user_information = chat.UserInformation(
                        userID=database_user["user_id"],
                        userName=request.userName,
                        signUpDate=database_user["created_at"],
                        status=database_user["status"],
                        biograpgy=database_user["biography"],
                        profilePictureDir=database_user["path_profile_picture"]
                    )
                    return proto_user_information
            except Exception:
                return chat.UserInformation()

    def SendUserRegistration(self, request, context):
        print(f"New Registration: {request}\n")
        db_connection = database.DBConnector()
        user_password = str(request.password)
        user_name = str(request.username)
        user = chat.User(userName=user_name, password=user_password)
        try:
            db_connection.insert_user(user)
            return chat.RequestSuccess(receivedRequest=True)
        except Exception:
            return chat.RequestSuccess(receivedRequest=False)


if __name__ == "__main__":
    print("Starting chat server...\n")
    port = 180302
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    rpc.add_ChatMessagesServicer_to_server(ChatServer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()
