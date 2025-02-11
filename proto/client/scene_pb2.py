# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scene.proto

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
  name='scene.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0bscene.proto\x1a\x11\x62\x61se/common.proto\"V\n\x10\x43\x32GSSyncPosQueue\x12\x10\n\x08scene_id\x18\x01 \x01(\r\x12\x0b\n\x03\x65id\x18\x02 \x01(\r\x12#\n\x07poslist\x18\x03 \x03(\x0b\x32\x12.base.PosQueueInfo\"B\n\x0c\x43\x32GSTransfer\x12\x10\n\x08scene_id\x18\x01 \x01(\r\x12\x0b\n\x03\x65id\x18\x02 \x01(\r\x12\x13\n\x0btransfer_id\x18\x03 \x01(\r\"B\n\x11\x43\x32GSClickWorldMap\x12\x10\n\x08scene_id\x18\x01 \x01(\r\x12\x0b\n\x03\x65id\x18\x02 \x01(\r\x12\x0e\n\x06map_id\x18\x03 \x01(\r\"8\n\x14\x43\x32GSClickTrapMineMap\x12\x10\n\x08scene_id\x18\x01 \x01(\r\x12\x0e\n\x06map_id\x18\x02 \x01(\r\"$\n\x12\x43\x32GSStartWaterWalk\x12\x0e\n\x06walkid\x18\x01 \x01(\r')
  ,
  dependencies=[base_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2GSSYNCPOSQUEUE = _descriptor.Descriptor(
  name='C2GSSyncPosQueue',
  full_name='C2GSSyncPosQueue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='C2GSSyncPosQueue.scene_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eid', full_name='C2GSSyncPosQueue.eid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poslist', full_name='C2GSSyncPosQueue.poslist', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=34,
  serialized_end=120,
)


_C2GSTRANSFER = _descriptor.Descriptor(
  name='C2GSTransfer',
  full_name='C2GSTransfer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='C2GSTransfer.scene_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eid', full_name='C2GSTransfer.eid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transfer_id', full_name='C2GSTransfer.transfer_id', index=2,
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
  serialized_start=122,
  serialized_end=188,
)


_C2GSCLICKWORLDMAP = _descriptor.Descriptor(
  name='C2GSClickWorldMap',
  full_name='C2GSClickWorldMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='C2GSClickWorldMap.scene_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eid', full_name='C2GSClickWorldMap.eid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='C2GSClickWorldMap.map_id', index=2,
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
  serialized_start=190,
  serialized_end=256,
)


_C2GSCLICKTRAPMINEMAP = _descriptor.Descriptor(
  name='C2GSClickTrapMineMap',
  full_name='C2GSClickTrapMineMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='C2GSClickTrapMineMap.scene_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map_id', full_name='C2GSClickTrapMineMap.map_id', index=1,
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
  serialized_start=258,
  serialized_end=314,
)


_C2GSSTARTWATERWALK = _descriptor.Descriptor(
  name='C2GSStartWaterWalk',
  full_name='C2GSStartWaterWalk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='walkid', full_name='C2GSStartWaterWalk.walkid', index=0,
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
  serialized_start=316,
  serialized_end=352,
)

_C2GSSYNCPOSQUEUE.fields_by_name['poslist'].message_type = base_dot_common__pb2._POSQUEUEINFO
DESCRIPTOR.message_types_by_name['C2GSSyncPosQueue'] = _C2GSSYNCPOSQUEUE
DESCRIPTOR.message_types_by_name['C2GSTransfer'] = _C2GSTRANSFER
DESCRIPTOR.message_types_by_name['C2GSClickWorldMap'] = _C2GSCLICKWORLDMAP
DESCRIPTOR.message_types_by_name['C2GSClickTrapMineMap'] = _C2GSCLICKTRAPMINEMAP
DESCRIPTOR.message_types_by_name['C2GSStartWaterWalk'] = _C2GSSTARTWATERWALK

C2GSSyncPosQueue = _reflection.GeneratedProtocolMessageType('C2GSSyncPosQueue', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSYNCPOSQUEUE,
  __module__ = 'scene_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSyncPosQueue)
  ))
_sym_db.RegisterMessage(C2GSSyncPosQueue)

C2GSTransfer = _reflection.GeneratedProtocolMessageType('C2GSTransfer', (_message.Message,), dict(
  DESCRIPTOR = _C2GSTRANSFER,
  __module__ = 'scene_pb2'
  # @@protoc_insertion_point(class_scope:C2GSTransfer)
  ))
_sym_db.RegisterMessage(C2GSTransfer)

C2GSClickWorldMap = _reflection.GeneratedProtocolMessageType('C2GSClickWorldMap', (_message.Message,), dict(
  DESCRIPTOR = _C2GSCLICKWORLDMAP,
  __module__ = 'scene_pb2'
  # @@protoc_insertion_point(class_scope:C2GSClickWorldMap)
  ))
_sym_db.RegisterMessage(C2GSClickWorldMap)

C2GSClickTrapMineMap = _reflection.GeneratedProtocolMessageType('C2GSClickTrapMineMap', (_message.Message,), dict(
  DESCRIPTOR = _C2GSCLICKTRAPMINEMAP,
  __module__ = 'scene_pb2'
  # @@protoc_insertion_point(class_scope:C2GSClickTrapMineMap)
  ))
_sym_db.RegisterMessage(C2GSClickTrapMineMap)

C2GSStartWaterWalk = _reflection.GeneratedProtocolMessageType('C2GSStartWaterWalk', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSTARTWATERWALK,
  __module__ = 'scene_pb2'
  # @@protoc_insertion_point(class_scope:C2GSStartWaterWalk)
  ))
_sym_db.RegisterMessage(C2GSStartWaterWalk)


# @@protoc_insertion_point(module_scope)
