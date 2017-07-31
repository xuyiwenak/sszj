# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import msg_base_pb2
import msg_item_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='msg_wardrobe.proto',
  package='',
  serialized_pb='\n\x12msg_wardrobe.proto\x1a\x0emsg_base.proto\x1a\x0emsg_item.proto\"\x16\n\x14PBMsgWardrobeRequest\"R\n\x15PBMsgWardrobeResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\'\n\x08\x66\x61shions\x18\x02 \x03(\x0b\x32\x15.PBMsgWardrobeFashion\"u\n\x14PBMsgWardrobeFashion\x12\x1c\n\x04part\x18\x01 \x01(\x0e\x32\x0e.PBFashionPart\x12\x0c\n\x04type\x18\x02 \x01(\x11\x12\x0f\n\x07is_have\x18\x03 \x01(\x08\x12 \n\x08wardrobe\x18\x04 \x01(\x0b\x32\x0e.PBMsgWardrobe\"S\n\rPBMsgWardrobe\x12\x1f\n\x08\x62\x61g_grid\x18\x01 \x01(\x0b\x32\r.PBMsgInvGrid\x12!\n\x05items\x18\x02 \x03(\x0b\x32\x12.PBMsgWardrobeItem\">\n\x11PBMsgWardrobeItem\x12\x0c\n\x04slot\x18\x01 \x01(\x11\x12\x1b\n\x04item\x18\x02 \x01(\x0b\x32\r.PBMsgInvSlot\"`\n\x1aPBMsgWardrobeHangUpRequest\x12\x1c\n\x08src_slot\x18\x01 \x01(\x0b\x32\n.PBMsgSlot\x12$\n\x08\x64st_slot\x18\x02 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"U\n\x1bPBMsgWardrobeHangUpResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12$\n\x08\x64st_slot\x18\x02 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"D\n\x1cPBMsgWardrobeHangDownRequest\x12$\n\x08src_slot\x18\x01 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"W\n\x1dPBMsgWardrobeHangDownResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12$\n\x08src_slot\x18\x02 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"C\n\x1aPBMsgWardrobeUnlockRequest\x12%\n\tlock_slot\x18\x01 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"V\n\x1bPBMsgWardrobeUnlockResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12%\n\tlock_slot\x18\x02 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"G\n\x1dPBMsgFashionShapeApplyRequest\x12&\n\nshape_slot\x18\x01 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"Z\n\x1ePBMsgFashionShapeApplyResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12&\n\nshape_slot\x18\x02 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"M\n\x11PBMsgWardrobeSlot\x12\x1c\n\x04part\x18\x01 \x01(\x0e\x32\x0e.PBFashionPart\x12\x0c\n\x04type\x18\x02 \x01(\x11\x12\x0c\n\x04slot\x18\x03 \x01(\r\"?\n\x1fPBMsgRestoreFashionShapeRequest\x12\x1c\n\x04part\x18\x01 \x01(\x0e\x32\x0e.PBFashionPart\"R\n PBMsgRestoreFashionShapeResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12\x1c\n\x04part\x18\x02 \x01(\x0e\x32\x0e.PBFashionPart\"J\n PBMsgEquitWardrobeFashionRequest\x12&\n\nequit_slot\x18\x01 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"]\n!PBMsgEquitWardrobeFashionResponse\x12\x10\n\x08ret_code\x18\x01 \x01(\x11\x12&\n\nequit_slot\x18\x02 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\"w\n\x19PBMsgWardrobeChangeNotice\x12\x1b\n\x02op\x18\x01 \x01(\x0e\x32\x0f.PBWardrobeOper\x12 \n\x04slot\x18\x02 \x01(\x0b\x32\x12.PBMsgWardrobeSlot\x12\x1b\n\x04item\x18\x03 \x01(\x0b\x32\r.PBMsgInvSlot*N\n\rPBFashionPart\x12\x12\n\x0e\x65nFashion_Head\x10\x01\x12\x15\n\x11\x65nFashion_Clothes\x10\x02\x12\x12\n\x0e\x65nFashion_Wing\x10\x03*R\n\x0ePBWardrobeOper\x12\x12\n\x0e\x65nWardrobe_Add\x10\x01\x12\x15\n\x11\x65nWardrobe_Remove\x10\x02\x12\x15\n\x11\x65nWardrobe_Update\x10\x03\x42\x02H\x01')

_PBFASHIONPART = descriptor.EnumDescriptor(
  name='PBFashionPart',
  full_name='PBFashionPart',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='enFashion_Head', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enFashion_Clothes', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enFashion_Wing', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1616,
  serialized_end=1694,
)


_PBWARDROBEOPER = descriptor.EnumDescriptor(
  name='PBWardrobeOper',
  full_name='PBWardrobeOper',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='enWardrobe_Add', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enWardrobe_Remove', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='enWardrobe_Update', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1696,
  serialized_end=1778,
)


