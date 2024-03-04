# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: column.proto

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
  name='column.proto',
  package='',
  serialized_pb=_b('\n\x0c\x63olumn.proto\"\xa1\x01\n\x0b\x44\x61taMessage\x12\x1f\n\x04type\x18\x01 \x02(\x0e\x32\x11.DataMessage.Type\x12\x12\n\noperatorID\x18\x02 \x01(\x04\x12\x1f\n\x07\x63olumns\x18\x03 \x03(\x0b\x32\x0e.ColumnMessage\x12\x12\n\nnum_tuples\x18\x04 \x01(\r\x12\x0b\n\x03seq\x18\x05 \x01(\x04\"\x1b\n\x04Type\x12\n\n\x06NORMAL\x10\x01\x12\x07\n\x03\x45OI\x10\x02\"\xbc\x03\n\rColumnMessage\x12!\n\x04type\x18\x01 \x02(\x0e\x32\x13.ColumnMessage.Type\x12%\n\nint_column\x18\x03 \x01(\x0b\x32\x11.IntColumnMessage\x12\'\n\x0blong_column\x18\x04 \x01(\x0b\x32\x12.LongColumnMessage\x12)\n\x0c\x66loat_column\x18\x05 \x01(\x0b\x32\x13.FloatColumnMessage\x12+\n\rdouble_column\x18\x06 \x01(\x0b\x32\x14.DoubleColumnMessage\x12+\n\rstring_column\x18\x07 \x01(\x0b\x32\x14.StringColumnMessage\x12-\n\x0e\x62oolean_column\x18\x08 \x01(\x0b\x32\x15.BooleanColumnMessage\x12+\n\x0b\x64\x61te_column\x18\t \x01(\x0b\x32\x16.DateTimeColumnMessage\"W\n\x04Type\x12\x07\n\x03INT\x10\x00\x12\x08\n\x04LONG\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\n\n\x06\x44OUBLE\x10\x03\x12\n\n\x06STRING\x10\x04\x12\x0b\n\x07\x42OOLEAN\x10\x05\x12\x0c\n\x08\x44\x41TETIME\x10\x06\" \n\x10IntColumnMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"!\n\x11LongColumnMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"\"\n\x12\x46loatColumnMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"#\n\x13\x44oubleColumnMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"O\n\x13StringColumnMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\x12\x15\n\rstart_indices\x18\x02 \x03(\x05\x12\x13\n\x0b\x65nd_indices\x18\x03 \x03(\x05\"$\n\x14\x42ooleanColumnMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\"%\n\x15\x44\x61teTimeColumnMessage\x12\x0c\n\x04\x64\x61ta\x18\x01 \x02(\x0c\x42\x30\n#edu.washington.escience.myria.protoB\tDataProto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DATAMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='DataMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EOI', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=151,
  serialized_end=178,
)
_sym_db.RegisterEnumDescriptor(_DATAMESSAGE_TYPE)

_COLUMNMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='ColumnMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LONG', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATETIME', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=538,
  serialized_end=625,
)
_sym_db.RegisterEnumDescriptor(_COLUMNMESSAGE_TYPE)


_DATAMESSAGE = _descriptor.Descriptor(
  name='DataMessage',
  full_name='DataMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='DataMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operatorID', full_name='DataMessage.operatorID', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='columns', full_name='DataMessage.columns', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_tuples', full_name='DataMessage.num_tuples', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seq', full_name='DataMessage.seq', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATAMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=178,
)


_COLUMNMESSAGE = _descriptor.Descriptor(
  name='ColumnMessage',
  full_name='ColumnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ColumnMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_column', full_name='ColumnMessage.int_column', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long_column', full_name='ColumnMessage.long_column', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_column', full_name='ColumnMessage.float_column', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_column', full_name='ColumnMessage.double_column', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_column', full_name='ColumnMessage.string_column', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_column', full_name='ColumnMessage.boolean_column', index=6,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_column', full_name='ColumnMessage.date_column', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COLUMNMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=625,
)


_INTCOLUMNMESSAGE = _descriptor.Descriptor(
  name='IntColumnMessage',
  full_name='IntColumnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='IntColumnMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=627,
  serialized_end=659,
)


_LONGCOLUMNMESSAGE = _descriptor.Descriptor(
  name='LongColumnMessage',
  full_name='LongColumnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='LongColumnMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=694,
)


_FLOATCOLUMNMESSAGE = _descriptor.Descriptor(
  name='FloatColumnMessage',
  full_name='FloatColumnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='FloatColumnMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=696,
  serialized_end=730,
)


_DOUBLECOLUMNMESSAGE = _descriptor.Descriptor(
  name='DoubleColumnMessage',
  full_name='DoubleColumnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DoubleColumnMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=732,
  serialized_end=767,
)


_STRINGCOLUMNMESSAGE = _descriptor.Descriptor(
  name='StringColumnMessage',
  full_name='StringColumnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='StringColumnMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_indices', full_name='StringColumnMessage.start_indices', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_indices', full_name='StringColumnMessage.end_indices', index=2,
      number=3, type=5, cpp_type=1, label=3,
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
  oneofs=[
  ],
  serialized_start=769,
  serialized_end=848,
)


_BOOLEANCOLUMNMESSAGE = _descriptor.Descriptor(
  name='BooleanColumnMessage',
  full_name='BooleanColumnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='BooleanColumnMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=850,
  serialized_end=886,
)


