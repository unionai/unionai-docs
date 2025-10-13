---
title: DataFrames
weight: 80
variants: +flyte +serverless +byoc +selfmanaged
---

# DataFrames

By default, return values in Python are materialized - meaning the actual data is downloaded and loaded into memory. This applies to simple types like integers, as well as more complex types like DataFrames.

To avoid downloading large datasets into memory, Flyte V2 exposes [`flyte.io.dataframe`](../../api-reference/flyte-sdk/packages/flyte.io#flyteiodataframe): a thin,  uniform wrapper type for DataFrame-style objects that allows you to pass a reference to the data, rather than the fully materialized contents.

The `flyte.io.DataFrame` type provides serialization support for common engines like `pandas`, `polars`, `pyarrow`, `dask`, etc.; enabling you to move data between different DataFrame backends.

## Constructing a flyte.io.DataFrame

- Use the `from_df` method to create a `flyte.io.DataFrame` from a native object:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="from_df" lang="python" >}}

## Declaring DataFrame inputs and outputs

To declare a task that returns a native pandas DataFrame, you can use `pd.DataFrame` directly in the signature, the SDK will treat the return as a DataFrame-type output and upload it at task completion.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="native" lang="python" >}}

To use the unified `flyte.io.DataFrame` wrapper (recommended when you want to be explicit about the DataFrame type and storage format), use an `Annotated` type where the second argument encodes format or other lightweight hints.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="annotated" lang="python" >}}

## Reading a DataFrame value inside a task

When a task receives a `flyte.io.DataFrame`, you can open it and request a concrete backend representation. For example, to download as a pandas DataFrame:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="download" lang="python" >}}

The `open(...)` call delegates to the DataFrame handler for the stored format and converts to the requested in-memory type.

You can also leverage Flyte to automatically download and convert the dataframe between types when needed:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="automatic" lang="python" >}}

## Example — full usage

The following example ([code](https://github.com/unionai/unionai-examples/blob/main/v2/user-guide/task-programming/dataframes/full_usage.py)) demonstrates creating a raw pandas DataFrame, wrapping a pandas DataFrame into `flyte.io.DataFrame`, joining them inside another task, and running locally.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/full_usage.py" lang="python" >}}
