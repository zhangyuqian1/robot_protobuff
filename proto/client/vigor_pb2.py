# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vigor.proto

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
  name='vigor.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bvigor.proto\"\x15\n\x13\x43\x32GSOpenVigorChange\"+\n\x14\x43\x32GSVigorChangeStart\x12\x13\n\x0b\x63hange_type\x18\x01 \x01(\r\"G\n\x19\x43\x32GSVigorChangeItemStatus\x12\x15\n\ris_change_all\x18\x01 \x01(\r\x12\x13\n\x0b\x63hange_type\x18\x02 \x01(\r\"\x15\n\x13\x43\x32GSVigorChangeList\"\x1b\n\x19\x43\x32GSChangeGoldcoinToVigor\"\"\n\x0b\x43\x32GSBuyGrid\x12\x13\n\x0b\x63hange_type\x18\x01 \x01(\r\"-\n\x16\x43\x32GSVigorChangeProduct\x12\x13\n\x0b\x63hange_type\x18\x01 \x01(\r\"\x1c\n\x1a\x43\x32GSVigorChangeALLProducts\"7\n\rChangeOneItem\x12\x0f\n\x07item_id\x18\x01 \x01(\r\x12\x15\n\rchange_amount\x18\x02 \x01(\r\"?\n\x15\x43\x32GSChangeItemToVigor\x12&\n\x0e\x63hangeItemList\x18\x01 \x03(\x0b\x32\x0e.ChangeOneItem')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2GSOPENVIGORCHANGE = _descriptor.Descriptor(
  name='C2GSOpenVigorChange',
  full_name='C2GSOpenVigorChange',
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
  serialized_start=15,
  serialized_end=36,
)


_C2GSVIGORCHANGESTART = _descriptor.Descriptor(
  name='C2GSVigorChangeStart',
  full_name='C2GSVigorChangeStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='change_type', full_name='C2GSVigorChangeStart.change_type', index=0,
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
  serialized_start=38,
  serialized_end=81,
)


_C2GSVIGORCHANGEITEMSTATUS = _descriptor.Descriptor(
  name='C2GSVigorChangeItemStatus',
  full_name='C2GSVigorChangeItemStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_change_all', full_name='C2GSVigorChangeItemStatus.is_change_all', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_type', full_name='C2GSVigorChangeItemStatus.change_type', index=1,
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
  serialized_start=83,
  serialized_end=154,
)


_C2GSVIGORCHANGELIST = _descriptor.Descriptor(
  name='C2GSVigorChangeList',
  full_name='C2GSVigorChangeList',
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
  serialized_start=156,
  serialized_end=177,
)


_C2GSCHANGEGOLDCOINTOVIGOR = _descriptor.Descriptor(
  name='C2GSChangeGoldcoinToVigor',
  full_name='C2GSChangeGoldcoinToVigor',
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
  serialized_start=179,
  serialized_end=206,
)


_C2GSBUYGRID = _descriptor.Descriptor(
  name='C2GSBuyGrid',
  full_name='C2GSBuyGrid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='change_type', full_name='C2GSBuyGrid.change_type', index=0,
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
  serialized_start=208,
  serialized_end=242,
)


_C2GSVIGORCHANGEPRODUCT = _descriptor.Descriptor(
  name='C2GSVigorChangeProduct',
  full_name='C2GSVigorChangeProduct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='change_type', full_name='C2GSVigorChangeProduct.change_type', index=0,
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
  serialized_start=244,
  serialized_end=289,
)


_C2GSVIGORCHANGEALLPRODUCTS = _descriptor.Descriptor(
  name='C2GSVigorChangeALLProducts',
  full_name='C2GSVigorChangeALLProducts',
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
  serialized_start=291,
  serialized_end=319,
)


_CHANGEONEITEM = _descriptor.Descriptor(
  name='ChangeOneItem',
  full_name='ChangeOneItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='ChangeOneItem.item_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_amount', full_name='ChangeOneItem.change_amount', index=1,
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
  serialized_start=321,
  serialized_end=376,
)


_C2GSCHANGEITEMTOVIGOR = _descriptor.Descriptor(
  name='C2GSChangeItemToVigor',
  full_name='C2GSChangeItemToVigor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='changeItemList', full_name='C2GSChangeItemToVigor.changeItemList', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=378,
  serialized_end=441,
)

