# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_spanwild.proto',
  package='',
  serialized_pb='\n\x13tmpl_spanwild.proto\x1a\x0ftmpl_base.proto\"|\n\rPBSpanWildCfg\x12\'\n\rspanwildscore\x18\x01 \x03(\x0b\x32\x10.PBSpanWildScore\x12)\n\x0espanwildreward\x18\x02 \x01(\x0b\x32\x11.PBSpanWildReward:\x17\xc2\xf3\x18\x13spanwild_config.xml\"\xa9\x01\n\x0fPBSpanWildScore\x12\r\n\x05index\x18\x01 \x01(\x11\x12\r\n\x05minlv\x18\x02 \x01(\x11\x12\r\n\x05maxlv\x18\x03 \x01(\x11\x12\x10\n\x08\x64mgscore\x18\x04 \x01(\x02\x12\x0f\n\x07sheetid\x18\x05 \x01(\t\x12\"\n\rgetscore_rate\x18\x06 \x03(\x0b\x32\x0b.PBGetScore\x12\r\n\x05\x61\x63tid\x18\x07 \x01(\t\x12\x13\n\x0bnotice_time\x18\x08 \x01(\x11\"*\n\nPBGetScore\x12\r\n\x05index\x18\x01 \x01(\x11\x12\r\n\x05ratio\x18\x02 \x01(\x02\".\n\x0cPBRewardItem\x12\x0f\n\x07sheetid\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"W\n\x14PBSpanWildRewardItem\x12\x0f\n\x07minRank\x18\x01 \x01(\x11\x12\x0f\n\x07maxRank\x18\x02 \x01(\x11\x12\x1d\n\x06reward\x18\x03 \x03(\x0b\x32\r.PBRewardItem\"=\n\x10PBSpanWildReward\x12)\n\nrewardlist\x18\x01 \x03(\x0b\x32\x15.PBSpanWildRewardItem')




_PBSPANWILDCFG = descriptor.Descriptor(
  name='PBSpanWildCfg',
  full_name='PBSpanWildCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='spanwildscore', full_name='PBSpanWildCfg.spanwildscore', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='spanwildreward', full_name='PBSpanWildCfg.spanwildreward', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  options=descriptor._ParseOptions(descriptor_pb2.MessageOptions(), '\302\363\030\023spanwild_config.xml'),
  is_extendable=False,
  extension_ranges=[],
  serialized_start=40,
  serialized_end=164,
)


_PBSPANWILDSCORE = descriptor.Descriptor(
  name='PBSpanWildScore',
  full_name='PBSpanWildScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='PBSpanWildScore.index', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='minlv', full_name='PBSpanWildScore.minlv', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxlv', full_name='PBSpanWildScore.maxlv', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dmgscore', full_name='PBSpanWildScore.dmgscore', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sheetid', full_name='PBSpanWildScore.sheetid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='getscore_rate', full_name='PBSpanWildScore.getscore_rate', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='actid', full_name='PBSpanWildScore.actid', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='notice_time', full_name='PBSpanWildScore.notice_time', index=7,
      number=8, type=17, cpp_type=1, label=1,
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
  serialized_start=167,
  serialized_end=336,
)


_PBGETSCORE = descriptor.Descriptor(
  name='PBGetScore',
  full_name='PBGetScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='PBGetScore.index', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ratio', full_name='PBGetScore.ratio', index=1,
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
  serialized_start=338,
  serialized_end=380,
)


_PBREWARDITEM = descriptor.Descriptor(
  name='PBRewardItem',
  full_name='PBRewardItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sheetid', full_name='PBRewardItem.sheetid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='PBRewardItem.count', index=1,
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
  serialized_start=382,
  serialized_end=428,
)


_PBSPANWILDREWARDITEM = descriptor.Descriptor(
  name='PBSpanWildRewardItem',
  full_name='PBSpanWildRewardItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='minRank', full_name='PBSpanWildRewardItem.minRank', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='maxRank', full_name='PBSpanWildRewardItem.maxRank', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='reward', full_name='PBSpanWildRewardItem.reward', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=430,
  serialized_end=517,
)


_PBSPANWILDREWARD = descriptor.Descriptor(
  name='PBSpanWildReward',
  full_name='PBSpanWildReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='rewardlist', full_name='PBSpanWildReward.rewardlist', index=0,
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
  serialized_start=519,
  serialized_end=580,
)

_PBSPANWILDCFG.fields_by_name['spanwildscore'].message_type = _PBSPANWILDSCORE
_PBSPANWILDCFG.fields_by_name['spanwildreward'].message_type = _PBSPANWILDREWARD
_PBSPANWILDSCORE.fields_by_name['getscore_rate'].message_type = _PBGETSCORE
_PBSPANWILDREWARDITEM.fields_by_name['reward'].message_type = _PBREWARDITEM
_PBSPANWILDREWARD.fields_by_name['rewardlist'].message_type = _PBSPANWILDREWARDITEM
DESCRIPTOR.message_types_by_name['PBSpanWildCfg'] = _PBSPANWILDCFG
DESCRIPTOR.message_types_by_name['PBSpanWildScore'] = _PBSPANWILDSCORE
DESCRIPTOR.message_types_by_name['PBGetScore'] = _PBGETSCORE
DESCRIPTOR.message_types_by_name['PBRewardItem'] = _PBREWARDITEM
DESCRIPTOR.message_types_by_name['PBSpanWildRewardItem'] = _PBSPANWILDREWARDITEM
DESCRIPTOR.message_types_by_name['PBSpanWildReward'] = _PBSPANWILDREWARD

class PBSpanWildCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSPANWILDCFG
  
  # @@protoc_insertion_point(class_scope:PBSpanWildCfg)

class PBSpanWildScore(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSPANWILDSCORE
  
  # @@protoc_insertion_point(class_scope:PBSpanWildScore)

class PBGetScore(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBGETSCORE
  
  # @@protoc_insertion_point(class_scope:PBGetScore)

class PBRewardItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBREWARDITEM
  
  # @@protoc_insertion_point(class_scope:PBRewardItem)

class PBSpanWildRewardItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSPANWILDREWARDITEM
  
  # @@protoc_insertion_point(class_scope:PBSpanWildRewardItem)

class PBSpanWildReward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSPANWILDREWARD
  
  # @@protoc_insertion_point(class_scope:PBSpanWildReward)

# @@protoc_insertion_point(module_scope)
