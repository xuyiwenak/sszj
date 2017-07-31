# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2
import msg_common_pb2
import msg_login_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_robot.proto',
  package='',
  serialized_pb='\n\x10tmpl_robot.proto\x1a\x0ftmpl_base.proto\x1a\x10msg_common.proto\x1a\x0fmsg_login.proto\"]\n\rPBConfigRobot\x12\'\n\x0clogin_config\x18\x01 \x01(\x0b\x32\x11.PBRobotLoginAddr\x12#\n\x06\x64\x65vice\x18\x02 \x01(\x0b\x32\x13.PBClientDeviceInfo\"\xbf\x02\n\x10PBRobotLoginAddr\x12\x15\n\rgenerate_addr\x18\x01 \x01(\t\x12\x15\n\rregister_addr\x18\x02 \x01(\t\x12\x12\n\nlogin_addr\x18\x03 \x01(\t\x12\x12\n\ngateway_id\x18\x04 \x01(\r\x12\x0f\n\x07game_id\x18\x05 \x01(\r\x12\x10\n\x08language\x18\x06 \x01(\t\x12\x18\n\x10\x63reate_char_addr\x18\x07 \x01(\t\x12\x17\n\x0f\x65nter_game_addr\x18\x08 \x01(\t\x12\x18\n\x10\x64\x65lete_char_addr\x18\t \x01(\t\x12\x18\n\x10random_name_addr\x18\n \x01(\t\x12\x11\n\trole_type\x18\x0b \x01(\r\x12\x11\n\tcamp_type\x18\x0c \x01(\r\x12\x0b\n\x03vpa\x18\r \x01(\t\x12\x0b\n\x03vpb\x18\x0e \x01(\t\x12\x0b\n\x03vpc\x18\x0f \x01(\t\"t\n\x0fPBRobotsFactory\x12\x16\n\x0elogin_interval\x18\x01 \x01(\x02\x12\x13\n\x0blogin_count\x18\x02 \x01(\x05\x12 \n\x07\x61\x63\x63ount\x18\x03 \x03(\x0b\x32\x0f.PBRobotAccount\x12\x12\n\nlogin_from\x18\x04 \x01(\x05\"F\n\x0ePBRobotAccount\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0f\n\x07\x65ncoded\x18\x03 \x01(\t\"L\n\x0ePBRyMsgName2Id\x12\x1e\n\x06\x62ranch\x18\x01 \x03(\x0b\x32\x0e.PBRyMsgBranch\x12\x1a\n\x04leaf\x18\x02 \x03(\x0b\x32\x0c.PBRyMsgLeaf\"E\n\rPBRyMsgBranch\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12\x1a\n\x04leaf\x18\x03 \x03(\x0b\x32\x0c.PBRyMsgLeaf\"7\n\x0bPBRyMsgLeaf\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06sendto\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\r\"=\n\x14PBRobotSendingRecord\x12%\n\x06packet\x18\x01 \x03(\x0b\x32\x15.PBRobotSendingPacket\"B\n\x14PBRobotSendingPacket\x12\x14\n\x0csending_time\x18\x01 \x01(\x02\x12\x14\n\x0csending_data\x18\x02 \x01(\x0c')




_PBCONFIGROBOT = descriptor.Descriptor(
  name='PBConfigRobot',
  full_name='PBConfigRobot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='login_config', full_name='PBConfigRobot.login_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='device', full_name='PBConfigRobot.device', index=1,
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
  serialized_start=72,
  serialized_end=165,
)


_PBROBOTLOGINADDR = descriptor.Descriptor(
  name='PBRobotLoginAddr',
  full_name='PBRobotLoginAddr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='generate_addr', full_name='PBRobotLoginAddr.generate_addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='register_addr', full_name='PBRobotLoginAddr.register_addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='login_addr', full_name='PBRobotLoginAddr.login_addr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='gateway_id', full_name='PBRobotLoginAddr.gateway_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='game_id', full_name='PBRobotLoginAddr.game_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='language', full_name='PBRobotLoginAddr.language', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='create_char_addr', full_name='PBRobotLoginAddr.create_char_addr', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='enter_game_addr', full_name='PBRobotLoginAddr.enter_game_addr', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='delete_char_addr', full_name='PBRobotLoginAddr.delete_char_addr', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='random_name_addr', full_name='PBRobotLoginAddr.random_name_addr', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role_type', full_name='PBRobotLoginAddr.role_type', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='camp_type', full_name='PBRobotLoginAddr.camp_type', index=11,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vpa', full_name='PBRobotLoginAddr.vpa', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vpb', full_name='PBRobotLoginAddr.vpb', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='vpc', full_name='PBRobotLoginAddr.vpc', index=14,
      number=15, type=9, cpp_type=9, label=1,
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
  serialized_start=168,
  serialized_end=487,
)


_PBROBOTSFACTORY = descriptor.Descriptor(
  name='PBRobotsFactory',
  full_name='PBRobotsFactory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='login_interval', full_name='PBRobotsFactory.login_interval', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='login_count', full_name='PBRobotsFactory.login_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='account', full_name='PBRobotsFactory.account', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='login_from', full_name='PBRobotsFactory.login_from', index=3,
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
  serialized_start=489,
  serialized_end=605,
)


