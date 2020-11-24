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

    """def SendUserLogin(self, request, context):
        print(f"New Login: {request}\n")
        db_connection = database.DBConnector()
        success = db_connection.insert_user(request)
        request_success = chat.RequestSuccess
        request_success.receivedRequest = success
        return request_success"""

    def SendUserLogin(self, request, context):
            print(f"New Login: {request}\n")
            db_connection = database.DBConnector()
            user_passsword = str(request.password)
            try:
                if db_connection.compare_passwords(user_passsword, request.userName):
                    database_user = db_connection.get_user_by_name(request.userName)
                    proto_user = chat.User(userID=database_user["user_id"], userName=request.userName)
                    return proto_user
            except Exception:
                return chat.User(userID="", userName="")


if __name__ == "__main__":
    print("Starting chat server...\n")
    port = 180302
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    rpc.add_ChatMessagesServicer_to_server(ChatServer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()
