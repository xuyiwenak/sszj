# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_sign.proto',
  package='',
  serialized_pb='\n\x0ftmpl_sign.proto\x1a\x0ftmpl_base.proto\"=\n\x14PBSignOccBaseCfgList\x12%\n\x07\x63\x66gList\x18\x01 \x03(\x0b\x32\x14.PBSignOcuBaseConfig\"G\n\x13PBSignOcuBaseConfig\x12\x0c\n\x04occu\x18\x01 \x01(\x11\x12\"\n\x07\x62\x61secof\x18\x02 \x01(\x0b\x32\x11.PBSignBaseConfig\"\xdd\x01\n\x10PBSignBaseConfig\x12\"\n\x0cnewsign_list\x18\x01 \x01(\x0b\x32\x0c.PBNewerSign\x12$\n\x0emonthsign_list\x18\x02 \x01(\x0b\x32\x0c.PBMonthSign\x12(\n\x10levelreward_list\x18\x03 \x01(\x0b\x32\x0e.PBLevelReward\x12*\n\x11onlinereward_list\x18\x04 \x01(\x0b\x32\x0f.PBOnlineReward\x12)\n\x0f\x61\x64\x64_energy_list\x18\x05 \x01(\x0b\x32\x10.PBAddEnergyList\"\x98\x01\n\x0bPBNewerSign\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x0enewsign_reward\x18\x02 \x03(\x0b\x32\x12.PBNewersignReward\x12\x12\n\natlas_name\x18\x03 \x01(\t\x12\x13\n\x0bsprite_name\x18\x04 \x01(\t\x12\r\n\x05sheet\x18\x05 \x01(\t\x12\x17\n\x0f\x61vaterSheetName\x18\x06 \x01(\t\"9\n\x11PBNewersignReward\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x18\n\titem_list\x18\x02 \x03(\x0b\x32\x05.Item\"\xe1\x01\n\x0bPBMonthSign\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ncost_sheet\x18\x02 \x01(\t\x12\x10\n\x08\x63ost_num\x18\x03 \x01(\x11\x12,\n\x10monthsign_reward\x18\x04 \x03(\x0b\x32\x12.PBMonthsignReward\x12\x15\n\rbuqian_sprite\x18\x05 \x01(\t\x12\x15\n\rlingqu_sprite\x18\x06 \x01(\t\x12\x12\n\nvip_sprite\x18\x07 \x01(\t\x12\x15\n\rdaytag_sprite\x18\x08 \x01(\t\x12\x17\n\x0f\x61vaterSheetName\x18\t \x01(\t\"n\n\x11PBMonthsignReward\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x0b\n\x03vip\x18\x02 \x01(\x11\x12\r\n\x05times\x18\x03 \x01(\x11\x12\r\n\x05sheet\x18\x04 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\x11\x12\x10\n\x08isdaytag\x18\x06 \x01(\x08\"d\n\rPBLevelReward\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x10levelreward_list\x18\x02 \x03(\x0b\x32\x12.PBLevelRewardList\x12\x17\n\x0f\x61vaterSheetName\x18\x03 \x01(\t\"H\n\x11PBLevelRewardList\x12\n\n\x02id\x18\x01 \x01(\x11\x12\r\n\x05level\x18\x02 \x01(\x11\x12\x18\n\titem_list\x18\x03 \x03(\x0b\x32\x05.Item\"g\n\x0ePBOnlineReward\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x11onlinereward_list\x18\x02 \x03(\x0b\x32\x13.PBOnlineRewardList\x12\x17\n\x0f\x61vaterSheetName\x18\x03 \x01(\t\"O\n\x12PBOnlineRewardList\x12\n\n\x02id\x18\x01 \x01(\x11\x12\x13\n\x0bneed_second\x18\x02 \x01(\x11\x12\x18\n\titem_list\x18\x03 \x03(\x0b\x32\x05.Item\"\'\n\x04Item\x12\r\n\x05sheet\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x11\"O\n\x0fPBAddEnergyList\x12#\n\nadd_energy\x18\x01 \x03(\x0b\x32\x0f.PBAddEnergyCfg\x12\x17\n\x0f\x61vaterSheetName\x18\x02 \x01(\t\"\x94\x01\n\x0ePBAddEnergyCfg\x12\x12\n\nstart_time\x18\x01 \x01(\x11\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x11\x12\x13\n\x0b\x65nergy_item\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\x11\x12\x12\n\nlabel_text\x18\x05 \x01(\t\x12\x12\n\natlas_name\x18\x06 \x01(\t\x12\x13\n\x0bsprite_name\x18\x07 \x01(\t')




