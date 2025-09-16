---
title: Files and directories
weight: 90
variants: +flyte +serverless +byoc +selfmanaged
---

# Files and directories

Flyte provides the [`flyte.io.File`](../../api-reference/flyte-sdk/packages/flyte.io#flyteiofile) and
[`flyte.io.Dir`](../../api-reference/flyte-sdk/packages/flyte.io#flyteiodir) types to represent files and directories, respectively.
Together with [`flyte.io.DataFrame`](./dataframes) they constitute the *offloaded data types* - unlike [materialized types](./dataclasses-and-structures) like dataclasses, these pass references rather than full data content.

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

The upload happens when the [`from_local`](../../api-reference/flyte-sdk/packages/flyte.io#from_local) command is called.
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

## Advanced Example: Mixing Files with Materialized Types

Files can be combined with [materialized types](./dataclasses-and-structures) like dataclasses and Pydantic models in the same workflow. This example demonstrates a batch processing pipeline that uses materialized types for structured data and Files for larger data storage.

The workflow processes prediction requests (materialized), writes results to a CSV file (offloaded), and then reads from that file to compute statistics.

```python
import asyncio
import csv
from dataclasses import dataclass
from typing import List

from pydantic import BaseModel

import flyte
from flyte.io import File

env = flyte.TaskEnvironment(name="mixed-types-example")


@dataclass
class InferenceRequest:
    feature_a: float
    feature_b: float


@env.task
async def predict_one(request: InferenceRequest) -> float:
    """
    A dummy linear model: prediction = 2 * feature_a + 3 * feature_b + bias(=1.0)
    """
    return 2.0 * request.feature_a + 3.0 * request.feature_b + 1.0


@dataclass
class BatchRequest:
    requests: List[InferenceRequest]


class BatchPredictionResults(BaseModel):
    predictions: List[float]  # Materialized: small list stored directly
    results_file: File        # Offloaded: file stored as reference

    class Config:
        arbitrary_types_allowed = True


@env.task
async def predict_batch(batch: BatchRequest) -> BatchPredictionResults:
    """
    Runs predictions and stores results both as materialized data and in a file.
    """
    tasks = [predict_one(request=req) for req in batch.requests]
    results = await asyncio.gather(*tasks)

    # Write predictions to a CSV file (offloaded storage)
    output_path = "predictions.csv"
    with open(output_path, mode="w", newline="") as f:  # noqa: ASYNC230
        writer = csv.writer(f)
        writer.writerow(["prediction"])
        for p in results:
            writer.writerow([p])

    csv_file = await File.from_local(output_path)

    return BatchPredictionResults(
        predictions=results,      # Materialized: passed directly
        results_file=csv_file     # Offloaded: passed as reference
    )


@env.task
async def avg_from_file(results: BatchPredictionResults) -> float:
    """
    Reads the CSV file to compute average, demonstrating file access.
    """
    total = 0.0
    count = 0
    async with results.results_file.open() as f:
        iter_f = iter(f)
        next(iter_f)  # Skip header
        for row in iter_f:
            total += float(row.strip())
            count += 1

    return total / count if count else 0.0


@env.task
async def mixed_types_workflow(batch: BatchRequest):
    """
    Demonstrates mixing materialized and offloaded data types.
    """
    results = await predict_batch(batch=batch)

    # Access materialized data directly
    print(f"Direct access to predictions: {results.predictions}")

    # Access offloaded data through file operations
    avg = await avg_from_file(results=results)
    print(f"Average from file: {avg}")


if __name__ == "__main__":
    flyte.init(
        endpoint="localhost:8090",
        insecure=True,
        project="testproject",
        domain="development",
        org="testorg",
    )

    batch_req = BatchRequest(
        requests=[
            InferenceRequest(feature_a=1.0, feature_b=2.0),
            InferenceRequest(feature_a=3.0, feature_b=4.0),
            InferenceRequest(feature_a=5.0, feature_b=6.0),
        ]
    )

    run = flyte.run(mixed_types_workflow, batch_req)
    print(f"Run URL: {run.url}")
```

