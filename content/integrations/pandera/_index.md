---
title: Pandera
weight: 1
variants: +flyte +union
sidebar_expanded: false
---

# Pandera

The [Pandera](https://pandera.readthedocs.io/en/latest/) plugin validates dataframes at task boundaries using
[`DataFrameModel`](https://pandera.readthedocs.io/en/latest/dataframe_models.html) schemas. When a task receives or
returns a pandera-typed dataframe, the plugin automatically validates the data, raises or warns on schema violations,
and writes an HTML validation report to the Flyte deck.

Pandera supports multiple dataframe backends. The `flyteplugins-pandera` plugin handles:

| Pandera typing module | DataFrame library | Additional plugin |
|-|-|-|
| `pandera.typing.pandas` | pandas | — |
| `pandera.typing.polars` | Polars (eager and lazy) | `flyteplugins-polars` |
| `pandera.typing.pyspark_sql` | PySpark SQL | `flyteplugins-spark` |

## When to use this plugin

- You want compile-time-style guarantees that data flowing between tasks conforms to a declared schema
- You need column-level type, constraint, and statistical checks on task inputs and outputs
- You want automatic validation reports visible in the Flyte UI

## Installation

Install the plugin with the pandera extras for your dataframe backend:

{{< tabs >}}
{{< tab "pandas" >}}

```bash
pip install flyteplugins-pandera 'pandera[pandas]'
```

{{< /tab >}}
{{< tab "Polars" >}}

```bash
pip install flyteplugins-pandera flyteplugins-polars 'pandera[polars]'
```

{{< /tab >}}
{{< tab "PySpark SQL" >}}

```bash
pip install flyteplugins-pandera flyteplugins-spark 'pandera[pyspark]'
```

{{< /tab >}}
{{< /tabs >}}

## Defining schemas

Schemas are defined as Python classes that inherit from pandera's `DataFrameModel`. Each field declares a column name,
type, and optional constraints:

```python
import pandera.pandas as pa

class EmployeeSchema(pa.DataFrameModel):
    employee_id: int = pa.Field(ge=0)
    name: str

class EmployeeSchemaWithStatus(EmployeeSchema):
    status: str = pa.Field(isin=["active", "inactive"])
```

Schemas compose through inheritance: `EmployeeSchemaWithStatus` includes all columns from `EmployeeSchema` plus the
`status` column.

For full details on schema definition—including custom checks, regex column matching, and `Config` options—see the
[pandera DataFrameModel documentation](https://pandera.readthedocs.io/en/latest/dataframe_models.html).

## Using schemas in tasks

Annotate task inputs and outputs with pandera's generic `DataFrame` type. The plugin validates data on every
encode (output) and decode (input):

```python
import pandera.typing.pandas as pt

@env.task(report=True)
async def build_employees() -> pt.DataFrame[EmployeeSchema]:
    return pd.DataFrame({
        "employee_id": [1, 2, 3],
        "name": ["Ada", "Grace", "Barbara"],
    })

@env.task(report=True)
async def add_status(
    df: pt.DataFrame[EmployeeSchema],
) -> pt.DataFrame[EmployeeSchemaWithStatus]:
    return df.assign(status="active")
```

Setting `report=True` on the task makes validation reports visible as deck tabs in the Flyte UI.

## Error handling with `ValidationConfig`

By default, a validation failure raises an exception and fails the task. To downgrade failures to warnings instead,
annotate the parameter with `ValidationConfig(on_error="warn")`:

```python
from typing import Annotated
from flyteplugins.pandera import ValidationConfig

@env.task(report=True)
async def lenient_pass_through(
    df: Annotated[pt.DataFrame[EmployeeSchema], ValidationConfig(on_error="warn")],
) -> Annotated[pt.DataFrame[EmployeeSchemaWithStatus], ValidationConfig(on_error="warn")]:
    ...
```

| `on_error` value | Behavior |
|-|-|
| `"raise"` (default) | Validation failure raises `pandera.errors.SchemaError` and the task fails |
| `"warn"` | Validation failure logs a warning and writes the report, but the task continues |

You can mix `"raise"` and `"warn"` across inputs and outputs of the same task. For example, use `"warn"` on inputs
to accept best-effort data while still enforcing strict output contracts.

## Image configuration

Include the plugin in your task image. The exact setup depends on your dataframe backend:

{{< tabs >}}
{{< tab "pandas" >}}

{{< markdown >}}

```python
import flyte

img = flyte.Image.from_debian_base(
    python_version=(3, 12),
).with_pip_packages("flyteplugins-pandera")

env = flyte.TaskEnvironment(
    "pandera_pandas",
    image=img,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)
```

{{< /markdown >}}

{{< /tab >}}
{{< tab "Polars" >}}

{{< markdown >}}

```python
import flyte

img = (
    flyte.Image.from_debian_base(python_version=(3, 12))
    .with_pip_packages("flyteplugins-polars", "pandera[polars]")
)

env = flyte.TaskEnvironment(
    "pandera_polars",
    image=img,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)
```

{{< /markdown >}}

{{< /tab >}}
{{< tab "PySpark SQL" >}}

{{< markdown >}}

```python
import flyte
from flyteplugins.spark.task import Spark

image = (
    flyte.Image.from_base("apache/spark-py:v3.4.0")
    .clone(name="pandera-pyspark-sql", python_version=(3, 10), extendable=True)
    .with_pip_packages("flyteplugins-spark", "pandera[pyspark]")
)

spark_conf = Spark(
    spark_conf={
        "spark.driver.memory": "1000M",
        "spark.executor.memory": "1000M",
        "spark.executor.cores": "1",
        "spark.executor.instances": "2",
        "spark.driver.cores": "1",
    },
)

env = flyte.TaskEnvironment(
    name="pandera_pyspark",
    plugin_config=spark_conf,
    image=image,
    resources=flyte.Resources(cpu="1", memory="2Gi"),
)
```

{{< /markdown >}}

{{< /tab >}}
{{< /tabs >}}

## Polars lazy frames

The Polars backend supports both `pt.DataFrame` (eager) and `pt.LazyFrame` (lazy). With lazy frames, pandera
validates the data when the frame is materialized at task I/O boundaries:

```python
import pandera.typing.polars as pt
import polars as pl

@env.task(report=True)
async def create_lazy() -> pt.LazyFrame[MetricsSchema]:
    return pl.LazyFrame({"item": ["x", "y"], "value": [3.0, 4.0]})

@env.task(report=True)
async def consume_lazy(
    lf: pt.LazyFrame[MetricsSchema],
) -> pt.DataFrame[MetricsSchema]:
    return lf.filter(pl.col("value") > 0.0).collect()
```

## Examples

{{< tabs >}}
{{< tab "pandas" >}}

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/pandera/pandas_schema.py" lang="python" >}}

{{< /tab >}}
{{< tab "Polars" >}}

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/pandera/polars_schema.py" lang="python" >}}

{{< /tab >}}
{{< tab "PySpark SQL" >}}

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/pandera/pyspark_sql_schema.py" lang="python" >}}

{{< /tab >}}
{{< /tabs >}}