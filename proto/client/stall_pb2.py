# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stall.proto

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
  name='stall.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bstall.proto\"Q\n\x0f\x43\x32GSAddSellItem\x12\x0e\n\x06pos_id\x18\x01 \x01(\r\x12\x0f\n\x07item_id\x18\x02 \x01(\r\x12\x0e\n\x06\x61mount\x18\x03 \x01(\r\x12\r\n\x05price\x18\x04 \x01(\r\":\n\x08SellItem\x12\x0f\n\x07item_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61mount\x18\x02 \x01(\r\x12\r\n\x05price\x18\x03 \x01(\r\"3\n\x13\x43\x32GSAddSellItemList\x12\x1c\n\titem_list\x18\x01 \x03(\x0b\x32\t.SellItem\"\x15\n\x13\x43\x32GSAddOverTimeItem\"3\n\x12\x43\x32GSResetItemPrice\x12\x0e\n\x06pos_id\x18\x01 \x01(\r\x12\r\n\x05price\x18\x02 \x01(\r\"*\n\tPriceUnit\x12\x0e\n\x06pos_id\x18\x01 \x01(\r\x12\r\n\x05price\x18\x02 \x01(\r\"7\n\x16\x43\x32GSResetItemListPrice\x12\x1d\n\titem_list\x18\x01 \x03(\x0b\x32\n.PriceUnit\"4\n\x12\x43\x32GSRemoveSellItem\x12\x0e\n\x06pos_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61mount\x18\x02 \x01(\r\"\x15\n\x13\x43\x32GSWithdrawAllCash\"%\n\x13\x43\x32GSWithdrawOneGrid\x12\x0e\n\x06pos_id\x18\x01 \x01(\r\"\x10\n\x0e\x43\x32GSUnlockGrid\"A\n\x0f\x43\x32GSBuySellItem\x12\x0e\n\x06\x63\x61t_id\x18\x01 \x01(\r\x12\x0e\n\x06pos_id\x18\x02 \x01(\r\x12\x0e\n\x06\x61mount\x18\x03 \x01(\r\"4\n\x12\x43\x32GSSellItemDetail\x12\x0e\n\x06\x63\x61t_id\x18\x01 \x01(\r\x12\x0e\n\x06pos_id\x18\x02 \x01(\r\"\x0f\n\rC2GSOpenStall\"P\n\x0f\x43\x32GSOpenCatalog\x12\x0e\n\x06\x63\x61t_id\x18\x01 \x01(\r\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\r\n\x05\x66irst\x18\x03 \x01(\r\x12\x10\n\x08item_sid\x18\x04 \x01(\r\"2\n\x12\x43\x32GSRefreshCatalog\x12\x0e\n\x06\x63\x61t_id\x18\x01 \x01(\r\x12\x0c\n\x04gold\x18\x02 \x01(\r\"\"\n\x13\x43\x32GSGetDefaultPrice\x12\x0b\n\x03sid\x18\x01 \x01(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2GSADDSELLITEM = _descriptor.Descriptor(
  name='C2GSAddSellItem',
  full_name='C2GSAddSellItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_id', full_name='C2GSAddSellItem.pos_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_id', full_name='C2GSAddSellItem.item_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='C2GSAddSellItem.amount', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='C2GSAddSellItem.price', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_end=96,
)


_SELLITEM = _descriptor.Descriptor(
  name='SellItem',
  full_name='SellItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='SellItem.item_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='SellItem.amount', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='SellItem.price', index=2,
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
  serialized_start=98,
  serialized_end=156,
)


_C2GSADDSELLITEMLIST = _descriptor.Descriptor(
  name='C2GSAddSellItemList',
  full_name='C2GSAddSellItemList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_list', full_name='C2GSAddSellItemList.item_list', index=0,
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
  serialized_start=158,
  serialized_end=209,
)


