# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: newbieguide.proto

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
  name='newbieguide.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x11newbieguide.proto\x1a\x11\x62\x61se/common.proto\")\n\x16\x43\x32GSNewSysOpenNotified\x12\x0f\n\x07sys_ids\x18\x01 \x03(\t\"c\n\x19\x43\x32GSUpdateNewbieGuideInfo\x12\x0c\n\x04mask\x18\x01 \x01(\t\x12(\n\x0bguide_links\x18\x02 \x03(\x0b\x32\x13.base.GuideLinkInfo\x12\x0e\n\x06\x65xdata\x18\x03 \x01(\t\"+\n\x16\x43\x32GSSelectNewbieSummon\x12\x11\n\tselection\x18\x01 \x01(\r\"\x18\n\x16\x43\x32GSGetNewbieGuildInfo')
  ,
  dependencies=[base_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2GSNEWSYSOPENNOTIFIED = _descriptor.Descriptor(
  name='C2GSNewSysOpenNotified',
  full_name='C2GSNewSysOpenNotified',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sys_ids', full_name='C2GSNewSysOpenNotified.sys_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=40,
  serialized_end=81,
)


_C2GSUPDATENEWBIEGUIDEINFO = _descriptor.Descriptor(
  name='C2GSUpdateNewbieGuideInfo',
  full_name='C2GSUpdateNewbieGuideInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mask', full_name='C2GSUpdateNewbieGuideInfo.mask', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guide_links', full_name='C2GSUpdateNewbieGuideInfo.guide_links', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exdata', full_name='C2GSUpdateNewbieGuideInfo.exdata', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=83,
  serialized_end=182,
)


_C2GSSELECTNEWBIESUMMON = _descriptor.Descriptor(
  name='C2GSSelectNewbieSummon',
  full_name='C2GSSelectNewbieSummon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='selection', full_name='C2GSSelectNewbieSummon.selection', index=0,
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
  serialized_start=184,
  serialized_end=227,
)


_C2GSGETNEWBIEGUILDINFO = _descriptor.Descriptor(
  name='C2GSGetNewbieGuildInfo',
  full_name='C2GSGetNewbieGuildInfo',
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
  serialized_start=229,
  serialized_end=253,
)

_C2GSUPDATENEWBIEGUIDEINFO.fields_by_name['guide_links'].message_type = base_dot_common__pb2._GUIDELINKINFO
DESCRIPTOR.message_types_by_name['C2GSNewSysOpenNotified'] = _C2GSNEWSYSOPENNOTIFIED
DESCRIPTOR.message_types_by_name['C2GSUpdateNewbieGuideInfo'] = _C2GSUPDATENEWBIEGUIDEINFO
DESCRIPTOR.message_types_by_name['C2GSSelectNewbieSummon'] = _C2GSSELECTNEWBIESUMMON
DESCRIPTOR.message_types_by_name['C2GSGetNewbieGuildInfo'] = _C2GSGETNEWBIEGUILDINFO

C2GSNewSysOpenNotified = _reflection.GeneratedProtocolMessageType('C2GSNewSysOpenNotified', (_message.Message,), dict(
  DESCRIPTOR = _C2GSNEWSYSOPENNOTIFIED,
  __module__ = 'newbieguide_pb2'
  # @@protoc_insertion_point(class_scope:C2GSNewSysOpenNotified)
  ))
_sym_db.RegisterMessage(C2GSNewSysOpenNotified)

C2GSUpdateNewbieGuideInfo = _reflection.GeneratedProtocolMessageType('C2GSUpdateNewbieGuideInfo', (_message.Message,), dict(
  DESCRIPTOR = _C2GSUPDATENEWBIEGUIDEINFO,
  __module__ = 'newbieguide_pb2'
  # @@protoc_insertion_point(class_scope:C2GSUpdateNewbieGuideInfo)
  ))
_sym_db.RegisterMessage(C2GSUpdateNewbieGuideInfo)

C2GSSelectNewbieSummon = _reflection.GeneratedProtocolMessageType('C2GSSelectNewbieSummon', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSELECTNEWBIESUMMON,
  __module__ = 'newbieguide_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSelectNewbieSummon)
  ))
_sym_db.RegisterMessage(C2GSSelectNewbieSummon)

C2GSGetNewbieGuildInfo = _reflection.GeneratedProtocolMessageType('C2GSGetNewbieGuildInfo', (_message.Message,), dict(
  DESCRIPTOR = _C2GSGETNEWBIEGUILDINFO,
  __module__ = 'newbieguide_pb2'
  # @@protoc_insertion_point(class_scope:C2GSGetNewbieGuildInfo)
  ))
_sym_db.RegisterMessage(C2GSGetNewbieGuildInfo)


# @@protoc_insertion_point(module_scope)
