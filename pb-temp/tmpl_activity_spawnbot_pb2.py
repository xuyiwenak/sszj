# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_activity_spawnbot.proto',
  package='',
  serialized_pb='\n\x1ctmpl_activity_spawnbot.proto\x1a\x0ftmpl_base.proto\"k\n\x18PBActivitySpawnBotConfig\x12\x34\n\titem_list\x18\x01 \x03(\x0b\x32!.PBActivitySpawnBotItemListConfig:\x19\xc2\xf3\x18\x15\x61\x63tivity_spawnbot.xml\"L\n\x16PBActivitySpawnBotFunc\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tint_param\x18\x02 \x03(\x05\x12\x11\n\tstr_param\x18\x03 \x03(\t\"x\n\x1cPBActivitySpawnBotItemConfig\x12\x12\n\ngroup_name\x18\x01 \x01(\t\x12\x0e\n\x06map_id\x18\x02 \x01(\x05\x12#\n\x08pos_list\x18\x03 \x03(\x0b\x32\x11.PBTemplateVector\x12\x0f\n\x07line_id\x18\x04 \x01(\x05\"\xa0\x01\n PBActivitySpawnBotItemListConfig\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\x05\x12%\n\x04\x66unc\x18\x02 \x03(\x0b\x32\x17.PBActivitySpawnBotFunc\x12+\n\x04item\x18\x03 \x03(\x0b\x32\x1d.PBActivitySpawnBotItemConfig\x12\x13\n\x0bsys_despawn\x18\x04 \x01(\x05')




_PBACTIVITYSPAWNBOTCONFIG = descriptor.Descriptor(
  name='PBActivitySpawnBotConfig',
  full_name='PBActivitySpawnBotConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='item_list', full_name='PBActivitySpawnBotConfig.item_list', index=0,
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
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\302\363\030\025activity_spawnbot.xml'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=49,
  serialized_end=156,
)


_PBACTIVITYSPAWNBOTFUNC = descriptor.Descriptor(
  name='PBActivitySpawnBotFunc',
  full_name='PBActivitySpawnBotFunc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='PBActivitySpawnBotFunc.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='int_param', full_name='PBActivitySpawnBotFunc.int_param', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='str_param', full_name='PBActivitySpawnBotFunc.str_param', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=158,
  serialized_end=234,
)


_PBACTIVITYSPAWNBOTITEMCONFIG = descriptor.Descriptor(
  name='PBActivitySpawnBotItemConfig',
  full_name='PBActivitySpawnBotItemConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='group_name', full_name='PBActivitySpawnBotItemConfig.group_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='map_id', full_name='PBActivitySpawnBotItemConfig.map_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pos_list', full_name='PBActivitySpawnBotItemConfig.pos_list', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='line_id', full_name='PBActivitySpawnBotItemConfig.line_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=236,
  serialized_end=356,
)


_PBACTIVITYSPAWNBOTITEMLISTCONFIG = descriptor.Descriptor(
  name='PBActivitySpawnBotItemListConfig',
  full_name='PBActivitySpawnBotItemListConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='activity_id', full_name='PBActivitySpawnBotItemListConfig.activity_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='func', full_name='PBActivitySpawnBotItemListConfig.func', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='PBActivitySpawnBotItemListConfig.item', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sys_despawn', full_name='PBActivitySpawnBotItemListConfig.sys_despawn', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=359,
  serialized_end=519,
)

_PBACTIVITYSPAWNBOTCONFIG.fields_by_name['item_list'].message_type = _PBACTIVITYSPAWNBOTITEMLISTCONFIG
_PBACTIVITYSPAWNBOTITEMCONFIG.fields_by_name['pos_list'].message_type = tmpl_base_pb2._PBTEMPLATEVECTOR
_PBACTIVITYSPAWNBOTITEMLISTCONFIG.fields_by_name['func'].message_type = _PBACTIVITYSPAWNBOTFUNC
_PBACTIVITYSPAWNBOTITEMLISTCONFIG.fields_by_name['item'].message_type = _PBACTIVITYSPAWNBOTITEMCONFIG
DESCRIPTOR.message_types_by_name['PBActivitySpawnBotConfig'] = _PBACTIVITYSPAWNBOTCONFIG
DESCRIPTOR.message_types_by_name['PBActivitySpawnBotFunc'] = _PBACTIVITYSPAWNBOTFUNC
DESCRIPTOR.message_types_by_name['PBActivitySpawnBotItemConfig'] = _PBACTIVITYSPAWNBOTITEMCONFIG
DESCRIPTOR.message_types_by_name['PBActivitySpawnBotItemListConfig'] = _PBACTIVITYSPAWNBOTITEMLISTCONFIG

class PBActivitySpawnBotConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBACTIVITYSPAWNBOTCONFIG
  
  # @@protoc_insertion_point(class_scope:PBActivitySpawnBotConfig)

class PBActivitySpawnBotFunc(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBACTIVITYSPAWNBOTFUNC
  
  # @@protoc_insertion_point(class_scope:PBActivitySpawnBotFunc)

class PBActivitySpawnBotItemConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBACTIVITYSPAWNBOTITEMCONFIG
  
  # @@protoc_insertion_point(class_scope:PBActivitySpawnBotItemConfig)

class PBActivitySpawnBotItemListConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBACTIVITYSPAWNBOTITEMLISTCONFIG
  
  # @@protoc_insertion_point(class_scope:PBActivitySpawnBotItemListConfig)

# @@protoc_insertion_point(module_scope)