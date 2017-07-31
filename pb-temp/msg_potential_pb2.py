# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_base_pb2
import msg_item_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_potential.proto',
  package='',
  serialized_pb='\n\x13msg_potential.proto\x1a\x0emsg_base.proto\x1a\x0emsg_item.proto\"\xf1\x01\n\x18PBMsgPotentialInfoNotice\x12\x10\n\x08\x61\x63tivete\x18\x01 \x01(\x08\x12\x11\n\tcur_value\x18\x02 \x01(\x11\x12\x11\n\tcur_calss\x18\x03 \x01(\x11\x12$\n\rtemp_pro_list\x18\x04 \x01(\x0b\x32\r.PBProperties\x12#\n\x0c\x63ur_pro_list\x18\x05 \x01(\x0b\x32\r.PBProperties\x12$\n\rlast_pro_list\x18\x06 \x01(\x0b\x32\r.PBProperties\x12,\n\x0e\x61ttrstate_list\x18\x07 \x01(\x0b\x32\x14.PBPotentialAttrList\"\x1b\n\x19PBMsgPotentialFeedRequest\"O\n\x1aPBMsgPotentialFeedResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x1f\n\x08pro_list\x18\x02 \x01(\x0b\x32\r.PBProperties\"\x1e\n\x1cPBMsgPotentialTenFeedRequest\"q\n\x1dPBMsgPotentialTenFeedResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12-\n\x0bresult_list\x18\x02 \x03(\x0b\x32\x18.PBMsgPotentialTenResult\x12\x0f\n\x07success\x18\x03 \x01(\x08\"N\n\x17PBMsgPotentialTenResult\x12\x12\n\nfeed_times\x18\x02 \x01(\x11\x12\x1f\n\x08pro_list\x18\x03 \x01(\x0b\x32\r.PBProperties\"!\n\x1fPBMsgPotentialTenReplaceRequest\"4\n PBMsgPotentialTenReplaceResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\"P\n\x14PBPotentialAttrState\x12\x11\n\tattr_type\x18\x01 \x01(\x11\x12\x11\n\tattr_mode\x18\x02 \x01(\x11\x12\x12\n\nattr_state\x18\x03 \x01(\x11\"?\n\x13PBPotentialAttrList\x12(\n\tattrstate\x18\x01 \x03(\x0b\x32\x15.PBPotentialAttrState\"E\n\x15PBMsgAttrStateRequest\x12,\n\x0e\x61ttrstate_list\x18\x01 \x01(\x0b\x32\x14.PBPotentialAttrList\"X\n\x16PBMsgAttrStateResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12,\n\x0e\x61ttrstate_list\x18\x02 \x01(\x0b\x32\x14.PBPotentialAttrList\"\x1e\n\x1cPBMsgPotentialReplaceRequest\"1\n\x1dPBMsgPotentialReplaceResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\"\x1e\n\x1cPBMsgPotentialUpClassRequest\"W\n\x1dPBMsgPotentialUpClassResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x11\n\tcur_class\x18\x02 \x01(\x11\x12\x11\n\tcur_value\x18\x03 \x01(\x11')




_PBMSGPOTENTIALINFONOTICE = descriptor.Descriptor(
  name='PBMsgPotentialInfoNotice',
  full_name='PBMsgPotentialInfoNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='activete', full_name='PBMsgPotentialInfoNotice.activete', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_value', full_name='PBMsgPotentialInfoNotice.cur_value', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_calss', full_name='PBMsgPotentialInfoNotice.cur_calss', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='temp_pro_list', full_name='PBMsgPotentialInfoNotice.temp_pro_list', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_pro_list', full_name='PBMsgPotentialInfoNotice.cur_pro_list', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_pro_list', full_name='PBMsgPotentialInfoNotice.last_pro_list', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attrstate_list', full_name='PBMsgPotentialInfoNotice.attrstate_list', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=56,
  serialized_end=297,
)


_PBMSGPOTENTIALFEEDREQUEST = descriptor.Descriptor(
  name='PBMsgPotentialFeedRequest',
  full_name='PBMsgPotentialFeedRequest',
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
  serialized_start=299,
  serialized_end=326,
)


_PBMSGPOTENTIALFEEDRESPONSE = descriptor.Descriptor(
  name='PBMsgPotentialFeedResponse',
  full_name='PBMsgPotentialFeedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgPotentialFeedResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pro_list', full_name='PBMsgPotentialFeedResponse.pro_list', index=1,
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
  serialized_start=328,
  serialized_end=407,
)


