# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ping.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ping.proto',
  package='Ping',
  syntax='proto2',
  serialized_pb=_b('\n\nping.proto\x12\x04Ping\"\x0e\n\x0cPingResponseB(\n com.google.android.finsky.protosB\x04Ping')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='Ping.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=34,
)

DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), dict(
  DESCRIPTOR = _PINGRESPONSE,
  __module__ = 'ping_pb2'
  # @@protoc_insertion_point(class_scope:Ping.PingResponse)
  ))
_sym_db.RegisterMessage(PingResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n com.google.android.finsky.protosB\004Ping'))
# @@protoc_insertion_point(module_scope)
