---
title: Dir
version: 2.1.2
variants: +flyte +byoc +selfmanaged
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



## Parameters

```python
class Dir(
    path: str,
    name: typing.Optional[str],
    format: str,
    hash: typing.Optional[str],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | The path to the directory (can be local or remote) |
| `name` | `typing.Optional[str]` | Optional name for the directory (defaults to basename of path) |
| `format` | `str` | |
| `hash` | `typing.Optional[str]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `lazy_uploader` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`download()`](#download) | Asynchronously download the entire directory to a local path. |
| [`download_sync()`](#download_sync) | Synchronously download the entire directory to a local path. |
| [`exists()`](#exists) | Asynchronously check if the directory exists. |
| [`exists_sync()`](#exists_sync) | Synchronously check if the directory exists. |
| [`from_existing_remote()`](#from_existing_remote) | Create a Dir reference from an existing remote directory. |
| [`from_local()`](#from_local) | Asynchronously create a new Dir by uploading a local directory to remote storage. |
| [`from_local_sync()`](#from_local_sync) | Synchronously create a new Dir by uploading a local directory to remote storage. |
| [`get_file()`](#get_file) | Asynchronously get a specific file from the directory by name. |
| [`get_file_sync()`](#get_file_sync) | Synchronously get a specific file from the directory by name. |
| [`list_files()`](#list_files) | Asynchronously get a list of all files in the directory (non-recursive). |
| [`list_files_sync()`](#list_files_sync) | Synchronously get a list of all files in the directory (non-recursive). |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialise private attributes. |
| [`new_remote()`](#new_remote) | Create a new Dir reference for a remote directory that will be written to. |
| [`pre_init()`](#pre_init) | Internal: Pydantic validator to set default name from path. |
| [`schema_match()`](#schema_match) | Internal: Check if incoming schema matches Dir schema. |
| [`walk()`](#walk) | Asynchronously walk through the directory and yield File objects. |
| [`walk_sync()`](#walk_sync) | Synchronously walk through the directory and yield File objects. |


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

**Returns:** The absolute path to the downloaded directory

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

**Returns:** The absolute path to the downloaded directory

### exists()

```python
def exists()
```
Asynchronously check if the directory exists.

Example (Async):

```python
@env.task
async def check_directory(d: Dir) -> bool:
    if await d.exists():
        print("Directory exists!")
        return True
    return False
```


**Returns**

True if the directory exists, False otherwise


### exists_sync()

```python
def exists_sync()
```
Synchronously check if the directory exists.

Use this in non-async tasks or when you need synchronous directory existence checking.

Example (Sync):

```python
@env.task
def check_directory_sync(d: Dir) -> bool:
    if d.exists_sync():
        print("Directory exists!")
        return True
    return False
```


**Returns**

True if the directory exists, False otherwise


### from_existing_remote()

```python
def from_existing_remote(
    remote_path: str,
    dir_cache_key: Optional[str],
) -> Dir[T]
```
Create a Dir reference from an existing remote directory.

Use this when you want to reference a directory that already exists in remote storage without uploading it.

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

**Returns:** A new Dir instance pointing to the existing remote directory

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

**Returns:** A new Dir instance pointing to the uploaded directory

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

**Returns:** A new Dir instance pointing to the uploaded directory

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

**Returns:** A File instance if the file exists, None otherwise

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

**Returns:** A File instance if the file exists, None otherwise

### list_files()

```python
def list_files()
```
Asynchronously get a list of all files in the directory (non-recursive).

Use this when you need a list of all files in the top-level directory at once.

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


**Returns**

A list of File objects for files in the top-level directory


### list_files_sync()

```python
def list_files_sync()
```
Synchronously get a list of all files in the directory (non-recursive).

Use this in non-async tasks when you need a list of all files in the top-level directory at once.

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


**Returns**

A list of File objects for files in the top-level directory


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

### new_remote()

```python
def new_remote(
    dir_name: Optional[str],
    hash: Optional[str],
) -> Dir[T]
```
Create a new Dir reference for a remote directory that will be written to.

Use this when you want to create a new directory and write files into it
directly without creating a local directory first.



| Parameter | Type | Description |
|-|-|-|
| `dir_name` | `Optional[str]` | Optional name for the remote directory. If not set, a generated name will be used. |
| `hash` | `Optional[str]` | Optional precomputed hash value to use for cache key computation when this Dir is used as an input to discoverable tasks. |

**Returns:** A new Dir instance with a generated remote path.

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

Yields:
    File objects for each file found in the directory


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

Yields:
    File objects for each file found in the directory


| Parameter | Type | Description |
|-|-|-|
| `recursive` | `bool` | If True, recursively walk subdirectories. If False, only list files in the top-level directory. |
| `file_pattern` | `str` | Glob pattern to filter files (e.g., "*.txt", "*.csv"). Default is "*" (all files). |
| `max_depth` | `Optional[int]` | Maximum depth for recursive walking. If None, walk through all subdirectories. |