_PBMSGPOTENTIALTENFEEDREQUEST = descriptor.Descriptor(
  name='PBMsgPotentialTenFeedRequest',
  full_name='PBMsgPotentialTenFeedRequest',
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
  serialized_start=409,
  serialized_end=439,
)


_PBMSGPOTENTIALTENFEEDRESPONSE = descriptor.Descriptor(
  name='PBMsgPotentialTenFeedResponse',
  full_name='PBMsgPotentialTenFeedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgPotentialTenFeedResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='result_list', full_name='PBMsgPotentialTenFeedResponse.result_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='success', full_name='PBMsgPotentialTenFeedResponse.success', index=2,
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
  serialized_start=441,
  serialized_end=554,
)


_PBMSGPOTENTIALTENRESULT = descriptor.Descriptor(
  name='PBMsgPotentialTenResult',
  full_name='PBMsgPotentialTenResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='feed_times', full_name='PBMsgPotentialTenResult.feed_times', index=0,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pro_list', full_name='PBMsgPotentialTenResult.pro_list', index=1,
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
  serialized_start=556,
  serialized_end=634,
)


_PBMSGPOTENTIALTENREPLACEREQUEST = descriptor.Descriptor(
  name='PBMsgPotentialTenReplaceRequest',
  full_name='PBMsgPotentialTenReplaceRequest',
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
  serialized_start=636,
  serialized_end=669,
)


_PBMSGPOTENTIALTENREPLACERESPONSE = descriptor.Descriptor(
  name='PBMsgPotentialTenReplaceResponse',
  full_name='PBMsgPotentialTenReplaceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgPotentialTenReplaceResponse.ret_code', index=0,
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
  serialized_start=671,
  serialized_end=723,
)


_PBPOTENTIALATTRSTATE = descriptor.Descriptor(
  name='PBPotentialAttrState',
  full_name='PBPotentialAttrState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr_type', full_name='PBPotentialAttrState.attr_type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr_mode', full_name='PBPotentialAttrState.attr_mode', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr_state', full_name='PBPotentialAttrState.attr_state', index=2,
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
  serialized_start=725,
  serialized_end=805,
)


_PBPOTENTIALATTRLIST = descriptor.Descriptor(
  name='PBPotentialAttrList',
  full_name='PBPotentialAttrList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attrstate', full_name='PBPotentialAttrList.attrstate', index=0,
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
  serialized_start=807,
  serialized_end=870,
)


_PBMSGATTRSTATEREQUEST = descriptor.Descriptor(
  name='PBMsgAttrStateRequest',
  full_name='PBMsgAttrStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attrstate_list', full_name='PBMsgAttrStateRequest.attrstate_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=872,
  serialized_end=941,
)


_PBMSGATTRSTATERESPONSE = descriptor.Descriptor(
  name='PBMsgAttrStateResponse',
  full_name='PBMsgAttrStateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgAttrStateResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attrstate_list', full_name='PBMsgAttrStateResponse.attrstate_list', index=1,
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
  serialized_start=943,
  serialized_end=1031,
)


_PBMSGPOTENTIALREPLACEREQUEST = descriptor.Descriptor(
  name='PBMsgPotentialReplaceRequest',
  full_name='PBMsgPotentialReplaceRequest',
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
  serialized_start=1033,
  serialized_end=1063,
)


_PBMSGPOTENTIALREPLACERESPONSE = descriptor.Descriptor(
  name='PBMsgPotentialReplaceResponse',
  full_name='PBMsgPotentialReplaceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgPotentialReplaceResponse.ret_code', index=0,
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
  serialized_start=1065,
  serialized_end=1114,
)


_PBMSGPOTENTIALUPCLASSREQUEST = descriptor.Descriptor(
  name='PBMsgPotentialUpClassRequest',
  full_name='PBMsgPotentialUpClassRequest',
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
  serialized_start=1116,
  serialized_end=1146,
)


_PBMSGPOTENTIALUPCLASSRESPONSE = descriptor.Descriptor(
  name='PBMsgPotentialUpClassResponse',
  full_name='PBMsgPotentialUpClassResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgPotentialUpClassResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_class', full_name='PBMsgPotentialUpClassResponse.cur_class', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_value', full_name='PBMsgPotentialUpClassResponse.cur_value', index=2,
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
  serialized_start=1148,
  serialized_end=1235,
)