enFashion_Head = 1
enFashion_Clothes = 2
enFashion_Wing = 3
enWardrobe_Add = 1
enWardrobe_Remove = 2
enWardrobe_Update = 3



_PBMSGWARDROBEREQUEST = descriptor.Descriptor(
  name='PBMsgWardrobeRequest',
  full_name='PBMsgWardrobeRequest',
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
  serialized_start=54,
  serialized_end=76,
)


_PBMSGWARDROBERESPONSE = descriptor.Descriptor(
  name='PBMsgWardrobeResponse',
  full_name='PBMsgWardrobeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWardrobeResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fashions', full_name='PBMsgWardrobeResponse.fashions', index=1,
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
  serialized_start=78,
  serialized_end=160,
)


_PBMSGWARDROBEFASHION = descriptor.Descriptor(
  name='PBMsgWardrobeFashion',
  full_name='PBMsgWardrobeFashion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='part', full_name='PBMsgWardrobeFashion.part', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='PBMsgWardrobeFashion.type', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_have', full_name='PBMsgWardrobeFashion.is_have', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='wardrobe', full_name='PBMsgWardrobeFashion.wardrobe', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=162,
  serialized_end=279,
)


_PBMSGWARDROBE = descriptor.Descriptor(
  name='PBMsgWardrobe',
  full_name='PBMsgWardrobe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='bag_grid', full_name='PBMsgWardrobe.bag_grid', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='items', full_name='PBMsgWardrobe.items', index=1,
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
  serialized_start=281,
  serialized_end=364,
)


_PBMSGWARDROBEITEM = descriptor.Descriptor(
  name='PBMsgWardrobeItem',
  full_name='PBMsgWardrobeItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='slot', full_name='PBMsgWardrobeItem.slot', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='PBMsgWardrobeItem.item', index=1,
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
  serialized_start=366,
  serialized_end=428,
)


_PBMSGWARDROBEHANGUPREQUEST = descriptor.Descriptor(
  name='PBMsgWardrobeHangUpRequest',
  full_name='PBMsgWardrobeHangUpRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='src_slot', full_name='PBMsgWardrobeHangUpRequest.src_slot', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dst_slot', full_name='PBMsgWardrobeHangUpRequest.dst_slot', index=1,
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
  serialized_start=430,
  serialized_end=526,
)


_PBMSGWARDROBEHANGUPRESPONSE = descriptor.Descriptor(
  name='PBMsgWardrobeHangUpResponse',
  full_name='PBMsgWardrobeHangUpResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWardrobeHangUpResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dst_slot', full_name='PBMsgWardrobeHangUpResponse.dst_slot', index=1,
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
  serialized_start=528,
  serialized_end=613,
)


_PBMSGWARDROBEHANGDOWNREQUEST = descriptor.Descriptor(
  name='PBMsgWardrobeHangDownRequest',
  full_name='PBMsgWardrobeHangDownRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='src_slot', full_name='PBMsgWardrobeHangDownRequest.src_slot', index=0,
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
  serialized_start=615,
  serialized_end=683,
)


_PBMSGWARDROBEHANGDOWNRESPONSE = descriptor.Descriptor(
  name='PBMsgWardrobeHangDownResponse',
  full_name='PBMsgWardrobeHangDownResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWardrobeHangDownResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='src_slot', full_name='PBMsgWardrobeHangDownResponse.src_slot', index=1,
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
  serialized_start=685,
  serialized_end=772,
)


_PBMSGWARDROBEUNLOCKREQUEST = descriptor.Descriptor(
  name='PBMsgWardrobeUnlockRequest',
  full_name='PBMsgWardrobeUnlockRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='lock_slot', full_name='PBMsgWardrobeUnlockRequest.lock_slot', index=0,
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
  serialized_start=774,
  serialized_end=841,
)


_PBMSGWARDROBEUNLOCKRESPONSE = descriptor.Descriptor(
  name='PBMsgWardrobeUnlockResponse',
  full_name='PBMsgWardrobeUnlockResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgWardrobeUnlockResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='lock_slot', full_name='PBMsgWardrobeUnlockResponse.lock_slot', index=1,
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
  serialized_start=843,
  serialized_end=929,
)


_PBMSGFASHIONSHAPEAPPLYREQUEST = descriptor.Descriptor(
  name='PBMsgFashionShapeApplyRequest',
  full_name='PBMsgFashionShapeApplyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='shape_slot', full_name='PBMsgFashionShapeApplyRequest.shape_slot', index=0,
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
  serialized_start=931,
  serialized_end=1002,
)


