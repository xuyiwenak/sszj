# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_rank.proto',
  package='',
  serialized_pb='\n\x0emsg_rank.proto\x1a\x0emsg_base.proto\"\x9f\x01\n\x10PBPlayerRankData\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\r\x12\x0f\n\x07user_id\x18\x03 \x01(\r\x12\x11\n\tchar_name\x18\x04 \x01(\t\x12\x0f\n\x07role_id\x18\x05 \x01(\r\x12\x12\n\nchar_level\x18\x06 \x01(\x11\x12\x12\n\nrank_value\x18\x07 \x01(\x12\x12\x0c\n\x04rank\x18\x08 \x01(\r\"N\n\x0cPBPlayerRank\x12\x11\n\trank_type\x18\x01 \x01(\x11\x12+\n\x10player_rank_data\x18\x02 \x03(\x0b\x32\x11.PBPlayerRankData\"\x94\x01\n\x11PBRankGuildMember\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0f\n\x07game_id\x18\x02 \x01(\r\x12\x0f\n\x07user_id\x18\x03 \x01(\r\x12\x11\n\tchar_name\x18\x04 \x01(\t\x12\x12\n\nchar_level\x18\x05 \x01(\x11\x12\x0f\n\x07role_id\x18\x06 \x01(\r\x12\x14\n\x0c\x62\x61ttle_score\x18\x07 \x01(\x11\"\xc0\x01\n\x0fPBGuildRankData\x12\x10\n\x08guild_id\x18\x01 \x01(\x04\x12\x12\n\nguild_name\x18\x02 \x01(\t\x12\x13\n\x0bguild_level\x18\x03 \x01(\x11\x12\x13\n\x0bmaster_name\x18\x04 \x01(\t\x12\x16\n\x0emaster_role_id\x18\x05 \x01(\r\x12\x12\n\nrank_value\x18\x06 \x01(\x12\x12\x0c\n\x04rank\x18\x07 \x01(\r\x12#\n\x07members\x18\x08 \x03(\x0b\x32\x12.PBRankGuildMember\"K\n\x0bPBGuildRank\x12\x11\n\trank_type\x18\x01 \x01(\x11\x12)\n\x0fguild_rank_data\x18\x02 \x03(\x0b\x32\x10.PBGuildRankData*\x83\x01\n\nERankScope\x12\x15\n\x11\x45RankScope_Global\x10\x00\x12\x17\n\x13\x45RankScope_ZongHeng\x10\x01\x12\x16\n\x12\x45RankScope_XiaoYao\x10\x02\x12\x17\n\x13\x45RankScope_TianMing\x10\x03\x12\x14\n\x10\x45RankScope_Count\x10\x04*\xb9\x06\n\tERankType\x12\x15\n\x11\x45Rank_PlayerBegin\x10\x01\x12\x15\n\x11\x45Rank_PlayerLevel\x10\x01\x12\x1b\n\x17\x45Rank_PlayerBattleScore\x10\x02\x12\x18\n\x14\x45Rank_PlayerPVPScore\x10\x03\x12\x1e\n\x1a\x45Rank_PlayerTreasureLingqi\x10\x04\x12\x17\n\x13\x45Rank_PlayerShiLian\x10\x05\x12\x1a\n\x16\x45Rank_PlayerCharmPoint\x10\x06\x12\x16\n\x12\x45Rank_PlayerKiller\x10\x07\x12\x16\n\x12\x45Rank_PlayerCurExp\x10\x08\x12\x1e\n\x1a\x45Rank_PlayerPetBattleScore\x10\t\x12\x17\n\x13\x45Rank_PlayerJustice\x10\n\x12\x14\n\x10\x45Rank_PlayerEvil\x10\x0b\x12\x15\n\x11\x45Rank_PlayerDeath\x10\x0c\x12\x1a\n\x16\x45Rank_PlayerJusticeExp\x10\r\x12\x17\n\x13\x45Rank_PlayerEvilExp\x10\x0e\x12\x1a\n\x16\x45Rank_PlayerClimbTower\x10\x0f\x12\x1e\n\x1a\x45Rank_PLayerClimbTowerTime\x10\x10\x12\x1b\n\x17\x45Rank_PlayerAnswerScore\x10\x11\x12\x1f\n\x1b\x45Rank_PlayerAnswerScoreTime\x10\x12\x12 \n\x1c\x45Rank_PlayerMountBattleScore\x10\x13\x12\x1d\n\x19\x45Rank_PlayerSpanWildScore\x10\x14\x12\x1f\n\x1b\x45Rank_PlayerSendFlowerScore\x10\x15\x12#\n\x1f\x45Rank_PlayerMagicPetBattleScore\x10\x16\x12\x13\n\x0f\x45Rank_PlayerEnd\x10\x17\x12\x14\n\x10\x45Rank_GuildBegin\x10\x64\x12\x14\n\x10\x45Rank_GuildLevel\x10\x64\x12\x1a\n\x16\x45Rank_GuildBattleScore\x10\x65\x12\x19\n\x15\x45Rank_GuildMatchPoint\x10\x66\x12\x12\n\x0e\x45Rank_GuildEnd\x10g\x12\x1a\n\x15\x45Rank_SPIMHistoryRank\x10\x96\x01*7\n\x0c\x45RankObjType\x12\x13\n\x0f\x45RankObj_Player\x10\x01\x12\x12\n\x0e\x45RankObj_Guild\x10\x02\x42\x02H\x01')

