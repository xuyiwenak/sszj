# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_exchange_shop.proto',
  package='',
  serialized_pb='\n\x18tmpl_exchange_shop.proto\x1a\x0ftmpl_base.proto\";\n\x11PBExchangeShopCfg\x12&\n\tshop_list\x18\x01 \x03(\x0b\x32\x13.PBTmplExchangeShop\"?\n\x15PBGameExchangeShopCfg\x12&\n\tshop_list\x18\x01 \x03(\x0b\x32\x13.PBTmplExchangeShop\"\x80\x01\n\x12PBTmplExchangeShop\x12\x0f\n\x07shop_id\x18\x01 \x01(\x11\x12\x11\n\tshop_name\x18\x04 \x01(\t\x12\x11\n\tshop_type\x18\x05 \x01(\x11\x12\x33\n\x12\x65xchange_time_list\x18\x06 \x03(\x0b\x32\x17.PBTmplExchangeTimeList\"\x8b\x01\n\x16PBTmplExchangeTimeList\x12+\n\x0e\x65xchange_times\x18\x01 \x03(\x0b\x32\x13.PBTmplExchangeTime\x12+\n\x0e\x65xchange_items\x18\x02 \x03(\x0b\x32\x13.PBTmplExchangeItem\x12\x17\n\x0fis_unlimit_time\x18\x03 \x01(\x11\"\x99\x02\n\x12PBTmplExchangeItem\x12\x10\n\x08goods_id\x18\x01 \x01(\x11\x12*\n\tsrc_items\x18\x02 \x03(\x0b\x32\x17.PBTemplateItemQuantity\x12+\n\ndest_items\x18\x03 \x03(\x0b\x32\x17.PBTemplateItemQuantity\x12\x14\n\x0cperson_count\x18\x04 \x01(\x11\x12\x12\n\ncamp_count\x18\x05 \x01(\x11\x12\x14\n\x0cserver_count\x18\x06 \x01(\x11\x12\x14\n\x0cis_vip_count\x18\x07 \x01(\x11\x12\x16\n\x0eis_daily_clear\x18\x08 \x01(\x11\x12\x19\n\x11\x63heck_world_level\x18\t \x01(\x11\x12\x0f\n\x07shop_id\x18\n \x01(\x11\"u\n\x12PBTmplExchangeTime\x12\x12\n\nstart_time\x18\x01 \x01(\t\x12\x15\n\rduration_hour\x18\x02 \x01(\x11\x12\x15\n\ris_new_server\x18\x03 \x01(\x11\x12\x1d\n\x15start_new_server_hour\x18\x04 \x01(\x11\"\x87\x01\n\x12PBConsignSearchCfg\x12%\n\x0ctrade_config\x18\x01 \x01(\x0b\x32\x0f.PBTradeListCfg\x12#\n\x0bsift_config\x18\x02 \x01(\x0b\x32\x0e.PBSiftListCfg\x12%\n\x0ehotitem_config\x18\x03 \x01(\x0b\x32\r.PBHotItemCfg\",\n\x0ePBTradeListCfg\x12\x1a\n\x05trade\x18\x01 \x03(\x0b\x32\x0b.PBTradeCfg\"h\n\nPBTradeCfg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08sifttype\x18\x02 \x01(\x11\x12\x18\n\x04item\x18\x03 \x03(\x0b\x32\n.PBItemCfg\x12\x0e\n\x06search\x18\x04 \x01(\t\x12\x10\n\x08itemtype\x18\x05 \x01(\t\"_\n\tPBItemCfg\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rshowsheetname\x18\x02 \x01(\t\x12\x0e\n\x06sprite\x18\x03 \x01(\t\x12\x1d\n\x08typeItem\x18\x04 \x03(\x0b\x32\x0b.PBTypeItem\"\x1e\n\nPBTypeItem\x12\x10\n\x08sitetype\x18\x01 \x01(\x11\")\n\rPBSiftListCfg\x12\x18\n\x04sift\x18\x01 \x03(\x0b\x32\n.PBSiftCfg\"b\n\tPBSiftCfg\x12\x0c\n\x04type\x18\x01 \x01(\x11\x12\x0c\n\x04name\x18\x02 \x01(\t\x12#\n\x04item\x18\x03 \x03(\x0b\x32\x15.PBSearchConditionCfg\x12\x14\n\x0c\x64\x65\x66\x61ultindex\x18\x04 \x01(\x11\"w\n\x14PBSearchConditionCfg\x12\r\n\x05index\x18\x01 \x01(\x11\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0c\n\x04suit\x18\x03 \x01(\x11\x12\r\n\x05start\x18\x04 \x01(\x11\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x11\x12\r\n\x05\x63lass\x18\x06 \x01(\x11\x12\n\n\x02ug\x18\x07 \x01(\x11\"+\n\x0cPBHotItemCfg\x12\x1b\n\x07hotitem\x18\x01 \x03(\x0b\x32\n.PBHotItem\",\n\tPBHotItem\x12\x0c\n\x04item\x18\x01 \x01(\t\x12\x11\n\tbuy_times\x18\x02 \x01(\x11\"\'\n\x0ePBConsignBlack\x12\x15\n\x04role\x18\x01 \x03(\x0b\x32\x07.PBRole\"\x18\n\x06PBRole\x12\x0e\n\x06roleid\x18\x01 \x01(\x11*}\n\tESiftType\x12\x0b\n\x07\x45ST_Hot\x10\x00\x12\r\n\tEST_Equip\x10\x01\x12\x10\n\x0c\x45ST_Designer\x10\x02\x12\x0b\n\x07\x45ST_Pet\x10\x03\x12\x10\n\x0c\x45ST_Material\x10\x04\x12\x14\n\x10\x45ST_ItemDesigner\x10\x05\x12\r\n\tEST_Other\x10\x06')