_PBMSGFASHIONSHAPEAPPLYRESPONSE = descriptor.Descriptor(
  name='PBMsgFashionShapeApplyResponse',
  full_name='PBMsgFashionShapeApplyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgFashionShapeApplyResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='shape_slot', full_name='PBMsgFashionShapeApplyResponse.shape_slot', index=1,
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
  serialized_start=1004,
  serialized_end=1094,
)


_PBMSGWARDROBESLOT = descriptor.Descriptor(
  name='PBMsgWardrobeSlot',
  full_name='PBMsgWardrobeSlot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='part', full_name='PBMsgWardrobeSlot.part', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='PBMsgWardrobeSlot.type', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slot', full_name='PBMsgWardrobeSlot.slot', index=2,
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
  serialized_start=1096,
  serialized_end=1173,
)


_PBMSGRESTOREFASHIONSHAPEREQUEST = descriptor.Descriptor(
  name='PBMsgRestoreFashionShapeRequest',
  full_name='PBMsgRestoreFashionShapeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='part', full_name='PBMsgRestoreFashionShapeRequest.part', index=0,
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
  serialized_start=1175,
  serialized_end=1238,
)


_PBMSGRESTOREFASHIONSHAPERESPONSE = descriptor.Descriptor(
  name='PBMsgRestoreFashionShapeResponse',
  full_name='PBMsgRestoreFashionShapeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgRestoreFashionShapeResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='part', full_name='PBMsgRestoreFashionShapeResponse.part', index=1,
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
  serialized_start=1240,
  serialized_end=1322,
)


_PBMSGEQUITWARDROBEFASHIONREQUEST = descriptor.Descriptor(
  name='PBMsgEquitWardrobeFashionRequest',
  full_name='PBMsgEquitWardrobeFashionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='equit_slot', full_name='PBMsgEquitWardrobeFashionRequest.equit_slot', index=0,
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
  serialized_start=1324,
  serialized_end=1398,
)


_PBMSGEQUITWARDROBEFASHIONRESPONSE = descriptor.Descriptor(
  name='PBMsgEquitWardrobeFashionResponse',
  full_name='PBMsgEquitWardrobeFashionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ret_code', full_name='PBMsgEquitWardrobeFashionResponse.ret_code', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='equit_slot', full_name='PBMsgEquitWardrobeFashionResponse.equit_slot', index=1,
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
  serialized_start=1400,
  serialized_end=1493,
)


_PBMSGWARDROBECHANGENOTICE = descriptor.Descriptor(
  name='PBMsgWardrobeChangeNotice',
  full_name='PBMsgWardrobeChangeNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='op', full_name='PBMsgWardrobeChangeNotice.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='slot', full_name='PBMsgWardrobeChangeNotice.slot', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='item', full_name='PBMsgWardrobeChangeNotice.item', index=2,
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
  serialized_start=1495,
  serialized_end=1614,
)

