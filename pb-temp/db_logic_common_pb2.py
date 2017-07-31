# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='db_logic_common.proto',
  package='',
  serialized_pb='\n\x15\x64\x62_logic_common.proto\"S\n\x0cPBAttachment\x12\x10\n\x08sheet_id\x18\x01 \x01(\r\x12\x10\n\x08quantity\x18\x02 \x01(\x11\x12\x0c\n\x04\x62ind\x18\x03 \x01(\x08\x12\x11\n\titem_desc\x18\x04 \x01(\t\"3\n\nPBKeyParam\x12\x12\n\nparam_type\x18\x01 \x01(\r\x12\x11\n\tparam_str\x18\x02 \x01(\t\"\xfe\x01\n\x06PBMail\x12\x0f\n\x07mail_id\x18\x01 \x01(\r\x12\x11\n\tsender_id\x18\x02 \x01(\r\x12\x13\n\x0bsender_name\x18\x03 \x01(\t\x12\r\n\x05title\x18\x04 \x01(\t\x12\x0c\n\x04\x62ody\x18\x05 \x01(\t\x12\x11\n\tsend_time\x18\x06 \x01(\r\x12!\n\nattachment\x18\x07 \x03(\x0b\x32\r.PBAttachment\x12\x0e\n\x06status\x18\x08 \x01(\r\x12\r\n\x05param\x18\t \x03(\t\x12\x10\n\x08\x64\x65l_time\x18\n \x01(\r\x12\x1e\n\tkey_param\x18\x0b \x03(\x0b\x32\x0b.PBKeyParam\x12\x17\n\x0f\x65xpiration_time\x18\x0c \x01(\r\"L\n\x0ePBIULeaderInfo\x12\x13\n\x0bleader_name\x18\x01 \x01(\t\x12\x0b\n\x03vpa\x18\x02 \x01(\x04\x12\x0b\n\x03vpb\x18\x03 \x01(\x04\x12\x0b\n\x03vpc\x18\x04 \x01(\x04\"\xbb\x01\n\x08PBRankIU\x12\x0f\n\x07iu_rank\x18\x01 \x01(\x11\x12\r\n\x05iu_id\x18\x02 \x01(\x04\x12\x0f\n\x07iu_name\x18\x03 \x01(\t\x12\x10\n\x08iu_level\x18\x04 \x01(\x11\x12\x14\n\x0c\x62\x61ttle_score\x18\x05 \x01(\x11\x12\x12\n\ngateway_id\x18\x06 \x01(\r\x12\x1c\n\x14received_leader_info\x18\x07 \x01(\x08\x12$\n\x0bleader_info\x18\x08 \x01(\x0b\x32\x0f.PBIULeaderInfoB\x02H\x01')




_PBATTACHMENT = descriptor.Descriptor(
  name='PBAttachment',
  full_name='PBAttachment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sheet_id', full_name='PBAttachment.sheet_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='quantity', full_name='PBAttachment.quantity', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='bind', full_name='PBAttachment.bind', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item_desc', full_name='PBAttachment.item_desc', index=3,
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
  serialized_start=25,
  serialized_end=108,
)


_PBKEYPARAM = descriptor.Descriptor(
  name='PBKeyParam',
  full_name='PBKeyParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='param_type', full_name='PBKeyParam.param_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='param_str', full_name='PBKeyParam.param_str', index=1,
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
  serialized_start=110,
  serialized_end=161,
)


_PBMAIL = descriptor.Descriptor(
  name='PBMail',
  full_name='PBMail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='mail_id', full_name='PBMail.mail_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sender_id', full_name='PBMail.sender_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sender_name', full_name='PBMail.sender_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='title', full_name='PBMail.title', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='body', full_name='PBMail.body', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='send_time', full_name='PBMail.send_time', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attachment', full_name='PBMail.attachment', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='status', full_name='PBMail.status', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='param', full_name='PBMail.param', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='del_time', full_name='PBMail.del_time', index=9,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key_param', full_name='PBMail.key_param', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='expiration_time', full_name='PBMail.expiration_time', index=11,
      number=12, type=13, cpp_type=3, label=1,
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
  serialized_start=164,
  serialized_end=418,
)


_PBIULEADERINFO = descriptor.Descriptor(
  name='PBIULeaderInfo',
  full_name='PBIULeaderInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='leader_name', full_name='PBIULeaderInfo.leader_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vpa', full_name='PBIULeaderInfo.vpa', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vpb', full_name='PBIULeaderInfo.vpb', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vpc', full_name='PBIULeaderInfo.vpc', index=3,
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
  serialized_start=420,
  serialized_end=496,
)


_PBRANKIU = descriptor.Descriptor(
  name='PBRankIU',
  full_name='PBRankIU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='iu_rank', full_name='PBRankIU.iu_rank', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='iu_id', full_name='PBRankIU.iu_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='iu_name', full_name='PBRankIU.iu_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='iu_level', full_name='PBRankIU.iu_level', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='battle_score', full_name='PBRankIU.battle_score', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gateway_id', full_name='PBRankIU.gateway_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='received_leader_info', full_name='PBRankIU.received_leader_info', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='leader_info', full_name='PBRankIU.leader_info', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=499,
  serialized_end=686,
)

_PBMAIL.fields_by_name['attachment'].message_type = _PBATTACHMENT
_PBMAIL.fields_by_name['key_param'].message_type = _PBKEYPARAM
_PBRANKIU.fields_by_name['leader_info'].message_type = _PBIULEADERINFO
DESCRIPTOR.message_types_by_name['PBAttachment'] = _PBATTACHMENT
DESCRIPTOR.message_types_by_name['PBKeyParam'] = _PBKEYPARAM
DESCRIPTOR.message_types_by_name['PBMail'] = _PBMAIL
DESCRIPTOR.message_types_by_name['PBIULeaderInfo'] = _PBIULEADERINFO
DESCRIPTOR.message_types_by_name['PBRankIU'] = _PBRANKIU

class PBAttachment(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBATTACHMENT
  
  # @@protoc_insertion_point(class_scope:PBAttachment)

class PBKeyParam(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBKEYPARAM
  
  # @@protoc_insertion_point(class_scope:PBKeyParam)

class PBMail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMAIL
  
  # @@protoc_insertion_point(class_scope:PBMail)

class PBIULeaderInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBIULEADERINFO
  
  # @@protoc_insertion_point(class_scope:PBIULeaderInfo)

class PBRankIU(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRANKIU
  
  # @@protoc_insertion_point(class_scope:PBRankIU)

# @@protoc_insertion_point(module_scope)
