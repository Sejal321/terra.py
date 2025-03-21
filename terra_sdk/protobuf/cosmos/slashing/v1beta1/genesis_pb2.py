# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/slashing/v1beta1/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.slashing.v1beta1 import (
    slashing_pb2 as cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2,
)
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmos/slashing/v1beta1/genesis.proto",
    package="cosmos.slashing.v1beta1",
    syntax="proto3",
    serialized_options=b"Z-github.com/cosmos/cosmos-sdk/x/slashing/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n%cosmos/slashing/v1beta1/genesis.proto\x12\x17\x63osmos.slashing.v1beta1\x1a\x14gogoproto/gogo.proto\x1a&cosmos/slashing/v1beta1/slashing.proto"\x85\x02\n\x0cGenesisState\x12\x35\n\x06params\x18\x01 \x01(\x0b\x32\x1f.cosmos.slashing.v1beta1.ParamsB\x04\xc8\xde\x1f\x00\x12Y\n\rsigning_infos\x18\x02 \x03(\x0b\x32$.cosmos.slashing.v1beta1.SigningInfoB\x1c\xf2\xde\x1f\x14yaml:"signing_infos"\xc8\xde\x1f\x00\x12\x63\n\rmissed_blocks\x18\x03 \x03(\x0b\x32..cosmos.slashing.v1beta1.ValidatorMissedBlocksB\x1c\xf2\xde\x1f\x14yaml:"missed_blocks"\xc8\xde\x1f\x00"\x94\x01\n\x0bSigningInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12t\n\x16validator_signing_info\x18\x02 \x01(\x0b\x32-.cosmos.slashing.v1beta1.ValidatorSigningInfoB%\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"validator_signing_info""\x83\x01\n\x15ValidatorMissedBlocks\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12Y\n\rmissed_blocks\x18\x02 \x03(\x0b\x32$.cosmos.slashing.v1beta1.MissedBlockB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"missed_blocks"",\n\x0bMissedBlock\x12\r\n\x05index\x18\x01 \x01(\x03\x12\x0e\n\x06missed\x18\x02 \x01(\x08\x42/Z-github.com/cosmos/cosmos-sdk/x/slashing/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2.DESCRIPTOR,
    ],
)


_GENESISSTATE = _descriptor.Descriptor(
    name="GenesisState",
    full_name="cosmos.slashing.v1beta1.GenesisState",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="params",
            full_name="cosmos.slashing.v1beta1.GenesisState.params",
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
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="signing_infos",
            full_name="cosmos.slashing.v1beta1.GenesisState.signing_infos",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\024yaml:"signing_infos"\310\336\037\000',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="missed_blocks",
            full_name="cosmos.slashing.v1beta1.GenesisState.missed_blocks",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\024yaml:"missed_blocks"\310\336\037\000',
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
    serialized_start=129,
    serialized_end=390,
)


_SIGNINGINFO = _descriptor.Descriptor(
    name="SigningInfo",
    full_name="cosmos.slashing.v1beta1.SigningInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="address",
            full_name="cosmos.slashing.v1beta1.SigningInfo.address",
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
            name="validator_signing_info",
            full_name="cosmos.slashing.v1beta1.SigningInfo.validator_signing_info",
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
            serialized_options=b'\310\336\037\000\362\336\037\035yaml:"validator_signing_info"',
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
    serialized_start=393,
    serialized_end=541,
)


_VALIDATORMISSEDBLOCKS = _descriptor.Descriptor(
    name="ValidatorMissedBlocks",
    full_name="cosmos.slashing.v1beta1.ValidatorMissedBlocks",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="address",
            full_name="cosmos.slashing.v1beta1.ValidatorMissedBlocks.address",
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
            name="missed_blocks",
            full_name="cosmos.slashing.v1beta1.ValidatorMissedBlocks.missed_blocks",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\310\336\037\000\362\336\037\024yaml:"missed_blocks"',
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
    serialized_start=544,
    serialized_end=675,
)


_MISSEDBLOCK = _descriptor.Descriptor(
    name="MissedBlock",
    full_name="cosmos.slashing.v1beta1.MissedBlock",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="index",
            full_name="cosmos.slashing.v1beta1.MissedBlock.index",
            index=0,
            number=1,
            type=3,
            cpp_type=2,
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
            name="missed",
            full_name="cosmos.slashing.v1beta1.MissedBlock.missed",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    serialized_start=677,
    serialized_end=721,
)

_GENESISSTATE.fields_by_name[
    "params"
].message_type = cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2._PARAMS
_GENESISSTATE.fields_by_name["signing_infos"].message_type = _SIGNINGINFO
_GENESISSTATE.fields_by_name["missed_blocks"].message_type = _VALIDATORMISSEDBLOCKS
_SIGNINGINFO.fields_by_name[
    "validator_signing_info"
].message_type = cosmos_dot_slashing_dot_v1beta1_dot_slashing__pb2._VALIDATORSIGNINGINFO
_VALIDATORMISSEDBLOCKS.fields_by_name["missed_blocks"].message_type = _MISSEDBLOCK
DESCRIPTOR.message_types_by_name["GenesisState"] = _GENESISSTATE
DESCRIPTOR.message_types_by_name["SigningInfo"] = _SIGNINGINFO
DESCRIPTOR.message_types_by_name["ValidatorMissedBlocks"] = _VALIDATORMISSEDBLOCKS
DESCRIPTOR.message_types_by_name["MissedBlock"] = _MISSEDBLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenesisState = _reflection.GeneratedProtocolMessageType(
    "GenesisState",
    (_message.Message,),
    {
        "DESCRIPTOR": _GENESISSTATE,
        "__module__": "cosmos.slashing.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.GenesisState)
    },
)
_sym_db.RegisterMessage(GenesisState)

SigningInfo = _reflection.GeneratedProtocolMessageType(
    "SigningInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIGNINGINFO,
        "__module__": "cosmos.slashing.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.SigningInfo)
    },
)
_sym_db.RegisterMessage(SigningInfo)

ValidatorMissedBlocks = _reflection.GeneratedProtocolMessageType(
    "ValidatorMissedBlocks",
    (_message.Message,),
    {
        "DESCRIPTOR": _VALIDATORMISSEDBLOCKS,
        "__module__": "cosmos.slashing.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.ValidatorMissedBlocks)
    },
)
_sym_db.RegisterMessage(ValidatorMissedBlocks)

MissedBlock = _reflection.GeneratedProtocolMessageType(
    "MissedBlock",
    (_message.Message,),
    {
        "DESCRIPTOR": _MISSEDBLOCK,
        "__module__": "cosmos.slashing.v1beta1.genesis_pb2"
        # @@protoc_insertion_point(class_scope:cosmos.slashing.v1beta1.MissedBlock)
    },
)
_sym_db.RegisterMessage(MissedBlock)


DESCRIPTOR._options = None
_GENESISSTATE.fields_by_name["params"]._options = None
_GENESISSTATE.fields_by_name["signing_infos"]._options = None
_GENESISSTATE.fields_by_name["missed_blocks"]._options = None
_SIGNINGINFO.fields_by_name["validator_signing_info"]._options = None
_VALIDATORMISSEDBLOCKS.fields_by_name["missed_blocks"]._options = None
# @@protoc_insertion_point(module_scope)
