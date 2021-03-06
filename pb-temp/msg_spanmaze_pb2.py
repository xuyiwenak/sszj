# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_spanmaze.proto',
  package='',
  serialized_pb='\n\x12msg_spanmaze.proto\"\x1a\n\x18PBMsgSpanMazeSignRequest\"-\n\x19PBMsgSpanMazeSignResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\"\x1b\n\x19PBMsgSpanMazeEnterRequest\".\n\x1aPBMsgSpanMazeEnterResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\"!\n\x1fPBMsgSpanMazeEnterDungeonNotice*O\n\x0f\x45SpanMazeStatus\x12\x0c\n\x08Undefine\x10\x00\x12\n\n\x06SignUp\x10\x01\x12\n\n\x06Round1\x10\x02\x12\n\n\x06Round2\x10\x03\x12\n\n\x06Round3\x10\x04')

_ESPANMAZESTATUS = descriptor.EnumDescriptor(
  name='ESpanMazeStatus',
  full_name='ESpanMazeStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='Undefine', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SignUp', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Round1', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Round2', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Round3', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=209,
  serialized_end=288,
)


Undefine = 0
SignUp = 1
Round1 = 2
Round2 = 3
Round3 = 4



_PBMSGSPANMAZESIGNREQUEST = descriptor.Descriptor(
  name='PBMsgSpanMazeSignRequest',
  full_name='PBMsgSpanMazeSignRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=22,
  serialized_end=48,
)


_PBMSGSPANMAZESIGNRESPONSE = descriptor.Descriptor(
  name='PBMsgSpanMazeSignResponse',
  full_name='PBMsgSpanMazeSignResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgSpanMazeSignResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
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
  serialized_start=50,
  serialized_end=95,
)


_PBMSGSPANMAZEENTERREQUEST = descriptor.Descriptor(
  name='PBMsgSpanMazeEnterRequest',
  full_name='PBMsgSpanMazeEnterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_end=124,
)


_PBMSGSPANMAZEENTERRESPONSE = descriptor.Descriptor(
  name='PBMsgSpanMazeEnterResponse',
  full_name='PBMsgSpanMazeEnterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgSpanMazeEnterResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
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
  serialized_start=126,
  serialized_end=172,
)


_PBMSGSPANMAZEENTERDUNGEONNOTICE = descriptor.Descriptor(
  name='PBMsgSpanMazeEnterDungeonNotice',
  full_name='PBMsgSpanMazeEnterDungeonNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=174,
  serialized_end=207,
)

DESCRIPTOR.message_types_by_name['PBMsgSpanMazeSignRequest'] = _PBMSGSPANMAZESIGNREQUEST
DESCRIPTOR.message_types_by_name['PBMsgSpanMazeSignResponse'] = _PBMSGSPANMAZESIGNRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgSpanMazeEnterRequest'] = _PBMSGSPANMAZEENTERREQUEST
DESCRIPTOR.message_types_by_name['PBMsgSpanMazeEnterResponse'] = _PBMSGSPANMAZEENTERRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgSpanMazeEnterDungeonNotice'] = _PBMSGSPANMAZEENTERDUNGEONNOTICE

class PBMsgSpanMazeSignRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGSPANMAZESIGNREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgSpanMazeSignRequest)

class PBMsgSpanMazeSignResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGSPANMAZESIGNRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgSpanMazeSignResponse)

class PBMsgSpanMazeEnterRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGSPANMAZEENTERREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgSpanMazeEnterRequest)

class PBMsgSpanMazeEnterResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGSPANMAZEENTERRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgSpanMazeEnterResponse)

class PBMsgSpanMazeEnterDungeonNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGSPANMAZEENTERDUNGEONNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgSpanMazeEnterDungeonNotice)

# @@protoc_insertion_point(module_scope)
