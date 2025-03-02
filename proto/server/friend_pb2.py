# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: friend.proto

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
  name='friend.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x66riend.proto\x1a\x11\x62\x61se/common.proto\"-\n\nSingleChat\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t\">\n\x0fLoginFriendChat\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x1e\n\tchat_list\x18\x02 \x03(\x0b\x32\x0b.SingleChat\"v\n\x0fRecommendFriend\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05shape\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\r\x12\r\n\x05grade\x18\x05 \x01(\r\x12\x0e\n\x06school\x18\x06 \x01(\r\x12\x0c\n\x04icon\x18\x07 \x01(\r\"5\n\x10OnlineStatusInfo\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x14\n\x0conlinestatus\x18\x02 \x01(\r\"\x86\x01\n\x0fGS2CLoginFriend\x12*\n\x10\x66riend_chat_list\x18\x01 \x03(\x0b\x32\x10.LoginFriendChat\x12\x12\n\nblack_list\x18\x02 \x03(\r\x12\x33\n\x18\x66riend_onlinestatus_list\x18\x03 \x03(\x0b\x32\x11.OnlineStatusInfo\":\n\rGS2CAddFriend\x12)\n\x0cprofile_list\x18\x01 \x03(\x0b\x32\x13.base.FriendProfile\"!\n\rGS2CDelFriend\x12\x10\n\x08pid_list\x18\x01 \x03(\r\"<\n\x16GS2CUpdateFriendDegree\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x15\n\rfriend_degree\x18\x02 \x01(\r\"0\n\rGS2CAckChatTo\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x12\n\nmessage_id\x18\x02 \x01(\t\"<\n\x0cGS2CChatFrom\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x12\n\nmessage_id\x18\x03 \x01(\t\"G\n\x14GS2CRecommendFriends\x12/\n\x15recommend_friend_list\x18\x01 \x03(\x0b\x32\x10.RecommendFriend\"@\n\x13GS2CStrangerProfile\x12)\n\x0cprofile_list\x18\x01 \x03(\x0b\x32\x13.base.FriendProfile\"$\n\x10GS2CFriendShield\x12\x10\n\x08pid_list\x18\x01 \x03(\r\"&\n\x12GS2CFriendUnshield\x12\x10\n\x08pid_list\x18\x01 \x03(\r\"x\n\x14GS2COpenSendFlowerUI\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\r\x12\r\n\x05grade\x18\x04 \x01(\r\x12\x15\n\rfriend_degree\x18\x05 \x01(\r\x12\x11\n\trole_type\x18\x06 \x01(\r\"3\n\x15GS2CSendFlowerSuccess\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\r\n\x05\x62less\x18\x02 \x01(\t\"@\n\x18GS2CRefreshFriendProfile\x12$\n\x07profile\x18\x01 \x01(\x0b\x32\x13.base.FriendProfile\"-\n\x10GS2CVerifyFriend\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\"=\n\x13VerifyFriendConfirm\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"D\n\x17GS2CVerifyFriendConfirm\x12)\n\x0bverify_list\x18\x01 \x03(\x0b\x32\x14.VerifyFriendConfirm\"*\n\x1bGS2CNotifyRefuseStrangerMsg\x12\x0b\n\x03pid\x18\x01 \x01(\r\"9\n\x1cGS2CRefreshFriendProfileBoth\x12\x0b\n\x03pid\x18\x01 \x01(\r\x12\x0c\n\x04\x62oth\x18\x02 \x01(\r\"L\n\x11GS2CPlayerProfile\x12)\n\x0cprofile_list\x18\x01 \x03(\x0b\x32\x13.base.FriendProfile\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r')
  ,
  dependencies=[base_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SINGLECHAT = _descriptor.Descriptor(
  name='SingleChat',
  full_name='SingleChat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='SingleChat.message_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='SingleChat.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=35,
  serialized_end=80,
)


_LOGINFRIENDCHAT = _descriptor.Descriptor(
  name='LoginFriendChat',
  full_name='LoginFriendChat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='LoginFriendChat.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chat_list', full_name='LoginFriendChat.chat_list', index=1,
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
  serialized_start=82,
  serialized_end=144,
)


_RECOMMENDFRIEND = _descriptor.Descriptor(
  name='RecommendFriend',
  full_name='RecommendFriend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='RecommendFriend.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='RecommendFriend.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape', full_name='RecommendFriend.shape', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='RecommendFriend.type', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grade', full_name='RecommendFriend.grade', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='school', full_name='RecommendFriend.school', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon', full_name='RecommendFriend.icon', index=6,
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
  serialized_start=146,
  serialized_end=264,
)


_ONLINESTATUSINFO = _descriptor.Descriptor(
  name='OnlineStatusInfo',
  full_name='OnlineStatusInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='OnlineStatusInfo.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='onlinestatus', full_name='OnlineStatusInfo.onlinestatus', index=1,
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
  serialized_start=266,
  serialized_end=319,
)


_GS2CLOGINFRIEND = _descriptor.Descriptor(
  name='GS2CLoginFriend',
  full_name='GS2CLoginFriend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='friend_chat_list', full_name='GS2CLoginFriend.friend_chat_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='black_list', full_name='GS2CLoginFriend.black_list', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_onlinestatus_list', full_name='GS2CLoginFriend.friend_onlinestatus_list', index=2,
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
  serialized_start=322,
  serialized_end=456,
)


_GS2CADDFRIEND = _descriptor.Descriptor(
  name='GS2CAddFriend',
  full_name='GS2CAddFriend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile_list', full_name='GS2CAddFriend.profile_list', index=0,
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
  serialized_start=458,
  serialized_end=516,
)


_GS2CDELFRIEND = _descriptor.Descriptor(
  name='GS2CDelFriend',
  full_name='GS2CDelFriend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid_list', full_name='GS2CDelFriend.pid_list', index=0,
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
  serialized_start=518,
  serialized_end=551,
)


_GS2CUPDATEFRIENDDEGREE = _descriptor.Descriptor(
  name='GS2CUpdateFriendDegree',
  full_name='GS2CUpdateFriendDegree',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2CUpdateFriendDegree.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_degree', full_name='GS2CUpdateFriendDegree.friend_degree', index=1,
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
  serialized_start=553,
  serialized_end=613,
)


_GS2CACKCHATTO = _descriptor.Descriptor(
  name='GS2CAckChatTo',
  full_name='GS2CAckChatTo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2CAckChatTo.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='GS2CAckChatTo.message_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=615,
  serialized_end=663,
)


_GS2CCHATFROM = _descriptor.Descriptor(
  name='GS2CChatFrom',
  full_name='GS2CChatFrom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2CChatFrom.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='GS2CChatFrom.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_id', full_name='GS2CChatFrom.message_id', index=2,
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
  serialized_start=665,
  serialized_end=725,
)


_GS2CRECOMMENDFRIENDS = _descriptor.Descriptor(
  name='GS2CRecommendFriends',
  full_name='GS2CRecommendFriends',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recommend_friend_list', full_name='GS2CRecommendFriends.recommend_friend_list', index=0,
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
  serialized_start=727,
  serialized_end=798,
)


_GS2CSTRANGERPROFILE = _descriptor.Descriptor(
  name='GS2CStrangerProfile',
  full_name='GS2CStrangerProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile_list', full_name='GS2CStrangerProfile.profile_list', index=0,
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
  serialized_start=800,
  serialized_end=864,
)


_GS2CFRIENDSHIELD = _descriptor.Descriptor(
  name='GS2CFriendShield',
  full_name='GS2CFriendShield',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid_list', full_name='GS2CFriendShield.pid_list', index=0,
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
  serialized_start=866,
  serialized_end=902,
)


_GS2CFRIENDUNSHIELD = _descriptor.Descriptor(
  name='GS2CFriendUnshield',
  full_name='GS2CFriendUnshield',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid_list', full_name='GS2CFriendUnshield.pid_list', index=0,
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
  serialized_start=904,
  serialized_end=942,
)


_GS2COPENSENDFLOWERUI = _descriptor.Descriptor(
  name='GS2COpenSendFlowerUI',
  full_name='GS2COpenSendFlowerUI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2COpenSendFlowerUI.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='GS2COpenSendFlowerUI.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='icon', full_name='GS2COpenSendFlowerUI.icon', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grade', full_name='GS2COpenSendFlowerUI.grade', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friend_degree', full_name='GS2COpenSendFlowerUI.friend_degree', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_type', full_name='GS2COpenSendFlowerUI.role_type', index=5,
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
  serialized_start=944,
  serialized_end=1064,
)


_GS2CSENDFLOWERSUCCESS = _descriptor.Descriptor(
  name='GS2CSendFlowerSuccess',
  full_name='GS2CSendFlowerSuccess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2CSendFlowerSuccess.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bless', full_name='GS2CSendFlowerSuccess.bless', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1066,
  serialized_end=1117,
)


_GS2CREFRESHFRIENDPROFILE = _descriptor.Descriptor(
  name='GS2CRefreshFriendProfile',
  full_name='GS2CRefreshFriendProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile', full_name='GS2CRefreshFriendProfile.profile', index=0,
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
  serialized_start=1119,
  serialized_end=1183,
)


_GS2CVERIFYFRIEND = _descriptor.Descriptor(
  name='GS2CVerifyFriend',
  full_name='GS2CVerifyFriend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2CVerifyFriend.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='GS2CVerifyFriend.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1185,
  serialized_end=1230,
)


_VERIFYFRIENDCONFIRM = _descriptor.Descriptor(
  name='VerifyFriendConfirm',
  full_name='VerifyFriendConfirm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='VerifyFriendConfirm.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='VerifyFriendConfirm.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='VerifyFriendConfirm.msg', index=2,
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
  serialized_start=1232,
  serialized_end=1293,
)


_GS2CVERIFYFRIENDCONFIRM = _descriptor.Descriptor(
  name='GS2CVerifyFriendConfirm',
  full_name='GS2CVerifyFriendConfirm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='verify_list', full_name='GS2CVerifyFriendConfirm.verify_list', index=0,
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
  serialized_start=1295,
  serialized_end=1363,
)


_GS2CNOTIFYREFUSESTRANGERMSG = _descriptor.Descriptor(
  name='GS2CNotifyRefuseStrangerMsg',
  full_name='GS2CNotifyRefuseStrangerMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2CNotifyRefuseStrangerMsg.pid', index=0,
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
  serialized_start=1365,
  serialized_end=1407,
)


_GS2CREFRESHFRIENDPROFILEBOTH = _descriptor.Descriptor(
  name='GS2CRefreshFriendProfileBoth',
  full_name='GS2CRefreshFriendProfileBoth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='GS2CRefreshFriendProfileBoth.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='both', full_name='GS2CRefreshFriendProfileBoth.both', index=1,
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
  serialized_start=1409,
  serialized_end=1466,
)


_GS2CPLAYERPROFILE = _descriptor.Descriptor(
  name='GS2CPlayerProfile',
  full_name='GS2CPlayerProfile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='profile_list', full_name='GS2CPlayerProfile.profile_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='GS2CPlayerProfile.flag', index=1,
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
  serialized_start=1468,
  serialized_end=1544,
)

_LOGINFRIENDCHAT.fields_by_name['chat_list'].message_type = _SINGLECHAT
_GS2CLOGINFRIEND.fields_by_name['friend_chat_list'].message_type = _LOGINFRIENDCHAT
_GS2CLOGINFRIEND.fields_by_name['friend_onlinestatus_list'].message_type = _ONLINESTATUSINFO
_GS2CADDFRIEND.fields_by_name['profile_list'].message_type = base_dot_common__pb2._FRIENDPROFILE
_GS2CRECOMMENDFRIENDS.fields_by_name['recommend_friend_list'].message_type = _RECOMMENDFRIEND
_GS2CSTRANGERPROFILE.fields_by_name['profile_list'].message_type = base_dot_common__pb2._FRIENDPROFILE
_GS2CREFRESHFRIENDPROFILE.fields_by_name['profile'].message_type = base_dot_common__pb2._FRIENDPROFILE
_GS2CVERIFYFRIENDCONFIRM.fields_by_name['verify_list'].message_type = _VERIFYFRIENDCONFIRM
_GS2CPLAYERPROFILE.fields_by_name['profile_list'].message_type = base_dot_common__pb2._FRIENDPROFILE
DESCRIPTOR.message_types_by_name['SingleChat'] = _SINGLECHAT
DESCRIPTOR.message_types_by_name['LoginFriendChat'] = _LOGINFRIENDCHAT
DESCRIPTOR.message_types_by_name['RecommendFriend'] = _RECOMMENDFRIEND
DESCRIPTOR.message_types_by_name['OnlineStatusInfo'] = _ONLINESTATUSINFO
DESCRIPTOR.message_types_by_name['GS2CLoginFriend'] = _GS2CLOGINFRIEND
DESCRIPTOR.message_types_by_name['GS2CAddFriend'] = _GS2CADDFRIEND
DESCRIPTOR.message_types_by_name['GS2CDelFriend'] = _GS2CDELFRIEND
DESCRIPTOR.message_types_by_name['GS2CUpdateFriendDegree'] = _GS2CUPDATEFRIENDDEGREE
DESCRIPTOR.message_types_by_name['GS2CAckChatTo'] = _GS2CACKCHATTO
DESCRIPTOR.message_types_by_name['GS2CChatFrom'] = _GS2CCHATFROM
DESCRIPTOR.message_types_by_name['GS2CRecommendFriends'] = _GS2CRECOMMENDFRIENDS
DESCRIPTOR.message_types_by_name['GS2CStrangerProfile'] = _GS2CSTRANGERPROFILE
DESCRIPTOR.message_types_by_name['GS2CFriendShield'] = _GS2CFRIENDSHIELD
DESCRIPTOR.message_types_by_name['GS2CFriendUnshield'] = _GS2CFRIENDUNSHIELD
DESCRIPTOR.message_types_by_name['GS2COpenSendFlowerUI'] = _GS2COPENSENDFLOWERUI
DESCRIPTOR.message_types_by_name['GS2CSendFlowerSuccess'] = _GS2CSENDFLOWERSUCCESS
DESCRIPTOR.message_types_by_name['GS2CRefreshFriendProfile'] = _GS2CREFRESHFRIENDPROFILE
DESCRIPTOR.message_types_by_name['GS2CVerifyFriend'] = _GS2CVERIFYFRIEND
DESCRIPTOR.message_types_by_name['VerifyFriendConfirm'] = _VERIFYFRIENDCONFIRM
DESCRIPTOR.message_types_by_name['GS2CVerifyFriendConfirm'] = _GS2CVERIFYFRIENDCONFIRM
DESCRIPTOR.message_types_by_name['GS2CNotifyRefuseStrangerMsg'] = _GS2CNOTIFYREFUSESTRANGERMSG
DESCRIPTOR.message_types_by_name['GS2CRefreshFriendProfileBoth'] = _GS2CREFRESHFRIENDPROFILEBOTH
DESCRIPTOR.message_types_by_name['GS2CPlayerProfile'] = _GS2CPLAYERPROFILE

SingleChat = _reflection.GeneratedProtocolMessageType('SingleChat', (_message.Message,), dict(
  DESCRIPTOR = _SINGLECHAT,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:SingleChat)
  ))
