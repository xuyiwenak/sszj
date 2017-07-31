# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import db_base_pb2
import player_pb2
import su_data_pb2
import billing_pb2
import gateway_pb2
import bigworld_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='message_set.proto',
  package='',
  serialized_pb='\n\x11message_set.proto\x1a\rdb_base.proto\x1a\x0cplayer.proto\x1a\rsu_data.proto\x1a\rbilling.proto\x1a\rgateway.proto\x1a\x0e\x62igworld.proto\"\xf1\x05\n\x0cPBMessageSet\x12\x19\n\x06\x64\x61ta_1\x18\x01 \x01(\x0b\x32\t.PBPlayer\x12\x1c\n\x06\x64\x61ta_2\x18\x02 \x01(\x0b\x32\x0c.PBCharacter\x12\x1e\n\x06\x64\x61ta_4\x18\x04 \x01(\x0b\x32\x0e.PBGateWayData\x12$\n\x06\x64\x61ta_5\x18\x05 \x01(\x0b\x32\x14.PBGateWaySocialData\x12 \n\x06\x64\x61ta_6\x18\x06 \x01(\x0b\x32\x10.PBBillingStatus\x12\x1f\n\x06\x64\x61ta_7\x18\x07 \x01(\x0b\x32\x0f.PBCashExchange\x12\x1f\n\x06\x64\x61ta_8\x18\x08 \x01(\x0b\x32\x0f.PBChargeRecord\x12\x1e\n\x06\x64\x61ta_9\x18\t \x01(\x0b\x32\x0e.PBAllGateData\x12 \n\x07\x64\x61ta_10\x18\n \x01(\x0b\x32\x0f.PBAddFreeMoney\x12\x1e\n\x07\x64\x61ta_11\x18\x0b \x01(\x0b\x32\r.PBChooseChar\x12\x1f\n\x07\x64\x61ta_12\x18\x0c \x01(\x0b\x32\x0e.PBConsignInfo\x12\x1e\n\x07\x64\x61ta_13\x18\r \x01(\x0b\x32\r.PBConsignLog\x12\x1f\n\x07\x64\x61ta_14\x18\x0e \x01(\x0b\x32\x0e.PBCharOffLine\x12!\n\x07\x64\x61ta_15\x18\x0f \x01(\x0b\x32\x10.PBGateWayDataEx\x12!\n\x07\x64\x61ta_16\x18\x10 \x01(\x0b\x32\x10.PBMarriageTable\x12#\n\x07\x64\x61ta_17\x18\x11 \x01(\x0b\x32\x12.PBGatWayGuildData\x12 \n\x07\x64\x61ta_18\x18\x12 \x01(\x0b\x32\x0f.PBRankLastData\x12!\n\x07\x64\x61ta_19\x18\x13 \x01(\x0b\x32\x10.PBGMSSpanBattle\x12!\n\x07\x64\x61ta_20\x18\x14 \x01(\x0b\x32\x10.PBSpanCurBattle\x12 \n\x07\x64\x61ta_21\x18\x15 \x01(\x0b\x32\x0f.PBSpanWildRank\x12!\n\x07\x64\x61ta_22\x18\x16 \x01(\x0b\x32\x10.PBGMSCommonData\x12\"\n\x07\x64\x61ta_23\x18\x17 \x01(\x0b\x32\x11.PBPetPvPRankDataB\x02H\x01')




_PBMESSAGESET = descriptor.Descriptor(
  name='PBMessageSet',
  full_name='PBMessageSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='data_1', full_name='PBMessageSet.data_1', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_2', full_name='PBMessageSet.data_2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_4', full_name='PBMessageSet.data_4', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_5', full_name='PBMessageSet.data_5', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_6', full_name='PBMessageSet.data_6', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_7', full_name='PBMessageSet.data_7', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_8', full_name='PBMessageSet.data_8', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_9', full_name='PBMessageSet.data_9', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_10', full_name='PBMessageSet.data_10', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_11', full_name='PBMessageSet.data_11', index=9,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_12', full_name='PBMessageSet.data_12', index=10,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_13', full_name='PBMessageSet.data_13', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_14', full_name='PBMessageSet.data_14', index=12,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_15', full_name='PBMessageSet.data_15', index=13,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_16', full_name='PBMessageSet.data_16', index=14,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_17', full_name='PBMessageSet.data_17', index=15,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_18', full_name='PBMessageSet.data_18', index=16,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_19', full_name='PBMessageSet.data_19', index=17,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_20', full_name='PBMessageSet.data_20', index=18,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_21', full_name='PBMessageSet.data_21', index=19,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_22', full_name='PBMessageSet.data_22', index=20,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data_23', full_name='PBMessageSet.data_23', index=21,
      number=23, type=11, cpp_type=10, label=1,
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
  serialized_start=112,
  serialized_end=865,
)

_PBMESSAGESET.fields_by_name['data_1'].message_type = player_pb2._PBPLAYER
_PBMESSAGESET.fields_by_name['data_2'].message_type = player_pb2._PBCHARACTER
_PBMESSAGESET.fields_by_name['data_4'].message_type = gateway_pb2._PBGATEWAYDATA
_PBMESSAGESET.fields_by_name['data_5'].message_type = gateway_pb2._PBGATEWAYSOCIALDATA
_PBMESSAGESET.fields_by_name['data_6'].message_type = billing_pb2._PBBILLINGSTATUS
_PBMESSAGESET.fields_by_name['data_7'].message_type = billing_pb2._PBCASHEXCHANGE
_PBMESSAGESET.fields_by_name['data_8'].message_type = billing_pb2._PBCHARGERECORD
_PBMESSAGESET.fields_by_name['data_9'].message_type = su_data_pb2._PBALLGATEDATA
_PBMESSAGESET.fields_by_name['data_10'].message_type = billing_pb2._PBADDFREEMONEY
_PBMESSAGESET.fields_by_name['data_11'].message_type = player_pb2._PBCHOOSECHAR
_PBMESSAGESET.fields_by_name['data_12'].message_type = player_pb2._PBCONSIGNINFO
_PBMESSAGESET.fields_by_name['data_13'].message_type = player_pb2._PBCONSIGNLOG
_PBMESSAGESET.fields_by_name['data_14'].message_type = gateway_pb2._PBCHAROFFLINE
_PBMESSAGESET.fields_by_name['data_15'].message_type = gateway_pb2._PBGATEWAYDATAEX
_PBMESSAGESET.fields_by_name['data_16'].message_type = gateway_pb2._PBMARRIAGETABLE
_PBMESSAGESET.fields_by_name['data_17'].message_type = gateway_pb2._PBGATWAYGUILDDATA
_PBMESSAGESET.fields_by_name['data_18'].message_type = gateway_pb2._PBRANKLASTDATA
_PBMESSAGESET.fields_by_name['data_19'].message_type = bigworld_pb2._PBGMSSPANBATTLE
_PBMESSAGESET.fields_by_name['data_20'].message_type = bigworld_pb2._PBSPANCURBATTLE
_PBMESSAGESET.fields_by_name['data_21'].message_type = bigworld_pb2._PBSPANWILDRANK
_PBMESSAGESET.fields_by_name['data_22'].message_type = bigworld_pb2._PBGMSCOMMONDATA
_PBMESSAGESET.fields_by_name['data_23'].message_type = gateway_pb2._PBPETPVPRANKDATA
DESCRIPTOR.message_types_by_name['PBMessageSet'] = _PBMESSAGESET

class PBMessageSet(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMESSAGESET
  
  # @@protoc_insertion_point(class_scope:PBMessageSet)

# @@protoc_insertion_point(module_scope)