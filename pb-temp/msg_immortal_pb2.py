# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_item_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_immortal.proto',
  package='',
  serialized_pb='\n\x12msg_immortal.proto\x1a\x0emsg_item.proto\"\xac\x01\n\x13PBMsgImmortalMember\x12\x0b\n\x03mId\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\r\x12\x0b\n\x03job\x18\x04 \x01(\r\x12\x13\n\x0bhornourPoit\x18\x05 \x01(\x05\x12\r\n\x05title\x18\x06 \x01(\r\x12\x10\n\x08isOnline\x18\x07 \x01(\x08\x12\x12\n\ncapitalSum\x18\x08 \x01(\x05\x12\x14\n\x0coffline_time\x18\t \x01(\r\"V\n\x1cPBMsgImmortalMembersResponse\x12\x0b\n\x03mId\x18\x01 \x01(\x04\x12)\n\x0bmember_list\x18\x02 \x03(\x0b\x32\x14.PBMsgImmortalMember\"\x1d\n\x1bPBMsgImmortalMembersRequest\"\x96\x01\n\x16PBMsgItemOperateRecord\x12\x0f\n\x07op_type\x18\x01 \x01(\x05\x12\x0f\n\x07op_time\x18\x02 \x01(\r\x12\x0c\n\x04rank\x18\x03 \x01(\x05\x12\x15\n\roperator_name\x18\x04 \x01(\t\x12\x13\n\x0bmember_name\x18\x05 \x01(\t\x12 \n\x04item\x18\x06 \x03(\x0b\x32\x12.PBMsgItemQuantity\"J\n\x1aPBMsgItemOperateRecordList\x12,\n\x0brecord_list\x18\x01 \x03(\x0b\x32\x17.PBMsgItemOperateRecord\"e\n PBMsgImmortalStoreGiveOutRequest\x12\x0c\n\x04slot\x18\x01 \x01(\x05\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\x12\n\noperatorId\x18\x03 \x01(\x04\x12\x10\n\x08memberId\x18\x04 \x01(\x04\"5\n!PBMsgImmortalStoreGiveOutResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x05\">\n\x1aPBMsgImmortalStoreItemInfo\x12 \n\titem_list\x18\x01 \x03(\x0b\x32\r.PBMsgInvSlot')




_PBMSGIMMORTALMEMBER = descriptor.Descriptor(
  name='PBMsgImmortalMember',
  full_name='PBMsgImmortalMember',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mId', full_name='PBMsgImmortalMember.mId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='PBMsgImmortalMember.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='level', full_name='PBMsgImmortalMember.level', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='job', full_name='PBMsgImmortalMember.job', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hornourPoit', full_name='PBMsgImmortalMember.hornourPoit', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='title', full_name='PBMsgImmortalMember.title', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='isOnline', full_name='PBMsgImmortalMember.isOnline', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='capitalSum', full_name='PBMsgImmortalMember.capitalSum', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offline_time', full_name='PBMsgImmortalMember.offline_time', index=8,
      number=9, type=13, cpp_type=3, label=1,
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
  serialized_start=39,
  serialized_end=211,
)


_PBMSGIMMORTALMEMBERSRESPONSE = descriptor.Descriptor(
  name='PBMsgImmortalMembersResponse',
  full_name='PBMsgImmortalMembersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mId', full_name='PBMsgImmortalMembersResponse.mId', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='member_list', full_name='PBMsgImmortalMembersResponse.member_list', index=1,
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
  serialized_start=213,
  serialized_end=299,
)


_PBMSGIMMORTALMEMBERSREQUEST = descriptor.Descriptor(
  name='PBMsgImmortalMembersRequest',
  full_name='PBMsgImmortalMembersRequest',
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
  serialized_start=301,
  serialized_end=330,
)


_PBMSGITEMOPERATERECORD = descriptor.Descriptor(
  name='PBMsgItemOperateRecord',
  full_name='PBMsgItemOperateRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='op_type', full_name='PBMsgItemOperateRecord.op_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='op_time', full_name='PBMsgItemOperateRecord.op_time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rank', full_name='PBMsgItemOperateRecord.rank', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='operator_name', full_name='PBMsgItemOperateRecord.operator_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='member_name', full_name='PBMsgItemOperateRecord.member_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='PBMsgItemOperateRecord.item', index=5,
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
  serialized_start=333,
  serialized_end=483,
)


