# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2
import msg_couplepvp_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_couplepvp.proto',
  package='',
  serialized_pb='\n\x14tmpl_couplepvp.proto\x1a\x0ftmpl_base.proto\x1a\x13msg_couplepvp.proto\"\x98\x01\n\x0ePBConfigCouple\x12 \n\x07\x61\x63t_ctl\x18\x01 \x01(\x0b\x32\x0f.PBCoupleActCtl\x12+\n\x0b\x64ungeon_cfg\x18\x02 \x01(\x0b\x32\x16.PBCouplePVPDungeonCfg\x12$\n\taward_cfg\x18\x03 \x01(\x0b\x32\x11.PBCoupleAwardCfg\x12\x11\n\tact_sheet\x18\x04 \x01(\t\"\x92\x01\n\x0ePBCoupleActCtl\x12\x1e\n\x04\x64\x61te\x18\x01 \x03(\x0b\x32\x10.PBCoupleActDate\x12\x11\n\tsign_time\x18\x02 \x01(\x11\x12\x12\n\nmax_couple\x18\x03 \x01(\x11\x12\x15\n\rclient_update\x18\x04 \x01(\x11\x12\"\n\x08\x61\x63t_time\x18\x05 \x03(\x0b\x32\x10.PBCoupleActTime\"-\n\x0fPBCoupleActDate\x12\x0c\n\x04week\x18\x01 \x01(\x11\x12\x0c\n\x04time\x18\x02 \x01(\t\"\xa9\x01\n\x0fPBCoupleActTime\x12\x13\n\x0bround_index\x18\x01 \x01(\x11\x12\x15\n\rdungeon_sheet\x18\x02 \x01(\t\x12\x12\n\nround_type\x18\x03 \x01(\x11\x12\x14\n\x0c\x64ungeon_time\x18\x04 \x01(\x11\x12\x11\n\trest_time\x18\x05 \x01(\x11\x12\x17\n\x0f\x64ungeon_gateway\x18\x06 \x01(\x11\x12\x14\n\x0c\x64ungeon_camp\x18\x07 \x01(\x11\"\x7f\n\x0fPBCouplePVPList\x12\x0f\n\x07\x62uff_id\x18\x01 \x01(\x11\x12\x10\n\x08min_rate\x18\x02 \x01(\x11\x12\x10\n\x08max_rate\x18\x03 \x01(\x11\x12\x11\n\tbuff_time\x18\x04 \x01(\x11\x12\x11\n\tbuff_name\x18\x05 \x01(\t\x12\x11\n\tbuff_desc\x18\x06 \x01(\t\"\xd6\x02\n\x15PBCouplePVPDungeonCfg\x12\x0f\n\x07\x62uff_id\x18\x01 \x01(\x11\x12\x11\n\twin_score\x18\x02 \x01(\x11\x12\x11\n\tintertime\x18\x03 \x01(\x11\x12\x11\n\tscore_val\x18\x04 \x01(\x11\x12\x17\n\x0fsure_buff_count\x18\x05 \x01(\x11\x12\x11\n\tbuff_rate\x18\x06 \x01(\x11\x12\x11\n\tbuff_name\x18\x07 \x01(\t\x12\x11\n\tbuff_desc\x18\x08 \x01(\t\x12#\n\tbuff_list\x18\t \x03(\x0b\x32\x10.PBCouplePVPList\x12\x13\n\x0bnotice_time\x18\n \x01(\x11\x12\x11\n\tover_time\x18\x0b \x01(\x11\x12\x10\n\x08off_time\x18\x0c \x01(\x11\x12\x12\n\nready_time\x18\r \x01(\x11\x12\x15\n\renter_buff_id\x18\x0e \x01(\x11\x12\x17\n\x0f\x65nter_buff_time\x18\x0f \x01(\x11\"f\n\x10PBCoupleAwardCfg\x12(\n\x0b\x66loor_award\x18\x01 \x03(\x0b\x32\x13.PBCoupleFloorAward\x12(\n\x0b\x66irst_award\x18\x02 \x01(\x0b\x32\x13.PBCoupleFloorAward')