_ESIFTTYPE = descriptor.EnumDescriptor(
  name='ESiftType',
  full_name='ESiftType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='EST_Hot', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EST_Equip', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EST_Designer', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EST_Pet', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EST_Material', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EST_ItemDesigner', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EST_Other', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1688,
  serialized_end=1813,
)


EST_Hot = 0
EST_Equip = 1
EST_Designer = 2
EST_Pet = 3
EST_Material = 4
EST_ItemDesigner = 5
EST_Other = 6



_PBEXCHANGESHOPCFG = descriptor.Descriptor(
  name='PBExchangeShopCfg',
  full_name='PBExchangeShopCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='shop_list', full_name='PBExchangeShopCfg.shop_list', index=0,
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
  serialized_start=45,
  serialized_end=104,
)


_PBGAMEEXCHANGESHOPCFG = descriptor.Descriptor(
  name='PBGameExchangeShopCfg',
  full_name='PBGameExchangeShopCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='shop_list', full_name='PBGameExchangeShopCfg.shop_list', index=0,
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
  serialized_start=106,
  serialized_end=169,
)


_PBTMPLEXCHANGESHOP = descriptor.Descriptor(
  name='PBTmplExchangeShop',
  full_name='PBTmplExchangeShop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='shop_id', full_name='PBTmplExchangeShop.shop_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shop_name', full_name='PBTmplExchangeShop.shop_name', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shop_type', full_name='PBTmplExchangeShop.shop_type', index=2,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exchange_time_list', full_name='PBTmplExchangeShop.exchange_time_list', index=3,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=172,
  serialized_end=300,
)


_PBTMPLEXCHANGETIMELIST = descriptor.Descriptor(
  name='PBTmplExchangeTimeList',
  full_name='PBTmplExchangeTimeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='exchange_times', full_name='PBTmplExchangeTimeList.exchange_times', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='exchange_items', full_name='PBTmplExchangeTimeList.exchange_items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_unlimit_time', full_name='PBTmplExchangeTimeList.is_unlimit_time', index=2,
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
  serialized_start=303,
  serialized_end=442,
)