_PBROBOTACCOUNT = descriptor.Descriptor(
  name='PBRobotAccount',
  full_name='PBRobotAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='user_name', full_name='PBRobotAccount.user_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='password', full_name='PBRobotAccount.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='encoded', full_name='PBRobotAccount.encoded', index=2,
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
  serialized_start=607,
  serialized_end=677,
)


_PBRYMSGNAME2ID = descriptor.Descriptor(
  name='PBRyMsgName2Id',
  full_name='PBRyMsgName2Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='branch', full_name='PBRyMsgName2Id.branch', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='leaf', full_name='PBRyMsgName2Id.leaf', index=1,
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
  serialized_start=679,
  serialized_end=755,
)


_PBRYMSGBRANCH = descriptor.Descriptor(
  name='PBRyMsgBranch',
  full_name='PBRyMsgBranch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBRyMsgBranch.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='PBRyMsgBranch.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='leaf', full_name='PBRyMsgBranch.leaf', index=2,
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
  serialized_start=757,
  serialized_end=826,
)


_PBRYMSGLEAF = descriptor.Descriptor(
  name='PBRyMsgLeaf',
  full_name='PBRyMsgLeaf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBRyMsgLeaf.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sendto', full_name='PBRyMsgLeaf.sendto', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='id', full_name='PBRyMsgLeaf.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=828,
  serialized_end=883,
)


_PBROBOTSENDINGRECORD = descriptor.Descriptor(
  name='PBRobotSendingRecord',
  full_name='PBRobotSendingRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='packet', full_name='PBRobotSendingRecord.packet', index=0,
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
  serialized_start=885,
  serialized_end=946,
)


_PBROBOTSENDINGPACKET = descriptor.Descriptor(
  name='PBRobotSendingPacket',
  full_name='PBRobotSendingPacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='sending_time', full_name='PBRobotSendingPacket.sending_time', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sending_data', full_name='PBRobotSendingPacket.sending_data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
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
  serialized_start=948,
  serialized_end=1014,
)

_PBCONFIGROBOT.fields_by_name['login_config'].message_type = _PBROBOTLOGINADDR
_PBCONFIGROBOT.fields_by_name['device'].message_type = msg_login_pb2._PBCLIENTDEVICEINFO
_PBROBOTSFACTORY.fields_by_name['account'].message_type = _PBROBOTACCOUNT
_PBRYMSGNAME2ID.fields_by_name['branch'].message_type = _PBRYMSGBRANCH
_PBRYMSGNAME2ID.fields_by_name['leaf'].message_type = _PBRYMSGLEAF
_PBRYMSGBRANCH.fields_by_name['leaf'].message_type = _PBRYMSGLEAF
_PBROBOTSENDINGRECORD.fields_by_name['packet'].message_type = _PBROBOTSENDINGPACKET
DESCRIPTOR.message_types_by_name['PBConfigRobot'] = _PBCONFIGROBOT
DESCRIPTOR.message_types_by_name['PBRobotLoginAddr'] = _PBROBOTLOGINADDR
DESCRIPTOR.message_types_by_name['PBRobotsFactory'] = _PBROBOTSFACTORY
DESCRIPTOR.message_types_by_name['PBRobotAccount'] = _PBROBOTACCOUNT
DESCRIPTOR.message_types_by_name['PBRyMsgName2Id'] = _PBRYMSGNAME2ID
DESCRIPTOR.message_types_by_name['PBRyMsgBranch'] = _PBRYMSGBRANCH
DESCRIPTOR.message_types_by_name['PBRyMsgLeaf'] = _PBRYMSGLEAF
DESCRIPTOR.message_types_by_name['PBRobotSendingRecord'] = _PBROBOTSENDINGRECORD
DESCRIPTOR.message_types_by_name['PBRobotSendingPacket'] = _PBROBOTSENDINGPACKET

class PBConfigRobot(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBCONFIGROBOT
  
  # @@protoc_insertion_point(class_scope:PBConfigRobot)

class PBRobotLoginAddr(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBROBOTLOGINADDR
  
  # @@protoc_insertion_point(class_scope:PBRobotLoginAddr)

class PBRobotsFactory(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBROBOTSFACTORY
  
  # @@protoc_insertion_point(class_scope:PBRobotsFactory)

class PBRobotAccount(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBROBOTACCOUNT
  
  # @@protoc_insertion_point(class_scope:PBRobotAccount)

class PBRyMsgName2Id(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRYMSGNAME2ID
  
  # @@protoc_insertion_point(class_scope:PBRyMsgName2Id)

class PBRyMsgBranch(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRYMSGBRANCH
  
  # @@protoc_insertion_point(class_scope:PBRyMsgBranch)

class PBRyMsgLeaf(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBRYMSGLEAF
  
  # @@protoc_insertion_point(class_scope:PBRyMsgLeaf)

class PBRobotSendingRecord(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBROBOTSENDINGRECORD
  
  # @@protoc_insertion_point(class_scope:PBRobotSendingRecord)

class PBRobotSendingPacket(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBROBOTSENDINGPACKET
  
  # @@protoc_insertion_point(class_scope:PBRobotSendingPacket)

# @@protoc_insertion_point(module_scope)
