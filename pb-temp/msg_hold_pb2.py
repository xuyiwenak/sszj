# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_hold.proto',
  package='',
  serialized_pb='\n\x0emsg_hold.proto\x1a\x0emsg_base.proto\"#\n\x10PBMsgHoldRequest\x12\x0f\n\x07\x63har_id\x18\x01 \x01(\x04\"6\n\x11PBMsgHoldResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x0f\n\x07\x63har_id\x18\x02 \x01(\x04\"8\n\x12PBMsgHoldAckNotice\x12\x0f\n\x07\x63har_id\x18\x01 \x01(\x04\x12\x11\n\tchar_name\x18\x02 \x01(\t\"8\n\x13PBMsgHoldAckRequest\x12\x10\n\x08is_agree\x18\x01 \x01(\x08\x12\x0f\n\x07\x63har_id\x18\x02 \x01(\x04\"M\n\x14PBMsgHoldAckResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x12\n\nhold_state\x18\x02 \x01(\x11\x12\x0f\n\x07\x63har_id\x18\x03 \x01(\x04\"9\n\x14PBMsgHoldDownRequest\x12!\n\tdown_type\x18\x01 \x01(\x0e\x32\x0e.EHoldDownType\")\n\x15PBMsgHoldDownResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\"=\n\x18PBMsgHoldInterruptNotice\x12\x0f\n\x07\x63har_id\x18\x01 \x01(\x04\x12\x10\n\x08is_block\x18\x02 \x01(\x08\",\n\x19PBMsgHoldDelAppListNotice\x12\x0f\n\x07\x63har_id\x18\x01 \x01(\x04\"B\n\x1aPBMsgHoldAutoShieldRequest\x12\x11\n\tis_shield\x18\x01 \x01(\x08\x12\x11\n\tis_action\x18\x02 \x01(\x08\"U\n\x1bPBMsgHoldAutoShieldResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x11\n\tis_shield\x18\x02 \x01(\x08\x12\x11\n\tis_action\x18\x03 \x01(\x08\"A\n\x19PBMsgHoldAutoShieldNotice\x12\x11\n\tis_shield\x18\x01 \x01(\x08\x12\x11\n\tis_action\x18\x02 \x01(\x08\"B\n\x17PBMsgInterActionRequest\x12\x11\n\taction_id\x18\x01 \x01(\x11\x12\x14\n\x0ctar_entityID\x18\x02 \x01(\x04\"?\n\x19PBMsgInterActionRequestEx\x12\x11\n\taction_id\x18\x01 \x01(\x11\x12\x0f\n\x07\x63har_id\x18\x02 \x01(\x04\"k\n\x18PBMsgInterActionResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x11\n\taction_id\x18\x02 \x01(\x11\x12\x14\n\x0csrc_entityID\x18\x03 \x01(\x04\x12\x14\n\x0ctar_entityID\x18\x04 \x01(\x04\"W\n\x16PBMsgInterActionNotice\x12\x11\n\taction_id\x18\x01 \x01(\x11\x12\x14\n\x0csrc_entityID\x18\x02 \x01(\x04\x12\x14\n\x0ctar_entityID\x18\x03 \x01(\x04\"\x1f\n\x1dPBMsgCancelInterActionRequest\"2\n\x1ePBMsgCancelInterActionResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\"B\n\x1cPBMsgInterActionVerifyNotice\x12\x11\n\trole_name\x18\x01 \x01(\t\x12\x0f\n\x07role_id\x18\x02 \x01(\r\"T\n\x1dPBMsgInterActionVerifyRequest\x12\x0f\n\x07role_id\x18\x01 \x01(\r\x12\"\n\x04type\x18\x02 \x01(\x0e\x32\x14.PBInterActionVerify\"2\n\x1ePBMsgInterActionVerifyResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11*+\n\rEHoldDownType\x12\x0c\n\x08\x45HT_DROP\x10\x01\x12\x0c\n\x08\x45HT_DOWN\x10\x02*:\n\x13PBInterActionVerify\x12\x10\n\x0cVerify_Agree\x10\x01\x12\x11\n\rVerify_Reject\x10\x02\x42\x02H\x01')