_DATETIMECOLUMNMESSAGE = _descriptor.Descriptor(
  name='DateTimeColumnMessage',
  full_name='DateTimeColumnMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='DateTimeColumnMessage.data', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=888,
  serialized_end=925,
)

_DATAMESSAGE.fields_by_name['type'].enum_type = _DATAMESSAGE_TYPE
_DATAMESSAGE.fields_by_name['columns'].message_type = _COLUMNMESSAGE
_DATAMESSAGE_TYPE.containing_type = _DATAMESSAGE
_COLUMNMESSAGE.fields_by_name['type'].enum_type = _COLUMNMESSAGE_TYPE
_COLUMNMESSAGE.fields_by_name['int_column'].message_type = _INTCOLUMNMESSAGE
_COLUMNMESSAGE.fields_by_name['long_column'].message_type = _LONGCOLUMNMESSAGE
_COLUMNMESSAGE.fields_by_name['float_column'].message_type = _FLOATCOLUMNMESSAGE
_COLUMNMESSAGE.fields_by_name['double_column'].message_type = _DOUBLECOLUMNMESSAGE
_COLUMNMESSAGE.fields_by_name['string_column'].message_type = _STRINGCOLUMNMESSAGE
_COLUMNMESSAGE.fields_by_name['boolean_column'].message_type = _BOOLEANCOLUMNMESSAGE
_COLUMNMESSAGE.fields_by_name['date_column'].message_type = _DATETIMECOLUMNMESSAGE
_COLUMNMESSAGE_TYPE.containing_type = _COLUMNMESSAGE
DESCRIPTOR.message_types_by_name['DataMessage'] = _DATAMESSAGE
DESCRIPTOR.message_types_by_name['ColumnMessage'] = _COLUMNMESSAGE
DESCRIPTOR.message_types_by_name['IntColumnMessage'] = _INTCOLUMNMESSAGE
DESCRIPTOR.message_types_by_name['LongColumnMessage'] = _LONGCOLUMNMESSAGE
DESCRIPTOR.message_types_by_name['FloatColumnMessage'] = _FLOATCOLUMNMESSAGE
DESCRIPTOR.message_types_by_name['DoubleColumnMessage'] = _DOUBLECOLUMNMESSAGE
DESCRIPTOR.message_types_by_name['StringColumnMessage'] = _STRINGCOLUMNMESSAGE
DESCRIPTOR.message_types_by_name['BooleanColumnMessage'] = _BOOLEANCOLUMNMESSAGE
DESCRIPTOR.message_types_by_name['DateTimeColumnMessage'] = _DATETIMECOLUMNMESSAGE

DataMessage = _reflection.GeneratedProtocolMessageType('DataMessage', (_message.Message,), dict(
  DESCRIPTOR = _DATAMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:DataMessage)
  ))
_sym_db.RegisterMessage(DataMessage)

ColumnMessage = _reflection.GeneratedProtocolMessageType('ColumnMessage', (_message.Message,), dict(
  DESCRIPTOR = _COLUMNMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:ColumnMessage)
  ))
_sym_db.RegisterMessage(ColumnMessage)

IntColumnMessage = _reflection.GeneratedProtocolMessageType('IntColumnMessage', (_message.Message,), dict(
  DESCRIPTOR = _INTCOLUMNMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:IntColumnMessage)
  ))
_sym_db.RegisterMessage(IntColumnMessage)

LongColumnMessage = _reflection.GeneratedProtocolMessageType('LongColumnMessage', (_message.Message,), dict(
  DESCRIPTOR = _LONGCOLUMNMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:LongColumnMessage)
  ))
_sym_db.RegisterMessage(LongColumnMessage)

FloatColumnMessage = _reflection.GeneratedProtocolMessageType('FloatColumnMessage', (_message.Message,), dict(
  DESCRIPTOR = _FLOATCOLUMNMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:FloatColumnMessage)
  ))
_sym_db.RegisterMessage(FloatColumnMessage)

DoubleColumnMessage = _reflection.GeneratedProtocolMessageType('DoubleColumnMessage', (_message.Message,), dict(
  DESCRIPTOR = _DOUBLECOLUMNMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:DoubleColumnMessage)
  ))
_sym_db.RegisterMessage(DoubleColumnMessage)

StringColumnMessage = _reflection.GeneratedProtocolMessageType('StringColumnMessage', (_message.Message,), dict(
  DESCRIPTOR = _STRINGCOLUMNMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:StringColumnMessage)
  ))
_sym_db.RegisterMessage(StringColumnMessage)

BooleanColumnMessage = _reflection.GeneratedProtocolMessageType('BooleanColumnMessage', (_message.Message,), dict(
  DESCRIPTOR = _BOOLEANCOLUMNMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:BooleanColumnMessage)
  ))
_sym_db.RegisterMessage(BooleanColumnMessage)

DateTimeColumnMessage = _reflection.GeneratedProtocolMessageType('DateTimeColumnMessage', (_message.Message,), dict(
  DESCRIPTOR = _DATETIMECOLUMNMESSAGE,
  __module__ = 'column_pb2'
  # @@protoc_insertion_point(class_scope:DateTimeColumnMessage)
  ))
_sym_db.RegisterMessage(DateTimeColumnMessage)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n#edu.washington.escience.myria.protoB\tDataProto'))
# @@protoc_insertion_point(module_scope)