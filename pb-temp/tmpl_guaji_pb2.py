# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_guaji.proto',
  package='',
  serialized_pb='\n\x10tmpl_guaji.proto\x1a\x0ftmpl_base.proto\"P\n\rPBConfigGuaJi\x12)\n\x0byaopin_info\x18\x01 \x01(\x0b\x32\x14.PBConfigGuaJiYaoPin:\x14\xc2\xf3\x18\x10guaji_config.xml\":\n\x13PBConfigGuaJiYaoPin\x12#\n\x08\x62uy_list\x18\x01 \x03(\x0b\x32\x11.PBConfigGuaJiBuy\"L\n\x10PBConfigGuaJiBuy\x12\x12\n\ngoods_name\x18\x01 \x01(\t\x12\x11\n\tsel_index\x18\x02 \x01(\x11\x12\x11\n\tbuy_vitem\x18\x03 \x01(\x11')




_PBCONFIGGUAJI = descriptor.Descriptor(
  name='PBConfigGuaJi',
  full_name='PBConfigGuaJi',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='yaopin_info', full_name='PBConfigGuaJi.yaopin_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\302\363\030\020guaji_config.xml'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=37,
  serialized_end=117,
)


_PBCONFIGGUAJIYAOPIN = descriptor.Descriptor(
  name='PBConfigGuaJiYaoPin',
  full_name='PBConfigGuaJiYaoPin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='buy_list', full_name='PBConfigGuaJiYaoPin.buy_list', index=0,
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
  serialized_start=119,
  serialized_end=177,
)


_PBCONFIGGUAJIBUY = descriptor.Descriptor(
  name='PBConfigGuaJiBuy',
  full_name='PBConfigGuaJiBuy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='goods_name', full_name='PBConfigGuaJiBuy.goods_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sel_index', full_name='PBConfigGuaJiBuy.sel_index', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buy_vitem', full_name='PBConfigGuaJiBuy.buy_vitem', index=2,
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
  serialized_start=179,
  serialized_end=255,
)

_PBCONFIGGUAJI.fields_by_name['yaopin_info'].message_type = _PBCONFIGGUAJIYAOPIN
_PBCONFIGGUAJIYAOPIN.fields_by_name['buy_list'].message_type = _PBCONFIGGUAJIBUY
DESCRIPTOR.message_types_by_name['PBConfigGuaJi'] = _PBCONFIGGUAJI
DESCRIPTOR.message_types_by_name['PBConfigGuaJiYaoPin'] = _PBCONFIGGUAJIYAOPIN
DESCRIPTOR.message_types_by_name['PBConfigGuaJiBuy'] = _PBCONFIGGUAJIBUY

class PBConfigGuaJi(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGGUAJI
  
  # @@protoc_insertion_point(class_scope:PBConfigGuaJi)

class PBConfigGuaJiYaoPin(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGGUAJIYAOPIN
  
  # @@protoc_insertion_point(class_scope:PBConfigGuaJiYaoPin)

class PBConfigGuaJiBuy(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGGUAJIBUY
  
  # @@protoc_insertion_point(class_scope:PBConfigGuaJiBuy)

# @@protoc_insertion_point(module_scope)