_EHOLDDOWNTYPE = descriptor.EnumDescriptor(
  name='EHoldDownType',
  full_name='EHoldDownType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='EHT_DROP', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='EHT_DOWN', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1377,
  serialized_end=1420,
)


_PBINTERACTIONVERIFY = descriptor.EnumDescriptor(
  name='PBInterActionVerify',
  full_name='PBInterActionVerify',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='Verify_Agree', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Verify_Reject', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1422,
  serialized_end=1480,
)


EHT_DROP = 1
EHT_DOWN = 2
Verify_Agree = 1
Verify_Reject = 2



_PBMSGHOLDREQUEST = descriptor.Descriptor(
  name='PBMsgHoldRequest',
  full_name='PBMsgHoldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBMsgHoldRequest.char_id', index=0,
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
  serialized_start=34,
  serialized_end=69,
)


_PBMSGHOLDRESPONSE = descriptor.Descriptor(
  name='PBMsgHoldResponse',
  full_name='PBMsgHoldResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgHoldResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBMsgHoldResponse.char_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=71,
  serialized_end=125,
)


_PBMSGHOLDACKNOTICE = descriptor.Descriptor(
  name='PBMsgHoldAckNotice',
  full_name='PBMsgHoldAckNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBMsgHoldAckNotice.char_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_name', full_name='PBMsgHoldAckNotice.char_name', index=1,
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
  serialized_start=127,
  serialized_end=183,
)


_PBMSGHOLDACKREQUEST = descriptor.Descriptor(
  name='PBMsgHoldAckRequest',
  full_name='PBMsgHoldAckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='is_agree', full_name='PBMsgHoldAckRequest.is_agree', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBMsgHoldAckRequest.char_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=185,
  serialized_end=241,
)


_PBMSGHOLDACKRESPONSE = descriptor.Descriptor(
  name='PBMsgHoldAckResponse',
  full_name='PBMsgHoldAckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgHoldAckResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hold_state', full_name='PBMsgHoldAckResponse.hold_state', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBMsgHoldAckResponse.char_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=243,
  serialized_end=320,
)


_PBMSGHOLDDOWNREQUEST = descriptor.Descriptor(
  name='PBMsgHoldDownRequest',
  full_name='PBMsgHoldDownRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='down_type', full_name='PBMsgHoldDownRequest.down_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=322,
  serialized_end=379,
)


_PBMSGHOLDDOWNRESPONSE = descriptor.Descriptor(
  name='PBMsgHoldDownResponse',
  full_name='PBMsgHoldDownResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgHoldDownResponse.ret_code', index=0,
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
  serialized_start=381,
  serialized_end=422,
)


_PBMSGHOLDINTERRUPTNOTICE = descriptor.Descriptor(
  name='PBMsgHoldInterruptNotice',
  full_name='PBMsgHoldInterruptNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBMsgHoldInterruptNotice.char_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_block', full_name='PBMsgHoldInterruptNotice.is_block', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=424,
  serialized_end=485,
)


_PBMSGHOLDDELAPPLISTNOTICE = descriptor.Descriptor(
  name='PBMsgHoldDelAppListNotice',
  full_name='PBMsgHoldDelAppListNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBMsgHoldDelAppListNotice.char_id', index=0,
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
  serialized_start=487,
  serialized_end=531,
)


_PBMSGHOLDAUTOSHIELDREQUEST = descriptor.Descriptor(
  name='PBMsgHoldAutoShieldRequest',
  full_name='PBMsgHoldAutoShieldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='is_shield', full_name='PBMsgHoldAutoShieldRequest.is_shield', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_action', full_name='PBMsgHoldAutoShieldRequest.is_action', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=533,
  serialized_end=599,
)


_PBMSGHOLDAUTOSHIELDRESPONSE = descriptor.Descriptor(
  name='PBMsgHoldAutoShieldResponse',
  full_name='PBMsgHoldAutoShieldResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgHoldAutoShieldResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_shield', full_name='PBMsgHoldAutoShieldResponse.is_shield', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_action', full_name='PBMsgHoldAutoShieldResponse.is_action', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=601,
  serialized_end=686,
)


