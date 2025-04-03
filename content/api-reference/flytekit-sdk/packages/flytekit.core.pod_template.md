---
title: flytekit.core.pod_template
version: 0.1.dev2184+g1e0cbe7.d20250401
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.pod_template

## Directory

### Classes

| Class | Description |
|-|-|
| [`PodTemplate`](.././flytekit.core.pod_template#flytekitcorepod_templatepodtemplate) | Custom PodTemplate specification for a Task. |

### Variables

| Property | Type | Description |
|-|-|-|
| `PRIMARY_CONTAINER_DEFAULT_NAME` | `str` |  |
| `TYPE_CHECKING` | `bool` |  |

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
| Parameter | Type |
|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` |
| `primary_container_name` | `str` |
| `labels` | `typing.Optional[typing.Dict[str, str]]` |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` |

