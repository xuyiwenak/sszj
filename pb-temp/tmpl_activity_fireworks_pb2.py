# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_activity_fireworks.proto',
  package='',
  serialized_pb='\n\x1dtmpl_activity_fireworks.proto\x1a\x0ftmpl_base.proto\"I\n\x19PBConfigActivityFireworks\x12,\n\x10\x66ireworks_config\x18\x01 \x03(\x0b\x32\x12.PBConfigFireworks\"\xd0\x02\n\x11PBConfigFireworks\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_date\x18\x03 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\t\x12.\n\rscore_collect\x18\x05 \x01(\x0b\x32\x17.PBConfigFireworksScore\x12-\n\nscore_open\x18\x06 \x01(\x0b\x32\x19.PBConfigFireworksDisplay\x12\x0e\n\x06\x61\x63t_id\x18\x07 \x01(\r\x12\x16\n\x0enpc_group_name\x18\x08 \x01(\t\x12\x10\n\x08\x62tn_name\x18\t \x01(\t\x12\x11\n\tbtn_event\x18\n \x01(\t\x12-\n\ract_desc_info\x18\x0c \x01(\x0b\x32\x16.PBConfigFireworksDesc\x12\x14\n\x0c\x61\x63t_tip_type\x18\r \x01(\r\"\xa0\x01\n\x15PBConfigFireworksDesc\x12\x10\n\x08\x61\x63t_desc\x18\x01 \x01(\t\x12\x15\n\ract_help_desc\x18\x02 \x01(\t\x12\x16\n\x0e\x61\x63t_award_desc\x18\x03 \x01(\t\x12\x16\n\x0e\x61\x63t_score_desc\x18\x04 \x01(\t\x12\x16\n\x0e\x61\x63t_title_icon\x18\x05 \x01(\t\x12\x16\n\x0e\x61\x63t_black_icon\x18\x06 \x01(\t\"\xac\x01\n\x16PBConfigFireworksScore\x12\x18\n\x10score_start_time\x18\x01 \x01(\t\x12\x16\n\x0escore_end_time\x18\x02 \x01(\t\x12+\n\nquest_info\x18\x03 \x03(\x0b\x32\x17.PBConfigFireworksQuest\x12\x1a\n\x12player_score_limit\x18\x04 \x01(\x11\x12\x17\n\x0f\x61\x63t_score_total\x18\x05 \x01(\r\"=\n\x16PBConfigFireworksQuest\x12\x10\n\x08quest_id\x18\x01 \x01(\x11\x12\x11\n\tadd_score\x18\x02 \x01(\x11\"\xed\x05\n\x18PBConfigFireworksDisplay\x12\x1a\n\x12\x64isplay_start_time\x18\x01 \x01(\t\x12\x18\n\x10\x64isplay_end_time\x18\x02 \x01(\t\x12\x16\n\x0e\x64isplay_map_id\x18\x03 \x03(\x11\x12\x1b\n\x13\x61\x64\x64_exp_tick_second\x18\x04 \x01(\x11\x12\x15\n\radd_exp_limit\x18\x05 \x01(\x11\x12\x31\n\x0cscore_player\x18\x06 \x03(\x0b\x32\x1b.PBConfigFireworksSocreChar\x12\x33\n\x0cscore_server\x18\x07 \x03(\x0b\x32\x1d.PBConfigFireworksSocreServer\x12\x19\n\x11is_show_fireworks\x18\x08 \x01(\x11\x12\x36\n\x11server_award_list\x18\t \x01(\x0b\x32\x1b.PBTemplateItemQuantityList\x12\x11\n\texp_table\x18\n \x01(\t\x12\x1f\n\x17server_award_mail_title\x18\x0b \x01(\t\x12\x1e\n\x16server_award_mail_body\x18\x0c \x01(\t\x12\x17\n\x0fis_server_award\x18\r \x01(\x11\x12\x19\n\x11show_fireworks_fx\x18\x0e \x01(\t\x12\x1d\n\x15\x64isplay_server_notice\x18\x0f \x01(\t\x12\"\n\x1a\x64isplay_server_notice_tick\x18\x10 \x01(\r\x12\x1e\n\x16\x64isplay_preview_notice\x18\x11 \x01(\t\x12%\n\x1d\x64isplay_preview_notice_second\x18\x12 \x03(\r\x12\x0e\n\x06map_fx\x18\x13 \x01(\t\x12\x17\n\x0fmap_fx_distance\x18\x14 \x01(\x11\x12\'\n\nmap_fx_pos\x18\x15 \x03(\x0b\x32\x13.PBTemplateVector2d\x12\x1a\n\x12\x61\x64\x64_fx_tick_second\x18\x16 \x01(\x11\x12\x14\n\x0c\x61\x64\x64_fx_limit\x18\x17 \x01(\x11\"]\n\x1aPBConfigFireworksSocreChar\x12\x11\n\tscore_min\x18\x01 \x01(\x11\x12\x11\n\tscore_max\x18\x02 \x01(\x11\x12\x19\n\x11\x61\x64\x64_score_precent\x18\x03 \x01(\x11\"o\n\x1cPBConfigFireworksSocreServer\x12\x19\n\x11score_min_precent\x18\x01 \x01(\x11\x12\x19\n\x11score_max_precent\x18\x02 \x01(\x11\x12\x19\n\x11\x61\x64\x64_score_precent\x18\x03 \x01(\x11')




