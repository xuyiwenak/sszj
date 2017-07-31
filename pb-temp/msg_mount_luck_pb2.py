# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_mount_luck.proto',
  package='',
  serialized_pb='\n\x14msg_mount_luck.proto\"\x9e\x02\n\x0ePBMsgMountLuck\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.PBELuckType\x12\x11\n\tcur_level\x18\x02 \x01(\x11\x12\x11\n\tcur_start\x18\x03 \x01(\x11\x12\x12\n\ncur_battle\x18\x04 \x01(\x11\x12\x16\n\x0e\x63ur_luck_value\x18\x05 \x01(\x11\x12\x12\n\nnext_level\x18\x06 \x01(\x11\x12\x12\n\nnext_start\x18\x07 \x01(\x11\x12\x13\n\x0bnext_battle\x18\x08 \x01(\x11\x12\x17\n\x0fnext_luck_value\x18\t \x01(\x11\x12\x14\n\x0cis_max_level\x18\n \x01(\x08\x12\x1c\n\x07pb_Item\x18\x0b \x03(\x0b\x32\x0b.PBLuckItem\x12\x14\n\x0c\x62\x61ttle_score\x18\x0c \x01(\x11\"*\n\nPBLuckItem\x12\x0f\n\x07sheetId\x18\x01 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x11\"\x19\n\x17PBMsgMoutAllLuckRequest\"Q\n\x19PBMsgMountAllLuckResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\"\n\tluck_info\x18\x02 \x03(\x0b\x32\x0f.PBMsgMountLuck\"K\n\x1bPBMsgMountLuckUpdateRequest\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.PBELuckType\x12\x10\n\x08sheet_id\x18\x02 \x01(\t\"T\n\x1cPBMsgMountLuckUpdateResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\"\n\tluck_info\x18\x02 \x01(\x0b\x32\x0f.PBMsgMountLuck\"L\n\x13PBMsgLuckInfoNotice\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.PBELuckType\x12\x19\n\x04item\x18\x02 \x03(\x0b\x32\x0b.PBLuckItem\"I\n\x17PBMsgLuckInfoListNotice\x12.\n\x10luck_info_notice\x18\x01 \x03(\x0b\x32\x14.PBMsgLuckInfoNotice\"M\n\nPBLuckInfo\x12\x1a\n\x04type\x18\x01 \x01(\x0e\x32\x0c.PBELuckType\x12\x11\n\tcur_level\x18\x02 \x01(\x11\x12\x10\n\x08\x63ur_star\x18\x03 \x01(\x11\",\n\x0cPBDBLuckInfo\x12\x1c\n\x07\x64\x62_info\x18\x01 \x03(\x0b\x32\x0b.PBLuckInfo*;\n\x0bPBELuckType\x12\x16\n\x12\x65LuckType_XianYuan\x10\x00\x12\x14\n\x10\x65LuckType_MoYuan\x10\x01\x42\x02H\x01')

_PBELUCKTYPE = descriptor.EnumDescriptor(
  name='PBELuckType',
  full_name='PBELuckType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='eLuckType_XianYuan', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='eLuckType_MoYuan', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=908,
  serialized_end=967,
)


eLuckType_XianYuan = 0
eLuckType_MoYuan = 1



_PBMSGMOUNTLUCK = descriptor.Descriptor(
  name='PBMsgMountLuck',
  full_name='PBMsgMountLuck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='PBMsgMountLuck.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_level', full_name='PBMsgMountLuck.cur_level', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_start', full_name='PBMsgMountLuck.cur_start', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_battle', full_name='PBMsgMountLuck.cur_battle', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_luck_value', full_name='PBMsgMountLuck.cur_luck_value', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next_level', full_name='PBMsgMountLuck.next_level', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next_start', full_name='PBMsgMountLuck.next_start', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next_battle', full_name='PBMsgMountLuck.next_battle', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next_luck_value', full_name='PBMsgMountLuck.next_luck_value', index=8,
      number=9, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_max_level', full_name='PBMsgMountLuck.is_max_level', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pb_Item', full_name='PBMsgMountLuck.pb_Item', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='battle_score', full_name='PBMsgMountLuck.battle_score', index=11,
      number=12, type=17, cpp_type=1, label=1,
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
  serialized_start=25,
  serialized_end=311,
)


_PBLUCKITEM = descriptor.Descriptor(
  name='PBLuckItem',
  full_name='PBLuckItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sheetId', full_name='PBLuckItem.sheetId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='num', full_name='PBLuckItem.num', index=1,
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
  serialized_start=313,
  serialized_end=355,
)


_PBMSGMOUTALLLUCKREQUEST = descriptor.Descriptor(
  name='PBMsgMoutAllLuckRequest',
  full_name='PBMsgMoutAllLuckRequest',
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
  serialized_start=357,
  serialized_end=382,
)


_PBMSGMOUNTALLLUCKRESPONSE = descriptor.Descriptor(
  name='PBMsgMountAllLuckResponse',
  full_name='PBMsgMountAllLuckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgMountAllLuckResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='luck_info', full_name='PBMsgMountAllLuckResponse.luck_info', index=1,
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
  serialized_start=384,
  serialized_end=465,
)


_PBMSGMOUNTLUCKUPDATEREQUEST = descriptor.Descriptor(
  name='PBMsgMountLuckUpdateRequest',
  full_name='PBMsgMountLuckUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='PBMsgMountLuckUpdateRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sheet_id', full_name='PBMsgMountLuckUpdateRequest.sheet_id', index=1,
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
  serialized_start=467,
  serialized_end=542,
)


