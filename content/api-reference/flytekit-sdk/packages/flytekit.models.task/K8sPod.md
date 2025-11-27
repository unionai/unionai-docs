---
title: K8sPod
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# K8sPod

**Package:** `flytekit.models.task`

```python
class K8sPod(
    metadata: flytekit.models.task.K8sObjectMetadata,
    pod_spec: typing.Dict[str, typing.Any],
    data_config: typing.Optional[flytekit.models.task.DataLoadingConfig],
    primary_container_name: typing.Optional[str],
)
```
This defines a kubernetes pod target.  It will build the pod target during task execution


| Parameter | Type | Description |
|-|-|-|
| `metadata` | `flytekit.models.task.K8sObjectMetadata` | |
| `pod_spec` | `typing.Dict[str, typing.Any]` | |
| `data_config` | `typing.Optional[flytekit.models.task.DataLoadingConfig]` | |
| `primary_container_name` | `typing.Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_pod_template()`](#from_pod_template) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`to_pod_template()`](#to_pod_template) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.tasks_pb2.K8sPod,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.tasks_pb2.K8sPod` | |

### from_pod_template()

```python
def from_pod_template(
    pod_template: PodTemplate,
) -> K8sPod
```
| Parameter | Type | Description |
|-|-|-|
| `pod_template` | `PodTemplate` | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
### to_pod_template()

```python
def to_pod_template()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `data_config` |  |  |
| `is_empty` |  |  |
| `metadata` |  |  |
| `pod_spec` |  |  |
| `primary_container_name` |  |  |

