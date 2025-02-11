# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jjc.proto

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
  name='jjc.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\tjjc.proto\"\'\n\x0b\x46ighterInfo\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\n\n\x02id\x18\x02 \x01(\r\"$\n\x08TargetID\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\n\n\x02id\x18\x02 \x01(\r\"\x13\n\x11\x43\x32GSOpenJJCMainUI\"(\n\x13\x43\x32GSSetJJCFormation\x12\x11\n\tformation\x18\x01 \x01(\r\"$\n\x10\x43\x32GSSetJJCSummon\x12\x10\n\x08summonid\x18\x01 \x01(\r\"\'\n\x11\x43\x32GSSetJJCPartner\x12\x12\n\npartnerids\x18\x01 \x03(\r\"5\n\x18\x43\x32GSQueryJJCTargetLineup\x12\x19\n\x06target\x18\x01 \x01(\x0b\x32\t.TargetID\".\n\x11\x43\x32GSJJCStartFight\x12\x19\n\x06target\x18\x01 \x01(\x0b\x32\t.TargetID\"\x14\n\x12\x43\x32GSJJCGetFightLog\"\x16\n\x14\x43\x32GSJJCBuyFightTimes\"\x10\n\x0e\x43\x32GSJJCClearCD\"\x15\n\x13\x43\x32GSOpenChallengeUI\"\"\n\x13\x43\x32GSChooseChallenge\x12\x0b\n\x03idx\x18\x01 \x01(\r\".\n\x19\x43\x32GSSetChallengeFormation\x12\x11\n\tformation\x18\x01 \x01(\r\"*\n\x16\x43\x32GSSetChallengeSummon\x12\x10\n\x08summonid\x18\x01 \x01(\r\"9\n\x17\x43\x32GSSetChallengeFighter\x12\x1e\n\x08\x66ighters\x18\x01 \x03(\x0b\x32\x0c.FighterInfo\"\x1a\n\x18\x43\x32GSResetChallengeTarget\"/\n\x12\x43\x32GSStartChallenge\x12\x19\n\x06target\x18\x01 \x01(\x0b\x32\t.TargetID\"\x18\n\x16\x43\x32GSGetChallengeReward\"6\n\x19\x43\x32GSChallengeTargetLineup\x12\x19\n\x06target\x18\x01 \x01(\x0b\x32\t.TargetID\"\x16\n\x14\x43\x32GSReceiveFirstGift\"\x16\n\x14\x43\x32GSRefreshJJCTarget')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FIGHTERINFO = _descriptor.Descriptor(
  name='FighterInfo',
  full_name='FighterInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='FighterInfo.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='FighterInfo.id', index=1,
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
  serialized_start=13,
  serialized_end=52,
)


_TARGETID = _descriptor.Descriptor(
  name='TargetID',
  full_name='TargetID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='TargetID.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='TargetID.id', index=1,
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
  serialized_start=54,
  serialized_end=90,
)


_C2GSOPENJJCMAINUI = _descriptor.Descriptor(
  name='C2GSOpenJJCMainUI',
  full_name='C2GSOpenJJCMainUI',
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
  serialized_start=92,
  serialized_end=111,
)


_C2GSSETJJCFORMATION = _descriptor.Descriptor(
  name='C2GSSetJJCFormation',
  full_name='C2GSSetJJCFormation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='formation', full_name='C2GSSetJJCFormation.formation', index=0,
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
  serialized_start=113,
  serialized_end=153,
)


_C2GSSETJJCSUMMON = _descriptor.Descriptor(
  name='C2GSSetJJCSummon',
  full_name='C2GSSetJJCSummon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summonid', full_name='C2GSSetJJCSummon.summonid', index=0,
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
  serialized_start=155,
  serialized_end=191,
)


_C2GSSETJJCPARTNER = _descriptor.Descriptor(
  name='C2GSSetJJCPartner',
  full_name='C2GSSetJJCPartner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='partnerids', full_name='C2GSSetJJCPartner.partnerids', index=0,
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
  serialized_start=193,
  serialized_end=232,
)


_C2GSQUERYJJCTARGETLINEUP = _descriptor.Descriptor(
  name='C2GSQueryJJCTargetLineup',
  full_name='C2GSQueryJJCTargetLineup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='C2GSQueryJJCTargetLineup.target', index=0,
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
  serialized_start=234,
  serialized_end=287,
)


_C2GSJJCSTARTFIGHT = _descriptor.Descriptor(
  name='C2GSJJCStartFight',
  full_name='C2GSJJCStartFight',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='C2GSJJCStartFight.target', index=0,
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
  serialized_start=289,
  serialized_end=335,
)


