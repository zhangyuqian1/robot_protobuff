# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: other.proto

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
  name='other.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bother.proto\x1a\x11\x62\x61se/common.proto\"\x1d\n\rGS2CHeartBeat\x12\x0c\n\x04time\x18\x01 \x01(\r\"\x1c\n\rGS2CGMMessage\x12\x0b\n\x03msg\x18\x01 \x01(\t\"i\n\x0fSummonCountInfo\x12\x0b\n\x03sid\x18\x01 \x01(\r\x12\r\n\x05sname\x18\x02 \x01(\t\x12\r\n\x05stype\x18\x03 \x01(\t\x12\x0b\n\x03num\x18\x04 \x01(\r\x12\x0f\n\x07percent\x18\x05 \x01(\x02\x12\r\n\x05\x63\x61rry\x18\x06 \x01(\r\"\x84\x01\n\x0fGS2CSummonCount\x12\x0c\n\x04sid1\x18\x01 \x01(\r\x12\x0c\n\x04sid2\x18\x02 \x01(\r\x12\x0b\n\x03\x63nt\x18\x03 \x01(\r\x12\"\n\x08infolist\x18\x04 \x03(\x0b\x32\x10.SummonCountInfo\x12\x11\n\tbypercent\x18\x05 \x01(\x02\x12\x11\n\txypercent\x18\x06 \x01(\x02\"\x19\n\nGS2COnline\x12\x0b\n\x03pid\x18\x01 \x01(\r\"\x1a\n\x0bGS2COffline\x12\x0b\n\x03pid\x18\x01 \x01(\r\"I\n\rGS2CBigPacket\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\r\n\x05total\x18\x02 \x01(\r\x12\r\n\x05index\x18\x03 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"$\n\x14GS2CClientUpdateCode\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"(\n\x15GS2COpSessionResponse\x12\x0f\n\x07session\x18\x01 \x01(\t\"/\n\x0cGS2CQRCToken\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08validity\x18\x02 \x01(\r\"\x14\n\x12GS2CQRCScanSuccess\"A\n\x12GS2CQRCAccountInfo\x12\x14\n\x0c\x61\x63\x63ount_info\x18\x01 \x01(\x0c\x12\x15\n\rtransfer_info\x18\x02 \x01(\x0c\"\x10\n\x0eGS2CQRCInvalid\"y\n\x0bGS2CPayInfo\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x13\n\x0bproduct_key\x18\x02 \x01(\t\x12\x16\n\x0eproduct_amount\x18\x03 \x01(\r\x12\x15\n\rproduct_value\x18\x04 \x01(\r\x12\x14\n\x0c\x63\x61llback_url\x18\x05 \x01(\t\"(\n\x0cGoldCoinUnit\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0b\n\x03val\x18\x02 \x01(\r\":\n\x12GS2CPayForGoldInfo\x12$\n\rgoldcoin_list\x18\x01 \x03(\x0b\x32\r.GoldCoinUnit\"6\n\x17GS2CRefreshGoldCoinUnit\x12\x1b\n\x04unit\x18\x01 \x01(\x0b\x32\r.GoldCoinUnit\"&\n\rGS2CQrpayScan\x12\x15\n\rtransfer_info\x18\x01 \x01(\x0c\"\"\n\x0fGS2CMergePacket\x12\x0f\n\x07packets\x18\x01 \x03(\x0c\"=\n\x1aGS2CClientUpdateResVersion\x12\x10\n\x08res_file\x18\x01 \x03(\t\x12\r\n\x05\x64\x65lay\x18\x02 \x01(\r\"X\n\x13GS2CClientUpdateRes\x12,\n\x08res_file\x18\x01 \x03(\x0b\x32\x1a.base.ClientResFileContent\x12\x13\n\x0b\x64\x65lete_file\x18\x02 \x03(\t\"*\n\x13GS2CShowInstruction\x12\x13\n\x0binstruction\x18\x01 \x01(\r\"u\n\x10\x46\x65\x65\x64\x42\x61\x63kQuestion\x12\x13\n\x0bquestion_id\x18\x01 \x01(\r\x12\x10\n\x08question\x18\x02 \x01(\t\x12\x15\n\rquestion_time\x18\x03 \x01(\r\x12\x0e\n\x06\x61nswer\x18\x04 \x01(\t\x12\x13\n\x0b\x61nswer_time\x18\x05 \x01(\r\"W\n\x16GS2CFeedBackAnswerList\x12(\n\rquestion_list\x18\x01 \x03(\x0b\x32\x11.FeedBackQuestion\x12\x13\n\x0b\x63heck_state\x18\x02 \x01(\r')
  ,
  dependencies=[base_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GS2CHEARTBEAT = _descriptor.Descriptor(
  name='GS2CHeartBeat',
  full_name='GS2CHeartBeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='GS2CHeartBeat.time', index=0,
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
  serialized_start=34,
  serialized_end=63,
)


_GS2CGMMESSAGE = _descriptor.Descriptor(
  name='GS2CGMMessage',
  full_name='GS2CGMMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='GS2CGMMessage.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=93,
)


_SUMMONCOUNTINFO = _descriptor.Descriptor(
  name='SummonCountInfo',
  full_name='SummonCountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid', full_name='SummonCountInfo.sid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sname', full_name='SummonCountInfo.sname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stype', full_name='SummonCountInfo.stype', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='SummonCountInfo.num', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='percent', full_name='SummonCountInfo.percent', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='carry', full_name='SummonCountInfo.carry', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=95,
  serialized_end=200,
)


_GS2CSUMMONCOUNT = _descriptor.Descriptor(
  name='GS2CSummonCount',
  full_name='GS2CSummonCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sid1', full_name='GS2CSummonCount.sid1', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sid2', full_name='GS2CSummonCount.sid2', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cnt', full_name='GS2CSummonCount.cnt', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='infolist', full_name='GS2CSummonCount.infolist', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bypercent', full_name='GS2CSummonCount.bypercent', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xypercent', full_name='GS2CSummonCount.xypercent', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=203,
  serialized_end=335,
)


_GS2CONLINE = _descriptor.Descriptor(
  name='GS2COnline',
  full_name='GS2COnline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2COnline.pid', index=0,
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
  serialized_start=337,
  serialized_end=362,
)


_GS2COFFLINE = _descriptor.Descriptor(
  name='GS2COffline',
  full_name='GS2COffline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2COffline.pid', index=0,
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
  serialized_start=364,
  serialized_end=390,
)


_GS2CBIGPACKET = _descriptor.Descriptor(
  name='GS2CBigPacket',
  full_name='GS2CBigPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GS2CBigPacket.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total', full_name='GS2CBigPacket.total', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='GS2CBigPacket.index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='GS2CBigPacket.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=392,
  serialized_end=465,
)


_GS2CCLIENTUPDATECODE = _descriptor.Descriptor(
  name='GS2CClientUpdateCode',
  full_name='GS2CClientUpdateCode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='GS2CClientUpdateCode.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=467,
  serialized_end=503,
)


_GS2COPSESSIONRESPONSE = _descriptor.Descriptor(
  name='GS2COpSessionResponse',
  full_name='GS2COpSessionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='GS2COpSessionResponse.session', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=505,
  serialized_end=545,
)


_GS2CQRCTOKEN = _descriptor.Descriptor(
  name='GS2CQRCToken',
  full_name='GS2CQRCToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='GS2CQRCToken.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validity', full_name='GS2CQRCToken.validity', index=1,
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
  serialized_start=547,
  serialized_end=594,
)


_GS2CQRCSCANSUCCESS = _descriptor.Descriptor(
  name='GS2CQRCScanSuccess',
  full_name='GS2CQRCScanSuccess',
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
  serialized_start=596,
  serialized_end=616,
)


_GS2CQRCACCOUNTINFO = _descriptor.Descriptor(
  name='GS2CQRCAccountInfo',
  full_name='GS2CQRCAccountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_info', full_name='GS2CQRCAccountInfo.account_info', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transfer_info', full_name='GS2CQRCAccountInfo.transfer_info', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=618,
  serialized_end=683,
)


_GS2CQRCINVALID = _descriptor.Descriptor(
  name='GS2CQRCInvalid',
  full_name='GS2CQRCInvalid',
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
  serialized_start=685,
  serialized_end=701,
)


_GS2CPAYINFO = _descriptor.Descriptor(
  name='GS2CPayInfo',
  full_name='GS2CPayInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='GS2CPayInfo.order_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_key', full_name='GS2CPayInfo.product_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_amount', full_name='GS2CPayInfo.product_amount', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_value', full_name='GS2CPayInfo.product_value', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='callback_url', full_name='GS2CPayInfo.callback_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=703,
  serialized_end=824,
)


_GOLDCOINUNIT = _descriptor.Descriptor(
  name='GoldCoinUnit',
  full_name='GoldCoinUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='GoldCoinUnit.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val', full_name='GoldCoinUnit.val', index=1,
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
  serialized_start=826,
  serialized_end=866,
)


_GS2CPAYFORGOLDINFO = _descriptor.Descriptor(
  name='GS2CPayForGoldInfo',
  full_name='GS2CPayForGoldInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='goldcoin_list', full_name='GS2CPayForGoldInfo.goldcoin_list', index=0,
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
  serialized_start=868,
  serialized_end=926,
)


_GS2CREFRESHGOLDCOINUNIT = _descriptor.Descriptor(
  name='GS2CRefreshGoldCoinUnit',
  full_name='GS2CRefreshGoldCoinUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit', full_name='GS2CRefreshGoldCoinUnit.unit', index=0,
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
  serialized_start=928,
  serialized_end=982,
)


_GS2CQRPAYSCAN = _descriptor.Descriptor(
  name='GS2CQrpayScan',
  full_name='GS2CQrpayScan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transfer_info', full_name='GS2CQrpayScan.transfer_info', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=984,
  serialized_end=1022,
)


_GS2CMERGEPACKET = _descriptor.Descriptor(
  name='GS2CMergePacket',
  full_name='GS2CMergePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='packets', full_name='GS2CMergePacket.packets', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=1024,
  serialized_end=1058,
)


_GS2CCLIENTUPDATERESVERSION = _descriptor.Descriptor(
  name='GS2CClientUpdateResVersion',
  full_name='GS2CClientUpdateResVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res_file', full_name='GS2CClientUpdateResVersion.res_file', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delay', full_name='GS2CClientUpdateResVersion.delay', index=1,
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
  serialized_start=1060,
  serialized_end=1121,
)


_GS2CCLIENTUPDATERES = _descriptor.Descriptor(
  name='GS2CClientUpdateRes',
  full_name='GS2CClientUpdateRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res_file', full_name='GS2CClientUpdateRes.res_file', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_file', full_name='GS2CClientUpdateRes.delete_file', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=1123,
  serialized_end=1211,
)


_GS2CSHOWINSTRUCTION = _descriptor.Descriptor(
  name='GS2CShowInstruction',
  full_name='GS2CShowInstruction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instruction', full_name='GS2CShowInstruction.instruction', index=0,
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
  serialized_start=1213,
  serialized_end=1255,
)


_FEEDBACKQUESTION = _descriptor.Descriptor(
  name='FeedBackQuestion',
  full_name='FeedBackQuestion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question_id', full_name='FeedBackQuestion.question_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='question', full_name='FeedBackQuestion.question', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='question_time', full_name='FeedBackQuestion.question_time', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='FeedBackQuestion.answer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer_time', full_name='FeedBackQuestion.answer_time', index=4,
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
  serialized_start=1257,
  serialized_end=1374,
)


_GS2CFEEDBACKANSWERLIST = _descriptor.Descriptor(
  name='GS2CFeedBackAnswerList',
  full_name='GS2CFeedBackAnswerList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question_list', full_name='GS2CFeedBackAnswerList.question_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='check_state', full_name='GS2CFeedBackAnswerList.check_state', index=1,
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
  serialized_start=1376,
  serialized_end=1463,
)

_GS2CSUMMONCOUNT.fields_by_name['infolist'].message_type = _SUMMONCOUNTINFO
_GS2CPAYFORGOLDINFO.fields_by_name['goldcoin_list'].message_type = _GOLDCOINUNIT
_GS2CREFRESHGOLDCOINUNIT.fields_by_name['unit'].message_type = _GOLDCOINUNIT
_GS2CCLIENTUPDATERES.fields_by_name['res_file'].message_type = base_dot_common__pb2._CLIENTRESFILECONTENT
_GS2CFEEDBACKANSWERLIST.fields_by_name['question_list'].message_type = _FEEDBACKQUESTION
DESCRIPTOR.message_types_by_name['GS2CHeartBeat'] = _GS2CHEARTBEAT
DESCRIPTOR.message_types_by_name['GS2CGMMessage'] = _GS2CGMMESSAGE
DESCRIPTOR.message_types_by_name['SummonCountInfo'] = _SUMMONCOUNTINFO
DESCRIPTOR.message_types_by_name['GS2CSummonCount'] = _GS2CSUMMONCOUNT
DESCRIPTOR.message_types_by_name['GS2COnline'] = _GS2CONLINE
DESCRIPTOR.message_types_by_name['GS2COffline'] = _GS2COFFLINE
DESCRIPTOR.message_types_by_name['GS2CBigPacket'] = _GS2CBIGPACKET
DESCRIPTOR.message_types_by_name['GS2CClientUpdateCode'] = _GS2CCLIENTUPDATECODE
DESCRIPTOR.message_types_by_name['GS2COpSessionResponse'] = _GS2COPSESSIONRESPONSE
DESCRIPTOR.message_types_by_name['GS2CQRCToken'] = _GS2CQRCTOKEN
DESCRIPTOR.message_types_by_name['GS2CQRCScanSuccess'] = _GS2CQRCSCANSUCCESS
DESCRIPTOR.message_types_by_name['GS2CQRCAccountInfo'] = _GS2CQRCACCOUNTINFO
DESCRIPTOR.message_types_by_name['GS2CQRCInvalid'] = _GS2CQRCINVALID
DESCRIPTOR.message_types_by_name['GS2CPayInfo'] = _GS2CPAYINFO
DESCRIPTOR.message_types_by_name['GoldCoinUnit'] = _GOLDCOINUNIT
DESCRIPTOR.message_types_by_name['GS2CPayForGoldInfo'] = _GS2CPAYFORGOLDINFO
DESCRIPTOR.message_types_by_name['GS2CRefreshGoldCoinUnit'] = _GS2CREFRESHGOLDCOINUNIT
DESCRIPTOR.message_types_by_name['GS2CQrpayScan'] = _GS2CQRPAYSCAN
DESCRIPTOR.message_types_by_name['GS2CMergePacket'] = _GS2CMERGEPACKET
DESCRIPTOR.message_types_by_name['GS2CClientUpdateResVersion'] = _GS2CCLIENTUPDATERESVERSION
DESCRIPTOR.message_types_by_name['GS2CClientUpdateRes'] = _GS2CCLIENTUPDATERES
DESCRIPTOR.message_types_by_name['GS2CShowInstruction'] = _GS2CSHOWINSTRUCTION
DESCRIPTOR.message_types_by_name['FeedBackQuestion'] = _FEEDBACKQUESTION
DESCRIPTOR.message_types_by_name['GS2CFeedBackAnswerList'] = _GS2CFEEDBACKANSWERLIST

GS2CHeartBeat = _reflection.GeneratedProtocolMessageType('GS2CHeartBeat', (_message.Message,), dict(
  DESCRIPTOR = _GS2CHEARTBEAT,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CHeartBeat)
  ))
