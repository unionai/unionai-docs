---
title: PodTemplate
version: 2.0.0b34.dev10+g162555e05
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PodTemplate

**Package:** `flyte`

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
| [`to_k8s_pod()`](#to_k8s_pod) |  |


### to_k8s_pod()

```python
def to_k8s_pod()
```
