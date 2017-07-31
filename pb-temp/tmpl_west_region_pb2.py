# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2
import msg_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_west_region.proto',
  package='',
  serialized_pb='\n\x16tmpl_west_region.proto\x1a\x0ftmpl_base.proto\x1a\x0emsg_base.proto\"\x91\x01\n\x12PBWestRegionConfig\x12&\n\nbasic_info\x18\x01 \x01(\x0b\x32\x12.PBWestRegionBasic\x12&\n\nwest_group\x18\x02 \x03(\x0b\x32\x12.PBWestRegionGroup\x12+\n\x0cnpc_postions\x18\x03 \x03(\x0b\x32\x15.PBWestRegionPostions\"\xa2\x01\n\x11PBWestRegionBasic\x12\x15\n\rdelay_levelid\x18\x01 \x01(\x11\x12\x16\n\x0ewaring_percent\x18\x02 \x01(\x11\x12\x17\n\x0fnormail_percent\x18\x03 \x01(\x11\x12\x15\n\renter_percent\x18\x04 \x01(\x11\x12\x18\n\x10min_member_count\x18\x05 \x01(\x11\x12\x14\n\x0cmax_distance\x18\x06 \x01(\x11\"N\n\x11PBWestRegionGroup\x12\x0f\n\x07levelid\x18\x01 \x01(\x11\x12(\n\tnpc_group\x18\x02 \x03(\x0b\x32\x15.PBWestRegionNPCGroup\"\xff\x01\n\x14PBWestRegionNPCGroup\x12(\n\ngroup_info\x18\x01 \x03(\x0b\x32\x14.PBWestRegionNPCPair\x12\x15\n\rsuggest_power\x18\x02 \x01(\x11\x12\x16\n\x0etarget_dungeon\x18\x03 \x01(\t\x12\x16\n\x0e\x63reature_title\x18\x04 \x01(\t\x12$\n\tboss_info\x18\x05 \x03(\x0b\x32\x11.PBWestRegionBoss\x12\x11\n\tborn_line\x18\x06 \x01(\x11\x12\x12\n\nborn_mapid\x18\x07 \x01(\x11\x12)\n\naward_item\x18\x08 \x01(\x0b\x32\x15.PBWestRegionShowInfo\";\n\x13PBWestRegionNPCPair\x12\x10\n\x08group_id\x18\x01 \x01(\x11\x12\x12\n\ngroup_name\x18\x02 \x01(\t\"I\n\x10PBWestRegionBoss\x12\x14\n\x0c\x62oss_sheetid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\x11\n\ticon_name\x18\x04 \x01(\t\"@\n\x14PBWestRegionShowInfo\x12(\n\tshow_item\x18\x01 \x03(\x0b\x32\x15.PBWestRegionShowItem\"\'\n\x14PBWestRegionShowItem\x12\x0f\n\x07sheetid\x18\x01 \x01(\t\"E\n\x14PBWestRegionPostions\x12\x0e\n\x06map_id\x18\x01 \x01(\x11\x12\x1d\n\x08postions\x18\x02 \x03(\x0b\x32\x0b.PBAIVector')




_PBWESTREGIONCONFIG = descriptor.Descriptor(
  name='PBWestRegionConfig',
  full_name='PBWestRegionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='basic_info', full_name='PBWestRegionConfig.basic_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='west_group', full_name='PBWestRegionConfig.west_group', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_postions', full_name='PBWestRegionConfig.npc_postions', index=2,
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
  serialized_start=60,
  serialized_end=205,
)


_PBWESTREGIONBASIC = descriptor.Descriptor(
  name='PBWestRegionBasic',
  full_name='PBWestRegionBasic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='delay_levelid', full_name='PBWestRegionBasic.delay_levelid', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='waring_percent', full_name='PBWestRegionBasic.waring_percent', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='normail_percent', full_name='PBWestRegionBasic.normail_percent', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enter_percent', full_name='PBWestRegionBasic.enter_percent', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='min_member_count', full_name='PBWestRegionBasic.min_member_count', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_distance', full_name='PBWestRegionBasic.max_distance', index=5,
      number=6, type=17, cpp_type=1, label=1,
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
  serialized_start=208,
  serialized_end=370,
)


_PBWESTREGIONGROUP = descriptor.Descriptor(
  name='PBWestRegionGroup',
  full_name='PBWestRegionGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='levelid', full_name='PBWestRegionGroup.levelid', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_group', full_name='PBWestRegionGroup.npc_group', index=1,
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
  serialized_start=372,
  serialized_end=450,
)


_PBWESTREGIONNPCGROUP = descriptor.Descriptor(
  name='PBWestRegionNPCGroup',
  full_name='PBWestRegionNPCGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='group_info', full_name='PBWestRegionNPCGroup.group_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='suggest_power', full_name='PBWestRegionNPCGroup.suggest_power', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_dungeon', full_name='PBWestRegionNPCGroup.target_dungeon', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='creature_title', full_name='PBWestRegionNPCGroup.creature_title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='boss_info', full_name='PBWestRegionNPCGroup.boss_info', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='born_line', full_name='PBWestRegionNPCGroup.born_line', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='born_mapid', full_name='PBWestRegionNPCGroup.born_mapid', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='award_item', full_name='PBWestRegionNPCGroup.award_item', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=453,
  serialized_end=708,
)


