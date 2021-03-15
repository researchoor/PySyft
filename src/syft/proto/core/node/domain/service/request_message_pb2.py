# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/core/node/domain/service/request_message.proto

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
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/core/node/domain/service/request_message.proto",
    package="syft.core.node.domain.service",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n4proto/core/node/domain/service/request_message.proto\x12\x1dsyft.core.node.domain.service\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto"\xbd\x02\n\x0eRequestMessage\x12)\n\nrequest_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12(\n\tobject_id\x18\x02 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x13\n\x0bobject_tags\x18\x03 \x03(\t\x12\x1b\n\x13request_description\x18\x04 \x01(\t\x12-\n\x0etarget_address\x18\x05 \x01(\x0b\x32\x15.syft.core.io.Address\x12,\n\rowner_address\x18\x06 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x1c\n\x14requester_verify_key\x18\x07 \x01(\x0c\x12\x14\n\x0ctimeout_secs\x18\x08 \x01(\x05\x12\x13\n\x0bobject_type\x18\t \x01(\tb\x06proto3',
    dependencies=[
        proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_REQUESTMESSAGE = _descriptor.Descriptor(
    name="RequestMessage",
    full_name="syft.core.node.domain.service.RequestMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="request_id",
            full_name="syft.core.node.domain.service.RequestMessage.request_id",
            index=0,
            number=1,
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
            name="object_id",
            full_name="syft.core.node.domain.service.RequestMessage.object_id",
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
            name="object_tags",
            full_name="syft.core.node.domain.service.RequestMessage.object_tags",
            index=2,
            number=3,
            type=9,
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
            name="request_description",
            full_name="syft.core.node.domain.service.RequestMessage.request_description",
            index=3,
            number=4,
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
            name="target_address",
            full_name="syft.core.node.domain.service.RequestMessage.target_address",
            index=4,
            number=5,
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
            name="owner_address",
            full_name="syft.core.node.domain.service.RequestMessage.owner_address",
            index=5,
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
            name="requester_verify_key",
            full_name="syft.core.node.domain.service.RequestMessage.requester_verify_key",
            index=6,
            number=7,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
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
            name="timeout_secs",
            full_name="syft.core.node.domain.service.RequestMessage.timeout_secs",
            index=7,
            number=8,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="object_type",
            full_name="syft.core.node.domain.service.RequestMessage.object_type",
            index=8,
            number=9,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=156,
    serialized_end=473,
)

_REQUESTMESSAGE.fields_by_name[
    "request_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_REQUESTMESSAGE.fields_by_name[
    "object_id"
].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_REQUESTMESSAGE.fields_by_name[
    "target_address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_REQUESTMESSAGE.fields_by_name[
    "owner_address"
].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name["RequestMessage"] = _REQUESTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestMessage = _reflection.GeneratedProtocolMessageType(
    "RequestMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _REQUESTMESSAGE,
        "__module__": "proto.core.node.domain.service.request_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.domain.service.RequestMessage)
    },
)
_sym_db.RegisterMessage(RequestMessage)


# @@protoc_insertion_point(module_scope)