_PBMSGPOTENTIALINFONOTICE.fields_by_name['temp_pro_list'].message_type = msg_item_pb2._PBPROPERTIES
_PBMSGPOTENTIALINFONOTICE.fields_by_name['cur_pro_list'].message_type = msg_item_pb2._PBPROPERTIES
_PBMSGPOTENTIALINFONOTICE.fields_by_name['last_pro_list'].message_type = msg_item_pb2._PBPROPERTIES
_PBMSGPOTENTIALINFONOTICE.fields_by_name['attrstate_list'].message_type = _PBPOTENTIALATTRLIST
_PBMSGPOTENTIALFEEDRESPONSE.fields_by_name['pro_list'].message_type = msg_item_pb2._PBPROPERTIES
_PBMSGPOTENTIALTENFEEDRESPONSE.fields_by_name['result_list'].message_type = _PBMSGPOTENTIALTENRESULT
_PBMSGPOTENTIALTENRESULT.fields_by_name['pro_list'].message_type = msg_item_pb2._PBPROPERTIES
_PBPOTENTIALATTRLIST.fields_by_name['attrstate'].message_type = _PBPOTENTIALATTRSTATE
_PBMSGATTRSTATEREQUEST.fields_by_name['attrstate_list'].message_type = _PBPOTENTIALATTRLIST
_PBMSGATTRSTATERESPONSE.fields_by_name['attrstate_list'].message_type = _PBPOTENTIALATTRLIST
DESCRIPTOR.message_types_by_name['PBMsgPotentialInfoNotice'] = _PBMSGPOTENTIALINFONOTICE
DESCRIPTOR.message_types_by_name['PBMsgPotentialFeedRequest'] = _PBMSGPOTENTIALFEEDREQUEST
DESCRIPTOR.message_types_by_name['PBMsgPotentialFeedResponse'] = _PBMSGPOTENTIALFEEDRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgPotentialTenFeedRequest'] = _PBMSGPOTENTIALTENFEEDREQUEST
DESCRIPTOR.message_types_by_name['PBMsgPotentialTenFeedResponse'] = _PBMSGPOTENTIALTENFEEDRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgPotentialTenResult'] = _PBMSGPOTENTIALTENRESULT
DESCRIPTOR.message_types_by_name['PBMsgPotentialTenReplaceRequest'] = _PBMSGPOTENTIALTENREPLACEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgPotentialTenReplaceResponse'] = _PBMSGPOTENTIALTENREPLACERESPONSE
DESCRIPTOR.message_types_by_name['PBPotentialAttrState'] = _PBPOTENTIALATTRSTATE
DESCRIPTOR.message_types_by_name['PBPotentialAttrList'] = _PBPOTENTIALATTRLIST
DESCRIPTOR.message_types_by_name['PBMsgAttrStateRequest'] = _PBMSGATTRSTATEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgAttrStateResponse'] = _PBMSGATTRSTATERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgPotentialReplaceRequest'] = _PBMSGPOTENTIALREPLACEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgPotentialReplaceResponse'] = _PBMSGPOTENTIALREPLACERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgPotentialUpClassRequest'] = _PBMSGPOTENTIALUPCLASSREQUEST
DESCRIPTOR.message_types_by_name['PBMsgPotentialUpClassResponse'] = _PBMSGPOTENTIALUPCLASSRESPONSE

class PBMsgPotentialInfoNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALINFONOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialInfoNotice)

class PBMsgPotentialFeedRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALFEEDREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialFeedRequest)

class PBMsgPotentialFeedResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALFEEDRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialFeedResponse)

class PBMsgPotentialTenFeedRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALTENFEEDREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialTenFeedRequest)

class PBMsgPotentialTenFeedResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALTENFEEDRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialTenFeedResponse)

class PBMsgPotentialTenResult(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALTENRESULT
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialTenResult)

class PBMsgPotentialTenReplaceRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALTENREPLACEREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialTenReplaceRequest)

class PBMsgPotentialTenReplaceResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALTENREPLACERESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialTenReplaceResponse)

class PBPotentialAttrState(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBPOTENTIALATTRSTATE
  
  # @@protoc_insertion_point(class_scope:PBPotentialAttrState)

class PBPotentialAttrList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBPOTENTIALATTRLIST
  
  # @@protoc_insertion_point(class_scope:PBPotentialAttrList)

class PBMsgAttrStateRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGATTRSTATEREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgAttrStateRequest)

class PBMsgAttrStateResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGATTRSTATERESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgAttrStateResponse)

class PBMsgPotentialReplaceRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALREPLACEREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialReplaceRequest)

class PBMsgPotentialReplaceResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALREPLACERESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialReplaceResponse)

class PBMsgPotentialUpClassRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALUPCLASSREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialUpClassRequest)

class PBMsgPotentialUpClassResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGPOTENTIALUPCLASSRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgPotentialUpClassResponse)

# @@protoc_insertion_point(module_scope)