_sym_db.RegisterMessage(SingleChat)

LoginFriendChat = _reflection.GeneratedProtocolMessageType('LoginFriendChat', (_message.Message,), dict(
  DESCRIPTOR = _LOGINFRIENDCHAT,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:LoginFriendChat)
  ))
_sym_db.RegisterMessage(LoginFriendChat)

RecommendFriend = _reflection.GeneratedProtocolMessageType('RecommendFriend', (_message.Message,), dict(
  DESCRIPTOR = _RECOMMENDFRIEND,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:RecommendFriend)
  ))
_sym_db.RegisterMessage(RecommendFriend)

OnlineStatusInfo = _reflection.GeneratedProtocolMessageType('OnlineStatusInfo', (_message.Message,), dict(
  DESCRIPTOR = _ONLINESTATUSINFO,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:OnlineStatusInfo)
  ))
_sym_db.RegisterMessage(OnlineStatusInfo)

GS2CLoginFriend = _reflection.GeneratedProtocolMessageType('GS2CLoginFriend', (_message.Message,), dict(
  DESCRIPTOR = _GS2CLOGINFRIEND,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CLoginFriend)
  ))
_sym_db.RegisterMessage(GS2CLoginFriend)

GS2CAddFriend = _reflection.GeneratedProtocolMessageType('GS2CAddFriend', (_message.Message,), dict(
  DESCRIPTOR = _GS2CADDFRIEND,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CAddFriend)
  ))
