# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_item_exchange.proto',
  package='',
  serialized_pb='\n\x18tmpl_item_exchange.proto\x1a\x0ftmpl_base.proto\"E\n\x11PBItemExchangeCfg\x12\x30\n\x12\x65xchange_item_list\x18\x01 \x03(\x0b\x32\x14.PBItemExchangeVaule\"V\n\x13PBItemExchangeVaule\x12\x15\n\rexchange_type\x18\x01 \x01(\x11\x12\x16\n\x0e\x65xchange_vaule\x18\x02 \x01(\x11\x12\x10\n\x08sheet_id\x18\x03 \x01(\t')




_PBITEMEXCHANGECFG = descriptor.Descriptor(
  name='PBItemExchangeCfg',
  full_name='PBItemExchangeCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='exchange_item_list', full_name='PBItemExchangeCfg.exchange_item_list', index=0,
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
  serialized_start=45,
  serialized_end=114,
)


_PBITEMEXCHANGEVAULE = descriptor.Descriptor(
  name='PBItemExchangeVaule',
  full_name='PBItemExchangeVaule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='exchange_type', full_name='PBItemExchangeVaule.exchange_type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exchange_vaule', full_name='PBItemExchangeVaule.exchange_vaule', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sheet_id', full_name='PBItemExchangeVaule.sheet_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=116,
  serialized_end=202,
)

_PBITEMEXCHANGECFG.fields_by_name['exchange_item_list'].message_type = _PBITEMEXCHANGEVAULE
DESCRIPTOR.message_types_by_name['PBItemExchangeCfg'] = _PBITEMEXCHANGECFG
DESCRIPTOR.message_types_by_name['PBItemExchangeVaule'] = _PBITEMEXCHANGEVAULE

class PBItemExchangeCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBITEMEXCHANGECFG
  
  # @@protoc_insertion_point(class_scope:PBItemExchangeCfg)

class PBItemExchangeVaule(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBITEMEXCHANGEVAULE
  
  # @@protoc_insertion_point(class_scope:PBItemExchangeVaule)

# @@protoc_insertion_point(module_scope)
