# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_db.proto',
  package='',
  serialized_pb='\n\x0cmsg_db.proto\"\x16\n\x07PBDBSql\x12\x0b\n\x03sql\x18\x01 \x01(\t\"\xc3\x01\n\x0ePBDBCreateRole\x12\x0f\n\x07\x63har_id\x18\x01 \x01(\x03\x12\x11\n\tplayer_id\x18\x02 \x01(\x03\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\x12\x0c\n\x04role\x18\x04 \x01(\x05\x12\x11\n\trole_name\x18\x05 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\x06 \x01(\r\x12\x10\n\x08op_state\x18\x07 \x01(\x05\x12\x0f\n\x07\x63\x61mp_id\x18\x08 \x01(\x05\x12\x12\n\ngateway_id\x18\t \x01(\x05\x12\x0f\n\x07user_id\x18\n \x01(\x05\"W\n\nPBDBResult\x12\x11\n\trow_count\x18\x01 \x01(\x05\x12\x11\n\tlow_count\x18\x02 \x01(\x05\x12\r\n\x05value\x18\x03 \x03(\t\x12\x14\n\x0cvalue_length\x18\x04 \x03(\x05\"f\n\x0fPBConsignModify\x12\x12\n\nconsign_id\x18\x01 \x01(\x04\x12\x14\n\x0c\x63onsign_flag\x18\x02 \x01(\x05\x12\x13\n\x0b\x62uy_role_id\x18\x03 \x01(\x05\x12\x14\n\x0c\x62uy_owner_id\x18\x04 \x01(\x05\"\"\n\x0cPBConsignDel\x12\x12\n\nconsign_id\x18\x01 \x01(\x04\"+\n\tPBExecSql\x12\x11\n\texec_type\x18\x01 \x01(\x05\x12\x0b\n\x03sql\x18\x02 \x01(\t\"`\n\x13PBConsignHotItemSql\x12\x10\n\x08opt_type\x18\x01 \x01(\x11\x12\x10\n\x08sheet_id\x18\x02 \x01(\x11\x12\x11\n\tbuy_times\x18\x03 \x01(\x11\x12\x12\n\nsheet_name\x18\x04 \x01(\t*\xd0\x01\n\teExecType\x12\r\n\tEXEC_NONE\x10\x00\x12\x0e\n\nEXEC_QUERY\x10\x01\x12\r\n\tEXEC_SAVE\x10\x02\x12\x0c\n\x08\x45XEC_SQL\x10\x03\x12\x14\n\x10\x45XEC_CREATE_ROLE\x10\x04\x12\x0f\n\x0b\x45XEC_UPDATE\x10\x05\x12\x17\n\x13\x45XEC_CONSIGN_INSERT\x10\x06\x12\x17\n\x13\x45XEC_CONSIGN_MODIFY\x10\x07\x12\x14\n\x10\x45XEC_CONSIGN_DEL\x10\x08\x12\x18\n\x14\x45XEC_CONSIGN_HOT_SQL\x10\t*G\n\rPBConsignOper\x12\x10\n\x0c\x43ONSIGN_NONE\x10\x00\x12\x10\n\x0c\x43ONSIGN_SALE\x10\x01\x12\x12\n\x0e\x43ONSIGN_REVOKE\x10\x02*@\n\x10PBConsignHotOper\x12\x15\n\x11\x43ONSIGNHOT_INSERT\x10\x01\x12\x15\n\x11\x43ONSIGNHOT_UPDATE\x10\x02\x42\x02H\x01')

_EEXECTYPE = descriptor.EnumDescriptor(
  name='eExecType',
  full_name='eExecType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='EXEC_NONE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_QUERY', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_SAVE', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_SQL', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_CREATE_ROLE', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_UPDATE', index=5, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_CONSIGN_INSERT', index=6, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_CONSIGN_MODIFY', index=7, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_CONSIGN_DEL', index=8, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EXEC_CONSIGN_HOT_SQL', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=611,
  serialized_end=819,
)


_PBCONSIGNOPER = descriptor.EnumDescriptor(
  name='PBConsignOper',
  full_name='PBConsignOper',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CONSIGN_NONE', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CONSIGN_SALE', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CONSIGN_REVOKE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=821,
  serialized_end=892,
)


_PBCONSIGNHOTOPER = descriptor.EnumDescriptor(
  name='PBConsignHotOper',
  full_name='PBConsignHotOper',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='CONSIGNHOT_INSERT', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CONSIGNHOT_UPDATE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=894,
  serialized_end=958,
)