_C2GSADDOVERTIMEITEM = _descriptor.Descriptor(
  name='C2GSAddOverTimeItem',
  full_name='C2GSAddOverTimeItem',
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
  serialized_start=211,
  serialized_end=232,
)


_C2GSRESETITEMPRICE = _descriptor.Descriptor(
  name='C2GSResetItemPrice',
  full_name='C2GSResetItemPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_id', full_name='C2GSResetItemPrice.pos_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='C2GSResetItemPrice.price', index=1,
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
  serialized_start=234,
  serialized_end=285,
)


_PRICEUNIT = _descriptor.Descriptor(
  name='PriceUnit',
  full_name='PriceUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_id', full_name='PriceUnit.pos_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='PriceUnit.price', index=1,
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
  serialized_start=287,
  serialized_end=329,
)


_C2GSRESETITEMLISTPRICE = _descriptor.Descriptor(
  name='C2GSResetItemListPrice',
  full_name='C2GSResetItemListPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_list', full_name='C2GSResetItemListPrice.item_list', index=0,
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
  serialized_start=331,
  serialized_end=386,
)


_C2GSREMOVESELLITEM = _descriptor.Descriptor(
  name='C2GSRemoveSellItem',
  full_name='C2GSRemoveSellItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_id', full_name='C2GSRemoveSellItem.pos_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='C2GSRemoveSellItem.amount', index=1,
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
  serialized_start=388,
  serialized_end=440,
)


_C2GSWITHDRAWALLCASH = _descriptor.Descriptor(
  name='C2GSWithdrawAllCash',
  full_name='C2GSWithdrawAllCash',
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
  serialized_start=442,
  serialized_end=463,
)


_C2GSWITHDRAWONEGRID = _descriptor.Descriptor(
  name='C2GSWithdrawOneGrid',
  full_name='C2GSWithdrawOneGrid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pos_id', full_name='C2GSWithdrawOneGrid.pos_id', index=0,
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
  serialized_start=465,
  serialized_end=502,
)


_C2GSUNLOCKGRID = _descriptor.Descriptor(
  name='C2GSUnlockGrid',
  full_name='C2GSUnlockGrid',
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
  serialized_start=504,
  serialized_end=520,
)


_C2GSBUYSELLITEM = _descriptor.Descriptor(
  name='C2GSBuySellItem',
  full_name='C2GSBuySellItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cat_id', full_name='C2GSBuySellItem.cat_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_id', full_name='C2GSBuySellItem.pos_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='C2GSBuySellItem.amount', index=2,
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
  serialized_start=522,
  serialized_end=587,
)


_C2GSSELLITEMDETAIL = _descriptor.Descriptor(
  name='C2GSSellItemDetail',
  full_name='C2GSSellItemDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cat_id', full_name='C2GSSellItemDetail.cat_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pos_id', full_name='C2GSSellItemDetail.pos_id', index=1,
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
  serialized_start=589,
  serialized_end=641,
)


_C2GSOPENSTALL = _descriptor.Descriptor(
  name='C2GSOpenStall',
  full_name='C2GSOpenStall',
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
  serialized_start=643,
  serialized_end=658,
)


_C2GSOPENCATALOG = _descriptor.Descriptor(
  name='C2GSOpenCatalog',
  full_name='C2GSOpenCatalog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cat_id', full_name='C2GSOpenCatalog.cat_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page', full_name='C2GSOpenCatalog.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first', full_name='C2GSOpenCatalog.first', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_sid', full_name='C2GSOpenCatalog.item_sid', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=660,
  serialized_end=740,
)


_C2GSREFRESHCATALOG = _descriptor.Descriptor(
  name='C2GSRefreshCatalog',
  full_name='C2GSRefreshCatalog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cat_id', full_name='C2GSRefreshCatalog.cat_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='C2GSRefreshCatalog.gold', index=1,
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
  serialized_start=742,
  serialized_end=792,
)


