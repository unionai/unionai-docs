---
title: Files and directories
weight: 90
variants: +flyte +serverless +byoc +selfmanaged
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

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/files-and-directories/file_and_dir.py" fragment="write-file" lang="python" >}}

The upload happens when the [`File.from_local`](../../api-reference/flyte-sdk/packages/flyte.io/file#from_local) command is called.
Because the upload would otherwise block execution, `File.from_local` is implemented as an `async` function.
The Flyte SDK frequently uses this class constructor pattern, so you will see it with other types as well.

This is a slightly more complicated task that calls the task above to produce `File` objects.

These are assembled into a directory and the `Dir` object is returned, also via invoking `from_local`.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/files-and-directories/file_and_dir.py" fragment="write-and-check-files" lang="python" >}}

Finally, these tasks show how to use an offloaded type as an input.
Helper functions like `walk` and `open` have been added to the objects
and do what you might expect.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/files-and-directories/file_and_dir.py" fragment="create-and-check-dir" lang="python" >}}
