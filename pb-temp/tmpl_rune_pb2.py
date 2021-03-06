# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_rune.proto',
  package='',
  serialized_pb='\n\x0ftmpl_rune.proto\x1a\x0ftmpl_base.proto\"\x90\x01\n\x10PBRuneLotteryCfg\x12%\n\tslot_info\x18\x01 \x03(\x0b\x32\x12.PBRuneLotteryList\x12&\n\rruneslot_info\x18\x02 \x01(\x0b\x32\x0f.PBRuneSlotInfo\x12-\n\x0frunereward_info\x18\x03 \x03(\x0b\x32\x14.PBRuneLotteryReward\"\x99\x01\n\x11PBRuneLotteryList\x12\x14\n\x0clottery_slot\x18\x01 \x01(\x11\x12\x16\n\x0enextslot_ratio\x18\x02 \x01(\x11\x12\x12\n\ncost_sheet\x18\x03 \x01(\t\x12\x10\n\x08one_cost\x18\x04 \x01(\x11\x12\x10\n\x08ten_cost\x18\x05 \x01(\x11\x12\x1e\n\trune_info\x18\x06 \x03(\x0b\x32\x0b.PBRuneList\"/\n\nPBRuneList\x12\x12\n\nrune_sheet\x18\x01 \x01(\t\x12\r\n\x05ratio\x18\x02 \x01(\x11\"\x8a\x01\n\x0ePBRuneSlotInfo\x12\x14\n\x0cinit_opennum\x18\x01 \x01(\x11\x12\x13\n\x0bmax_opennum\x18\x02 \x01(\x11\x12&\n\topen_slot\x18\x03 \x03(\x0b\x32\x13.PBRuneSlotOpenInfo\x12\x12\n\ncost_sheet\x18\x04 \x01(\t\x12\x11\n\tcost_rate\x18\x05 \x01(\x02\"Z\n\x12PBRuneSlotOpenInfo\x12\x0f\n\x07slot_id\x18\x01 \x01(\x11\x12\r\n\x05level\x18\x02 \x01(\x11\x12\x12\n\ncost_sheet\x18\x03 \x01(\t\x12\x10\n\x08\x63ost_num\x18\x04 \x01(\x11\"Z\n\x13PBRuneLotteryReward\x12\x14\n\x0clottery_time\x18\x01 \x01(\x11\x12-\n\x0breward_list\x18\x02 \x03(\x0b\x32\x18.PBRuneLotteryRewardItem\"Q\n\x17PBRuneLotteryRewardItem\x12\x14\n\x0creward_sheet\x18\x01 \x01(\t\x12\x12\n\nreward_num\x18\x02 \x01(\x11\x12\x0c\n\x04odds\x18\x03 \x01(\x11')




_PBRUNELOTTERYCFG = descriptor.Descriptor(
  name='PBRuneLotteryCfg',
  full_name='PBRuneLotteryCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBRuneLotteryCfg.slot_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='runeslot_info', full_name='PBRuneLotteryCfg.runeslot_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='runereward_info', full_name='PBRuneLotteryCfg.runereward_info', index=2,
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
  extension_ranges=[],
  serialized_start=37,
  serialized_end=181,
)


_PBRUNELOTTERYLIST = descriptor.Descriptor(
  name='PBRuneLotteryList',
  full_name='PBRuneLotteryList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='lottery_slot', full_name='PBRuneLotteryList.lottery_slot', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='nextslot_ratio', full_name='PBRuneLotteryList.nextslot_ratio', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_sheet', full_name='PBRuneLotteryList.cost_sheet', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='one_cost', full_name='PBRuneLotteryList.one_cost', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ten_cost', full_name='PBRuneLotteryList.ten_cost', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rune_info', full_name='PBRuneLotteryList.rune_info', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  extension_ranges=[],
  serialized_start=184,
  serialized_end=337,
)


_PBRUNELIST = descriptor.Descriptor(
  name='PBRuneList',
  full_name='PBRuneList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='rune_sheet', full_name='PBRuneList.rune_sheet', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ratio', full_name='PBRuneList.ratio', index=1,
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
  serialized_start=339,
  serialized_end=386,
)


_PBRUNESLOTINFO = descriptor.Descriptor(
  name='PBRuneSlotInfo',
  full_name='PBRuneSlotInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='init_opennum', full_name='PBRuneSlotInfo.init_opennum', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_opennum', full_name='PBRuneSlotInfo.max_opennum', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='open_slot', full_name='PBRuneSlotInfo.open_slot', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_sheet', full_name='PBRuneSlotInfo.cost_sheet', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_rate', full_name='PBRuneSlotInfo.cost_rate', index=4,
      number=5, type=2, cpp_type=6, label=1,
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
  serialized_start=389,
  serialized_end=527,
)


