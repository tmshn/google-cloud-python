# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/cloudtrace_v2/proto/tracing.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.trace_v2.proto import trace_pb2 as google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/cloudtrace_v2/proto/tracing.proto',
  package='google.devtools.cloudtrace.v2',
  syntax='proto3',
  serialized_pb=_b('\n1google/devtools/cloudtrace_v2/proto/tracing.proto\x12\x1dgoogle.devtools.cloudtrace.v2\x1a\x1cgoogle/api/annotations.proto\x1a/google/devtools/cloudtrace_v2/proto/trace.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"Z\n\x16\x42\x61tchWriteSpansRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x32\n\x05spans\x18\x02 \x03(\x0b\x32#.google.devtools.cloudtrace.v2.Span2\xaf\x02\n\x0cTraceService\x12\x94\x01\n\x0f\x42\x61tchWriteSpans\x12\x35.google.devtools.cloudtrace.v2.BatchWriteSpansRequest\x1a\x16.google.protobuf.Empty\"2\x82\xd3\xe4\x93\x02,\"\'/v2/{name=projects/*}/traces:batchWrite:\x01*\x12\x87\x01\n\nCreateSpan\x12#.google.devtools.cloudtrace.v2.Span\x1a#.google.devtools.cloudtrace.v2.Span\"/\x82\xd3\xe4\x93\x02)\"$/v2/{name=projects/*/traces/*}/spans:\x01*B\xac\x01\n!com.google.devtools.cloudtrace.v2B\x0cTracingProtoP\x01ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v2;cloudtrace\xaa\x02\x15Google.Cloud.Trace.V2\xca\x02\x15Google\\Cloud\\Trace\\V2b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_BATCHWRITESPANSREQUEST = _descriptor.Descriptor(
  name='BatchWriteSpansRequest',
  full_name='google.devtools.cloudtrace.v2.BatchWriteSpansRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.devtools.cloudtrace.v2.BatchWriteSpansRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spans', full_name='google.devtools.cloudtrace.v2.BatchWriteSpansRequest.spans', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=225,
  serialized_end=315,
)

_BATCHWRITESPANSREQUEST.fields_by_name['spans'].message_type = google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2._SPAN
DESCRIPTOR.message_types_by_name['BatchWriteSpansRequest'] = _BATCHWRITESPANSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BatchWriteSpansRequest = _reflection.GeneratedProtocolMessageType('BatchWriteSpansRequest', (_message.Message,), dict(
  DESCRIPTOR = _BATCHWRITESPANSREQUEST,
  __module__ = 'google.devtools.cloudtrace_v2.proto.tracing_pb2'
  ,
  __doc__ = """The request message for the ``BatchWriteSpans`` method.
  
  
  Attributes:
      name:
          Required. The name of the project where the spans belong. The
          format is ``projects/[PROJECT_ID]``.
      spans:
          A list of new spans. The span names must not match existing
          spans, or the results are undefined.
  """,
  # @@protoc_insertion_point(class_scope:google.devtools.cloudtrace.v2.BatchWriteSpansRequest)
  ))
_sym_db.RegisterMessage(BatchWriteSpansRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n!com.google.devtools.cloudtrace.v2B\014TracingProtoP\001ZGgoogle.golang.org/genproto/googleapis/devtools/cloudtrace/v2;cloudtrace\252\002\025Google.Cloud.Trace.V2\312\002\025Google\\Cloud\\Trace\\V2'))

_TRACESERVICE = _descriptor.ServiceDescriptor(
  name='TraceService',
  full_name='google.devtools.cloudtrace.v2.TraceService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=318,
  serialized_end=621,
  methods=[
  _descriptor.MethodDescriptor(
    name='BatchWriteSpans',
    full_name='google.devtools.cloudtrace.v2.TraceService.BatchWriteSpans',
    index=0,
    containing_service=None,
    input_type=_BATCHWRITESPANSREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002,\"\'/v2/{name=projects/*}/traces:batchWrite:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='CreateSpan',
    full_name='google.devtools.cloudtrace.v2.TraceService.CreateSpan',
    index=1,
    containing_service=None,
    input_type=google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2._SPAN,
    output_type=google_dot_devtools_dot_cloudtrace__v2_dot_proto_dot_trace__pb2._SPAN,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002)\"$/v2/{name=projects/*/traces/*}/spans:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_TRACESERVICE)

DESCRIPTOR.services_by_name['TraceService'] = _TRACESERVICE

# @@protoc_insertion_point(module_scope)