_C2GSJJCGETFIGHTLOG = _descriptor.Descriptor(
  name='C2GSJJCGetFightLog',
  full_name='C2GSJJCGetFightLog',
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
  serialized_start=337,
  serialized_end=357,
)


_C2GSJJCBUYFIGHTTIMES = _descriptor.Descriptor(
  name='C2GSJJCBuyFightTimes',
  full_name='C2GSJJCBuyFightTimes',
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
  serialized_start=359,
  serialized_end=381,
)


_C2GSJJCCLEARCD = _descriptor.Descriptor(
  name='C2GSJJCClearCD',
  full_name='C2GSJJCClearCD',
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
  serialized_start=383,
  serialized_end=399,
)


_C2GSOPENCHALLENGEUI = _descriptor.Descriptor(
  name='C2GSOpenChallengeUI',
  full_name='C2GSOpenChallengeUI',
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
  serialized_start=401,
  serialized_end=422,
)


_C2GSCHOOSECHALLENGE = _descriptor.Descriptor(
  name='C2GSChooseChallenge',
  full_name='C2GSChooseChallenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='idx', full_name='C2GSChooseChallenge.idx', index=0,
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
  serialized_start=424,
  serialized_end=458,
)


_C2GSSETCHALLENGEFORMATION = _descriptor.Descriptor(
  name='C2GSSetChallengeFormation',
  full_name='C2GSSetChallengeFormation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='formation', full_name='C2GSSetChallengeFormation.formation', index=0,
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
  serialized_start=460,
  serialized_end=506,
)


_C2GSSETCHALLENGESUMMON = _descriptor.Descriptor(
  name='C2GSSetChallengeSummon',
  full_name='C2GSSetChallengeSummon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='summonid', full_name='C2GSSetChallengeSummon.summonid', index=0,
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
  serialized_start=508,
  serialized_end=550,
)


_C2GSSETCHALLENGEFIGHTER = _descriptor.Descriptor(
  name='C2GSSetChallengeFighter',
  full_name='C2GSSetChallengeFighter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fighters', full_name='C2GSSetChallengeFighter.fighters', index=0,
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
  serialized_start=552,
  serialized_end=609,
)


_C2GSRESETCHALLENGETARGET = _descriptor.Descriptor(
  name='C2GSResetChallengeTarget',
  full_name='C2GSResetChallengeTarget',
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
  serialized_start=611,
  serialized_end=637,
)


_C2GSSTARTCHALLENGE = _descriptor.Descriptor(
  name='C2GSStartChallenge',
  full_name='C2GSStartChallenge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='C2GSStartChallenge.target', index=0,
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
  serialized_start=639,
  serialized_end=686,
)


_C2GSGETCHALLENGEREWARD = _descriptor.Descriptor(
  name='C2GSGetChallengeReward',
  full_name='C2GSGetChallengeReward',
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
  serialized_start=688,
  serialized_end=712,
)


_C2GSCHALLENGETARGETLINEUP = _descriptor.Descriptor(
  name='C2GSChallengeTargetLineup',
  full_name='C2GSChallengeTargetLineup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='C2GSChallengeTargetLineup.target', index=0,
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
  serialized_start=714,
  serialized_end=768,
)


_C2GSRECEIVEFIRSTGIFT = _descriptor.Descriptor(
  name='C2GSReceiveFirstGift',
  full_name='C2GSReceiveFirstGift',
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
  serialized_start=770,
  serialized_end=792,
)


_C2GSREFRESHJJCTARGET = _descriptor.Descriptor(
  name='C2GSRefreshJJCTarget',
  full_name='C2GSRefreshJJCTarget',
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
  serialized_start=794,
  serialized_end=816,
)

