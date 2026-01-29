---
title: Databricks
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Databricks

**Package:** `flyteplugins.connectors.databricks.task`

Use this to configure a Databricks task. Task's marked with this will automatically execute
natively onto databricks platform as a distributed execution of spark



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
| `spark_conf` | `typing.Optional[typing.Dict[str, str]]` | |
| `hadoop_conf` | `typing.Optional[typing.Dict[str, str]]` | |
| `executor_path` | `typing.Optional[str]` | |
| `applications_path` | `typing.Optional[str]` | |
| `driver_pod` | `typing.Optional[flyte._pod.PodTemplate]` | |
| `executor_pod` | `typing.Optional[flyte._pod.PodTemplate]` | |
| `databricks_conf` | `typing.Optional[typing.Dict[str, typing.Union[str, dict]]]` | Databricks job configuration compliant with API version 2.1, supporting 2.0 use cases. |
| `databricks_instance` | `typing.Optional[str]` | Domain name of your deployment. Use the form &lt;account&gt;.cloud.databricks.com. |
| `databricks_token` | `typing.Optional[str]` | the name of the secret containing the Databricks token for authentication. |

