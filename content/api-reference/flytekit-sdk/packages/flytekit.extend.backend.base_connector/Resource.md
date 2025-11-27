---
title: Resource
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Resource

**Package:** `flytekit.extend.backend.base_connector`

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
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1093a7750>,
    message: typing.Optional[str],
    log_links: typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]],
    outputs: typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType],
    custom_info: typing.Optional[typing.Dict[str, typing.Any]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1093a7750>` | |
| `message` | `typing.Optional[str]` | |
| `log_links` | `typing.Optional[typing.List[flyteidl.core.execution_pb2.TaskLog]]` | |
| `outputs` | `typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, typing.Any], NoneType]` | |
| `custom_info` | `typing.Optional[typing.Dict[str, typing.Any]]` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | This function is async to call the async type engine functions. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.admin.agent_pb2.Resource,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.admin.agent_pb2.Resource` | |

### to_flyte_idl()

```python
def to_flyte_idl()
```
This function is async to call the async type engine functions. This is okay to do because this is not a
normal model class that inherits from FlyteIdlEntity


