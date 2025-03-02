# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guild.proto

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
  name='guild.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bguild.proto\"/\n\rC2GSOpenGuild\x12\x0e\n\x06\x63\x61t_id\x18\x01 \x01(\r\x12\x0e\n\x06sub_id\x18\x02 \x01(\r\"3\n\x10\x43\x32GSBuyGuildItem\x12\x0f\n\x07good_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61mount\x18\x02 \x01(\r\"4\n\x11\x43\x32GSSellGuildItem\x12\x0f\n\x07item_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61mount\x18\x02 \x01(\r\"$\n\x11\x43\x32GSGetGuildPrice\x12\x0f\n\x07good_id\x18\x01 \x01(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2GSOPENGUILD = _descriptor.Descriptor(
  name='C2GSOpenGuild',
  full_name='C2GSOpenGuild',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cat_id', full_name='C2GSOpenGuild.cat_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_id', full_name='C2GSOpenGuild.sub_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=15,
  serialized_end=62,
)


_C2GSBUYGUILDITEM = _descriptor.Descriptor(
  name='C2GSBuyGuildItem',
  full_name='C2GSBuyGuildItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='good_id', full_name='C2GSBuyGuildItem.good_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='C2GSBuyGuildItem.amount', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=64,
  serialized_end=115,
)


_C2GSSELLGUILDITEM = _descriptor.Descriptor(
  name='C2GSSellGuildItem',
  full_name='C2GSSellGuildItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='C2GSSellGuildItem.item_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='C2GSSellGuildItem.amount', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=117,
  serialized_end=169,
)


_C2GSGETGUILDPRICE = _descriptor.Descriptor(
  name='C2GSGetGuildPrice',
  full_name='C2GSGetGuildPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='good_id', full_name='C2GSGetGuildPrice.good_id', index=0,
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
  serialized_start=171,
  serialized_end=207,
)

DESCRIPTOR.message_types_by_name['C2GSOpenGuild'] = _C2GSOPENGUILD
DESCRIPTOR.message_types_by_name['C2GSBuyGuildItem'] = _C2GSBUYGUILDITEM
DESCRIPTOR.message_types_by_name['C2GSSellGuildItem'] = _C2GSSELLGUILDITEM
DESCRIPTOR.message_types_by_name['C2GSGetGuildPrice'] = _C2GSGETGUILDPRICE

C2GSOpenGuild = _reflection.GeneratedProtocolMessageType('C2GSOpenGuild', (_message.Message,), dict(
  DESCRIPTOR = _C2GSOPENGUILD,
  __module__ = 'guild_pb2'
  # @@protoc_insertion_point(class_scope:C2GSOpenGuild)
  ))
_sym_db.RegisterMessage(C2GSOpenGuild)

C2GSBuyGuildItem = _reflection.GeneratedProtocolMessageType('C2GSBuyGuildItem', (_message.Message,), dict(
  DESCRIPTOR = _C2GSBUYGUILDITEM,
  __module__ = 'guild_pb2'
  # @@protoc_insertion_point(class_scope:C2GSBuyGuildItem)
  ))
_sym_db.RegisterMessage(C2GSBuyGuildItem)

C2GSSellGuildItem = _reflection.GeneratedProtocolMessageType('C2GSSellGuildItem', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSELLGUILDITEM,
  __module__ = 'guild_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSellGuildItem)
  ))
_sym_db.RegisterMessage(C2GSSellGuildItem)

C2GSGetGuildPrice = _reflection.GeneratedProtocolMessageType('C2GSGetGuildPrice', (_message.Message,), dict(
  DESCRIPTOR = _C2GSGETGUILDPRICE,
  __module__ = 'guild_pb2'
  # @@protoc_insertion_point(class_scope:C2GSGetGuildPrice)
  ))
_sym_db.RegisterMessage(C2GSGetGuildPrice)


# @@protoc_insertion_point(module_scope)