_PBSIGNOCCBASECFGLIST = descriptor.Descriptor(
  name='PBSignOccBaseCfgList',
  full_name='PBSignOccBaseCfgList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cfgList', full_name='PBSignOccBaseCfgList.cfgList', index=0,
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
  serialized_start=36,
  serialized_end=97,
)


_PBSIGNOCUBASECONFIG = descriptor.Descriptor(
  name='PBSignOcuBaseConfig',
  full_name='PBSignOcuBaseConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='occu', full_name='PBSignOcuBaseConfig.occu', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='basecof', full_name='PBSignOcuBaseConfig.basecof', index=1,
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=99,
  serialized_end=170,
)


_PBSIGNBASECONFIG = descriptor.Descriptor(
  name='PBSignBaseConfig',
  full_name='PBSignBaseConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='newsign_list', full_name='PBSignBaseConfig.newsign_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='monthsign_list', full_name='PBSignBaseConfig.monthsign_list', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='levelreward_list', full_name='PBSignBaseConfig.levelreward_list', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='onlinereward_list', full_name='PBSignBaseConfig.onlinereward_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='add_energy_list', full_name='PBSignBaseConfig.add_energy_list', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=173,
  serialized_end=394,
)


_PBNEWERSIGN = descriptor.Descriptor(
  name='PBNewerSign',
  full_name='PBNewerSign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBNewerSign.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='newsign_reward', full_name='PBNewerSign.newsign_reward', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='atlas_name', full_name='PBNewerSign.atlas_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sprite_name', full_name='PBNewerSign.sprite_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sheet', full_name='PBNewerSign.sheet', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='avaterSheetName', full_name='PBNewerSign.avaterSheetName', index=5,
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
  serialized_start=397,
  serialized_end=549,
)


_PBNEWERSIGNREWARD = descriptor.Descriptor(
  name='PBNewersignReward',
  full_name='PBNewersignReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='PBNewersignReward.id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_list', full_name='PBNewersignReward.item_list', index=1,
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
  serialized_start=551,
  serialized_end=608,
)


_PBMONTHSIGN = descriptor.Descriptor(
  name='PBMonthSign',
  full_name='PBMonthSign',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBMonthSign.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_sheet', full_name='PBMonthSign.cost_sheet', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_num', full_name='PBMonthSign.cost_num', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='monthsign_reward', full_name='PBMonthSign.monthsign_reward', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buqian_sprite', full_name='PBMonthSign.buqian_sprite', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lingqu_sprite', full_name='PBMonthSign.lingqu_sprite', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vip_sprite', full_name='PBMonthSign.vip_sprite', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='daytag_sprite', full_name='PBMonthSign.daytag_sprite', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='avaterSheetName', full_name='PBMonthSign.avaterSheetName', index=8,
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
  serialized_start=611,
  serialized_end=836,
)


_PBMONTHSIGNREWARD = descriptor.Descriptor(
  name='PBMonthsignReward',
  full_name='PBMonthsignReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='PBMonthsignReward.id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vip', full_name='PBMonthsignReward.vip', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='times', full_name='PBMonthsignReward.times', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sheet', full_name='PBMonthsignReward.sheet', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quantity', full_name='PBMonthsignReward.quantity', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isdaytag', full_name='PBMonthsignReward.isdaytag', index=5,
      number=6, type=8, cpp_type=7, label=1,
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
  serialized_start=838,
  serialized_end=948,
)