_sym_db.RegisterMessage(GS2CHeartBeat)

GS2CGMMessage = _reflection.GeneratedProtocolMessageType('GS2CGMMessage', (_message.Message,), dict(
  DESCRIPTOR = _GS2CGMMESSAGE,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CGMMessage)
  ))
_sym_db.RegisterMessage(GS2CGMMessage)

SummonCountInfo = _reflection.GeneratedProtocolMessageType('SummonCountInfo', (_message.Message,), dict(
  DESCRIPTOR = _SUMMONCOUNTINFO,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:SummonCountInfo)
  ))
_sym_db.RegisterMessage(SummonCountInfo)

GS2CSummonCount = _reflection.GeneratedProtocolMessageType('GS2CSummonCount', (_message.Message,), dict(
  DESCRIPTOR = _GS2CSUMMONCOUNT,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CSummonCount)
  ))
_sym_db.RegisterMessage(GS2CSummonCount)

GS2COnline = _reflection.GeneratedProtocolMessageType('GS2COnline', (_message.Message,), dict(
  DESCRIPTOR = _GS2CONLINE,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2COnline)
  ))
_sym_db.RegisterMessage(GS2COnline)

GS2COffline = _reflection.GeneratedProtocolMessageType('GS2COffline', (_message.Message,), dict(
  DESCRIPTOR = _GS2COFFLINE,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2COffline)
  ))