_C2GSQUERYJJCTARGETLINEUP.fields_by_name['target'].message_type = _TARGETID
_C2GSJJCSTARTFIGHT.fields_by_name['target'].message_type = _TARGETID
_C2GSSETCHALLENGEFIGHTER.fields_by_name['fighters'].message_type = _FIGHTERINFO
_C2GSSTARTCHALLENGE.fields_by_name['target'].message_type = _TARGETID
_C2GSCHALLENGETARGETLINEUP.fields_by_name['target'].message_type = _TARGETID
DESCRIPTOR.message_types_by_name['FighterInfo'] = _FIGHTERINFO
DESCRIPTOR.message_types_by_name['TargetID'] = _TARGETID
DESCRIPTOR.message_types_by_name['C2GSOpenJJCMainUI'] = _C2GSOPENJJCMAINUI
DESCRIPTOR.message_types_by_name['C2GSSetJJCFormation'] = _C2GSSETJJCFORMATION
DESCRIPTOR.message_types_by_name['C2GSSetJJCSummon'] = _C2GSSETJJCSUMMON
DESCRIPTOR.message_types_by_name['C2GSSetJJCPartner'] = _C2GSSETJJCPARTNER
DESCRIPTOR.message_types_by_name['C2GSQueryJJCTargetLineup'] = _C2GSQUERYJJCTARGETLINEUP
DESCRIPTOR.message_types_by_name['C2GSJJCStartFight'] = _C2GSJJCSTARTFIGHT
DESCRIPTOR.message_types_by_name['C2GSJJCGetFightLog'] = _C2GSJJCGETFIGHTLOG
DESCRIPTOR.message_types_by_name['C2GSJJCBuyFightTimes'] = _C2GSJJCBUYFIGHTTIMES
DESCRIPTOR.message_types_by_name['C2GSJJCClearCD'] = _C2GSJJCCLEARCD
DESCRIPTOR.message_types_by_name['C2GSOpenChallengeUI'] = _C2GSOPENCHALLENGEUI
DESCRIPTOR.message_types_by_name['C2GSChooseChallenge'] = _C2GSCHOOSECHALLENGE
DESCRIPTOR.message_types_by_name['C2GSSetChallengeFormation'] = _C2GSSETCHALLENGEFORMATION
DESCRIPTOR.message_types_by_name['C2GSSetChallengeSummon'] = _C2GSSETCHALLENGESUMMON
DESCRIPTOR.message_types_by_name['C2GSSetChallengeFighter'] = _C2GSSETCHALLENGEFIGHTER
DESCRIPTOR.message_types_by_name['C2GSResetChallengeTarget'] = _C2GSRESETCHALLENGETARGET
DESCRIPTOR.message_types_by_name['C2GSStartChallenge'] = _C2GSSTARTCHALLENGE
DESCRIPTOR.message_types_by_name['C2GSGetChallengeReward'] = _C2GSGETCHALLENGEREWARD
DESCRIPTOR.message_types_by_name['C2GSChallengeTargetLineup'] = _C2GSCHALLENGETARGETLINEUP
DESCRIPTOR.message_types_by_name['C2GSReceiveFirstGift'] = _C2GSRECEIVEFIRSTGIFT
DESCRIPTOR.message_types_by_name['C2GSRefreshJJCTarget'] = _C2GSREFRESHJJCTARGET

FighterInfo = _reflection.GeneratedProtocolMessageType('FighterInfo', (_message.Message,), dict(
  DESCRIPTOR = _FIGHTERINFO,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:FighterInfo)
  ))
_sym_db.RegisterMessage(FighterInfo)

TargetID = _reflection.GeneratedProtocolMessageType('TargetID', (_message.Message,), dict(
  DESCRIPTOR = _TARGETID,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:TargetID)
  ))
_sym_db.RegisterMessage(TargetID)

C2GSOpenJJCMainUI = _reflection.GeneratedProtocolMessageType('C2GSOpenJJCMainUI', (_message.Message,), dict(
  DESCRIPTOR = _C2GSOPENJJCMAINUI,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSOpenJJCMainUI)
  ))
_sym_db.RegisterMessage(C2GSOpenJJCMainUI)

C2GSSetJJCFormation = _reflection.GeneratedProtocolMessageType('C2GSSetJJCFormation', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSETJJCFORMATION,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSetJJCFormation)
  ))
_sym_db.RegisterMessage(C2GSSetJJCFormation)

C2GSSetJJCSummon = _reflection.GeneratedProtocolMessageType('C2GSSetJJCSummon', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSETJJCSUMMON,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSetJJCSummon)
  ))
_sym_db.RegisterMessage(C2GSSetJJCSummon)

C2GSSetJJCPartner = _reflection.GeneratedProtocolMessageType('C2GSSetJJCPartner', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSETJJCPARTNER,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSetJJCPartner)
  ))
_sym_db.RegisterMessage(C2GSSetJJCPartner)

C2GSQueryJJCTargetLineup = _reflection.GeneratedProtocolMessageType('C2GSQueryJJCTargetLineup', (_message.Message,), dict(
  DESCRIPTOR = _C2GSQUERYJJCTARGETLINEUP,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSQueryJJCTargetLineup)
  ))
_sym_db.RegisterMessage(C2GSQueryJJCTargetLineup)

C2GSJJCStartFight = _reflection.GeneratedProtocolMessageType('C2GSJJCStartFight', (_message.Message,), dict(
  DESCRIPTOR = _C2GSJJCSTARTFIGHT,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSJJCStartFight)
  ))
_sym_db.RegisterMessage(C2GSJJCStartFight)

