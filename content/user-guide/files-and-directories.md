---
title: Files and directories
weight: 70
variants: +flyte +serverless +byoc +selfmanaged
---

# Files and directories

Flyte continues to support files and folders and top level type constructs. These are two of the three major offloaded types
(dataframes of all kinds being the third). Once offloaded, they are persisted on the blob store configured for your Flyte cluster.
While the SDK will handle the underlying call to the blob store, users are still responsible for invoking the commands.
Files and folders are no longer uploaded automatically at the end of a task simply by returning them.

The examples below show the basic use-cases of uploading Files and Dirs created locally, and using them as inputs to a task.

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

The upload happens when the `from_local` command is called, which is why it's an async function. The Flyte SDK frequently
uses this class constructor pattern so you'll see it with other types as well.


This is a slightly more complicated task that calls the task above to produce Files. These files are assembled into a directory
and the Dir is returned, also via invoking `from_local`.
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

Finally these tasks show how to use an offloaded type as an input. Helper functions like `walk` and `open` have been added to the objects
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