_PBMSGHOLDAUTOSHIELDNOTICE = descriptor.Descriptor(
  name='PBMsgHoldAutoShieldNotice',
  full_name='PBMsgHoldAutoShieldNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='is_shield', full_name='PBMsgHoldAutoShieldNotice.is_shield', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_action', full_name='PBMsgHoldAutoShieldNotice.is_action', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=688,
  serialized_end=753,
)


_PBMSGINTERACTIONREQUEST = descriptor.Descriptor(
  name='PBMsgInterActionRequest',
  full_name='PBMsgInterActionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='action_id', full_name='PBMsgInterActionRequest.action_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tar_entityID', full_name='PBMsgInterActionRequest.tar_entityID', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=755,
  serialized_end=821,
)


_PBMSGINTERACTIONREQUESTEX = descriptor.Descriptor(
  name='PBMsgInterActionRequestEx',
  full_name='PBMsgInterActionRequestEx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='action_id', full_name='PBMsgInterActionRequestEx.action_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='char_id', full_name='PBMsgInterActionRequestEx.char_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=823,
  serialized_end=886,
)


_PBMSGINTERACTIONRESPONSE = descriptor.Descriptor(
  name='PBMsgInterActionResponse',
  full_name='PBMsgInterActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgInterActionResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='action_id', full_name='PBMsgInterActionResponse.action_id', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='src_entityID', full_name='PBMsgInterActionResponse.src_entityID', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tar_entityID', full_name='PBMsgInterActionResponse.tar_entityID', index=3,
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
  serialized_start=888,
  serialized_end=995,
)


_PBMSGINTERACTIONNOTICE = descriptor.Descriptor(
  name='PBMsgInterActionNotice',
  full_name='PBMsgInterActionNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='action_id', full_name='PBMsgInterActionNotice.action_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='src_entityID', full_name='PBMsgInterActionNotice.src_entityID', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tar_entityID', full_name='PBMsgInterActionNotice.tar_entityID', index=2,
      number=3, type=4, cpp_type=4, label=1,
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
  serialized_start=997,
  serialized_end=1084,
)


_PBMSGCANCELINTERACTIONREQUEST = descriptor.Descriptor(
  name='PBMsgCancelInterActionRequest',
  full_name='PBMsgCancelInterActionRequest',
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
  serialized_start=1086,
  serialized_end=1117,
)


_PBMSGCANCELINTERACTIONRESPONSE = descriptor.Descriptor(
  name='PBMsgCancelInterActionResponse',
  full_name='PBMsgCancelInterActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgCancelInterActionResponse.ret_code', index=0,
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
  serialized_start=1119,
  serialized_end=1169,
)


_PBMSGINTERACTIONVERIFYNOTICE = descriptor.Descriptor(
  name='PBMsgInterActionVerifyNotice',
  full_name='PBMsgInterActionVerifyNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='role_name', full_name='PBMsgInterActionVerifyNotice.role_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgInterActionVerifyNotice.role_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=1171,
  serialized_end=1237,
)


_PBMSGINTERACTIONVERIFYREQUEST = descriptor.Descriptor(
  name='PBMsgInterActionVerifyRequest',
  full_name='PBMsgInterActionVerifyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='role_id', full_name='PBMsgInterActionVerifyRequest.role_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='PBMsgInterActionVerifyRequest.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
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
  serialized_start=1239,
  serialized_end=1323,
)


_PBMSGINTERACTIONVERIFYRESPONSE = descriptor.Descriptor(
  name='PBMsgInterActionVerifyResponse',
  full_name='PBMsgInterActionVerifyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgInterActionVerifyResponse.ret_code', index=0,
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
  serialized_start=1325,
  serialized_end=1375,
)

