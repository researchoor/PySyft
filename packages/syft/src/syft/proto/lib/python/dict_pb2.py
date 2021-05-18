# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/python/dict.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/python/dict.proto",
    package="syft.lib.python",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1bproto/lib/python/dict.proto\x12\x0fsyft.lib.python\x1a%proto/core/common/common_object.proto"G\n\x04\x44ict\x12\x0c\n\x04keys\x18\x01 \x03(\x0c\x12\x0e\n\x06values\x18\x02 \x03(\x0c\x12!\n\x02id\x18\x03 \x01(\x0b\x32\x15.syft.core.common.UIDb\x06proto3',
    dependencies=[proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,],
)


_DICT = _descriptor.Descriptor(
    name="Dict",
    full_name="syft.lib.python.Dict",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="keys",
            full_name="syft.lib.python.Dict.keys",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="values",
            full_name="syft.lib.python.Dict.values",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
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
            name="id",
            full_name="syft.lib.python.Dict.id",
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=87,
    serialized_end=158,
)

_DICT.fields_by_name[
    "id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
DESCRIPTOR.message_types_by_name["Dict"] = _DICT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dict = _reflection.GeneratedProtocolMessageType(
    "Dict",
    (_message.Message,),
    {
        "DESCRIPTOR": _DICT,
        "__module__": "proto.lib.python.dict_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.python.Dict)
    },
)
_sym_db.RegisterMessage(Dict)


# @@protoc_insertion_point(module_scope)
