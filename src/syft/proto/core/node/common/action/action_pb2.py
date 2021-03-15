# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/common/action/action.proto

# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.node.common.action import (
    garbage_collect_object_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_garbage__collect__object__pb2,
)
from syft.proto.core.node.common.action import (
    get_enum_attribute_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_get__enum__attribute__pb2,
)
from syft.proto.core.node.common.action import (
    get_object_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_get__object__pb2,
)
from syft.proto.core.node.common.action import (
    get_set_property_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_get__set__property__pb2,
)
from syft.proto.core.node.common.action import (
    get_set_static_attribute_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_get__set__static__attribute__pb2,
)
from syft.proto.core.node.common.action import (
    run_class_method_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_run__class__method__pb2,
)
from syft.proto.core.node.common.action import (
    run_function_or_constructor_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_run__function__or__constructor__pb2,
)
from syft.proto.core.node.common.action import (
    save_object_pb2 as proto_dot_core_dot_node_dot_common_dot_action_dot_save__object__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/node/common/action/action.proto",
    package="syft.core.node.common.action",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n*proto/core/node/common/action/action.proto\x12\x1csyft.core.node.common.action\x1a.proto/core/node/common/action/get_object.proto\x1a?proto/core/node/common/action/run_function_or_constructor.proto\x1a\x34proto/core/node/common/action/run_class_method.proto\x1a:proto/core/node/common/action/garbage_collect_object.proto\x1a\x36proto/core/node/common/action/get_enum_attribute.proto\x1a\x34proto/core/node/common/action/get_set_property.proto\x1a<proto/core/node/common/action/get_set_static_attribute.proto\x1a/proto/core/node/common/action/save_object.proto"\xfd\x05\n\x06\x41\x63tion\x12\x10\n\x08obj_type\x18\x01 \x01(\t\x12J\n\x11get_object_action\x18\x02 \x01(\x0b\x32-.syft.core.node.common.action.GetObjectActionH\x00\x12j\n"run_function_or_constructor_action\x18\x03 \x01(\x0b\x32<.syft.core.node.common.action.RunFunctionOrConstructorActionH\x00\x12U\n\x17run_class_method_action\x18\x04 \x01(\x0b\x32\x32.syft.core.node.common.action.RunClassMethodActionH\x00\x12\x61\n\x1dgarbage_collect_object_action\x18\x06 \x01(\x0b\x32\x38.syft.core.node.common.action.GarbageCollectObjectActionH\x00\x12U\n\x15\x65num_attribute_action\x18\x07 \x01(\x0b\x32\x34.syft.core.node.common.action.GetEnumAttributeActionH\x00\x12Z\n\x1aget_or_set_property_action\x18\x08 \x01(\x0b\x32\x34.syft.core.node.common.action.GetOrSetPropertyActionH\x00\x12\x64\n\x1fget_set_static_attribute_action\x18\t \x01(\x0b\x32\x39.syft.core.node.common.action.GetSetStaticAttributeActionH\x00\x12L\n\x12save_object_action\x18\n \x01(\x0b\x32..syft.core.node.common.action.SaveObjectActionH\x00\x42\x08\n\x06\x61\x63tionb\x06proto3',
    dependencies=[
        proto_dot_core_dot_node_dot_common_dot_action_dot_get__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_node_dot_common_dot_action_dot_run__function__or__constructor__pb2.DESCRIPTOR,
        proto_dot_core_dot_node_dot_common_dot_action_dot_run__class__method__pb2.DESCRIPTOR,
        proto_dot_core_dot_node_dot_common_dot_action_dot_garbage__collect__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_node_dot_common_dot_action_dot_get__enum__attribute__pb2.DESCRIPTOR,
        proto_dot_core_dot_node_dot_common_dot_action_dot_get__set__property__pb2.DESCRIPTOR,
        proto_dot_core_dot_node_dot_common_dot_action_dot_get__set__static__attribute__pb2.DESCRIPTOR,
        proto_dot_core_dot_node_dot_common_dot_action_dot_save__object__pb2.DESCRIPTOR,
    ],
)


_ACTION = _descriptor.Descriptor(
    name="Action",
    full_name="syft.core.node.common.action.Action",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="obj_type",
            full_name="syft.core.node.common.action.Action.obj_type",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="get_object_action",
            full_name="syft.core.node.common.action.Action.get_object_action",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="run_function_or_constructor_action",
            full_name="syft.core.node.common.action.Action.run_function_or_constructor_action",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="run_class_method_action",
            full_name="syft.core.node.common.action.Action.run_class_method_action",
            index=3,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="garbage_collect_object_action",
            full_name="syft.core.node.common.action.Action.garbage_collect_object_action",
            index=4,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="enum_attribute_action",
            full_name="syft.core.node.common.action.Action.enum_attribute_action",
            index=5,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="get_or_set_property_action",
            full_name="syft.core.node.common.action.Action.get_or_set_property_action",
            index=6,
            number=8,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="get_set_static_attribute_action",
            full_name="syft.core.node.common.action.Action.get_set_static_attribute_action",
            index=7,
            number=9,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="save_object_action",
            full_name="syft.core.node.common.action.Action.save_object_action",
            index=8,
            number=10,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="action",
            full_name="syft.core.node.common.action.Action.action",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=525,
    serialized_end=1290,
)

_ACTION.fields_by_name[
    "get_object_action"
].message_type = (
    proto_dot_core_dot_node_dot_common_dot_action_dot_get__object__pb2._GETOBJECTACTION
)
_ACTION.fields_by_name[
    "run_function_or_constructor_action"
].message_type = (
    proto_dot_core_dot_node_dot_common_dot_action_dot_run__function__or__constructor__pb2._RUNFUNCTIONORCONSTRUCTORACTION
)
_ACTION.fields_by_name[
    "run_class_method_action"
].message_type = (
    proto_dot_core_dot_node_dot_common_dot_action_dot_run__class__method__pb2._RUNCLASSMETHODACTION
)
_ACTION.fields_by_name[
    "garbage_collect_object_action"
].message_type = (
    proto_dot_core_dot_node_dot_common_dot_action_dot_garbage__collect__object__pb2._GARBAGECOLLECTOBJECTACTION
)
_ACTION.fields_by_name[
    "enum_attribute_action"
].message_type = (
    proto_dot_core_dot_node_dot_common_dot_action_dot_get__enum__attribute__pb2._GETENUMATTRIBUTEACTION
)
_ACTION.fields_by_name[
    "get_or_set_property_action"
].message_type = (
    proto_dot_core_dot_node_dot_common_dot_action_dot_get__set__property__pb2._GETORSETPROPERTYACTION
)
_ACTION.fields_by_name[
    "get_set_static_attribute_action"
].message_type = (
    proto_dot_core_dot_node_dot_common_dot_action_dot_get__set__static__attribute__pb2._GETSETSTATICATTRIBUTEACTION
)
_ACTION.fields_by_name[
    "save_object_action"
].message_type = (
    proto_dot_core_dot_node_dot_common_dot_action_dot_save__object__pb2._SAVEOBJECTACTION
)
_ACTION.oneofs_by_name["action"].fields.append(
    _ACTION.fields_by_name["get_object_action"]
)
_ACTION.fields_by_name["get_object_action"].containing_oneof = _ACTION.oneofs_by_name[
    "action"
]
_ACTION.oneofs_by_name["action"].fields.append(
    _ACTION.fields_by_name["run_function_or_constructor_action"]
)
_ACTION.fields_by_name[
    "run_function_or_constructor_action"
].containing_oneof = _ACTION.oneofs_by_name["action"]
_ACTION.oneofs_by_name["action"].fields.append(
    _ACTION.fields_by_name["run_class_method_action"]
)
_ACTION.fields_by_name[
    "run_class_method_action"
].containing_oneof = _ACTION.oneofs_by_name["action"]
_ACTION.oneofs_by_name["action"].fields.append(
    _ACTION.fields_by_name["garbage_collect_object_action"]
)
_ACTION.fields_by_name[
    "garbage_collect_object_action"
].containing_oneof = _ACTION.oneofs_by_name["action"]
_ACTION.oneofs_by_name["action"].fields.append(
    _ACTION.fields_by_name["enum_attribute_action"]
)
_ACTION.fields_by_name[
    "enum_attribute_action"
].containing_oneof = _ACTION.oneofs_by_name["action"]
_ACTION.oneofs_by_name["action"].fields.append(
    _ACTION.fields_by_name["get_or_set_property_action"]
)
_ACTION.fields_by_name[
    "get_or_set_property_action"
].containing_oneof = _ACTION.oneofs_by_name["action"]
_ACTION.oneofs_by_name["action"].fields.append(
    _ACTION.fields_by_name["get_set_static_attribute_action"]
)
_ACTION.fields_by_name[
    "get_set_static_attribute_action"
].containing_oneof = _ACTION.oneofs_by_name["action"]
_ACTION.oneofs_by_name["action"].fields.append(
    _ACTION.fields_by_name["save_object_action"]
)
_ACTION.fields_by_name["save_object_action"].containing_oneof = _ACTION.oneofs_by_name[
    "action"
]
DESCRIPTOR.message_types_by_name["Action"] = _ACTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Action = _reflection.GeneratedProtocolMessageType(
    "Action",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTION,
        "__module__": "proto.core.node.common.action.action_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.action.Action)
    },
)
_sym_db.RegisterMessage(Action)


# @@protoc_insertion_point(module_scope)
