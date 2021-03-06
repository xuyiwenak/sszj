# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import tmpl_base_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='tmpl_interaction.proto',
  package='',
  serialized_pb='\n\x16tmpl_interaction.proto\x1a\x0ftmpl_base.proto\"B\n\x13PBInteractionConfig\x12+\n\x10interaction_list\x18\x01 \x03(\x0b\x32\x11.PBOneInteraction\"\xac\x01\n\x10PBOneInteraction\x12\x11\n\taction_id\x18\x01 \x01(\x11\x12*\n\nlogic_data\x18\x02 \x01(\x0b\x32\x16.PBOneInteractionLogic\x12,\n\x0b\x63lient_data\x18\x03 \x01(\x0b\x32\x17.PBOneInteractionClient\x12+\n\x0e\x63lient_ui_data\x18\x04 \x01(\x0b\x32\x13.PBOneInteractionUI\"\xc4\x01\n\x15PBOneInteractionLogic\x12\x0c\n\x04type\x18\x01 \x01(\x11\x12\x15\n\raffect_target\x18\x02 \x01(\x08\x12\x10\n\x08sys_mode\x18\x03 \x01(\x11\x12\n\n\x02\x63\x64\x18\x04 \x01(\x11\x12\x0b\n\x03\x64is\x18\x05 \x01(\x02\x12\x1a\n\x12src_sys_prompt_key\x18\x06 \x01(\t\x12\x1a\n\x12tar_sys_prompt_key\x18\x07 \x01(\t\x12\x11\n\tis_notice\x18\x08 \x01(\x08\x12\x10\n\x08is_lover\x18\t \x01(\x08\"\xc3\x02\n\x16PBOneInteractionClient\x12\x12\n\nclient_dis\x18\x01 \x01(\x02\x12\x10\n\x08\x64ir_type\x18\x02 \x01(\x11\x12\x16\n\x0esrc_sta_afx_id\x18\x03 \x01(\x11\x12\x17\n\x0fsrc_loop_afx_id\x18\x04 \x01(\x11\x12\x1a\n\x12src_only_anim_loop\x18\x05 \x01(\x08\x12\x16\n\x0etar_sta_afx_id\x18\x06 \x01(\x11\x12\x17\n\x0ftar_loop_afx_id\x18\x07 \x01(\x11\x12\x1a\n\x12tar_only_anim_loop\x18\x08 \x01(\x08\x12\x1b\n\x13\x64\x65lete_fx_when_over\x18\t \x01(\x08\x12\x11\n\tforce_dis\x18\n \x01(\x02\x12\x11\n\tlast_time\x18\x0b \x01(\x02\x12\x13\n\x0bhide_weapon\x18\x0c \x01(\x08\x12\x11\n\thide_wing\x18\r \x01(\x08\"3\n\x12PBOneInteractionUI\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07picture\x18\x02 \x01(\t')




_PBINTERACTIONCONFIG = descriptor.Descriptor(
  name='PBInteractionConfig',
  full_name='PBInteractionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='interaction_list', full_name='PBInteractionConfig.interaction_list', index=0,
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
  serialized_start=43,
  serialized_end=109,
)


_PBONEINTERACTION = descriptor.Descriptor(
  name='PBOneInteraction',
  full_name='PBOneInteraction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='action_id', full_name='PBOneInteraction.action_id', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='logic_data', full_name='PBOneInteraction.logic_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='client_data', full_name='PBOneInteraction.client_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='client_ui_data', full_name='PBOneInteraction.client_ui_data', index=3,
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
  serialized_start=112,
  serialized_end=284,
)


