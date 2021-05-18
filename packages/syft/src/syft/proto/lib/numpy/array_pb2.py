# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/lib/numpy/array.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.lib.torch import tensor_pb2 as proto_dot_lib_dot_torch_dot_tensor__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/lib/numpy/array.proto",
    package="syft.lib.numpy",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1bproto/lib/numpy/array.proto\x12\x0esyft.lib.numpy\x1a\x1cproto/lib/torch/tensor.proto"G\n\nNumpyProto\x12*\n\x06tensor\x18\x01 \x01(\x0b\x32\x1a.syft.lib.torch.TensorData\x12\r\n\x05\x64type\x18\x02 \x01(\tb\x06proto3',
    dependencies=[proto_dot_lib_dot_torch_dot_tensor__pb2.DESCRIPTOR,],
)


_NUMPYPROTO = _descriptor.Descriptor(
    name="NumpyProto",
    full_name="syft.lib.numpy.NumpyProto",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="tensor",
            full_name="syft.lib.numpy.NumpyProto.tensor",
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
            name="dtype",
            full_name="syft.lib.numpy.NumpyProto.dtype",
            index=1,
            number=2,
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
    serialized_start=77,
    serialized_end=148,
)

_NUMPYPROTO.fields_by_name[
    "tensor"
].message_type = proto_dot_lib_dot_torch_dot_tensor__pb2._TENSORDATA
DESCRIPTOR.message_types_by_name["NumpyProto"] = _NUMPYPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NumpyProto = _reflection.GeneratedProtocolMessageType(
    "NumpyProto",
    (_message.Message,),
    {
        "DESCRIPTOR": _NUMPYPROTO,
        "__module__": "proto.lib.numpy.array_pb2"
        # @@protoc_insertion_point(class_scope:syft.lib.numpy.NumpyProto)
    },
)
_sym_db.RegisterMessage(NumpyProto)


# @@protoc_insertion_point(module_scope)
