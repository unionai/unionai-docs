---
title: Data flow
weight: 1
variants: +flyte +serverless +byoc +selfmanaged
---

# Data flow

Understanding how data flows between tasks is critical for optimizing workflow performance in Flyte. Tasks take inputs and produce outputs, with data flowing seamlessly through your workflow using an efficient transport layer.

## Overview

Flyte tasks are run to completion. Each task takes inputs and produces exactly one output. Even if multiple instances run concurrently (such as in retries), only one output will be accepted. This deterministic data flow model provides several key benefits:

1. **Reduced boilerplate**: Automatic handling of files, DataFrames, directories, custom types, data classes, Pydantic models, and primitive types without manual serialization.
2. **Type safety**: Optional type annotations enable deeper type understanding, automatic UI form generation, and runtime type validation.
3. **Efficient transport**: Data is passed by reference (files, directories, DataFrames) or by value (primitives) based on type.
4. **Durable storage**: All data is stored durably and accessible through APIs and the UI.
5. **Caching support**: Efficient caching using shallow immutable references for referenced data.

## Data types and transport

Flyte handles different data types with different transport mechanisms:

### Passed by reference

These types are not copied but passed as references to storage locations:

- **Files**: `flyte.io.File`
- **Directories**: `flyte.io.Directory`
- **Dataframes**: `flyte.io.DataFrame`, `pd.DataFrame`, `pl.DataFrame`, etc.

Dataframes are automatically converted to Parquet format and read using Arrow for zero-copy reads. Use `flyte.io.DataFrame` for lazy materialization to any supported type like pandas or polars.

### Passed by value (inline I/O)

Primitive and structured types are serialized and passed inline:

| Type Category | Examples | Serialization |
|--------------|----------|---------------|
| **Primitives** | `int`, `float`, `str`, `bool`, `None` | MessagePack |
| **Time types** | `datetime.datetime`, `datetime.date`, `datetime.timedelta` | MessagePack |
| **Collections** | `list`, `dict`, `tuple` | MessagePack |
| **Data structures** | data classes, Pydantic `BaseModel` | MessagePack |
| **Enums** | `enum.Enum` subclasses | MessagePack |
| **Unions** | `Union[T1, T2]`, `Optional[T]` | MessagePack |
| **Protobuf** | `google.protobuf.Message` | Binary |

Flyte uses efficient MessagePack serialization for most types, providing compact binary representation with strong type safety.

> [!NOTE]
> If type annotations are not used, or if `typing.Any` or unrecognized types are used, data will be pickled. By default, picked objects smaller than 10KB are passed inline, while larger picked objects are automatically passed as a file. Pickling allows for progressive typing but should be used carefully.


## Task execution and data flow

### Input download

When a task starts:

1. **Inline inputs download**: The task downloads inline inputs from the configured Flyte object store.
2. **Size limits**: By default, inline inputs are limited to 10MB, but this can be adjusted using `flyte.TaskEnvironment`'s `max_inline_io` parameter.
3. **Memory consideration**: Inline data is materialized in memory, so adjust your task resources accordingly.
4. **Reference materialization**: Reference data (files, directories) is passed using special types in `flyte.io`. Dataframes are automatically materialized if using `pd.DataFrame`. Use `flyte.io.DataFrame` to avoid automatic materialization.

### Output upload

When a task returns data:

1. **Inline data**: Uploaded to the Flyte object store configured at the organization, project, or domain level.
2. **Reference data**: Stored in the same metadata store by default, or configured using `flyte.with_runcontext(raw_data_storage=...)`.
3. **Separate prefixes**: Each task creates one output per retry attempt in separate prefixes, making data incorruptible by design.

## Task-to-task data flow

When a task invokes downstream tasks:

1. **Input recording**: The input to the downstream task is recorded to the object store.
2. **Reference upload**: All referenced objects are uploaded (if not already present).
3. **Task invocation**: The downstream task is invoked on the remote server.
4. **Parallel execution**: When multiple tasks are invoked in parallel using `flyte.map` or `asyncio`, inputs are written in parallel.
5. **Storage layer**: Data writing uses the `flyte.storage` layer, backed by the Rust-based `object-store` crate and optionally `fsspec` plugins.
6. **Output download**: Once the downstream task completes, inline outputs are downloaded and returned to the calling task.

## Caching and data hashing

Understanding how Flyte caches data is essential for performance optimization.

### Cache key computation

A cache hit occurs when the following components match:

- **Task name**: The fully-qualified task name
- **Computed input hash**: Hash of all inputs (excluding `ignored_inputs`)
- **Task interface hash**: Hash of input and output types
- **Task config hash**: Hash of task configuration
- **Cache version**: User-specified or automatically computed

### Inline data caching

All inline data is cached using a consistent hashing system. The cache key is derived from the data content.

### Reference data hashing

Reference data (files, directories) is hashed shallowly by default using the hash of the storage location. You can customize hashing:

- Use `flyte.io.File.new_remote()` or `flyte.io.File.from_existing_remote()` with custom hash functions or values.
- Provide explicit hash values for deep content hashing if needed.

### Cache control

Control caching behavior using `flyte.with_runcontext`:

- **Scope**: Set `cache_lookup_scope` to `"global"` or `"project/domain"`.
- **Disable cache**: Set `overwrite_cache=True` to force re-execution.

For more details on caching configuration, see [Caching](../task-configuration/caching).

## Traces and data flow

When using [traces](../task-programming/traces), the data flow behavior is different:

1. **Full execution first**: The trace is fully executed before inputs and outputs are recorded.
2. **Checkpoint behavior**: Recording happens like a checkpoint at the end of trace execution.
3. **Streaming iterators**: The entire output is buffered and recorded after the stream completes. Buffering is pass-through, allowing caller functions to consume output while buffering.
4. **Chained traces**: All traces are recorded after the last one completes consumption.
5. **Same process with `asyncio`**: Traces run within the same Python process and support `asyncio` parallelism, so failures can be retried, effectively re-running the trace.
6. **Lightweight overhead**: Traces only have the overhead of data storage (no task orchestration overhead).

> [!NOTE]
> Traces are not a substitute for tasks if you need caching. Tasks provide full caching capabilities, while traces provide lightweight checkpointing with storage overhead. However, traces support concurrent execution using `asyncio` patterns within a single task.

## Object stores and latency considerations

By default, Flyte uses object stores like S3, GCS, Azure Storage, and R2 as metadata stores. These have high latency for smaller objects, so:

- **Minimum task duration**: Tasks should take at least a second to run to amortize storage overhead.
- **Future improvements**: High-performance metastores like Redis and PostgreSQL may be supported in the future. Contact the Union team if you're interested.

## Configuring data storage

### Organization and project level

Object stores are configured at the organization level or per project/domain. Documentation for this configuration is coming soon.

### Per-run configuration

Configure raw data storage on a per-run basis using `flyte.with_runcontext`:

```python
run = flyte.with_runcontext(
    raw_data_storage="s3://my-bucket/custom-path"
).run(my_task, input_data=data)
```

This allows you to control where reference data (files, directories, DataFrames) is stored for specific runs.
