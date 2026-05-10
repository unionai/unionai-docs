---
title: Spark
weight: 1
variants: +flyte +union
---

# Spark

The Spark plugin lets you run [Apache Spark](https://spark.apache.org/) jobs natively on Kubernetes. Flyte manages the full cluster lifecycle: provisioning a transient Spark cluster for each task execution, running the job, and tearing the cluster down on completion.

Under the hood, the plugin uses the [Spark on Kubernetes Operator](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator) to create and manage Spark applications. No external Spark service or long-running cluster is required.

## When to use this plugin

- Large-scale data processing and ETL pipelines
- Jobs that benefit from Spark's distributed execution engine (Spark SQL, PySpark, Spark MLlib)
- Workloads that need Hadoop-compatible storage access (S3, GCS, HDFS)

## Installation

```bash
pip install flyteplugins-spark
```

## Configuration

Create a `Spark` configuration and pass it as `plugin_config` to a `TaskEnvironment`:

```python
from flyteplugins.spark import Spark

spark_config = Spark(
    spark_conf={
        "spark.driver.memory": "3000M",
        "spark.executor.memory": "1000M",
        "spark.executor.cores": "1",
        "spark.executor.instances": "2",
        "spark.driver.cores": "1",
    },
)

spark_env = flyte.TaskEnvironment(
    name="spark_env",
    plugin_config=spark_config,
    image=image,
)
```

### `Spark` parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `spark_conf` | `Dict[str, str]` | Spark configuration key-value pairs (e.g., executor memory, cores, instances) |
| `hadoop_conf` | `Dict[str, str]` | Hadoop configuration key-value pairs (e.g., S3/GCS access settings) |
| `executor_path` | `str` | Path to the Python binary for PySpark executors |
| `applications_path` | `str` | Path to the main Spark application file |
| `driver_pod` | `PodTemplate` | Pod template for the Spark driver pod |
| `executor_pod` | `PodTemplate` | Pod template for the Spark executor pods |

### Accessing the Spark session

Inside a Spark task, the `SparkSession` is available through the task context:

```python
from flyte._context import internal_ctx

@spark_env.task
async def my_spark_task() -> float:
    ctx = internal_ctx()
    spark = ctx.data.task_context.data["spark_session"]
    # Use spark as a normal SparkSession
    df = spark.read.parquet("s3://my-bucket/data.parquet")
    return df.count()
```

### Overriding configuration at runtime

You can override Spark configuration for individual task calls using `.override()`:

```python
from copy import deepcopy

updated_config = deepcopy(spark_config)
updated_config.spark_conf["spark.executor.instances"] = "4"

result = await my_spark_task.override(plugin_config=updated_config)()
```

## Example

{{< code file="/unionai-examples/v2/integrations/flyte-plugins/spark/spark_example.py" lang="python" >}}

## API reference

See the [Spark API reference](../../api-reference/integrations/spark/_index) for full details.