_PBRUNESLOTOPENINFO = descriptor.Descriptor(
  name='PBRuneSlotOpenInfo',
  full_name='PBRuneSlotOpenInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='slot_id', full_name='PBRuneSlotOpenInfo.slot_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='PBRuneSlotOpenInfo.level', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_sheet', full_name='PBRuneSlotOpenInfo.cost_sheet', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_num', full_name='PBRuneSlotOpenInfo.cost_num', index=3,
      number=4, type=17, cpp_type=1, label=1,
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
  serialized_start=529,
  serialized_end=619,
)


_PBRUNELOTTERYREWARD = descriptor.Descriptor(
  name='PBRuneLotteryReward',
  full_name='PBRuneLotteryReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='lottery_time', full_name='PBRuneLotteryReward.lottery_time', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reward_list', full_name='PBRuneLotteryReward.reward_list', index=1,
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
  extension_ranges=[],
  serialized_start=621,
  serialized_end=711,
)


_PBRUNELOTTERYREWARDITEM = descriptor.Descriptor(
  name='PBRuneLotteryRewardItem',
  full_name='PBRuneLotteryRewardItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reward_sheet', full_name='PBRuneLotteryRewardItem.reward_sheet', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reward_num', full_name='PBRuneLotteryRewardItem.reward_num', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='odds', full_name='PBRuneLotteryRewardItem.odds', index=2,
      number=3, type=17, cpp_type=1, label=1,
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
  serialized_start=713,
  serialized_end=794,
)

_PBRUNELOTTERYCFG.fields_by_name['slot_info'].message_type = _PBRUNELOTTERYLIST
_PBRUNELOTTERYCFG.fields_by_name['runeslot_info'].message_type = _PBRUNESLOTINFO
_PBRUNELOTTERYCFG.fields_by_name['runereward_info'].message_type = _PBRUNELOTTERYREWARD
_PBRUNELOTTERYLIST.fields_by_name['rune_info'].message_type = _PBRUNELIST
_PBRUNESLOTINFO.fields_by_name['open_slot'].message_type = _PBRUNESLOTOPENINFO
_PBRUNELOTTERYREWARD.fields_by_name['reward_list'].message_type = _PBRUNELOTTERYREWARDITEM
DESCRIPTOR.message_types_by_name['PBRuneLotteryCfg'] = _PBRUNELOTTERYCFG
DESCRIPTOR.message_types_by_name['PBRuneLotteryList'] = _PBRUNELOTTERYLIST
DESCRIPTOR.message_types_by_name['PBRuneList'] = _PBRUNELIST
DESCRIPTOR.message_types_by_name['PBRuneSlotInfo'] = _PBRUNESLOTINFO
DESCRIPTOR.message_types_by_name['PBRuneSlotOpenInfo'] = _PBRUNESLOTOPENINFO
DESCRIPTOR.message_types_by_name['PBRuneLotteryReward'] = _PBRUNELOTTERYREWARD
DESCRIPTOR.message_types_by_name['PBRuneLotteryRewardItem'] = _PBRUNELOTTERYREWARDITEM

class PBRuneLotteryCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRUNELOTTERYCFG
  
  # @@protoc_insertion_point(class_scope:PBRuneLotteryCfg)

class PBRuneLotteryList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRUNELOTTERYLIST
  
  # @@protoc_insertion_point(class_scope:PBRuneLotteryList)

class PBRuneList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRUNELIST
  
  # @@protoc_insertion_point(class_scope:PBRuneList)

class PBRuneSlotInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRUNESLOTINFO
  
  # @@protoc_insertion_point(class_scope:PBRuneSlotInfo)

class PBRuneSlotOpenInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRUNESLOTOPENINFO
  
  # @@protoc_insertion_point(class_scope:PBRuneSlotOpenInfo)

class PBRuneLotteryReward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRUNELOTTERYREWARD
  
  # @@protoc_insertion_point(class_scope:PBRuneLotteryReward)

class PBRuneLotteryRewardItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRUNELOTTERYREWARDITEM
  
  # @@protoc_insertion_point(class_scope:PBRuneLotteryRewardItem)

# @@protoc_insertion_point(module_scope)
