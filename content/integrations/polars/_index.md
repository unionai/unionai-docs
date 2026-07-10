---
title: Polars
weight: 1
variants: +flyte +union
---

# Polars

The Polars plugin adds native support for [Polars](https://pola.rs/) `pl.DataFrame` (eager) and `pl.LazyFrame` (lazy) values as task inputs and outputs. Frames are serialized to and from [Parquet](https://parquet.apache.org/) automatically, so you can pass Polars data between tasks with no manual conversion — just annotate your task signatures with the Polars types.

Installing the plugin registers encode/decode handlers with Flyte's `flyte.io.DataFrame` transformer engine. That also means a `pl.DataFrame` can be exchanged with the generic `flyte.io.DataFrame` type and with other dataframe backends (pandas, PySpark) through the same Parquet interchange.

## When to use this plugin

- High-performance dataframe processing with Polars' query engine
- Passing large tabular datasets between tasks efficiently via Parquet
- Deferred, optimized computation with `pl.LazyFrame`
- Interoperating with `flyte.io.DataFrame` or other dataframe libraries in the same workflow

## Installation

```bash
pip install flyteplugins-polars
```

Add the plugin to your task image. Installing it registers the Polars type handlers automatically — no explicit registration call is needed:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/polars/polars_example.py" fragment="setup" lang="python" >}}

## Using Polars DataFrames

Annotate task inputs and outputs with `pl.DataFrame`. The plugin encodes returned frames to Parquet and decodes them back on the receiving task:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/polars/polars_example.py" fragment="dataframe" lang="python" >}}

Run it with:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/polars/polars_example.py" fragment="run" lang="python" >}}

## Using LazyFrames

`pl.LazyFrame` is supported the same way and lets Polars defer and optimize the query until the frame is materialized:

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/polars/polars_example.py" fragment="lazyframe" lang="python" >}}

> [!NOTE]
> When a task returns a `pl.LazyFrame` and you want the caller to receive it as a `pl.LazyFrame` (rather than an eagerly collected frame), run with `preserve_original_types=True`:
>
> ```python
> run = flyte.with_runcontext(preserve_original_types=True).run(lazy_summary, lf=my_lazyframe)
> ```

## Interoperating with `flyte.io.DataFrame`

Because the Polars handlers register against the shared dataframe transformer engine, a task can accept the generic `flyte.io.DataFrame` and return a Polars frame, or vice versa. Convert an in-memory Polars frame to a `flyte.io.DataFrame` with `flyte.io.DataFrame.wrap_df()` (preferred over deprecated `from_df()`):

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/polars/polars_example.py" fragment="interop" lang="python" >}}

This makes it straightforward to mix Polars with pandas or PySpark tasks in the same workflow — each side declares the dataframe type it wants, and Flyte handles the Parquet interchange.

## Common use cases

- **ETL and feature engineering** — filter, join, and aggregate large tables with Polars' fast query engine across task boundaries.
- **Deferred pipelines** — build up a `pl.LazyFrame` query plan and let Polars optimize it before materialization.
- **Mixed-backend workflows** — bridge Polars and pandas/PySpark tasks through `flyte.io.DataFrame`.

## API reference

See the [Polars API reference](../../api-reference/integrations/polars/_index) for the full list of encode/decode handlers.