_PBWESTREGIONNPCPAIR = descriptor.Descriptor(
  name='PBWestRegionNPCPair',
  full_name='PBWestRegionNPCPair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='group_id', full_name='PBWestRegionNPCPair.group_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='group_name', full_name='PBWestRegionNPCPair.group_name', index=1,
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
  serialized_start=710,
  serialized_end=769,
)


_PBWESTREGIONBOSS = descriptor.Descriptor(
  name='PBWestRegionBoss',
  full_name='PBWestRegionBoss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='boss_sheetid', full_name='PBWestRegionBoss.boss_sheetid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='desc', full_name='PBWestRegionBoss.desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='icon_name', full_name='PBWestRegionBoss.icon_name', index=2,
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
  serialized_start=771,
  serialized_end=844,
)


_PBWESTREGIONSHOWINFO = descriptor.Descriptor(
  name='PBWestRegionShowInfo',
  full_name='PBWestRegionShowInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='show_item', full_name='PBWestRegionShowInfo.show_item', index=0,
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
  extension_ranges=[],
  serialized_start=846,
  serialized_end=910,
)


_PBWESTREGIONSHOWITEM = descriptor.Descriptor(
  name='PBWestRegionShowItem',
  full_name='PBWestRegionShowItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sheetid', full_name='PBWestRegionShowItem.sheetid', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=912,
  serialized_end=951,
)


_PBWESTREGIONPOSTIONS = descriptor.Descriptor(
  name='PBWestRegionPostions',
  full_name='PBWestRegionPostions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='map_id', full_name='PBWestRegionPostions.map_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='postions', full_name='PBWestRegionPostions.postions', index=1,
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
  serialized_start=953,
  serialized_end=1022,
)

_PBWESTREGIONCONFIG.fields_by_name['basic_info'].message_type = _PBWESTREGIONBASIC
_PBWESTREGIONCONFIG.fields_by_name['west_group'].message_type = _PBWESTREGIONGROUP
_PBWESTREGIONCONFIG.fields_by_name['npc_postions'].message_type = _PBWESTREGIONPOSTIONS
_PBWESTREGIONGROUP.fields_by_name['npc_group'].message_type = _PBWESTREGIONNPCGROUP
_PBWESTREGIONNPCGROUP.fields_by_name['group_info'].message_type = _PBWESTREGIONNPCPAIR
_PBWESTREGIONNPCGROUP.fields_by_name['boss_info'].message_type = _PBWESTREGIONBOSS
_PBWESTREGIONNPCGROUP.fields_by_name['award_item'].message_type = _PBWESTREGIONSHOWINFO
_PBWESTREGIONSHOWINFO.fields_by_name['show_item'].message_type = _PBWESTREGIONSHOWITEM
_PBWESTREGIONPOSTIONS.fields_by_name['postions'].message_type = msg_base_pb2._PBAIVECTOR
DESCRIPTOR.message_types_by_name['PBWestRegionConfig'] = _PBWESTREGIONCONFIG
DESCRIPTOR.message_types_by_name['PBWestRegionBasic'] = _PBWESTREGIONBASIC
DESCRIPTOR.message_types_by_name['PBWestRegionGroup'] = _PBWESTREGIONGROUP
DESCRIPTOR.message_types_by_name['PBWestRegionNPCGroup'] = _PBWESTREGIONNPCGROUP
DESCRIPTOR.message_types_by_name['PBWestRegionNPCPair'] = _PBWESTREGIONNPCPAIR
DESCRIPTOR.message_types_by_name['PBWestRegionBoss'] = _PBWESTREGIONBOSS
DESCRIPTOR.message_types_by_name['PBWestRegionShowInfo'] = _PBWESTREGIONSHOWINFO
DESCRIPTOR.message_types_by_name['PBWestRegionShowItem'] = _PBWESTREGIONSHOWITEM
DESCRIPTOR.message_types_by_name['PBWestRegionPostions'] = _PBWESTREGIONPOSTIONS

class PBWestRegionConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONCONFIG
  
  # @@protoc_insertion_point(class_scope:PBWestRegionConfig)

class PBWestRegionBasic(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONBASIC
  
  # @@protoc_insertion_point(class_scope:PBWestRegionBasic)

class PBWestRegionGroup(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONGROUP
  
  # @@protoc_insertion_point(class_scope:PBWestRegionGroup)

class PBWestRegionNPCGroup(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONNPCGROUP
  
  # @@protoc_insertion_point(class_scope:PBWestRegionNPCGroup)

class PBWestRegionNPCPair(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONNPCPAIR
  
  # @@protoc_insertion_point(class_scope:PBWestRegionNPCPair)

class PBWestRegionBoss(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONBOSS
  
  # @@protoc_insertion_point(class_scope:PBWestRegionBoss)

class PBWestRegionShowInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONSHOWINFO
  
  # @@protoc_insertion_point(class_scope:PBWestRegionShowInfo)

class PBWestRegionShowItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONSHOWITEM
  
  # @@protoc_insertion_point(class_scope:PBWestRegionShowItem)

class PBWestRegionPostions(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWESTREGIONPOSTIONS
  
  # @@protoc_insertion_point(class_scope:PBWestRegionPostions)

# @@protoc_insertion_point(module_scope)