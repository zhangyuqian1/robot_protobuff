# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: store.proto

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
  name='store.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bstore.proto\"(\n\x10\x43\x32GSExchangeGold\x12\x14\n\x0cstore_itemid\x18\x01 \x01(\r\"*\n\x12\x43\x32GSExchangeSilver\x12\x14\n\x0cstore_itemid\x18\x01 \x01(\r\"G\n\x0f\x43\x32GSNpcStoreBuy\x12\x0e\n\x06\x62uy_id\x18\x01 \x01(\r\x12\x11\n\tbuy_count\x18\x02 \x01(\r\x12\x11\n\tall_money\x18\x03 \x01(\r\"/\n\x0f\x43\x32GSFastBuyItem\x12\x0f\n\x07item_id\x18\x01 \x01(\r\x12\x0b\n\x03\x63nt\x18\x02 \x01(\r\"\x17\n\x15\x43\x32GSExChangeDanceBook')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2GSEXCHANGEGOLD = _descriptor.Descriptor(
  name='C2GSExchangeGold',
  full_name='C2GSExchangeGold',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store_itemid', full_name='C2GSExchangeGold.store_itemid', index=0,
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
  serialized_start=15,
  serialized_end=55,
)


_C2GSEXCHANGESILVER = _descriptor.Descriptor(
  name='C2GSExchangeSilver',
  full_name='C2GSExchangeSilver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='store_itemid', full_name='C2GSExchangeSilver.store_itemid', index=0,
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
  serialized_start=57,
  serialized_end=99,
)


_C2GSNPCSTOREBUY = _descriptor.Descriptor(
  name='C2GSNpcStoreBuy',
  full_name='C2GSNpcStoreBuy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buy_id', full_name='C2GSNpcStoreBuy.buy_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buy_count', full_name='C2GSNpcStoreBuy.buy_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='all_money', full_name='C2GSNpcStoreBuy.all_money', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=101,
  serialized_end=172,
)


_C2GSFASTBUYITEM = _descriptor.Descriptor(
  name='C2GSFastBuyItem',
  full_name='C2GSFastBuyItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='C2GSFastBuyItem.item_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cnt', full_name='C2GSFastBuyItem.cnt', index=1,
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
  serialized_start=174,
  serialized_end=221,
)


_C2GSEXCHANGEDANCEBOOK = _descriptor.Descriptor(
  name='C2GSExChangeDanceBook',
  full_name='C2GSExChangeDanceBook',
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
  serialized_start=223,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['C2GSExchangeGold'] = _C2GSEXCHANGEGOLD
DESCRIPTOR.message_types_by_name['C2GSExchangeSilver'] = _C2GSEXCHANGESILVER
DESCRIPTOR.message_types_by_name['C2GSNpcStoreBuy'] = _C2GSNPCSTOREBUY
DESCRIPTOR.message_types_by_name['C2GSFastBuyItem'] = _C2GSFASTBUYITEM
DESCRIPTOR.message_types_by_name['C2GSExChangeDanceBook'] = _C2GSEXCHANGEDANCEBOOK

C2GSExchangeGold = _reflection.GeneratedProtocolMessageType('C2GSExchangeGold', (_message.Message,), dict(
  DESCRIPTOR = _C2GSEXCHANGEGOLD,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:C2GSExchangeGold)
  ))
_sym_db.RegisterMessage(C2GSExchangeGold)

C2GSExchangeSilver = _reflection.GeneratedProtocolMessageType('C2GSExchangeSilver', (_message.Message,), dict(
  DESCRIPTOR = _C2GSEXCHANGESILVER,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:C2GSExchangeSilver)
  ))
_sym_db.RegisterMessage(C2GSExchangeSilver)

C2GSNpcStoreBuy = _reflection.GeneratedProtocolMessageType('C2GSNpcStoreBuy', (_message.Message,), dict(
  DESCRIPTOR = _C2GSNPCSTOREBUY,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:C2GSNpcStoreBuy)
  ))
_sym_db.RegisterMessage(C2GSNpcStoreBuy)

C2GSFastBuyItem = _reflection.GeneratedProtocolMessageType('C2GSFastBuyItem', (_message.Message,), dict(
  DESCRIPTOR = _C2GSFASTBUYITEM,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:C2GSFastBuyItem)
  ))
_sym_db.RegisterMessage(C2GSFastBuyItem)

C2GSExChangeDanceBook = _reflection.GeneratedProtocolMessageType('C2GSExChangeDanceBook', (_message.Message,), dict(
  DESCRIPTOR = _C2GSEXCHANGEDANCEBOOK,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:C2GSExChangeDanceBook)
  ))
_sym_db.RegisterMessage(C2GSExChangeDanceBook)


# @@protoc_insertion_point(module_scope)
