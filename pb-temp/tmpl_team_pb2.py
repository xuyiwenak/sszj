# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2
import msg_common_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_team.proto',
  package='',
  serialized_pb='\n\x0ftmpl_team.proto\x1a\x0ftmpl_base.proto\x1a\x10msg_common.proto\"M\n\x0ePBTeamBaseInfo\x12!\n\x19offline_keep_team_seconds\x18\x01 \x01(\x11\x12\x18\n\x10\x63\x61llfriend_alive\x18\x02 \x01(\x11\"d\n\x10PBTeamFollowInfo\x12\x19\n\x11order_keep_second\x18\x01 \x01(\x11\x12\x1b\n\x13\x66ollow_change_speed\x18\x02 \x01(\x11\x12\x18\n\x10\x66ollow_open_ctrl\x18\x03 \x01(\x11\"Z\n\x0cPBConfigTeam\x12\"\n\tbase_info\x18\x01 \x01(\x0b\x32\x0f.PBTeamBaseInfo\x12&\n\x0b\x66ollow_info\x18\x02 \x01(\x0b\x32\x11.PBTeamFollowInfo')




_PBTEAMBASEINFO = descriptor.Descriptor(
  name='PBTeamBaseInfo',
  full_name='PBTeamBaseInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='offline_keep_team_seconds', full_name='PBTeamBaseInfo.offline_keep_team_seconds', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='callfriend_alive', full_name='PBTeamBaseInfo.callfriend_alive', index=1,
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
  serialized_start=54,
  serialized_end=131,
)


_PBTEAMFOLLOWINFO = descriptor.Descriptor(
  name='PBTeamFollowInfo',
  full_name='PBTeamFollowInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='order_keep_second', full_name='PBTeamFollowInfo.order_keep_second', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='follow_change_speed', full_name='PBTeamFollowInfo.follow_change_speed', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='follow_open_ctrl', full_name='PBTeamFollowInfo.follow_open_ctrl', index=2,
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
  serialized_start=133,
  serialized_end=233,
)


_PBCONFIGTEAM = descriptor.Descriptor(
  name='PBConfigTeam',
  full_name='PBConfigTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='base_info', full_name='PBConfigTeam.base_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='follow_info', full_name='PBConfigTeam.follow_info', index=1,
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
  serialized_start=235,
  serialized_end=325,
)

_PBCONFIGTEAM.fields_by_name['base_info'].message_type = _PBTEAMBASEINFO
_PBCONFIGTEAM.fields_by_name['follow_info'].message_type = _PBTEAMFOLLOWINFO
DESCRIPTOR.message_types_by_name['PBTeamBaseInfo'] = _PBTEAMBASEINFO
DESCRIPTOR.message_types_by_name['PBTeamFollowInfo'] = _PBTEAMFOLLOWINFO
DESCRIPTOR.message_types_by_name['PBConfigTeam'] = _PBCONFIGTEAM

class PBTeamBaseInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTEAMBASEINFO
  
  # @@protoc_insertion_point(class_scope:PBTeamBaseInfo)

class PBTeamFollowInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTEAMFOLLOWINFO
  
  # @@protoc_insertion_point(class_scope:PBTeamFollowInfo)

class PBConfigTeam(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGTEAM
  
  # @@protoc_insertion_point(class_scope:PBConfigTeam)

# @@protoc_insertion_point(module_scope)
