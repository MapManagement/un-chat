from concurrent import futures
from unchat import database
from google.protobuf.timestamp_pb2 import Timestamp

import grpc
import psutil
import shutil
import platform
import time
import base64

import unchat.chat_message_pb2_grpc as rpc
import unchat.chat_message_pb2 as chat


class ChatServer(rpc.ChatMessagesServicer):

    def __init__(self):
        self.chats = []
        self.db_connection = database.DBConnector()

    def SendMessage(self, request, context):
        print(f"Incoming Message {request} \n")
        self.chats.append(request)
        if request.recipientID != "-3":
            self.db_connection.insert_new_message(request)
        else:
            self.db_connection.set_user_online_status(request.userName, 0)
        return chat.RequestSuccess(receivedRequest=True)

    def ChatStream(self, request, context):
        last_index = 0
        self.chats = []
        while context.is_active():
            while len(self.chats) > last_index:
                print(self.chats)
                message = self.chats[last_index]
                if message.senderID == request.userID and message.recipientID == "-3":
                    return
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
            is_online = True if database_user[7] == 1 else False
            proto_user_information = chat.User(
                userID=str(database_user[0]),
                userName=database_user[1],
                signUpDate=timestamp_object,
                status=database_user[4],
                biography=database_user[5],
                profilePictureDir=database_user[6],
                is_online=is_online
            )
            return proto_user_information
        except Exception as ex:
            print(ex)
            return chat.User()

    def CheckUserLogin(self, request, context):
        print(f"CheckLogin: {context.peer()}")
        user_password = str(request.password)

        passwords_equal = self.db_connection.compare_passwords(user_password, request.userName)
        if passwords_equal:
            self.db_connection.set_user_online_status(request.userName, 1)
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
            is_online = True if user[7] == 1 else False
            new_user = chat.User(
                userID=str(user[0]),
                userName=user[1],
                signUpDate=timestamp_object,
                status=user[4],
                biography=user[5],
                profilePictureDir=user[6],
                is_online=is_online
            )
            users.user.append(new_user)
        return users

    def LoadOldMessages(self, request, context):
        messages = self.db_connection.get_old_messages_by_user_id(request)
        if messages is None:
            return
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

    def DeleteProfile(self, request, context):
        user_password = str(request.password)

        passwords_equal = self.db_connection.compare_passwords(user_password, request.userName)
        if passwords_equal:
            self.db_connection.delete_user(request)
        return chat.RequestSuccess(receivedRequest=passwords_equal)

    def GetSystemInformation(self, request, context):
        uname = platform.uname()
        ip_address = ""
        mac_address = ""
        for i_name, i_addresses in psutil.net_if_addrs().items():
            for address in i_addresses:
                if str(address.family) == "AddressFamily.AF_INET":
                    ip_address = address.address
                elif str(address.family) == "AddressFamily.AF_PACKET":
                    mac_address = address.address

        system_information = chat.SystemInformation(
            os=uname.system,
            version=uname.version,
            cpuName=uname.processor,
            cpuCores=int(psutil.cpu_count(False)),
            cpuThreads=int(psutil.cpu_count(True)),
            installedRam=psutil.virtual_memory().total,
            ipAddress=ip_address,
            macAddress=mac_address
        )
        return system_information

    def GetSystemMetrics(self, request, context):
        interval = request.seconds
        while context.is_active():
            metrics = chat.Metrics(
                cpuUsageP=round(psutil.cpu_percent(1), 1),
                ramUsageP=round(psutil.virtual_memory().used / psutil.virtual_memory().total * 100, 1),
                ramUsageV=round(psutil.virtual_memory().used / (1024**3), 2),  # in gigabytes
                upload=round(psutil.net_io_counters().bytes_sent / (1024**2), 2),  # in megabytes
                download=round(psutil.net_io_counters().bytes_recv (2014**2), 2),  # in megabytes
                avDiskSpaceP=round((shutil.disk_usage("/").used / shutil.disk_usage("/").total), 1),
                avDiskSpaceV=round(shutil.disk_usage("/").used / (1024**3), 2)  # in gigabytes
            )
            time.sleep(interval)
            yield metrics

    def GetAllUsers(self, request, context):
        users = self.db_connection.get_all_users()
        for user in users:
            timestamp_object = Timestamp(seconds=int(user[2].timestamp()))
            proto_user = chat.User(
                userID=str(user[0]),
                userName=user[1],
                signUpDate=timestamp_object,
                status=user[3],
                biography=user[4]
            )
            yield proto_user

    def UploadImage(self, request_iterator, context):
        metadata_dict = dict(context.invocation_metadata())
        print(metadata_dict)
        file_name = metadata_dict["filename"]
        print(file_name)
        with open(f"resources/{file_name}", "wb") as file:
            for request in request_iterator:
                if request.statusCode == chat.FileStatusCode.InProgress:
                    file.write(request.image)
                elif request.statusCode == chat.FileStatusCode.Ok:
                    response = chat.UploadImageResponse(
                        statusCode=chat.FileStatusCode.Ok
                    )
                    return response
                else:
                    response = chat.UploadImageResponse(
                        statusCode=chat.FileStatusCode.Failed
                    )
                    return response
            file.close()

    def DownloadImage(self, request, context):
        file_name = request.fileName
        try:
            f = open(f"resources/{file_name}", "rb")
            f.close()
        except FileNotFoundError:
            file_name = "default_profile_picture.png"

        with open(f"resources/{file_name}", "rb") as file:
            while True:
                file_bytes = file.read(2048)
                if file_bytes:
                    byte_response = chat.UploadImageRequest(
                        image=file_bytes,
                        fileName=file_name,
                        statusCode=chat.FileStatusCode.InProgress
                    )
                    yield byte_response
                else:
                    byte_response = chat.UploadImageRequest(
                        fileName=file_name,
                        statusCode=chat.FileStatusCode.Ok
                    )
                    yield byte_response
                    break


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
