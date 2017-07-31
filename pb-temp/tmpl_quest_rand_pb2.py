# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_quest_rand.proto',
  package='',
  serialized_pb='\n\x15tmpl_quest_rand.proto\x1a\x0ftmpl_base.proto\"5\n\x0ePBQuestRandCfg\x12#\n\x05group\x18\x01 \x03(\x0b\x32\x14.PBQuestRandGroupCfg\"\xcb\x01\n\x13PBQuestRandGroupCfg\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x11\n\tcommitNum\x18\x02 \x01(\x11\x12\x11\n\tclearType\x18\x03 \x01(\x11\x12(\n\x0brandLibrary\x18\x04 \x03(\x0b\x32\x13.PBQuestRandLibrary\x12*\n\ncycleAward\x18\x05 \x03(\x0b\x32\x16.PBQuestRandCycleAward\x12,\n\x0b\x63ycleNotice\x18\x06 \x03(\x0b\x32\x17.PBQuestRandCycleNotice\"Q\n\x12PBQuestRandLibrary\x12\x11\n\tlibraryID\x18\x01 \x01(\x11\x12(\n\tcondition\x18\x02 \x03(\x0b\x32\x15.PBQuestRandCondition\"\xb6\x01\n\x14PBQuestRandCondition\x12\x1f\n\x04type\x18\x01 \x01(\x0e\x32\x11.PBEConditionType\x12\x10\n\x08minLevel\x18\x02 \x01(\x11\x12\x10\n\x08maxLevel\x18\x03 \x01(\x11\x12\x10\n\x08minCycle\x18\x04 \x01(\x11\x12\x10\n\x08maxCycle\x18\x05 \x01(\x11\x12\x19\n\x11guildBuildingType\x18\x06 \x01(\x11\x12\x1a\n\x12guildBuildingLevel\x18\x07 \x01(\x11\"6\n\x15PBQuestRandCycleAward\x12\x0f\n\x07\x63ycleID\x18\x01 \x01(\x11\x12\x0c\n\x04loot\x18\x02 \x01(\t\"9\n\x16PBQuestRandCycleNotice\x12\x0f\n\x07\x63ycleID\x18\x01 \x01(\x11\x12\x0e\n\x06notice\x18\x02 \x01(\t*q\n\x10PBEConditionType\x12\x13\n\x0f\x65\x43ondition_None\x10\x00\x12\x19\n\x15\x65\x43ondition_NormalRand\x10\x01\x12\x17\n\x13\x65\x43ondition_Building\x10\x02\x12\x14\n\x10\x65\x43ondition_Guild\x10\x03')

_PBECONDITIONTYPE = descriptor.EnumDescriptor(
  name='PBEConditionType',
  full_name='PBEConditionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='eCondition_None', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='eCondition_NormalRand', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='eCondition_Building', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='eCondition_Guild', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=686,
  serialized_end=799,
)


eCondition_None = 0
eCondition_NormalRand = 1
eCondition_Building = 2
eCondition_Guild = 3



_PBQUESTRANDCFG = descriptor.Descriptor(
  name='PBQuestRandCfg',
  full_name='PBQuestRandCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='group', full_name='PBQuestRandCfg.group', index=0,
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
  serialized_start=42,
  serialized_end=95,
)


_PBQUESTRANDGROUPCFG = descriptor.Descriptor(
  name='PBQuestRandGroupCfg',
  full_name='PBQuestRandGroupCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='PBQuestRandGroupCfg.id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='commitNum', full_name='PBQuestRandGroupCfg.commitNum', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='clearType', full_name='PBQuestRandGroupCfg.clearType', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='randLibrary', full_name='PBQuestRandGroupCfg.randLibrary', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cycleAward', full_name='PBQuestRandGroupCfg.cycleAward', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cycleNotice', full_name='PBQuestRandGroupCfg.cycleNotice', index=5,
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
  serialized_start=98,
  serialized_end=301,
)


_PBQUESTRANDLIBRARY = descriptor.Descriptor(
  name='PBQuestRandLibrary',
  full_name='PBQuestRandLibrary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='libraryID', full_name='PBQuestRandLibrary.libraryID', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='condition', full_name='PBQuestRandLibrary.condition', index=1,
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
  serialized_start=303,
  serialized_end=384,
)


