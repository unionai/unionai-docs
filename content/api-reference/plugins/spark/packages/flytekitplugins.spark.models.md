---
title: flytekitplugins.spark.models
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.spark.models

## Directory

### Classes

| Class | Description |
|-|-|
| [`SparkJob`](.././flytekitplugins.spark.models#flytekitpluginssparkmodelssparkjob) |  |

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



| Parameter | Type |
|-|-|
| `spark_type` | `<enum 'SparkType'>` |
| `application_file` | `str` |
| `main_class` | `str` |
| `spark_conf` | `typing.Dict[str, str]` |
| `hadoop_conf` | `typing.Dict[str, str]` |
| `executor_path` | `str` |
| `databricks_conf` | `typing.Optional[typing.Dict[str, typing.Dict[str, typing.Dict]]]` |
| `databricks_instance` | `typing.Optional[str]` |
| `driver_pod` | `typing.Optional[flytekit.models.task.K8sPod]` |
| `executor_pod` | `typing.Optional[flytekit.models.task.K8sPod]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |
| [`with_overrides()`](#with_overrides) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: SparkJob
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


#### with_overrides()

```python
def with_overrides(
    new_spark_conf: typing.Optional[typing.Dict[str, str]],
    new_hadoop_conf: typing.Optional[typing.Dict[str, str]],
    new_databricks_conf: typing.Optional[typing.Dict[str, typing.Dict]],
) -> SparkJob
```
| Parameter | Type |
|-|-|
| `new_spark_conf` | `typing.Optional[typing.Dict[str, str]]` |
| `new_hadoop_conf` | `typing.Optional[typing.Dict[str, str]]` |
| `new_databricks_conf` | `typing.Optional[typing.Dict[str, typing.Dict]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `application_file` |  | {{< multiline >}}The main application file to execute
:rtype: Text
{{< /multiline >}} |
| `databricks_conf` |  | {{< multiline >}}databricks_conf: Databricks job configuration.
Config structure can be found here. https://docs.databricks.com/dev-tools/api/2.0/jobs.html#request-structure
:rtype: dict[Text, dict[Text, Text]]
{{< /multiline >}} |
| `databricks_instance` |  | {{< multiline >}}Domain name of your deployment. Use the form &lt;account&gt;.cloud.databricks.com.
:rtype: str
{{< /multiline >}} |
| `driver_pod` |  | {{< multiline >}}Additional pod specs for driver pod.
:rtype: K8sPod
{{< /multiline >}} |
| `executor_path` |  | {{< multiline >}}The python executable to use
:rtype: Text
{{< /multiline >}} |
| `executor_pod` |  | {{< multiline >}}Additional pod specs for the worker node pods.
:rtype: K8sPod
{{< /multiline >}} |
| `hadoop_conf` |  | {{< multiline >}}A definition of key-value pairs for hadoop config for the job.
rtype: dict[Text, Text]
{{< /multiline >}} |
| `is_empty` |  |  |
| `main_class` |  | {{< multiline >}}The main class to execute
:rtype: Text
{{< /multiline >}} |
| `spark_conf` |  | {{< multiline >}}A definition of key-value pairs for spark config for the job.
 :rtype: dict[Text, Text]
{{< /multiline >}} |
| `spark_type` |  | {{< multiline >}}Spark Job Type
:rtype: Text
{{< /multiline >}} |

