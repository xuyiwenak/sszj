# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_id_define_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_base.proto',
  package='',
  serialized_pb='\n\x0emsg_base.proto\x1a\x13msg_id_define.proto\"C\n\x0bPBMsgReward\x12\x17\n\x0freward_sheed_id\x18\x01 \x01(\r\x12\x0b\n\x03num\x18\x02 \x01(\x11\x12\x0e\n\x06\x62inded\x18\x03 \x01(\x08\"X\n\x07PBParam\x12\x12\n\nparam_type\x18\x01 \x01(\r\x12\x11\n\tparam_str\x18\x02 \x01(\t\x12&\n\x0bparam_color\x18\x03 \x01(\x0e\x32\x11.PBParamColorType\"\"\n\nPBAIVector\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02*7\n\x10PBParamColorType\x12\x10\n\x0c\x65nColor_None\x10\x00\x12\x11\n\renColor_Class\x10\x01\x42\x02H\x01')

_PBPARAMCOLORTYPE = descriptor.EnumDescriptor(
  name='PBParamColorType',
  full_name='PBParamColorType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='enColor_None', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enColor_Class', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=234,
  serialized_end=289,
)


enColor_None = 0
enColor_Class = 1



_PBMSGREWARD = descriptor.Descriptor(
  name='PBMsgReward',
  full_name='PBMsgReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='reward_sheed_id', full_name='PBMsgReward.reward_sheed_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='num', full_name='PBMsgReward.num', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='binded', full_name='PBMsgReward.binded', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=39,
  serialized_end=106,
)


_PBPARAM = descriptor.Descriptor(
  name='PBParam',
  full_name='PBParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='param_type', full_name='PBParam.param_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='param_str', full_name='PBParam.param_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='param_color', full_name='PBParam.param_color', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=108,
  serialized_end=196,
)


_PBAIVECTOR = descriptor.Descriptor(
  name='PBAIVector',
  full_name='PBAIVector',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='x', full_name='PBAIVector.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='PBAIVector.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=198,
  serialized_end=232,
)

_PBPARAM.fields_by_name['param_color'].enum_type = _PBPARAMCOLORTYPE
DESCRIPTOR.message_types_by_name['PBMsgReward'] = _PBMSGREWARD
DESCRIPTOR.message_types_by_name['PBParam'] = _PBPARAM
DESCRIPTOR.message_types_by_name['PBAIVector'] = _PBAIVECTOR

class PBMsgReward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGREWARD
  
  # @@protoc_insertion_point(class_scope:PBMsgReward)

class PBParam(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBPARAM
  
  # @@protoc_insertion_point(class_scope:PBParam)

class PBAIVector(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBAIVECTOR
  
  # @@protoc_insertion_point(class_scope:PBAIVector)

# @@protoc_insertion_point(module_scope)