_PBQUESTRANDCONDITION = descriptor.Descriptor(
  name='PBQuestRandCondition',
  full_name='PBQuestRandCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='PBQuestRandCondition.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='minLevel', full_name='PBQuestRandCondition.minLevel', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxLevel', full_name='PBQuestRandCondition.maxLevel', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='minCycle', full_name='PBQuestRandCondition.minCycle', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxCycle', full_name='PBQuestRandCondition.maxCycle', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='guildBuildingType', full_name='PBQuestRandCondition.guildBuildingType', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='guildBuildingLevel', full_name='PBQuestRandCondition.guildBuildingLevel', index=6,
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
  serialized_start=387,
  serialized_end=569,
)


_PBQUESTRANDCYCLEAWARD = descriptor.Descriptor(
  name='PBQuestRandCycleAward',
  full_name='PBQuestRandCycleAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cycleID', full_name='PBQuestRandCycleAward.cycleID', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='loot', full_name='PBQuestRandCycleAward.loot', index=1,
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
  serialized_start=571,
  serialized_end=625,
)


_PBQUESTRANDCYCLENOTICE = descriptor.Descriptor(
  name='PBQuestRandCycleNotice',
  full_name='PBQuestRandCycleNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cycleID', full_name='PBQuestRandCycleNotice.cycleID', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='notice', full_name='PBQuestRandCycleNotice.notice', index=1,
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
  serialized_start=627,
  serialized_end=684,
)

_PBQUESTRANDCFG.fields_by_name['group'].message_type = _PBQUESTRANDGROUPCFG
_PBQUESTRANDGROUPCFG.fields_by_name['randLibrary'].message_type = _PBQUESTRANDLIBRARY
_PBQUESTRANDGROUPCFG.fields_by_name['cycleAward'].message_type = _PBQUESTRANDCYCLEAWARD
_PBQUESTRANDGROUPCFG.fields_by_name['cycleNotice'].message_type = _PBQUESTRANDCYCLENOTICE
_PBQUESTRANDLIBRARY.fields_by_name['condition'].message_type = _PBQUESTRANDCONDITION
_PBQUESTRANDCONDITION.fields_by_name['type'].enum_type = _PBECONDITIONTYPE
DESCRIPTOR.message_types_by_name['PBQuestRandCfg'] = _PBQUESTRANDCFG
DESCRIPTOR.message_types_by_name['PBQuestRandGroupCfg'] = _PBQUESTRANDGROUPCFG
DESCRIPTOR.message_types_by_name['PBQuestRandLibrary'] = _PBQUESTRANDLIBRARY
DESCRIPTOR.message_types_by_name['PBQuestRandCondition'] = _PBQUESTRANDCONDITION
DESCRIPTOR.message_types_by_name['PBQuestRandCycleAward'] = _PBQUESTRANDCYCLEAWARD
DESCRIPTOR.message_types_by_name['PBQuestRandCycleNotice'] = _PBQUESTRANDCYCLENOTICE

class PBQuestRandCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBQUESTRANDCFG
  
  # @@protoc_insertion_point(class_scope:PBQuestRandCfg)

class PBQuestRandGroupCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBQUESTRANDGROUPCFG
  
  # @@protoc_insertion_point(class_scope:PBQuestRandGroupCfg)

class PBQuestRandLibrary(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBQUESTRANDLIBRARY
  
  # @@protoc_insertion_point(class_scope:PBQuestRandLibrary)

class PBQuestRandCondition(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBQUESTRANDCONDITION
  
  # @@protoc_insertion_point(class_scope:PBQuestRandCondition)

class PBQuestRandCycleAward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBQUESTRANDCYCLEAWARD
  
  # @@protoc_insertion_point(class_scope:PBQuestRandCycleAward)

class PBQuestRandCycleNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBQUESTRANDCYCLENOTICE
  
  # @@protoc_insertion_point(class_scope:PBQuestRandCycleNotice)

# @@protoc_insertion_point(module_scope)