_PBTMPLEXCHANGEITEM = descriptor.Descriptor(
  name='PBTmplExchangeItem',
  full_name='PBTmplExchangeItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='goods_id', full_name='PBTmplExchangeItem.goods_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='src_items', full_name='PBTmplExchangeItem.src_items', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dest_items', full_name='PBTmplExchangeItem.dest_items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='person_count', full_name='PBTmplExchangeItem.person_count', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='camp_count', full_name='PBTmplExchangeItem.camp_count', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='server_count', full_name='PBTmplExchangeItem.server_count', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_vip_count', full_name='PBTmplExchangeItem.is_vip_count', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_daily_clear', full_name='PBTmplExchangeItem.is_daily_clear', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='check_world_level', full_name='PBTmplExchangeItem.check_world_level', index=8,
      number=9, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shop_id', full_name='PBTmplExchangeItem.shop_id', index=9,
      number=10, type=17, cpp_type=1, label=1,
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
  serialized_start=445,
  serialized_end=726,
)


_PBTMPLEXCHANGETIME = descriptor.Descriptor(
  name='PBTmplExchangeTime',
  full_name='PBTmplExchangeTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='start_time', full_name='PBTmplExchangeTime.start_time', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='duration_hour', full_name='PBTmplExchangeTime.duration_hour', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_new_server', full_name='PBTmplExchangeTime.is_new_server', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_new_server_hour', full_name='PBTmplExchangeTime.start_new_server_hour', index=3,
      number=4, type=17, cpp_type=1, label=1,
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
  serialized_start=728,
  serialized_end=845,
)


_PBCONSIGNSEARCHCFG = descriptor.Descriptor(
  name='PBConsignSearchCfg',
  full_name='PBConsignSearchCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='trade_config', full_name='PBConsignSearchCfg.trade_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sift_config', full_name='PBConsignSearchCfg.sift_config', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hotitem_config', full_name='PBConsignSearchCfg.hotitem_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=848,
  serialized_end=983,
)


_PBTRADELISTCFG = descriptor.Descriptor(
  name='PBTradeListCfg',
  full_name='PBTradeListCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='trade', full_name='PBTradeListCfg.trade', index=0,
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
  serialized_start=985,
  serialized_end=1029,
)


_PBTRADECFG = descriptor.Descriptor(
  name='PBTradeCfg',
  full_name='PBTradeCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBTradeCfg.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sifttype', full_name='PBTradeCfg.sifttype', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='PBTradeCfg.item', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='search', full_name='PBTradeCfg.search', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='itemtype', full_name='PBTradeCfg.itemtype', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=1031,
  serialized_end=1135,
)


_PBITEMCFG = descriptor.Descriptor(
  name='PBItemCfg',
  full_name='PBItemCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBItemCfg.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='showsheetname', full_name='PBItemCfg.showsheetname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sprite', full_name='PBItemCfg.sprite', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='typeItem', full_name='PBItemCfg.typeItem', index=3,
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
  serialized_start=1137,
  serialized_end=1232,
)


_PBTYPEITEM = descriptor.Descriptor(
  name='PBTypeItem',
  full_name='PBTypeItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sitetype', full_name='PBTypeItem.sitetype', index=0,
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
  serialized_start=1234,
  serialized_end=1264,
)


_PBSIFTLISTCFG = descriptor.Descriptor(
  name='PBSiftListCfg',
  full_name='PBSiftListCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sift', full_name='PBSiftListCfg.sift', index=0,
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
  serialized_start=1266,
  serialized_end=1307,
)


_PBSIFTCFG = descriptor.Descriptor(
  name='PBSiftCfg',
  full_name='PBSiftCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='PBSiftCfg.type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='PBSiftCfg.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='PBSiftCfg.item', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='defaultindex', full_name='PBSiftCfg.defaultindex', index=3,
      number=4, type=17, cpp_type=1, label=1,
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
  serialized_start=1309,
  serialized_end=1407,
)


