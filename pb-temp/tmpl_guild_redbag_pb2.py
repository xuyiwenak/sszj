# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_guild_redbag.proto',
  package='',
  serialized_pb='\n\x17tmpl_guild_redbag.proto\x1a\x0ftmpl_base.proto\"6\n\rPBRedBagCount\x12\x12\n\ncount_type\x18\x01 \x01(\x11\x12\x11\n\tcount_val\x18\x02 \x01(\x11\"\xd8\x01\n\x0ePBConfigRedBag\x12\x12\n\nused_level\x18\x01 \x01(\x11\x12\x0e\n\x06max_yb\x18\x02 \x01(\x11\x12\x0e\n\x06min_yb\x18\x03 \x01(\x11\x12\x11\n\tmax_allot\x18\x04 \x01(\x11\x12\x11\n\tmin_allot\x18\x05 \x01(\x11\x12\x12\n\nexist_time\x18\x06 \x01(\x11\x12\"\n\nsend_count\x18\x07 \x01(\x0b\x32\x0e.PBRedBagCount\x12\"\n\ndraw_count\x18\x08 \x01(\x0b\x32\x0e.PBRedBagCount\x12\x10\n\x08red_type\x18\t \x01(\t')




_PBREDBAGCOUNT = descriptor.Descriptor(
  name='PBRedBagCount',
  full_name='PBRedBagCount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='count_type', full_name='PBRedBagCount.count_type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count_val', full_name='PBRedBagCount.count_val', index=1,
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
  serialized_start=44,
  serialized_end=98,
)


_PBCONFIGREDBAG = descriptor.Descriptor(
  name='PBConfigRedBag',
  full_name='PBConfigRedBag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='used_level', full_name='PBConfigRedBag.used_level', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_yb', full_name='PBConfigRedBag.max_yb', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='min_yb', full_name='PBConfigRedBag.min_yb', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_allot', full_name='PBConfigRedBag.max_allot', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='min_allot', full_name='PBConfigRedBag.min_allot', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exist_time', full_name='PBConfigRedBag.exist_time', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='send_count', full_name='PBConfigRedBag.send_count', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='draw_count', full_name='PBConfigRedBag.draw_count', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='red_type', full_name='PBConfigRedBag.red_type', index=8,
      number=9, type=9, cpp_type=9, label=1,
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
  serialized_start=101,
  serialized_end=317,
)

_PBCONFIGREDBAG.fields_by_name['send_count'].message_type = _PBREDBAGCOUNT
_PBCONFIGREDBAG.fields_by_name['draw_count'].message_type = _PBREDBAGCOUNT
DESCRIPTOR.message_types_by_name['PBRedBagCount'] = _PBREDBAGCOUNT
DESCRIPTOR.message_types_by_name['PBConfigRedBag'] = _PBCONFIGREDBAG

class PBRedBagCount(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBREDBAGCOUNT
  
  # @@protoc_insertion_point(class_scope:PBRedBagCount)

class PBConfigRedBag(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGREDBAG
  
  # @@protoc_insertion_point(class_scope:PBConfigRedBag)

# @@protoc_insertion_point(module_scope)