_PBMSGWARDROBERESPONSE.fields_by_name['fashions'].message_type = _PBMSGWARDROBEFASHION
_PBMSGWARDROBEFASHION.fields_by_name['part'].enum_type = _PBFASHIONPART
_PBMSGWARDROBEFASHION.fields_by_name['wardrobe'].message_type = _PBMSGWARDROBE
_PBMSGWARDROBE.fields_by_name['bag_grid'].message_type = msg_item_pb2._PBMSGINVGRID
_PBMSGWARDROBE.fields_by_name['items'].message_type = _PBMSGWARDROBEITEM
_PBMSGWARDROBEITEM.fields_by_name['item'].message_type = msg_item_pb2._PBMSGINVSLOT
_PBMSGWARDROBEHANGUPREQUEST.fields_by_name['src_slot'].message_type = msg_item_pb2._PBMSGSLOT
_PBMSGWARDROBEHANGUPREQUEST.fields_by_name['dst_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGWARDROBEHANGUPRESPONSE.fields_by_name['dst_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGWARDROBEHANGDOWNREQUEST.fields_by_name['src_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGWARDROBEHANGDOWNRESPONSE.fields_by_name['src_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGWARDROBEUNLOCKREQUEST.fields_by_name['lock_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGWARDROBEUNLOCKRESPONSE.fields_by_name['lock_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGFASHIONSHAPEAPPLYREQUEST.fields_by_name['shape_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGFASHIONSHAPEAPPLYRESPONSE.fields_by_name['shape_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGWARDROBESLOT.fields_by_name['part'].enum_type = _PBFASHIONPART
_PBMSGRESTOREFASHIONSHAPEREQUEST.fields_by_name['part'].enum_type = _PBFASHIONPART
_PBMSGRESTOREFASHIONSHAPERESPONSE.fields_by_name['part'].enum_type = _PBFASHIONPART
_PBMSGEQUITWARDROBEFASHIONREQUEST.fields_by_name['equit_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGEQUITWARDROBEFASHIONRESPONSE.fields_by_name['equit_slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGWARDROBECHANGENOTICE.fields_by_name['op'].enum_type = _PBWARDROBEOPER
_PBMSGWARDROBECHANGENOTICE.fields_by_name['slot'].message_type = _PBMSGWARDROBESLOT
_PBMSGWARDROBECHANGENOTICE.fields_by_name['item'].message_type = msg_item_pb2._PBMSGINVSLOT
DESCRIPTOR.message_types_by_name['PBMsgWardrobeRequest'] = _PBMSGWARDROBEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWardrobeResponse'] = _PBMSGWARDROBERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWardrobeFashion'] = _PBMSGWARDROBEFASHION
DESCRIPTOR.message_types_by_name['PBMsgWardrobe'] = _PBMSGWARDROBE
DESCRIPTOR.message_types_by_name['PBMsgWardrobeItem'] = _PBMSGWARDROBEITEM
DESCRIPTOR.message_types_by_name['PBMsgWardrobeHangUpRequest'] = _PBMSGWARDROBEHANGUPREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWardrobeHangUpResponse'] = _PBMSGWARDROBEHANGUPRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWardrobeHangDownRequest'] = _PBMSGWARDROBEHANGDOWNREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWardrobeHangDownResponse'] = _PBMSGWARDROBEHANGDOWNRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWardrobeUnlockRequest'] = _PBMSGWARDROBEUNLOCKREQUEST
DESCRIPTOR.message_types_by_name['PBMsgWardrobeUnlockResponse'] = _PBMSGWARDROBEUNLOCKRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgFashionShapeApplyRequest'] = _PBMSGFASHIONSHAPEAPPLYREQUEST
DESCRIPTOR.message_types_by_name['PBMsgFashionShapeApplyResponse'] = _PBMSGFASHIONSHAPEAPPLYRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWardrobeSlot'] = _PBMSGWARDROBESLOT
DESCRIPTOR.message_types_by_name['PBMsgRestoreFashionShapeRequest'] = _PBMSGRESTOREFASHIONSHAPEREQUEST
DESCRIPTOR.message_types_by_name['PBMsgRestoreFashionShapeResponse'] = _PBMSGRESTOREFASHIONSHAPERESPONSE
DESCRIPTOR.message_types_by_name['PBMsgEquitWardrobeFashionRequest'] = _PBMSGEQUITWARDROBEFASHIONREQUEST
DESCRIPTOR.message_types_by_name['PBMsgEquitWardrobeFashionResponse'] = _PBMSGEQUITWARDROBEFASHIONRESPONSE
DESCRIPTOR.message_types_by_name['PBMsgWardrobeChangeNotice'] = _PBMSGWARDROBECHANGENOTICE

class PBMsgWardrobeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeRequest)

class PBMsgWardrobeResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBERESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeResponse)

class PBMsgWardrobeFashion(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEFASHION
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeFashion)

class PBMsgWardrobe(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBE
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobe)

class PBMsgWardrobeItem(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEITEM
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeItem)

class PBMsgWardrobeHangUpRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEHANGUPREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeHangUpRequest)

class PBMsgWardrobeHangUpResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEHANGUPRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeHangUpResponse)

class PBMsgWardrobeHangDownRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEHANGDOWNREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeHangDownRequest)

class PBMsgWardrobeHangDownResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEHANGDOWNRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeHangDownResponse)

class PBMsgWardrobeUnlockRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEUNLOCKREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeUnlockRequest)

class PBMsgWardrobeUnlockResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBEUNLOCKRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeUnlockResponse)

class PBMsgFashionShapeApplyRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGFASHIONSHAPEAPPLYREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgFashionShapeApplyRequest)

class PBMsgFashionShapeApplyResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGFASHIONSHAPEAPPLYRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgFashionShapeApplyResponse)

class PBMsgWardrobeSlot(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBESLOT
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeSlot)

class PBMsgRestoreFashionShapeRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGRESTOREFASHIONSHAPEREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgRestoreFashionShapeRequest)

class PBMsgRestoreFashionShapeResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGRESTOREFASHIONSHAPERESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgRestoreFashionShapeResponse)

class PBMsgEquitWardrobeFashionRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGEQUITWARDROBEFASHIONREQUEST
  
  # @@protoc_insertion_point(class_scope:PBMsgEquitWardrobeFashionRequest)

class PBMsgEquitWardrobeFashionResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGEQUITWARDROBEFASHIONRESPONSE
  
  # @@protoc_insertion_point(class_scope:PBMsgEquitWardrobeFashionResponse)

class PBMsgWardrobeChangeNotice(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBMSGWARDROBECHANGENOTICE
  
  # @@protoc_insertion_point(class_scope:PBMsgWardrobeChangeNotice)

# @@protoc_insertion_point(module_scope)