---
title: Files and directories
weight: 1
variants: +flyte +union
---

# Files and directories

Flyte provides the `flyte.io.File` and
`flyte.io.Dir` types to represent files and directories, respectively.
Together with [`flyte.io.DataFrame`](./dataframes) they constitute the *offloaded data types*. Unlike [materialized types](./dataclasses-and-structures) like data classes, these pass references rather than full data content.

A variable of an offloaded type does not contain its actual data, but rather a reference to the data.
The actual data is stored in the internal blob store of your Union/Flyte instance.
When a variable of an offloaded type is first created, its data is uploaded to the blob store.
It can then be passed from task to task as a reference.
The actual data is only downloaded from the blob stored when the task needs to access it, for example, when the task calls `open()` on a `File` or `Dir` object.

This allows Flyte to efficiently handle large files and directories without needing to transfer the data unnecessarily.
Even very large data objects like video files and DNA datasets can be passed efficiently between tasks.

For the full picture of what gets stored in the bucket versus what stays in the control plane database, see [Where your data lives](../core-concepts/where-data-lives).

The `File` and `Dir` classes provide both synchronous and asynchronous methods to interact with the data, so you can use them from either kind of task. See [Synchronous and asynchronous APIs](#synchronous-and-asynchronous-apis) for the full method pairing.

> [!NOTE]
> Because `File` and `Dir` are passed by reference, a downstream cached task does not get a cache hit on identical content stored at a new path. To cache on content, attach a hash at production time. See [Content-based caching for DataFrames, files, and directories](../task-configuration/caching#content-based-caching-for-dataframes-files-and-directories).

## Example usage

The examples below show the basic use-cases of uploading files and directories created locally, and using them as inputs to a task.

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/file_and_dir.py" fragment="write-file" lang="python" >}}

The upload happens when the [`File.from_local`](../../api-reference/flyte-sdk/packages/flyte.io/file#from_local) command is called.
Because the upload would otherwise block execution, `File.from_local` is implemented as an `async` function.
The Flyte SDK frequently uses this class constructor pattern, so you will see it with other types as well.

This is a slightly more complicated task that calls the task above to produce `File` objects.

These are assembled into a directory and the `Dir` object is returned, also via invoking `from_local`.

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/file_and_dir.py" fragment="write-and-check-files" lang="python" >}}

Finally, these tasks show how to use an offloaded type as an input.
Helper functions like `walk` and `open` have been added to the objects
and do what you might expect.

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/file_and_dir.py" fragment="create-and-check-dir" lang="python" >}}

## Synchronous and asynchronous APIs

Every I/O operation on `File` and `Dir` comes in two forms, so you can use the offloaded types from both asynchronous and synchronous tasks:

- In an **asynchronous task** (`async def`), use the coroutine methods: `await` the upload, download, and existence calls, use `async with file.open(...)` to stream, and `async for` to walk a `Dir`. This is the pattern shown in [Example usage](#example-usage) above.
- In a **synchronous task** (plain `def`), use the `_sync` variants: `File.from_local_sync()`, `file.open_sync()`, `dir.walk_sync()`, and so on. These block until the operation completes.

The two forms are otherwise equivalent. Pick the one that matches how your task is defined. A few constructors do no I/O and so have a single form that is used unchanged from either kind of task: `File.new_remote()`, `File.from_existing_remote()`, `Dir.new_remote()`, and `Dir.from_existing_remote()`.

### File methods

| Asynchronous (in `async def` tasks) | Synchronous (in `def` tasks) | Purpose |
|---|---|---|
| `await File.from_local(path)` | `File.from_local_sync(path)` | Upload a local file to the blob store |
| `File.new_remote()` | `File.new_remote()` | Allocate a new remote file to stream into |
| `File.from_existing_remote(uri)` | `File.from_existing_remote(uri)` | Reference a file that already exists remotely |
| `async with file.open(mode) as fh` | `with file.open_sync(mode) as fh` | Open the file as a stream for reading or writing |
| `await file.download()` | `file.download_sync()` | Download the file to the local filesystem |
| `await file.exists()` | `file.exists_sync()` | Check whether the file exists |

### Dir methods

| Asynchronous (in `async def` tasks) | Synchronous (in `def` tasks) | Purpose |
|---|---|---|
| `await Dir.from_local(path)` | `Dir.from_local_sync(path)` | Upload a local directory to the blob store |
| `Dir.new_remote()` | `Dir.new_remote()` | Allocate a new remote directory to stream into |
| `Dir.from_existing_remote(uri)` | `Dir.from_existing_remote(uri)` | Reference a directory that already exists remotely |
| `async for f in dir.walk()` | `for f in dir.walk_sync()` | Iterate over the files in the directory |
| `await dir.list_files()` | `dir.list_files_sync()` | List the files in the directory (non-recursive) |
| `await dir.get_file(name)` | `dir.get_file_sync(name)` | Get a single file from the directory by name |
| `await dir.download()` | `dir.download_sync()` | Download the whole directory to the local filesystem |
| `await dir.exists()` | `dir.exists_sync()` | Check whether the directory exists |

> [!NOTE]
> `walk_sync()` additionally accepts a `file_pattern` glob (for example `file_pattern="*.txt"`) to filter the files it yields. Both forms accept `recursive` and `max_depth`.

### Synchronous example

The [example above](#example-usage) uses `await`, `async with`, and `async for`. The same kind of workflow written with the synchronous API uses plain `def` tasks and the `_sync` method names:

```python
import flyte
from flyte.io import File

env = flyte.TaskEnvironment(name="sync-file")


@env.task
def write_file(content: str) -> File:
    # Allocate a new remote file and stream content into it
    f = File.new_remote()
    with f.open_sync("wb") as fh:
        fh.write(content.encode("utf-8"))
    return f


@env.task
def read_file(f: File) -> str:
    # Open the file for reading without downloading the whole object
    with f.open_sync("rb") as fh:
        return fh.read().decode("utf-8")


@env.task
def main() -> str:
    f = write_file(content="hello world")
    return read_file(f)
```

Directories work the same way: use `Dir.from_local_sync()` to upload and `walk_sync()` to iterate:

```python
import os
import tempfile

import flyte
from flyte.io import Dir

env = flyte.TaskEnvironment(name="sync-dir")


@env.task
def upload_dir() -> Dir:
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(3):
            with open(os.path.join(tmp, f"file{i}.txt"), "w") as fh:
                fh.write(f"content {i}")
        # Upload the directory to the blob store
        return Dir.from_local_sync(tmp)


@env.task
def read_dir(d: Dir) -> int:
    count = 0
    # Walk and read every file, all synchronously
    for file in d.walk_sync(recursive=True):
        with file.open_sync("rb") as fh:
            print(f"{file.name}: {fh.read().decode('utf-8')}")
        count += 1
    return count


@env.task
def main() -> int:
    d = upload_dir()
    return read_dir(d)
```

## JSONL files

Flyte provides typed JSON Lines (JSONL) I/O through the `flyteplugins-jsonl` plugin, which extends `File` and `Dir` with the `JsonlFile` and `JsonlDir` types, adding streaming record-level read/write, optional zstd compression, and automatic shard rotation for large datasets.

See the [JSONL integration](../../integrations/jsonl/_index) guide for installation and usage.
