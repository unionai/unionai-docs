---
title: flytekit.types.structured.structured_dataset
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.types.structured.structured_dataset

## Directory

### Classes

| Class | Description |
|-|-|
| [`StructuredDataset`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddataset) | This is the user facing StructuredDataset class. |
| [`StructuredDatasetDecoder`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetdecoder) |  |
| [`StructuredDatasetEncoder`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasetencoder) |  |
| [`StructuredDatasetTransformerEngine`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetstructureddatasettransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |

### Errors

| Exception | Description |
|-|-|
| [`DuplicateHandlerError`](.././flytekit.types.structured.structured_dataset#flytekittypesstructuredstructured_datasetduplicatehandlererror) |  |

### Methods

| Method | Description |
|-|-|
| [`convert_schema_type_to_structured_dataset_type()`](#convert_schema_type_to_structured_dataset_type) |  |
| [`extract_cols_and_format()`](#extract_cols_and_format) | Helper function, just used to iterate through Annotations and extract out the following information:. |
| [`flatten_dict()`](#flatten_dict) |  |
| [`get_supported_types()`](#get_supported_types) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `CSV` | `str` |  |
| `DF` | `TypeVar` |  |
| `GENERIC_FORMAT` | `str` |  |
| `GENERIC_PROTOCOL` | `str` |  |
| `MESSAGEPACK` | `str` |  |
| `PARQUET` | `str` |  |
| `T` | `TypeVar` |  |
| `flyte_dataset_transformer` | `StructuredDatasetTransformerEngine` |  |

## Methods

#### convert_schema_type_to_structured_dataset_type()

```python
def convert_schema_type_to_structured_dataset_type(
    column_type: int,
) -> int
```
| Parameter | Type | Description |
|-|-|-|
| `column_type` | `int` | |

#### extract_cols_and_format()

```python
def extract_cols_and_format(
    t: typing.Any,
) -> typing.Tuple[Type[T], Optional[typing.OrderedDict[str, Type]], Optional[str], Optional['pa.lib.Schema']]
```
Helper function, just used to iterate through Annotations and extract out the following information:
  - base type, if not Annotated, it will just be the type that was passed in.
  - column information, as a collections.OrderedDict,
  - the storage format, as a ``StructuredDatasetFormat`` (str),
  - pa.lib.Schema

If more than one of any type of thing is found, an error will be raised.
If no instances of a given type are found, then None will be returned.

If we add more things, we should put all the returned items in a dataclass instead of just a tuple.



| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Any` | The incoming type which may or may not be Annotated :return: Tuple representing the original type, optional OrderedDict of columns, optional str for the format, optional pyarrow Schema |

#### flatten_dict()

```python
def flatten_dict(
    sub_dict: dict,
    parent_key: str,
) -> typing.Dict
```
| Parameter | Type | Description |
|-|-|-|
| `sub_dict` | `dict` | |
| `parent_key` | `str` | |

#### get_supported_types()

```python
def get_supported_types()
```
## flytekit.types.structured.structured_dataset.DuplicateHandlerError

## flytekit.types.structured.structured_dataset.StructuredDataset

This is the user facing StructuredDataset class. Please don't confuse it with the literals.StructuredDataset
class (that is just a model, a Python class representation of the protobuf).



```python
class StructuredDataset(
    dataframe: typing.Optional[typing.Any],
    uri: typing.Optional[str],
    metadata: typing.Optional[literals.StructuredDatasetMetadata],
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `dataframe` | `typing.Optional[typing.Any]` | |
| `uri` | `typing.Optional[str]` | |
| `metadata` | `typing.Optional[literals.StructuredDatasetMetadata]` | |
| `kwargs` | `**kwargs` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `dataframe` | `None` |  |
| `literal` | `None` |  |
| `metadata` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`deserialize_structured_dataset()`](#deserialize_structured_dataset) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`iter()`](#iter) |  |
| [`open()`](#open) |  |
| [`serialize_structured_dataset()`](#serialize_structured_dataset) |  |
| [`set_literal()`](#set_literal) | A public wrapper method to set the StructuredDataset Literal. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### all()

```python
def all()
```
#### column_names()

```python
def column_names()
```
#### columns()

```python
def columns()
```
#### deserialize_structured_dataset()

```python
def deserialize_structured_dataset(
    info,
) -> StructuredDataset
```
| Parameter | Type | Description |
|-|-|-|
| `info` |  | |

#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type | Description |
|-|-|-|
| `d` |  | |
| `dialect` |  | |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` | |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` | |
| `from_dict_kwargs` | `typing.Any` | |

#### iter()

```python
def iter()
```
#### open()

```python
def open(
    dataframe_type: Type[DF],
)
```
| Parameter | Type | Description |
|-|-|-|
| `dataframe_type` | `Type[DF]` | |

#### serialize_structured_dataset()

```python
def serialize_structured_dataset()
```
#### set_literal()

```python
def set_literal(
    ctx: FlyteContext,
    expected: LiteralType,
)
```
A public wrapper method to set the StructuredDataset Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `expected` | `LiteralType` | |

#### to_dict()

```python
def to_dict()
```
#### to_json()

```python
def to_json(
    encoder: collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]],
    to_dict_kwargs: typing.Any,
) -> typing.Union[str, bytes, bytearray]
```
| Parameter | Type | Description |
|-|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` | |
| `to_dict_kwargs` | `typing.Any` | |

## flytekit.types.structured.structured_dataset.StructuredDatasetDecoder

```python
class StructuredDatasetDecoder(
    python_type: Type[DF],
    protocol: Optional[str],
    supported_format: Optional[str],
    additional_protocols: Optional[List[str]],
)
```
Extend this abstract class, implement the decode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the StructuredDatasetEncoder



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[DF]` | The dataframe class in question that you want to register this decoder with |
| `protocol` | `Optional[str]` | A prefix representing the storage driver (e.g. 's3, 'gs', 'bq', etc.). You can use either "s3" or "s3://". They are the same since the "://" will just be stripped by the constructor. If None, this decoder will be registered with all protocols that flytekit's data persistence layer is capable of handling. |
| `supported_format` | `Optional[str]` | Arbitrary string representing the format. If not supplied then an empty string will be used. An empty string implies that the decoder works with any format. If the format being asked for does not exist, the transformer enginer will look for the "" decoder instead and write a warning. |
| `additional_protocols` | `Optional[List[str]]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


#### decode()

```python
def decode(
    ctx: FlyteContext,
    flyte_value: literals.StructuredDataset,
    current_task_metadata: StructuredDatasetMetadata,
) -> Union[DF, typing.Iterator[DF]]
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `flyte_value` | `literals.StructuredDataset` | This will be a Flyte IDL StructuredDataset Literal - do not confuse this with the StructuredDataset class defined also in this module. |
| `current_task_metadata` | `StructuredDatasetMetadata` | Metadata object containing the type (and columns if any) for the currently executing task. This type may have more or less information than the type information bundled inside the incoming flyte_value. :return: This function can either return an instance of the dataframe that this decoder handles, or an iterator of those dataframes. |

## flytekit.types.structured.structured_dataset.StructuredDatasetEncoder

```python
class StructuredDatasetEncoder(
    python_type: Type[T],
    protocol: Optional[str],
    supported_format: Optional[str],
)
```
Extend this abstract class, implement the encode function, and register your concrete class with the
StructuredDatasetTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the StructuredDatasetEncoder



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[T]` | The dataframe class in question that you want to register this encoder with |
| `protocol` | `Optional[str]` | A prefix representing the storage driver (e.g. 's3, 'gs', 'bq', etc.). You can use either "s3" or "s3://". They are the same since the "://" will just be stripped by the constructor. If None, this encoder will be registered with all protocols that flytekit's data persistence layer is capable of handling. |
| `supported_format` | `Optional[str]` | Arbitrary string representing the format. If not supplied then an empty string will be used. An empty string implies that the encoder works with any format. If the format being asked for does not exist, the transformer engine will look for the "" encoder instead and write a warning. |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the. |


#### encode()

```python
def encode(
    ctx: FlyteContext,
    structured_dataset: StructuredDataset,
    structured_dataset_type: StructuredDatasetType,
) -> literals.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `structured_dataset` | `StructuredDataset` | This is a StructuredDataset wrapper object. See more info above. |
| `structured_dataset_type` | `StructuredDatasetType` | This the StructuredDatasetType, as found in the LiteralType of the interface of the task that invoked this encoding call. It is passed along to encoders so that authors of encoders can include it in the returned literals.StructuredDataset. See the IDL for more information on why this literal in particular carries the type information along with it. If the encoder doesn't supply it, it will also be filled in after the encoder runs by the transformer engine. :return: This function should return a StructuredDataset literal object. Do not confuse this with the StructuredDataset wrapper class used as input to this function - that is the user facing Python class. This function needs to return the IDL StructuredDataset. |

## flytekit.types.structured.structured_dataset.StructuredDatasetTransformerEngine

Think of this transformer as a higher-level meta transformer that is used for all the dataframe types.
If you are bringing a custom data frame type, or any data frame type, to flytekit, instead of
registering with the main type engine, you should register with this transformer instead.



```python
def StructuredDatasetTransformerEngine()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `is_async` | `None` |  |
| `name` | `None` |  |
| `python_type` | `None` | This returns the python type |
| `type_assertions_enabled` | `None` | Indicates if the transformer wants type assertions to be enabled at the core type engine layer |

### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`async_to_literal()`](#async_to_literal) | Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type. |
| [`async_to_python_value()`](#async_to_python_value) | The only tricky thing with converting a Literal (say the output of an earlier task), to a Python value at. |
| [`dict_to_structured_dataset()`](#dict_to_structured_dataset) |  |
| [`encode()`](#encode) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
| [`from_generic_idl()`](#from_generic_idl) | If the input is from Flyte Console, the Life Cycle will be as follows:. |
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
| [`to_python_value()`](#to_python_value) | Converts the given Literal to a Python Type. |


#### assert_type()

```python
def assert_type(
    t: Type[StructuredDataset],
    v: typing.Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `t` | `Type[StructuredDataset]` | |
| `v` | `typing.Any` | |

#### async_to_literal()

```python
def async_to_literal(
    ctx: FlyteContext,
    python_val: Union[StructuredDataset, typing.Any],
    python_type: Union[Type[StructuredDataset], Type],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `Union[StructuredDataset, typing.Any]` | The actual value to be transformed |
| `python_type` | `Union[Type[StructuredDataset], Type]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

#### async_to_python_value()

```python
def async_to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
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
| `ctx` | `FlyteContext` | |
| `lv` | `Literal` | |
| `expected_python_type` | `Type[T] \| StructuredDataset` | |

#### dict_to_structured_dataset()

```python
def dict_to_structured_dataset(
    dict_obj: typing.Dict[str, str],
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
| Parameter | Type | Description |
|-|-|-|
| `dict_obj` | `typing.Dict[str, str]` | |
| `expected_python_type` | `Type[T] \| StructuredDataset` | |

#### encode()

```python
def encode(
    ctx: FlyteContext,
    sd: StructuredDataset,
    df_type: Type,
    protocol: str,
    format: str,
    structured_literal_type: StructuredDatasetType,
) -> Literal
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `sd` | `StructuredDataset` | |
| `df_type` | `Type` | |
| `protocol` | `str` | |
| `format` | `str` | |
| `structured_literal_type` | `StructuredDatasetType` | |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: Binary,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -&gt; resolved binary         -&gt; bytes                   -&gt; expected Python object
(flytekit customized          (propeller processing)     (flytekit binary IDL)      (flytekit customized
serialization)                                                                       deserialization)

Example Code:
@dataclass
class DC:
    sd: StructuredDataset

@workflow
def wf(dc: DC):
    t_sd(dc.sd)

Note:
- The deserialization is the same as put a structured dataset in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type | Description |
|-|-|-|
| `binary_idl_object` | `Binary` | |
| `expected_python_type` | `Type[T] \| StructuredDataset` | |

#### from_generic_idl()

```python
def from_generic_idl(
    generic: Struct,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
If the input is from Flyte Console, the Life Cycle will be as follows:

Life Cycle:
json str            -&gt; protobuf struct         -&gt; resolved protobuf struct   -&gt; expected Python object
(console user input)   (console output)           (propeller)                   (flytekit customized deserialization)

Example Code:
@dataclass
class DC:
    sd: StructuredDataset

@workflow
def wf(dc: DC):
    t_sd(dc.sd)

Note:
- The deserialization is the same as put a structured dataset in a dataclass, which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type | Description |
|-|-|-|
| `generic` | `Struct` | |
| `expected_python_type` | `Type[T] \| StructuredDataset` | |

#### get_decoder()

```python
def get_decoder(
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

#### get_encoder()

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

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Union[Type[StructuredDataset], typing.Any],
) -> LiteralType
```
Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that
special about the literal type. Any dataframe type will always be associated with the structured dataset type.
The other aspects of it - columns, external schema type, etc. can be read from associated metadata.



| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Union[Type[StructuredDataset], typing.Any]` | The python dataframe type, which is mostly ignored. |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: LiteralType,
) -> Type[StructuredDataset]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `LiteralType` | |

#### isinstance_generic()

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

#### iter_as()

```python
def iter_as(
    ctx: FlyteContext,
    sd: literals.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: StructuredDatasetMetadata,
) -> typing.Iterator[DF]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `sd` | `literals.StructuredDataset` | |
| `df_type` | `Type[DF]` | |
| `updated_metadata` | `StructuredDatasetMetadata` | |

#### open_as()

```python
def open_as(
    ctx: FlyteContext,
    sd: literals.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: StructuredDatasetMetadata,
) -> DF
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `sd` | `literals.StructuredDataset` | |
| `df_type` | `Type[DF]` | |
| `updated_metadata` | `StructuredDatasetMetadata` | New metadata type, since it might be different from the metadata in the literal. :return: dataframe. It could be pandas dataframe or arrow table, etc. |

#### register()

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
| `h` | `Handlers` | The StructuredDatasetEncoder or StructuredDatasetDecoder you wish to register with this transformer. |
| `default_for_type` | `bool` | If set, when a user returns from a task an instance of the dataframe the handler handles, e.g. ``return pd.DataFrame(...)``, not wrapped around the ``StructuredDataset`` object, we will use this handler's protocol and format as the default, effectively saying that this handler will be called. Note that this shouldn't be set if your handler's protocol is None, because that implies that your handler is capable of handling all the different storage protocols that flytekit's data persistence layer is aware of. In these cases, the protocol is determined by the raw output data prefix set in the active context. |
| `override` | `bool` | Override any previous registrations. If default_for_type is also set, this will also override the default. |
| `default_format_for_type` | `bool` | Unlike the default_for_type arg that will set this handler's format and storage as the default, this will only set the format. Error if already set, unless override is specified. |
| `default_storage_for_type` | `bool` | Same as above but only for the storage format. Error if already set, unless override is specified. |

#### register_for_protocol()

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

#### register_renderer()

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

#### to_html()

```python
def to_html(
    ctx: FlyteContext,
    python_val: typing.Any,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | |
| `python_val` | `typing.Any` | |
| `expected_python_type` | `Type[T]` | |

#### to_literal()

```python
def to_literal(
    ctx: FlyteContext,
    python_val: typing.Any,
    python_type: Type[T],
    expected: LiteralType,
) -> Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | A FlyteContext, useful in accessing the filesystem and other attributes |
| `python_val` | `typing.Any` | The actual value to be transformed |
| `python_type` | `Type[T]` | The assumed type of the value (this matches the declared type on the function) |
| `expected` | `LiteralType` | Expected Literal Type |

#### to_python_value()

```python
def to_python_value(
    ctx: FlyteContext,
    lv: Literal,
    expected_python_type: Type[T],
) -> Optional[T]
```
Converts the given Literal to a Python Type. If the conversion cannot be done an AssertionError should be raised


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `FlyteContext` | FlyteContext |
| `lv` | `Literal` | The received literal Value |
| `expected_python_type` | `Type[T]` | Expected native python type that should be returned |