_PBCONFIGACTIVITYFIREWORKS = descriptor.Descriptor(
  name='PBConfigActivityFireworks',
  full_name='PBConfigActivityFireworks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='fireworks_config', full_name='PBConfigActivityFireworks.fireworks_config', index=0,
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
  serialized_start=50,
  serialized_end=123,
)


_PBCONFIGFIREWORKS = descriptor.Descriptor(
  name='PBConfigFireworks',
  full_name='PBConfigFireworks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='start_date', full_name='PBConfigFireworks.start_date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_time', full_name='PBConfigFireworks.start_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_date', full_name='PBConfigFireworks.end_date', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_time', full_name='PBConfigFireworks.end_time', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_collect', full_name='PBConfigFireworks.score_collect', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_open', full_name='PBConfigFireworks.score_open', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_id', full_name='PBConfigFireworks.act_id', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='npc_group_name', full_name='PBConfigFireworks.npc_group_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='btn_name', full_name='PBConfigFireworks.btn_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='btn_event', full_name='PBConfigFireworks.btn_event', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_desc_info', full_name='PBConfigFireworks.act_desc_info', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_tip_type', full_name='PBConfigFireworks.act_tip_type', index=11,
      number=13, type=13, cpp_type=3, label=1,
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
  serialized_end=462,
)


_PBCONFIGFIREWORKSDESC = descriptor.Descriptor(
  name='PBConfigFireworksDesc',
  full_name='PBConfigFireworksDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='act_desc', full_name='PBConfigFireworksDesc.act_desc', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_help_desc', full_name='PBConfigFireworksDesc.act_help_desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_award_desc', full_name='PBConfigFireworksDesc.act_award_desc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_score_desc', full_name='PBConfigFireworksDesc.act_score_desc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_title_icon', full_name='PBConfigFireworksDesc.act_title_icon', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_black_icon', full_name='PBConfigFireworksDesc.act_black_icon', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=465,
  serialized_end=625,
)


_PBCONFIGFIREWORKSSCORE = descriptor.Descriptor(
  name='PBConfigFireworksScore',
  full_name='PBConfigFireworksScore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='score_start_time', full_name='PBConfigFireworksScore.score_start_time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_end_time', full_name='PBConfigFireworksScore.score_end_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quest_info', full_name='PBConfigFireworksScore.quest_info', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='player_score_limit', full_name='PBConfigFireworksScore.player_score_limit', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='act_score_total', full_name='PBConfigFireworksScore.act_score_total', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=628,
  serialized_end=800,
)