EXEC_NONE = 0
EXEC_QUERY = 1
EXEC_SAVE = 2
EXEC_SQL = 3
EXEC_CREATE_ROLE = 4
EXEC_UPDATE = 5
EXEC_CONSIGN_INSERT = 6
EXEC_CONSIGN_MODIFY = 7
EXEC_CONSIGN_DEL = 8
EXEC_CONSIGN_HOT_SQL = 9
CONSIGN_NONE = 0
CONSIGN_SALE = 1
CONSIGN_REVOKE = 2
CONSIGNHOT_INSERT = 1
CONSIGNHOT_UPDATE = 2



_PBDBSQL = descriptor.Descriptor(
  name='PBDBSql',
  full_name='PBDBSql',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sql', full_name='PBDBSql.sql', index=0,
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
  serialized_start=16,
  serialized_end=38,
)


_PBDBCREATEROLE = descriptor.Descriptor(
  name='PBDBCreateRole',
  full_name='PBDBCreateRole',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBDBCreateRole.char_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='player_id', full_name='PBDBCreateRole.player_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role_id', full_name='PBDBCreateRole.role_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role', full_name='PBDBCreateRole.role', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role_name', full_name='PBDBCreateRole.role_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='create_time', full_name='PBDBCreateRole.create_time', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='op_state', full_name='PBDBCreateRole.op_state', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='camp_id', full_name='PBDBCreateRole.camp_id', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gateway_id', full_name='PBDBCreateRole.gateway_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_id', full_name='PBDBCreateRole.user_id', index=9,
      number=10, type=5, cpp_type=1, label=1,
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
  serialized_start=41,
  serialized_end=236,
)


_PBDBRESULT = descriptor.Descriptor(
  name='PBDBResult',
  full_name='PBDBResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='row_count', full_name='PBDBResult.row_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='low_count', full_name='PBDBResult.low_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='PBDBResult.value', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value_length', full_name='PBDBResult.value_length', index=3,
      number=4, type=5, cpp_type=1, label=3,
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
  serialized_start=238,
  serialized_end=325,
)


_PBCONSIGNMODIFY = descriptor.Descriptor(
  name='PBConsignModify',
  full_name='PBConsignModify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='consign_id', full_name='PBConsignModify.consign_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='consign_flag', full_name='PBConsignModify.consign_flag', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buy_role_id', full_name='PBConsignModify.buy_role_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buy_owner_id', full_name='PBConsignModify.buy_owner_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=327,
  serialized_end=429,
)


_PBCONSIGNDEL = descriptor.Descriptor(
  name='PBConsignDel',
  full_name='PBConsignDel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='consign_id', full_name='PBConsignDel.consign_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=431,
  serialized_end=465,
)


_PBEXECSQL = descriptor.Descriptor(
  name='PBExecSql',
  full_name='PBExecSql',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='exec_type', full_name='PBExecSql.exec_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sql', full_name='PBExecSql.sql', index=1,
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
  serialized_end=510,
)


_PBCONSIGNHOTITEMSQL = descriptor.Descriptor(
  name='PBConsignHotItemSql',
  full_name='PBConsignHotItemSql',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='opt_type', full_name='PBConsignHotItemSql.opt_type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sheet_id', full_name='PBConsignHotItemSql.sheet_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='buy_times', full_name='PBConsignHotItemSql.buy_times', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sheet_name', full_name='PBConsignHotItemSql.sheet_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=512,
  serialized_end=608,
)

DESCRIPTOR.message_types_by_name['PBDBSql'] = _PBDBSQL
DESCRIPTOR.message_types_by_name['PBDBCreateRole'] = _PBDBCREATEROLE
DESCRIPTOR.message_types_by_name['PBDBResult'] = _PBDBRESULT
DESCRIPTOR.message_types_by_name['PBConsignModify'] = _PBCONSIGNMODIFY
DESCRIPTOR.message_types_by_name['PBConsignDel'] = _PBCONSIGNDEL
DESCRIPTOR.message_types_by_name['PBExecSql'] = _PBEXECSQL
DESCRIPTOR.message_types_by_name['PBConsignHotItemSql'] = _PBCONSIGNHOTITEMSQL

class PBDBSql(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBDBSQL
  
  # @@protoc_insertion_point(class_scope:PBDBSql)

class PBDBCreateRole(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBDBCREATEROLE
  
  # @@protoc_insertion_point(class_scope:PBDBCreateRole)

class PBDBResult(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBDBRESULT
  
  # @@protoc_insertion_point(class_scope:PBDBResult)

class PBConsignModify(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONSIGNMODIFY
  
  # @@protoc_insertion_point(class_scope:PBConsignModify)

class PBConsignDel(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONSIGNDEL
  
  # @@protoc_insertion_point(class_scope:PBConsignDel)

class PBExecSql(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBEXECSQL
  
  # @@protoc_insertion_point(class_scope:PBExecSql)

class PBConsignHotItemSql(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONSIGNHOTITEMSQL
  
  # @@protoc_insertion_point(class_scope:PBConsignHotItemSql)

# @@protoc_insertion_point(module_scope)