_sym_db.RegisterMessage(GS2COffline)

GS2CBigPacket = _reflection.GeneratedProtocolMessageType('GS2CBigPacket', (_message.Message,), dict(
  DESCRIPTOR = _GS2CBIGPACKET,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CBigPacket)
  ))
_sym_db.RegisterMessage(GS2CBigPacket)

GS2CClientUpdateCode = _reflection.GeneratedProtocolMessageType('GS2CClientUpdateCode', (_message.Message,), dict(
  DESCRIPTOR = _GS2CCLIENTUPDATECODE,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CClientUpdateCode)
  ))
_sym_db.RegisterMessage(GS2CClientUpdateCode)

GS2COpSessionResponse = _reflection.GeneratedProtocolMessageType('GS2COpSessionResponse', (_message.Message,), dict(
  DESCRIPTOR = _GS2COPSESSIONRESPONSE,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2COpSessionResponse)
  ))
_sym_db.RegisterMessage(GS2COpSessionResponse)

GS2CQRCToken = _reflection.GeneratedProtocolMessageType('GS2CQRCToken', (_message.Message,), dict(
  DESCRIPTOR = _GS2CQRCTOKEN,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CQRCToken)
  ))
_sym_db.RegisterMessage(GS2CQRCToken)

GS2CQRCScanSuccess = _reflection.GeneratedProtocolMessageType('GS2CQRCScanSuccess', (_message.Message,), dict(
  DESCRIPTOR = _GS2CQRCSCANSUCCESS,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CQRCScanSuccess)
  ))
