# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_base_pb2
import msg_item_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_uiopen.proto',
  package='',
  serialized_pb='\n\x10msg_uiopen.proto\x1a\x0emsg_base.proto\x1a\x0emsg_item.proto\"M\n\x15PBMsgUIOpenInfoNotice\x12\x10\n\x08ui_state\x18\x01 \x03(\x12\x12\x10\n\x08ui_story\x18\x02 \x03(\r\x12\x10\n\x08ui_guide\x18\x03 \x03(\r\"9\n\x12PBMsgUIStoryReport\x12\x10\n\x08ui_story\x18\x01 \x01(\r\x12\x11\n\tsave_flag\x18\x02 \x01(\r\"&\n\x12PBMsgUIGuideReport\x12\x10\n\x08ui_guide\x18\x01 \x01(\r\".\n\x16PBMsgUIPushLevelReport\x12\x14\n\x0cui_pushlevel\x18\x01 \x01(\r\".\n\x16PBMsgUIPushLevelNotice\x12\x14\n\x0cui_pushlevel\x18\x01 \x03(\r\"7\n\x11PBMsgUIHideNotice\x12\x11\n\tfunc_type\x18\x01 \x01(\x11\x12\x0f\n\x07is_hide\x18\x02 \x01(\x08\x42\x02H\x01')




_PBMSGUIOPENINFONOTICE = descriptor.Descriptor(
  name='PBMsgUIOpenInfoNotice',
  full_name='PBMsgUIOpenInfoNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ui_state', full_name='PBMsgUIOpenInfoNotice.ui_state', index=0,
      number=1, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ui_story', full_name='PBMsgUIOpenInfoNotice.ui_story', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ui_guide', full_name='PBMsgUIOpenInfoNotice.ui_guide', index=2,
      number=3, type=13, cpp_type=3, label=3,
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
  serialized_end=129,
)


_PBMSGUISTORYREPORT = descriptor.Descriptor(
  name='PBMsgUIStoryReport',
  full_name='PBMsgUIStoryReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ui_story', full_name='PBMsgUIStoryReport.ui_story', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='save_flag', full_name='PBMsgUIStoryReport.save_flag', index=1,
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
  serialized_start=131,
  serialized_end=188,
)


_PBMSGUIGUIDEREPORT = descriptor.Descriptor(
  name='PBMsgUIGuideReport',
  full_name='PBMsgUIGuideReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ui_guide', full_name='PBMsgUIGuideReport.ui_guide', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=190,
  serialized_end=228,
)


_PBMSGUIPUSHLEVELREPORT = descriptor.Descriptor(
  name='PBMsgUIPushLevelReport',
  full_name='PBMsgUIPushLevelReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ui_pushlevel', full_name='PBMsgUIPushLevelReport.ui_pushlevel', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=230,
  serialized_end=276,
)


_PBMSGUIPUSHLEVELNOTICE = descriptor.Descriptor(
  name='PBMsgUIPushLevelNotice',
  full_name='PBMsgUIPushLevelNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ui_pushlevel', full_name='PBMsgUIPushLevelNotice.ui_pushlevel', index=0,
      number=1, type=13, cpp_type=3, label=3,
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
  serialized_start=278,
  serialized_end=324,
)


_PBMSGUIHIDENOTICE = descriptor.Descriptor(
  name='PBMsgUIHideNotice',
  full_name='PBMsgUIHideNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='func_type', full_name='PBMsgUIHideNotice.func_type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_hide', full_name='PBMsgUIHideNotice.is_hide', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=326,
  serialized_end=381,
)

DESCRIPTOR.message_types_by_name['PBMsgUIOpenInfoNotice'] = _PBMSGUIOPENINFONOTICE
DESCRIPTOR.message_types_by_name['PBMsgUIStoryReport'] = _PBMSGUISTORYREPORT
DESCRIPTOR.message_types_by_name['PBMsgUIGuideReport'] = _PBMSGUIGUIDEREPORT
DESCRIPTOR.message_types_by_name['PBMsgUIPushLevelReport'] = _PBMSGUIPUSHLEVELREPORT
DESCRIPTOR.message_types_by_name['PBMsgUIPushLevelNotice'] = _PBMSGUIPUSHLEVELNOTICE
DESCRIPTOR.message_types_by_name['PBMsgUIHideNotice'] = _PBMSGUIHIDENOTICE

class PBMsgUIOpenInfoNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGUIOPENINFONOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgUIOpenInfoNotice)

class PBMsgUIStoryReport(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGUISTORYREPORT
  
  # @@protoc_insertion_point(class_scope:PBMsgUIStoryReport)

class PBMsgUIGuideReport(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGUIGUIDEREPORT
  
  # @@protoc_insertion_point(class_scope:PBMsgUIGuideReport)

class PBMsgUIPushLevelReport(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGUIPUSHLEVELREPORT
  
  # @@protoc_insertion_point(class_scope:PBMsgUIPushLevelReport)

class PBMsgUIPushLevelNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGUIPUSHLEVELNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgUIPushLevelNotice)

class PBMsgUIHideNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGUIHIDENOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgUIHideNotice)

# @@protoc_insertion_point(module_scope)