_ERANKSCOPE = descriptor.EnumDescriptor(
  name='ERankScope',
  full_name='ERankScope',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ERankScope_Global', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERankScope_ZongHeng', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERankScope_XiaoYao', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERankScope_TianMing', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERankScope_Count', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=700,
  serialized_end=831,
)


_ERANKTYPE = descriptor.EnumDescriptor(
  name='ERankType',
  full_name='ERankType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerBegin', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerLevel', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerBattleScore', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerPVPScore', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerTreasureLingqi', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerShiLian', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerCharmPoint', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerKiller', index=7, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerCurExp', index=8, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerPetBattleScore', index=9, number=9,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerJustice', index=10, number=10,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerEvil', index=11, number=11,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerDeath', index=12, number=12,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerJusticeExp', index=13, number=13,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerEvilExp', index=14, number=14,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerClimbTower', index=15, number=15,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PLayerClimbTowerTime', index=16, number=16,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerAnswerScore', index=17, number=17,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerAnswerScoreTime', index=18, number=18,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerMountBattleScore', index=19, number=19,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerSpanWildScore', index=20, number=20,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerSendFlowerScore', index=21, number=21,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerMagicPetBattleScore', index=22, number=22,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_PlayerEnd', index=23, number=23,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_GuildBegin', index=24, number=100,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_GuildLevel', index=25, number=100,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_GuildBattleScore', index=26, number=101,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_GuildMatchPoint', index=27, number=102,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_GuildEnd', index=28, number=103,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERank_SPIMHistoryRank', index=29, number=150,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=834,
  serialized_end=1659,
)


_ERANKOBJTYPE = descriptor.EnumDescriptor(
  name='ERankObjType',
  full_name='ERankObjType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ERankObj_Player', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ERankObj_Guild', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1661,
  serialized_end=1716,
)


ERankScope_Global = 0
ERankScope_ZongHeng = 1
ERankScope_XiaoYao = 2
ERankScope_TianMing = 3
ERankScope_Count = 4
ERank_PlayerBegin = 1
ERank_PlayerLevel = 1
ERank_PlayerBattleScore = 2
ERank_PlayerPVPScore = 3
ERank_PlayerTreasureLingqi = 4
ERank_PlayerShiLian = 5
ERank_PlayerCharmPoint = 6
ERank_PlayerKiller = 7
ERank_PlayerCurExp = 8
ERank_PlayerPetBattleScore = 9
ERank_PlayerJustice = 10
ERank_PlayerEvil = 11
ERank_PlayerDeath = 12
ERank_PlayerJusticeExp = 13
ERank_PlayerEvilExp = 14
ERank_PlayerClimbTower = 15
ERank_PLayerClimbTowerTime = 16
ERank_PlayerAnswerScore = 17
ERank_PlayerAnswerScoreTime = 18
ERank_PlayerMountBattleScore = 19
ERank_PlayerSpanWildScore = 20
ERank_PlayerSendFlowerScore = 21
ERank_PlayerMagicPetBattleScore = 22
ERank_PlayerEnd = 23
ERank_GuildBegin = 100
ERank_GuildLevel = 100
ERank_GuildBattleScore = 101
ERank_GuildMatchPoint = 102
ERank_GuildEnd = 103
ERank_SPIMHistoryRank = 150
ERankObj_Player = 1
ERankObj_Guild = 2



