---
title: union.io
version: 0.1.0
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# union.io


## IO data types

This package contains additional data types beyond the primitive data types in python to abstract data flow
of large datasets in Union.

## Directory

### Classes

| Class | Description |
|-|-|
| [`Dir`](.././union.io#unioniodir) | A generic directory class representing a directory with files of a specified format. |
| [`File`](.././union.io#unioniofile) | A generic file class representing a file with a specified format. |

## union.io.Dir

A generic directory class representing a directory with files of a specified format.
Provides both async and sync interfaces for directory operations.

The generic type T represents the format of the files in the directory.

Example:
    ```python
    # Async usage
    from pandas import DataFrame
    data_dir = Dir[DataFrame](path="s3://my-bucket/data/")

    # Walk through files
    async for file in data_dir.walk():
        async with file.open() as f:
            content = await f.read()

    # Sync alternative
    for file in data_dir.walk_sync():
        with file.open_sync() as f:
            content = f.read()
    ```


```python
class Dir(
    path: str,
    name: Optional[str],
)
```
Create a new Dir reference.



| Parameter | Type |
|-|-|
| `path` | `str` |
| `name` | `Optional[str]` |

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
| [`from_local()`](#from_local) | Asynchronously create a new Dir by uploading a local directory to the configured remote store. |
| [`from_local_sync()`](#from_local_sync) | Synchronously create a new Dir by uploading a local directory to the configured remote store. |
| [`from_orm()`](#from_orm) |  |
| [`get_file()`](#get_file) | Asynchronously get a specific file from the directory. |
| [`get_file_sync()`](#get_file_sync) | Synchronously get a specific file from the directory. |
| [`json()`](#json) |  |
| [`list_files()`](#list_files) | Asynchronously get a list of all files in the directory (non-recursive). |
| [`list_files_sync()`](#list_files_sync) | Synchronously get a list of all files in the directory (non-recursive). |
| [`model_construct()`](#model_construct) | Creates a new instance of the `Model` class with validated data. |
| [`model_copy()`](#model_copy) | Usage docs: https://docs. |
| [`model_dump()`](#model_dump) | Usage docs: https://docs. |
| [`model_dump_json()`](#model_dump_json) | Usage docs: https://docs. |
| [`model_json_schema()`](#model_json_schema) | Generates a JSON schema for a model class. |
| [`model_parametrized_name()`](#model_parametrized_name) | Compute the class name for parametrizations of generic classes. |
| [`model_post_init()`](#model_post_init) | Override this method to perform additional initialization after `__init__` and `model_construct`. |
| [`model_rebuild()`](#model_rebuild) | Try to rebuild the pydantic-core schema for the model. |
| [`model_validate()`](#model_validate) | Validate a pydantic model instance. |
| [`model_validate_json()`](#model_validate_json) | Usage docs: https://docs. |
| [`model_validate_strings()`](#model_validate_strings) | Validate the given object with string data against the Pydantic model. |
| [`parse_file()`](#parse_file) |  |
| [`parse_obj()`](#parse_obj) |  |
| [`parse_raw()`](#parse_raw) |  |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
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
| Parameter | Type |
|-|-|
| `_fields_set` | `set[str] \| None` |
| `values` | `Any` |

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

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```python {test="skip" lint="skip"}
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```



| Parameter | Type |
|-|-|
| `include` | `AbstractSetIntStr \| MappingIntStrAny \| None` |
| `exclude` | `AbstractSetIntStr \| MappingIntStrAny \| None` |
| `update` | `Dict[str, Any] \| None` |
| `deep` | `bool` |

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
| Parameter | Type |
|-|-|
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |

#### download()

```python
def download(
    local_path: Optional[Union[str, Path]],
) -> str
```
Asynchronously download the entire directory to a local path.



| Parameter | Type |
|-|-|
| `local_path` | `Optional[Union[str, Path]]` |

#### download_sync()

```python
def download_sync(
    local_path: Optional[Union[str, Path]],
) -> str
```
Synchronously download the entire directory to a local path.



| Parameter | Type |
|-|-|
| `local_path` | `Optional[Union[str, Path]]` |

#### exists()

```python
def exists()
```
Asynchronously check if the directory exists.

Returns:
    True if the directory exists, False otherwise

Example:
    ```python
    if await directory.exists():
        # Process the directory
    ```


#### exists_sync()

```python
def exists_sync()
```
Synchronously check if the directory exists.

Returns:
    True if the directory exists, False otherwise

Example:
    ```python
    if directory.exists_sync():
        # Process the directory
    ```


#### from_local()

```python
def from_local(
    local_path: Union[str, Path],
    remote_path: Optional[str],
) -> Dir[T]
```
Asynchronously create a new Dir by uploading a local directory to the configured remote store.



| Parameter | Type |
|-|-|
| `local_path` | `Union[str, Path]` |
| `remote_path` | `Optional[str]` |

#### from_local_sync()

```python
def from_local_sync(
    local_path: Union[str, Path],
    remote_path: Optional[str],
) -> Dir[T]
```
Synchronously create a new Dir by uploading a local directory to the configured remote store.



| Parameter | Type |
|-|-|
| `local_path` | `Union[str, Path]` |
| `remote_path` | `Optional[str]` |

#### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `obj` | `Any` |

#### get_file()

```python
def get_file(
    file_name: str,
) -> Optional[File[T]]
```
Asynchronously get a specific file from the directory.



| Parameter | Type |
|-|-|
| `file_name` | `str` |

#### get_file_sync()

```python
def get_file_sync(
    file_name: str,
) -> Optional[File[T]]
```
Synchronously get a specific file from the directory.



| Parameter | Type |
|-|-|
| `file_name` | `str` |

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
| Parameter | Type |
|-|-|
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `encoder` | `Callable[[Any], Any] \| None` |
| `models_as_dict` | `bool` |
| `dumps_kwargs` | `Any` |

#### list_files()

```python
def list_files()
```
Asynchronously get a list of all files in the directory (non-recursive).

Returns:
    A list of File objects

Example:
    ```python
    files = await directory.list_files()
    for file in files:
        # Process the file
    ```


#### list_files_sync()

```python
def list_files_sync()
```
Synchronously get a list of all files in the directory (non-recursive).

Returns:
    A list of File objects

Example:
    ```python
    files = directory.list_files_sync()
    for file in files:
        # Process the file
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

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.



| Parameter | Type |
|-|-|
| `_fields_set` | `set[str] \| None` |
| `values` | `Any` |

#### model_copy()

```python
def model_copy(
    update: Mapping[str, Any] | None,
    deep: bool,
) -> Self
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#model_copy

Returns a copy of the model.



| Parameter | Type |
|-|-|
| `update` | `Mapping[str, Any] \| None` |
| `deep` | `bool` |

#### model_dump()

```python
def model_dump(
    mode: Literal['json', 'python'] | str,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    serialize_as_any: bool,
) -> dict[str, Any]
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type |
|-|-|
| `mode` | `Literal['json', 'python'] \| str` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `serialize_as_any` | `bool` |

#### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    serialize_as_any: bool,
) -> str
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type |
|-|-|
| `indent` | `int \| None` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `serialize_as_any` | `bool` |

#### model_json_schema()

```python
def model_json_schema(
    by_alias: bool,
    ref_template: str,
    schema_generator: type[GenerateJsonSchema],
    mode: JsonSchemaMode,
) -> dict[str, Any]
```
Generates a JSON schema for a model class.



| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |
| `schema_generator` | `type[GenerateJsonSchema]` |
| `mode` | `JsonSchemaMode` |

#### model_parametrized_name()

```python
def model_parametrized_name(
    params: tuple[type[Any], ...],
) -> str
```
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.



| Parameter | Type |
|-|-|
| `params` | `tuple[type[Any], ...]` |

#### model_post_init()

```python
def model_post_init(
    _BaseModel__context: Any,
)
```
Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.


| Parameter | Type |
|-|-|
| `_BaseModel__context` | `Any` |

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



| Parameter | Type |
|-|-|
| `force` | `bool` |
| `raise_errors` | `bool` |
| `_parent_namespace_depth` | `int` |
| `_types_namespace` | `MappingNamespace \| None` |

#### model_validate()

```python
def model_validate(
    obj: Any,
    strict: bool | None,
    from_attributes: bool | None,
    context: Any | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `from_attributes` | `bool \| None` |
| `context` | `Any \| None` |

#### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    context: Any | None,
) -> Self
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.



| Parameter | Type |
|-|-|
| `json_data` | `str \| bytes \| bytearray` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |

#### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    context: Any | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |

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
| Parameter | Type |
|-|-|
| `path` | `str \| Path` |
| `content_type` | `str \| None` |
| `encoding` | `str` |
| `proto` | `DeprecatedParseProtocol \| None` |
| `allow_pickle` | `bool` |

#### parse_obj()

```python
def parse_obj(
    obj: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `obj` | `Any` |

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
| Parameter | Type |
|-|-|
| `b` | `str \| bytes` |
| `content_type` | `str \| None` |
| `encoding` | `str` |
| `proto` | `DeprecatedParseProtocol \| None` |
| `allow_pickle` | `bool` |

#### schema()

```python
def schema(
    by_alias: bool,
    ref_template: str,
) -> Dict[str, Any]
```
| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |

#### schema_json()

```python
def schema_json(
    by_alias: bool,
    ref_template: str,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |
| `dumps_kwargs` | `Any` |

#### update_forward_refs()

```python
def update_forward_refs(
    localns: Any,
)
```
| Parameter | Type |
|-|-|
| `localns` | `Any` |

#### validate()

```python
def validate(
    value: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `value` | `Any` |

#### walk()

```python
def walk(
    recursive: bool,
    file_pattern: str,
    max_depth: Optional[int],
) -> AsyncIterator[File[T]]
```
Asynchronously walk through the directory and yield File objects.



| Parameter | Type |
|-|-|
| `recursive` | `bool` |
| `file_pattern` | `str` |
| `max_depth` | `Optional[int]` |

#### walk_sync()

```python
def walk_sync(
    recursive: bool,
    file_pattern: str,
    max_depth: Optional[int],
) -> Iterator[File[T]]
```
Synchronously walk through the directory and yield File objects.



| Parameter | Type |
|-|-|
| `recursive` | `bool` |
| `file_pattern` | `str` |
| `max_depth` | `Optional[int]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `model_extra` |  | {{< multiline >}}Get extra fields set during validation.

Returns:
    A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`.
{{< /multiline >}} |
| `model_fields_set` |  | {{< multiline >}}Returns the set of fields that have been explicitly set on this model instance.

Returns:
    A set of strings representing the fields that have been set,
        i.e. that were not filled from defaults.
{{< /multiline >}} |

## union.io.File

A generic file class representing a file with a specified format.
Provides both async and sync interfaces for file operations.

The generic type T represents the format of the file.

Example:
    ```python
    # Async usage
    from pandas import DataFrame
    csv_file = File[DataFrame](path="s3://my-bucket/data.csv")

    async with csv_file.open() as f:
        content = await f.read()

    # Sync alternative
    with csv_file.open_sync() as f:
        content = f.read()
    ```


```python
class File(
    path: str,
    name: Optional[str],
)
```
Create a new File reference.



| Parameter | Type |
|-|-|
| `path` | `str` |
| `name` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`construct()`](#construct) |  |
| [`copy()`](#copy) | Returns a copy of the model. |
| [`dict()`](#dict) |  |
| [`download()`](#download) | Asynchronously download the file to a local path. |
| [`download_sync()`](#download_sync) | Synchronously download the file to a local path. |
| [`from_local()`](#from_local) | Asynchronously create a new File by uploading a local file to the configured remote store. |
| [`from_local_sync()`](#from_local_sync) | Synchronously create a new File by uploading a local file to the configured remote store. |
| [`from_orm()`](#from_orm) |  |
| [`json()`](#json) |  |
| [`model_construct()`](#model_construct) | Creates a new instance of the `Model` class with validated data. |
| [`model_copy()`](#model_copy) | Usage docs: https://docs. |
| [`model_dump()`](#model_dump) | Usage docs: https://docs. |
| [`model_dump_json()`](#model_dump_json) | Usage docs: https://docs. |
| [`model_json_schema()`](#model_json_schema) | Generates a JSON schema for a model class. |
| [`model_parametrized_name()`](#model_parametrized_name) | Compute the class name for parametrizations of generic classes. |
| [`model_post_init()`](#model_post_init) | Override this method to perform additional initialization after `__init__` and `model_construct`. |
| [`model_rebuild()`](#model_rebuild) | Try to rebuild the pydantic-core schema for the model. |
| [`model_validate()`](#model_validate) | Validate a pydantic model instance. |
| [`model_validate_json()`](#model_validate_json) | Usage docs: https://docs. |
| [`model_validate_strings()`](#model_validate_strings) | Validate the given object with string data against the Pydantic model. |
| [`open()`](#open) | Asynchronously open the file and return a file-like object. |
| [`open_sync()`](#open_sync) | Synchronously open the file and return a file-like object. |
| [`parse_file()`](#parse_file) |  |
| [`parse_obj()`](#parse_obj) |  |
| [`parse_raw()`](#parse_raw) |  |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
| [`update_forward_refs()`](#update_forward_refs) |  |
| [`validate()`](#validate) |  |


#### construct()

```python
def construct(
    _fields_set: set[str] | None,
    values: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `_fields_set` | `set[str] \| None` |
| `values` | `Any` |

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

!!! warning "Deprecated"
    This method is now deprecated; use `model_copy` instead.

If you need `include` or `exclude`, use:

```python {test="skip" lint="skip"}
data = self.model_dump(include=include, exclude=exclude, round_trip=True)
data = {**data, **(update or {})}
copied = self.model_validate(data)
```



| Parameter | Type |
|-|-|
| `include` | `AbstractSetIntStr \| MappingIntStrAny \| None` |
| `exclude` | `AbstractSetIntStr \| MappingIntStrAny \| None` |
| `update` | `Dict[str, Any] \| None` |
| `deep` | `bool` |

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
| Parameter | Type |
|-|-|
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |

#### download()

```python
def download(
    local_path: Optional[Union[str, Path]],
) -> str
```
Asynchronously download the file to a local path.



| Parameter | Type |
|-|-|
| `local_path` | `Optional[Union[str, Path]]` |

#### download_sync()

```python
def download_sync(
    local_path: Optional[Union[str, Path]],
) -> str
```
Synchronously download the file to a local path.



| Parameter | Type |
|-|-|
| `local_path` | `Optional[Union[str, Path]]` |

#### from_local()

```python
def from_local(
    local_path: Union[str, Path],
    remote_path: Optional[str],
) -> File[T]
```
Asynchronously create a new File by uploading a local file to the configured remote store.



| Parameter | Type |
|-|-|
| `local_path` | `Union[str, Path]` |
| `remote_path` | `Optional[str]` |

#### from_local_sync()

```python
def from_local_sync(
    local_path: Union[str, Path],
    remote_path: Optional[str],
) -> File[T]
```
Synchronously create a new File by uploading a local file to the configured remote store.



| Parameter | Type |
|-|-|
| `local_path` | `Union[str, Path]` |
| `remote_path` | `Optional[str]` |

#### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `obj` | `Any` |

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
| Parameter | Type |
|-|-|
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `encoder` | `Callable[[Any], Any] \| None` |
| `models_as_dict` | `bool` |
| `dumps_kwargs` | `Any` |

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

!!! note
    `model_construct()` generally respects the `model_config.extra` setting on the provided model.
    That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
    and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
    Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
    an error if extra values are passed, but they will be ignored.



| Parameter | Type |
|-|-|
| `_fields_set` | `set[str] \| None` |
| `values` | `Any` |

#### model_copy()

```python
def model_copy(
    update: Mapping[str, Any] | None,
    deep: bool,
) -> Self
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#model_copy

Returns a copy of the model.



| Parameter | Type |
|-|-|
| `update` | `Mapping[str, Any] \| None` |
| `deep` | `bool` |

#### model_dump()

```python
def model_dump(
    mode: Literal['json', 'python'] | str,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    serialize_as_any: bool,
) -> dict[str, Any]
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type |
|-|-|
| `mode` | `Literal['json', 'python'] \| str` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `serialize_as_any` | `bool` |

#### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    serialize_as_any: bool,
) -> str
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/serialization/#modelmodel_dump_json

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type |
|-|-|
| `indent` | `int \| None` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `serialize_as_any` | `bool` |

#### model_json_schema()

```python
def model_json_schema(
    by_alias: bool,
    ref_template: str,
    schema_generator: type[GenerateJsonSchema],
    mode: JsonSchemaMode,
) -> dict[str, Any]
```
Generates a JSON schema for a model class.



| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |
| `schema_generator` | `type[GenerateJsonSchema]` |
| `mode` | `JsonSchemaMode` |

#### model_parametrized_name()

```python
def model_parametrized_name(
    params: tuple[type[Any], ...],
) -> str
```
Compute the class name for parametrizations of generic classes.

This method can be overridden to achieve a custom naming scheme for generic BaseModels.



| Parameter | Type |
|-|-|
| `params` | `tuple[type[Any], ...]` |

#### model_post_init()

```python
def model_post_init(
    _BaseModel__context: Any,
)
```
Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.


| Parameter | Type |
|-|-|
| `_BaseModel__context` | `Any` |

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



| Parameter | Type |
|-|-|
| `force` | `bool` |
| `raise_errors` | `bool` |
| `_parent_namespace_depth` | `int` |
| `_types_namespace` | `MappingNamespace \| None` |

#### model_validate()

```python
def model_validate(
    obj: Any,
    strict: bool | None,
    from_attributes: bool | None,
    context: Any | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `from_attributes` | `bool \| None` |
| `context` | `Any \| None` |

#### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    context: Any | None,
) -> Self
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/json/#json-parsing

Validate the given JSON data against the Pydantic model.



| Parameter | Type |
|-|-|
| `json_data` | `str \| bytes \| bytearray` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |

#### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    context: Any | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |

#### open()

```python
def open(
    mode: str,
    block_size: Optional[int],
    cache_type: str,
    cache_options: Optional[dict],
    compression: Optional[str],
    kwargs,
) -> AsyncContextManager[IO[Any]]
```
Asynchronously open the file and return a file-like object.



| Parameter | Type |
|-|-|
| `mode` | `str` |
| `block_size` | `Optional[int]` |
| `cache_type` | `str` |
| `cache_options` | `Optional[dict]` |
| `compression` | `Optional[str]` |
| `kwargs` | ``**kwargs`` |

#### open_sync()

```python
def open_sync(
    mode: str,
    block_size: Optional[int],
    cache_type: str,
    cache_options: Optional[dict],
    compression: Optional[str],
    kwargs,
) -> IO[Any]
```
Synchronously open the file and return a file-like object.



| Parameter | Type |
|-|-|
| `mode` | `str` |
| `block_size` | `Optional[int]` |
| `cache_type` | `str` |
| `cache_options` | `Optional[dict]` |
| `compression` | `Optional[str]` |
| `kwargs` | ``**kwargs`` |

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
| Parameter | Type |
|-|-|
| `path` | `str \| Path` |
| `content_type` | `str \| None` |
| `encoding` | `str` |
| `proto` | `DeprecatedParseProtocol \| None` |
| `allow_pickle` | `bool` |

#### parse_obj()

```python
def parse_obj(
    obj: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `obj` | `Any` |

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
| Parameter | Type |
|-|-|
| `b` | `str \| bytes` |
| `content_type` | `str \| None` |
| `encoding` | `str` |
| `proto` | `DeprecatedParseProtocol \| None` |
| `allow_pickle` | `bool` |

#### schema()

```python
def schema(
    by_alias: bool,
    ref_template: str,
) -> Dict[str, Any]
```
| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |

#### schema_json()

```python
def schema_json(
    by_alias: bool,
    ref_template: str,
    dumps_kwargs: Any,
) -> str
```
| Parameter | Type |
|-|-|
| `by_alias` | `bool` |
| `ref_template` | `str` |
| `dumps_kwargs` | `Any` |

#### update_forward_refs()

```python
def update_forward_refs(
    localns: Any,
)
```
| Parameter | Type |
|-|-|
| `localns` | `Any` |

#### validate()

```python
def validate(
    value: Any,
) -> Self
```
| Parameter | Type |
|-|-|
| `value` | `Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `model_extra` |  | {{< multiline >}}Get extra fields set during validation.

Returns:
    A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`.
{{< /multiline >}} |
| `model_fields_set` |  | {{< multiline >}}Returns the set of fields that have been explicitly set on this model instance.

Returns:
    A set of strings representing the fields that have been set,
        i.e. that were not filled from defaults.
{{< /multiline >}} |

