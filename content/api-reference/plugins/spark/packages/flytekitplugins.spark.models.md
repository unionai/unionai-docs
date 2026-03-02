---
title: flytekitplugins.spark.models
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
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
| `application_file` | `None` | The main application file to execute :rtype: Text |
| `databricks_conf` | `None` | databricks_conf: Databricks job configuration. Config structure can be found here. https://docs.databricks.com/dev-tools/api/2.0/jobs.html#request-structure :rtype: dict[Text, dict[Text, Text]] |
| `databricks_instance` | `None` | Domain name of your deployment. Use the form &lt;account&gt;.cloud.databricks.com. :rtype: str |
| `driver_pod` | `None` | Additional pod specs for driver pod. :rtype: K8sPod |
| `executor_path` | `None` | The python executable to use :rtype: Text |
| `executor_pod` | `None` | Additional pod specs for the worker node pods. :rtype: K8sPod |
| `hadoop_conf` | `None` | A definition of key-value pairs for hadoop config for the job. rtype: dict[Text, Text] |
| `is_empty` | `None` |  |
| `main_class` | `None` | The main class to execute :rtype: Text |
| `spark_conf` | `None` | A definition of key-value pairs for spark config for the job.  :rtype: dict[Text, Text] |
| `spark_type` | `None` | Spark Job Type :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
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

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.plugins.spark_pb2.SparkJob


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

