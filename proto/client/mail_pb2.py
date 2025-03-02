# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import common_pb2 as base_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mail.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nmail.proto\x1a\x11\x62\x61se/common.proto\"\x1e\n\x0c\x43\x32GSOpenMail\x12\x0e\n\x06mailid\x18\x01 \x01(\r\"\"\n\x10\x43\x32GSAcceptAttach\x12\x0e\n\x06mailid\x18\x01 \x01(\r\"\x15\n\x13\x43\x32GSAcceptAllAttach\"!\n\x0e\x43\x32GSDeleteMail\x12\x0f\n\x07mailids\x18\x01 \x03(\r\",\n\x11\x43\x32GSDeleteAllMail\x12\x17\n\x0f\x63nt_only_client\x18\x01 \x01(\r')
  ,
  dependencies=[base_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2GSOPENMAIL = _descriptor.Descriptor(
  name='C2GSOpenMail',
  full_name='C2GSOpenMail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mailid', full_name='C2GSOpenMail.mailid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=33,
  serialized_end=63,
)


_C2GSACCEPTATTACH = _descriptor.Descriptor(
  name='C2GSAcceptAttach',
  full_name='C2GSAcceptAttach',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mailid', full_name='C2GSAcceptAttach.mailid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=65,
  serialized_end=99,
)


_C2GSACCEPTALLATTACH = _descriptor.Descriptor(
  name='C2GSAcceptAllAttach',
  full_name='C2GSAcceptAllAttach',
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
  serialized_start=101,
  serialized_end=122,
)


_C2GSDELETEMAIL = _descriptor.Descriptor(
  name='C2GSDeleteMail',
  full_name='C2GSDeleteMail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mailids', full_name='C2GSDeleteMail.mailids', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=124,
  serialized_end=157,
)


_C2GSDELETEALLMAIL = _descriptor.Descriptor(
  name='C2GSDeleteAllMail',
  full_name='C2GSDeleteAllMail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cnt_only_client', full_name='C2GSDeleteAllMail.cnt_only_client', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=159,
  serialized_end=203,
)

DESCRIPTOR.message_types_by_name['C2GSOpenMail'] = _C2GSOPENMAIL
DESCRIPTOR.message_types_by_name['C2GSAcceptAttach'] = _C2GSACCEPTATTACH
DESCRIPTOR.message_types_by_name['C2GSAcceptAllAttach'] = _C2GSACCEPTALLATTACH
DESCRIPTOR.message_types_by_name['C2GSDeleteMail'] = _C2GSDELETEMAIL
DESCRIPTOR.message_types_by_name['C2GSDeleteAllMail'] = _C2GSDELETEALLMAIL

C2GSOpenMail = _reflection.GeneratedProtocolMessageType('C2GSOpenMail', (_message.Message,), dict(
  DESCRIPTOR = _C2GSOPENMAIL,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:C2GSOpenMail)
  ))
_sym_db.RegisterMessage(C2GSOpenMail)

C2GSAcceptAttach = _reflection.GeneratedProtocolMessageType('C2GSAcceptAttach', (_message.Message,), dict(
  DESCRIPTOR = _C2GSACCEPTATTACH,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:C2GSAcceptAttach)
  ))
_sym_db.RegisterMessage(C2GSAcceptAttach)

C2GSAcceptAllAttach = _reflection.GeneratedProtocolMessageType('C2GSAcceptAllAttach', (_message.Message,), dict(
  DESCRIPTOR = _C2GSACCEPTALLATTACH,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:C2GSAcceptAllAttach)
  ))
_sym_db.RegisterMessage(C2GSAcceptAllAttach)

C2GSDeleteMail = _reflection.GeneratedProtocolMessageType('C2GSDeleteMail', (_message.Message,), dict(
  DESCRIPTOR = _C2GSDELETEMAIL,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:C2GSDeleteMail)
  ))
_sym_db.RegisterMessage(C2GSDeleteMail)

C2GSDeleteAllMail = _reflection.GeneratedProtocolMessageType('C2GSDeleteAllMail', (_message.Message,), dict(
  DESCRIPTOR = _C2GSDELETEALLMAIL,
  __module__ = 'mail_pb2'
  # @@protoc_insertion_point(class_scope:C2GSDeleteAllMail)
  ))
_sym_db.RegisterMessage(C2GSDeleteAllMail)


# @@protoc_insertion_point(module_scope)
