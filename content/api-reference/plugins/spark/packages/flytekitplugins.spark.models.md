---
title: flytekitplugins.spark.models
version: 1.16.19
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# flytekitplugins.spark.models

## Directory

### Classes

| Class | Description |
|-|-|
| [`SparkJob`](.././flytekitplugins.spark.models#flytekitpluginssparkmodelssparkjob) |  |
| [`SparkType`](.././flytekitplugins.spark.models#flytekitpluginssparkmodelssparktype) |  |

## flytekitplugins.spark.models.SparkJob

### Parameters

```python
class SparkJob(
    spark_type: <enum 'SparkType'>,
    application_file: str,
    main_class: str,
    spark_conf: typing.Dict[str, str],
    hadoop_conf: typing.Dict[str, str],
    executor_path: str,
    databricks_conf: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict]]],
    databricks_instance: typing.Optional[str],
    driver_pod: typing.Optional[flytekit.models.task.K8sPod],
    executor_pod: typing.Optional[flytekit.models.task.K8sPod],
)
```
This defines a SparkJob target.  It will execute the appropriate SparkJob.



| Parameter | Type | Description |
|-|-|-|
| `spark_type` | `<enum 'SparkType'>` | |
| `application_file` | `str` | The main application file to execute. |
| `main_class` | `str` | |
| `spark_conf` | `typing.Dict[str, str]` | |
| `hadoop_conf` | `typing.Dict[str, str]` | |
| `executor_path` | `str` | |
| `databricks_conf` | `typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict]]]` | |
| `databricks_instance` | `typing.Optional[str]` | |
| `driver_pod` | `typing.Optional[flytekit.models.task.K8sPod]` | |
| `executor_pod` | `typing.Optional[flytekit.models.task.K8sPod]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `application_file` | `None` | The main application file to execute |
| `databricks_conf` | `typing.Dict[str, typing.Dict]` | databricks_conf: Databricks job configuration. Config structure can be found here. https://docs.databricks.com/dev-tools/api/2.0/jobs.html#request-structure |
| `databricks_instance` | `str` | Domain name of your deployment. Use the form &lt;account&gt;.cloud.databricks.com. |
| `driver_pod` | `flytekit.models.task.K8sPod` | Additional pod specs for driver pod. |
| `executor_path` | `None` | The python executable to use |
| `executor_pod` | `flytekit.models.task.K8sPod` | Additional pod specs for the worker node pods. |
| `hadoop_conf` | `None` | A definition of key-value pairs for hadoop config for the job. |
| `is_empty` | `None` |  |
| `main_class` | `None` | The main class to execute |
| `spark_conf` | `None` | A definition of key-value pairs for spark config for the job. |
| `spark_type` | `None` | Spark Job Type |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`with_overrides()`](#with_overrides) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** SparkJob

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.plugins.spark_pb2.SparkJob

#### with_overrides()

```python
def with_overrides(
    new_spark_conf: typing.Optional[typing.Dict[str, str]],
    new_hadoop_conf: typing.Optional[typing.Dict[str, str]],
    new_databricks_conf: typing.Optional[typing.Dict[str, typing.Dict]],
) -> SparkJob
```
| Parameter | Type | Description |
|-|-|-|
| `new_spark_conf` | `typing.Optional[typing.Dict[str, str]]` | |
| `new_hadoop_conf` | `typing.Optional[typing.Dict[str, str]]` | |
| `new_databricks_conf` | `typing.Optional[typing.Dict[str, typing.Dict]]` | |

## flytekitplugins.spark.models.SparkType

