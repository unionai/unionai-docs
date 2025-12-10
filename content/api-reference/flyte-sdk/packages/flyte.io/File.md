---
title: File
version: 2.0.0b35
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# File

**Package:** `flyte.io`

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

## Methods

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


### construct()

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

### copy()

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

### dict()

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

### download()

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

### download_sync()

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

### exists()

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


### exists_sync()

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


### from_existing_remote()

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

### from_local()

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

### from_local_sync()

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

### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

### json()

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

### model_construct()

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

### model_copy()

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

### model_dump()

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

### model_dump_json()

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

### model_json_schema()

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

### model_parametrized_name()

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

### model_post_init()

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

### model_rebuild()

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

### model_validate()

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

### model_validate_json()

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

### model_validate_strings()

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

### new_remote()

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

### open()

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

### open_sync()

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

### parse_file()

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

### parse_obj()

```python
def parse_obj(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

### parse_raw()

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

### pre_init()

```python
def pre_init(
    data,
)
```
Internal: Pydantic validator to set default name from path. Not intended for direct use.


| Parameter | Type | Description |
|-|-|-|
| `data` |  | |

### schema()

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

### schema_json()

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

### schema_match()

```python
def schema_match(
    incoming: dict,
)
```
Internal: Check if incoming schema matches File schema. Not intended for direct use.


| Parameter | Type | Description |
|-|-|-|
| `incoming` | `dict` | |

### update_forward_refs()

```python
def update_forward_refs(
    localns: Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `localns` | `Any` | |

### validate()

```python
def validate(
    value: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `value` | `Any` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `model_extra` | `None` | Get extra fields set during validation.  Returns:     A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. |
| `model_fields_set` | `None` | Returns the set of fields that have been explicitly set on this model instance.  Returns:     A set of strings representing the fields that have been set,         i.e. that were not filled from defaults. |

