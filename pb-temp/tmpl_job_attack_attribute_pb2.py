# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_job_attack_attribute.proto',
  package='',
  serialized_pb='\n\x1ftmpl_job_attack_attribute.proto\x1a\x0ftmpl_base.proto\"+\n\x0bPBJobAttack\x12\x0e\n\x06\x61ttack\x18\x01 \x01(\r\x12\x0c\n\x04role\x18\x02 \x03(\r\".\n\x0ePBJobAttackCfg\x12\x1c\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\x0c.PBJobAttack')




_PBJOBATTACK = descriptor.Descriptor(
  name='PBJobAttack',
  full_name='PBJobAttack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attack', full_name='PBJobAttack.attack', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role', full_name='PBJobAttack.role', index=1,
      number=2, type=13, cpp_type=3, label=3,
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
  serialized_start=52,
  serialized_end=95,
)


_PBJOBATTACKCFG = descriptor.Descriptor(
  name='PBJobAttackCfg',
  full_name='PBJobAttackCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='config', full_name='PBJobAttackCfg.config', index=0,
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
  serialized_start=97,
  serialized_end=143,
)

_PBJOBATTACKCFG.fields_by_name['config'].message_type = _PBJOBATTACK
DESCRIPTOR.message_types_by_name['PBJobAttack'] = _PBJOBATTACK
DESCRIPTOR.message_types_by_name['PBJobAttackCfg'] = _PBJOBATTACKCFG

class PBJobAttack(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBJOBATTACK
  
  # @@protoc_insertion_point(class_scope:PBJobAttack)

class PBJobAttackCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBJOBATTACKCFG
  
  # @@protoc_insertion_point(class_scope:PBJobAttackCfg)

# @@protoc_insertion_point(module_scope)
