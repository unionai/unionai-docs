---
title: flytekit.core.pod_template
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.pod_template

## Directory

### Classes

| Class | Description |
|-|-|
| [`PodTemplate`](.././flytekit.core.pod_template#flytekitcorepod_templatepodtemplate) | Custom PodTemplate specification for a Task. |

### Methods

| Method | Description |
|-|-|
| [`serialize_pod_template()`](#serialize_pod_template) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `PRIMARY_CONTAINER_DEFAULT_NAME` | `str` |  |
| `TYPE_CHECKING` | `bool` |  |

## Methods

#### serialize_pod_template()

```python
def serialize_pod_template(
    obj,
)
```
| Parameter | Type | Description |
|-|-|-|
| `obj` |  | |

## flytekit.core.pod_template.PodTemplate

Custom PodTemplate specification for a Task.


```python
class PodTemplate(
    pod_spec: typing.Optional[ForwardRef('V1PodSpec')],
    primary_container_name: str,
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` | |
| `primary_container_name` | `str` | |
| `labels` | `typing.Optional[typing.Dict[str, str]]` | |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` | |

### Methods

| Method | Description |
|-|-|
| [`version_hash()`](#version_hash) |  |


#### version_hash()

```python
def version_hash()
```
