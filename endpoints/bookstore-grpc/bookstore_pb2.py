# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookstore.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bookstore.proto',
  package='endpoints.examples.bookstore',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x62ookstore.proto\x12\x1c\x65ndpoints.examples.bookstore\x1a\x1bgoogle/protobuf/empty.proto\"\"\n\x05Shelf\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05theme\x18\x02 \x01(\t\"1\n\x04\x42ook\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\"K\n\x13ListShelvesResponse\x12\x34\n\x07shelves\x18\x01 \x03(\x0b\x32#.endpoints.examples.bookstore.Shelf\"H\n\x12\x43reateShelfRequest\x12\x32\n\x05shelf\x18\x01 \x01(\x0b\x32#.endpoints.examples.bookstore.Shelf\" \n\x0fGetShelfRequest\x12\r\n\x05shelf\x18\x01 \x01(\x03\"#\n\x12\x44\x65leteShelfRequest\x12\r\n\x05shelf\x18\x01 \x01(\x03\"!\n\x10ListBooksRequest\x12\r\n\x05shelf\x18\x01 \x01(\x03\"F\n\x11ListBooksResponse\x12\x31\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\".endpoints.examples.bookstore.Book\"T\n\x11\x43reateBookRequest\x12\r\n\x05shelf\x18\x01 \x01(\x03\x12\x30\n\x04\x62ook\x18\x02 \x01(\x0b\x32\".endpoints.examples.bookstore.Book\"-\n\x0eGetBookRequest\x12\r\n\x05shelf\x18\x01 \x01(\x03\x12\x0c\n\x04\x62ook\x18\x02 \x01(\x03\"0\n\x11\x44\x65leteBookRequest\x12\r\n\x05shelf\x18\x01 \x01(\x03\x12\x0c\n\x04\x62ook\x18\x02 \x01(\x03\x32\x99\x06\n\tBookstore\x12Z\n\x0bListShelves\x12\x16.google.protobuf.Empty\x1a\x31.endpoints.examples.bookstore.ListShelvesResponse\"\x00\x12\x66\n\x0b\x43reateShelf\x12\x30.endpoints.examples.bookstore.CreateShelfRequest\x1a#.endpoints.examples.bookstore.Shelf\"\x00\x12`\n\x08GetShelf\x12-.endpoints.examples.bookstore.GetShelfRequest\x1a#.endpoints.examples.bookstore.Shelf\"\x00\x12Y\n\x0b\x44\x65leteShelf\x12\x30.endpoints.examples.bookstore.DeleteShelfRequest\x1a\x16.google.protobuf.Empty\"\x00\x12n\n\tListBooks\x12..endpoints.examples.bookstore.ListBooksRequest\x1a/.endpoints.examples.bookstore.ListBooksResponse\"\x00\x12\x63\n\nCreateBook\x12/.endpoints.examples.bookstore.CreateBookRequest\x1a\".endpoints.examples.bookstore.Book\"\x00\x12]\n\x07GetBook\x12,.endpoints.examples.bookstore.GetBookRequest\x1a\".endpoints.examples.bookstore.Book\"\x00\x12W\n\nDeleteBook\x12/.endpoints.examples.bookstore.DeleteBookRequest\x1a\x16.google.protobuf.Empty\"\x00\x42;\n\'com.google.endpoints.examples.bookstoreB\x0e\x42ookstoreProtoP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_SHELF = _descriptor.Descriptor(
  name='Shelf',
  full_name='endpoints.examples.bookstore.Shelf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='endpoints.examples.bookstore.Shelf.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='theme', full_name='endpoints.examples.bookstore.Shelf.theme', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=78,
  serialized_end=112,
)


_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='endpoints.examples.bookstore.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='endpoints.examples.bookstore.Book.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='endpoints.examples.bookstore.Book.author', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='endpoints.examples.bookstore.Book.title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=114,
  serialized_end=163,
)


_LISTSHELVESRESPONSE = _descriptor.Descriptor(
  name='ListShelvesResponse',
  full_name='endpoints.examples.bookstore.ListShelvesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelves', full_name='endpoints.examples.bookstore.ListShelvesResponse.shelves', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=165,
  serialized_end=240,
)


