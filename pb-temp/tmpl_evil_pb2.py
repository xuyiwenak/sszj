# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_evil.proto',
  package='',
  serialized_pb='\n\x0ftmpl_evil.proto\x1a\x0ftmpl_base.proto\"\xf6\x02\n\tPBEvilCfg\x12\x13\n\x0buse_drop_hp\x18\x01 \x01(\x11\x12\x12\n\ngain_times\x18\x02 \x01(\x11\x12\x11\n\tuse_times\x18\x03 \x01(\x11\x12\x0f\n\x07kill_cd\x18\x04 \x01(\x11\x12\x13\n\x0b\x61pron_ratio\x18\x05 \x01(\x11\x12\x17\n\x0fman_apron_sheet\x18\x06 \x01(\t\x12\x19\n\x11women_apron_sheet\x18\x07 \x01(\t\x12\x12\n\nkill_times\x18\x08 \x01(\x11\x12\x13\n\x0bkill_ratio1\x18\t \x01(\x02\x12\x13\n\x0bkill_ratio2\x18\n \x01(\x02\x12\x11\n\tmax_ratio\x18\x0b \x01(\x02\x12#\n\x0c\x64rop_hp_list\x18\x0c \x03(\x0b\x32\r.PBEvilDropHp\x12\x14\n\x0c\x64urance_rate\x18\r \x01(\x11\x12\x17\n\x0f\x61\x63t_kill_ratio1\x18\x0e \x01(\x02\x12\x17\n\x0f\x61\x63t_kill_ratio2\x18\x0f \x01(\x02\x12\x15\n\ract_max_ratio\x18\x10 \x01(\x02\"G\n\x0cPBEvilDropHp\x12\x13\n\x0buse_drop_hp\x18\x01 \x01(\x11\x12\x10\n\x08min_rate\x18\x02 \x01(\x11\x12\x10\n\x08max_rate\x18\x03 \x01(\x11')




_PBEVILCFG = descriptor.Descriptor(
  name='PBEvilCfg',
  full_name='PBEvilCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='use_drop_hp', full_name='PBEvilCfg.use_drop_hp', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gain_times', full_name='PBEvilCfg.gain_times', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='use_times', full_name='PBEvilCfg.use_times', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kill_cd', full_name='PBEvilCfg.kill_cd', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='apron_ratio', full_name='PBEvilCfg.apron_ratio', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='man_apron_sheet', full_name='PBEvilCfg.man_apron_sheet', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='women_apron_sheet', full_name='PBEvilCfg.women_apron_sheet', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kill_times', full_name='PBEvilCfg.kill_times', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kill_ratio1', full_name='PBEvilCfg.kill_ratio1', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='kill_ratio2', full_name='PBEvilCfg.kill_ratio2', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_ratio', full_name='PBEvilCfg.max_ratio', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='drop_hp_list', full_name='PBEvilCfg.drop_hp_list', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='durance_rate', full_name='PBEvilCfg.durance_rate', index=12,
      number=13, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_kill_ratio1', full_name='PBEvilCfg.act_kill_ratio1', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_kill_ratio2', full_name='PBEvilCfg.act_kill_ratio2', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_max_ratio', full_name='PBEvilCfg.act_max_ratio', index=15,
      number=16, type=2, cpp_type=6, label=1,
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
  serialized_start=37,
  serialized_end=411,
)


_PBEVILDROPHP = descriptor.Descriptor(
  name='PBEvilDropHp',
  full_name='PBEvilDropHp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='use_drop_hp', full_name='PBEvilDropHp.use_drop_hp', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='min_rate', full_name='PBEvilDropHp.min_rate', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_rate', full_name='PBEvilDropHp.max_rate', index=2,
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
  serialized_start=413,
  serialized_end=484,
)

_PBEVILCFG.fields_by_name['drop_hp_list'].message_type = _PBEVILDROPHP
DESCRIPTOR.message_types_by_name['PBEvilCfg'] = _PBEVILCFG
DESCRIPTOR.message_types_by_name['PBEvilDropHp'] = _PBEVILDROPHP

class PBEvilCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBEVILCFG
  
  # @@protoc_insertion_point(class_scope:PBEvilCfg)

class PBEvilDropHp(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBEVILDROPHP
  
  # @@protoc_insertion_point(class_scope:PBEvilDropHp)

# @@protoc_insertion_point(module_scope)