_PBMSGHOLDDOWNREQUEST.fields_by_name['down_type'].enum_type = _EHOLDDOWNTYPE
_PBMSGINTERACTIONVERIFYREQUEST.fields_by_name['type'].enum_type = _PBINTERACTIONVERIFY
DESCRIPTOR.message_types_by_name['PBMsgHoldRequest'] = _PBMSGHOLDREQUEST
DESCRIPTOR.message_types_by_name['PBMsgHoldResponse'] = _PBMSGHOLDRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgHoldAckNotice'] = _PBMSGHOLDACKNOTICE
DESCRIPTOR.message_types_by_name['PBMsgHoldAckRequest'] = _PBMSGHOLDACKREQUEST
DESCRIPTOR.message_types_by_name['PBMsgHoldAckResponse'] = _PBMSGHOLDACKRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgHoldDownRequest'] = _PBMSGHOLDDOWNREQUEST
DESCRIPTOR.message_types_by_name['PBMsgHoldDownResponse'] = _PBMSGHOLDDOWNRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgHoldInterruptNotice'] = _PBMSGHOLDINTERRUPTNOTICE
DESCRIPTOR.message_types_by_name['PBMsgHoldDelAppListNotice'] = _PBMSGHOLDDELAPPLISTNOTICE
DESCRIPTOR.message_types_by_name['PBMsgHoldAutoShieldRequest'] = _PBMSGHOLDAUTOSHIELDREQUEST
DESCRIPTOR.message_types_by_name['PBMsgHoldAutoShieldResponse'] = _PBMSGHOLDAUTOSHIELDRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgHoldAutoShieldNotice'] = _PBMSGHOLDAUTOSHIELDNOTICE
DESCRIPTOR.message_types_by_name['PBMsgInterActionRequest'] = _PBMSGINTERACTIONREQUEST
DESCRIPTOR.message_types_by_name['PBMsgInterActionRequestEx'] = _PBMSGINTERACTIONREQUESTEX
DESCRIPTOR.message_types_by_name['PBMsgInterActionResponse'] = _PBMSGINTERACTIONRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgInterActionNotice'] = _PBMSGINTERACTIONNOTICE
DESCRIPTOR.message_types_by_name['PBMsgCancelInterActionRequest'] = _PBMSGCANCELINTERACTIONREQUEST
DESCRIPTOR.message_types_by_name['PBMsgCancelInterActionResponse'] = _PBMSGCANCELINTERACTIONRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgInterActionVerifyNotice'] = _PBMSGINTERACTIONVERIFYNOTICE
DESCRIPTOR.message_types_by_name['PBMsgInterActionVerifyRequest'] = _PBMSGINTERACTIONVERIFYREQUEST
DESCRIPTOR.message_types_by_name['PBMsgInterActionVerifyResponse'] = _PBMSGINTERACTIONVERIFYRESPONSE

class PBMsgHoldRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldRequest)

class PBMsgHoldResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldResponse)

class PBMsgHoldAckNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDACKNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldAckNotice)

class PBMsgHoldAckRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDACKREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldAckRequest)

class PBMsgHoldAckResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDACKRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldAckResponse)

class PBMsgHoldDownRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDDOWNREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldDownRequest)

class PBMsgHoldDownResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDDOWNRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldDownResponse)

class PBMsgHoldInterruptNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDINTERRUPTNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldInterruptNotice)

class PBMsgHoldDelAppListNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDDELAPPLISTNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldDelAppListNotice)

class PBMsgHoldAutoShieldRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDAUTOSHIELDREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldAutoShieldRequest)

class PBMsgHoldAutoShieldResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDAUTOSHIELDRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldAutoShieldResponse)

class PBMsgHoldAutoShieldNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGHOLDAUTOSHIELDNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgHoldAutoShieldNotice)

class PBMsgInterActionRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGINTERACTIONREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgInterActionRequest)

class PBMsgInterActionRequestEx(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGINTERACTIONREQUESTEX
  
  # @@protoc_insertion_point(class_scope:PBMsgInterActionRequestEx)

class PBMsgInterActionResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGINTERACTIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgInterActionResponse)

class PBMsgInterActionNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGINTERACTIONNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgInterActionNotice)

class PBMsgCancelInterActionRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGCANCELINTERACTIONREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgCancelInterActionRequest)

class PBMsgCancelInterActionResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGCANCELINTERACTIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgCancelInterActionResponse)

class PBMsgInterActionVerifyNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGINTERACTIONVERIFYNOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgInterActionVerifyNotice)

class PBMsgInterActionVerifyRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGINTERACTIONVERIFYREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgInterActionVerifyRequest)

class PBMsgInterActionVerifyResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGINTERACTIONVERIFYRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgInterActionVerifyResponse)

# @@protoc_insertion_point(module_scope)