_CREATESHELFREQUEST = _descriptor.Descriptor(
  name='CreateShelfRequest',
  full_name='endpoints.examples.bookstore.CreateShelfRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelf', full_name='endpoints.examples.bookstore.CreateShelfRequest.shelf', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=242,
  serialized_end=314,
)


_GETSHELFREQUEST = _descriptor.Descriptor(
  name='GetShelfRequest',
  full_name='endpoints.examples.bookstore.GetShelfRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelf', full_name='endpoints.examples.bookstore.GetShelfRequest.shelf', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=316,
  serialized_end=348,
)


_DELETESHELFREQUEST = _descriptor.Descriptor(
  name='DeleteShelfRequest',
  full_name='endpoints.examples.bookstore.DeleteShelfRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelf', full_name='endpoints.examples.bookstore.DeleteShelfRequest.shelf', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=350,
  serialized_end=385,
)


_LISTBOOKSREQUEST = _descriptor.Descriptor(
  name='ListBooksRequest',
  full_name='endpoints.examples.bookstore.ListBooksRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelf', full_name='endpoints.examples.bookstore.ListBooksRequest.shelf', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=387,
  serialized_end=420,
)


_LISTBOOKSRESPONSE = _descriptor.Descriptor(
  name='ListBooksResponse',
  full_name='endpoints.examples.bookstore.ListBooksResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='endpoints.examples.bookstore.ListBooksResponse.books', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=422,
  serialized_end=492,
)


_CREATEBOOKREQUEST = _descriptor.Descriptor(
  name='CreateBookRequest',
  full_name='endpoints.examples.bookstore.CreateBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelf', full_name='endpoints.examples.bookstore.CreateBookRequest.shelf', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book', full_name='endpoints.examples.bookstore.CreateBookRequest.book', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=494,
  serialized_end=578,
)


_GETBOOKREQUEST = _descriptor.Descriptor(
  name='GetBookRequest',
  full_name='endpoints.examples.bookstore.GetBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelf', full_name='endpoints.examples.bookstore.GetBookRequest.shelf', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book', full_name='endpoints.examples.bookstore.GetBookRequest.book', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=580,
  serialized_end=625,
)


_DELETEBOOKREQUEST = _descriptor.Descriptor(
  name='DeleteBookRequest',
  full_name='endpoints.examples.bookstore.DeleteBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shelf', full_name='endpoints.examples.bookstore.DeleteBookRequest.shelf', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book', full_name='endpoints.examples.bookstore.DeleteBookRequest.book', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=627,
  serialized_end=675,
)

_LISTSHELVESRESPONSE.fields_by_name['shelves'].message_type = _SHELF
_CREATESHELFREQUEST.fields_by_name['shelf'].message_type = _SHELF
_LISTBOOKSRESPONSE.fields_by_name['books'].message_type = _BOOK
_CREATEBOOKREQUEST.fields_by_name['book'].message_type = _BOOK
DESCRIPTOR.message_types_by_name['Shelf'] = _SHELF
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['ListShelvesResponse'] = _LISTSHELVESRESPONSE
DESCRIPTOR.message_types_by_name['CreateShelfRequest'] = _CREATESHELFREQUEST
DESCRIPTOR.message_types_by_name['GetShelfRequest'] = _GETSHELFREQUEST
DESCRIPTOR.message_types_by_name['DeleteShelfRequest'] = _DELETESHELFREQUEST
DESCRIPTOR.message_types_by_name['ListBooksRequest'] = _LISTBOOKSREQUEST
DESCRIPTOR.message_types_by_name['ListBooksResponse'] = _LISTBOOKSRESPONSE
DESCRIPTOR.message_types_by_name['CreateBookRequest'] = _CREATEBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookRequest'] = _GETBOOKREQUEST
DESCRIPTOR.message_types_by_name['DeleteBookRequest'] = _DELETEBOOKREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Shelf = _reflection.GeneratedProtocolMessageType('Shelf', (_message.Message,), dict(
  DESCRIPTOR = _SHELF,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.Shelf)
  ))
