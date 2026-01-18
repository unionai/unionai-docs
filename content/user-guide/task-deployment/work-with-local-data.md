---
title: Work with local data
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
sidebar_expanded: true
---

# Work with local data

When running Flyte tasks that take inputs like DataFrames, files, or directories, data is passed between actions through the configured blob store. For details on how data flows through your workflows, see [data flow](../run-scaling/data-flow).

Flyte provides several built-in types for handling data:
- `flyte.io.DataFrame` for tabular data
- `flyte.io.File` for individual files
- `flyte.io.Dir` for directories

You can also create custom type extensions for specialized data types. See [custom types](../task-programming/handling-custom-types) for details.

## Local execution

One of the most powerful features of Flyte is the ability to work with data entirely locally, without creating a remote run. When you run tasks in local mode, all inputs, outputs, and intermediate data stay on your local machine.

```python
import flyte

env = flyte.TaskEnvironment(name="local_data")

@env.task
async def process_data(data: str) -> str:
    return f"Processed: {data}"

# Run locally - no remote storage needed
run = flyte.with_runcontext(mode="local").run(process_data, data="test")
run.wait()
print(run.outputs()[0])
```

For more details on local execution, see [how task run works](how-task-run-works#local-execution).

## Uploading local data to remote runs

When you want to send local data to a remote task, you need to upload it first. Flyte provides a secure data uploading system that handles this automatically. The same system used for [code bundling](packaging) can upload files, DataFrames, and directories.

To upload local data, use the Flyte core representation for that type with the `from_local_sync()` method.

### Uploading DataFrames

Use `flyte.io.DataFrame.from_local_sync()` to upload a local DataFrame:

```python
from typing import Annotated

import pandas as pd

import flyte
import flyte.io

img = flyte.Image.from_debian_base()
img = img.with_pip_packages("pandas", "pyarrow")

env = flyte.TaskEnvironment(
    "dataframe_usage",
    image=img,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)


@env.task
async def process_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Process a DataFrame and return the result."""
    df["processed"] = True
    return df


if __name__ == "__main__":
    flyte.init_from_config()

    # Create a local pandas DataFrame
    local_df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "value": [10, 20, 30]
    })

    # Upload the local DataFrame for remote execution
    uploaded_df = flyte.io.DataFrame.from_local_sync(local_df)

    # Pass to a remote task
    run = flyte.run(process_dataframe, df=uploaded_df)
    print(f"Run URL: {run.url}")
    run.wait()
    print(run.outputs()[0])
```

### Uploading files

Use `flyte.io.File.from_local_sync()` to upload a local file:

```python
import tempfile

import flyte
from flyte.io import File

env = flyte.TaskEnvironment(name="file-local")


@env.task
async def process_file(file: File) -> str:
    """Read and process a file."""
    async with file.open("rb") as f:
        content = bytes(await f.read())
        return content.decode("utf-8")


if __name__ == "__main__":
    flyte.init_from_config()

    # Create a temporary local file
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt") as temp:
        temp.write("Hello, Flyte!")
        temp_path = temp.name

    # Upload the local file for remote execution
    file = File.from_local_sync(temp_path)

    # Pass to a remote task
    run = flyte.run(process_file, file=file)
    print(f"Run URL: {run.url}")
    run.wait()
    print(run.outputs()[0])
```

### Uploading directories

Use `flyte.io.Dir.from_local_sync()` to upload a local directory:

```python
import os
import tempfile

import flyte
from flyte.io import Dir

env = flyte.TaskEnvironment(name="dir-local")


@env.task
async def process_dir(dir: Dir) -> dict[str, str]:
    """Process a directory and return file contents."""
    file_contents = {}
    async for file in dir.walk(recursive=False):
        if file.name.endswith(".py"):
            async with file.open("rb") as f:
                content = bytes(await f.read())
                file_contents[file.name] = content.decode("utf-8")[:100]
    return file_contents


if __name__ == "__main__":
    flyte.init_from_config()

    # Create a temporary directory with test files
    with tempfile.TemporaryDirectory() as temp_dir:
        for i in range(3):
            with open(os.path.join(temp_dir, f"file{i}.py"), "w") as f:
                f.write(f"print('Hello from file {i}!')")

        # Upload the local directory for remote execution
        dir = Dir.from_local_sync(temp_dir)

        # Pass to a remote task
        run = flyte.run(process_dir, dir=dir)
        print(f"Run URL: {run.url}")
        run.wait()
        print(run.outputs()[0])
```

## Passing outputs between runs

If you're passing outputs from a previous run to a new run, no upload is needed. Flyte's data is represented using native references that point to storage locations, so passing them between runs works automatically:

```python
import flyte

flyte.init_from_config()

# Get outputs from a previous run
previous_run = flyte.remote.Run.get("my_previous_run")
previous_output = previous_run.outputs()[0]  # Already a Flyte reference

# Pass directly to a new run - no upload needed
new_run = flyte.run(my_task, data=previous_output)
```

## Performance considerations

The `from_local_sync()` method uses HTTP to upload data. This is convenient but not the most performant option for large datasets.

**Best suited for:**
- Small to medium test datasets
- Development and debugging
- Quick prototyping

**For larger data uploads**, configure cloud storage access and use `flyte.storage` directly:

```python
import flyte
import flyte.storage

# Configure storage access
flyte.init_from_config(
    storage=flyte.storage.S3.auto(region="us-east-2")
)
```

For details on configuring storage access, see [interact with runs and actions](interacting-with-runs#accessing-large-data-from-cloud-storage).

## Summary

| Scenario | Approach |
|----------|----------|
| Local development and testing | Use local execution mode |
| Small test data to remote tasks | Use `from_local_sync()` |
| Passing data between runs | Pass outputs directly (automatic) |
| Large datasets | Configure `flyte.storage` for direct cloud access |