_PBCONFIGCOUPLE = descriptor.Descriptor(
  name='PBConfigCouple',
  full_name='PBConfigCouple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='act_ctl', full_name='PBConfigCouple.act_ctl', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dungeon_cfg', full_name='PBConfigCouple.dungeon_cfg', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='award_cfg', full_name='PBConfigCouple.award_cfg', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_sheet', full_name='PBConfigCouple.act_sheet', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=63,
  serialized_end=215,
)


_PBCOUPLEACTCTL = descriptor.Descriptor(
  name='PBCoupleActCtl',
  full_name='PBCoupleActCtl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='date', full_name='PBCoupleActCtl.date', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sign_time', full_name='PBCoupleActCtl.sign_time', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_couple', full_name='PBCoupleActCtl.max_couple', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='client_update', full_name='PBCoupleActCtl.client_update', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_time', full_name='PBCoupleActCtl.act_time', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=218,
  serialized_end=364,
)


_PBCOUPLEACTDATE = descriptor.Descriptor(
  name='PBCoupleActDate',
  full_name='PBCoupleActDate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='week', full_name='PBCoupleActDate.week', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time', full_name='PBCoupleActDate.time', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=366,
  serialized_end=411,
)


_PBCOUPLEACTTIME = descriptor.Descriptor(
  name='PBCoupleActTime',
  full_name='PBCoupleActTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='round_index', full_name='PBCoupleActTime.round_index', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dungeon_sheet', full_name='PBCoupleActTime.dungeon_sheet', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='round_type', full_name='PBCoupleActTime.round_type', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dungeon_time', full_name='PBCoupleActTime.dungeon_time', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rest_time', full_name='PBCoupleActTime.rest_time', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dungeon_gateway', full_name='PBCoupleActTime.dungeon_gateway', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dungeon_camp', full_name='PBCoupleActTime.dungeon_camp', index=6,
      number=7, type=17, cpp_type=1, label=1,
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
  serialized_start=414,
  serialized_end=583,
)


_PBCOUPLEPVPLIST = descriptor.Descriptor(
  name='PBCouplePVPList',
  full_name='PBCouplePVPList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='buff_id', full_name='PBCouplePVPList.buff_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='min_rate', full_name='PBCouplePVPList.min_rate', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_rate', full_name='PBCouplePVPList.max_rate', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buff_time', full_name='PBCouplePVPList.buff_time', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buff_name', full_name='PBCouplePVPList.buff_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buff_desc', full_name='PBCouplePVPList.buff_desc', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=585,
  serialized_end=712,
)


_PBCOUPLEPVPDUNGEONCFG = descriptor.Descriptor(
  name='PBCouplePVPDungeonCfg',
  full_name='PBCouplePVPDungeonCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='buff_id', full_name='PBCouplePVPDungeonCfg.buff_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='win_score', full_name='PBCouplePVPDungeonCfg.win_score', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='intertime', full_name='PBCouplePVPDungeonCfg.intertime', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_val', full_name='PBCouplePVPDungeonCfg.score_val', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sure_buff_count', full_name='PBCouplePVPDungeonCfg.sure_buff_count', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buff_rate', full_name='PBCouplePVPDungeonCfg.buff_rate', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buff_name', full_name='PBCouplePVPDungeonCfg.buff_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buff_desc', full_name='PBCouplePVPDungeonCfg.buff_desc', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buff_list', full_name='PBCouplePVPDungeonCfg.buff_list', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='notice_time', full_name='PBCouplePVPDungeonCfg.notice_time', index=9,
      number=10, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='over_time', full_name='PBCouplePVPDungeonCfg.over_time', index=10,
      number=11, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='off_time', full_name='PBCouplePVPDungeonCfg.off_time', index=11,
      number=12, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ready_time', full_name='PBCouplePVPDungeonCfg.ready_time', index=12,
      number=13, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enter_buff_id', full_name='PBCouplePVPDungeonCfg.enter_buff_id', index=13,
      number=14, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enter_buff_time', full_name='PBCouplePVPDungeonCfg.enter_buff_time', index=14,
      number=15, type=17, cpp_type=1, label=1,
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
  serialized_start=715,
  serialized_end=1057,
)