_C2GSGETDEFAULTPRICE = _descriptor.Descriptor(
  name='C2GSGetDefaultPrice',
  full_name='C2GSGetDefaultPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='C2GSGetDefaultPrice.sid', index=0,
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
  serialized_start=794,
  serialized_end=828,
)

_C2GSADDSELLITEMLIST.fields_by_name['item_list'].message_type = _SELLITEM
_C2GSRESETITEMLISTPRICE.fields_by_name['item_list'].message_type = _PRICEUNIT
DESCRIPTOR.message_types_by_name['C2GSAddSellItem'] = _C2GSADDSELLITEM
DESCRIPTOR.message_types_by_name['SellItem'] = _SELLITEM
DESCRIPTOR.message_types_by_name['C2GSAddSellItemList'] = _C2GSADDSELLITEMLIST
DESCRIPTOR.message_types_by_name['C2GSAddOverTimeItem'] = _C2GSADDOVERTIMEITEM
DESCRIPTOR.message_types_by_name['C2GSResetItemPrice'] = _C2GSRESETITEMPRICE
DESCRIPTOR.message_types_by_name['PriceUnit'] = _PRICEUNIT
DESCRIPTOR.message_types_by_name['C2GSResetItemListPrice'] = _C2GSRESETITEMLISTPRICE
DESCRIPTOR.message_types_by_name['C2GSRemoveSellItem'] = _C2GSREMOVESELLITEM
DESCRIPTOR.message_types_by_name['C2GSWithdrawAllCash'] = _C2GSWITHDRAWALLCASH
DESCRIPTOR.message_types_by_name['C2GSWithdrawOneGrid'] = _C2GSWITHDRAWONEGRID
DESCRIPTOR.message_types_by_name['C2GSUnlockGrid'] = _C2GSUNLOCKGRID
DESCRIPTOR.message_types_by_name['C2GSBuySellItem'] = _C2GSBUYSELLITEM
DESCRIPTOR.message_types_by_name['C2GSSellItemDetail'] = _C2GSSELLITEMDETAIL
DESCRIPTOR.message_types_by_name['C2GSOpenStall'] = _C2GSOPENSTALL
DESCRIPTOR.message_types_by_name['C2GSOpenCatalog'] = _C2GSOPENCATALOG
DESCRIPTOR.message_types_by_name['C2GSRefreshCatalog'] = _C2GSREFRESHCATALOG
DESCRIPTOR.message_types_by_name['C2GSGetDefaultPrice'] = _C2GSGETDEFAULTPRICE

C2GSAddSellItem = _reflection.GeneratedProtocolMessageType('C2GSAddSellItem', (_message.Message,), dict(
  DESCRIPTOR = _C2GSADDSELLITEM,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSAddSellItem)
  ))
_sym_db.RegisterMessage(C2GSAddSellItem)

SellItem = _reflection.GeneratedProtocolMessageType('SellItem', (_message.Message,), dict(
  DESCRIPTOR = _SELLITEM,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:SellItem)
  ))
_sym_db.RegisterMessage(SellItem)

C2GSAddSellItemList = _reflection.GeneratedProtocolMessageType('C2GSAddSellItemList', (_message.Message,), dict(
  DESCRIPTOR = _C2GSADDSELLITEMLIST,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSAddSellItemList)
  ))
_sym_db.RegisterMessage(C2GSAddSellItemList)

C2GSAddOverTimeItem = _reflection.GeneratedProtocolMessageType('C2GSAddOverTimeItem', (_message.Message,), dict(
  DESCRIPTOR = _C2GSADDOVERTIMEITEM,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSAddOverTimeItem)
  ))
_sym_db.RegisterMessage(C2GSAddOverTimeItem)

C2GSResetItemPrice = _reflection.GeneratedProtocolMessageType('C2GSResetItemPrice', (_message.Message,), dict(
  DESCRIPTOR = _C2GSRESETITEMPRICE,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSResetItemPrice)
  ))
