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
pip install --pre flyteplugins-polars
```

Add the plugin to your task image. Installing it registers the Polars type handlers automatically — no explicit registration call is needed:

```python
import flyte

image = flyte.Image.from_debian_base(name="polars").with_pip_packages("flyteplugins-polars")

env = flyte.TaskEnvironment(
    name="polars_env",
    image=image,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)
```

## Using Polars DataFrames

Annotate task inputs and outputs with `pl.DataFrame`. The plugin encodes returned frames to Parquet and decodes them back on the receiving task:

```python
import polars as pl


@env.task
def make_dataframe() -> pl.DataFrame:
    return pl.DataFrame(
        {
            "name": ["Alice", "Bob", "Charlie"],
            "category": ["A", "B", "A"],
            "salary": [55000.0, 75000.0, 72000.0],
            "active": [True, False, True],
        }
    )


@env.task
def summarize(df: pl.DataFrame) -> pl.DataFrame:
    return (
        df.filter(pl.col("active"))
        .group_by("category")
        .agg(pl.col("salary").mean().alias("avg_salary"), pl.len().alias("count"))
        .sort("category")
    )


@env.task
def main() -> pl.DataFrame:
    return summarize(make_dataframe())
```

Run it with:

```python
if __name__ == "__main__":
    flyte.init_from_config()
    run = flyte.run(main)
    print(run.url)
```

## Using LazyFrames

`pl.LazyFrame` is supported the same way and lets Polars defer and optimize the query until the frame is materialized:

```python
@env.task
def lazy_summary(lf: pl.LazyFrame) -> pl.LazyFrame:
    return (
        lf.filter(pl.col("active"))
        .group_by("category")
        .agg(pl.col("salary").mean().alias("avg_salary"))
        .sort("category")
    )
```

> [!NOTE]
> When a task returns a `pl.LazyFrame` and you want the caller to receive it as a `pl.LazyFrame` (rather than an eagerly collected frame), run with `preserve_original_types=True`:
>
> ```python
> run = flyte.with_runcontext(preserve_original_types=True).run(lazy_summary, lf=my_lazyframe)
> ```

## Interoperating with `flyte.io.DataFrame`

Because the Polars handlers register against the shared dataframe transformer engine, a task can accept the generic `flyte.io.DataFrame` and return a Polars frame, or vice versa. Convert an in-memory Polars frame to a `flyte.io.DataFrame` with `flyte.io.DataFrame.wrap_df()` (preferred over deprecated `from_df()`):

```python
import polars as pl
import flyte.io


@env.task
def to_flyte_df(df: pl.DataFrame) -> flyte.io.DataFrame:
    return flyte.io.DataFrame.wrap_df(df)


@env.task
def from_flyte_df(df: flyte.io.DataFrame) -> pl.DataFrame:
    return df  # decoded to a Polars DataFrame on input
```

This makes it straightforward to mix Polars with pandas or PySpark tasks in the same workflow — each side declares the dataframe type it wants, and Flyte handles the Parquet interchange.

## Common use cases

- **ETL and feature engineering** — filter, join, and aggregate large tables with Polars' fast query engine across task boundaries.
- **Deferred pipelines** — build up a `pl.LazyFrame` query plan and let Polars optimize it before materialization.
- **Mixed-backend workflows** — bridge Polars and pandas/PySpark tasks through `flyte.io.DataFrame`.

## API reference

See the [Polars API reference](../../api-reference/integrations/polars/_index) for the full list of encode/decode handlers.
