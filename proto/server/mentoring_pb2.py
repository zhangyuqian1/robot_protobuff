# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mentoring.proto

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
  name='mentoring.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0fmentoring.proto\x1a\x11\x62\x61se/common.proto\"-\n\x06Option\x12\x13\n\x0bquestion_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61nswer\x18\x02 \x01(\r\"F\n\x18GS2CMentoringStartAnswer\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x1c\n\x0boption_list\x18\x02 \x03(\x0b\x32\x07.Option\"G\n\x1cGS2CMentoringRecommendMentor\x12\'\n\x0bmentor_list\x18\x01 \x03(\x0b\x32\x12.base.SimplePlayer\"-\n\x08TaskUnit\x12\x0f\n\x07task_id\x18\x01 \x01(\r\x12\x10\n\x08task_cnt\x18\x02 \x01(\r\"3\n\nRewardUnit\x12\x11\n\treward_id\x18\x01 \x01(\r\x12\x12\n\nreward_cnt\x18\x02 \x01(\r\"\xd0\x01\n\x11GS2CMentoringTask\x12\x1c\n\ttask_list\x18\x01 \x03(\x0b\x32\t.TaskUnit\x12\x10\n\x08progress\x18\x02 \x01(\r\x12 \n\x0breward_list\x18\x03 \x03(\x0b\x32\x0b.RewardUnit\x12\x0b\n\x03key\x18\x04 \x01(\t\x12\x1c\n\tstep_list\x18\x05 \x03(\x0b\x32\t.StepUnit\x12\x14\n\x0ctarget_grade\x18\x06 \x01(\r\x12\x14\n\x0ctarget_score\x18\x07 \x01(\r\x12\x12\n\ngrowup_num\x18\x08 \x01(\r\"=\n\x08StepUnit\x12\x0f\n\x07step_id\x18\x01 \x01(\r\x12\x0e\n\x06status\x18\x02 \x01(\x05\x12\x10\n\x08step_cnt\x18\x03 \x01(\r\"9\n\x14GS2CMentorEvalutaion\x12\r\n\x05grade\x18\x01 \x01(\r\x12\x12\n\nsessionidx\x18\x02 \x01(\r')
  ,
  dependencies=[base_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_OPTION = _descriptor.Descriptor(
  name='Option',
  full_name='Option',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='question_id', full_name='Option.question_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='answer', full_name='Option.answer', index=1,
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
  serialized_start=38,
  serialized_end=83,
)


_GS2CMENTORINGSTARTANSWER = _descriptor.Descriptor(
  name='GS2CMentoringStartAnswer',
  full_name='GS2CMentoringStartAnswer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='GS2CMentoringStartAnswer.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='option_list', full_name='GS2CMentoringStartAnswer.option_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=85,
  serialized_end=155,
)


_GS2CMENTORINGRECOMMENDMENTOR = _descriptor.Descriptor(
  name='GS2CMentoringRecommendMentor',
  full_name='GS2CMentoringRecommendMentor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mentor_list', full_name='GS2CMentoringRecommendMentor.mentor_list', index=0,
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
  serialized_start=157,
  serialized_end=228,
)


_TASKUNIT = _descriptor.Descriptor(
  name='TaskUnit',
  full_name='TaskUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='TaskUnit.task_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_cnt', full_name='TaskUnit.task_cnt', index=1,
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
  serialized_start=230,
  serialized_end=275,
)


_REWARDUNIT = _descriptor.Descriptor(
  name='RewardUnit',
  full_name='RewardUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reward_id', full_name='RewardUnit.reward_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_cnt', full_name='RewardUnit.reward_cnt', index=1,
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
  serialized_start=277,
  serialized_end=328,
)


_GS2CMENTORINGTASK = _descriptor.Descriptor(
  name='GS2CMentoringTask',
  full_name='GS2CMentoringTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_list', full_name='GS2CMentoringTask.task_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='progress', full_name='GS2CMentoringTask.progress', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reward_list', full_name='GS2CMentoringTask.reward_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='GS2CMentoringTask.key', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_list', full_name='GS2CMentoringTask.step_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_grade', full_name='GS2CMentoringTask.target_grade', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_score', full_name='GS2CMentoringTask.target_score', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='growup_num', full_name='GS2CMentoringTask.growup_num', index=7,
      number=8, type=13, cpp_type=3, label=1,
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
  serialized_start=331,
  serialized_end=539,
)


_STEPUNIT = _descriptor.Descriptor(
  name='StepUnit',
  full_name='StepUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step_id', full_name='StepUnit.step_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='StepUnit.status', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_cnt', full_name='StepUnit.step_cnt', index=2,
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
  serialized_start=541,
  serialized_end=602,
)


_GS2CMENTOREVALUTAION = _descriptor.Descriptor(
  name='GS2CMentorEvalutaion',
  full_name='GS2CMentorEvalutaion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grade', full_name='GS2CMentorEvalutaion.grade', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sessionidx', full_name='GS2CMentorEvalutaion.sessionidx', index=1,
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
  serialized_start=604,
  serialized_end=661,
)

_GS2CMENTORINGSTARTANSWER.fields_by_name['option_list'].message_type = _OPTION
_GS2CMENTORINGRECOMMENDMENTOR.fields_by_name['mentor_list'].message_type = base_dot_common__pb2._SIMPLEPLAYER
_GS2CMENTORINGTASK.fields_by_name['task_list'].message_type = _TASKUNIT
_GS2CMENTORINGTASK.fields_by_name['reward_list'].message_type = _REWARDUNIT
_GS2CMENTORINGTASK.fields_by_name['step_list'].message_type = _STEPUNIT
DESCRIPTOR.message_types_by_name['Option'] = _OPTION
DESCRIPTOR.message_types_by_name['GS2CMentoringStartAnswer'] = _GS2CMENTORINGSTARTANSWER
DESCRIPTOR.message_types_by_name['GS2CMentoringRecommendMentor'] = _GS2CMENTORINGRECOMMENDMENTOR
DESCRIPTOR.message_types_by_name['TaskUnit'] = _TASKUNIT
DESCRIPTOR.message_types_by_name['RewardUnit'] = _REWARDUNIT
DESCRIPTOR.message_types_by_name['GS2CMentoringTask'] = _GS2CMENTORINGTASK
DESCRIPTOR.message_types_by_name['StepUnit'] = _STEPUNIT
DESCRIPTOR.message_types_by_name['GS2CMentorEvalutaion'] = _GS2CMENTOREVALUTAION

Option = _reflection.GeneratedProtocolMessageType('Option', (_message.Message,), dict(
  DESCRIPTOR = _OPTION,
  __module__ = 'mentoring_pb2'
  # @@protoc_insertion_point(class_scope:Option)
  ))
_sym_db.RegisterMessage(Option)

GS2CMentoringStartAnswer = _reflection.GeneratedProtocolMessageType('GS2CMentoringStartAnswer', (_message.Message,), dict(
  DESCRIPTOR = _GS2CMENTORINGSTARTANSWER,
  __module__ = 'mentoring_pb2'
  # @@protoc_insertion_point(class_scope:GS2CMentoringStartAnswer)
  ))
_sym_db.RegisterMessage(GS2CMentoringStartAnswer)

GS2CMentoringRecommendMentor = _reflection.GeneratedProtocolMessageType('GS2CMentoringRecommendMentor', (_message.Message,), dict(
  DESCRIPTOR = _GS2CMENTORINGRECOMMENDMENTOR,
  __module__ = 'mentoring_pb2'
  # @@protoc_insertion_point(class_scope:GS2CMentoringRecommendMentor)
  ))
_sym_db.RegisterMessage(GS2CMentoringRecommendMentor)

TaskUnit = _reflection.GeneratedProtocolMessageType('TaskUnit', (_message.Message,), dict(
  DESCRIPTOR = _TASKUNIT,
  __module__ = 'mentoring_pb2'
  # @@protoc_insertion_point(class_scope:TaskUnit)
  ))
_sym_db.RegisterMessage(TaskUnit)

RewardUnit = _reflection.GeneratedProtocolMessageType('RewardUnit', (_message.Message,), dict(
  DESCRIPTOR = _REWARDUNIT,
  __module__ = 'mentoring_pb2'
  # @@protoc_insertion_point(class_scope:RewardUnit)
  ))
_sym_db.RegisterMessage(RewardUnit)

GS2CMentoringTask = _reflection.GeneratedProtocolMessageType('GS2CMentoringTask', (_message.Message,), dict(
  DESCRIPTOR = _GS2CMENTORINGTASK,
  __module__ = 'mentoring_pb2'
  # @@protoc_insertion_point(class_scope:GS2CMentoringTask)
  ))
_sym_db.RegisterMessage(GS2CMentoringTask)

StepUnit = _reflection.GeneratedProtocolMessageType('StepUnit', (_message.Message,), dict(
  DESCRIPTOR = _STEPUNIT,
  __module__ = 'mentoring_pb2'
  # @@protoc_insertion_point(class_scope:StepUnit)
  ))
_sym_db.RegisterMessage(StepUnit)

GS2CMentorEvalutaion = _reflection.GeneratedProtocolMessageType('GS2CMentorEvalutaion', (_message.Message,), dict(
  DESCRIPTOR = _GS2CMENTOREVALUTAION,
  __module__ = 'mentoring_pb2'
  # @@protoc_insertion_point(class_scope:GS2CMentorEvalutaion)
  ))
_sym_db.RegisterMessage(GS2CMentorEvalutaion)


# @@protoc_insertion_point(module_scope)
