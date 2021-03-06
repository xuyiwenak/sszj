# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_resource_punishment.proto',
  package='',
  serialized_pb='\n\x1etmpl_resource_punishment.proto\x1a\x0ftmpl_base.proto\"j\n\x17PBResourcePunishmentCfg\x12\x32\n\x13resource_punishment\x18\x01 \x03(\x0b\x32\x15.PBResourcePunishment:\x1b\xc2\xf3\x18\x17resource_punishment.xml\"\xa0\x01\n\x14PBResourcePunishment\x12\x15\n\rresource_type\x18\x01 \x01(\x11\x12\x19\n\x11gain_resource_per\x18\x02 \x01(\x11\x12\x1d\n\x15punishment_start_time\x18\x03 \x01(\t\x12\x1b\n\x13punishment_end_time\x18\x04 \x01(\t\x12\x1a\n\x12punishment_role_id\x18\x05 \x03(\r')




_PBRESOURCEPUNISHMENTCFG = descriptor.Descriptor(
  name='PBResourcePunishmentCfg',
  full_name='PBResourcePunishmentCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='resource_punishment', full_name='PBResourcePunishmentCfg.resource_punishment', index=0,
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
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\302\363\030\027resource_punishment.xml'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=51,
  serialized_end=157,
)


_PBRESOURCEPUNISHMENT = descriptor.Descriptor(
  name='PBResourcePunishment',
  full_name='PBResourcePunishment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='resource_type', full_name='PBResourcePunishment.resource_type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gain_resource_per', full_name='PBResourcePunishment.gain_resource_per', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='punishment_start_time', full_name='PBResourcePunishment.punishment_start_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='punishment_end_time', full_name='PBResourcePunishment.punishment_end_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='punishment_role_id', full_name='PBResourcePunishment.punishment_role_id', index=4,
      number=5, type=13, cpp_type=3, label=3,
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
  serialized_start=160,
  serialized_end=320,
)

_PBRESOURCEPUNISHMENTCFG.fields_by_name['resource_punishment'].message_type = _PBRESOURCEPUNISHMENT
DESCRIPTOR.message_types_by_name['PBResourcePunishmentCfg'] = _PBRESOURCEPUNISHMENTCFG
DESCRIPTOR.message_types_by_name['PBResourcePunishment'] = _PBRESOURCEPUNISHMENT

class PBResourcePunishmentCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRESOURCEPUNISHMENTCFG
  
  # @@protoc_insertion_point(class_scope:PBResourcePunishmentCfg)

class PBResourcePunishment(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRESOURCEPUNISHMENT
  
  # @@protoc_insertion_point(class_scope:PBResourcePunishment)

# @@protoc_insertion_point(module_scope)