_PBLEVELREWARD = descriptor.Descriptor(
  name='PBLevelReward',
  full_name='PBLevelReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBLevelReward.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='levelreward_list', full_name='PBLevelReward.levelreward_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='avaterSheetName', full_name='PBLevelReward.avaterSheetName', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=950,
  serialized_end=1050,
)


_PBLEVELREWARDLIST = descriptor.Descriptor(
  name='PBLevelRewardList',
  full_name='PBLevelRewardList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='PBLevelRewardList.id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='PBLevelRewardList.level', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_list', full_name='PBLevelRewardList.item_list', index=2,
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
  serialized_start=1052,
  serialized_end=1124,
)


_PBONLINEREWARD = descriptor.Descriptor(
  name='PBOnlineReward',
  full_name='PBOnlineReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBOnlineReward.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='onlinereward_list', full_name='PBOnlineReward.onlinereward_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='avaterSheetName', full_name='PBOnlineReward.avaterSheetName', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=1126,
  serialized_end=1229,
)


_PBONLINEREWARDLIST = descriptor.Descriptor(
  name='PBOnlineRewardList',
  full_name='PBOnlineRewardList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='PBOnlineRewardList.id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='need_second', full_name='PBOnlineRewardList.need_second', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_list', full_name='PBOnlineRewardList.item_list', index=2,
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
  serialized_start=1231,
  serialized_end=1310,
)


_ITEM = descriptor.Descriptor(
  name='Item',
  full_name='Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sheet', full_name='Item.sheet', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quantity', full_name='Item.quantity', index=1,
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
  serialized_start=1312,
  serialized_end=1351,
)


_PBADDENERGYLIST = descriptor.Descriptor(
  name='PBAddEnergyList',
  full_name='PBAddEnergyList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='add_energy', full_name='PBAddEnergyList.add_energy', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='avaterSheetName', full_name='PBAddEnergyList.avaterSheetName', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1353,
  serialized_end=1432,
)


_PBADDENERGYCFG = descriptor.Descriptor(
  name='PBAddEnergyCfg',
  full_name='PBAddEnergyCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='start_time', full_name='PBAddEnergyCfg.start_time', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_time', full_name='PBAddEnergyCfg.end_time', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='energy_item', full_name='PBAddEnergyCfg.energy_item', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='PBAddEnergyCfg.id', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='label_text', full_name='PBAddEnergyCfg.label_text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='atlas_name', full_name='PBAddEnergyCfg.atlas_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sprite_name', full_name='PBAddEnergyCfg.sprite_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=1435,
  serialized_end=1583,
)

