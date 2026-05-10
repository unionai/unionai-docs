---
title: Databricks
weight: 1
variants: +flyte +union
---

# Databricks

The Databricks plugin lets you run PySpark jobs on [Databricks](https://www.databricks.com/) clusters directly from Flyte tasks. You write normal PySpark code in a Flyte task, and the plugin submits it to Databricks via the [Jobs API 2.1](https://docs.databricks.com/api/workspace/jobs/submit). The connector handles job submission, polling, and cancellation.

The plugin supports:

- Running PySpark tasks on new or existing Databricks clusters
- Full Spark configuration (driver/executor memory, cores, instances)
- Databricks cluster auto-scaling
- API token-based authentication

## Installation

```bash
pip install flyteplugins-databricks
```

This also installs `flyteplugins-spark` as a dependency, since the Databricks plugin extends the Spark plugin.

## Quick start

Create a `Databricks` configuration and pass it as `plugin_config` to a `TaskEnvironment`:

```python
from flyteplugins.databricks import Databricks
import flyte

image = (
    flyte.Image.from_base("databricksruntime/standard:16.4-LTS")
    .clone(name="spark", registry="ghcr.io/flyteorg", extendable=True)
    .with_env_vars({"UV_PYTHON": "/databricks/python3/bin/python"})
    .with_pip_packages("flyteplugins-databricks", pre=True)
)

databricks_conf = Databricks(
    spark_conf={
        "spark.driver.memory": "2000M",
        "spark.executor.memory": "1000M",
        "spark.executor.cores": "1",
        "spark.executor.instances": "2",
        "spark.driver.cores": "1",
    },
    executor_path="/databricks/python3/bin/python",
    databricks_conf={
        "run_name": "flyte databricks plugin",
        "new_cluster": {
            "spark_version": "13.3.x-scala2.12",
            "node_type_id": "m6i.large",
            "autoscale": {"min_workers": 1, "max_workers": 2},
        },
        "timeout_seconds": 3600,
        "max_retries": 1,
    },
    databricks_instance="myaccount.cloud.databricks.com",
    databricks_token="DATABRICKS_TOKEN",
)

databricks_env = flyte.TaskEnvironment(
    name="databricks_env",
    resources=flyte.Resources(cpu=(1, 2), memory=("3000Mi", "5000Mi")),
    plugin_config=databricks_conf,
    image=image,
)
```

Then use the environment to decorate your task:

```python
@databricks_env.task
async def hello_databricks() -> float:
    spark = flyte.ctx().data["spark_session"]
    # Use spark as a normal SparkSession
    count = spark.sparkContext.parallelize(range(100)).count()
    return float(count)
```

## Configuration

The `Databricks` config extends the [Spark](../spark/_index) config with Databricks-specific fields.

### Spark fields (inherited)

| Parameter | Type | Description |
|-----------|------|-------------|
| `spark_conf` | `Dict[str, str]` | Spark configuration key-value pairs |
| `hadoop_conf` | `Dict[str, str]` | Hadoop configuration key-value pairs |
| `executor_path` | `str` | Path to the Python binary on the Databricks cluster (e.g., `/databricks/python3/bin/python`) |
| `applications_path` | `str` | Path to the main application file |

### Databricks-specific fields

| Parameter | Type | Description |
|-----------|------|-------------|
| `databricks_conf` | `Dict[str, Union[str, dict]]` | Databricks [run-submit](https://docs.databricks.com/api/workspace/jobs/submit) job configuration. Must contain either `existing_cluster_id` or `new_cluster` |
| `databricks_instance` | `str` | Your workspace domain (e.g., `myaccount.cloud.databricks.com`). Can also be set via the `FLYTE_DATABRICKS_INSTANCE` env var on the connector |
| `databricks_token` | `str` | Name of the Flyte secret containing the Databricks API token |

### `databricks_conf` structure

The `databricks_conf` dict maps to the Databricks run-submit API payload. Key fields:

| Field | Description |
|-------|-------------|
| `new_cluster` | Cluster spec with `spark_version`, `node_type_id`, `autoscale`, etc. |
| `existing_cluster_id` | ID of an existing cluster to use instead of creating a new one |
| `run_name` | Display name in the Databricks UI |
| `timeout_seconds` | Maximum job duration |
| `max_retries` | Number of retries before marking the job as failed |

The connector automatically injects the Docker image, Spark configuration, and environment variables from the task container into the cluster spec.

## Authentication

Store your Databricks API token as a Flyte secret. The `databricks_token` parameter specifies the secret name:

```python
databricks_conf = Databricks(
    # ...
    databricks_token="DATABRICKS_TOKEN",
)
```

## Accessing the Spark session

Inside a Databricks task, the `SparkSession` is available through the task context, just like the [Spark plugin](../spark/_index):

```python
@databricks_env.task
async def my_databricks_task() -> float:
    spark = flyte.ctx().data["spark_session"]
    df = spark.read.parquet("s3://my-bucket/data.parquet")
    return float(df.count())
```

## API reference

See the [Databricks API reference](../../api-reference/integrations/databricks/_index) for full details.
