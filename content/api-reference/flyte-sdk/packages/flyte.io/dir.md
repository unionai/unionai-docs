---
title: Dir
version: 2.0.0b59
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Dir

**Package:** `flyte.io`

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
async def process_all_files(d: Dir) -> int:
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
def process_all_files_sync(d: Dir) -> int:
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
async def count_files(d: Dir) -> int:
    files = await d.list_files()
    return len(files)
```

Example: List files in directory (Sync).

```python
@env.task
def count_files_sync(d: Dir) -> int:
    files = d.list_files_sync()
    return len(files)
```

Example: Get a specific file from directory (Async).

```python
@env.task
async def read_config_file(d: Dir) -> str:
    config_file = await d.get_file("config.json")
    if config_file:
        async with config_file.open("rb") as f:
            return (await f.read()).decode("utf-8")
    return "Config not found"
```

Example: Get a specific file from directory (Sync).

```python
@env.task
def read_config_file_sync(d: Dir) -> str:
    config_file = d.get_file_sync("config.json")
    if config_file:
        with config_file.open_sync("rb") as f:
            return f.read().decode("utf-8")
    return "Config not found"
```

Example: Upload a local directory to remote storage (Async).

```python
@env.task
async def upload_directory() -> Dir:
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
def upload_directory_sync() -> Dir:
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
async def download_directory(d: Dir) -> str:
    local_path = await d.download()
    # Process files in local directory
    return local_path
```

Example: Download a directory to local storage (Sync).

```python
@env.task
def download_directory_sync(d: Dir) -> str:
    local_path = d.download_sync()
    # Process files in local directory
    return local_path
```

Example: Reference an existing remote directory.

```python
@env.task
async def process_existing_dir() -> int:
    d = Dir.from_existing_remote("s3://my-bucket/data/")
    files = await d.list_files()
    return len(files)
```

Example: Check if directory exists (Async).

```python
@env.task
async def check_directory(d: Dir) -> bool:
    return await d.exists()
```

Example: Check if directory exists (Sync).

```python
@env.task
def check_directory_sync(d: Dir) -> bool:
    return d.exists_sync()