_PBSIGNOCCBASECFGLIST.fields_by_name['cfgList'].message_type = _PBSIGNOCUBASECONFIG
_PBSIGNOCUBASECONFIG.fields_by_name['basecof'].message_type = _PBSIGNBASECONFIG
_PBSIGNBASECONFIG.fields_by_name['newsign_list'].message_type = _PBNEWERSIGN
_PBSIGNBASECONFIG.fields_by_name['monthsign_list'].message_type = _PBMONTHSIGN
_PBSIGNBASECONFIG.fields_by_name['levelreward_list'].message_type = _PBLEVELREWARD
_PBSIGNBASECONFIG.fields_by_name['onlinereward_list'].message_type = _PBONLINEREWARD
_PBSIGNBASECONFIG.fields_by_name['add_energy_list'].message_type = _PBADDENERGYLIST
_PBNEWERSIGN.fields_by_name['newsign_reward'].message_type = _PBNEWERSIGNREWARD
_PBNEWERSIGNREWARD.fields_by_name['item_list'].message_type = _ITEM
_PBMONTHSIGN.fields_by_name['monthsign_reward'].message_type = _PBMONTHSIGNREWARD
_PBLEVELREWARD.fields_by_name['levelreward_list'].message_type = _PBLEVELREWARDLIST
_PBLEVELREWARDLIST.fields_by_name['item_list'].message_type = _ITEM
_PBONLINEREWARD.fields_by_name['onlinereward_list'].message_type = _PBONLINEREWARDLIST
_PBONLINEREWARDLIST.fields_by_name['item_list'].message_type = _ITEM
_PBADDENERGYLIST.fields_by_name['add_energy'].message_type = _PBADDENERGYCFG
DESCRIPTOR.message_types_by_name['PBSignOccBaseCfgList'] = _PBSIGNOCCBASECFGLIST
DESCRIPTOR.message_types_by_name['PBSignOcuBaseConfig'] = _PBSIGNOCUBASECONFIG
DESCRIPTOR.message_types_by_name['PBSignBaseConfig'] = _PBSIGNBASECONFIG
DESCRIPTOR.message_types_by_name['PBNewerSign'] = _PBNEWERSIGN
DESCRIPTOR.message_types_by_name['PBNewersignReward'] = _PBNEWERSIGNREWARD
DESCRIPTOR.message_types_by_name['PBMonthSign'] = _PBMONTHSIGN
DESCRIPTOR.message_types_by_name['PBMonthsignReward'] = _PBMONTHSIGNREWARD
DESCRIPTOR.message_types_by_name['PBLevelReward'] = _PBLEVELREWARD
DESCRIPTOR.message_types_by_name['PBLevelRewardList'] = _PBLEVELREWARDLIST
DESCRIPTOR.message_types_by_name['PBOnlineReward'] = _PBONLINEREWARD
DESCRIPTOR.message_types_by_name['PBOnlineRewardList'] = _PBONLINEREWARDLIST
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['PBAddEnergyList'] = _PBADDENERGYLIST
DESCRIPTOR.message_types_by_name['PBAddEnergyCfg'] = _PBADDENERGYCFG

class PBSignOccBaseCfgList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSIGNOCCBASECFGLIST
  
  # @@protoc_insertion_point(class_scope:PBSignOccBaseCfgList)

class PBSignOcuBaseConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSIGNOCUBASECONFIG
  
  # @@protoc_insertion_point(class_scope:PBSignOcuBaseConfig)

class PBSignBaseConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSIGNBASECONFIG
  
  # @@protoc_insertion_point(class_scope:PBSignBaseConfig)

class PBNewerSign(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBNEWERSIGN
  
  # @@protoc_insertion_point(class_scope:PBNewerSign)

class PBNewersignReward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBNEWERSIGNREWARD
  
  # @@protoc_insertion_point(class_scope:PBNewersignReward)

class PBMonthSign(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMONTHSIGN
  
  # @@protoc_insertion_point(class_scope:PBMonthSign)

class PBMonthsignReward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMONTHSIGNREWARD
  
  # @@protoc_insertion_point(class_scope:PBMonthsignReward)

class PBLevelReward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBLEVELREWARD
  
  # @@protoc_insertion_point(class_scope:PBLevelReward)

class PBLevelRewardList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBLEVELREWARDLIST
  
  # @@protoc_insertion_point(class_scope:PBLevelRewardList)

class PBOnlineReward(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONLINEREWARD
  
  # @@protoc_insertion_point(class_scope:PBOnlineReward)

class PBOnlineRewardList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONLINEREWARDLIST
  
  # @@protoc_insertion_point(class_scope:PBOnlineRewardList)

class Item(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEM
  
  # @@protoc_insertion_point(class_scope:Item)

class PBAddEnergyList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBADDENERGYLIST
  
  # @@protoc_insertion_point(class_scope:PBAddEnergyList)

class PBAddEnergyCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBADDENERGYCFG
  
  # @@protoc_insertion_point(class_scope:PBAddEnergyCfg)

# @@protoc_insertion_point(module_scope)
