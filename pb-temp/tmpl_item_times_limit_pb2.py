# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_item_times_limit.proto',
  package='',
  serialized_pb='\n\x1btmpl_item_times_limit.proto\x1a\x0ftmpl_base.proto\"^\n\x13PBItemTimesLimitCfg\x12)\n\titem_list\x18\x01 \x03(\x0b\x32\x16.PBItemTimesLimitValue:\x1c\xc2\xf3\x18\x18item_times_limit_cfg.xml\"8\n\x15PBItemTimesLimitValue\x12\x10\n\x08sheet_id\x18\x01 \x01(\t\x12\r\n\x05times\x18\x02 \x01(\r')




_PBITEMTIMESLIMITCFG = descriptor.Descriptor(
  name='PBItemTimesLimitCfg',
  full_name='PBItemTimesLimitCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='item_list', full_name='PBItemTimesLimitCfg.item_list', index=0,
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
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\302\363\030\030item_times_limit_cfg.xml'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=48,
  serialized_end=142,
)


_PBITEMTIMESLIMITVALUE = descriptor.Descriptor(
  name='PBItemTimesLimitValue',
  full_name='PBItemTimesLimitValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sheet_id', full_name='PBItemTimesLimitValue.sheet_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='times', full_name='PBItemTimesLimitValue.times', index=1,
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
  extension_ranges=[],
  serialized_start=144,
  serialized_end=200,
)

_PBITEMTIMESLIMITCFG.fields_by_name['item_list'].message_type = _PBITEMTIMESLIMITVALUE
DESCRIPTOR.message_types_by_name['PBItemTimesLimitCfg'] = _PBITEMTIMESLIMITCFG
DESCRIPTOR.message_types_by_name['PBItemTimesLimitValue'] = _PBITEMTIMESLIMITVALUE

class PBItemTimesLimitCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBITEMTIMESLIMITCFG
  
  # @@protoc_insertion_point(class_scope:PBItemTimesLimitCfg)

class PBItemTimesLimitValue(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBITEMTIMESLIMITVALUE
  
  # @@protoc_insertion_point(class_scope:PBItemTimesLimitValue)

# @@protoc_insertion_point(module_scope)
