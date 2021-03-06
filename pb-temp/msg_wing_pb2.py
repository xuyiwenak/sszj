# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_base_pb2
import msg_item_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_wing.proto',
  package='',
  serialized_pb='\n\x0emsg_wing.proto\x1a\x0emsg_base.proto\x1a\x0emsg_item.proto\":\n\x19PBMsgWingTrainInfoRequest\x12\x1d\n\tslot_info\x18\x01 \x01(\x0b\x32\n.PBMsgSlot\"p\n\x1aPBMsgWingTrainInfoResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12!\n\twing_info\x18\x02 \x01(\x0b\x32\x0e.PBWingJieInfo\x12\x1d\n\tslot_info\x18\x03 \x01(\x0b\x32\n.PBMsgSlot\"6\n\x15PBMsgWingTrainRequest\x12\x1d\n\tslot_info\x18\x01 \x01(\x0b\x32\n.PBMsgSlot\"l\n\x16PBMsgWingTrainResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12!\n\twing_info\x18\x02 \x01(\x0b\x32\x0e.PBWingJieInfo\x12\x1d\n\tslot_info\x18\x03 \x01(\x0b\x32\n.PBMsgSlot\":\n\x19PBMsgWingUpdateJieRequest\x12\x1d\n\tslot_info\x18\x01 \x01(\x0b\x32\n.PBMsgSlot\"p\n\x1aPBMsgWingUpdateJieResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12!\n\twing_info\x18\x02 \x01(\x0b\x32\x0e.PBWingJieInfo\x12\x1d\n\tslot_info\x18\x03 \x01(\x0b\x32\n.PBMsgSlot\"F\n\x13PBMsgWingProRequest\x12\x10\n\x08wing_jie\x18\x01 \x01(\x11\x12\x1d\n\tslot_info\x18\x02 \x01(\x0b\x32\n.PBMsgSlot\"\x8d\x01\n\x14PBMsgWingProResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x10\n\x08wing_jie\x18\x02 \x01(\x11\x12\x1d\n\tslot_info\x18\x03 \x01(\x0b\x32\n.PBMsgSlot\x12\x1f\n\x08wing_pro\x18\x04 \x01(\x0b\x32\r.PBProperties\x12\x11\n\tcur_shape\x18\x05 \x01(\t\".\n\x18PBMsgWingSheetProRequest\x12\x12\n\nwing_sheet\x18\x01 \x01(\t\"b\n\x19PBMsgWingSheetProResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x12\n\nwing_sheet\x18\x02 \x01(\t\x12\x1f\n\x08wing_pro\x18\x03 \x01(\x0b\x32\r.PBProperties\"\xe5\x01\n\rPBWingJieInfo\x12\x0f\n\x07\x63ur_jie\x18\x01 \x01(\x11\x12\x10\n\x08\x63ur_star\x18\x02 \x01(\x11\x12\x10\n\x08max_star\x18\x03 \x01(\x11\x12\x0f\n\x07max_jie\x18\x04 \x01(\x11\x12\x11\n\tcost_item\x18\x05 \x01(\t\x12\x10\n\x08\x63ost_num\x18\x06 \x01(\x11\x12\x1e\n\x07\x63ur_pro\x18\x07 \x01(\x0b\x32\r.PBProperties\x12\x1f\n\x08next_pro\x18\x08 \x01(\x0b\x32\r.PBProperties\x12\x15\n\rcur_jie_shape\x18\t \x01(\t\x12\x11\n\tdiff_star\x18\n \x01(\x11\":\n\x15PBWingTrainInfoNotice\x12\x0f\n\x07\x63ur_jie\x18\x01 \x01(\x11\x12\x10\n\x08\x63ur_star\x18\x02 \x01(\x11\"2\n\rPBDBWingTrain\x12\x10\n\x08\x63ur_star\x18\x01 \x01(\x11\x12\x0f\n\x07\x63ur_jie\x18\x02 \x01(\x11\x42\x02H\x01')




_PBMSGWINGTRAININFOREQUEST = descriptor.Descriptor(
  name='PBMsgWingTrainInfoRequest',
  full_name='PBMsgWingTrainInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBMsgWingTrainInfoRequest.slot_info', index=0,
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
  serialized_start=50,
  serialized_end=108,
)