```



```python
class Dir(
    data: Any,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `data` | `Any` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `lazy_uploader` | `None` |  |
| `model_extra` | `None` | Get extra fields set during validation.  Returns:     A dictionary of extra fields, or `None` if `config.extra` is not set to `"allow"`. |
| `model_fields_set` | `None` | Returns the set of fields that have been explicitly set on this model instance.  Returns:     A set of strings representing the fields that have been set,         i.e. that were not filled from defaults. |

## Methods

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
| [`model_copy()`](#model_copy) | Returns a copy of the model. |
| [`model_dump()`](#model_dump) | Generate a dictionary representation of the model, optionally specifying which fields to include or exclude. |
| [`model_dump_json()`](#model_dump_json) | Generates a JSON representation of the model using Pydantic's `to_json` method. |
| [`model_json_schema()`](#model_json_schema) | Generates a JSON schema for a model class. |
| [`model_parametrized_name()`](#model_parametrized_name) | Compute the class name for parametrizations of generic classes. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialise private attributes. |
| [`model_rebuild()`](#model_rebuild) | Try to rebuild the pydantic-core schema for the model. |
| [`model_validate()`](#model_validate) | Validate a pydantic model instance. |
| [`model_validate_json()`](#model_validate_json) | Validate the given JSON data against the Pydantic model. |
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

> [!WARNING] Deprecated
> This method is now deprecated; use `model_copy` instead.

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
Asynchronously download the entire directory to a local path.

Use this when you need to download all files in a directory to your local filesystem for processing.

Example (Async):

```python
@env.task
async def download_directory(d: Dir) -> str:
    local_dir = await d.download()
    # Process files in the local directory
    return local_dir
```

Example (Async - Download to specific path):

```python
@env.task
async def download_to_path(d: Dir) -> str:
    local_dir = await d.download("/tmp/my_data/")
    return local_dir
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Optional[Union[str, Path]]` | The local path to download the directory to. If None, a temporary directory will be used and a path will be generated. |

### download_sync()

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
def download_directory_sync(d: Dir) -> str:
    local_dir = d.download_sync()
    # Process files in the local directory
    return local_dir
```

Example (Sync - Download to specific path):

```python
@env.task
def download_to_path_sync(d: Dir) -> str:
    local_dir = d.download_sync("/tmp/my_data/")
    return local_dir
```


| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Optional[Union[str, Path]]` | The local path to download the directory to. If None, a temporary directory will be used and a path will be generated. |

### exists()

```python
def exists()
```
Asynchronously check if the directory exists.

Returns:
    True if the directory exists, False otherwise

Example (Async):

```python
@env.task
async def check_directory(d: Dir) -> bool:
    if await d.exists():
        print("Directory exists!")
        return True
    return False
```


### exists_sync()

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
def check_directory_sync(d: Dir) -> bool:
    if d.exists_sync():
        print("Directory exists!")
        return True
    return False
```


### from_existing_remote()

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
async def process_existing_directory() -> int:
    d = Dir.from_existing_remote("s3://my-bucket/data/")
    files = await d.list_files()
    return len(files)
```

Example (With cache key):

```python
@env.task
async def process_with_cache_key() -> int:
    d = Dir.from_existing_remote("s3://my-bucket/data/", dir_cache_key="abc123")
    files = await d.list_files()
    return len(files)
```



| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | The remote path to the existing directory |
| `dir_cache_key` | `Optional[str]` | Optional hash value to use for cache key computation. If not specified, the cache key will be computed based on the directory's attributes. |

### from_local()

```python
def from_local(
    local_path: Union[str, Path],
    remote_destination: Optional[str],
    dir_cache_key: Optional[str],
    batch_size: Optional[int],
) -> Dir[T]
```
Asynchronously create a new Dir by uploading a local directory to remote storage.

Use this in async tasks when you have a local directory that needs to be uploaded to remote storage.

Example (Async):

```python
@env.task
async def upload_local_directory() -> Dir:
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
async def upload_to_specific_path() -> Dir:
    remote_dir = await Dir.from_local("/tmp/data_dir/", "s3://my-bucket/data/")
    return remote_dir
```

Example (Async - With cache key):

```python
@env.task
async def upload_with_cache_key() -> Dir:
    remote_dir = await Dir.from_local("/tmp/data_dir/", dir_cache_key="my_cache_key_123")
    return remote_dir
```


| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Union[str, Path]` | Path to the local directory |
| `remote_destination` | `Optional[str]` | Optional remote path to store the directory. If None, a path will be automatically generated. |
| `dir_cache_key` | `Optional[str]` | Optional precomputed hash value to use for cache key computation when this Dir is used as an input to discoverable tasks. If not specified, the cache key will be based on directory attributes. |
| `batch_size` | `Optional[int]` | Optional concurrency limit for uploading files. If not specified, the default value is determined by the FLYTE_IO_BATCH_SIZE environment variable (default: 32). |

### from_local_sync()

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
def upload_local_directory_sync() -> Dir:
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
def upload_to_specific_path_sync() -> Dir:
    remote_dir = Dir.from_local_sync("/tmp/data_dir/", "s3://my-bucket/data/")
    return remote_dir
```

Example (Sync - With cache key):

```python
@env.task
def upload_with_cache_key_sync() -> Dir:
    remote_dir = Dir.from_local_sync("/tmp/data_dir/", dir_cache_key="my_cache_key_123")
    return remote_dir
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Union[str, Path]` | Path to the local directory |
| `remote_destination` | `Optional[str]` | Optional remote path to store the directory. If None, a path will be automatically generated. |
| `dir_cache_key` | `Optional[str]` | Optional precomputed hash value to use for cache key computation when this Dir is used as an input to discoverable tasks. If not specified, the cache key will be based on directory attributes. |

### from_orm()

```python
def from_orm(
    obj: Any,
) -> Self
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `Any` | |

### get_file()

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
async def read_specific_file(d: Dir) -> str:
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

### get_file_sync()

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
def read_specific_file_sync(d: Dir) -> str:
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

### list_files()

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
async def count_files(d: Dir) -> int:
    files = await d.list_files()
    return len(files)
```

Example (Async - Process files):

```python
@env.task
async def process_all_files(d: Dir) -> list[str]:
    files = await d.list_files()
    contents = []
    for file in files:
        async with file.open("rb") as f:
            content = await f.read()
            contents.append(content.decode("utf-8"))
    return contents
```


### list_files_sync()

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
def count_files_sync(d: Dir) -> int:
    files = d.list_files_sync()
    return len(files)
```

Example (Sync - Process files):

```python
@env.task
def process_all_files_sync(d: Dir) -> list[str]:
    files = d.list_files_sync()
    contents = []
    for file in files:
        with file.open_sync("rb") as f:
            content = f.read()
            contents.append(content.decode("utf-8"))
    return contents
```


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

> [!NOTE]
> `model_construct()` generally respects the `model_config.extra` setting on the provided model.
> That is, if `model_config.extra == 'allow'`, then all extra passed values are added to the model instance's `__dict__`
> and `__pydantic_extra__` fields. If `model_config.extra == 'ignore'` (the default), then all extra passed values are ignored.
> Because no validation is performed with a call to `model_construct()`, having `model_config.extra == 'forbid'` does not result in
> an error if extra values are passed, but they will be ignored.



| Parameter | Type | Description |
|-|-|-|
| `_fields_set` | `set[str] \| None` | A set of field names that were originally explicitly set during instantiation. If provided, this is directly used for the [`model_fields_set`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_fields_set) attribute. Otherwise, the field names from the `values` argument will be used. |
| `values` | `Any` | Trusted or pre-validated data dictionary. |

### model_copy()

```python
def model_copy(
    update: Mapping[str, Any] | None,
    deep: bool,
) -> Self
```
> [!TIP] Usage Documentation (external docs for inherited method)
> [`model_copy`](https://docs.pydantic.dev/latest/concepts/models/#model-copy)

Returns a copy of the model.

> [!NOTE]
> The underlying instance's [`__dict__`](https://docs.python.org/3/library/stdtypes.html#object.__dict__) attribute is copied. This
> might have unexpected side effects if you store anything in it, on top of the model
> fields (e.g. the value of [cached properties](https://docs.python.org/3/library/functools.html#functools.cached_property)).



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
> [!TIP] Usage Documentation (external docs for inherited method)
> [`model_dump`](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode)

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
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |
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
> [!TIP] Usage Documentation (external docs for inherited method)
> [`model_dump_json`](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode)

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
| `warnings` | `bool \| Literal['none', 'warn', 'error']` | How to handle serialization errors. False/"none" ignores them, True/"warn" logs errors, "error" raises a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError). |
| `fallback` | `Callable[[Any], Any] \| None` | A function to call when an unknown value is encountered. If not provided, a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) error is raised. |
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
This function is meant to behave like a BaseModel method to initialise private attributes.

It takes context as an argument since that's what pydantic-core passes when calling it.



| Parameter | Type | Description |
|-|-|-|
| `context` | `Any` | The context. |

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
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.ConfigDict.extra) for details. |
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
> [!TIP] Usage Documentation (external docs for inherited method)
> [JSON Parsing](https://docs.pydantic.dev/latest/concepts/json/#json-parsing)

Validate the given JSON data against the Pydantic model.



| Parameter | Type | Description |
|-|-|-|
| `json_data` | `str \| bytes \| bytearray` | The JSON data to validate. |
| `strict` | `bool \| None` | Whether to enforce types strictly. |
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.ConfigDict.extra) for details. |
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
| `extra` | `ExtraValues \| None` | Whether to ignore, allow, or forbid extra data during model validation. See the [`extra` configuration value](https://docs.pydantic.dev/latest/api/config/#pydantic.ConfigDict.extra) for details. |
| `context` | `Any \| None` | Extra variables to pass to the validator. |
| `by_alias` | `bool \| None` | Whether to use the field's alias when validating against the provided input data. |
| `by_name` | `bool \| None` | Whether to use the field's name when validating against the provided input data. |

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
Internal: Check if incoming schema matches Dir schema. Not intended for direct use.


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

### walk()

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
async def list_all_files(d: Dir) -> list[str]:
    file_names = []
    async for file in d.walk(recursive=True):
        file_names.append(file.name)
    return file_names
```

Example (Async - Non-recursive):

```python
@env.task
async def list_top_level_files(d: Dir) -> list[str]:
    file_names = []
    async for file in d.walk(recursive=False):
        file_names.append(file.name)
    return file_names
```

Example (Async - With max depth):

```python
@env.task
async def list_files_max_depth(d: Dir) -> list[str]:
    file_names = []
    async for file in d.walk(recursive=True, max_depth=2):
        file_names.append(file.name)
    return file_names
```



| Parameter | Type | Description |
|-|-|-|
| `recursive` | `bool` | If True, recursively walk subdirectories. If False, only list files in the top-level directory. |
| `max_depth` | `Optional[int]` | Maximum depth for recursive walking. If None, walk through all subdirectories. |

### walk_sync()

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
def list_all_files_sync(d: Dir) -> list[str]:
    file_names = []
    for file in d.walk_sync(recursive=True):
        file_names.append(file.name)
    return file_names
```

Example (Sync - With file pattern):

```python
@env.task
def list_text_files(d: Dir) -> list[str]:
    file_names = []
    for file in d.walk_sync(recursive=True, file_pattern="*.txt"):
        file_names.append(file.name)
    return file_names
```

Example (Sync - Non-recursive with max depth):

```python
@env.task
def list_files_limited(d: Dir) -> list[str]:
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

