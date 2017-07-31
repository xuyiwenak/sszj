# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2
import msg_common_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_match.proto',
  package='',
  serialized_pb='\n\x10tmpl_match.proto\x1a\x0ftmpl_base.proto\x1a\x10msg_common.proto\"\x9d\x01\n\rPBConfigMatch\x12 \n\nmatch_rule\x18\x01 \x03(\x0b\x32\x0c.PBMatchRule\x12\x16\n\x0emax_signup_num\x18\x02 \x01(\x05\x12\'\n\x0b\x62\x61se_config\x18\x03 \x01(\x0b\x32\x12.PBMatchBaseConfig\x12)\n\x0c\x65nter_notice\x18\x04 \x03(\x0b\x32\x13.PBMatchNoticeEnter\"G\n\x11PBMatchBaseConfig\x12\x1b\n\x13max_confirming_secs\x18\x01 \x01(\x05\x12\x15\n\rcallfriend_cd\x18\x02 \x01(\x05\"\xd1\x03\n\x0bPBMatchRule\x12\x10\n\x08match_id\x18\x01 \x01(\x05\x12\x19\n\x11match_target_type\x18\x02 \x01(\r\x12\x17\n\x0fmatch_target_id\x18\x03 \x01(\r\x12 \n\nmatch_type\x18\x04 \x01(\x0e\x32\x0c.PBMatchType\x12#\n\tspan_type\x18\x05 \x01(\x0e\x32\x10.PBMatchSpanType\x12\x1f\n\tmust_cond\x18\x06 \x03(\x0b\x32\x0c.PBMatchCond\x12!\n\x0b\x62\x65tter_cond\x18\x07 \x03(\x0b\x32\x0c.PBMatchCond\x12\x17\n\x0f\x63\x61n_enter_doing\x18\x08 \x01(\x08\x12\x11\n\tkeep_time\x18\t \x01(\x05\x12\x16\n\x0emin_player_num\x18\n \x01(\x05\x12\x16\n\x0emax_player_num\x18\x0b \x01(\x05\x12\x14\n\x0cneed_confirm\x18\x0c \x01(\x08\x12\x17\n\x0f\x62\x65st_match_time\x18\r \x01(\x05\x12\"\n\x1a\x63\x61llfriend_need_build_team\x18\x0e \x01(\x08\x12\x1c\n\x14match_target_sheetid\x18\x0f \x01(\t\x12\x14\n\x0c\x64ungeon_type\x18\x10 \x01(\x05\x12\x0e\n\x06\x61\x63t_id\x18\x11 \x01(\r\"G\n\x0bPBMatchCond\x12\x11\n\tcond_type\x18\x01 \x01(\x05\x12\x12\n\nbest_scope\x18\x02 \x01(\x05\x12\x11\n\tmax_scope\x18\x03 \x01(\x05\")\n\x12PBMatchNoticeEnter\x12\x13\n\x0b\x61\x63t_sheetid\x18\x01 \x01(\t*\xda\x01\n\x0bPBMatchType\x12\x18\n\x14\x65nPBMatchType_Single\x10\x01\x12\x16\n\x12\x65nPBMatchType_Team\x10\x02\x12\x17\n\x13\x65nPBMatchType_Team2\x10\x03\x12\x16\n\x12\x65nPBMatchType_Room\x10\x04\x12\x16\n\x12\x65nPBMatchType_Cqpk\x10\x05\x12\x18\n\x14\x65nPBMatchType_Battle\x10\x06\x12\x19\n\x15\x65nPBMatchType_PveSpan\x10\x07\x12\x1b\n\x17\x65nPBMatchType_NoDungeon\x10\x08*J\n\x0fPBMatchSpanType\x12\x1b\n\x17\x65nPBMatchSpanType_Local\x10\x01\x12\x1a\n\x16\x65nPBMatchSpanType_Span\x10\x02*\x94\x01\n\x13PBMatchMustCondType\x12\x1b\n\x17\x65nPBMatchCondType_Level\x10\x01\x12!\n\x1d\x65nPBMatchCondType_BattleScore\x10\x02\x12!\n\x1d\x65nPBMatchCondType_PvPScoreSeg\x10\x03\x12\x1a\n\x16\x65nPBMatchCondType_Camp\x10\x04*\x90\x01\n\x15PBMatchBetterCondType\x12%\n!enPBMatchBetterCondType_MatchTime\x10\x01\x12*\n&enPBMatchBetterCondType_SameShardFirst\x10\x02\x12$\n enPBMatchBetterCondType_DiffRole\x10\x03')

_PBMATCHTYPE = descriptor.EnumDescriptor(
  name='PBMatchType',
  full_name='PBMatchType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='enPBMatchType_Single', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchType_Team', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchType_Team2', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchType_Room', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchType_Cqpk', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchType_Battle', index=5, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchType_PveSpan', index=6, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchType_NoDungeon', index=7, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=873,
  serialized_end=1091,
)


_PBMATCHSPANTYPE = descriptor.EnumDescriptor(
  name='PBMatchSpanType',
  full_name='PBMatchSpanType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='enPBMatchSpanType_Local', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchSpanType_Span', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1093,
  serialized_end=1167,
)


_PBMATCHMUSTCONDTYPE = descriptor.EnumDescriptor(
  name='PBMatchMustCondType',
  full_name='PBMatchMustCondType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='enPBMatchCondType_Level', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchCondType_BattleScore', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchCondType_PvPScoreSeg', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchCondType_Camp', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1170,
  serialized_end=1318,
)


