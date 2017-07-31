# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_channel_reward.proto',
  package='',
  serialized_pb='\n\x18msg_channel_reward.proto\x1a\x0emsg_base.proto\".\n\x0bPBOneReward\x12\x12\n\nitem_sheet\x18\x01 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x11\"\x98\x01\n\x0fPBOneRewardInfo\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x1c\n\x06reward\x18\x02 \x03(\x0b\x32\x0c.PBOneReward\x12\x1e\n\tgetreward\x18\x04 \x01(\x0e\x32\x0b.EGetReward\x12\x0b\n\x03idx\x18\x05 \x01(\x11\x12\x14\n\x0c\x63urbegintime\x18\x06 \x01(\t\x12\x12\n\ncurendtime\x18\x07 \x01(\t\"\x9a\x01\n\x1aPBMsgQQGetRewardListNotice\x12\x11\n\tbegintime\x18\x01 \x01(\x11\x12\x0f\n\x07\x65ndtime\x18\x02 \x01(\x11\x12\'\n\ronerewardinfo\x18\x03 \x03(\x0b\x32\x10.PBOneRewardInfo\x12\x0f\n\x07nowused\x18\x04 \x01(\x11\x12\x1e\n\topenstate\x18\x05 \x01(\x0e\x32\x0b.EOpenState\"\x19\n\x17PBMsgQQGetRewardRequest\"9\n\x18PBMsgQQGetRewardResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x0b\n\x03idx\x18\x02 \x01(\x11*7\n\nEOpenState\x12\x13\n\x0f\x45OpenState_Open\x10\x01\x12\x14\n\x10\x45OpenState_Close\x10\x02*=\n\nEGetReward\x12\x15\n\x11\x45GetReward_Pickup\x10\x01\x12\x18\n\x14\x45GetReward_Un_Pickup\x10\x02')

_EOPENSTATE = descriptor.EnumDescriptor(
  name='EOpenState',
  full_name='EOpenState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='EOpenState_Open', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EOpenState_Close', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=490,
  serialized_end=545,
)


_EGETREWARD = descriptor.EnumDescriptor(
  name='EGetReward',
  full_name='EGetReward',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='EGetReward_Pickup', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EGetReward_Un_Pickup', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=547,
  serialized_end=608,
)


EOpenState_Open = 1
EOpenState_Close = 2
EGetReward_Pickup = 1
EGetReward_Un_Pickup = 2



_PBONEREWARD = descriptor.Descriptor(
  name='PBOneReward',
  full_name='PBOneReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='item_sheet', full_name='PBOneReward.item_sheet', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='num', full_name='PBOneReward.num', index=1,
      number=2, type=17, cpp_type=1, label=1,
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
  extension_ranges=[],
  serialized_start=44,
  serialized_end=90,
)


_PBONEREWARDINFO = descriptor.Descriptor(
  name='PBOneRewardInfo',
  full_name='PBOneRewardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBOneRewardInfo.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reward', full_name='PBOneRewardInfo.reward', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='getreward', full_name='PBOneRewardInfo.getreward', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='idx', full_name='PBOneRewardInfo.idx', index=3,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curbegintime', full_name='PBOneRewardInfo.curbegintime', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='curendtime', full_name='PBOneRewardInfo.curendtime', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=93,
  serialized_end=245,
)


_PBMSGQQGETREWARDLISTNOTICE = descriptor.Descriptor(
  name='PBMsgQQGetRewardListNotice',
  full_name='PBMsgQQGetRewardListNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='begintime', full_name='PBMsgQQGetRewardListNotice.begintime', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='endtime', full_name='PBMsgQQGetRewardListNotice.endtime', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='onerewardinfo', full_name='PBMsgQQGetRewardListNotice.onerewardinfo', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nowused', full_name='PBMsgQQGetRewardListNotice.nowused', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='openstate', full_name='PBMsgQQGetRewardListNotice.openstate', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  extension_ranges=[],
  serialized_start=248,
  serialized_end=402,
)


_PBMSGQQGETREWARDREQUEST = descriptor.Descriptor(
  name='PBMsgQQGetRewardRequest',
  full_name='PBMsgQQGetRewardRequest',
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
  extension_ranges=[],
  serialized_start=404,
  serialized_end=429,
)


_PBMSGQQGETREWARDRESPONSE = descriptor.Descriptor(
  name='PBMsgQQGetRewardResponse',
  full_name='PBMsgQQGetRewardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgQQGetRewardResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='idx', full_name='PBMsgQQGetRewardResponse.idx', index=1,
      number=2, type=17, cpp_type=1, label=1,
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
  extension_ranges=[],
  serialized_start=431,
  serialized_end=488,
)

_PBONEREWARDINFO.fields_by_name['reward'].message_type = _PBONEREWARD
_PBONEREWARDINFO.fields_by_name['getreward'].enum_type = _EGETREWARD
_PBMSGQQGETREWARDLISTNOTICE.fields_by_name['onerewardinfo'].message_type = _PBONEREWARDINFO
_PBMSGQQGETREWARDLISTNOTICE.fields_by_name['openstate'].enum_type = _EOPENSTATE
DESCRIPTOR.message_types_by_name['PBOneReward'] = _PBONEREWARD
DESCRIPTOR.message_types_by_name['PBOneRewardInfo'] = _PBONEREWARDINFO
DESCRIPTOR.message_types_by_name['PBMsgQQGetRewardListNotice'] = _PBMSGQQGETREWARDLISTNOTICE
DESCRIPTOR.message_types_by_name['PBMsgQQGetRewardRequest'] = _PBMSGQQGETREWARDREQUEST
DESCRIPTOR.message_types_by_name['PBMsgQQGetRewardResponse'] = _PBMSGQQGETREWARDRESPONSE

class PBOneReward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONEREWARD
  
  # @@protoc_insertion_point(class_scope:PBOneReward)

class PBOneRewardInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONEREWARDINFO
  
  # @@protoc_insertion_point(class_scope:PBOneRewardInfo)

class PBMsgQQGetRewardListNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGQQGETREWARDLISTNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgQQGetRewardListNotice)

class PBMsgQQGetRewardRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGQQGETREWARDREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgQQGetRewardRequest)

class PBMsgQQGetRewardResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGQQGETREWARDRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgQQGetRewardResponse)

# @@protoc_insertion_point(module_scope)