_PBCOUPLEAWARDCFG = descriptor.Descriptor(
  name='PBCoupleAwardCfg',
  full_name='PBCoupleAwardCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='floor_award', full_name='PBCoupleAwardCfg.floor_award', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='first_award', full_name='PBCoupleAwardCfg.first_award', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=1059,
  serialized_end=1161,
)

_PBCONFIGCOUPLE.fields_by_name['act_ctl'].message_type = _PBCOUPLEACTCTL
_PBCONFIGCOUPLE.fields_by_name['dungeon_cfg'].message_type = _PBCOUPLEPVPDUNGEONCFG
_PBCONFIGCOUPLE.fields_by_name['award_cfg'].message_type = _PBCOUPLEAWARDCFG
_PBCOUPLEACTCTL.fields_by_name['date'].message_type = _PBCOUPLEACTDATE
_PBCOUPLEACTCTL.fields_by_name['act_time'].message_type = _PBCOUPLEACTTIME
_PBCOUPLEPVPDUNGEONCFG.fields_by_name['buff_list'].message_type = _PBCOUPLEPVPLIST
_PBCOUPLEAWARDCFG.fields_by_name['floor_award'].message_type = msg_couplepvp_pb2._PBCOUPLEFLOORAWARD
_PBCOUPLEAWARDCFG.fields_by_name['first_award'].message_type = msg_couplepvp_pb2._PBCOUPLEFLOORAWARD
DESCRIPTOR.message_types_by_name['PBConfigCouple'] = _PBCONFIGCOUPLE
DESCRIPTOR.message_types_by_name['PBCoupleActCtl'] = _PBCOUPLEACTCTL
DESCRIPTOR.message_types_by_name['PBCoupleActDate'] = _PBCOUPLEACTDATE
DESCRIPTOR.message_types_by_name['PBCoupleActTime'] = _PBCOUPLEACTTIME
DESCRIPTOR.message_types_by_name['PBCouplePVPList'] = _PBCOUPLEPVPLIST
DESCRIPTOR.message_types_by_name['PBCouplePVPDungeonCfg'] = _PBCOUPLEPVPDUNGEONCFG
DESCRIPTOR.message_types_by_name['PBCoupleAwardCfg'] = _PBCOUPLEAWARDCFG

class PBConfigCouple(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGCOUPLE
  
  # @@protoc_insertion_point(class_scope:PBConfigCouple)

class PBCoupleActCtl(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCOUPLEACTCTL
  
  # @@protoc_insertion_point(class_scope:PBCoupleActCtl)

class PBCoupleActDate(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCOUPLEACTDATE
  
  # @@protoc_insertion_point(class_scope:PBCoupleActDate)

class PBCoupleActTime(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCOUPLEACTTIME
  
  # @@protoc_insertion_point(class_scope:PBCoupleActTime)

class PBCouplePVPList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCOUPLEPVPLIST
  
  # @@protoc_insertion_point(class_scope:PBCouplePVPList)

class PBCouplePVPDungeonCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCOUPLEPVPDUNGEONCFG
  
  # @@protoc_insertion_point(class_scope:PBCouplePVPDungeonCfg)

class PBCoupleAwardCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCOUPLEAWARDCFG
  
  # @@protoc_insertion_point(class_scope:PBCoupleAwardCfg)

# @@protoc_insertion_point(module_scope)