_PBONEINTERACTIONLOGIC = descriptor.Descriptor(
  name='PBOneInteractionLogic',
  full_name='PBOneInteractionLogic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='type', full_name='PBOneInteractionLogic.type', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='affect_target', full_name='PBOneInteractionLogic.affect_target', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='sys_mode', full_name='PBOneInteractionLogic.sys_mode', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='cd', full_name='PBOneInteractionLogic.cd', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dis', full_name='PBOneInteractionLogic.dis', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='src_sys_prompt_key', full_name='PBOneInteractionLogic.src_sys_prompt_key', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tar_sys_prompt_key', full_name='PBOneInteractionLogic.tar_sys_prompt_key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_notice', full_name='PBOneInteractionLogic.is_notice', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='is_lover', full_name='PBOneInteractionLogic.is_lover', index=8,
      number=9, type=8, cpp_type=7, label=1,
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
  serialized_start=287,
  serialized_end=483,
)


_PBONEINTERACTIONCLIENT = descriptor.Descriptor(
  name='PBOneInteractionClient',
  full_name='PBOneInteractionClient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='client_dis', full_name='PBOneInteractionClient.client_dis', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='dir_type', full_name='PBOneInteractionClient.dir_type', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='src_sta_afx_id', full_name='PBOneInteractionClient.src_sta_afx_id', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='src_loop_afx_id', full_name='PBOneInteractionClient.src_loop_afx_id', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='src_only_anim_loop', full_name='PBOneInteractionClient.src_only_anim_loop', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tar_sta_afx_id', full_name='PBOneInteractionClient.tar_sta_afx_id', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tar_loop_afx_id', full_name='PBOneInteractionClient.tar_loop_afx_id', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='tar_only_anim_loop', full_name='PBOneInteractionClient.tar_only_anim_loop', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='delete_fx_when_over', full_name='PBOneInteractionClient.delete_fx_when_over', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='force_dis', full_name='PBOneInteractionClient.force_dis', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='last_time', full_name='PBOneInteractionClient.last_time', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hide_weapon', full_name='PBOneInteractionClient.hide_weapon', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hide_wing', full_name='PBOneInteractionClient.hide_wing', index=12,
      number=13, type=8, cpp_type=7, label=1,
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
  serialized_start=486,
  serialized_end=809,
)


_PBONEINTERACTIONUI = descriptor.Descriptor(
  name='PBOneInteractionUI',
  full_name='PBOneInteractionUI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='PBOneInteractionUI.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='picture', full_name='PBOneInteractionUI.picture', index=1,
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
  serialized_start=811,
  serialized_end=862,
)

_PBINTERACTIONCONFIG.fields_by_name['interaction_list'].message_type = _PBONEINTERACTION
_PBONEINTERACTION.fields_by_name['logic_data'].message_type = _PBONEINTERACTIONLOGIC
_PBONEINTERACTION.fields_by_name['client_data'].message_type = _PBONEINTERACTIONCLIENT
_PBONEINTERACTION.fields_by_name['client_ui_data'].message_type = _PBONEINTERACTIONUI
DESCRIPTOR.message_types_by_name['PBInteractionConfig'] = _PBINTERACTIONCONFIG
DESCRIPTOR.message_types_by_name['PBOneInteraction'] = _PBONEINTERACTION
DESCRIPTOR.message_types_by_name['PBOneInteractionLogic'] = _PBONEINTERACTIONLOGIC
DESCRIPTOR.message_types_by_name['PBOneInteractionClient'] = _PBONEINTERACTIONCLIENT
DESCRIPTOR.message_types_by_name['PBOneInteractionUI'] = _PBONEINTERACTIONUI

class PBInteractionConfig(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBINTERACTIONCONFIG
  
  # @@protoc_insertion_point(class_scope:PBInteractionConfig)

class PBOneInteraction(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONEINTERACTION
  
  # @@protoc_insertion_point(class_scope:PBOneInteraction)

class PBOneInteractionLogic(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONEINTERACTIONLOGIC
  
  # @@protoc_insertion_point(class_scope:PBOneInteractionLogic)

class PBOneInteractionClient(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONEINTERACTIONCLIENT
  
  # @@protoc_insertion_point(class_scope:PBOneInteractionClient)

class PBOneInteractionUI(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBONEINTERACTIONUI
  
  # @@protoc_insertion_point(class_scope:PBOneInteractionUI)

# @@protoc_insertion_point(module_scope)
