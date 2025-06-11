---
title: flyte.io
version: 0.2.0b10.dev2+g9bf3bb9
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
| [`Dir`](.././flyte.io#flyteiodir) | A generic directory class representing a directory with files of a specified format. |
| [`File`](.././flyte.io#flyteiofile) | A generic file class representing a file with a specified format. |
| [`StructuredDataset`](.././flyte.io#flyteiostructureddataset) | This is the user facing StructuredDataset class. |
| [`StructuredDatasetDecoder`](.././flyte.io#flyteiostructureddatasetdecoder) | Helper class that provides a standard way to create an ABC using. |
| [`StructuredDatasetEncoder`](.././flyte.io#flyteiostructureddatasetencoder) | Helper class that provides a standard way to create an ABC using. |
| [`StructuredDatasetTransformerEngine`](.././flyte.io#flyteiostructureddatasettransformerengine) | Think of this transformer as a higher-level meta transformer that is used for all the dataframe types. |

### Methods

| Method | Description |
|-|-|
| [`lazy_import_structured_dataset_handler()`](#lazy_import_structured_dataset_handler) |  |


## Methods

#### lazy_import_structured_dataset_handler()

```python
def lazy_import_structured_dataset_handler()
```
## flyte.io.Dir

A generic directory class representing a directory with files of a specified format.
Provides both async and sync interfaces for directory operations.
Users are responsible for handling all I/O - the type transformer for Dir does not do any automatic uploading
or downloading of files.

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
    data: Any,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type |
|-|-|
| `data` | `Any` |

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
| [`pre_init()`](#pre_init) |  |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
| [`schema_match()`](#schema_match) |  |
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

> [!WARNING] Deprecated
> This method is now deprecated; use `model_copy` instead.

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

> [!NOTE]
> `model_construct()` generally respects the `model_config.extra` setting on the provided model.
> That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
> and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
> Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
> an error if extra values are passed, but they will be ignored.



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
!!! abstract "Usage Documentation"
    [`model_copy`](../concepts/serialization.md#model_copy)

Returns a copy of the model.

> [!NOTE]
> The underlying instance's [`__dict__`][object.__dict__] attribute is copied. This
> might have unexpected side effects if you store anything in it, on top of the model
> fields (e.g. the value of [cached properties][functools.cached_property]).



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
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> dict[str, Any]
```
!!! abstract "Usage Documentation"
    [`model_dump`](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type |
|-|-|
| `mode` | `Literal['json', 'python'] \| str` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `fallback` | `Callable[[Any], Any] \| None` |
| `serialize_as_any` | `bool` |

#### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> str
```
!!! abstract "Usage Documentation"
    [`model_dump_json`](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type |
|-|-|
| `indent` | `int \| None` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `fallback` | `Callable[[Any], Any] \| None` |
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
    context: Any,
)
```
Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.


| Parameter | Type |
|-|-|
| `context` | `Any` |

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
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `from_attributes` | `bool \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `by_name` | `bool \| None` |

#### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
!!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.



| Parameter | Type |
|-|-|
| `json_data` | `str \| bytes \| bytearray` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `by_name` | `bool \| None` |

#### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `by_name` | `bool \| None` |

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

#### pre_init()

```python
def pre_init(
    data,
)
```
| Parameter | Type |
|-|-|
| `data` |  |

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

#### schema_match()

```python
def schema_match(
    incoming: dict,
)
```
| Parameter | Type |
|-|-|
| `incoming` | `dict` |

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
    max_depth: Optional[int],
) -> AsyncIterator[File[T]]
```
Asynchronously walk through the directory and yield File objects.



| Parameter | Type |
|-|-|
| `recursive` | `bool` |
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
| `model_extra` | `None` | {{< multiline >}}Get extra fields set during validation.

Returns:
    A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`.
{{< /multiline >}} |
| `model_fields_set` | `None` | {{< multiline >}}Returns the set of fields that have been explicitly set on this model instance.

Returns:
    A set of strings representing the fields that have been set,
        i.e. that were not filled from defaults.
{{< /multiline >}} |

## flyte.io.File

A generic file class representing a file with a specified format.
Provides both async and sync interfaces for file operations.
Users must handle all I/O operations themselves by instantiating this class with the appropriate class methods.

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

Example: Read a file input in a Task.
```
@env.task
async def my_task(file: File[DataFrame]):
    async with file.open() as f:
        df = pd.read_csv(f)
```

Example: Write a file by streaming it directly to blob storage
```
@env.task
async def my_task() -> File[DataFrame]:
    df = pd.DataFrame(...)
    file = File.new_remote()
    async with file.open("wb") as f:
        df.to_csv(f)
    # No additional uploading will be done here.
    return file
```
Example: Write a file by writing it locally first, and then uploading it.
```
@env.task
async def my_task() -> File[DataFrame]:
    # write to /tmp/data.csv
    return File.from_local("/tmp/data.csv", optional="s3://my-bucket/data.csv")
```

Example: From an existing remote file
```
@env.task
async def my_task() -> File[DataFrame]:
    return File.from_existing_remote("s3://my-bucket/data.csv")
```

Example: Take a remote file as input and return the same one, should not do any copy
```
@env.task
async def my_task(file: File[DataFrame]) -> File[DataFrame]:
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


| Parameter | Type |
|-|-|
| `data` | `Any` |

### Methods

| Method | Description |
|-|-|
| [`construct()`](#construct) |  |
| [`copy()`](#copy) | Returns a copy of the model. |
| [`dict()`](#dict) |  |
| [`download()`](#download) | Asynchronously download the file to a local path. |
| [`exists_sync()`](#exists_sync) | Synchronously check if the file exists. |
| [`from_existing_remote()`](#from_existing_remote) | Create a File reference from an existing remote file. |
| [`from_local()`](#from_local) | Create a new File object from a local file that will be uploaded to the configured remote store. |
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
| [`pre_init()`](#pre_init) |  |
| [`schema()`](#schema) |  |
| [`schema_json()`](#schema_json) |  |
| [`schema_match()`](#schema_match) |  |
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

> [!WARNING] Deprecated
> This method is now deprecated; use `model_copy` instead.

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

#### exists_sync()

```python
def exists_sync()
```
Synchronously check if the file exists.

Returns:
    True if the file exists, False otherwise

Example:
    ```python
    if file.exists_sync():
        # Process the file
    ```


#### from_existing_remote()

```python
def from_existing_remote(
    remote_path: str,
) -> File[T]
```
Create a File reference from an existing remote file.

Example:
```python
@env.task
async def my_task() -> File[DataFrame]:
    return File.from_existing_remote("s3://my-bucket/data.csv")
```



| Parameter | Type |
|-|-|
| `remote_path` | `str` |

#### from_local()

```python
def from_local(
    local_path: Union[str, Path],
    remote_destination: Optional[str],
) -> File[T]
```
Create a new File object from a local file that will be uploaded to the configured remote store.



| Parameter | Type |
|-|-|
| `local_path` | `Union[str, Path]` |
| `remote_destination` | `Optional[str]` |

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

> [!NOTE]
> `model_construct()` generally respects the `model_config.extra` setting on the provided model.
> That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
> and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
> Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
> an error if extra values are passed, but they will be ignored.



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
!!! abstract "Usage Documentation"
    [`model_copy`](../concepts/serialization.md#model_copy)

Returns a copy of the model.

> [!NOTE]
> The underlying instance's [`__dict__`][object.__dict__] attribute is copied. This
> might have unexpected side effects if you store anything in it, on top of the model
> fields (e.g. the value of [cached properties][functools.cached_property]).



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
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> dict[str, Any]
```
!!! abstract "Usage Documentation"
    [`model_dump`](../concepts/serialization.md#modelmodel_dump)

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.



| Parameter | Type |
|-|-|
| `mode` | `Literal['json', 'python'] \| str` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `fallback` | `Callable[[Any], Any] \| None` |
| `serialize_as_any` | `bool` |

#### model_dump_json()

```python
def model_dump_json(
    indent: int | None,
    include: IncEx | None,
    exclude: IncEx | None,
    context: Any | None,
    by_alias: bool | None,
    exclude_unset: bool,
    exclude_defaults: bool,
    exclude_none: bool,
    round_trip: bool,
    warnings: bool | Literal['none', 'warn', 'error'],
    fallback: Callable[[Any], Any] | None,
    serialize_as_any: bool,
) -> str
```
!!! abstract "Usage Documentation"
    [`model_dump_json`](../concepts/serialization.md#modelmodel_dump_json)

Generates a JSON representation of the model using Pydantic's `to_json` method.



| Parameter | Type |
|-|-|
| `indent` | `int \| None` |
| `include` | `IncEx \| None` |
| `exclude` | `IncEx \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `exclude_unset` | `bool` |
| `exclude_defaults` | `bool` |
| `exclude_none` | `bool` |
| `round_trip` | `bool` |
| `warnings` | `bool \| Literal['none', 'warn', 'error']` |
| `fallback` | `Callable[[Any], Any] \| None` |
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
    context: Any,
)
```
Override this method to perform additional initialization after `__init__` and `model_construct`.
This is useful if you want to do some validation that requires the entire model to be initialized.


| Parameter | Type |
|-|-|
| `context` | `Any` |

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
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate a pydantic model instance.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `from_attributes` | `bool \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `by_name` | `bool \| None` |

#### model_validate_json()

```python
def model_validate_json(
    json_data: str | bytes | bytearray,
    strict: bool | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
!!! abstract "Usage Documentation"
    [JSON Parsing](../concepts/json.md#json-parsing)

Validate the given JSON data against the Pydantic model.



| Parameter | Type |
|-|-|
| `json_data` | `str \| bytes \| bytearray` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `by_name` | `bool \| None` |

#### model_validate_strings()

```python
def model_validate_strings(
    obj: Any,
    strict: bool | None,
    context: Any | None,
    by_alias: bool | None,
    by_name: bool | None,
) -> Self
```
Validate the given object with string data against the Pydantic model.



| Parameter | Type |
|-|-|
| `obj` | `Any` |
| `strict` | `bool \| None` |
| `context` | `Any \| None` |
| `by_alias` | `bool \| None` |
| `by_name` | `bool \| None` |

#### new_remote()

```python
def new_remote()
```
Create a new File reference for a remote file that will be written to.

Example:
```
@env.task
async def my_task() -> File[DataFrame]:
    df = pd.DataFrame(...)
    file = File.new_remote()
    async with file.open("wb") as f:
        df.to_csv(f)
    return file
```


#### open()

```python
def open(
    mode: str,
    block_size: Optional[int],
    cache_type: str,
    cache_options: Optional[dict],
    compression: Optional[str],
    kwargs,
) -> AsyncGenerator[IO[Any]]
```
Asynchronously open the file and return a file-like object.



| Parameter | Type |
|-|-|
| `mode` | `str` |
| `block_size` | `Optional[int]` |
| `cache_type` | `str` |
| `cache_options` | `Optional[dict]` |
| `compression` | `Optional[str]` |
| `kwargs` | `**kwargs` |

#### open_sync()

```python
def open_sync(
    mode: str,
    block_size: Optional[int],
    cache_type: str,
    cache_options: Optional[dict],
    compression: Optional[str],
    kwargs,
) -> Generator[IO[Any]]
```
Synchronously open the file and return a file-like object.



| Parameter | Type |
|-|-|
| `mode` | `str` |
| `block_size` | `Optional[int]` |
| `cache_type` | `str` |
| `cache_options` | `Optional[dict]` |
| `compression` | `Optional[str]` |
| `kwargs` | `**kwargs` |

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

#### pre_init()

```python
def pre_init(
    data,
)
```
| Parameter | Type |
|-|-|
| `data` |  |

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

#### schema_match()

```python
def schema_match(
    incoming: dict,
)
```
| Parameter | Type |
|-|-|
| `incoming` | `dict` |

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
| `model_extra` | `None` | {{< multiline >}}Get extra fields set during validation.

Returns:
    A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`.
{{< /multiline >}} |
| `model_fields_set` | `None` | {{< multiline >}}Returns the set of fields that have been explicitly set on this model instance.

Returns:
    A set of strings representing the fields that have been set,
        i.e. that were not filled from defaults.
{{< /multiline >}} |

## flyte.io.StructuredDataset

This is the user facing StructuredDataset class. Please don't confuse it with the literals.StructuredDataset
class (that is just a model, a Python class representation of the protobuf).


```python
class StructuredDataset(
    dataframe: typing.Optional[typing.Any],
    uri: typing.Optional[str],
    metadata: typing.Optional[literals_pb2.StructuredDatasetMetadata],
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `dataframe` | `typing.Optional[typing.Any]` |
| `uri` | `typing.Optional[str]` |
| `metadata` | `typing.Optional[literals_pb2.StructuredDatasetMetadata]` |
| `kwargs` | `**kwargs` |

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
| Parameter | Type |
|-|-|
| `info` |  |

#### from_dict()

```python
def from_dict(
    d,
    dialect,
)
```
| Parameter | Type |
|-|-|
| `d` |  |
| `dialect` |  |

#### from_json()

```python
def from_json(
    data: typing.Union[str, bytes, bytearray],
    decoder: collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]],
    from_dict_kwargs: typing.Any,
) -> ~T
```
| Parameter | Type |
|-|-|
| `data` | `typing.Union[str, bytes, bytearray]` |
| `decoder` | `collections.abc.Callable[[typing.Union[str, bytes, bytearray]], dict[typing.Any, typing.Any]]` |
| `from_dict_kwargs` | `typing.Any` |

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
| Parameter | Type |
|-|-|
| `dataframe_type` | `Type[DF]` |

#### serialize_structured_dataset()

```python
def serialize_structured_dataset()
```
#### set_literal()

```python
def set_literal(
    expected: types_pb2.LiteralType,
)
```
A public wrapper method to set the StructuredDataset Literal.

This method provides external access to the internal _set_literal method.


| Parameter | Type |
|-|-|
| `expected` | `types_pb2.LiteralType` |

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
| Parameter | Type |
|-|-|
| `encoder` | `collections.abc.Callable[[typing.Any], typing.Union[str, bytes, bytearray]]` |
| `to_dict_kwargs` | `typing.Any` |

### Properties

| Property | Type | Description |
|-|-|-|
| `dataframe` | `None` |  |
| `literal` | `None` |  |
| `metadata` | `None` |  |

## flyte.io.StructuredDatasetDecoder

Helper class that provides a standard way to create an ABC using
inheritance.


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



| Parameter | Type |
|-|-|
| `python_type` | `Type[DF]` |
| `protocol` | `Optional[str]` |
| `supported_format` | `Optional[str]` |
| `additional_protocols` | `Optional[List[str]]` |

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



| Parameter | Type |
|-|-|
| `flyte_value` | `literals_pb2.StructuredDataset` |
| `current_task_metadata` | `literals_pb2.StructuredDatasetMetadata` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

## flyte.io.StructuredDatasetEncoder

Helper class that provides a standard way to create an ABC using
inheritance.


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



| Parameter | Type |
|-|-|
| `python_type` | `Type[T]` |
| `protocol` | `Optional[str]` |
| `supported_format` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`encode()`](#encode) | Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the. |


#### encode()

```python
def encode(
    structured_dataset: StructuredDataset,
    structured_dataset_type: types_pb2.StructuredDatasetType,
) -> literals_pb2.StructuredDataset
```
Even if the user code returns a plain dataframe instance, the dataset transformer engine will wrap the
incoming dataframe with defaults set for that dataframe
type. This simplifies this function's interface as a lot of data that could be specified by the user using
the
# TODO: Do we need to add a flag to indicate if it was wrapped by the transformer or by the user?



| Parameter | Type |
|-|-|
| `structured_dataset` | `StructuredDataset` |
| `structured_dataset_type` | `types_pb2.StructuredDatasetType` |

### Properties

| Property | Type | Description |
|-|-|-|
| `protocol` | `None` |  |
| `python_type` | `None` |  |
| `supported_format` | `None` |  |

## flyte.io.StructuredDatasetTransformerEngine

Think of this transformer as a higher-level meta transformer that is used for all the dataframe types.
If you are bringing a custom data frame type, or any data frame type, to flytekit, instead of
registering with the main type engine, you should register with this transformer instead.


```python
def StructuredDatasetTransformerEngine()
```
### Methods

| Method | Description |
|-|-|
| [`assert_type()`](#assert_type) |  |
| [`dict_to_structured_dataset()`](#dict_to_structured_dataset) |  |
| [`encode()`](#encode) |  |
| [`from_binary_idl()`](#from_binary_idl) | If the input is from flytekit, the Life Cycle will be as follows:. |
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
    t: Type[StructuredDataset],
    v: typing.Any,
)
```
| Parameter | Type |
|-|-|
| `t` | `Type[StructuredDataset]` |
| `v` | `typing.Any` |

#### dict_to_structured_dataset()

```python
def dict_to_structured_dataset(
    dict_obj: typing.Dict[str, str],
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
| Parameter | Type |
|-|-|
| `dict_obj` | `typing.Dict[str, str]` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### encode()

```python
def encode(
    sd: StructuredDataset,
    df_type: Type,
    protocol: str,
    format: str,
    structured_literal_type: types_pb2.StructuredDatasetType,
) -> literals_pb2.Literal
```
| Parameter | Type |
|-|-|
| `sd` | `StructuredDataset` |
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |
| `structured_literal_type` | `types_pb2.StructuredDatasetType` |

#### from_binary_idl()

```python
def from_binary_idl(
    binary_idl_object: literals_pb2.Binary,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
If the input is from flytekit, the Life Cycle will be as follows:

Life Cycle:
binary IDL                 -> resolved binary         -> bytes                   -> expected Python object
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
- The deserialization is the same as put a structured dataset in a dataclass,
  which will deserialize by the mashumaro's API.

Related PR:
- Title: Override Dataclass Serialization/Deserialization Behavior for FlyteTypes via Mashumaro
- Link: https://github.com/flyteorg/flytekit/pull/2554


| Parameter | Type |
|-|-|
| `binary_idl_object` | `literals_pb2.Binary` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

#### get_decoder()

```python
def get_decoder(
    df_type: Type,
    protocol: str,
    format: str,
) -> StructuredDatasetDecoder
```
| Parameter | Type |
|-|-|
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |

#### get_encoder()

```python
def get_encoder(
    df_type: Type,
    protocol: str,
    format: str,
)
```
| Parameter | Type |
|-|-|
| `df_type` | `Type` |
| `protocol` | `str` |
| `format` | `str` |

#### get_literal_type()

```python
def get_literal_type(
    t: typing.Union[Type[StructuredDataset], typing.Any],
) -> types_pb2.LiteralType
```
Provide a concrete implementation so that writers of custom dataframe handlers since there's nothing that
special about the literal type. Any dataframe type will always be associated with the structured dataset type.
The other aspects of it - columns, external schema type, etc. can be read from associated metadata.



| Parameter | Type |
|-|-|
| `t` | `typing.Union[Type[StructuredDataset], typing.Any]` |

#### guess_python_type()

```python
def guess_python_type(
    literal_type: types_pb2.LiteralType,
) -> Type[StructuredDataset]
```
Converts the Flyte LiteralType to a python object type.


| Parameter | Type |
|-|-|
| `literal_type` | `types_pb2.LiteralType` |

#### isinstance_generic()

```python
def isinstance_generic(
    obj,
    generic_alias,
)
```
| Parameter | Type |
|-|-|
| `obj` |  |
| `generic_alias` |  |

#### iter_as()

```python
def iter_as(
    sd: literals_pb2.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: literals_pb2.StructuredDatasetMetadata,
) -> typing.AsyncIterator[DF]
```
| Parameter | Type |
|-|-|
| `sd` | `literals_pb2.StructuredDataset` |
| `df_type` | `Type[DF]` |
| `updated_metadata` | `literals_pb2.StructuredDatasetMetadata` |

#### open_as()

```python
def open_as(
    sd: literals_pb2.StructuredDataset,
    df_type: Type[DF],
    updated_metadata: literals_pb2.StructuredDatasetMetadata,
) -> DF
```
| Parameter | Type |
|-|-|
| `sd` | `literals_pb2.StructuredDataset` |
| `df_type` | `Type[DF]` |
| `updated_metadata` | `literals_pb2.StructuredDatasetMetadata` |

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



| Parameter | Type |
|-|-|
| `h` | `Handlers` |
| `default_for_type` | `bool` |
| `override` | `bool` |
| `default_format_for_type` | `bool` |
| `default_storage_for_type` | `bool` |

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


| Parameter | Type |
|-|-|
| `h` | `Handlers` |
| `protocol` | `str` |
| `default_for_type` | `bool` |
| `override` | `bool` |
| `default_format_for_type` | `bool` |
| `default_storage_for_type` | `bool` |

#### register_renderer()

```python
def register_renderer(
    python_type: Type,
    renderer: Renderable,
)
```
| Parameter | Type |
|-|-|
| `python_type` | `Type` |
| `renderer` | `Renderable` |

#### to_html()

```python
def to_html(
    python_val: typing.Any,
    expected_python_type: Type[T],
) -> str
```
Converts any python val (dataframe, int, float) to a html string, and it will be wrapped in the HTML div


| Parameter | Type |
|-|-|
| `python_val` | `typing.Any` |
| `expected_python_type` | `Type[T]` |

#### to_literal()

```python
def to_literal(
    python_val: Union[StructuredDataset, typing.Any],
    python_type: Union[Type[StructuredDataset], Type],
    expected: types_pb2.LiteralType,
) -> literals_pb2.Literal
```
Converts a given python_val to a Flyte Literal, assuming the given python_val matches the declared python_type.
Implementers should refrain from using type(python_val) instead rely on the passed in python_type. If these
do not match (or are not allowed) the Transformer implementer should raise an AssertionError, clearly stating
what was the mismatch


| Parameter | Type |
|-|-|
| `python_val` | `Union[StructuredDataset, typing.Any]` |
| `python_type` | `Union[Type[StructuredDataset], Type]` |
| `expected` | `types_pb2.LiteralType` |

#### to_python_value()

```python
def to_python_value(
    lv: literals_pb2.Literal,
    expected_python_type: Type[T] | StructuredDataset,
) -> T | StructuredDataset
```
The only tricky thing with converting a Literal (say the output of an earlier task), to a Python value at
the start of a task execution, is the column subsetting behavior. For example, if you have,

def t1() -> Annotated[StructuredDataset, kwtypes(col_a=int, col_b=float)]: ...
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


| Parameter | Type |
|-|-|
| `lv` | `literals_pb2.Literal` |
| `expected_python_type` | `Type[T] \| StructuredDataset` |

### Properties

| Property | Type | Description |
|-|-|-|
| `name` | `None` |  |
| `python_type` | `None` | {{< multiline >}}This returns the python type
{{< /multiline >}} |
| `type_assertions_enabled` | `None` | {{< multiline >}}Indicates if the transformer wants type assertions to be enabled at the core type engine layer
{{< /multiline >}} |

