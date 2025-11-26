---
title: flyte.io
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.io


## IO data types

This package contains additional data types beyond the primitive data types in python to abstract data flow
of large datasets in Union.


## Directory

### Classes

| Class | Description |
|-|-|
| [`DataFrame`](.././flyte.io#flyteiodataframe) | This is the user facing DataFrame class. |
| [`DataFrameDecoder`](.././flyte.io#flyteiodataframedecoder) | Helper class that provides a standard way to create an ABC using. |
| [`DataFrameEncoder`](.././flyte.io#flyteiodataframeencoder) | Helper class that provides a standard way to create an ABC using. |
| [`DataFrameTransformerEngine`](.././flyte.io#flyteiodataframetransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |
| [`Dir`](.././flyte.io#flyteiodir) | A generic directory class representing a directory with files of a specified format. |
| [`File`](.././flyte.io#flyteiofile) | A generic file class representing a file with a specified format. |

### Methods

| Method | Description |
|-|-|
| [`lazy_import_dataframe_handler()`](#lazy_import_dataframe_handler) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `PARQUET` | `str` |  |

## Methods

#### lazy_import_dataframe_handler()

```python
def lazy_import_dataframe_handler()
```
## flyte.io.DataFrame

This is the user facing DataFrame class. Please don't confuse it with the literals.StructuredDataset
class (that is just a model, a Python class representation of the protobuf).


```python
class DataFrame(
    data: Any,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `data` | `Any` | |

### Methods

| Method | Description |
|-|-|
| [`all()`](#all) |  |
| [`column_names()`](#column_names) |  |
| [`columns()`](#columns) |  |
| [`construct()`](#construct) |  |
| [`copy()`](#copy) | Returns a copy of the model. |
| [`deserialize_dataframe()`](#deserialize_dataframe) |  |
| [`dict()`](#dict) |  |
| [`from_df()`](#from_df) | Wrapper to create a DataFrame from a dataframe. |
| [`from_existing_remote()`](#from_existing_remote) | Create a DataFrame reference from an existing remote dataframe. |
| [`from_orm()`](#from_orm) |  |
| [`iter()`](#iter) |  |
| [`json()`](#json) |  |
| [`model_construct()`](#model_construct) | Creates a new instance of the `Model` class with validated data. |
| [`model_copy()`](#model_copy) | !!! abstract "Usage Documentation". |
| [`model_dump()`](#model_dump) | !!! abstract "Usage Documentation". |
| [`model_dump_json()`](#model_dump_json) | !!! abstract "Usage Documentation". |
| [`model_json_schema()`](#model_json_schema) | Generates a JSON schema for a model class. |
| [`model_parametrized_name()`](#model_parametrized_name) | Compute the class name for parametrizations of generic classes. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialise private attributes. |
| [`model_rebuild()`](#model_rebuild) | Try to rebuild the pydantic-core schema for the model. |
| [`model_validate()`](#model_validate) | Validate a pydantic model instance. |
| [`model_validate_json()`](#model_validate_json) | !!! abstract "Usage Documentation". |
| [`model_validate_strings()`](#model_validate_strings) | Validate the given object with string data against the Pydantic model. |
| [`open()`](#open) | Load the handler if needed. |
| [`parse_file()`](#parse_file) |  |
| [`parse_obj()`](#parse_obj) |  |
| [`parse_raw()`](#parse_raw) |  |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
| [`serialize_dataframe()`](#serialize_dataframe) |  |
| [`set_literal()`](#set_literal) | A public wrapper method to set the DataFrame Literal. |
| [`update_forward_refs()`](#update_forward_refs) |  |
| [`validate()`](#validate) |  |


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
#### construct()

```python
def construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | |
| `values` | `Any` | |

#### copy()

```python
def copy(
    include: AbstractSetIntStr | MappingIntStrAny | None,
    exclude: AbstractSetIntStr | MappingIntStrAny | None,
    update: Dict[str, Any] | None,
    deep: bool,
) -> Self
```
Returns a copy of the model.

&gt; [!WARNING] Deprecated
&gt; This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```python {test="skip" lint="skip"}
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```



| Parameter | Type | Description |
|-|-|-|
| `include` | `AbstractSetIntStr \| MappingIntStrAny \| None` | Optional set or mapping specifying which fields to include in the copied model. |
| `exclude` | `AbstractSetIntStr \| MappingIntStrAny \| None` | Optional set or mapping specifying which fields to exclude in the copied model. |
| `update` | `Dict[str, Any] \| None` | Optional dictionary of field-value pairs to override field values in the copied model. |
| `deep` | `bool` | If True, the values of fields that are Pydantic models will be deep-copied. |

#### deserialize_dataframe()

```python
def deserialize_dataframe(
    info,
) -> DataFrame
```
| Parameter | Type | Description |
|-|-|-|
| `info` |  | |

#### dict()

```python
def dict(
    include: IncEx | None,
    exclude: IncEx | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
) -> Dict[str, Any]
```
| Parameter | Type | Description |
|-|-|-|
| `include` | `IncEx \| None` | |
| `exclude` | `IncEx \| None` | |
| `by_alias` | `bool` | |
| `exclude_unset` | `bool` | |
| `exclude_defaults` | `bool` | |
| `exclude_none` | `bool` | |

#### from_df()

```python
def from_df(
    val: typing.Optional[typing.Any],
    uri: typing.Optional[str],
) -> DataFrame
```
Wrapper to create a DataFrame from a dataframe.
The reason this is implemented as a wrapper instead of a full translation invoking
the type engine and the encoders is because there's too much information in the type
signature of the task that we don't want the user to have to replicate.


| Parameter | Type | Description |
|-|-|-|
| `val` | `typing.Optional[typing.Any]` | |
| `uri` | `typing.Optional[str]` | |

#### from_existing_remote()

```python
def from_existing_remote(
    remote_path: str,
    format: typing.Optional[str],
    kwargs,
) -> 'DataFrame'
```
Create a DataFrame reference from an existing remote dataframe.



| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | The remote path to the existing dataframe |
| `format` | `typing.Optional[str]` | Format of the stored dataframe |
| `kwargs` | `**kwargs` | |

#### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

#### iter()

```python
def iter()
```
#### json()

```python
def json(
    include: IncEx | None,
    exclude: IncEx | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    encoder: Callable[[Any], Any] | None,
    models_as_dict: bool,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `include` | `IncEx \| None` | |
| `exclude` | `IncEx \| None` | |
| `by_alias` | `bool` | |
| `exclude_unset` | `bool` | |
| `exclude_defaults` | `bool` | |
| `exclude_none` | `bool` | |
| `encoder` | `Callable[[Any], Any] \| None` | |
| `models_as_dict` | `bool` | |
| `dumps_kwargs` | `Any` | |

#### model_construct()

```python
def model_construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

&gt; [!NOTE]
&gt; `model_construct()` generally respects the `model_config.extra` setting on the provided model.
&gt; That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
&gt; and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
&gt; Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
&gt; an error if extra values are passed, but they will be ignored.



| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | A set of field names that were originally explicitly set during instantiation. If provided, this is directly used for the [`model_fields_set`][pydantic.BaseModel.model_fields_set] attribute. Otherwise, the field names from the `values` argument will be used. |
| `values` | `Any` | Trusted or pre-validated data dictionary. |

#### model_copy()

```python
def model_copy(
    update: Mapping[str, Any] | None,
    deep: bool,
) -> Self
```
!!! abstract "Usage Documentation"
    [`model_copy`](../concepts/models.md#model-copy)

Returns a copy of the model.

&gt; [!NOTE]
&gt; The underlying instance's [`__dict__`][object.__dict__] attribute is copied. This
&gt; might have unexpected side effects if you store anything in it, on top of the model
&gt; fields (e.g. the value of [cached properties][functools.cached_property]).



| Parameter | Type | Description |
|-|-|-|
| `update` | `Mapping[str, Any] \| None` | |
| `deep` | `bool` | Set to `True` to make a deep copy of the model. |

#### model_dump()

```python
def model_dump(
    mode: Literal['json', 'python'] | str,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    exclude_computed_fields: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> dict[str, Any]
```
!!! abstract "Usage Documentation"
    [`model_dump`](../concepts/serialization.md#python-mode)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type | Description |
|-|-|-|
| `mode` | `Literal['json', 'python'] \| str` | The mode in which `to_python` should run. If mode is 'json', the output will only contain JSON serializable types. If mode is 'python', the output may contain non-JSON-serializable Python objects. |
| `include` | `IncEx \| None` | A set of fields to include in the output. |
| `exclude` | `IncEx \| None` | A set of fields to exclude from the output. |
| `context` | `Any \| None` | Additional context to pass to the serializer. |
| `by_alias` | `bool \| None` | Whether to use the field's alias in the dictionary key if defined. |
| `exclude_unset` | `bool` | Whether to exclude fields that have not been explicitly set. |
| `exclude_defaults` | `bool` | Whether to exclude fields that are set to their default value. |
| `exclude_none` | `bool` | Whether to exclude fields that have a value of `None`. |
| `exclude_computed_fields` | `bool` | Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |
| `round_trip` | `bool` | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised. |
| `serialize_as_any` | `bool` | Whether to serialize fields with duck-typing serialization behavior. |

#### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    ensure_ascii: bool,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    exclude_computed_fields: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> str
```
!!! abstract "Usage Documentation"
    [`model_dump_json`](../concepts/serialization.md#json-mode)

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type | Description |
|-|-|-|
| `indent` | `int \| None` | Indentation to use in the JSON output. If None is passed, the output will be compact. |
| `ensure_ascii` | `bool` | If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |
| `include` | `IncEx \| None` | Field(s) to include in the JSON output. |
| `exclude` | `IncEx \| None` | Field(s) to exclude from the JSON output. |
| `context` | `Any \| None` | Additional context to pass to the serializer. |
| `by_alias` | `bool \| None` | Whether to serialize using field aliases. |
| `exclude_unset` | `bool` | Whether to exclude fields that have not been explicitly set. |
| `exclude_defaults` | `bool` | Whether to exclude fields that are set to their default value. |
| `exclude_none` | `bool` | Whether to exclude fields that have a value of `None`. |
| `exclude_computed_fields` | `bool` | Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |
| `round_trip` | `bool` | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised. |
| `serialize_as_any` | `bool` | Whether to serialize fields with duck-typing serialization behavior. |

#### model_json_schema()

```python
def model_json_schema(
    by_alias: bool,
    ref_template: str,
    schema_generator: type[GenerateJsonSchema],
    mode: JsonSchemaMode,
    union_format: Literal['any_of', 'primitive_type_array'],
) -> dict[str, Any]
```
Generates a JSON schema for a model class.



| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | Whether to use attribute aliases or not. |
| `ref_template` | `str` | The reference template. - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf) keyword to combine schemas (the default). - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type) keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`. |
| `schema_generator` | `type[GenerateJsonSchema]` | To override the logic used to generate the JSON schema, as a subclass of `GenerateJsonSchema` with your desired modifications |
| `mode` | `JsonSchemaMode` | The mode in which to generate the schema. |
| `union_format` | `Literal['any_of', 'primitive_type_array']` | |

#### model_parametrized_name()

```python
def model_parametrized_name(
    params: tuple[type[Any], ...],
) -> str
```
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.



| Parameter | Type | Description |
|-|-|-|
| `params` | `tuple[type[Any], ...]` | Tuple of types of the class. Given a generic class `Model` with 2 type variables and a concrete model `Model[str, int]`, the value `(str, int)` would be passed to `params`. |

#### model_post_init()

```python
def model_post_init(
    context: Any,
)
```
This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that's what pydantic-core passes when calling it.



| Parameter | Type | Description |
|-|-|-|
| `context` | `Any` | The context. |

#### model_rebuild()

```python
def model_rebuild(
    force: bool,
    raise_errors: bool,
    _parent_namespace_depth: int,
    _types_namespace: MappingNamespace | None,
) -> bool | None
```
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.



| Parameter | Type | Description |
|-|-|-|
| `force` | `bool` | Whether to force the rebuilding of the model schema, defaults to `False`. |
| `raise_errors` | `bool` | Whether to raise errors, defaults to `True`. |
| `_parent_namespace_depth` | `int` | The depth level of the parent namespace, defaults to 2. |
| `_types_namespace` | `MappingNamespace \| None` | The types namespace, defaults to `None`. |

#### model_validate()

```python
def model_validate(
    obj: Any,
    strict: bool | None,
    extra: ExtraValues | None,
    from_attributes: bool | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `from_attributes` | `bool \| None` | Whether to extract data from object attributes. |
| `context` | `Any \| None` | Additional context to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    extra: ExtraValues | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
!!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `json_data` | `str \| bytes \| bytearray` | The JSON data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    extra: ExtraValues | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object containing string data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### open()

```python
def open(
    dataframe_type: Type[DF],
)
```
Load the handler if needed. For the use case like:
@task
def t1(df: DataFrame):
  import pandas as pd
  df.open(pd.DataFrame).all()

pandas is imported inside the task, so panda handler won't be loaded during deserialization in type engine.


| Parameter | Type | Description |
|-|-|-|
| `dataframe_type` | `Type[DF]` | |

#### parse_file()

```python
def parse_file(
    path: str | Path,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str \| Path` | |
| `content_type` | `str \| None` | |
| `encoding` | `str` | |
| `proto` | `DeprecatedParseProtocol \| None` | |
| `allow_pickle` | `bool` | |

#### parse_obj()

```python
def parse_obj(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

#### parse_raw()

```python
def parse_raw(
    b: str | bytes,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `b` | `str \| bytes` | |
| `content_type` | `str \| None` | |
| `encoding` | `str` | |
| `proto` | `DeprecatedParseProtocol \| None` | |
| `allow_pickle` | `bool` | |

#### schema()

```python
def schema(
    by_alias: bool,
    ref_template: str,
) -> Dict[str, Any]
```
| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | |
| `ref_template` | `str` | |

#### schema_json()

```python
def schema_json(
    by_alias: bool,
    ref_template: str,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | |
| `ref_template` | `str` | |
| `dumps_kwargs` | `Any` | |

#### serialize_dataframe()

```python
def serialize_dataframe()
```
#### set_literal()

```python
def set_literal(
    expected: types_pb2.LiteralType,
)
```
A public wrapper method to set the DataFrame Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type | Description |
|-|-|-|
| `expected` | `types_pb2.LiteralType` | |

#### update_forward_refs()

```python
def update_forward_refs(
    localns: Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `localns` | `Any` | |

#### validate()

```python
def validate(
    value: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `Any` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `literal` | `None` |  |
| `metadata` | `None` |  |
| `model_extra` | `None` | Get extra fields set during validation.  Returns:     A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. |
| `model_fields_set` | `None` | Returns the set of fields that have been explicitly set on this model instance.  Returns:     A set of strings representing the fields that have been set,         i.e. that were not filled from defaults. |
| `val` | `None` |  |

## flyte.io.DataFrameDecoder

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class DataFrameDecoder(
    python_type: Type[DF],
    protocol: Optional[str],
    supported_format: Optional[str],
    additional_protocols: Optional[List[str]],
)
```
Extend this abstract class, implement the decode function, and register your concrete class with the
DataFrameTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the decoder interface, meaning it is used when there is a Flyte Literal value,
and we have to get a Python value out of it. For the other way, see the DataFrameEncoder



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[DF]` | The dataframe class in question that you want to register this decoder with |
| `protocol` | `Optional[str]` | A prefix representing the storage driver (e.g. 's3, 'gs', 'bq', etc.). You can use either "s3" or "s3://". They are the same since the "://" will just be stripped by the constructor. If None, this decoder will be registered with all protocols that flytekit's data persistence layer is capable of handling. |
| `supported_format` | `Optional[str]` | Arbitrary string representing the format. If not supplied then an empty string will be used. An empty string implies that the decoder works with any format. If the format being asked for does not exist, the transformer enginer will look for the "" decoder instead and write a warning. |
| `additional_protocols` | `Optional[List[str]]` | |

### Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal. |


#### decode()

```python
def decode(
    flyte_value: literals_pb2.StructuredDataset,
    current_task_metadata: literals_pb2.StructuredDatasetMetadata,
) -> Union[DF, typing.AsyncIterator[DF]]
```
This is code that will be called by the dataset transformer engine to ultimately translate from a Flyte Literal
value into a Python instance.



| Parameter | Type | Description |
|-|-|-|
| `flyte_value` | `literals_pb2.StructuredDataset` | This will be a Flyte IDL DataFrame Literal - do not confuse this with the DataFrame class defined also in this module. |
| `current_task_metadata` | `literals_pb2.StructuredDatasetMetadata` | Metadata object containing the type (and columns if any) for the currently executing task. This type may have more or less information than the type information bundled inside the incoming flyte_value. :return: This function can either return an instance of the dataframe that this decoder handles, or an iterator of those dataframes. |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

## flyte.io.DataFrameEncoder

Helper class that provides a standard way to create an ABC using
inheritance.


```python
class DataFrameEncoder(
    python_type: Type[T],
    protocol: Optional[str],
    supported_format: Optional[str],
)
```
Extend this abstract class, implement the encode function, and register your concrete class with the
DataFrameTransformerEngine class in order for the core flytekit type engine to handle
dataframe libraries. This is the encoding interface, meaning it is used when there is a Python value that the
flytekit type engine is trying to convert into a Flyte Literal. For the other way, see
the DataFrameEncoder



| Parameter | Type | Description |
|-|-|-|
| `python_type` | `Type[T]` | The dataframe class in question that you want to register this encoder with |
| `protocol` | `Optional[str]` | A prefix representing the storage driver (e.g. 's3, 'gs', 'bq', etc.). You can use either "s3" or "s3://". They are the same since the "://" will just be stripped by the constructor. If None, this encoder will be registered with all protocols that flytekit's data persistence layer is capable of handling. |
| `supported_format` | `Optional[str]` | Arbitrary string representing the format. If not supplied then an empty string will be used. An empty string implies that the encoder works with any format. If the format being asked for does not exist, the transformer engine will look for the "" encoder instead and write a warning. |

### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the. |


#### encode()

```python
def encode(
    dataframe: DataFrame,
    structured_dataset_type: types_pb2.StructuredDatasetType,
) -> literals_pb2.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type | Description |
|-|-|-|
| `dataframe` | `DataFrame` | This is a DataFrame wrapper object. See more info above. |
| `structured_dataset_type` | `types_pb2.StructuredDatasetType` | This the DataFrameType, as found in the LiteralType of the interface of the task that invoked this encoding call. It is passed along to encoders so that authors of encoders can include it in the returned literals.DataFrame. See the IDL for more information on why this literal in particular carries the type information along with it. If the encoder doesn't supply it, it will also be filled in after the encoder runs by the transformer engine. :return: This function should return a DataFrame literal object. Do not confuse this with the DataFrame wrapper class used as input to this function - that is the user facing Python class. This function needs to return the IDL DataFrame. |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

## flyte.io.DataFrameTransformerEngine

Think of this transformer as a higher-level meta transformer that is used for all the dataframe types.
If you are bringing a custom data frame type, or any data frame type, to flytekit, instead of
registering with the main type engine, you should register with this transformer instead.


```python
def DataFrameTransformerEngine()
```
### Methods

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


#### assert_type()

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

#### encode()

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

#### from_binary_idl()

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

#### get_decoder()

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
    t: typing.Union[Type[DataFrame], typing.Any],
) -> types_pb2.LiteralType
```
Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that
special about the literal type. Any dataframe type will always be associated with the structured dataset type.
The other aspects of it - columns, external schema type, etc. can be read from associated metadata.



| Parameter | Type | Description |
|-|-|-|
| `t` | `typing.Union[Type[DataFrame], typing.Any]` | The python dataframe type, which is mostly ignored. |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: types_pb2.LiteralType,
) -> Type[DataFrame]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type | Description |
|-|-|-|
| `literal_type` | `types_pb2.LiteralType` | |

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

#### open_as()

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
| `h` | `Handlers` | The DataFrameEncoder or DataFrameDecoder you wish to register with this transformer. |
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
    python_val: typing.Any,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type | Description |
|-|-|-|
| `python_val` | `typing.Any` | |
| `expected_python_type` | `Type[T]` | |

#### to_literal()

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

#### to_python_value()

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

### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` |  |
| `python_type` | `None` | This returns the python type |
| `type_assertions_enabled` | `None` | Indicates if the transformer wants type assertions to be enabled at the core type engine layer |

## flyte.io.Dir

A generic directory class representing a directory with files of a specified format.
Provides both async and sync interfaces for directory operations. All methods without _sync suffix are async.

The class should be instantiated using one of the class methods. The constructor should only be used to
instantiate references to existing remote directories.

The generic type T represents the format of the files in the directory.

Important methods:
- `from_existing_remote`: Create a Dir object referencing an existing remote directory.
- `from_local` / `from_local_sync`: Upload a local directory to remote storage.

**Asynchronous methods**:
- `walk`: Asynchronously iterate through files in the directory.
- `list_files`: Asynchronously get a list of all files (non-recursive).
- `download`: Asynchronously download the entire directory to a local path.
- `exists`: Asynchronously check if the directory exists.
- `get_file`: Asynchronously get a specific file from the directory by name.

**Synchronous methods** (suffixed with `_sync`):
- `walk_sync`: Synchronously iterate through files in the directory.
- `list_files_sync`: Synchronously get a list of all files (non-recursive).
- `download_sync`: Synchronously download the entire directory to a local path.
- `exists_sync`: Synchronously check if the directory exists.
- `get_file_sync`: Synchronously get a specific file from the directory by name.

Example: Walk through directory files recursively (Async).

```python
@env.task
async def process_all_files(d: Dir) -&gt; int:
    file_count = 0
    async for file in d.walk(recursive=True):
        async with file.open("rb") as f:
            content = await f.read()
            # Process content
            file_count += 1
    return file_count
```

Example: Walk through directory files recursively (Sync).

```python
@env.task
def process_all_files_sync(d: Dir) -&gt; int:
    file_count = 0
    for file in d.walk_sync(recursive=True):
        with file.open_sync("rb") as f:
            content = f.read()
            # Process content
            file_count += 1
    return file_count
```

Example: List files in directory (Async).

```python
@env.task
async def count_files(d: Dir) -&gt; int:
    files = await d.list_files()
    return len(files)
```

Example: List files in directory (Sync).

```python
@env.task
def count_files_sync(d: Dir) -&gt; int:
    files = d.list_files_sync()
    return len(files)
```

Example: Get a specific file from directory (Async).

```python
@env.task
async def read_config_file(d: Dir) -&gt; str:
    config_file = await d.get_file("config.json")
    if config_file:
        async with config_file.open("rb") as f:
            return (await f.read()).decode("utf-8")
    return "Config not found"
```

Example: Get a specific file from directory (Sync).

```python
@env.task
def read_config_file_sync(d: Dir) -&gt; str:
    config_file = d.get_file_sync("config.json")
    if config_file:
        with config_file.open_sync("rb") as f:
            return f.read().decode("utf-8")
    return "Config not found"
```

Example: Upload a local directory to remote storage (Async).

```python
@env.task
async def upload_directory() -&gt; Dir:
    # Create local directory with files
    os.makedirs("/tmp/my_data", exist_ok=True)
    with open("/tmp/my_data/file1.txt", "w") as f:
        f.write("data1")
    # Upload to remote storage
    return await Dir.from_local("/tmp/my_data/")
```

Example: Upload a local directory to remote storage (Sync).

```python
@env.task
def upload_directory_sync() -&gt; Dir:
    # Create local directory with files
    os.makedirs("/tmp/my_data", exist_ok=True)
    with open("/tmp/my_data/file1.txt", "w") as f:
        f.write("data1")
    # Upload to remote storage
    return Dir.from_local_sync("/tmp/my_data/")
```

Example: Download a directory to local storage (Async).

```python
@env.task
async def download_directory(d: Dir) -&gt; str:
    local_path = await d.download()
    # Process files in local directory
    return local_path
```

Example: Download a directory to local storage (Sync).

```python
@env.task
def download_directory_sync(d: Dir) -&gt; str:
    local_path = d.download_sync()
    # Process files in local directory
    return local_path
```

Example: Reference an existing remote directory.

```python
@env.task
async def process_existing_dir() -&gt; int:
    d = Dir.from_existing_remote("s3://my-bucket/data/")
    files = await d.list_files()
    return len(files)
```

Example: Check if directory exists (Async).

```python
@env.task
async def check_directory(d: Dir) -&gt; bool:
    return await d.exists()
```

Example: Check if directory exists (Sync).

```python
@env.task
def check_directory_sync(d: Dir) -&gt; bool:
    return d.exists_sync()
```



```python
class Dir(
    data: Any,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `data` | `Any` | |

### Methods

| Method | Description |
|-|-|
| [`construct()`](#construct) |  |
| [`copy()`](#copy) | Returns a copy of the model. |
| [`dict()`](#dict) |  |
| [`download()`](#download) | Asynchronously download the entire directory to a local path. |
| [`download_sync()`](#download_sync) | Synchronously download the entire directory to a local path. |
| [`exists()`](#exists) | Asynchronously check if the directory exists. |
| [`exists_sync()`](#exists_sync) | Synchronously check if the directory exists. |
| [`from_existing_remote()`](#from_existing_remote) | Create a Dir reference from an existing remote directory. |
| [`from_local()`](#from_local) | Asynchronously create a new Dir by uploading a local directory to remote storage. |
| [`from_local_sync()`](#from_local_sync) | Synchronously create a new Dir by uploading a local directory to remote storage. |
| [`from_orm()`](#from_orm) |  |
| [`get_file()`](#get_file) | Asynchronously get a specific file from the directory by name. |
| [`get_file_sync()`](#get_file_sync) | Synchronously get a specific file from the directory by name. |
| [`json()`](#json) |  |
| [`list_files()`](#list_files) | Asynchronously get a list of all files in the directory (non-recursive). |
| [`list_files_sync()`](#list_files_sync) | Synchronously get a list of all files in the directory (non-recursive). |
| [`model_construct()`](#model_construct) | Creates a new instance of the `Model` class with validated data. |
| [`model_copy()`](#model_copy) | !!! abstract "Usage Documentation". |
| [`model_dump()`](#model_dump) | !!! abstract "Usage Documentation". |
| [`model_dump_json()`](#model_dump_json) | !!! abstract "Usage Documentation". |
| [`model_json_schema()`](#model_json_schema) | Generates a JSON schema for a model class. |
| [`model_parametrized_name()`](#model_parametrized_name) | Compute the class name for parametrizations of generic classes. |
| [`model_post_init()`](#model_post_init) | Override this method to perform additional initialization after `__init__` and `model_construct`. |
| [`model_rebuild()`](#model_rebuild) | Try to rebuild the pydantic-core schema for the model. |
| [`model_validate()`](#model_validate) | Validate a pydantic model instance. |
| [`model_validate_json()`](#model_validate_json) | !!! abstract "Usage Documentation". |
| [`model_validate_strings()`](#model_validate_strings) | Validate the given object with string data against the Pydantic model. |
| [`parse_file()`](#parse_file) |  |
| [`parse_obj()`](#parse_obj) |  |
| [`parse_raw()`](#parse_raw) |  |
| [`pre_init()`](#pre_init) | Internal: Pydantic validator to set default name from path. |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
| [`schema_match()`](#schema_match) | Internal: Check if incoming schema matches Dir schema. |
| [`update_forward_refs()`](#update_forward_refs) |  |
| [`validate()`](#validate) |  |
| [`walk()`](#walk) | Asynchronously walk through the directory and yield File objects. |
| [`walk_sync()`](#walk_sync) | Synchronously walk through the directory and yield File objects. |


#### construct()

```python
def construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | |
| `values` | `Any` | |

#### copy()

```python
def copy(
    include: AbstractSetIntStr | MappingIntStrAny | None,
    exclude: AbstractSetIntStr | MappingIntStrAny | None,
    update: Dict[str, Any] | None,
    deep: bool,
) -> Self
```
Returns a copy of the model.

&gt; [!WARNING] Deprecated
&gt; This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```python {test="skip" lint="skip"}
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```



| Parameter | Type | Description |
|-|-|-|
| `include` | `AbstractSetIntStr \| MappingIntStrAny \| None` | Optional set or mapping specifying which fields to include in the copied model. |
| `exclude` | `AbstractSetIntStr \| MappingIntStrAny \| None` | Optional set or mapping specifying which fields to exclude in the copied model. |
| `update` | `Dict[str, Any] \| None` | Optional dictionary of field-value pairs to override field values in the copied model. |
| `deep` | `bool` | If True, the values of fields that are Pydantic models will be deep-copied. |

#### dict()

```python
def dict(
    include: IncEx | None,
    exclude: IncEx | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
) -> Dict[str, Any]
```
| Parameter | Type | Description |
|-|-|-|
| `include` | `IncEx \| None` | |
| `exclude` | `IncEx \| None` | |
| `by_alias` | `bool` | |
| `exclude_unset` | `bool` | |
| `exclude_defaults` | `bool` | |
| `exclude_none` | `bool` | |

#### download()

```python
def download(
    local_path: Optional[Union[str, Path]],
) -> str
```
Asynchronously download the entire directory to a local path.

Use this when you need to download all files in a directory to your local filesystem for processing.

Example (Async):

```python
@env.task
async def download_directory(d: Dir) -&gt; str:
    local_dir = await d.download()
    # Process files in the local directory
    return local_dir
```

Example (Async - Download to specific path):

```python
@env.task
async def download_to_path(d: Dir) -&gt; str:
    local_dir = await d.download("/tmp/my_data/")
    return local_dir
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Optional[Union[str, Path]]` | The local path to download the directory to. If None, a temporary directory will be used and a path will be generated. |

#### download_sync()

```python
def download_sync(
    local_path: Optional[Union[str, Path]],
) -> str
```
Synchronously download the entire directory to a local path.

Use this in non-async tasks when you need to download all files in a directory to your local filesystem.

Example (Sync):

```python
@env.task
def download_directory_sync(d: Dir) -&gt; str:
    local_dir = d.download_sync()
    # Process files in the local directory
    return local_dir
```

Example (Sync - Download to specific path):

```python
@env.task
def download_to_path_sync(d: Dir) -&gt; str:
    local_dir = d.download_sync("/tmp/my_data/")
    return local_dir
```


| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Optional[Union[str, Path]]` | The local path to download the directory to. If None, a temporary directory will be used and a path will be generated. |

#### exists()

```python
def exists()
```
Asynchronously check if the directory exists.

Returns:
    True if the directory exists, False otherwise

Example (Async):

```python
@env.task
async def check_directory(d: Dir) -&gt; bool:
    if await d.exists():
        print("Directory exists!")
        return True
    return False
```


#### exists_sync()

```python
def exists_sync()
```
Synchronously check if the directory exists.

Use this in non-async tasks or when you need synchronous directory existence checking.

Returns:
    True if the directory exists, False otherwise

Example (Sync):

```python
@env.task
def check_directory_sync(d: Dir) -&gt; bool:
    if d.exists_sync():
        print("Directory exists!")
        return True
    return False
```


#### from_existing_remote()

```python
def from_existing_remote(
    remote_path: str,
    dir_cache_key: Optional[str],
) -> Dir[T]
```
Create a Dir reference from an existing remote directory.

Use this when you want to reference a directory that already exists in remote storage without uploading it.

Example:

```python
@env.task
async def process_existing_directory() -&gt; int:
    d = Dir.from_existing_remote("s3://my-bucket/data/")
    files = await d.list_files()
    return len(files)
```

Example (With cache key):

```python
@env.task
async def process_with_cache_key() -&gt; int:
    d = Dir.from_existing_remote("s3://my-bucket/data/", dir_cache_key="abc123")
    files = await d.list_files()
    return len(files)
```



| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | The remote path to the existing directory |
| `dir_cache_key` | `Optional[str]` | Optional hash value to use for cache key computation. If not specified, the cache key will be computed based on the directory's attributes. |

#### from_local()

```python
def from_local(
    local_path: Union[str, Path],
    remote_destination: Optional[str],
    dir_cache_key: Optional[str],
) -> Dir[T]
```
Asynchronously create a new Dir by uploading a local directory to remote storage.

Use this in async tasks when you have a local directory that needs to be uploaded to remote storage.

Example (Async):

```python
@env.task
async def upload_local_directory() -&gt; Dir:
    # Create a local directory with files
    os.makedirs("/tmp/data_dir", exist_ok=True)
    with open("/tmp/data_dir/file1.txt", "w") as f:
        f.write("data1")

    # Upload to remote storage
    remote_dir = await Dir.from_local("/tmp/data_dir/")
    return remote_dir
```

Example (Async - With specific destination):

```python
@env.task
async def upload_to_specific_path() -&gt; Dir:
    remote_dir = await Dir.from_local("/tmp/data_dir/", "s3://my-bucket/data/")
    return remote_dir
```

Example (Async - With cache key):

```python
@env.task
async def upload_with_cache_key() -&gt; Dir:
    remote_dir = await Dir.from_local("/tmp/data_dir/", dir_cache_key="my_cache_key_123")
    return remote_dir
```


| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Union[str, Path]` | Path to the local directory |
| `remote_destination` | `Optional[str]` | Optional remote path to store the directory. If None, a path will be automatically generated. |
| `dir_cache_key` | `Optional[str]` | Optional precomputed hash value to use for cache key computation when this Dir is used as an input to discoverable tasks. If not specified, the cache key will be based on directory attributes. |

#### from_local_sync()

```python
def from_local_sync(
    local_path: Union[str, Path],
    remote_destination: Optional[str],
    dir_cache_key: Optional[str],
) -> Dir[T]
```
Synchronously create a new Dir by uploading a local directory to remote storage.

Use this in non-async tasks when you have a local directory that needs to be uploaded to remote storage.

Example (Sync):

```python
@env.task
def upload_local_directory_sync() -&gt; Dir:
    # Create a local directory with files
    os.makedirs("/tmp/data_dir", exist_ok=True)
    with open("/tmp/data_dir/file1.txt", "w") as f:
        f.write("data1")

    # Upload to remote storage
    remote_dir = Dir.from_local_sync("/tmp/data_dir/")
    return remote_dir
```

Example (Sync - With specific destination):

```python
@env.task
def upload_to_specific_path_sync() -&gt; Dir:
    remote_dir = Dir.from_local_sync("/tmp/data_dir/", "s3://my-bucket/data/")
    return remote_dir
```

Example (Sync - With cache key):

```python
@env.task
def upload_with_cache_key_sync() -&gt; Dir:
    remote_dir = Dir.from_local_sync("/tmp/data_dir/", dir_cache_key="my_cache_key_123")
    return remote_dir
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Union[str, Path]` | Path to the local directory |
| `remote_destination` | `Optional[str]` | Optional remote path to store the directory. If None, a path will be automatically generated. |
| `dir_cache_key` | `Optional[str]` | Optional precomputed hash value to use for cache key computation when this Dir is used as an input to discoverable tasks. If not specified, the cache key will be based on directory attributes. |

#### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

#### get_file()

```python
def get_file(
    file_name: str,
) -> Optional[File[T]]
```
Asynchronously get a specific file from the directory by name.

Use this when you know the name of a specific file in the directory you want to access.

Example (Async):

```python
@env.task
async def read_specific_file(d: Dir) -&gt; str:
    file = await d.get_file("data.csv")
    if file:
        async with file.open("rb") as f:
            content = await f.read()
            return content.decode("utf-8")
    return "File not found"
```



| Parameter | Type | Description |
|-|-|-|
| `file_name` | `str` | The name of the file to get |

#### get_file_sync()

```python
def get_file_sync(
    file_name: str,
) -> Optional[File[T]]
```
Synchronously get a specific file from the directory by name.

Use this in non-async tasks when you know the name of a specific file in the directory you want to access.

Example (Sync):

```python
@env.task
def read_specific_file_sync(d: Dir) -&gt; str:
    file = d.get_file_sync("data.csv")
    if file:
        with file.open_sync("rb") as f:
            content = f.read()
            return content.decode("utf-8")
    return "File not found"
```



| Parameter | Type | Description |
|-|-|-|
| `file_name` | `str` | The name of the file to get |

#### json()

```python
def json(
    include: IncEx | None,
    exclude: IncEx | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    encoder: Callable[[Any], Any] | None,
    models_as_dict: bool,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `include` | `IncEx \| None` | |
| `exclude` | `IncEx \| None` | |
| `by_alias` | `bool` | |
| `exclude_unset` | `bool` | |
| `exclude_defaults` | `bool` | |
| `exclude_none` | `bool` | |
| `encoder` | `Callable[[Any], Any] \| None` | |
| `models_as_dict` | `bool` | |
| `dumps_kwargs` | `Any` | |

#### list_files()

```python
def list_files()
```
Asynchronously get a list of all files in the directory (non-recursive).

Use this when you need a list of all files in the top-level directory at once.

Returns:
    A list of File objects for files in the top-level directory

Example (Async):

```python
@env.task
async def count_files(d: Dir) -&gt; int:
    files = await d.list_files()
    return len(files)
```

Example (Async - Process files):

```python
@env.task
async def process_all_files(d: Dir) -&gt; list[str]:
    files = await d.list_files()
    contents = []
    for file in files:
        async with file.open("rb") as f:
            content = await f.read()
            contents.append(content.decode("utf-8"))
    return contents
```


#### list_files_sync()

```python
def list_files_sync()
```
Synchronously get a list of all files in the directory (non-recursive).

Use this in non-async tasks when you need a list of all files in the top-level directory at once.

Returns:
    A list of File objects for files in the top-level directory

Example (Sync):

```python
@env.task
def count_files_sync(d: Dir) -&gt; int:
    files = d.list_files_sync()
    return len(files)
```

Example (Sync - Process files):

```python
@env.task
def process_all_files_sync(d: Dir) -&gt; list[str]:
    files = d.list_files_sync()
    contents = []
    for file in files:
        with file.open_sync("rb") as f:
            content = f.read()
            contents.append(content.decode("utf-8"))
    return contents
```


#### model_construct()

```python
def model_construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

&gt; [!NOTE]
&gt; `model_construct()` generally respects the `model_config.extra` setting on the provided model.
&gt; That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
&gt; and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
&gt; Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
&gt; an error if extra values are passed, but they will be ignored.



| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | A set of field names that were originally explicitly set during instantiation. If provided, this is directly used for the [`model_fields_set`][pydantic.BaseModel.model_fields_set] attribute. Otherwise, the field names from the `values` argument will be used. |
| `values` | `Any` | Trusted or pre-validated data dictionary. |

#### model_copy()

```python
def model_copy(
    update: Mapping[str, Any] | None,
    deep: bool,
) -> Self
```
!!! abstract "Usage Documentation"
    [`model_copy`](../concepts/models.md#model-copy)

Returns a copy of the model.

&gt; [!NOTE]
&gt; The underlying instance's [`__dict__`][object.__dict__] attribute is copied. This
&gt; might have unexpected side effects if you store anything in it, on top of the model
&gt; fields (e.g. the value of [cached properties][functools.cached_property]).



| Parameter | Type | Description |
|-|-|-|
| `update` | `Mapping[str, Any] \| None` | |
| `deep` | `bool` | Set to `True` to make a deep copy of the model. |

#### model_dump()

```python
def model_dump(
    mode: Literal['json', 'python'] | str,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    exclude_computed_fields: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> dict[str, Any]
```
!!! abstract "Usage Documentation"
    [`model_dump`](../concepts/serialization.md#python-mode)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type | Description |
|-|-|-|
| `mode` | `Literal['json', 'python'] \| str` | The mode in which `to_python` should run. If mode is 'json', the output will only contain JSON serializable types. If mode is 'python', the output may contain non-JSON-serializable Python objects. |
| `include` | `IncEx \| None` | A set of fields to include in the output. |
| `exclude` | `IncEx \| None` | A set of fields to exclude from the output. |
| `context` | `Any \| None` | Additional context to pass to the serializer. |
| `by_alias` | `bool \| None` | Whether to use the field's alias in the dictionary key if defined. |
| `exclude_unset` | `bool` | Whether to exclude fields that have not been explicitly set. |
| `exclude_defaults` | `bool` | Whether to exclude fields that are set to their default value. |
| `exclude_none` | `bool` | Whether to exclude fields that have a value of `None`. |
| `exclude_computed_fields` | `bool` | Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |
| `round_trip` | `bool` | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised. |
| `serialize_as_any` | `bool` | Whether to serialize fields with duck-typing serialization behavior. |

#### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    ensure_ascii: bool,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    exclude_computed_fields: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> str
```
!!! abstract "Usage Documentation"
    [`model_dump_json`](../concepts/serialization.md#json-mode)

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type | Description |
|-|-|-|
| `indent` | `int \| None` | Indentation to use in the JSON output. If None is passed, the output will be compact. |
| `ensure_ascii` | `bool` | If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |
| `include` | `IncEx \| None` | Field(s) to include in the JSON output. |
| `exclude` | `IncEx \| None` | Field(s) to exclude from the JSON output. |
| `context` | `Any \| None` | Additional context to pass to the serializer. |
| `by_alias` | `bool \| None` | Whether to serialize using field aliases. |
| `exclude_unset` | `bool` | Whether to exclude fields that have not been explicitly set. |
| `exclude_defaults` | `bool` | Whether to exclude fields that are set to their default value. |
| `exclude_none` | `bool` | Whether to exclude fields that have a value of `None`. |
| `exclude_computed_fields` | `bool` | Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |
| `round_trip` | `bool` | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised. |
| `serialize_as_any` | `bool` | Whether to serialize fields with duck-typing serialization behavior. |

#### model_json_schema()

```python
def model_json_schema(
    by_alias: bool,
    ref_template: str,
    schema_generator: type[GenerateJsonSchema],
    mode: JsonSchemaMode,
    union_format: Literal['any_of', 'primitive_type_array'],
) -> dict[str, Any]
```
Generates a JSON schema for a model class.



| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | Whether to use attribute aliases or not. |
| `ref_template` | `str` | The reference template. - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf) keyword to combine schemas (the default). - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type) keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`. |
| `schema_generator` | `type[GenerateJsonSchema]` | To override the logic used to generate the JSON schema, as a subclass of `GenerateJsonSchema` with your desired modifications |
| `mode` | `JsonSchemaMode` | The mode in which to generate the schema. |
| `union_format` | `Literal['any_of', 'primitive_type_array']` | |

#### model_parametrized_name()

```python
def model_parametrized_name(
    params: tuple[type[Any], ...],
) -> str
```
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.



| Parameter | Type | Description |
|-|-|-|
| `params` | `tuple[type[Any], ...]` | Tuple of types of the class. Given a generic class `Model` with 2 type variables and a concrete model `Model[str, int]`, the value `(str, int)` would be passed to `params`. |

#### model_post_init()

```python
def model_post_init(
    context: Any,
)
```
Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.


| Parameter | Type | Description |
|-|-|-|
| `context` | `Any` | |

#### model_rebuild()

```python
def model_rebuild(
    force: bool,
    raise_errors: bool,
    _parent_namespace_depth: int,
    _types_namespace: MappingNamespace | None,
) -> bool | None
```
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.



| Parameter | Type | Description |
|-|-|-|
| `force` | `bool` | Whether to force the rebuilding of the model schema, defaults to `False`. |
| `raise_errors` | `bool` | Whether to raise errors, defaults to `True`. |
| `_parent_namespace_depth` | `int` | The depth level of the parent namespace, defaults to 2. |
| `_types_namespace` | `MappingNamespace \| None` | The types namespace, defaults to `None`. |

#### model_validate()

```python
def model_validate(
    obj: Any,
    strict: bool | None,
    extra: ExtraValues | None,
    from_attributes: bool | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `from_attributes` | `bool \| None` | Whether to extract data from object attributes. |
| `context` | `Any \| None` | Additional context to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    extra: ExtraValues | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
!!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `json_data` | `str \| bytes \| bytearray` | The JSON data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    extra: ExtraValues | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object containing string data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### parse_file()

```python
def parse_file(
    path: str | Path,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str \| Path` | |
| `content_type` | `str \| None` | |
| `encoding` | `str` | |
| `proto` | `DeprecatedParseProtocol \| None` | |
| `allow_pickle` | `bool` | |

#### parse_obj()

```python
def parse_obj(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

#### parse_raw()

```python
def parse_raw(
    b: str | bytes,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `b` | `str \| bytes` | |
| `content_type` | `str \| None` | |
| `encoding` | `str` | |
| `proto` | `DeprecatedParseProtocol \| None` | |
| `allow_pickle` | `bool` | |

#### pre_init()

```python
def pre_init(
    data,
)
```
Internal: Pydantic validator to set default name from path. Not intended for direct use.


| Parameter | Type | Description |
|-|-|-|
| `data` |  | |

#### schema()

```python
def schema(
    by_alias: bool,
    ref_template: str,
) -> Dict[str, Any]
```
| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | |
| `ref_template` | `str` | |

#### schema_json()

```python
def schema_json(
    by_alias: bool,
    ref_template: str,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | |
| `ref_template` | `str` | |
| `dumps_kwargs` | `Any` | |

#### schema_match()

```python
def schema_match(
    incoming: dict,
)
```
Internal: Check if incoming schema matches Dir schema. Not intended for direct use.


| Parameter | Type | Description |
|-|-|-|
| `incoming` | `dict` | |

#### update_forward_refs()

```python
def update_forward_refs(
    localns: Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `localns` | `Any` | |

#### validate()

```python
def validate(
    value: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `Any` | |

#### walk()

```python
def walk(
    recursive: bool,
    max_depth: Optional[int],
) -> AsyncIterator[File[T]]
```
Asynchronously walk through the directory and yield File objects.

Use this to iterate through all files in a directory. Each yielded File can be read directly without
downloading.

Example (Async - Recursive):

```python
@env.task
async def list_all_files(d: Dir) -&gt; list[str]:
    file_names = []
    async for file in d.walk(recursive=True):
        file_names.append(file.name)
    return file_names
```

Example (Async - Non-recursive):

```python
@env.task
async def list_top_level_files(d: Dir) -&gt; list[str]:
    file_names = []
    async for file in d.walk(recursive=False):
        file_names.append(file.name)
    return file_names
```

Example (Async - With max depth):

```python
@env.task
async def list_files_max_depth(d: Dir) -&gt; list[str]:
    file_names = []
    async for file in d.walk(recursive=True, max_depth=2):
        file_names.append(file.name)
    return file_names
```



| Parameter | Type | Description |
|-|-|-|
| `recursive` | `bool` | If True, recursively walk subdirectories. If False, only list files in the top-level directory. |
| `max_depth` | `Optional[int]` | Maximum depth for recursive walking. If None, walk through all subdirectories. |

#### walk_sync()

```python
def walk_sync(
    recursive: bool,
    file_pattern: str,
    max_depth: Optional[int],
) -> Iterator[File[T]]
```
Synchronously walk through the directory and yield File objects.

Use this in non-async tasks to iterate through all files in a directory.

Example (Sync - Recursive):

```python
@env.task
def list_all_files_sync(d: Dir) -&gt; list[str]:
    file_names = []
    for file in d.walk_sync(recursive=True):
        file_names.append(file.name)
    return file_names
```

Example (Sync - With file pattern):

```python
@env.task
def list_text_files(d: Dir) -&gt; list[str]:
    file_names = []
    for file in d.walk_sync(recursive=True, file_pattern="*.txt"):
        file_names.append(file.name)
    return file_names
```

Example (Sync - Non-recursive with max depth):

```python
@env.task
def list_files_limited(d: Dir) -&gt; list[str]:
    file_names = []
    for file in d.walk_sync(recursive=True, max_depth=2):
        file_names.append(file.name)
    return file_names
```



| Parameter | Type | Description |
|-|-|-|
| `recursive` | `bool` | If True, recursively walk subdirectories. If False, only list files in the top-level directory. |
| `file_pattern` | `str` | Glob pattern to filter files (e.g., "*.txt", "*.csv"). Default is "*" (all files). |
| `max_depth` | `Optional[int]` | Maximum depth for recursive walking. If None, walk through all subdirectories. |

### Properties

| Property | Type | Description |
|-|-|-|
| `model_extra` | `None` | Get extra fields set during validation.  Returns:     A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. |
| `model_fields_set` | `None` | Returns the set of fields that have been explicitly set on this model instance.  Returns:     A set of strings representing the fields that have been set,         i.e. that were not filled from defaults. |

## flyte.io.File

A generic file class representing a file with a specified format.
Provides both async and sync interfaces for file operations. All methods without _sync suffix are async.

The class should be instantiated using one of the class methods. The constructor should be used only to
instantiate references to existing remote objects.

The generic type T represents the format of the file.

Important methods:
- `from_existing_remote`: Create a File object from an existing remote file.
- `new_remote`: Create a new File reference for a remote file that will be written to.

**Asynchronous methods**:
- `open`: Asynchronously open the file and return a file-like object.
- `download`: Asynchronously download the file to a local path.
- `from_local`: Asynchronously create a File object from a local file, uploading it to remote storage.
- `exists`: Asynchronously check if the file exists.

**Synchronous methods** (suffixed with `_sync`):
- `open_sync`: Synchronously open the file and return a file-like object.
- `download_sync`: Synchronously download the file to a local path.
- `from_local_sync`: Synchronously create a File object from a local file, uploading it to remote storage.
- `exists_sync`: Synchronously check if the file exists.

Example: Read a file input in a Task (Async).

```python
@env.task
async def read_file(file: File) -&gt; str:
    async with file.open("rb") as f:
        content = bytes(await f.read())
        return content.decode("utf-8")
```

Example: Read a file input in a Task (Sync).

```python
@env.task
def read_file_sync(file: File) -&gt; str:
    with file.open_sync("rb") as f:
        content = f.read()
        return content.decode("utf-8")
```

Example: Write a file by streaming it directly to blob storage (Async).

```python
@env.task
async def write_file() -&gt; File:
    file = File.new_remote()
    async with file.open("wb") as f:
        await f.write(b"Hello, World!")
    return file
```

Example: Upload a local file to remote storage (Async).

```python
@env.task
async def upload_file() -&gt; File:
    # Write to local file first
    with open("/tmp/data.csv", "w") as f:
        f.write("col1,col2\n1,2\n3,4\n")
    # Upload to remote storage
    return await File.from_local("/tmp/data.csv")
```

Example: Upload a local file to remote storage (Sync).

```python
@env.task
def upload_file_sync() -&gt; File:
    # Write to local file first
    with open("/tmp/data.csv", "w") as f:
        f.write("col1,col2\n1,2\n3,4\n")
    # Upload to remote storage
    return File.from_local_sync("/tmp/data.csv")
```

Example: Download a file to local storage (Async).

```python
@env.task
async def download_file(file: File) -&gt; str:
    local_path = await file.download()
    # Process the local file
    with open(local_path, "r") as f:
        return f.read()
```

Example: Download a file to local storage (Sync).

```python
@env.task
def download_file_sync(file: File) -&gt; str:
    local_path = file.download_sync()
    # Process the local file
    with open(local_path, "r") as f:
        return f.read()
```

Example: Reference an existing remote file.

```python
@env.task
async def process_existing_file() -&gt; str:
    file = File.from_existing_remote("s3://my-bucket/data.csv")
    async with file.open("rb") as f:
        content = await f.read()
        return content.decode("utf-8")
```

Example: Check if a file exists (Async).

```python
@env.task
async def check_file(file: File) -&gt; bool:
    return await file.exists()
```

Example: Check if a file exists (Sync).

```python
@env.task
def check_file_sync(file: File) -&gt; bool:
    return file.exists_sync()
```

Example: Pass through a file without copying.

```python
@env.task
async def pass_through(file: File) -&gt; File:
    # No copy occurs - just passes the reference
    return file
```



```python
class File(
    data: Any,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `data` | `Any` | |

### Methods

| Method | Description |
|-|-|
| [`construct()`](#construct) |  |
| [`copy()`](#copy) | Returns a copy of the model. |
| [`dict()`](#dict) |  |
| [`download()`](#download) | Asynchronously download the file to a local path. |
| [`download_sync()`](#download_sync) | Synchronously download the file to a local path. |
| [`exists()`](#exists) | Asynchronously check if the file exists. |
| [`exists_sync()`](#exists_sync) | Synchronously check if the file exists. |
| [`from_existing_remote()`](#from_existing_remote) | Create a File reference from an existing remote file. |
| [`from_local()`](#from_local) | Asynchronously create a new File object from a local file by uploading it to remote storage. |
| [`from_local_sync()`](#from_local_sync) | Synchronously create a new File object from a local file by uploading it to remote storage. |
| [`from_orm()`](#from_orm) |  |
| [`json()`](#json) |  |
| [`model_construct()`](#model_construct) | Creates a new instance of the `Model` class with validated data. |
| [`model_copy()`](#model_copy) | !!! abstract "Usage Documentation". |
| [`model_dump()`](#model_dump) | !!! abstract "Usage Documentation". |
| [`model_dump_json()`](#model_dump_json) | !!! abstract "Usage Documentation". |
| [`model_json_schema()`](#model_json_schema) | Generates a JSON schema for a model class. |
| [`model_parametrized_name()`](#model_parametrized_name) | Compute the class name for parametrizations of generic classes. |
| [`model_post_init()`](#model_post_init) | Override this method to perform additional initialization after `__init__` and `model_construct`. |
| [`model_rebuild()`](#model_rebuild) | Try to rebuild the pydantic-core schema for the model. |
| [`model_validate()`](#model_validate) | Validate a pydantic model instance. |
| [`model_validate_json()`](#model_validate_json) | !!! abstract "Usage Documentation". |
| [`model_validate_strings()`](#model_validate_strings) | Validate the given object with string data against the Pydantic model. |
| [`new_remote()`](#new_remote) | Create a new File reference for a remote file that will be written to. |
| [`open()`](#open) | Asynchronously open the file and return a file-like object. |
| [`open_sync()`](#open_sync) | Synchronously open the file and return a file-like object. |
| [`parse_file()`](#parse_file) |  |
| [`parse_obj()`](#parse_obj) |  |
| [`parse_raw()`](#parse_raw) |  |
| [`pre_init()`](#pre_init) | Internal: Pydantic validator to set default name from path. |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
| [`schema_match()`](#schema_match) | Internal: Check if incoming schema matches File schema. |
| [`update_forward_refs()`](#update_forward_refs) |  |
| [`validate()`](#validate) |  |


#### construct()

```python
def construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | |
| `values` | `Any` | |

#### copy()

```python
def copy(
    include: AbstractSetIntStr | MappingIntStrAny | None,
    exclude: AbstractSetIntStr | MappingIntStrAny | None,
    update: Dict[str, Any] | None,
    deep: bool,
) -> Self
```
Returns a copy of the model.

&gt; [!WARNING] Deprecated
&gt; This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```python {test="skip" lint="skip"}
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```



| Parameter | Type | Description |
|-|-|-|
| `include` | `AbstractSetIntStr \| MappingIntStrAny \| None` | Optional set or mapping specifying which fields to include in the copied model. |
| `exclude` | `AbstractSetIntStr \| MappingIntStrAny \| None` | Optional set or mapping specifying which fields to exclude in the copied model. |
| `update` | `Dict[str, Any] \| None` | Optional dictionary of field-value pairs to override field values in the copied model. |
| `deep` | `bool` | If True, the values of fields that are Pydantic models will be deep-copied. |

#### dict()

```python
def dict(
    include: IncEx | None,
    exclude: IncEx | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
) -> Dict[str, Any]
```
| Parameter | Type | Description |
|-|-|-|
| `include` | `IncEx \| None` | |
| `exclude` | `IncEx \| None` | |
| `by_alias` | `bool` | |
| `exclude_unset` | `bool` | |
| `exclude_defaults` | `bool` | |
| `exclude_none` | `bool` | |

#### download()

```python
def download(
    local_path: Optional[Union[str, Path]],
) -> str
```
Asynchronously download the file to a local path.

Use this when you need to download a remote file to your local filesystem for processing.

Example (Async):

```python
@env.task
async def download_and_process(f: File) -&gt; str:
    local_path = await f.download()
    # Now process the local file
    with open(local_path, "r") as fh:
        return fh.read()
```

Example (Download to specific path):

```python
@env.task
async def download_to_path(f: File) -&gt; str:
    local_path = await f.download("/tmp/myfile.csv")
    return local_path
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Optional[Union[str, Path]]` | The local path to download the file to. If None, a temporary directory will be used and a path will be generated. |

#### download_sync()

```python
def download_sync(
    local_path: Optional[Union[str, Path]],
) -> str
```
Synchronously download the file to a local path.

Use this in non-async tasks when you need to download a remote file to your local filesystem.

Example (Sync):

```python
@env.task
def download_and_process_sync(f: File) -&gt; str:
    local_path = f.download_sync()
    # Now process the local file
    with open(local_path, "r") as fh:
        return fh.read()
```

Example (Download to specific path):

```python
@env.task
def download_to_path_sync(f: File) -&gt; str:
    local_path = f.download_sync("/tmp/myfile.csv")
    return local_path
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Optional[Union[str, Path]]` | The local path to download the file to. If None, a temporary directory will be used and a path will be generated. |

#### exists()

```python
def exists()
```
Asynchronously check if the file exists.

Example (Async):

```python
@env.task
async def check_file(f: File) -&gt; bool:
    if await f.exists():
        print("File exists!")
        return True
    return False
```

Returns:
    True if the file exists, False otherwise


#### exists_sync()

```python
def exists_sync()
```
Synchronously check if the file exists.

Use this in non-async tasks or when you need synchronous file existence checking.

Example (Sync):

```python
@env.task
def check_file_sync(f: File) -&gt; bool:
    if f.exists_sync():
        print("File exists!")
        return True
    return False
```

Returns:
    True if the file exists, False otherwise


#### from_existing_remote()

```python
def from_existing_remote(
    remote_path: str,
    file_cache_key: Optional[str],
) -> File[T]
```
Create a File reference from an existing remote file.

Use this when you want to reference a file that already exists in remote storage without uploading it.

Example:

```python
@env.task
async def process_existing_file() -&gt; str:
    file = File.from_existing_remote("s3://my-bucket/data.csv")
    async with file.open("rb") as f:
        content = await f.read()
    return content.decode("utf-8")
```



| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | The remote path to the existing file |
| `file_cache_key` | `Optional[str]` | Optional hash value to use for cache key computation. If not specified, the cache key will be computed based on the file's attributes (path, name, format). |

#### from_local()

```python
def from_local(
    local_path: Union[str, Path],
    remote_destination: Optional[str],
    hash_method: Optional[HashMethod | str],
) -> File[T]
```
Asynchronously create a new File object from a local file by uploading it to remote storage.

Use this in async tasks when you have a local file that needs to be uploaded to remote storage.

Example (Async):

```python
@env.task
async def upload_local_file() -&gt; File:
    # Create a local file
    async with aiofiles.open("/tmp/data.csv", "w") as f:
        await f.write("col1,col2




    # Upload to remote storage
    remote_file = await File.from_local("/tmp/data.csv")
    return remote_file
```

Example (With specific destination):

```python
@env.task
async def upload_to_specific_path() -&gt; File:
    remote_file = await File.from_local("/tmp/data.csv", "s3://my-bucket/data.csv")
    return remote_file
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Union[str, Path]` | Path to the local file |
| `remote_destination` | `Optional[str]` | Optional remote path to store the file. If None, a path will be automatically generated. |
| `hash_method` | `Optional[HashMethod \| str]` | Optional HashMethod or string to use for cache key computation. If a string is provided, it will be used as a precomputed cache key. If a HashMethod is provided, it will compute the hash during upload. If not specified, the cache key will be based on file attributes. |

#### from_local_sync()

```python
def from_local_sync(
    local_path: Union[str, Path],
    remote_destination: Optional[str],
    hash_method: Optional[HashMethod | str],
) -> File[T]
```
Synchronously create a new File object from a local file by uploading it to remote storage.

Use this in non-async tasks when you have a local file that needs to be uploaded to remote storage.

Example (Sync):

```python
@env.task
def upload_local_file_sync() -&gt; File:
    # Create a local file
    with open("/tmp/data.csv", "w") as f:
        f.write("col1,col2




    # Upload to remote storage
    remote_file = File.from_local_sync("/tmp/data.csv")
    return remote_file
```

Example (With specific destination):

```python
@env.task
def upload_to_specific_path() -&gt; File:
    remote_file = File.from_local_sync("/tmp/data.csv", "s3://my-bucket/data.csv")
    return remote_file
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Union[str, Path]` | Path to the local file |
| `remote_destination` | `Optional[str]` | Optional remote path to store the file. If None, a path will be automatically generated. |
| `hash_method` | `Optional[HashMethod \| str]` | Optional HashMethod or string to use for cache key computation. If a string is provided, it will be used as a precomputed cache key. If a HashMethod is provided, it will compute the hash during upload. If not specified, the cache key will be based on file attributes. |

#### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

#### json()

```python
def json(
    include: IncEx | None,
    exclude: IncEx | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    encoder: Callable[[Any], Any] | None,
    models_as_dict: bool,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `include` | `IncEx \| None` | |
| `exclude` | `IncEx \| None` | |
| `by_alias` | `bool` | |
| `exclude_unset` | `bool` | |
| `exclude_defaults` | `bool` | |
| `exclude_none` | `bool` | |
| `encoder` | `Callable[[Any], Any] \| None` | |
| `models_as_dict` | `bool` | |
| `dumps_kwargs` | `Any` | |

#### model_construct()

```python
def model_construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
Creates a new instance of the `Model` class with validated data.

Creates a new model setting `__dict__` and `__pydantic_fields_set__` from trusted or pre-validated data.
Default values are respected, but no other validation is performed.

&gt; [!NOTE]
&gt; `model_construct()` generally respects the `model_config.extra` setting on the provided model.
&gt; That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
&gt; and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
&gt; Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
&gt; an error if extra values are passed, but they will be ignored.



| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | A set of field names that were originally explicitly set during instantiation. If provided, this is directly used for the [`model_fields_set`][pydantic.BaseModel.model_fields_set] attribute. Otherwise, the field names from the `values` argument will be used. |
| `values` | `Any` | Trusted or pre-validated data dictionary. |

#### model_copy()

```python
def model_copy(
    update: Mapping[str, Any] | None,
    deep: bool,
) -> Self
```
!!! abstract "Usage Documentation"
    [`model_copy`](../concepts/models.md#model-copy)

Returns a copy of the model.

&gt; [!NOTE]
&gt; The underlying instance's [`__dict__`][object.__dict__] attribute is copied. This
&gt; might have unexpected side effects if you store anything in it, on top of the model
&gt; fields (e.g. the value of [cached properties][functools.cached_property]).



| Parameter | Type | Description |
|-|-|-|
| `update` | `Mapping[str, Any] \| None` | |
| `deep` | `bool` | Set to `True` to make a deep copy of the model. |

#### model_dump()

```python
def model_dump(
    mode: Literal['json', 'python'] | str,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    exclude_computed_fields: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> dict[str, Any]
```
!!! abstract "Usage Documentation"
    [`model_dump`](../concepts/serialization.md#python-mode)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type | Description |
|-|-|-|
| `mode` | `Literal['json', 'python'] \| str` | The mode in which `to_python` should run. If mode is 'json', the output will only contain JSON serializable types. If mode is 'python', the output may contain non-JSON-serializable Python objects. |
| `include` | `IncEx \| None` | A set of fields to include in the output. |
| `exclude` | `IncEx \| None` | A set of fields to exclude from the output. |
| `context` | `Any \| None` | Additional context to pass to the serializer. |
| `by_alias` | `bool \| None` | Whether to use the field's alias in the dictionary key if defined. |
| `exclude_unset` | `bool` | Whether to exclude fields that have not been explicitly set. |
| `exclude_defaults` | `bool` | Whether to exclude fields that are set to their default value. |
| `exclude_none` | `bool` | Whether to exclude fields that have a value of `None`. |
| `exclude_computed_fields` | `bool` | Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |
| `round_trip` | `bool` | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised. |
| `serialize_as_any` | `bool` | Whether to serialize fields with duck-typing serialization behavior. |

#### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    ensure_ascii: bool,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    exclude_computed_fields: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> str
```
!!! abstract "Usage Documentation"
    [`model_dump_json`](../concepts/serialization.md#json-mode)

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type | Description |
|-|-|-|
| `indent` | `int \| None` | Indentation to use in the JSON output. If None is passed, the output will be compact. |
| `ensure_ascii` | `bool` | If `True`, the output is guaranteed to have all incoming non-ASCII characters escaped. If `False` (the default), these characters will be output as-is. |
| `include` | `IncEx \| None` | Field(s) to include in the JSON output. |
| `exclude` | `IncEx \| None` | Field(s) to exclude from the JSON output. |
| `context` | `Any \| None` | Additional context to pass to the serializer. |
| `by_alias` | `bool \| None` | Whether to serialize using field aliases. |
| `exclude_unset` | `bool` | Whether to exclude fields that have not been explicitly set. |
| `exclude_defaults` | `bool` | Whether to exclude fields that are set to their default value. |
| `exclude_none` | `bool` | Whether to exclude fields that have a value of `None`. |
| `exclude_computed_fields` | `bool` | Whether to exclude computed fields. While this can be useful for round-tripping, it is usually recommended to use the dedicated `round_trip` parameter instead. |
| `round_trip` | `bool` | If True, dumped values should be valid as input for non-idempotent types such as Json[T]. |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError]. |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`][pydantic_core.PydanticSerializationError] error is raised. |
| `serialize_as_any` | `bool` | Whether to serialize fields with duck-typing serialization behavior. |

#### model_json_schema()

```python
def model_json_schema(
    by_alias: bool,
    ref_template: str,
    schema_generator: type[GenerateJsonSchema],
    mode: JsonSchemaMode,
    union_format: Literal['any_of', 'primitive_type_array'],
) -> dict[str, Any]
```
Generates a JSON schema for a model class.



| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | Whether to use attribute aliases or not. |
| `ref_template` | `str` | The reference template. - `'any_of'`: Use the [`anyOf`](https://json-schema.org/understanding-json-schema/reference/combining#anyOf) keyword to combine schemas (the default). - `'primitive_type_array'`: Use the [`type`](https://json-schema.org/understanding-json-schema/reference/type) keyword as an array of strings, containing each type of the combination. If any of the schemas is not a primitive type (`string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`. |
| `schema_generator` | `type[GenerateJsonSchema]` | To override the logic used to generate the JSON schema, as a subclass of `GenerateJsonSchema` with your desired modifications |
| `mode` | `JsonSchemaMode` | The mode in which to generate the schema. |
| `union_format` | `Literal['any_of', 'primitive_type_array']` | |

#### model_parametrized_name()

```python
def model_parametrized_name(
    params: tuple[type[Any], ...],
) -> str
```
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.



| Parameter | Type | Description |
|-|-|-|
| `params` | `tuple[type[Any], ...]` | Tuple of types of the class. Given a generic class `Model` with 2 type variables and a concrete model `Model[str, int]`, the value `(str, int)` would be passed to `params`. |

#### model_post_init()

```python
def model_post_init(
    context: Any,
)
```
Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.


| Parameter | Type | Description |
|-|-|-|
| `context` | `Any` | |

#### model_rebuild()

```python
def model_rebuild(
    force: bool,
    raise_errors: bool,
    _parent_namespace_depth: int,
    _types_namespace: MappingNamespace | None,
) -> bool | None
```
Try to rebuild the pydantic-core schema for the model.

This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
the initial attempt to build the schema, and automatic rebuilding fails.



| Parameter | Type | Description |
|-|-|-|
| `force` | `bool` | Whether to force the rebuilding of the model schema, defaults to `False`. |
| `raise_errors` | `bool` | Whether to raise errors, defaults to `True`. |
| `_parent_namespace_depth` | `int` | The depth level of the parent namespace, defaults to 2. |
| `_types_namespace` | `MappingNamespace \| None` | The types namespace, defaults to `None`. |

#### model_validate()

```python
def model_validate(
    obj: Any,
    strict: bool | None,
    extra: ExtraValues | None,
    from_attributes: bool | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `from_attributes` | `bool \| None` | Whether to extract data from object attributes. |
| `context` | `Any \| None` | Additional context to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    extra: ExtraValues | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
!!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `json_data` | `str \| bytes \| bytearray` | The JSON data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    extra: ExtraValues | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | The object containing string data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value][pydantic.ConfigDict.extra] for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

#### new_remote()

```python
def new_remote(
    file_name: Optional[str],
    hash_method: Optional[HashMethod | str],
) -> File[T]
```
Create a new File reference for a remote file that will be written to.

Use this when you want to create a new file and write to it directly without creating a local file first.

Example (Async):

```python
@env.task
async def create_csv() -&gt; File:
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    file = File.new_remote()
    async with file.open("wb") as f:
        df.to_csv(f)
    return file
```



| Parameter | Type | Description |
|-|-|-|
| `file_name` | `Optional[str]` | Optional string specifying a remote file name. If not set, a generated file name will be returned. |
| `hash_method` | `Optional[HashMethod \| str]` | Optional HashMethod or string to use for cache key computation. If a string is provided, it will be used as a precomputed cache key. If a HashMethod is provided, it will be used to compute the hash as data is written. |

#### open()

```python
def open(
    mode: str,
    block_size: Optional[int],
    cache_type: str,
    cache_options: Optional[dict],
    compression: Optional[str],
    kwargs,
) -> AsyncGenerator[Union[AsyncWritableFile, AsyncReadableFile, 'HashingWriter'], None]
```
Asynchronously open the file and return a file-like object.

Use this method in async tasks to read from or write to files directly.

Example (Async Read):

```python
@env.task
async def read_file(f: File) -&gt; str:
    async with f.open("rb") as fh:
        content = bytes(await fh.read())
        return content.decode("utf-8")
```

Example (Async Write):

```python
@env.task
async def write_file() -&gt; File:
    f = File.new_remote()
    async with f.open("wb") as fh:
        await fh.write(b"Hello, World!")
    return f
```

Example (Streaming Read):

```python
@env.task
async def stream_read(f: File) -&gt; str:
    content_parts = []
    async with f.open("rb", block_size=1024) as fh:
        while True:
            chunk = await fh.read()
            if not chunk:
                break
            content_parts.append(chunk)
    return b"".join(content_parts).decode("utf-8")
```



| Parameter | Type | Description |
|-|-|-|
| `mode` | `str` | |
| `block_size` | `Optional[int]` | Size of blocks for reading in bytes. Useful for streaming large files. |
| `cache_type` | `str` | Caching mechanism to use ('readahead', 'mmap', 'bytes', 'none') |
| `cache_options` | `Optional[dict]` | Dictionary of options for the cache |
| `compression` | `Optional[str]` | Compression format or None for auto-detection |
| `kwargs` | `**kwargs` | |

#### open_sync()

```python
def open_sync(
    mode: str,
    block_size: Optional[int],
    cache_type: str,
    cache_options: Optional[dict],
    compression: Optional[str],
    kwargs,
) -> Generator[IO[Any], None, None]
```
Synchronously open the file and return a file-like object.

Use this method in non-async tasks to read from or write to files directly.

Example (Sync Read):

```python
@env.task
def read_file_sync(f: File) -&gt; str:
    with f.open_sync("rb") as fh:
        content = fh.read()
        return content.decode("utf-8")
```

Example (Sync Write):

```python
@env.task
def write_file_sync() -&gt; File:
    f = File.new_remote()
    with f.open_sync("wb") as fh:
        fh.write(b"Hello, World!")
    return f
```



| Parameter | Type | Description |
|-|-|-|
| `mode` | `str` | |
| `block_size` | `Optional[int]` | Size of blocks for reading in bytes. Useful for streaming large files. |
| `cache_type` | `str` | Caching mechanism to use ('readahead', 'mmap', 'bytes', 'none') |
| `cache_options` | `Optional[dict]` | Dictionary of options for the cache |
| `compression` | `Optional[str]` | Compression format or None for auto-detection |
| `kwargs` | `**kwargs` | |

#### parse_file()

```python
def parse_file(
    path: str | Path,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str \| Path` | |
| `content_type` | `str \| None` | |
| `encoding` | `str` | |
| `proto` | `DeprecatedParseProtocol \| None` | |
| `allow_pickle` | `bool` | |

#### parse_obj()

```python
def parse_obj(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

#### parse_raw()

```python
def parse_raw(
    b: str | bytes,
    content_type: str | None,
    encoding: str,
    proto: DeprecatedParseProtocol | None,
    allow_pickle: bool,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `b` | `str \| bytes` | |
| `content_type` | `str \| None` | |
| `encoding` | `str` | |
| `proto` | `DeprecatedParseProtocol \| None` | |
| `allow_pickle` | `bool` | |

#### pre_init()

```python
def pre_init(
    data,
)
```
Internal: Pydantic validator to set default name from path. Not intended for direct use.


| Parameter | Type | Description |
|-|-|-|
| `data` |  | |

#### schema()

```python
def schema(
    by_alias: bool,
    ref_template: str,
) -> Dict[str, Any]
```
| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | |
| `ref_template` | `str` | |

#### schema_json()

```python
def schema_json(
    by_alias: bool,
    ref_template: str,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `by_alias` | `bool` | |
| `ref_template` | `str` | |
| `dumps_kwargs` | `Any` | |

#### schema_match()

```python
def schema_match(
    incoming: dict,
)
```
Internal: Check if incoming schema matches File schema. Not intended for direct use.


| Parameter | Type | Description |
|-|-|-|
| `incoming` | `dict` | |

#### update_forward_refs()

```python
def update_forward_refs(
    localns: Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `localns` | `Any` | |

#### validate()

```python
def validate(
    value: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `Any` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `model_extra` | `None` | Get extra fields set during validation.  Returns:     A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. |
| `model_fields_set` | `None` | Returns the set of fields that have been explicitly set on this model instance.  Returns:     A set of strings representing the fields that have been set,         i.e. that were not filled from defaults. |