_sym_db.RegisterMessage(GS2CAddFriend)

GS2CDelFriend = _reflection.GeneratedProtocolMessageType('GS2CDelFriend', (_message.Message,), dict(
  DESCRIPTOR = _GS2CDELFRIEND,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CDelFriend)
  ))
_sym_db.RegisterMessage(GS2CDelFriend)

GS2CUpdateFriendDegree = _reflection.GeneratedProtocolMessageType('GS2CUpdateFriendDegree', (_message.Message,), dict(
  DESCRIPTOR = _GS2CUPDATEFRIENDDEGREE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CUpdateFriendDegree)
  ))
_sym_db.RegisterMessage(GS2CUpdateFriendDegree)

GS2CAckChatTo = _reflection.GeneratedProtocolMessageType('GS2CAckChatTo', (_message.Message,), dict(
  DESCRIPTOR = _GS2CACKCHATTO,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CAckChatTo)
  ))
_sym_db.RegisterMessage(GS2CAckChatTo)

GS2CChatFrom = _reflection.GeneratedProtocolMessageType('GS2CChatFrom', (_message.Message,), dict(
  DESCRIPTOR = _GS2CCHATFROM,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CChatFrom)
  ))
_sym_db.RegisterMessage(GS2CChatFrom)

GS2CRecommendFriends = _reflection.GeneratedProtocolMessageType('GS2CRecommendFriends', (_message.Message,), dict(
  DESCRIPTOR = _GS2CRECOMMENDFRIENDS,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CRecommendFriends)
  ))
