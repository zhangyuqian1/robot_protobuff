# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recovery.proto

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
  name='recovery.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0erecovery.proto\"\x1e\n\x10\x43\x32GSRecoveryItem\x12\n\n\x02id\x18\x01 \x01(\r\"\x1d\n\x0f\x43\x32GSRecoverySum\x12\n\n\x02id\x18\x01 \x01(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2GSRECOVERYITEM = _descriptor.Descriptor(
  name='C2GSRecoveryItem',
  full_name='C2GSRecoveryItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='C2GSRecoveryItem.id', index=0,
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
  serialized_start=18,
  serialized_end=48,
)


_C2GSRECOVERYSUM = _descriptor.Descriptor(
  name='C2GSRecoverySum',
  full_name='C2GSRecoverySum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='C2GSRecoverySum.id', index=0,
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
  serialized_start=50,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['C2GSRecoveryItem'] = _C2GSRECOVERYITEM
DESCRIPTOR.message_types_by_name['C2GSRecoverySum'] = _C2GSRECOVERYSUM

C2GSRecoveryItem = _reflection.GeneratedProtocolMessageType('C2GSRecoveryItem', (_message.Message,), dict(
  DESCRIPTOR = _C2GSRECOVERYITEM,
  __module__ = 'recovery_pb2'
  # @@protoc_insertion_point(class_scope:C2GSRecoveryItem)
  ))
_sym_db.RegisterMessage(C2GSRecoveryItem)

C2GSRecoverySum = _reflection.GeneratedProtocolMessageType('C2GSRecoverySum', (_message.Message,), dict(
  DESCRIPTOR = _C2GSRECOVERYSUM,
  __module__ = 'recovery_pb2'
  # @@protoc_insertion_point(class_scope:C2GSRecoverySum)
  ))
_sym_db.RegisterMessage(C2GSRecoverySum)


# @@protoc_insertion_point(module_scope)