_PBCONFIGFIREWORKSQUEST = descriptor.Descriptor(
  name='PBConfigFireworksQuest',
  full_name='PBConfigFireworksQuest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='quest_id', full_name='PBConfigFireworksQuest.quest_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='add_score', full_name='PBConfigFireworksQuest.add_score', index=1,
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
  serialized_start=802,
  serialized_end=863,
)


_PBCONFIGFIREWORKSDISPLAY = descriptor.Descriptor(
  name='PBConfigFireworksDisplay',
  full_name='PBConfigFireworksDisplay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='display_start_time', full_name='PBConfigFireworksDisplay.display_start_time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='display_end_time', full_name='PBConfigFireworksDisplay.display_end_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='display_map_id', full_name='PBConfigFireworksDisplay.display_map_id', index=2,
      number=3, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='add_exp_tick_second', full_name='PBConfigFireworksDisplay.add_exp_tick_second', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='add_exp_limit', full_name='PBConfigFireworksDisplay.add_exp_limit', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_player', full_name='PBConfigFireworksDisplay.score_player', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_server', full_name='PBConfigFireworksDisplay.score_server', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_show_fireworks', full_name='PBConfigFireworksDisplay.is_show_fireworks', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_award_list', full_name='PBConfigFireworksDisplay.server_award_list', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exp_table', full_name='PBConfigFireworksDisplay.exp_table', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_award_mail_title', full_name='PBConfigFireworksDisplay.server_award_mail_title', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_award_mail_body', full_name='PBConfigFireworksDisplay.server_award_mail_body', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_server_award', full_name='PBConfigFireworksDisplay.is_server_award', index=12,
      number=13, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='show_fireworks_fx', full_name='PBConfigFireworksDisplay.show_fireworks_fx', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='display_server_notice', full_name='PBConfigFireworksDisplay.display_server_notice', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='display_server_notice_tick', full_name='PBConfigFireworksDisplay.display_server_notice_tick', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='display_preview_notice', full_name='PBConfigFireworksDisplay.display_preview_notice', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='display_preview_notice_second', full_name='PBConfigFireworksDisplay.display_preview_notice_second', index=17,
      number=18, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='map_fx', full_name='PBConfigFireworksDisplay.map_fx', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='map_fx_distance', full_name='PBConfigFireworksDisplay.map_fx_distance', index=19,
      number=20, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='map_fx_pos', full_name='PBConfigFireworksDisplay.map_fx_pos', index=20,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='add_fx_tick_second', full_name='PBConfigFireworksDisplay.add_fx_tick_second', index=21,
      number=22, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='add_fx_limit', full_name='PBConfigFireworksDisplay.add_fx_limit', index=22,
      number=23, type=17, cpp_type=1, label=1,
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
  serialized_start=866,
  serialized_end=1615,
)


_PBCONFIGFIREWORKSSOCRECHAR = descriptor.Descriptor(
  name='PBConfigFireworksSocreChar',
  full_name='PBConfigFireworksSocreChar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='score_min', full_name='PBConfigFireworksSocreChar.score_min', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_max', full_name='PBConfigFireworksSocreChar.score_max', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='add_score_precent', full_name='PBConfigFireworksSocreChar.add_score_precent', index=2,
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
  serialized_start=1617,
  serialized_end=1710,
)


_PBCONFIGFIREWORKSSOCRESERVER = descriptor.Descriptor(
  name='PBConfigFireworksSocreServer',
  full_name='PBConfigFireworksSocreServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='score_min_precent', full_name='PBConfigFireworksSocreServer.score_min_precent', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='score_max_precent', full_name='PBConfigFireworksSocreServer.score_max_precent', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='add_score_precent', full_name='PBConfigFireworksSocreServer.add_score_precent', index=2,
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
  serialized_start=1712,
  serialized_end=1823,
)

