---
title: DataFrameTransformerEngine
version: 2.0.0b44
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# DataFrameTransformerEngine

**Package:** `flyte.io.extend`

Think of this transformer as a higher-level meta transformer that is used for all the dataframe types.
If you are bringing a custom data frame type, or any data frame type, to flytekit, instead of
registering with the main type engine, you should register with this transformer instead.


```python
def DataFrameTransformerEngine()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` |  |
| `python_type` | `None` | This returns the python type |
| `type_assertions_enabled` | `None` | Indicates if the transformer wants type assertions to be enabled at the core type engine layer |

## Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`encode()`](#encode) |  |
| [`from_binary_idl()`](#from_binary_idl) | This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and. |
| [`get_decoder()`](#get_decoder) |  |
| [`get_encoder()`](#get_encoder) |  |
| [`get_literal_type()`](#get_literal_type) | Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that. |
| [`guess_python_type()`](#guess_python_type) | Converts the Flyte LiteralType to a python object type. |
| [`isinstance_generic()`](#isinstance_generic) |  |
| [`iter_as()`](#iter_as) |  |
| [`open_as()`](#open_as) |  |
| [`register()`](#register) | Call this with any Encoder or Decoder to register it with the flytekit type system. |
| [`register_for_protocol()`](#register_for_protocol) | See the main register function instead. |
| [`register_renderer()`](#register_renderer) |  |
| [`to_html()`](#to_html) | Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div. |
| [`to_literal()`](#to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`to_python_value()`](#to_python_value) | The only tricky thing with converting a Literal (say the output of an earlier task), to a Python value at. |


### assert_type()

```python
def assert_type(
    t: Type[DataFrame],
    v: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[DataFrame]` | |
| `v` | `typing.Any` | |

### encode()

```python
def encode(
    df: DataFrame,
    df_type: Type,
    protocol: str,
    format: str,
    structured_literal_type: types_pb2.StructuredDatasetType,
) -> literals_pb2.Literal
```
| Parameter | Type | Description |
|-|-|-|
| `df` | `DataFrame` | |
| `df_type` | `Type` | |
| `protocol` | `str` | |
| `format` | `str` | |
| `structured_literal_type` | `types_pb2.StructuredDatasetType` | |

### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T],
) -> Optional[T]
```
This function primarily handles deserialization for untyped dicts, dataclasses, Pydantic BaseModels, and
 attribute access.

For untyped dict, dataclass, and pydantic basemodel:
Life Cycle (Untyped Dict as example):
    python val -&gt; msgpack bytes -&gt; binary literal scalar -&gt; msgpack bytes -&gt; python val
                  (to_literal)                             (from_binary_idl)

For attribute access:
Life Cycle:
    python val -&gt; msgpack bytes -&gt; binary literal scalar -&gt; resolved golang value -&gt; binary literal scalar
     -&gt; msgpack bytes -&gt; python val
                  (to_literal)      (propeller attribute access)     (from_binary_idl)


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `Type[T]` | |

### get_decoder()

```python
def get_decoder(
    df_type: Type,
    protocol: str,
    format: str,
) -> DataFrameDecoder
```
| Parameter | Type | Description |
|-|-|-|
| `df_type` | `Type` | |
| `protocol` | `str` | |
| `format` | `str` | |

### get_encoder()

```python
def get_encoder(
    df_type: Type,
    protocol: str,
    format: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `df_type` | `Type` | |
| `protocol` | `str` | |
| `format` | `str` | |

### get_literal_type()

```python
def get_literal_type(
    t: typing.Union[Type[DataFrame], typing.Any],
) -> types_pb2.LiteralType
```
Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that
special about the literal type. Any dataframe type will always be associated with the structured dataset type.
The other aspects of it - columns, external schema type, etc. can be read from associated metadata.



| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Union[Type[DataFrame], typing.Any]` | The python dataframe type, which is mostly ignored. |

### guess_python_type()

```python
def guess_python_type(
    literal_type: types_pb2.LiteralType,
) -> Type[DataFrame]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `types_pb2.LiteralType` | |

### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type | Description |
|-|-|-|
| `obj` |  | |
| `generic_alias` |  | |

### iter_as()

```python
def iter_as(
    sd: literals_pb2.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: literals_pb2.StructuredDatasetMetadata,
) -> typing.AsyncIterator[DF]
```
| Parameter | Type | Description |
|-|-|-|
| `sd` | `literals_pb2.StructuredDataset` | |
| `df_type` | `Type[DF]` | |
| `updated_metadata` | `literals_pb2.StructuredDatasetMetadata` | |

### open_as()

```python
def open_as(
    sd: literals_pb2.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: literals_pb2.StructuredDatasetMetadata,
) -> DF
```
| Parameter | Type | Description |
|-|-|-|
| `sd` | `literals_pb2.StructuredDataset` | |
| `df_type` | `Type[DF]` | |
| `updated_metadata` | `literals_pb2.StructuredDatasetMetadata` | New metadata type, since it might be different from the metadata in the literal. :return: dataframe. It could be pandas dataframe or arrow table, etc. |

### register()

```python
def register(
    h: Handlers,
    default_for_type: bool,
    override: bool,
    default_format_for_type: bool,
    default_storage_for_type: bool,
)
```
Call this with any Encoder or Decoder to register it with the flytekit type system. If your handler does not
specify a protocol (e.g. s3, gs, etc.) field, then



| Parameter | Type | Description |
|-|-|-|
| `h` | `Handlers` | The DataFrameEncoder or DataFrameDecoder you wish to register with this transformer. |
| `default_for_type` | `bool` | If set, when a user returns from a task an instance of the dataframe the handler handles, e.g. ``return pd.DataFrame(...)``, not wrapped around the ``StructuredDataset`` object, we will use this handler's protocol and format as the default, effectively saying that this handler will be called. Note that this shouldn't be set if your handler's protocol is None, because that implies that your handler is capable of handling all the different storage protocols that flytekit's data persistence layer is aware of. In these cases, the protocol is determined by the raw output data prefix set in the active context. |
| `override` | `bool` | Override any previous registrations. If default_for_type is also set, this will also override the default. |
| `default_format_for_type` | `bool` | Unlike the default_for_type arg that will set this handler's format and storage as the default, this will only set the format. Error if already set, unless override is specified. |
| `default_storage_for_type` | `bool` | Same as above but only for the storage format. Error if already set, unless override is specified. |

### register_for_protocol()

```python
def register_for_protocol(
    h: Handlers,
    protocol: str,
    default_for_type: bool,
    override: bool,
    default_format_for_type: bool,
    default_storage_for_type: bool,
)
```
See the main register function instead.


| Parameter | Type | Description |
|-|-|-|
| `h` | `Handlers` | |
| `protocol` | `str` | |
| `default_for_type` | `bool` | |
| `override` | `bool` | |
| `default_format_for_type` | `bool` | |
| `default_storage_for_type` | `bool` | |

### register_renderer()

```python
def register_renderer(
    python_type: Type,
    renderer: Renderable,
)
```
| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type` | |
| `renderer` | `Renderable` | |

### to_html()

```python
def to_html(
    python_val: typing.Any,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type | Description |
|-|-|-|
| `python_val` | `typing.Any` | |
| `expected_python_type` | `Type[T]` | |

### to_literal()

```python
def to_literal(
    python_val: Union[DataFrame, typing.Any],
    python_type: Union[Type[DataFrame], Type],
    expected: types_pb2.LiteralType,
) -> literals_pb2.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type | Description |
|-|-|-|
| `python_val` | `Union[DataFrame, typing.Any]` | The actual value to be transformed |
| `python_type` | `Union[Type[DataFrame], Type]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `types_pb2.LiteralType` | Expected Literal Type |

### to_python_value()

```python
def to_python_value(
    lv: literals_pb2.Literal,
    expected_python_type: Type[T] | DataFrame,
) -> T | DataFrame
```
The only tricky thing with converting a Literal (say the output of an earlier task), to a Python value at
the start of a task execution, is the column subsetting behavior. For example, if you have,

def t1() -&gt; Annotated[StructuredDataset, kwtypes(col_a=int, col_b=float)]: ...
def t2(in_a: Annotated[StructuredDataset, kwtypes(col_b=float)]): ...

where t2(in_a=t1()), when t2 does in_a.open(pd.DataFrame).all(), it should get a DataFrame
with only one column.

+-----------------------------+-----------------------------------------+--------------------------------------+
|                             |          StructuredDatasetType of the incoming Literal                         |
+-----------------------------+-----------------------------------------+--------------------------------------+
| StructuredDatasetType       | Has columns defined                     |  [] columns or None                  |
| of currently running task   |                                         |                                      |
+=============================+=========================================+======================================+
|    Has columns              | The StructuredDatasetType passed to the decoder will have the columns          |
|    defined                  | as defined by the type annotation of the currently running task.               |
|                             |                                                                                |
|                             | Decoders **should** then subset the incoming data to the columns requested.    |
|                             |                                                                                |
+-----------------------------+-----------------------------------------+--------------------------------------+
|   [] columns or None        | StructuredDatasetType passed to decoder | StructuredDatasetType passed to the  |
|                             | will have the columns from the incoming | decoder will have an empty list of   |
|                             | Literal. This is the scenario where     | columns.                             |
|                             | the Literal returned by the running     |                                      |
|                             | task will have more information than    |                                      |
|                             | the running task's signature.           |                                      |
+-----------------------------+-----------------------------------------+--------------------------------------+


| Parameter | Type | Description |
|-|-|-|
| `lv` | `literals_pb2.Literal` | |
| `expected_python_type` | `Type[T] \| DataFrame` | |

