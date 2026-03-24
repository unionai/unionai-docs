---
title: JsonlFile
version: 2.0.10
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# JsonlFile

**Package:** `flyteplugins.jsonl`

A file type for JSONL (JSON Lines) files, backed by `orjson` for fast
serialisation.

Provides streaming read and write methods that process one record at a time
without loading the entire file into memory. Inherits all `File`
capabilities (remote storage, upload/download, etc.).

Supports zstd-compressed files transparently via extension detection
(`.jsonl.zst` / `.jsonl.zstd`).

Example (Async read - compressed or uncompressed):

```python
@env.task
async def process(f: JsonlFile):
    async for record in f.iter_records():
        print(record)
```

Example (Async write - compressed or uncompressed):

```python
@env.task
async def create() -> JsonlFile:
    f = JsonlFile.new_remote("data.jsonl")
    async with f.writer() as w:
        await w.write({"key": "value"})
    return f
```

Example (Sync write - compressed or uncompressed):

```python
@env.task
def create() -> JsonlFile:
    f = JsonlFile.new_remote("data.jsonl")
    with f.writer_sync() as w:
        w.write({"key": "value"})
    return f
```



## Parameters

```python
class JsonlFile(
    path: str,
    name: typing.Optional[str],
    format: str,
    hash: typing.Optional[str],
    hash_method: typing.Optional[flyte.io._hashing_io.HashMethod],
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `name` | `typing.Optional[str]` | |
| `format` | `str` | |
| `hash` | `typing.Optional[str]` | |
| `hash_method` | `typing.Optional[flyte.io._hashing_io.HashMethod]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `lazy_uploader` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`download()`](#download) | Asynchronously download the file to a local path. |
| [`download_sync()`](#download_sync) | Synchronously download the file to a local path. |
| [`exists()`](#exists) | Asynchronously check if the file exists. |
| [`exists_sync()`](#exists_sync) | Synchronously check if the file exists. |
| [`from_existing_remote()`](#from_existing_remote) | Create a File reference from an existing remote file. |
| [`from_local()`](#from_local) | Asynchronously create a new File object from a local file by uploading it to remote storage. |
| [`from_local_sync()`](#from_local_sync) | Synchronously create a new File object from a local file by uploading it to remote storage. |
| [`iter_arrow_batches()`](#iter_arrow_batches) | Stream JSONL as Arrow RecordBatches. |
| [`iter_arrow_batches_sync()`](#iter_arrow_batches_sync) | Sync generator that yields Arrow RecordBatches. |
| [`iter_records()`](#iter_records) | Async generator that yields parsed dicts line by line. |
| [`iter_records_sync()`](#iter_records_sync) | Sync generator that yields parsed dicts line by line. |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialise private attributes. |
| [`named_remote()`](#named_remote) | Create a File reference whose remote path is derived deterministically from *name*. |
| [`new_remote()`](#new_remote) | Create a new File reference for a remote file that will be written to. |
| [`open()`](#open) | Asynchronously open the file and return a file-like object. |
| [`open_sync()`](#open_sync) | Synchronously open the file and return a file-like object. |
| [`pre_init()`](#pre_init) | Internal: Pydantic validator to set default name from path. |
| [`schema_match()`](#schema_match) | Internal: Check if incoming schema matches File schema. |
| [`writer()`](#writer) | Async context manager returning a `JsonlWriter` for streaming writes. |
| [`writer_sync()`](#writer_sync) | Sync context manager returning a `JsonlWriterSync` for streaming writes. |


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
async def download_and_process(f: File) -> str:
    local_path = await f.download()
    # Now process the local file
    with open(local_path, "r") as fh:
        return fh.read()
```

Example (Download to specific path):

```python
@env.task
async def download_to_path(f: File) -> str:
    local_path = await f.download("/tmp/myfile.csv")
    return local_path
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Optional[Union[str, Path]]` | The local path to download the file to. If None, a temporary directory will be used and a path will be generated. |

**Returns:** The absolute path to the downloaded file

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
def download_and_process_sync(f: File) -> str:
    local_path = f.download_sync()
    # Now process the local file
    with open(local_path, "r") as fh:
        return fh.read()
```

Example (Download to specific path):

```python
@env.task
def download_to_path_sync(f: File) -> str:
    local_path = f.download_sync("/tmp/myfile.csv")
    return local_path
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Optional[Union[str, Path]]` | The local path to download the file to. If None, a temporary directory will be used and a path will be generated. |

**Returns:** The absolute path to the downloaded file

### exists()

```python
def exists()
```
Asynchronously check if the file exists.

Example (Async):

```python
@env.task
async def check_file(f: File) -> bool:
    if await f.exists():
        print("File exists!")
        return True
    return False
```



**Returns:** True if the file exists, False otherwise

### exists_sync()

```python
def exists_sync()
```
Synchronously check if the file exists.

Use this in non-async tasks or when you need synchronous file existence checking.

Example (Sync):

```python
@env.task
def check_file_sync(f: File) -> bool:
    if f.exists_sync():
        print("File exists!")
        return True
    return False
```



**Returns:** True if the file exists, False otherwise

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
async def process_existing_file() -> str:
    file = File.from_existing_remote("s3://my-bucket/data.csv")
    async with file.open("rb") as f:
        content = await f.read()
    return content.decode("utf-8")
```



| Parameter | Type | Description |
|-|-|-|
| `remote_path` | `str` | The remote path to the existing file |
| `file_cache_key` | `Optional[str]` | Optional hash value to use for cache key computation. If not specified, the cache key will be computed based on the file's attributes (path, name, format). |

**Returns:** A new File instance pointing to the existing remote file

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
async def upload_local_file() -> File:
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
async def upload_to_specific_path() -> File:
    remote_file = await File.from_local("/tmp/data.csv", "s3://my-bucket/data.csv")
    return remote_file
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Union[str, Path]` | Path to the local file |
| `remote_destination` | `Optional[str]` | Optional remote path to store the file. If None, a path will be automatically generated. |
| `hash_method` | `Optional[HashMethod \| str]` | Optional HashMethod or string to use for cache key computation. If a string is provided, it will be used as a precomputed cache key. If a HashMethod is provided, it will compute the hash during upload. If not specified, the cache key will be based on file attributes. |

**Returns**

A new File instance pointing to the uploaded remote file


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
def upload_local_file_sync() -> File:
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
def upload_to_specific_path() -> File:
    remote_file = File.from_local_sync("/tmp/data.csv", "s3://my-bucket/data.csv")
    return remote_file
```



| Parameter | Type | Description |
|-|-|-|
| `local_path` | `Union[str, Path]` | Path to the local file |
| `remote_destination` | `Optional[str]` | Optional remote path to store the file. If None, a path will be automatically generated. |
| `hash_method` | `Optional[HashMethod \| str]` | Optional HashMethod or string to use for cache key computation. If a string is provided, it will be used as a precomputed cache key. If a HashMethod is provided, it will compute the hash during upload. If not specified, the cache key will be based on file attributes. |

**Returns**

A new File instance pointing to the uploaded remote file


### iter_arrow_batches()

```python
def iter_arrow_batches(
    batch_size: int,
    on_error: Literal['raise', 'skip'] | ErrorHandler,
) -> AsyncGenerator[Any, None]
```
Stream JSONL as Arrow RecordBatches.

Memory usage is bounded by batch_size.


| Parameter | Type | Description |
|-|-|-|
| `batch_size` | `int` | |
| `on_error` | `Literal['raise', 'skip'] \| ErrorHandler` | |

### iter_arrow_batches_sync()

```python
def iter_arrow_batches_sync(
    batch_size: int,
    on_error: Literal['raise', 'skip'] | ErrorHandler,
) -> Generator[Any, None, None]
```
Sync generator that yields Arrow RecordBatches.

Memory usage is bounded by batch_size.


| Parameter | Type | Description |
|-|-|-|
| `batch_size` | `int` | |
| `on_error` | `Literal['raise', 'skip'] \| ErrorHandler` | |

### iter_records()

```python
def iter_records(
    on_error: Literal['raise', 'skip'] | ErrorHandler,
) -> AsyncGenerator[dict[str, Any], None]
```
Async generator that yields parsed dicts line by line.


| Parameter | Type | Description |
|-|-|-|
| `on_error` | `Literal['raise', 'skip'] \| ErrorHandler` | |

### iter_records_sync()

```python
def iter_records_sync(
    on_error: Literal['raise', 'skip'] | ErrorHandler,
) -> Generator[dict[str, Any], None, None]
```
Sync generator that yields parsed dicts line by line.


| Parameter | Type | Description |
|-|-|-|
| `on_error` | `Literal['raise', 'skip'] \| ErrorHandler` | |

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

### named_remote()

```python
def named_remote(
    name: str,
) -> File[T]
```
Create a File reference whose remote path is derived deterministically from *name*.

Unlike `new_remote`, which generates a random path on every call, this method
produces the same path for the same *name* within a given task execution. This makes
it safe across retries: the first attempt uploads to the path and subsequent retries
resolve to the identical location without re-uploading.

The path is optionally namespaced by the node ID extracted from the backend
raw-data path, which follows the convention:

    {run_name}-{node_id}-{attempt_index}

If extraction fails, the function falls back to the run base directory alone.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Plain filename (e.g., "data.csv"). Must not contain path separators. |

**Returns:** A `File` instance whose path is stable across retries.

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
async def create_csv() -> File:
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

**Returns:** A new File instance with a generated remote path

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
async def read_file(f: File) -> str:
    async with f.open("rb") as fh:
        content = bytes(await fh.read())
        return content.decode("utf-8")
```

Example (Async Write):

```python
@env.task
async def write_file() -> File:
    f = File.new_remote()
    async with f.open("wb") as fh:
        await fh.write(b"Hello, World!")
    return f
```

Example (Streaming Read):

```python
@env.task
async def stream_read(f: File) -> str:
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
| `mode` | `str` | The mode to open the file in (default: 'rb'). Common modes: 'rb' (read binary), 'wb' (write binary), 'rt' (read text), 'wt' (write text) |
| `block_size` | `Optional[int]` | Size of blocks for reading in bytes. Useful for streaming large files. |
| `cache_type` | `str` | Caching mechanism to use ('readahead', 'mmap', 'bytes', 'none') |
| `cache_options` | `Optional[dict]` | Dictionary of options for the cache |
| `compression` | `Optional[str]` | Compression format or None for auto-detection |
| `kwargs` | `**kwargs` | |

**Returns:** An async file-like object that can be used with async read/write operations

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
def read_file_sync(f: File) -> str:
    with f.open_sync("rb") as fh:
        content = fh.read()
        return content.decode("utf-8")
```

Example (Sync Write):

```python
@env.task
def write_file_sync() -> File:
    f = File.new_remote()
    with f.open_sync("wb") as fh:
        fh.write(b"Hello, World!")
    return f
```



| Parameter | Type | Description |
|-|-|-|
| `mode` | `str` | The mode to open the file in (default: 'rb'). Common modes: 'rb' (read binary), 'wb' (write binary), 'rt' (read text), 'wt' (write text) |
| `block_size` | `Optional[int]` | Size of blocks for reading in bytes. Useful for streaming large files. |
| `cache_type` | `str` | Caching mechanism to use ('readahead', 'mmap', 'bytes', 'none') |
| `cache_options` | `Optional[dict]` | Dictionary of options for the cache |
| `compression` | `Optional[str]` | Compression format or None for auto-detection |
| `kwargs` | `**kwargs` | |

**Returns:** A file-like object that can be used with standard read/write operations

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
Internal: Check if incoming schema matches File schema. Not intended for direct use.


| Parameter | Type | Description |
|-|-|-|
| `incoming` | `dict` | |

### writer()

```python
def writer(
    flush_bytes: int,
    compression_level: int,
) -> AsyncGenerator[JsonlWriter, None]
```
Async context manager returning a `JsonlWriter` for streaming writes.

If the file path ends in `.jsonl.zst`, output is zstd-compressed.



| Parameter | Type | Description |
|-|-|-|
| `flush_bytes` | `int` | Buffer flush threshold in bytes (default 1 MB). |
| `compression_level` | `int` | Zstd compression level (default 3). Only used for `.jsonl.zst` paths. Higher = smaller files, slower writes. |

### writer_sync()

```python
def writer_sync(
    flush_bytes: int,
    compression_level: int,
) -> Generator[JsonlWriterSync, None, None]
```
Sync context manager returning a `JsonlWriterSync` for streaming writes.

If the file path ends in `.jsonl.zst`, output is zstd-compressed.



| Parameter | Type | Description |
|-|-|-|
| `flush_bytes` | `int` | Buffer flush threshold in bytes (default 1 MB). |
| `compression_level` | `int` | Zstd compression level (default 3). Only used for `.jsonl.zst` paths. Higher = smaller files, slower writes. |

