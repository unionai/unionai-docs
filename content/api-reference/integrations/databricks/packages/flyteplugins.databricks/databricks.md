---
title: Databricks
version: 2.0.12.dev22+g879ad6de4
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# Databricks

**Package:** `flyteplugins.databricks`

Configuration for a Databricks task.

Tasks configured with this will execute natively on Databricks as a
distributed PySpark job. Extends `Spark` with Databricks-specific
cluster and authentication settings.



## Parameters

```python
class Databricks(
    spark_conf: typing.Optional[typing.Dict[str, str]],
    hadoop_conf: typing.Optional[typing.Dict[str, str]],
    executor_path: typing.Optional[str],
    applications_path: typing.Optional[str],
    driver_pod: typing.Optional[flyte._pod.PodTemplate],
    executor_pod: typing.Optional[flyte._pod.PodTemplate],
    databricks_conf: typing.Optional[typing.Dict[str, typing.Union[str, dict]]],
    databricks_instance: typing.Optional[str],
    databricks_token: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `spark_conf` | `typing.Optional[typing.Dict[str, str]]` | Spark configuration key-value pairs, e.g. `{"spark.executor.memory": "4g"}`. |
| `hadoop_conf` | `typing.Optional[typing.Dict[str, str]]` | Hadoop configuration key-value pairs. |
| `executor_path` | `typing.Optional[str]` | Path to the Python binary used for PySpark execution. Defaults to the interpreter path from the serialization context. |
| `applications_path` | `typing.Optional[str]` | Path to the main application file. Defaults to the task entrypoint path. |
| `driver_pod` | `typing.Optional[flyte._pod.PodTemplate]` | Pod template applied to the Spark driver pod. |
| `executor_pod` | `typing.Optional[flyte._pod.PodTemplate]` | Pod template applied to the Spark executor pods. |
| `databricks_conf` | `typing.Optional[typing.Dict[str, typing.Union[str, dict]]]` | Databricks job configuration dict compliant with the Databricks Jobs API v2.1 (also supports v2.0 use cases). Typically includes `new_cluster` or `existing_cluster_id`, `run_name`, and other job settings. |
| `databricks_instance` | `typing.Optional[str]` | Domain name of your Databricks deployment, e.g. `"myorg.cloud.databricks.com"`. |
| `databricks_token` | `typing.Optional[str]` | Name of the Flyte secret containing the Databricks API token used for authentication. |