_sym_db.RegisterMessage(GS2CRecommendFriends)

GS2CStrangerProfile = _reflection.GeneratedProtocolMessageType('GS2CStrangerProfile', (_message.Message,), dict(
  DESCRIPTOR = _GS2CSTRANGERPROFILE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CStrangerProfile)
  ))
_sym_db.RegisterMessage(GS2CStrangerProfile)

GS2CFriendShield = _reflection.GeneratedProtocolMessageType('GS2CFriendShield', (_message.Message,), dict(
  DESCRIPTOR = _GS2CFRIENDSHIELD,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CFriendShield)
  ))
_sym_db.RegisterMessage(GS2CFriendShield)

GS2CFriendUnshield = _reflection.GeneratedProtocolMessageType('GS2CFriendUnshield', (_message.Message,), dict(
  DESCRIPTOR = _GS2CFRIENDUNSHIELD,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CFriendUnshield)
  ))
_sym_db.RegisterMessage(GS2CFriendUnshield)

GS2COpenSendFlowerUI = _reflection.GeneratedProtocolMessageType('GS2COpenSendFlowerUI', (_message.Message,), dict(
  DESCRIPTOR = _GS2COPENSENDFLOWERUI,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2COpenSendFlowerUI)
  ))
_sym_db.RegisterMessage(GS2COpenSendFlowerUI)

