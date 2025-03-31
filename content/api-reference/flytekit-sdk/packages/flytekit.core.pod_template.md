---
title: flytekit.core.pod_template
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.pod_template

## Directory

### Classes

| Class | Description |
|-|-|
| [`PodTemplate`](.././flytekit.core.pod_template#flytekitcorepod_templatepodtemplate) | Custom PodTemplate specification for a Task. |

## flytekit.core.pod_template.PodTemplate

Custom PodTemplate specification for a Task.


```python
def PodTemplate(
    pod_spec: typing.Optional[ForwardRef('V1PodSpec')],
    primary_container_name: str,
    labels: typing.Optional[typing.Dict[str, str]],
    annotations: typing.Optional[typing.Dict[str, str]],
):
```
| Parameter | Type |
|-|-|
| `pod_spec` | `typing.Optional[ForwardRef('V1PodSpec')]` |
| `primary_container_name` | `str` |
| `labels` | `typing.Optional[typing.Dict[str, str]]` |
| `annotations` | `typing.Optional[typing.Dict[str, str]]` |