_sym_db.RegisterMessage(Shelf)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), dict(
  DESCRIPTOR = _BOOK,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.Book)
  ))
_sym_db.RegisterMessage(Book)

ListShelvesResponse = _reflection.GeneratedProtocolMessageType('ListShelvesResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTSHELVESRESPONSE,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.ListShelvesResponse)
  ))
_sym_db.RegisterMessage(ListShelvesResponse)

CreateShelfRequest = _reflection.GeneratedProtocolMessageType('CreateShelfRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATESHELFREQUEST,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.CreateShelfRequest)
  ))
_sym_db.RegisterMessage(CreateShelfRequest)

GetShelfRequest = _reflection.GeneratedProtocolMessageType('GetShelfRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSHELFREQUEST,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.GetShelfRequest)
  ))
_sym_db.RegisterMessage(GetShelfRequest)

DeleteShelfRequest = _reflection.GeneratedProtocolMessageType('DeleteShelfRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETESHELFREQUEST,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.DeleteShelfRequest)
  ))
_sym_db.RegisterMessage(DeleteShelfRequest)

ListBooksRequest = _reflection.GeneratedProtocolMessageType('ListBooksRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTBOOKSREQUEST,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.ListBooksRequest)
  ))
_sym_db.RegisterMessage(ListBooksRequest)

ListBooksResponse = _reflection.GeneratedProtocolMessageType('ListBooksResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTBOOKSRESPONSE,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.ListBooksResponse)
  ))
_sym_db.RegisterMessage(ListBooksResponse)

CreateBookRequest = _reflection.GeneratedProtocolMessageType('CreateBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEBOOKREQUEST,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.CreateBookRequest)
  ))
_sym_db.RegisterMessage(CreateBookRequest)

GetBookRequest = _reflection.GeneratedProtocolMessageType('GetBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBOOKREQUEST,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.GetBookRequest)
  ))
_sym_db.RegisterMessage(GetBookRequest)

DeleteBookRequest = _reflection.GeneratedProtocolMessageType('DeleteBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEBOOKREQUEST,
  __module__ = 'bookstore_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.examples.bookstore.DeleteBookRequest)
  ))
_sym_db.RegisterMessage(DeleteBookRequest)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'com.google.endpoints.examples.bookstoreB\016BookstoreProtoP\001'))

_BOOKSTORE = _descriptor.ServiceDescriptor(
  name='Bookstore',
  full_name='endpoints.examples.bookstore.Bookstore',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=678,
  serialized_end=1471,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListShelves',
    full_name='endpoints.examples.bookstore.Bookstore.ListShelves',
    index=0,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTSHELVESRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateShelf',
    full_name='endpoints.examples.bookstore.Bookstore.CreateShelf',
    index=1,
    containing_service=None,
    input_type=_CREATESHELFREQUEST,
    output_type=_SHELF,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetShelf',
    full_name='endpoints.examples.bookstore.Bookstore.GetShelf',
    index=2,
    containing_service=None,
    input_type=_GETSHELFREQUEST,
    output_type=_SHELF,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteShelf',
    full_name='endpoints.examples.bookstore.Bookstore.DeleteShelf',
    index=3,
    containing_service=None,
    input_type=_DELETESHELFREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListBooks',
    full_name='endpoints.examples.bookstore.Bookstore.ListBooks',
    index=4,
    containing_service=None,
    input_type=_LISTBOOKSREQUEST,
    output_type=_LISTBOOKSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CreateBook',
    full_name='endpoints.examples.bookstore.Bookstore.CreateBook',
    index=5,
    containing_service=None,
    input_type=_CREATEBOOKREQUEST,
    output_type=_BOOK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBook',
    full_name='endpoints.examples.bookstore.Bookstore.GetBook',
    index=6,
    containing_service=None,
    input_type=_GETBOOKREQUEST,
    output_type=_BOOK,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBook',
    full_name='endpoints.examples.bookstore.Bookstore.DeleteBook',
    index=7,
    containing_service=None,
    input_type=_DELETEBOOKREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BOOKSTORE)

DESCRIPTOR.services_by_name['Bookstore'] = _BOOKSTORE

# @@protoc_insertion_point(module_scope)