_PBMSGWINGTRAININFORESPONSE = descriptor.Descriptor(
  name='PBMsgWingTrainInfoResponse',
  full_name='PBMsgWingTrainInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWingTrainInfoResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wing_info', full_name='PBMsgWingTrainInfoResponse.wing_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBMsgWingTrainInfoResponse.slot_info', index=2,
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
  serialized_start=110,
  serialized_end=222,
)


_PBMSGWINGTRAINREQUEST = descriptor.Descriptor(
  name='PBMsgWingTrainRequest',
  full_name='PBMsgWingTrainRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBMsgWingTrainRequest.slot_info', index=0,
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
  serialized_start=224,
  serialized_end=278,
)


_PBMSGWINGTRAINRESPONSE = descriptor.Descriptor(
  name='PBMsgWingTrainResponse',
  full_name='PBMsgWingTrainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWingTrainResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wing_info', full_name='PBMsgWingTrainResponse.wing_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBMsgWingTrainResponse.slot_info', index=2,
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
  serialized_start=280,
  serialized_end=388,
)


_PBMSGWINGUPDATEJIEREQUEST = descriptor.Descriptor(
  name='PBMsgWingUpdateJieRequest',
  full_name='PBMsgWingUpdateJieRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBMsgWingUpdateJieRequest.slot_info', index=0,
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
  serialized_start=390,
  serialized_end=448,
)


_PBMSGWINGUPDATEJIERESPONSE = descriptor.Descriptor(
  name='PBMsgWingUpdateJieResponse',
  full_name='PBMsgWingUpdateJieResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWingUpdateJieResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wing_info', full_name='PBMsgWingUpdateJieResponse.wing_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBMsgWingUpdateJieResponse.slot_info', index=2,
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
  serialized_start=450,
  serialized_end=562,
)


_PBMSGWINGPROREQUEST = descriptor.Descriptor(
  name='PBMsgWingProRequest',
  full_name='PBMsgWingProRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='wing_jie', full_name='PBMsgWingProRequest.wing_jie', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBMsgWingProRequest.slot_info', index=1,
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
  serialized_start=564,
  serialized_end=634,
)


_PBMSGWINGPRORESPONSE = descriptor.Descriptor(
  name='PBMsgWingProResponse',
  full_name='PBMsgWingProResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWingProResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wing_jie', full_name='PBMsgWingProResponse.wing_jie', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slot_info', full_name='PBMsgWingProResponse.slot_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wing_pro', full_name='PBMsgWingProResponse.wing_pro', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_shape', full_name='PBMsgWingProResponse.cur_shape', index=4,
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
  serialized_start=637,
  serialized_end=778,
)


_PBMSGWINGSHEETPROREQUEST = descriptor.Descriptor(
  name='PBMsgWingSheetProRequest',
  full_name='PBMsgWingSheetProRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='wing_sheet', full_name='PBMsgWingSheetProRequest.wing_sheet', index=0,
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
  serialized_start=780,
  serialized_end=826,
)


_PBMSGWINGSHEETPRORESPONSE = descriptor.Descriptor(
  name='PBMsgWingSheetProResponse',
  full_name='PBMsgWingSheetProResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWingSheetProResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wing_sheet', full_name='PBMsgWingSheetProResponse.wing_sheet', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wing_pro', full_name='PBMsgWingSheetProResponse.wing_pro', index=2,
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
  serialized_start=828,
  serialized_end=926,
)


_PBWINGJIEINFO = descriptor.Descriptor(
  name='PBWingJieInfo',
  full_name='PBWingJieInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cur_jie', full_name='PBWingJieInfo.cur_jie', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_star', full_name='PBWingJieInfo.cur_star', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_star', full_name='PBWingJieInfo.max_star', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='max_jie', full_name='PBWingJieInfo.max_jie', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_item', full_name='PBWingJieInfo.cost_item', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cost_num', full_name='PBWingJieInfo.cost_num', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_pro', full_name='PBWingJieInfo.cur_pro', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='next_pro', full_name='PBWingJieInfo.next_pro', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_jie_shape', full_name='PBWingJieInfo.cur_jie_shape', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='diff_star', full_name='PBWingJieInfo.diff_star', index=9,
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
  serialized_start=929,
  serialized_end=1158,
)


_PBWINGTRAININFONOTICE = descriptor.Descriptor(
  name='PBWingTrainInfoNotice',
  full_name='PBWingTrainInfoNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cur_jie', full_name='PBWingTrainInfoNotice.cur_jie', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_star', full_name='PBWingTrainInfoNotice.cur_star', index=1,
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
  serialized_start=1160,
  serialized_end=1218,
)


