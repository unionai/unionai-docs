---
title: Dataclasses and structures
weight: 70
variants: +flyte +serverless +byoc +selfmanaged
---

# Dataclasses and structures

Dataclasses and Pydantic models are fully supported in Flyte as **materialized data types**:
Structured data where the full content is serialized and passed between tasks.
Use these as you would normally, passing them as inputs and outputs of tasks.

Unlike **offloaded types** like [`DataFrame`s](./dataframes), [`File`s and `Dir`s](./files-and-directories), dataclass and Pydantic model data is fully serialized, stored, and deserialized between tasks.
This makes them ideal for configuration objects, metadata, and smaller structured data where all fields should be serializable.

## Example: Combining Dataclasses and Pydantic Models

This example demonstrates how dataclasses and Pydantic models work together as materialized data types, showing nested structures and batch processing patterns:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataclasses-and-structures/example.py" lang="python" >}}

## Running the example

You can run the example with python like this:

```shell
python dataclasses-and-structures.py
```

This will run the `__main__` block, which initializes Flyte and deploys your code to the backend platform configured in your Flyte config file.
Not that in here there are two nested runs: the outer one runs the `summarize_results` task, and the inner one runs the `process_batch` task.
It uses the example `BatchRequest` dataclass defined in the code as input to the `process_batch` task, and then passes the output to the `summarize_results` task.

Alternatively, you can run the example using the `flyte` CLI:

```shell
flyte run dataclass_example.py process_batch --batch '{"requests": [{"feature_a": 1, "feature_b": 2}, {"feature_a": 3, "feature_b": 4}], "batch_id": "test_batch"}'
```

Here, the `--batch` argument is used because it matches the name of the parameter in the `process_batch` task, and its value is passed as a JSON string representing the `BatchRequest` dataclass.

You could then take the output of that run (a `PredictionSummary` Pydantic model) and pass it to the `summarize_results` task like this:

```shell
flyte run dataclass_example.py summarize_results --summary '{"predictions": [8.0, 18.0], "average": 13.0, "count": 2, "batch_id": "test_batch"}'
```