_sym_db.RegisterMessage(GS2CQRCScanSuccess)

GS2CQRCAccountInfo = _reflection.GeneratedProtocolMessageType('GS2CQRCAccountInfo', (_message.Message,), dict(
  DESCRIPTOR = _GS2CQRCACCOUNTINFO,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CQRCAccountInfo)
  ))
_sym_db.RegisterMessage(GS2CQRCAccountInfo)

GS2CQRCInvalid = _reflection.GeneratedProtocolMessageType('GS2CQRCInvalid', (_message.Message,), dict(
  DESCRIPTOR = _GS2CQRCINVALID,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CQRCInvalid)
  ))
_sym_db.RegisterMessage(GS2CQRCInvalid)

GS2CPayInfo = _reflection.GeneratedProtocolMessageType('GS2CPayInfo', (_message.Message,), dict(
  DESCRIPTOR = _GS2CPAYINFO,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CPayInfo)
  ))
_sym_db.RegisterMessage(GS2CPayInfo)

GoldCoinUnit = _reflection.GeneratedProtocolMessageType('GoldCoinUnit', (_message.Message,), dict(
  DESCRIPTOR = _GOLDCOINUNIT,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GoldCoinUnit)
  ))
_sym_db.RegisterMessage(GoldCoinUnit)

