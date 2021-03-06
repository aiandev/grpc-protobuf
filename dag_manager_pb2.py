# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dag_manager.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dag_manager.proto',
  package='dagmanagerpb',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x64\x61g_manager.proto\x12\x0c\x64\x61gmanagerpb\"\x11\n\x0f\x43urveDagRequest\"\x1c\n\x08\x43urveDag\x12\x10\n\x08\x64\x61g_name\x18\x01 \x01(\t\"4\n\tDagParams\x12\x12\n\nparam_name\x18\x01 \x01(\t\x12\x13\n\x0bparam_value\x18\x02 \x03(\t\">\n\x17GetAllCurveDagsResponse\x12#\n\x03\x64\x61g\x18\x01 \x03(\x0b\x32\x16.dagmanagerpb.CurveDag2g\n\nDagService\x12Y\n\x0fGetAllCurveDags\x12\x1d.dagmanagerpb.CurveDagRequest\x1a%.dagmanagerpb.GetAllCurveDagsResponse\"\x00\x62\x06proto3')
)




_CURVEDAGREQUEST = _descriptor.Descriptor(
  name='CurveDagRequest',
  full_name='dagmanagerpb.CurveDagRequest',
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=52,
)


_CURVEDAG = _descriptor.Descriptor(
  name='CurveDag',
  full_name='dagmanagerpb.CurveDag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dag_name', full_name='dagmanagerpb.CurveDag.dag_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=82,
)


_DAGPARAMS = _descriptor.Descriptor(
  name='DagParams',
  full_name='dagmanagerpb.DagParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='param_name', full_name='dagmanagerpb.DagParams.param_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='param_value', full_name='dagmanagerpb.DagParams.param_value', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=136,
)


_GETALLCURVEDAGSRESPONSE = _descriptor.Descriptor(
  name='GetAllCurveDagsResponse',
  full_name='dagmanagerpb.GetAllCurveDagsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dag', full_name='dagmanagerpb.GetAllCurveDagsResponse.dag', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=138,
  serialized_end=200,
)

_GETALLCURVEDAGSRESPONSE.fields_by_name['dag'].message_type = _CURVEDAG
DESCRIPTOR.message_types_by_name['CurveDagRequest'] = _CURVEDAGREQUEST
DESCRIPTOR.message_types_by_name['CurveDag'] = _CURVEDAG
DESCRIPTOR.message_types_by_name['DagParams'] = _DAGPARAMS
DESCRIPTOR.message_types_by_name['GetAllCurveDagsResponse'] = _GETALLCURVEDAGSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CurveDagRequest = _reflection.GeneratedProtocolMessageType('CurveDagRequest', (_message.Message,), dict(
  DESCRIPTOR = _CURVEDAGREQUEST,
  __module__ = 'dag_manager_pb2'
  # @@protoc_insertion_point(class_scope:dagmanagerpb.CurveDagRequest)
  ))
_sym_db.RegisterMessage(CurveDagRequest)

CurveDag = _reflection.GeneratedProtocolMessageType('CurveDag', (_message.Message,), dict(
  DESCRIPTOR = _CURVEDAG,
  __module__ = 'dag_manager_pb2'
  # @@protoc_insertion_point(class_scope:dagmanagerpb.CurveDag)
  ))
_sym_db.RegisterMessage(CurveDag)

DagParams = _reflection.GeneratedProtocolMessageType('DagParams', (_message.Message,), dict(
  DESCRIPTOR = _DAGPARAMS,
  __module__ = 'dag_manager_pb2'
  # @@protoc_insertion_point(class_scope:dagmanagerpb.DagParams)
  ))
_sym_db.RegisterMessage(DagParams)

GetAllCurveDagsResponse = _reflection.GeneratedProtocolMessageType('GetAllCurveDagsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALLCURVEDAGSRESPONSE,
  __module__ = 'dag_manager_pb2'
  # @@protoc_insertion_point(class_scope:dagmanagerpb.GetAllCurveDagsResponse)
  ))
_sym_db.RegisterMessage(GetAllCurveDagsResponse)



_DAGSERVICE = _descriptor.ServiceDescriptor(
  name='DagService',
  full_name='dagmanagerpb.DagService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=202,
  serialized_end=305,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllCurveDags',
    full_name='dagmanagerpb.DagService.GetAllCurveDags',
    index=0,
    containing_service=None,
    input_type=_CURVEDAGREQUEST,
    output_type=_GETALLCURVEDAGSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DAGSERVICE)

DESCRIPTOR.services_by_name['DagService'] = _DAGSERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class DagServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetAllCurveDags = channel.unary_unary(
          '/dagmanagerpb.DagService/GetAllCurveDags',
          request_serializer=CurveDagRequest.SerializeToString,
          response_deserializer=GetAllCurveDagsResponse.FromString,
          )


  class DagServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def GetAllCurveDags(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_DagServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetAllCurveDags': grpc.unary_unary_rpc_method_handler(
            servicer.GetAllCurveDags,
            request_deserializer=CurveDagRequest.FromString,
            response_serializer=GetAllCurveDagsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'dagmanagerpb.DagService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaDagServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetAllCurveDags(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaDagServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def GetAllCurveDags(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    GetAllCurveDags.future = None


  def beta_create_DagService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('dagmanagerpb.DagService', 'GetAllCurveDags'): CurveDagRequest.FromString,
    }
    response_serializers = {
      ('dagmanagerpb.DagService', 'GetAllCurveDags'): GetAllCurveDagsResponse.SerializeToString,
    }
    method_implementations = {
      ('dagmanagerpb.DagService', 'GetAllCurveDags'): face_utilities.unary_unary_inline(servicer.GetAllCurveDags),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_DagService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('dagmanagerpb.DagService', 'GetAllCurveDags'): CurveDagRequest.SerializeToString,
    }
    response_deserializers = {
      ('dagmanagerpb.DagService', 'GetAllCurveDags'): GetAllCurveDagsResponse.FromString,
    }
    cardinalities = {
      'GetAllCurveDags': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'dagmanagerpb.DagService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