GS2CSendFlowerSuccess = _reflection.GeneratedProtocolMessageType('GS2CSendFlowerSuccess', (_message.Message,), dict(
  DESCRIPTOR = _GS2CSENDFLOWERSUCCESS,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CSendFlowerSuccess)
  ))
_sym_db.RegisterMessage(GS2CSendFlowerSuccess)

GS2CRefreshFriendProfile = _reflection.GeneratedProtocolMessageType('GS2CRefreshFriendProfile', (_message.Message,), dict(
  DESCRIPTOR = _GS2CREFRESHFRIENDPROFILE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CRefreshFriendProfile)
  ))
_sym_db.RegisterMessage(GS2CRefreshFriendProfile)

GS2CVerifyFriend = _reflection.GeneratedProtocolMessageType('GS2CVerifyFriend', (_message.Message,), dict(
  DESCRIPTOR = _GS2CVERIFYFRIEND,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CVerifyFriend)
  ))
_sym_db.RegisterMessage(GS2CVerifyFriend)

VerifyFriendConfirm = _reflection.GeneratedProtocolMessageType('VerifyFriendConfirm', (_message.Message,), dict(
  DESCRIPTOR = _VERIFYFRIENDCONFIRM,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:VerifyFriendConfirm)
  ))
_sym_db.RegisterMessage(VerifyFriendConfirm)

GS2CVerifyFriendConfirm = _reflection.GeneratedProtocolMessageType('GS2CVerifyFriendConfirm', (_message.Message,), dict(
  DESCRIPTOR = _GS2CVERIFYFRIENDCONFIRM,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CVerifyFriendConfirm)
  ))
_sym_db.RegisterMessage(GS2CVerifyFriendConfirm)

GS2CNotifyRefuseStrangerMsg = _reflection.GeneratedProtocolMessageType('GS2CNotifyRefuseStrangerMsg', (_message.Message,), dict(
  DESCRIPTOR = _GS2CNOTIFYREFUSESTRANGERMSG,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CNotifyRefuseStrangerMsg)
  ))
_sym_db.RegisterMessage(GS2CNotifyRefuseStrangerMsg)

GS2CRefreshFriendProfileBoth = _reflection.GeneratedProtocolMessageType('GS2CRefreshFriendProfileBoth', (_message.Message,), dict(
  DESCRIPTOR = _GS2CREFRESHFRIENDPROFILEBOTH,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CRefreshFriendProfileBoth)
  ))
_sym_db.RegisterMessage(GS2CRefreshFriendProfileBoth)

GS2CPlayerProfile = _reflection.GeneratedProtocolMessageType('GS2CPlayerProfile', (_message.Message,), dict(
  DESCRIPTOR = _GS2CPLAYERPROFILE,
  __module__ = 'friend_pb2'
  # @@protoc_insertion_point(class_scope:GS2CPlayerProfile)
  ))
_sym_db.RegisterMessage(GS2CPlayerProfile)


# @@protoc_insertion_point(module_scope)
