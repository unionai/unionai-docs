---
title: Spark
version: 2.0.0b54
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Spark

**Package:** `flyteplugins.spark`

Use this to configure a SparkContext for a your task. Task's marked with this will automatically execute
natively onto K8s as a distributed execution of spark

Attributes:
    spark_conf (Optional[Dict[str, str]]): Spark configuration dictionary.
    hadoop_conf (Optional[Dict[str, str]]): Hadoop configuration dictionary.
    executor_path (Optional[str]): Path to the Python binary for PySpark execution.
    applications_path (Optional[str]): Path to the main application file.
    driver_pod (Optional[PodTemplate]): Pod template for the driver pod.
    executor_pod (Optional[PodTemplate]): Pod template for the executor pods.


```python
class Spark(
    spark_conf: typing.Optional[typing.Dict[str, str]],
    hadoop_conf: typing.Optional[typing.Dict[str, str]],
    executor_path: typing.Optional[str],
    applications_path: typing.Optional[str],
    driver_pod: typing.Optional[flyte._pod.PodTemplate],
    executor_pod: typing.Optional[flyte._pod.PodTemplate],
)
```
| Parameter | Type | Description |
|-|-|-|
| `spark_conf` | `typing.Optional[typing.Dict[str, str]]` | |
| `hadoop_conf` | `typing.Optional[typing.Dict[str, str]]` | |
| `executor_path` | `typing.Optional[str]` | |
| `applications_path` | `typing.Optional[str]` | |
| `driver_pod` | `typing.Optional[flyte._pod.PodTemplate]` | |
| `executor_pod` | `typing.Optional[flyte._pod.PodTemplate]` | |

