# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import chat_message_pb2 as chat__message__pb2


class ChatMessagesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ChatStream = channel.stream_stream(
                '/grpc.ChatMessages/ChatStream',
                request_serializer=chat__message__pb2.ChatMessage.SerializeToString,
                response_deserializer=chat__message__pb2.ChatMessage.FromString,
                )
        self.SendMessage = channel.unary_unary(
                '/grpc.ChatMessages/SendMessage',
                request_serializer=chat__message__pb2.ChatMessage.SerializeToString,
                response_deserializer=chat__message__pb2.RequestSuccess.FromString,
                )


class ChatMessagesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ChatStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChatMessagesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ChatStream': grpc.stream_stream_rpc_method_handler(
                    servicer.ChatStream,
                    request_deserializer=chat__message__pb2.ChatMessage.FromString,
                    response_serializer=chat__message__pb2.ChatMessage.SerializeToString,
            ),
            'SendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SendMessage,
                    request_deserializer=chat__message__pb2.ChatMessage.FromString,
                    response_serializer=chat__message__pb2.RequestSuccess.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc.ChatMessages', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChatMessages(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ChatStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/grpc.ChatMessages/ChatStream',
            chat__message__pb2.ChatMessage.SerializeToString,
            chat__message__pb2.ChatMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/grpc.ChatMessages/SendMessage',
            chat__message__pb2.ChatMessage.SerializeToString,
            chat__message__pb2.RequestSuccess.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
