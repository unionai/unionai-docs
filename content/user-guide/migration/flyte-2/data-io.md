---
title: Data types and I/O
weight: 8
variants: +flyte +union
---

# Data types and I/O

Flyte 2 renames the offloaded-data types and makes their I/O `async`, but the mental model is the same: pass lightweight references to large data between tasks. See [Migration](./migration) for the overall approach.

## Files and directories

`FlyteFile` and `FlyteDirectory` become `flyte.io.File` and `flyte.io.Dir` — the way you pass model artifacts and datasets between tasks. The I/O is now `async`: use `await File.from_local(...)` to upload and `file.open(...)` to read. Like their Flyte 1 counterparts, these are lightweight references to offloaded data, not the materialized bytes.

{{< tabs "migration-files" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/files_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/files_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

See [Files and directories](../../task-programming/files-and-directories) for more.

## DataFrames

`StructuredDataset` becomes `flyte.io.DataFrame`. Construct one with `flyte.io.DataFrame.from_df(df)` and read it back with `await df.open(pandas.DataFrame).all()`.

{{< tabs "migration-dataframe" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/dataframe_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/dataframe_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

See [DataFrames](../../task-programming/dataframes) for more.

## Dataclasses and structured types

Flyte 1 required a `@dataclass_json` mixin for dataclass I/O. In Flyte 2, plain dataclasses (and Pydantic `BaseModel`s) work directly as task inputs and outputs — handy for passing around a training config.

{{< tabs "migration-dataclasses" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/dataclasses_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/dataclasses_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Data ETL

Putting the data types together: extract, clean, aggregate, and write out a feature table. `StructuredDataset` becomes `flyte.io.DataFrame`, and the tasks become `async`.

{{< tabs "migration-data-etl" >}}
{{< tab "Flyte 1" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/data_etl_v1.py" lang="python" >}}
{{< /tab >}}
{{< tab "Flyte 2" >}}
{{< code file="/unionai-examples/v2/user-guide/migration/flyte-2/data_etl_v2.py" fragment="all" lang="python" >}}
{{< /tab >}}
{{< /tabs >}}

## Next

- [ML workloads](./ml-workloads) — training, HPO, and batch inference
- [Parallelism and fan-out](./parallelism) — processing partitions in parallel