C2GSJJCGetFightLog = _reflection.GeneratedProtocolMessageType('C2GSJJCGetFightLog', (_message.Message,), dict(
  DESCRIPTOR = _C2GSJJCGETFIGHTLOG,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSJJCGetFightLog)
  ))
_sym_db.RegisterMessage(C2GSJJCGetFightLog)

C2GSJJCBuyFightTimes = _reflection.GeneratedProtocolMessageType('C2GSJJCBuyFightTimes', (_message.Message,), dict(
  DESCRIPTOR = _C2GSJJCBUYFIGHTTIMES,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSJJCBuyFightTimes)
  ))
_sym_db.RegisterMessage(C2GSJJCBuyFightTimes)

C2GSJJCClearCD = _reflection.GeneratedProtocolMessageType('C2GSJJCClearCD', (_message.Message,), dict(
  DESCRIPTOR = _C2GSJJCCLEARCD,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSJJCClearCD)
  ))
_sym_db.RegisterMessage(C2GSJJCClearCD)

C2GSOpenChallengeUI = _reflection.GeneratedProtocolMessageType('C2GSOpenChallengeUI', (_message.Message,), dict(
  DESCRIPTOR = _C2GSOPENCHALLENGEUI,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSOpenChallengeUI)
  ))
_sym_db.RegisterMessage(C2GSOpenChallengeUI)

C2GSChooseChallenge = _reflection.GeneratedProtocolMessageType('C2GSChooseChallenge', (_message.Message,), dict(
  DESCRIPTOR = _C2GSCHOOSECHALLENGE,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSChooseChallenge)
  ))
_sym_db.RegisterMessage(C2GSChooseChallenge)

C2GSSetChallengeFormation = _reflection.GeneratedProtocolMessageType('C2GSSetChallengeFormation', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSETCHALLENGEFORMATION,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSetChallengeFormation)
  ))
_sym_db.RegisterMessage(C2GSSetChallengeFormation)

C2GSSetChallengeSummon = _reflection.GeneratedProtocolMessageType('C2GSSetChallengeSummon', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSETCHALLENGESUMMON,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSetChallengeSummon)
  ))
_sym_db.RegisterMessage(C2GSSetChallengeSummon)

C2GSSetChallengeFighter = _reflection.GeneratedProtocolMessageType('C2GSSetChallengeFighter', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSETCHALLENGEFIGHTER,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSSetChallengeFighter)
  ))
_sym_db.RegisterMessage(C2GSSetChallengeFighter)

C2GSResetChallengeTarget = _reflection.GeneratedProtocolMessageType('C2GSResetChallengeTarget', (_message.Message,), dict(
  DESCRIPTOR = _C2GSRESETCHALLENGETARGET,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSResetChallengeTarget)
  ))
_sym_db.RegisterMessage(C2GSResetChallengeTarget)

C2GSStartChallenge = _reflection.GeneratedProtocolMessageType('C2GSStartChallenge', (_message.Message,), dict(
  DESCRIPTOR = _C2GSSTARTCHALLENGE,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSStartChallenge)
  ))
_sym_db.RegisterMessage(C2GSStartChallenge)

C2GSGetChallengeReward = _reflection.GeneratedProtocolMessageType('C2GSGetChallengeReward', (_message.Message,), dict(
  DESCRIPTOR = _C2GSGETCHALLENGEREWARD,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSGetChallengeReward)
  ))
_sym_db.RegisterMessage(C2GSGetChallengeReward)

C2GSChallengeTargetLineup = _reflection.GeneratedProtocolMessageType('C2GSChallengeTargetLineup', (_message.Message,), dict(
  DESCRIPTOR = _C2GSCHALLENGETARGETLINEUP,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSChallengeTargetLineup)
  ))
_sym_db.RegisterMessage(C2GSChallengeTargetLineup)

C2GSReceiveFirstGift = _reflection.GeneratedProtocolMessageType('C2GSReceiveFirstGift', (_message.Message,), dict(
  DESCRIPTOR = _C2GSRECEIVEFIRSTGIFT,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSReceiveFirstGift)
  ))
_sym_db.RegisterMessage(C2GSReceiveFirstGift)

C2GSRefreshJJCTarget = _reflection.GeneratedProtocolMessageType('C2GSRefreshJJCTarget', (_message.Message,), dict(
  DESCRIPTOR = _C2GSREFRESHJJCTARGET,
  __module__ = 'jjc_pb2'
  # @@protoc_insertion_point(class_scope:C2GSRefreshJJCTarget)
  ))
_sym_db.RegisterMessage(C2GSRefreshJJCTarget)


# @@protoc_insertion_point(module_scope)
