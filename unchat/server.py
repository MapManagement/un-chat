from concurrent import futures

import time
import grpc

import unchat.chat_message_pb2_grpc as rpc
import unchat.chat_message_pb2 as chat


class ChatServer(rpc.ChatMessagesServicer):

    def __init__(self):
        self.chats = []
        self.clients = []

    def SendMessage(self, request, context):
        print(f"Incoming Message {request} \n")
        self.chats.append(request)
        self.clients.append(str(request.senderID))
        return chat.RequestSuccess()

    def ChatStream(self, request_iterator, context):
        old_messages = []
        for new_message in request_iterator:
            for old_message in old_messages:
                if old_message.location == new_message.location:
                    yield old_message
            old_messages.append(new_message)

    """def ChatStream(self, request, context):
        last_index = 0
        while True:
            while len(self.chats) > last_index:
                message = self.chats[last_index]
                last_index += 1
                print(message)
                yield message"""


if __name__ == "__main__":
    print("Starting chat server...\n")
    port = 180320
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    rpc.add_ChatMessagesServicer_to_server(ChatServer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    while True:
        time.sleep(18 * 3 * 2002)