_PBMATCHBETTERCONDTYPE = descriptor.EnumDescriptor(
  name='PBMatchBetterCondType',
  full_name='PBMatchBetterCondType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='enPBMatchBetterCondType_MatchTime', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchBetterCondType_SameShardFirst', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enPBMatchBetterCondType_DiffRole', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1321,
  serialized_end=1465,
)


enPBMatchType_Single = 1
enPBMatchType_Team = 2
enPBMatchType_Team2 = 3
enPBMatchType_Room = 4
enPBMatchType_Cqpk = 5
enPBMatchType_Battle = 6
enPBMatchType_PveSpan = 7
enPBMatchType_NoDungeon = 8
enPBMatchSpanType_Local = 1
enPBMatchSpanType_Span = 2
enPBMatchCondType_Level = 1
enPBMatchCondType_BattleScore = 2
enPBMatchCondType_PvPScoreSeg = 3
enPBMatchCondType_Camp = 4
enPBMatchBetterCondType_MatchTime = 1
enPBMatchBetterCondType_SameShardFirst = 2
enPBMatchBetterCondType_DiffRole = 3



_PBCONFIGMATCH = descriptor.Descriptor(
  name='PBConfigMatch',
  full_name='PBConfigMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='match_rule', full_name='PBConfigMatch.match_rule', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_signup_num', full_name='PBConfigMatch.max_signup_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='base_config', full_name='PBConfigMatch.base_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enter_notice', full_name='PBConfigMatch.enter_notice', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=56,
  serialized_end=213,
)


_PBMATCHBASECONFIG = descriptor.Descriptor(
  name='PBMatchBaseConfig',
  full_name='PBMatchBaseConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='max_confirming_secs', full_name='PBMatchBaseConfig.max_confirming_secs', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='callfriend_cd', full_name='PBMatchBaseConfig.callfriend_cd', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=215,
  serialized_end=286,
)


_PBMATCHRULE = descriptor.Descriptor(
  name='PBMatchRule',
  full_name='PBMatchRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='match_id', full_name='PBMatchRule.match_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='match_target_type', full_name='PBMatchRule.match_target_type', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='match_target_id', full_name='PBMatchRule.match_target_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='match_type', full_name='PBMatchRule.match_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='span_type', full_name='PBMatchRule.span_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='must_cond', full_name='PBMatchRule.must_cond', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='better_cond', full_name='PBMatchRule.better_cond', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='can_enter_doing', full_name='PBMatchRule.can_enter_doing', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='keep_time', full_name='PBMatchRule.keep_time', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='min_player_num', full_name='PBMatchRule.min_player_num', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_player_num', full_name='PBMatchRule.max_player_num', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='need_confirm', full_name='PBMatchRule.need_confirm', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='best_match_time', full_name='PBMatchRule.best_match_time', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='callfriend_need_build_team', full_name='PBMatchRule.callfriend_need_build_team', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='match_target_sheetid', full_name='PBMatchRule.match_target_sheetid', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dungeon_type', full_name='PBMatchRule.dungeon_type', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_id', full_name='PBMatchRule.act_id', index=16,
      number=17, type=13, cpp_type=3, label=1,
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
  serialized_start=289,
  serialized_end=754,
)


_PBMATCHCOND = descriptor.Descriptor(
  name='PBMatchCond',
  full_name='PBMatchCond',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cond_type', full_name='PBMatchCond.cond_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='best_scope', full_name='PBMatchCond.best_scope', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_scope', full_name='PBMatchCond.max_scope', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=756,
  serialized_end=827,
)


_PBMATCHNOTICEENTER = descriptor.Descriptor(
  name='PBMatchNoticeEnter',
  full_name='PBMatchNoticeEnter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='act_sheetid', full_name='PBMatchNoticeEnter.act_sheetid', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=829,
  serialized_end=870,
)

_PBCONFIGMATCH.fields_by_name['match_rule'].message_type = _PBMATCHRULE
_PBCONFIGMATCH.fields_by_name['base_config'].message_type = _PBMATCHBASECONFIG
_PBCONFIGMATCH.fields_by_name['enter_notice'].message_type = _PBMATCHNOTICEENTER
_PBMATCHRULE.fields_by_name['match_type'].enum_type = _PBMATCHTYPE
_PBMATCHRULE.fields_by_name['span_type'].enum_type = _PBMATCHSPANTYPE
_PBMATCHRULE.fields_by_name['must_cond'].message_type = _PBMATCHCOND
_PBMATCHRULE.fields_by_name['better_cond'].message_type = _PBMATCHCOND
DESCRIPTOR.message_types_by_name['PBConfigMatch'] = _PBCONFIGMATCH
DESCRIPTOR.message_types_by_name['PBMatchBaseConfig'] = _PBMATCHBASECONFIG
DESCRIPTOR.message_types_by_name['PBMatchRule'] = _PBMATCHRULE
DESCRIPTOR.message_types_by_name['PBMatchCond'] = _PBMATCHCOND
DESCRIPTOR.message_types_by_name['PBMatchNoticeEnter'] = _PBMATCHNOTICEENTER

class PBConfigMatch(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGMATCH
  
  # @@protoc_insertion_point(class_scope:PBConfigMatch)

class PBMatchBaseConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMATCHBASECONFIG
  
  # @@protoc_insertion_point(class_scope:PBMatchBaseConfig)

class PBMatchRule(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMATCHRULE
  
  # @@protoc_insertion_point(class_scope:PBMatchRule)

class PBMatchCond(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMATCHCOND
  
  # @@protoc_insertion_point(class_scope:PBMatchCond)

class PBMatchNoticeEnter(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMATCHNOTICEENTER
  
  # @@protoc_insertion_point(class_scope:PBMatchNoticeEnter)

# @@protoc_insertion_point(module_scope)