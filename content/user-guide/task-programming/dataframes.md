---
title: DataFrames
weight: 80
variants: +flyte +serverless +byoc +selfmanaged
---

# DataFrames

By default, return values in Python are materialized - meaning the actual data is downloaded and loaded into memory. This applies to simple types like integers, as well as more complex types like DataFrames.

To avoid downloading large datasets into memory, Flyte V2 exposes [`flyte.io.dataframe`](../../api-reference/flyte-sdk/packages/flyte.io#flyteiodataframe): a thin,  uniform wrapper type for DataFrame-style objects that allows you to pass a reference to the data, rather than the fully materialized contents.

The `flyte.io.DataFrame` type provides serialization support for common engines like `pandas`, `polars`, `pyarrow`, `dask`, etc.; enabling you to move data between different DataFrame backends.

## Setting up the environment and sample data

For our example we will start by setting up our task environment with the required dependencies and create some sample data.

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="setup" lang="python" >}}

## Create a raw dataframe

Now, let's create a task that returns a native Pandas DataFrame:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="raw-dataframe" lang="python" >}}

This is the most basic use-case of how to pass DataFrames (of all kinds, not just Pandas).
We simply create the DataFrame as normal, and return it.

Because the task has been declared to return a supported native DataFrame type (in this case `pandas.DataFrame` Flyte will automatically detect it, serialize it correctly and upload it at task completion enabling it to be passed transparently to the next task.

Flyte supports auto-serialization for the following DataFrame types:
* `pandas.DataFrame`
* `pyarrow.Table`
* `dask.dataframe.DataFrame`
* `polars.DataFrame`
* `flyte.io.DataFrame` (see below)

## Create a flyte.io.DataFrame

Alternatively you can also create a `flyte.io.DataFrame` object directly from a native object with the `from_df` method:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="from-df" lang="python" >}}

The `flyte.io.DataFrame` class creates a thin wrapper around objects of any standard DataFrame type. It serves as a generic "any dataframe type" (a concept that Python itself does not cxurrently offer).

As with native DataFrame types, Flyte will automatically serialize and upload the data at task completion.

The advantage of the unified `flyte.io.DataFrame` wrapper is that you can be explicit about the storage format that makes sense for your use case, by using an `Annotated` type where the second argument encodes format or other lightweight hints. For example, here we specify that the DataFrame should be stored as Parquet:

## Automatically convert between types

You can leverage Flyte to automatically download and convert the dataframe between types when needed:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="automatic" lang="python" >}}

This task takes two dataframes as input. We'll pass one raw Pandas dataframe, and one `flyte.io.DataFrame`.
Flyte automatically converts the `flyte.io.DataFrame` to a Pandas DataFrame (since we declared that as the input type) before passing it to the task.
The actual download and conversion happens only when we access the data, in this case, when we do the merge.

## Downloading DataFrames

When a task receives a `flyte.io.DataFrame`, you can request a concrete backend representation. For example, to download as a pandas DataFrame:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="download" lang="python" >}}

The `open()` call delegates to the DataFrame handler for the stored format and converts to the requested in-memory type.

## Run the example

Finally, we can define a `main` function to run the tasks defined above and a `__main__` block to execute the workflow:

{{< code file="/external/unionai-examples/v2/user-guide/task-programming/dataframes/dataframes.py" fragment="main" lang="python" >}}
