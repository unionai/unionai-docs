---
title: Resource
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Resource

**Package:** `flyte.connectors`

This is the output resource of the job.

Attributes
----------
    phase : TaskExecution.Phase
        The phase of the job.
    message : Optional[str]
        The return message from the job.
    log_links : Optional[List[TaskLog]]
        The log links of the job. For example, the link to the BigQuery Console.
    outputs : Optional[Union[LiteralMap, typing.Dict[str, Any]]]
        The outputs of the job. If return python native types, the agent will convert them to flyte literals.
    custom_info : Optional[typing.Dict[str, Any]]
        The custom info of the job. For example, the job config.


```python
class Resource(
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10b576150>,
    message: typing.Optional[str],
    log_links: typing.Optional[typing.List[flyteidl2.core.execution_pb2.TaskLog]],
    outputs: typing.Optional[typing.Dict[str, typing.Any]],
    custom_info: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10b576150>` | |
| `message` | `typing.Optional[str]` | |
| `log_links` | `typing.Optional[typing.List[flyteidl2.core.execution_pb2.TaskLog]]` | |
| `outputs` | `typing.Optional[typing.Dict[str, typing.Any]]` | |
| `custom_info` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