_PBMSGMOUNTLUCKUPDATERESPONSE = descriptor.Descriptor(
  name='PBMsgMountLuckUpdateResponse',
  full_name='PBMsgMountLuckUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgMountLuckUpdateResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='luck_info', full_name='PBMsgMountLuckUpdateResponse.luck_info', index=1,
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
  serialized_start=544,
  serialized_end=628,
)


_PBMSGLUCKINFONOTICE = descriptor.Descriptor(
  name='PBMsgLuckInfoNotice',
  full_name='PBMsgLuckInfoNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='PBMsgLuckInfoNotice.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='PBMsgLuckInfoNotice.item', index=1,
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
  serialized_start=630,
  serialized_end=706,
)


_PBMSGLUCKINFOLISTNOTICE = descriptor.Descriptor(
  name='PBMsgLuckInfoListNotice',
  full_name='PBMsgLuckInfoListNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='luck_info_notice', full_name='PBMsgLuckInfoListNotice.luck_info_notice', index=0,
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
  serialized_start=708,
  serialized_end=781,
)


_PBLUCKINFO = descriptor.Descriptor(
  name='PBLuckInfo',
  full_name='PBLuckInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='PBLuckInfo.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_level', full_name='PBLuckInfo.cur_level', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_star', full_name='PBLuckInfo.cur_star', index=2,
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
  serialized_start=783,
  serialized_end=860,
)


_PBDBLUCKINFO = descriptor.Descriptor(
  name='PBDBLuckInfo',
  full_name='PBDBLuckInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='db_info', full_name='PBDBLuckInfo.db_info', index=0,
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
  serialized_start=862,
  serialized_end=906,
)

_PBMSGMOUNTLUCK.fields_by_name['type'].enum_type = _PBELUCKTYPE
_PBMSGMOUNTLUCK.fields_by_name['pb_Item'].message_type = _PBLUCKITEM
_PBMSGMOUNTALLLUCKRESPONSE.fields_by_name['luck_info'].message_type = _PBMSGMOUNTLUCK
_PBMSGMOUNTLUCKUPDATEREQUEST.fields_by_name['type'].enum_type = _PBELUCKTYPE
_PBMSGMOUNTLUCKUPDATERESPONSE.fields_by_name['luck_info'].message_type = _PBMSGMOUNTLUCK
_PBMSGLUCKINFONOTICE.fields_by_name['type'].enum_type = _PBELUCKTYPE
_PBMSGLUCKINFONOTICE.fields_by_name['item'].message_type = _PBLUCKITEM
_PBMSGLUCKINFOLISTNOTICE.fields_by_name['luck_info_notice'].message_type = _PBMSGLUCKINFONOTICE
_PBLUCKINFO.fields_by_name['type'].enum_type = _PBELUCKTYPE
_PBDBLUCKINFO.fields_by_name['db_info'].message_type = _PBLUCKINFO
DESCRIPTOR.message_types_by_name['PBMsgMountLuck'] = _PBMSGMOUNTLUCK
DESCRIPTOR.message_types_by_name['PBLuckItem'] = _PBLUCKITEM
DESCRIPTOR.message_types_by_name['PBMsgMoutAllLuckRequest'] = _PBMSGMOUTALLLUCKREQUEST
DESCRIPTOR.message_types_by_name['PBMsgMountAllLuckResponse'] = _PBMSGMOUNTALLLUCKRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgMountLuckUpdateRequest'] = _PBMSGMOUNTLUCKUPDATEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgMountLuckUpdateResponse'] = _PBMSGMOUNTLUCKUPDATERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgLuckInfoNotice'] = _PBMSGLUCKINFONOTICE
DESCRIPTOR.message_types_by_name['PBMsgLuckInfoListNotice'] = _PBMSGLUCKINFOLISTNOTICE
DESCRIPTOR.message_types_by_name['PBLuckInfo'] = _PBLUCKINFO
DESCRIPTOR.message_types_by_name['PBDBLuckInfo'] = _PBDBLUCKINFO

class PBMsgMountLuck(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGMOUNTLUCK
  
  # @@protoc_insertion_point(class_scope:PBMsgMountLuck)

class PBLuckItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBLUCKITEM
  
  # @@protoc_insertion_point(class_scope:PBLuckItem)

class PBMsgMoutAllLuckRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGMOUTALLLUCKREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgMoutAllLuckRequest)

class PBMsgMountAllLuckResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGMOUNTALLLUCKRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgMountAllLuckResponse)

class PBMsgMountLuckUpdateRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGMOUNTLUCKUPDATEREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgMountLuckUpdateRequest)

class PBMsgMountLuckUpdateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGMOUNTLUCKUPDATERESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgMountLuckUpdateResponse)

class PBMsgLuckInfoNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGLUCKINFONOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgLuckInfoNotice)

class PBMsgLuckInfoListNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGLUCKINFOLISTNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgLuckInfoListNotice)

class PBLuckInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBLUCKINFO
  
  # @@protoc_insertion_point(class_scope:PBLuckInfo)

class PBDBLuckInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBDBLUCKINFO
  
  # @@protoc_insertion_point(class_scope:PBDBLuckInfo)

# @@protoc_insertion_point(module_scope)