_C2GSCHANGEITEMTOVIGOR.fields_by_name['changeItemList'].message_type = _CHANGEONEITEM
DESCRIPTOR.message_types_by_name['C2GSOpenVigorChange'] = _C2GSOPENVIGORCHANGE
DESCRIPTOR.message_types_by_name['C2GSVigorChangeStart'] = _C2GSVIGORCHANGESTART
DESCRIPTOR.message_types_by_name['C2GSVigorChangeItemStatus'] = _C2GSVIGORCHANGEITEMSTATUS
DESCRIPTOR.message_types_by_name['C2GSVigorChangeList'] = _C2GSVIGORCHANGELIST
DESCRIPTOR.message_types_by_name['C2GSChangeGoldcoinToVigor'] = _C2GSCHANGEGOLDCOINTOVIGOR
DESCRIPTOR.message_types_by_name['C2GSBuyGrid'] = _C2GSBUYGRID
DESCRIPTOR.message_types_by_name['C2GSVigorChangeProduct'] = _C2GSVIGORCHANGEPRODUCT
DESCRIPTOR.message_types_by_name['C2GSVigorChangeALLProducts'] = _C2GSVIGORCHANGEALLPRODUCTS
DESCRIPTOR.message_types_by_name['ChangeOneItem'] = _CHANGEONEITEM
DESCRIPTOR.message_types_by_name['C2GSChangeItemToVigor'] = _C2GSCHANGEITEMTOVIGOR

C2GSOpenVigorChange = _reflection.GeneratedProtocolMessageType('C2GSOpenVigorChange', (_message.Message,), dict(
  DESCRIPTOR = _C2GSOPENVIGORCHANGE,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSOpenVigorChange)
  ))
_sym_db.RegisterMessage(C2GSOpenVigorChange)

C2GSVigorChangeStart = _reflection.GeneratedProtocolMessageType('C2GSVigorChangeStart', (_message.Message,), dict(
  DESCRIPTOR = _C2GSVIGORCHANGESTART,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSVigorChangeStart)
  ))
_sym_db.RegisterMessage(C2GSVigorChangeStart)

C2GSVigorChangeItemStatus = _reflection.GeneratedProtocolMessageType('C2GSVigorChangeItemStatus', (_message.Message,), dict(
  DESCRIPTOR = _C2GSVIGORCHANGEITEMSTATUS,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSVigorChangeItemStatus)
  ))
_sym_db.RegisterMessage(C2GSVigorChangeItemStatus)

C2GSVigorChangeList = _reflection.GeneratedProtocolMessageType('C2GSVigorChangeList', (_message.Message,), dict(
  DESCRIPTOR = _C2GSVIGORCHANGELIST,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSVigorChangeList)
  ))
_sym_db.RegisterMessage(C2GSVigorChangeList)

C2GSChangeGoldcoinToVigor = _reflection.GeneratedProtocolMessageType('C2GSChangeGoldcoinToVigor', (_message.Message,), dict(
  DESCRIPTOR = _C2GSCHANGEGOLDCOINTOVIGOR,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSChangeGoldcoinToVigor)
  ))
_sym_db.RegisterMessage(C2GSChangeGoldcoinToVigor)

C2GSBuyGrid = _reflection.GeneratedProtocolMessageType('C2GSBuyGrid', (_message.Message,), dict(
  DESCRIPTOR = _C2GSBUYGRID,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSBuyGrid)
  ))
_sym_db.RegisterMessage(C2GSBuyGrid)

C2GSVigorChangeProduct = _reflection.GeneratedProtocolMessageType('C2GSVigorChangeProduct', (_message.Message,), dict(
  DESCRIPTOR = _C2GSVIGORCHANGEPRODUCT,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSVigorChangeProduct)
  ))
_sym_db.RegisterMessage(C2GSVigorChangeProduct)

C2GSVigorChangeALLProducts = _reflection.GeneratedProtocolMessageType('C2GSVigorChangeALLProducts', (_message.Message,), dict(
  DESCRIPTOR = _C2GSVIGORCHANGEALLPRODUCTS,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSVigorChangeALLProducts)
  ))
_sym_db.RegisterMessage(C2GSVigorChangeALLProducts)

ChangeOneItem = _reflection.GeneratedProtocolMessageType('ChangeOneItem', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEONEITEM,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:ChangeOneItem)
  ))
_sym_db.RegisterMessage(ChangeOneItem)

C2GSChangeItemToVigor = _reflection.GeneratedProtocolMessageType('C2GSChangeItemToVigor', (_message.Message,), dict(
  DESCRIPTOR = _C2GSCHANGEITEMTOVIGOR,
  __module__ = 'vigor_pb2'
  # @@protoc_insertion_point(class_scope:C2GSChangeItemToVigor)
  ))
_sym_db.RegisterMessage(C2GSChangeItemToVigor)


# @@protoc_insertion_point(module_scope)