GS2CPayForGoldInfo = _reflection.GeneratedProtocolMessageType('GS2CPayForGoldInfo', (_message.Message,), dict(
  DESCRIPTOR = _GS2CPAYFORGOLDINFO,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CPayForGoldInfo)
  ))
_sym_db.RegisterMessage(GS2CPayForGoldInfo)

GS2CRefreshGoldCoinUnit = _reflection.GeneratedProtocolMessageType('GS2CRefreshGoldCoinUnit', (_message.Message,), dict(
  DESCRIPTOR = _GS2CREFRESHGOLDCOINUNIT,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CRefreshGoldCoinUnit)
  ))
_sym_db.RegisterMessage(GS2CRefreshGoldCoinUnit)

GS2CQrpayScan = _reflection.GeneratedProtocolMessageType('GS2CQrpayScan', (_message.Message,), dict(
  DESCRIPTOR = _GS2CQRPAYSCAN,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CQrpayScan)
  ))
_sym_db.RegisterMessage(GS2CQrpayScan)

GS2CMergePacket = _reflection.GeneratedProtocolMessageType('GS2CMergePacket', (_message.Message,), dict(
  DESCRIPTOR = _GS2CMERGEPACKET,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CMergePacket)
  ))
_sym_db.RegisterMessage(GS2CMergePacket)

GS2CClientUpdateResVersion = _reflection.GeneratedProtocolMessageType('GS2CClientUpdateResVersion', (_message.Message,), dict(
  DESCRIPTOR = _GS2CCLIENTUPDATERESVERSION,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CClientUpdateResVersion)
  ))
_sym_db.RegisterMessage(GS2CClientUpdateResVersion)

GS2CClientUpdateRes = _reflection.GeneratedProtocolMessageType('GS2CClientUpdateRes', (_message.Message,), dict(
  DESCRIPTOR = _GS2CCLIENTUPDATERES,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CClientUpdateRes)
  ))
_sym_db.RegisterMessage(GS2CClientUpdateRes)

GS2CShowInstruction = _reflection.GeneratedProtocolMessageType('GS2CShowInstruction', (_message.Message,), dict(
  DESCRIPTOR = _GS2CSHOWINSTRUCTION,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CShowInstruction)
  ))
_sym_db.RegisterMessage(GS2CShowInstruction)

FeedBackQuestion = _reflection.GeneratedProtocolMessageType('FeedBackQuestion', (_message.Message,), dict(
  DESCRIPTOR = _FEEDBACKQUESTION,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:FeedBackQuestion)
  ))
_sym_db.RegisterMessage(FeedBackQuestion)

GS2CFeedBackAnswerList = _reflection.GeneratedProtocolMessageType('GS2CFeedBackAnswerList', (_message.Message,), dict(
  DESCRIPTOR = _GS2CFEEDBACKANSWERLIST,
  __module__ = 'other_pb2'
  # @@protoc_insertion_point(class_scope:GS2CFeedBackAnswerList)
  ))
_sym_db.RegisterMessage(GS2CFeedBackAnswerList)


# @@protoc_insertion_point(module_scope)
