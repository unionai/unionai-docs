---
title: Files and directories
weight: 70
variants: +flyte +serverless +byoc +selfmanaged
---

# Files and directories

Flyte provides the [`flyte.io.File`](../api-reference/flyte-sdk/packages/flyte.io#flyteiofile) and
[`flyte.io.Dir`](../api-reference/flyte-sdk/packages/flyte.io#flyteiodir) types to represent files and folders, respectively.
Together with [`flyte.io.StructuredDataset`](../api-reference/flyte-sdk/packages/flyte.io#flyteiostructureddataset) they constitute the *offloaded data types*.

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

```python
import asyncio
import tempfile
from pathlib import Path

import flyte
from flyte.io import Dir, File

env = flyte.TaskEnvironment(name="files-and-folders")


@env.task
async def write_file(name: str) -> File:

    # Create a file and write some content to it
    with open("test.txt", "w") as f:
        f.write(f"hello world {name}")

    # Upload the file using flyte
    uploaded_file_obj = await File.from_local("test.txt")
    return uploaded_file_obj

```

The upload happens when the [`from_local`](../api-reference/flyte-sdk/packages/flyte.io#from_local) command is called.
Because the upload would otherwise block execution, `from_local` is implemented as an `async` function.
The Flyte SDK frequently uses this class constructor pattern, so you will see it with other types as well.

This is a slightly more complicated task that calls the task above to produce `File` objects.
These are assembled into a directory and the `Dir` object is returned, also via invoking `from_local`.

```python
@env.task
async def write_and_check_files() -> Dir:
    coros = []
    for name in ["Alice", "Bob", "Eve"]:
        coros.append(write_file(name=name))

    vals = await asyncio.gather(*coros)
    temp_dir = tempfile.mkdtemp()
    for file in vals:
        async with file.open() as fh:
            contents = fh.read()
            print(f"File {file.path} contents: {contents}")
            new_file = Path(temp_dir) / file.name
            with open(new_file, "wb") as out:  # noqa: ASYNC230
                out.write(contents)
    print(f"Files written to {temp_dir}")

    # walk the directory and ls
    for path in Path(temp_dir).iterdir():
        print(f"File: {path.name}")

    my_dir = await Dir.from_local(temp_dir)
    return my_dir
```

Finally, these tasks show how to use an offloaded type as an input.
Helper functions like `walk` and `open` have been added to the objects
and do what you might expect.

```python
@env.task
async def check_dir(my_dir: Dir):
    print(f"Dir {my_dir.path} contents:")
    async for file in my_dir.walk():
        print(f"File: {file.name}")
        async with file.open() as fh:
            contents = fh.read()
            print(f"Contents: {contents.decode('utf-8')}")


@env.task
async def create_and_check_dir():
    my_dir = await write_and_check_files()
    await check_dir(my_dir=my_dir)


if __name__ == "__main__":
    flyte.init_from_config("./config.yaml")
    run = flyte.run(create_and_check_dir)
    print(run.name)
    print(run.url)
    run.wait(run)
```