_sym_db.RegisterMessage(C2GSResetItemPrice)

PriceUnit = _reflection.GeneratedProtocolMessageType('PriceUnit', (_message.Message,), dict(
  DESCRIPTOR = _PRICEUNIT,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:PriceUnit)
  ))
_sym_db.RegisterMessage(PriceUnit)

C2GSResetItemListPrice = _reflection.GeneratedProtocolMessageType('C2GSResetItemListPrice', (_message.Message,), dict(
  DESCRIPTOR = _C2GSRESETITEMLISTPRICE,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSResetItemListPrice)
  ))
_sym_db.RegisterMessage(C2GSResetItemListPrice)

C2GSRemoveSellItem = _reflection.GeneratedProtocolMessageType('C2GSRemoveSellItem', (_message.Message,), dict(
  DESCRIPTOR = _C2GSREMOVESELLITEM,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSRemoveSellItem)
  ))
_sym_db.RegisterMessage(C2GSRemoveSellItem)

C2GSWithdrawAllCash = _reflection.GeneratedProtocolMessageType('C2GSWithdrawAllCash', (_message.Message,), dict(
  DESCRIPTOR = _C2GSWITHDRAWALLCASH,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSWithdrawAllCash)
  ))
_sym_db.RegisterMessage(C2GSWithdrawAllCash)

C2GSWithdrawOneGrid = _reflection.GeneratedProtocolMessageType('C2GSWithdrawOneGrid', (_message.Message,), dict(
  DESCRIPTOR = _C2GSWITHDRAWONEGRID,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSWithdrawOneGrid)
  ))
_sym_db.RegisterMessage(C2GSWithdrawOneGrid)

C2GSUnlockGrid = _reflection.GeneratedProtocolMessageType('C2GSUnlockGrid', (_message.Message,), dict(
  DESCRIPTOR = _C2GSUNLOCKGRID,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSUnlockGrid)
  ))
_sym_db.RegisterMessage(C2GSUnlockGrid)

C2GSBuySellItem = _reflection.GeneratedProtocolMessageType('C2GSBuySellItem', (_message.Message,), dict(
  DESCRIPTOR = _C2GSBUYSELLITEM,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSBuySellItem)
  ))
_sym_db.RegisterMessage(C2GSBuySellItem)

C2GSSellItemDetail = _reflection.GeneratedProtocolMessageType('C2GSSellItemDetail', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSELLITEMDETAIL,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSellItemDetail)
  ))
_sym_db.RegisterMessage(C2GSSellItemDetail)

C2GSOpenStall = _reflection.GeneratedProtocolMessageType('C2GSOpenStall', (_message.Message,), dict(
  DESCRIPTOR = _C2GSOPENSTALL,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSOpenStall)
  ))
_sym_db.RegisterMessage(C2GSOpenStall)

C2GSOpenCatalog = _reflection.GeneratedProtocolMessageType('C2GSOpenCatalog', (_message.Message,), dict(
  DESCRIPTOR = _C2GSOPENCATALOG,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSOpenCatalog)
  ))
_sym_db.RegisterMessage(C2GSOpenCatalog)

C2GSRefreshCatalog = _reflection.GeneratedProtocolMessageType('C2GSRefreshCatalog', (_message.Message,), dict(
  DESCRIPTOR = _C2GSREFRESHCATALOG,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSRefreshCatalog)
  ))
_sym_db.RegisterMessage(C2GSRefreshCatalog)

C2GSGetDefaultPrice = _reflection.GeneratedProtocolMessageType('C2GSGetDefaultPrice', (_message.Message,), dict(
  DESCRIPTOR = _C2GSGETDEFAULTPRICE,
  __module__ = 'stall_pb2'
  # @@protoc_insertion_point(class_scope:C2GSGetDefaultPrice)
  ))
_sym_db.RegisterMessage(C2GSGetDefaultPrice)


# @@protoc_insertion_point(module_scope)
