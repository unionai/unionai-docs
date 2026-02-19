---
title: PodTemplate
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PodTemplate

**Package:** `flytekit.core.pod_template`

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

## Methods

| Method | Description |
|-|-|
| [`version_hash()`](#version_hash) |  |


### version_hash()

```python
def version_hash()
```