_PBMSGITEMOPERATERECORDLIST = descriptor.Descriptor(
  name='PBMsgItemOperateRecordList',
  full_name='PBMsgItemOperateRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='record_list', full_name='PBMsgItemOperateRecordList.record_list', index=0,
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
  serialized_start=485,
  serialized_end=559,
)


_PBMSGIMMORTALSTOREGIVEOUTREQUEST = descriptor.Descriptor(
  name='PBMsgImmortalStoreGiveOutRequest',
  full_name='PBMsgImmortalStoreGiveOutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='slot', full_name='PBMsgImmortalStoreGiveOutRequest.slot', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='count', full_name='PBMsgImmortalStoreGiveOutRequest.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='operatorId', full_name='PBMsgImmortalStoreGiveOutRequest.operatorId', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='memberId', full_name='PBMsgImmortalStoreGiveOutRequest.memberId', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_start=561,
  serialized_end=662,
)


_PBMSGIMMORTALSTOREGIVEOUTRESPONSE = descriptor.Descriptor(
  name='PBMsgImmortalStoreGiveOutResponse',
  full_name='PBMsgImmortalStoreGiveOutResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgImmortalStoreGiveOutResponse.ret_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=664,
  serialized_end=717,
)


_PBMSGIMMORTALSTOREITEMINFO = descriptor.Descriptor(
  name='PBMsgImmortalStoreItemInfo',
  full_name='PBMsgImmortalStoreItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='item_list', full_name='PBMsgImmortalStoreItemInfo.item_list', index=0,
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
  serialized_start=719,
  serialized_end=781,
)

_PBMSGIMMORTALMEMBERSRESPONSE.fields_by_name['member_list'].message_type = _PBMSGIMMORTALMEMBER
_PBMSGITEMOPERATERECORD.fields_by_name['item'].message_type = msg_item_pb2._PBMSGITEMQUANTITY
_PBMSGITEMOPERATERECORDLIST.fields_by_name['record_list'].message_type = _PBMSGITEMOPERATERECORD
_PBMSGIMMORTALSTOREITEMINFO.fields_by_name['item_list'].message_type = msg_item_pb2._PBMSGINVSLOT
DESCRIPTOR.message_types_by_name['PBMsgImmortalMember'] = _PBMSGIMMORTALMEMBER
DESCRIPTOR.message_types_by_name['PBMsgImmortalMembersResponse'] = _PBMSGIMMORTALMEMBERSRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgImmortalMembersRequest'] = _PBMSGIMMORTALMEMBERSREQUEST
DESCRIPTOR.message_types_by_name['PBMsgItemOperateRecord'] = _PBMSGITEMOPERATERECORD
DESCRIPTOR.message_types_by_name['PBMsgItemOperateRecordList'] = _PBMSGITEMOPERATERECORDLIST
DESCRIPTOR.message_types_by_name['PBMsgImmortalStoreGiveOutRequest'] = _PBMSGIMMORTALSTOREGIVEOUTREQUEST
DESCRIPTOR.message_types_by_name['PBMsgImmortalStoreGiveOutResponse'] = _PBMSGIMMORTALSTOREGIVEOUTRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgImmortalStoreItemInfo'] = _PBMSGIMMORTALSTOREITEMINFO

class PBMsgImmortalMember(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGIMMORTALMEMBER
  
  # @@protoc_insertion_point(class_scope:PBMsgImmortalMember)

class PBMsgImmortalMembersResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGIMMORTALMEMBERSRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgImmortalMembersResponse)

class PBMsgImmortalMembersRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGIMMORTALMEMBERSREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgImmortalMembersRequest)

class PBMsgItemOperateRecord(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGITEMOPERATERECORD
  
  # @@protoc_insertion_point(class_scope:PBMsgItemOperateRecord)

class PBMsgItemOperateRecordList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGITEMOPERATERECORDLIST
  
  # @@protoc_insertion_point(class_scope:PBMsgItemOperateRecordList)

class PBMsgImmortalStoreGiveOutRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGIMMORTALSTOREGIVEOUTREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgImmortalStoreGiveOutRequest)

class PBMsgImmortalStoreGiveOutResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGIMMORTALSTOREGIVEOUTRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgImmortalStoreGiveOutResponse)

class PBMsgImmortalStoreItemInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGIMMORTALSTOREITEMINFO
  
  # @@protoc_insertion_point(class_scope:PBMsgImmortalStoreItemInfo)

# @@protoc_insertion_point(module_scope)