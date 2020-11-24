# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat_message.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x63hat_message.proto\x12\x04grpc\x1a\x1fgoogle/protobuf/timestamp.proto\"(\n\x04User\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12\x10\n\x08userName\x18\x02 \x01(\t\"\x8f\x01\n\x0fUserInformation\x12\x0e\n\x06userID\x18\x01 \x01(\t\x12.\n\nsignUpDate\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x11\n\tbiography\x18\x04 \x01(\t\x12\x19\n\x11profilePictureDir\x18\x05 \x01(\t\"I\n\x0b\x43hatMessage\x12\x10\n\x08senderID\x18\x01 \x01(\t\x12\x13\n\x0brecipientID\x18\x02 \x01(\t\x12\x13\n\x0bmessageText\x18\x03 \x01(\t\")\n\x0eRequestSuccess\x12\x17\n\x0freceivedRequest\x18\x01 \x01(\x08\"/\n\tUserLogin\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2\xed\x01\n\x0c\x43hatMessages\x12-\n\nChatStream\x12\n.grpc.User\x1a\x11.grpc.ChatMessage0\x01\x12\x36\n\x0bSendMessage\x12\x11.grpc.ChatMessage\x1a\x14.grpc.RequestSuccess\x12\x37\n\rSendUserLogin\x12\x0f.grpc.UserLogin\x1a\x15.grpc.UserInformation\x12=\n\x14SendUserRegistration\x12\x0f.grpc.UserLogin\x1a\x14.grpc.RequestSuccessb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_USER = _descriptor.Descriptor(
  name='User',
  full_name='grpc.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userID', full_name='grpc.User.userID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userName', full_name='grpc.User.userName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=101,
)


_USERINFORMATION = _descriptor.Descriptor(
  name='UserInformation',
  full_name='grpc.UserInformation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userID', full_name='grpc.UserInformation.userID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signUpDate', full_name='grpc.UserInformation.signUpDate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='grpc.UserInformation.status', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='biography', full_name='grpc.UserInformation.biography', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='profilePictureDir', full_name='grpc.UserInformation.profilePictureDir', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=247,
)


_CHATMESSAGE = _descriptor.Descriptor(
  name='ChatMessage',
  full_name='grpc.ChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='senderID', full_name='grpc.ChatMessage.senderID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipientID', full_name='grpc.ChatMessage.recipientID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='messageText', full_name='grpc.ChatMessage.messageText', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=322,
)


_REQUESTSUCCESS = _descriptor.Descriptor(
  name='RequestSuccess',
  full_name='grpc.RequestSuccess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='receivedRequest', full_name='grpc.RequestSuccess.receivedRequest', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=324,
  serialized_end=365,
)


_USERLOGIN = _descriptor.Descriptor(
  name='UserLogin',
  full_name='grpc.UserLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='grpc.UserLogin.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='grpc.UserLogin.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=414,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=416,
  serialized_end=423,
)

_USERINFORMATION.fields_by_name['signUpDate'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['UserInformation'] = _USERINFORMATION
DESCRIPTOR.message_types_by_name['ChatMessage'] = _CHATMESSAGE
DESCRIPTOR.message_types_by_name['RequestSuccess'] = _REQUESTSUCCESS
DESCRIPTOR.message_types_by_name['UserLogin'] = _USERLOGIN
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'chat_message_pb2'
  # @@protoc_insertion_point(class_scope:grpc.User)
  })
_sym_db.RegisterMessage(User)

UserInformation = _reflection.GeneratedProtocolMessageType('UserInformation', (_message.Message,), {
  'DESCRIPTOR' : _USERINFORMATION,
  '__module__' : 'chat_message_pb2'
  # @@protoc_insertion_point(class_scope:grpc.UserInformation)
  })
_sym_db.RegisterMessage(UserInformation)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _CHATMESSAGE,
  '__module__' : 'chat_message_pb2'
  # @@protoc_insertion_point(class_scope:grpc.ChatMessage)
  })
_sym_db.RegisterMessage(ChatMessage)

RequestSuccess = _reflection.GeneratedProtocolMessageType('RequestSuccess', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSUCCESS,
  '__module__' : 'chat_message_pb2'
  # @@protoc_insertion_point(class_scope:grpc.RequestSuccess)
  })
_sym_db.RegisterMessage(RequestSuccess)

UserLogin = _reflection.GeneratedProtocolMessageType('UserLogin', (_message.Message,), {
  'DESCRIPTOR' : _USERLOGIN,
  '__module__' : 'chat_message_pb2'
  # @@protoc_insertion_point(class_scope:grpc.UserLogin)
  })
_sym_db.RegisterMessage(UserLogin)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'chat_message_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Empty)
  })
_sym_db.RegisterMessage(Empty)



_CHATMESSAGES = _descriptor.ServiceDescriptor(
  name='ChatMessages',
  full_name='grpc.ChatMessages',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=426,
  serialized_end=663,
  methods=[
  _descriptor.MethodDescriptor(
    name='ChatStream',
    full_name='grpc.ChatMessages.ChatStream',
    index=0,
    containing_service=None,
    input_type=_USER,
    output_type=_CHATMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendMessage',
    full_name='grpc.ChatMessages.SendMessage',
    index=1,
    containing_service=None,
    input_type=_CHATMESSAGE,
    output_type=_REQUESTSUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendUserLogin',
    full_name='grpc.ChatMessages.SendUserLogin',
    index=2,
    containing_service=None,
    input_type=_USERLOGIN,
    output_type=_USERINFORMATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SendUserRegistration',
    full_name='grpc.ChatMessages.SendUserRegistration',
    index=3,
    containing_service=None,
    input_type=_USERLOGIN,
    output_type=_REQUESTSUCCESS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHATMESSAGES)

DESCRIPTOR.services_by_name['ChatMessages'] = _CHATMESSAGES

# @@protoc_insertion_point(module_scope)
