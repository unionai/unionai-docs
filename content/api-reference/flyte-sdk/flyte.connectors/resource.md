---
title: Resource
version: 2.5.19
variants: +flyte +union
layout: py_api
---

# Resource

**Package:** `flyte.connectors`

This is the output resource of the job.



## Parameters

```python
class Resource(
    phase: google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper,
    message: typing.Optional[str] = None,
    log_links: typing.Optional[typing.List[flyteidl2.core.execution_pb2.TaskLog]] = None,
    outputs: typing.Optional[typing.Dict[str, typing.Any]] = None,
    custom_info: typing.Optional[typing.Dict[str, typing.Any]] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `phase` | `google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper` | The phase of the job. |
| `message` | `typing.Optional[str]` | The return message from the job. |
| `log_links` | `typing.Optional[typing.List[flyteidl2.core.execution_pb2.TaskLog]]` | The log links of the job. For example, the link to the BigQuery Console. |
| `outputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | The outputs of the job. If return python native types, the agent will convert them to flyte literals. |
| `custom_info` | `typing.Optional[typing.Dict[str, typing.Any]]` | The custom info of the job. For example, the job config. |