_PBSEARCHCONDITIONCFG = descriptor.Descriptor(
  name='PBSearchConditionCfg',
  full_name='PBSearchConditionCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='index', full_name='PBSearchConditionCfg.index', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key', full_name='PBSearchConditionCfg.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='suit', full_name='PBSearchConditionCfg.suit', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start', full_name='PBSearchConditionCfg.start', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end', full_name='PBSearchConditionCfg.end', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='class', full_name='PBSearchConditionCfg.class', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ug', full_name='PBSearchConditionCfg.ug', index=6,
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
  serialized_start=1409,
  serialized_end=1528,
)


_PBHOTITEMCFG = descriptor.Descriptor(
  name='PBHotItemCfg',
  full_name='PBHotItemCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hotitem', full_name='PBHotItemCfg.hotitem', index=0,
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
  serialized_start=1530,
  serialized_end=1573,
)


_PBHOTITEM = descriptor.Descriptor(
  name='PBHotItem',
  full_name='PBHotItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='item', full_name='PBHotItem.item', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buy_times', full_name='PBHotItem.buy_times', index=1,
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
  serialized_start=1575,
  serialized_end=1619,
)


_PBCONSIGNBLACK = descriptor.Descriptor(
  name='PBConsignBlack',
  full_name='PBConsignBlack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='role', full_name='PBConsignBlack.role', index=0,
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
  serialized_start=1621,
  serialized_end=1660,
)


_PBROLE = descriptor.Descriptor(
  name='PBRole',
  full_name='PBRole',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roleid', full_name='PBRole.roleid', index=0,
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
  serialized_start=1662,
  serialized_end=1686,
)

_PBEXCHANGESHOPCFG.fields_by_name['shop_list'].message_type = _PBTMPLEXCHANGESHOP
_PBGAMEEXCHANGESHOPCFG.fields_by_name['shop_list'].message_type = _PBTMPLEXCHANGESHOP
_PBTMPLEXCHANGESHOP.fields_by_name['exchange_time_list'].message_type = _PBTMPLEXCHANGETIMELIST
_PBTMPLEXCHANGETIMELIST.fields_by_name['exchange_times'].message_type = _PBTMPLEXCHANGETIME
_PBTMPLEXCHANGETIMELIST.fields_by_name['exchange_items'].message_type = _PBTMPLEXCHANGEITEM
_PBTMPLEXCHANGEITEM.fields_by_name['src_items'].message_type = tmpl_base_pb2._PBTEMPLATEITEMQUANTITY
_PBTMPLEXCHANGEITEM.fields_by_name['dest_items'].message_type = tmpl_base_pb2._PBTEMPLATEITEMQUANTITY
_PBCONSIGNSEARCHCFG.fields_by_name['trade_config'].message_type = _PBTRADELISTCFG
_PBCONSIGNSEARCHCFG.fields_by_name['sift_config'].message_type = _PBSIFTLISTCFG
_PBCONSIGNSEARCHCFG.fields_by_name['hotitem_config'].message_type = _PBHOTITEMCFG
_PBTRADELISTCFG.fields_by_name['trade'].message_type = _PBTRADECFG
_PBTRADECFG.fields_by_name['item'].message_type = _PBITEMCFG
_PBITEMCFG.fields_by_name['typeItem'].message_type = _PBTYPEITEM
_PBSIFTLISTCFG.fields_by_name['sift'].message_type = _PBSIFTCFG
_PBSIFTCFG.fields_by_name['item'].message_type = _PBSEARCHCONDITIONCFG
_PBHOTITEMCFG.fields_by_name['hotitem'].message_type = _PBHOTITEM
_PBCONSIGNBLACK.fields_by_name['role'].message_type = _PBROLE
DESCRIPTOR.message_types_by_name['PBExchangeShopCfg'] = _PBEXCHANGESHOPCFG
DESCRIPTOR.message_types_by_name['PBGameExchangeShopCfg'] = _PBGAMEEXCHANGESHOPCFG
DESCRIPTOR.message_types_by_name['PBTmplExchangeShop'] = _PBTMPLEXCHANGESHOP
DESCRIPTOR.message_types_by_name['PBTmplExchangeTimeList'] = _PBTMPLEXCHANGETIMELIST
DESCRIPTOR.message_types_by_name['PBTmplExchangeItem'] = _PBTMPLEXCHANGEITEM
DESCRIPTOR.message_types_by_name['PBTmplExchangeTime'] = _PBTMPLEXCHANGETIME
DESCRIPTOR.message_types_by_name['PBConsignSearchCfg'] = _PBCONSIGNSEARCHCFG
DESCRIPTOR.message_types_by_name['PBTradeListCfg'] = _PBTRADELISTCFG
DESCRIPTOR.message_types_by_name['PBTradeCfg'] = _PBTRADECFG
DESCRIPTOR.message_types_by_name['PBItemCfg'] = _PBITEMCFG
DESCRIPTOR.message_types_by_name['PBTypeItem'] = _PBTYPEITEM
DESCRIPTOR.message_types_by_name['PBSiftListCfg'] = _PBSIFTLISTCFG
DESCRIPTOR.message_types_by_name['PBSiftCfg'] = _PBSIFTCFG
DESCRIPTOR.message_types_by_name['PBSearchConditionCfg'] = _PBSEARCHCONDITIONCFG
DESCRIPTOR.message_types_by_name['PBHotItemCfg'] = _PBHOTITEMCFG
DESCRIPTOR.message_types_by_name['PBHotItem'] = _PBHOTITEM
DESCRIPTOR.message_types_by_name['PBConsignBlack'] = _PBCONSIGNBLACK
DESCRIPTOR.message_types_by_name['PBRole'] = _PBROLE

class PBExchangeShopCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBEXCHANGESHOPCFG
  
  # @@protoc_insertion_point(class_scope:PBExchangeShopCfg)

class PBGameExchangeShopCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBGAMEEXCHANGESHOPCFG
  
  # @@protoc_insertion_point(class_scope:PBGameExchangeShopCfg)

class PBTmplExchangeShop(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTMPLEXCHANGESHOP
  
  # @@protoc_insertion_point(class_scope:PBTmplExchangeShop)

class PBTmplExchangeTimeList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTMPLEXCHANGETIMELIST
  
  # @@protoc_insertion_point(class_scope:PBTmplExchangeTimeList)

class PBTmplExchangeItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTMPLEXCHANGEITEM
  
  # @@protoc_insertion_point(class_scope:PBTmplExchangeItem)

class PBTmplExchangeTime(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTMPLEXCHANGETIME
  
  # @@protoc_insertion_point(class_scope:PBTmplExchangeTime)

class PBConsignSearchCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONSIGNSEARCHCFG
  
  # @@protoc_insertion_point(class_scope:PBConsignSearchCfg)

class PBTradeListCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTRADELISTCFG
  
  # @@protoc_insertion_point(class_scope:PBTradeListCfg)

class PBTradeCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTRADECFG
  
  # @@protoc_insertion_point(class_scope:PBTradeCfg)

class PBItemCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBITEMCFG
  
  # @@protoc_insertion_point(class_scope:PBItemCfg)

class PBTypeItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBTYPEITEM
  
  # @@protoc_insertion_point(class_scope:PBTypeItem)

class PBSiftListCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSIFTLISTCFG
  
  # @@protoc_insertion_point(class_scope:PBSiftListCfg)

class PBSiftCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSIFTCFG
  
  # @@protoc_insertion_point(class_scope:PBSiftCfg)

class PBSearchConditionCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBSEARCHCONDITIONCFG
  
  # @@protoc_insertion_point(class_scope:PBSearchConditionCfg)

class PBHotItemCfg(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBHOTITEMCFG
  
  # @@protoc_insertion_point(class_scope:PBHotItemCfg)

class PBHotItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBHOTITEM
  
  # @@protoc_insertion_point(class_scope:PBHotItem)

class PBConsignBlack(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONSIGNBLACK
  
  # @@protoc_insertion_point(class_scope:PBConsignBlack)

class PBRole(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBROLE
  
  # @@protoc_insertion_point(class_scope:PBRole)

# @@protoc_insertion_point(module_scope)