_PBCONFIGACTIVITYFIREWORKS.fields_by_name['fireworks_config'].message_type = _PBCONFIGFIREWORKS
_PBCONFIGFIREWORKS.fields_by_name['score_collect'].message_type = _PBCONFIGFIREWORKSSCORE
_PBCONFIGFIREWORKS.fields_by_name['score_open'].message_type = _PBCONFIGFIREWORKSDISPLAY
_PBCONFIGFIREWORKS.fields_by_name['act_desc_info'].message_type = _PBCONFIGFIREWORKSDESC
_PBCONFIGFIREWORKSSCORE.fields_by_name['quest_info'].message_type = _PBCONFIGFIREWORKSQUEST
_PBCONFIGFIREWORKSDISPLAY.fields_by_name['score_player'].message_type = _PBCONFIGFIREWORKSSOCRECHAR
_PBCONFIGFIREWORKSDISPLAY.fields_by_name['score_server'].message_type = _PBCONFIGFIREWORKSSOCRESERVER
_PBCONFIGFIREWORKSDISPLAY.fields_by_name['server_award_list'].message_type = tmpl_base_pb2._PBTEMPLATEITEMQUANTITYLIST
_PBCONFIGFIREWORKSDISPLAY.fields_by_name['map_fx_pos'].message_type = tmpl_base_pb2._PBTEMPLATEVECTOR2D
DESCRIPTOR.message_types_by_name['PBConfigActivityFireworks'] = _PBCONFIGACTIVITYFIREWORKS
DESCRIPTOR.message_types_by_name['PBConfigFireworks'] = _PBCONFIGFIREWORKS
DESCRIPTOR.message_types_by_name['PBConfigFireworksDesc'] = _PBCONFIGFIREWORKSDESC
DESCRIPTOR.message_types_by_name['PBConfigFireworksScore'] = _PBCONFIGFIREWORKSSCORE
DESCRIPTOR.message_types_by_name['PBConfigFireworksQuest'] = _PBCONFIGFIREWORKSQUEST
DESCRIPTOR.message_types_by_name['PBConfigFireworksDisplay'] = _PBCONFIGFIREWORKSDISPLAY
DESCRIPTOR.message_types_by_name['PBConfigFireworksSocreChar'] = _PBCONFIGFIREWORKSSOCRECHAR
DESCRIPTOR.message_types_by_name['PBConfigFireworksSocreServer'] = _PBCONFIGFIREWORKSSOCRESERVER

class PBConfigActivityFireworks(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGACTIVITYFIREWORKS
  
  # @@protoc_insertion_point(class_scope:PBConfigActivityFireworks)

class PBConfigFireworks(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGFIREWORKS
  
  # @@protoc_insertion_point(class_scope:PBConfigFireworks)

class PBConfigFireworksDesc(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGFIREWORKSDESC
  
  # @@protoc_insertion_point(class_scope:PBConfigFireworksDesc)

class PBConfigFireworksScore(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGFIREWORKSSCORE
  
  # @@protoc_insertion_point(class_scope:PBConfigFireworksScore)

class PBConfigFireworksQuest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGFIREWORKSQUEST
  
  # @@protoc_insertion_point(class_scope:PBConfigFireworksQuest)

class PBConfigFireworksDisplay(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGFIREWORKSDISPLAY
  
  # @@protoc_insertion_point(class_scope:PBConfigFireworksDisplay)

class PBConfigFireworksSocreChar(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGFIREWORKSSOCRECHAR
  
  # @@protoc_insertion_point(class_scope:PBConfigFireworksSocreChar)

class PBConfigFireworksSocreServer(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGFIREWORKSSOCRESERVER
  
  # @@protoc_insertion_point(class_scope:PBConfigFireworksSocreServer)

# @@protoc_insertion_point(module_scope)
