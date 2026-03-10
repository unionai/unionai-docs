---
title: Files and directories
weight: 1
variants: +flyte +byoc +selfmanaged
---

# Files and directories

Flyte provides the [`flyte.io.File`](../../api-reference/flyte-sdk/packages/flyte.io/file) and
[`flyte.io.Dir`](../../api-reference/flyte-sdk/packages/flyte.io/dir) types to represent files and directories, respectively.
Together with [`flyte.io.DataFrame`](./dataframes) they constitute the *offloaded data types* - unlike [materialized types](./dataclasses-and-structures) like data classes, these pass references rather than full data content.

A variable of an offloaded type does not contain its actual data, but rather a reference to the data.
The actual data is stored in the internal blob store of your Union/Flyte instance.
When a variable of an offloaded type is first created, its data is uploaded to the blob store.
It can then be passed from task to task as a reference.
The actual data is only downloaded from the blob stored when the task needs to access it, for example, when the task calls `open()` on a `File` or `Dir` object.

This allows Flyte to efficiently handle large files and directories without needing to transfer the data unnecessarily.
Even very large data objects like video files and DNA datasets can be passed efficiently between tasks.

The `File` and `Dir` classes provide both `sync` and `async` methods to interact with the data.

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

## JSONL files

The `flyteplugins-jsonl` package extends `File` and `Dir` with JSONL-aware types: `JsonlFile` and `JsonlDir`. They add streaming record-level read and write on top of the standard file/directory capabilities, with optional zstd compression and automatic shard rotation for large datasets.

```bash
pip install flyteplugins-jsonl
```

### Setup

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="setup" lang="python" >}}

### JsonlFile

`JsonlFile` is a `File` subclass for single JSONL files. Use its async context manager to write records incrementally without requiring the entire dataset to be loaded into memory:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="write-jsonl-file" lang="python" >}}

Reading is equally streaming:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="read-jsonl-file" lang="python" >}}

Compressed files (`.jsonl.zst` / `.jsonl.zstd`) are handled transparently based on the file extension.

### JsonlDir

`JsonlDir` is a `Dir` subclass that shards records across multiple JSONL files. When a shard reaches the `max_bytes` threshold, a new shard is opened automatically. This keeps individual files at a manageable size even for very large datasets:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="write-jsonl-dir" lang="python" >}}

Reading iterates across all shards transparently:

{{< code file="/unionai-examples/v2/user-guide/task-programming/files-and-directories/jsonl.py" fragment="read-jsonl-dir" lang="python" >}}