_PBDBWINGTRAIN = descriptor.Descriptor(
  name='PBDBWingTrain',
  full_name='PBDBWingTrain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cur_star', full_name='PBDBWingTrain.cur_star', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cur_jie', full_name='PBDBWingTrain.cur_jie', index=1,
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
  serialized_start=1220,
  serialized_end=1270,
)

_PBMSGWINGTRAININFOREQUEST.fields_by_name['slot_info'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWINGTRAININFORESPONSE.fields_by_name['wing_info'].message_type = _PBWINGJIEINFO
_PBMSGWINGTRAININFORESPONSE.fields_by_name['slot_info'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWINGTRAINREQUEST.fields_by_name['slot_info'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWINGTRAINRESPONSE.fields_by_name['wing_info'].message_type = _PBWINGJIEINFO
_PBMSGWINGTRAINRESPONSE.fields_by_name['slot_info'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWINGUPDATEJIEREQUEST.fields_by_name['slot_info'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWINGUPDATEJIERESPONSE.fields_by_name['wing_info'].message_type = _PBWINGJIEINFO
_PBMSGWINGUPDATEJIERESPONSE.fields_by_name['slot_info'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWINGPROREQUEST.fields_by_name['slot_info'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWINGPRORESPONSE.fields_by_name['slot_info'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWINGPRORESPONSE.fields_by_name['wing_pro'].message_type = msg_item_pb2._PBPROPERTIES
_PBMSGWINGSHEETPRORESPONSE.fields_by_name['wing_pro'].message_type = msg_item_pb2._PBPROPERTIES
_PBWINGJIEINFO.fields_by_name['cur_pro'].message_type = msg_item_pb2._PBPROPERTIES
_PBWINGJIEINFO.fields_by_name['next_pro'].message_type = msg_item_pb2._PBPROPERTIES
DESCRIPTOR.message_types_by_name['PBMsgWingTrainInfoRequest'] = _PBMSGWINGTRAININFOREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWingTrainInfoResponse'] = _PBMSGWINGTRAININFORESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWingTrainRequest'] = _PBMSGWINGTRAINREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWingTrainResponse'] = _PBMSGWINGTRAINRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWingUpdateJieRequest'] = _PBMSGWINGUPDATEJIEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWingUpdateJieResponse'] = _PBMSGWINGUPDATEJIERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWingProRequest'] = _PBMSGWINGPROREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWingProResponse'] = _PBMSGWINGPRORESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWingSheetProRequest'] = _PBMSGWINGSHEETPROREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWingSheetProResponse'] = _PBMSGWINGSHEETPRORESPONSE
DESCRIPTOR.message_types_by_name['PBWingJieInfo'] = _PBWINGJIEINFO
DESCRIPTOR.message_types_by_name['PBWingTrainInfoNotice'] = _PBWINGTRAININFONOTICE
DESCRIPTOR.message_types_by_name['PBDBWingTrain'] = _PBDBWINGTRAIN

class PBMsgWingTrainInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGTRAININFOREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWingTrainInfoRequest)

class PBMsgWingTrainInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGTRAININFORESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWingTrainInfoResponse)

class PBMsgWingTrainRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGTRAINREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWingTrainRequest)

class PBMsgWingTrainResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGTRAINRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWingTrainResponse)

class PBMsgWingUpdateJieRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGUPDATEJIEREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWingUpdateJieRequest)

class PBMsgWingUpdateJieResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGUPDATEJIERESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWingUpdateJieResponse)

class PBMsgWingProRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGPROREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWingProRequest)

class PBMsgWingProResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGPRORESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWingProResponse)

class PBMsgWingSheetProRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGSHEETPROREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWingSheetProRequest)

class PBMsgWingSheetProResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWINGSHEETPRORESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWingSheetProResponse)

class PBWingJieInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWINGJIEINFO
  
  # @@protoc_insertion_point(class_scope:PBWingJieInfo)

class PBWingTrainInfoNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBWINGTRAININFONOTICE
  
  # @@protoc_insertion_point(class_scope:PBWingTrainInfoNotice)

class PBDBWingTrain(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBDBWINGTRAIN
  
  # @@protoc_insertion_point(class_scope:PBDBWingTrain)

# @@protoc_insertion_point(module_scope)
