# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_imbattle.proto',
  package='',
  serialized_pb='\n\x13tmpl_imbattle.proto\x1a\x0ftmpl_base.proto\"`\n\x10PBIMBattleConfig\x12&\n\tbasic_var\x18\x01 \x01(\x0b\x32\x13.PBIMBattleBasicVar\x12$\n\x0b\x62\x61ttle_list\x18\x02 \x03(\x0b\x32\x0f.PBIMBattleList\"\xd7\x02\n\x12PBIMBattleBasicVar\x12\x19\n\x11imbattle_sign_end\x18\x01 \x01(\x02\x12\x1e\n\x16imbattle_sign_lock_end\x18\x02 \x01(\x02\x12\x18\n\x10imbattle_pvp_end\x18\x03 \x01(\x02\x12\x1b\n\x13imbattle_win_scends\x18\x04 \x01(\x11\x12\x16\n\x0eimbattle_token\x18\x05 \x01(\t\x12\x17\n\x0fmax_sign_battle\x18\x06 \x01(\x11\x12!\n\x19imbattle_kill_rank_reward\x18\x07 \x01(\t\x12!\n\x19imbattle_sign_level_limit\x18\x08 \x01(\x11\x12\x1b\n\x13imbattle_pvp_notice\x18\t \x01(\x11\x12\x1e\n\x16imbattle_rest_end_time\x18\n \x01(\x02\x12\x1b\n\x13imbattle_max_member\x18\x0b \x01(\x11\"3\n\x0ePBIMBattleList\x12\x10\n\x08week_day\x18\x01 \x01(\x11\x12\x0f\n\x07\x62\x61ttles\x18\x02 \x01(\t')




_PBIMBATTLECONFIG = descriptor.Descriptor(
  name='PBIMBattleConfig',
  full_name='PBIMBattleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='basic_var', full_name='PBIMBattleConfig.basic_var', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='battle_list', full_name='PBIMBattleConfig.battle_list', index=1,
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
  serialized_start=40,
  serialized_end=136,
)


_PBIMBATTLEBASICVAR = descriptor.Descriptor(
  name='PBIMBattleBasicVar',
  full_name='PBIMBattleBasicVar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='imbattle_sign_end', full_name='PBIMBattleBasicVar.imbattle_sign_end', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_sign_lock_end', full_name='PBIMBattleBasicVar.imbattle_sign_lock_end', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_pvp_end', full_name='PBIMBattleBasicVar.imbattle_pvp_end', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_win_scends', full_name='PBIMBattleBasicVar.imbattle_win_scends', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_token', full_name='PBIMBattleBasicVar.imbattle_token', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_sign_battle', full_name='PBIMBattleBasicVar.max_sign_battle', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_kill_rank_reward', full_name='PBIMBattleBasicVar.imbattle_kill_rank_reward', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_sign_level_limit', full_name='PBIMBattleBasicVar.imbattle_sign_level_limit', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_pvp_notice', full_name='PBIMBattleBasicVar.imbattle_pvp_notice', index=8,
      number=9, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_rest_end_time', full_name='PBIMBattleBasicVar.imbattle_rest_end_time', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='imbattle_max_member', full_name='PBIMBattleBasicVar.imbattle_max_member', index=10,
      number=11, type=17, cpp_type=1, label=1,
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
  serialized_start=139,
  serialized_end=482,
)


_PBIMBATTLELIST = descriptor.Descriptor(
  name='PBIMBattleList',
  full_name='PBIMBattleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='week_day', full_name='PBIMBattleList.week_day', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='battles', full_name='PBIMBattleList.battles', index=1,
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
  serialized_start=484,
  serialized_end=535,
)

_PBIMBATTLECONFIG.fields_by_name['basic_var'].message_type = _PBIMBATTLEBASICVAR
_PBIMBATTLECONFIG.fields_by_name['battle_list'].message_type = _PBIMBATTLELIST
DESCRIPTOR.message_types_by_name['PBIMBattleConfig'] = _PBIMBATTLECONFIG
DESCRIPTOR.message_types_by_name['PBIMBattleBasicVar'] = _PBIMBATTLEBASICVAR
DESCRIPTOR.message_types_by_name['PBIMBattleList'] = _PBIMBATTLELIST

class PBIMBattleConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBIMBATTLECONFIG
  
  # @@protoc_insertion_point(class_scope:PBIMBattleConfig)

class PBIMBattleBasicVar(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBIMBATTLEBASICVAR
  
  # @@protoc_insertion_point(class_scope:PBIMBattleBasicVar)

class PBIMBattleList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBIMBATTLELIST
  
  # @@protoc_insertion_point(class_scope:PBIMBattleList)

# @@protoc_insertion_point(module_scope)
