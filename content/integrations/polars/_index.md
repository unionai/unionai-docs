---
title: Polars
description: Pass Polars DataFrame and LazyFrame values between tasks, serialized through Parquet.
icon: table
weight: 3
variants: +flyte +union
---

# Polars

The Polars plugin adds native support for [Polars](https://pola.rs/) `pl.DataFrame` (eager) and `pl.LazyFrame` (lazy) values as task inputs and outputs. Frames are serialized to and from [Parquet](https://parquet.apache.org/) automatically, so you can pass Polars data between tasks with no manual conversion. Just annotate your task signatures with the Polars types.

Installing the plugin registers encode/decode handlers with Flyte's `flyte.io.DataFrame` transformer engine. That also means a `pl.DataFrame` can be exchanged with the generic `flyte.io.DataFrame` type. A `pl.DataFrame` input can read a frame that a pandas task returned, but not one that a PySpark task returned. The Polars decoder reads only the single file `<uri>/00000`, and Spark writes `part-*` files instead.

## When to use this plugin

- High-performance dataframe processing with Polars' query engine
- Passing large tabular datasets between tasks efficiently via Parquet
- Deferred, optimized computation with `pl.LazyFrame`
- Interoperating with `flyte.io.DataFrame` or pandas tasks in the same workflow

## Installation

```bash
pip install flyteplugins-polars
```

Add the plugin to your task image. Installing it registers the Polars type handlers automatically; no explicit registration call is needed:

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
> When you fetch the outputs of a remote run, a returned `pl.LazyFrame` comes back as the generic `flyte.io.DataFrame` unless the run sets `preserve_original_types=True`. `flyte.run()` turns the setting on by default when you run from IPython or a notebook; `flyte.with_runcontext()` leaves it off unless you pass it. Local runs return the `pl.LazyFrame` either way:
>
> ```python
> run = flyte.with_runcontext(preserve_original_types=True).run(lazy_summary, lf=my_lazyframe)
> ```

## Interoperating with `flyte.io.DataFrame`

Because the Polars handlers register against the shared dataframe transformer engine, a task can accept the generic `flyte.io.DataFrame` and return a `pl.DataFrame`, or vice versa. This doesn't extend to `pl.LazyFrame`, which uses a different Parquet file name: a `pl.LazyFrame` input can't read a frame that a `pl.DataFrame` or pandas task returned, and a `pl.DataFrame` input can't read a returned `pl.LazyFrame`. Convert an in-memory Polars frame to a `flyte.io.DataFrame` with `flyte.io.DataFrame.wrap_df()` (preferred over deprecated `from_df()`):

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/polars/polars_example.py" fragment="interop" lang="python" >}}

## Common use cases

- **ETL and feature engineering**: filter, join, and aggregate large tables with Polars' fast query engine across task boundaries.
- **Deferred pipelines**: build up a `pl.LazyFrame` query plan and let Polars optimize it before materialization.
- **Mixed-backend workflows**: pass frames from pandas tasks into tasks that take a `pl.DataFrame`.

## API reference

See the [Polars API reference](../../api-reference/integrations/polars/_index) for the full list of encode/decode handlers.