_PBPLAYERRANKDATA = descriptor.Descriptor(
  name='PBPlayerRankData',
  full_name='PBPlayerRankData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='account', full_name='PBPlayerRankData.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_id', full_name='PBPlayerRankData.game_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_id', full_name='PBPlayerRankData.user_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_name', full_name='PBPlayerRankData.char_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role_id', full_name='PBPlayerRankData.role_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_level', full_name='PBPlayerRankData.char_level', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rank_value', full_name='PBPlayerRankData.rank_value', index=6,
      number=7, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rank', full_name='PBPlayerRankData.rank', index=7,
      number=8, type=13, cpp_type=3, label=1,
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
  serialized_start=35,
  serialized_end=194,
)


_PBPLAYERRANK = descriptor.Descriptor(
  name='PBPlayerRank',
  full_name='PBPlayerRank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='rank_type', full_name='PBPlayerRank.rank_type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='player_rank_data', full_name='PBPlayerRank.player_rank_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=196,
  serialized_end=274,
)


_PBRANKGUILDMEMBER = descriptor.Descriptor(
  name='PBRankGuildMember',
  full_name='PBRankGuildMember',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='account', full_name='PBRankGuildMember.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_id', full_name='PBRankGuildMember.game_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_id', full_name='PBRankGuildMember.user_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_name', full_name='PBRankGuildMember.char_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_level', full_name='PBRankGuildMember.char_level', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role_id', full_name='PBRankGuildMember.role_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='battle_score', full_name='PBRankGuildMember.battle_score', index=6,
      number=7, type=17, cpp_type=1, label=1,
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
  serialized_start=277,
  serialized_end=425,
)


_PBGUILDRANKDATA = descriptor.Descriptor(
  name='PBGuildRankData',
  full_name='PBGuildRankData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='guild_id', full_name='PBGuildRankData.guild_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='guild_name', full_name='PBGuildRankData.guild_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='guild_level', full_name='PBGuildRankData.guild_level', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='master_name', full_name='PBGuildRankData.master_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='master_role_id', full_name='PBGuildRankData.master_role_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rank_value', full_name='PBGuildRankData.rank_value', index=5,
      number=6, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rank', full_name='PBGuildRankData.rank', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='members', full_name='PBGuildRankData.members', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=428,
  serialized_end=620,
)


_PBGUILDRANK = descriptor.Descriptor(
  name='PBGuildRank',
  full_name='PBGuildRank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='rank_type', full_name='PBGuildRank.rank_type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='guild_rank_data', full_name='PBGuildRank.guild_rank_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=622,
  serialized_end=697,
)

_PBPLAYERRANK.fields_by_name['player_rank_data'].message_type = _PBPLAYERRANKDATA
_PBGUILDRANKDATA.fields_by_name['members'].message_type = _PBRANKGUILDMEMBER
_PBGUILDRANK.fields_by_name['guild_rank_data'].message_type = _PBGUILDRANKDATA
DESCRIPTOR.message_types_by_name['PBPlayerRankData'] = _PBPLAYERRANKDATA
DESCRIPTOR.message_types_by_name['PBPlayerRank'] = _PBPLAYERRANK
DESCRIPTOR.message_types_by_name['PBRankGuildMember'] = _PBRANKGUILDMEMBER
DESCRIPTOR.message_types_by_name['PBGuildRankData'] = _PBGUILDRANKDATA
DESCRIPTOR.message_types_by_name['PBGuildRank'] = _PBGUILDRANK

class PBPlayerRankData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBPLAYERRANKDATA
  
  # @@protoc_insertion_point(class_scope:PBPlayerRankData)

class PBPlayerRank(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBPLAYERRANK
  
  # @@protoc_insertion_point(class_scope:PBPlayerRank)

class PBRankGuildMember(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRANKGUILDMEMBER
  
  # @@protoc_insertion_point(class_scope:PBRankGuildMember)

class PBGuildRankData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBGUILDRANKDATA
  
  # @@protoc_insertion_point(class_scope:PBGuildRankData)

class PBGuildRank(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBGUILDRANK
  
  # @@protoc_insertion_point(class_scope:PBGuildRank)

# @@protoc_insertion_point(module_scope)
