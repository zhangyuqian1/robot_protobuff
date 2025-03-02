# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: auction.proto

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
  name='auction.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\rauction.proto\x1a\x11\x62\x61se/common.proto\"\x92\x02\n\x08SellUnit\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\x0b\n\x03sid\x18\x03 \x01(\r\x12\r\n\x05price\x18\x04 \x01(\r\x12\x12\n\nmoney_type\x18\x05 \x01(\r\x12\x0e\n\x06\x62idder\x18\x06 \x01(\r\x12\x11\n\tshow_time\x18\x07 \x01(\r\x12\x12\n\nprice_time\x18\x08 \x01(\r\x12\x11\n\tis_follow\x18\t \x01(\r\x12\x14\n\x0cproxy_bidder\x18\n \x01(\r\x12\x13\n\x0bproxy_price\x18\x0b \x01(\r\x12\x11\n\tview_time\x18\x0c \x01(\r\x12\x0f\n\x07sys_idx\x18\r \x01(\r\x12\x0f\n\x07quality\x18\x0e \x01(\r\x12\x12\n\nbase_price\x18\x0f \x01(\r\"l\n\x0fGS2COpenAuction\x12\x0e\n\x06\x63\x61t_id\x18\x01 \x01(\r\x12\x0e\n\x06sub_id\x18\x02 \x01(\r\x12\x1c\n\tsell_list\x18\x03 \x03(\x0b\x32\t.SellUnit\x12\r\n\x05total\x18\x04 \x01(\r\x12\x0c\n\x04page\x18\x05 \x01(\r\".\n\x13GS2CRefreshSellUnit\x12\x17\n\x04unit\x18\x01 \x01(\x0b\x32\t.SellUnit\"\x89\x01\n\x0cGS2CShowLink\x12\x0e\n\x06\x63\x61t_id\x18\x01 \x01(\r\x12\x0e\n\x06sub_id\x18\x02 \x01(\r\x12\x1c\n\tsell_list\x18\x03 \x03(\x0b\x32\t.SellUnit\x12\r\n\x05total\x18\x04 \x01(\r\x12\x0c\n\x04page\x18\x05 \x01(\r\x12\x0e\n\x06status\x18\x06 \x01(\r\x12\x0e\n\x06target\x18\x07 \x01(\r\"W\n\x16GS2CAuctionPriceChange\x12\n\n\x02id\x18\x01 \x01(\r\x12\r\n\x05price\x18\x02 \x01(\r\x12\x12\n\nprice_time\x18\x03 \x01(\r\x12\x0e\n\x06\x62idder\x18\x04 \x01(\r\"u\n\x11GS2CAuctionDetail\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\r\x12 \n\x08itemdata\x18\x03 \x01(\x0b\x32\x0e.base.ItemInfo\x12$\n\nsummondata\x18\x04 \x01(\x0b\x32\x10.base.SummonInfo')
  ,
  dependencies=[base_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SELLUNIT = _descriptor.Descriptor(
  name='SellUnit',
  full_name='SellUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SellUnit.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='SellUnit.type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sid', full_name='SellUnit.sid', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='SellUnit.price', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='money_type', full_name='SellUnit.money_type', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidder', full_name='SellUnit.bidder', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='show_time', full_name='SellUnit.show_time', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_time', full_name='SellUnit.price_time', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_follow', full_name='SellUnit.is_follow', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy_bidder', full_name='SellUnit.proxy_bidder', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proxy_price', full_name='SellUnit.proxy_price', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='view_time', full_name='SellUnit.view_time', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sys_idx', full_name='SellUnit.sys_idx', index=12,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quality', full_name='SellUnit.quality', index=13,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_price', full_name='SellUnit.base_price', index=14,
      number=15, type=13, cpp_type=3, label=1,
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
  serialized_start=37,
  serialized_end=311,
)


_GS2COPENAUCTION = _descriptor.Descriptor(
  name='GS2COpenAuction',
  full_name='GS2COpenAuction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cat_id', full_name='GS2COpenAuction.cat_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_id', full_name='GS2COpenAuction.sub_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sell_list', full_name='GS2COpenAuction.sell_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total', full_name='GS2COpenAuction.total', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page', full_name='GS2COpenAuction.page', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=313,
  serialized_end=421,
)


_GS2CREFRESHSELLUNIT = _descriptor.Descriptor(
  name='GS2CRefreshSellUnit',
  full_name='GS2CRefreshSellUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit', full_name='GS2CRefreshSellUnit.unit', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=423,
  serialized_end=469,
)


_GS2CSHOWLINK = _descriptor.Descriptor(
  name='GS2CShowLink',
  full_name='GS2CShowLink',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cat_id', full_name='GS2CShowLink.cat_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_id', full_name='GS2CShowLink.sub_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sell_list', full_name='GS2CShowLink.sell_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total', full_name='GS2CShowLink.total', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page', full_name='GS2CShowLink.page', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='GS2CShowLink.status', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='GS2CShowLink.target', index=6,
      number=7, type=13, cpp_type=3, label=1,
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
  serialized_start=472,
  serialized_end=609,
)


_GS2CAUCTIONPRICECHANGE = _descriptor.Descriptor(
  name='GS2CAuctionPriceChange',
  full_name='GS2CAuctionPriceChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GS2CAuctionPriceChange.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='GS2CAuctionPriceChange.price', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_time', full_name='GS2CAuctionPriceChange.price_time', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidder', full_name='GS2CAuctionPriceChange.bidder', index=3,
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
  serialized_start=611,
  serialized_end=698,
)


_GS2CAUCTIONDETAIL = _descriptor.Descriptor(
  name='GS2CAuctionDetail',
  full_name='GS2CAuctionDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GS2CAuctionDetail.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='GS2CAuctionDetail.type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemdata', full_name='GS2CAuctionDetail.itemdata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summondata', full_name='GS2CAuctionDetail.summondata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=700,
  serialized_end=817,
)

_GS2COPENAUCTION.fields_by_name['sell_list'].message_type = _SELLUNIT
_GS2CREFRESHSELLUNIT.fields_by_name['unit'].message_type = _SELLUNIT
_GS2CSHOWLINK.fields_by_name['sell_list'].message_type = _SELLUNIT
_GS2CAUCTIONDETAIL.fields_by_name['itemdata'].message_type = base_dot_common__pb2._ITEMINFO
_GS2CAUCTIONDETAIL.fields_by_name['summondata'].message_type = base_dot_common__pb2._SUMMONINFO
DESCRIPTOR.message_types_by_name['SellUnit'] = _SELLUNIT
DESCRIPTOR.message_types_by_name['GS2COpenAuction'] = _GS2COPENAUCTION
DESCRIPTOR.message_types_by_name['GS2CRefreshSellUnit'] = _GS2CREFRESHSELLUNIT
DESCRIPTOR.message_types_by_name['GS2CShowLink'] = _GS2CSHOWLINK
DESCRIPTOR.message_types_by_name['GS2CAuctionPriceChange'] = _GS2CAUCTIONPRICECHANGE
DESCRIPTOR.message_types_by_name['GS2CAuctionDetail'] = _GS2CAUCTIONDETAIL

SellUnit = _reflection.GeneratedProtocolMessageType('SellUnit', (_message.Message,), dict(
  DESCRIPTOR = _SELLUNIT,
  __module__ = 'auction_pb2'
  # @@protoc_insertion_point(class_scope:SellUnit)
  ))
_sym_db.RegisterMessage(SellUnit)

GS2COpenAuction = _reflection.GeneratedProtocolMessageType('GS2COpenAuction', (_message.Message,), dict(
  DESCRIPTOR = _GS2COPENAUCTION,
  __module__ = 'auction_pb2'
  # @@protoc_insertion_point(class_scope:GS2COpenAuction)
  ))
_sym_db.RegisterMessage(GS2COpenAuction)

GS2CRefreshSellUnit = _reflection.GeneratedProtocolMessageType('GS2CRefreshSellUnit', (_message.Message,), dict(
  DESCRIPTOR = _GS2CREFRESHSELLUNIT,
  __module__ = 'auction_pb2'
  # @@protoc_insertion_point(class_scope:GS2CRefreshSellUnit)
  ))
_sym_db.RegisterMessage(GS2CRefreshSellUnit)

GS2CShowLink = _reflection.GeneratedProtocolMessageType('GS2CShowLink', (_message.Message,), dict(
  DESCRIPTOR = _GS2CSHOWLINK,
  __module__ = 'auction_pb2'
  # @@protoc_insertion_point(class_scope:GS2CShowLink)
  ))
_sym_db.RegisterMessage(GS2CShowLink)

GS2CAuctionPriceChange = _reflection.GeneratedProtocolMessageType('GS2CAuctionPriceChange', (_message.Message,), dict(
  DESCRIPTOR = _GS2CAUCTIONPRICECHANGE,
  __module__ = 'auction_pb2'
  # @@protoc_insertion_point(class_scope:GS2CAuctionPriceChange)
  ))
_sym_db.RegisterMessage(GS2CAuctionPriceChange)

GS2CAuctionDetail = _reflection.GeneratedProtocolMessageType('GS2CAuctionDetail', (_message.Message,), dict(
  DESCRIPTOR = _GS2CAUCTIONDETAIL,
  __module__ = 'auction_pb2'
  # @@protoc_insertion_point(class_scope:GS2CAuctionDetail)
  ))
_sym_db.RegisterMessage(GS2CAuctionDetail)


# @@protoc_insertion_point(module_scope)
