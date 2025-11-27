---
title: flytekit.extend.backend.utils
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extend.backend.utils

## Directory

### Methods

| Method | Description |
|-|-|
| [`convert_to_flyte_phase()`](#convert_to_flyte_phase) | Convert the state from the connector to the phase in flyte. |
| [`get_agent_secret()`](#get_agent_secret) |  |
| [`get_connector_secret()`](#get_connector_secret) |  |
| [`is_terminal_phase()`](#is_terminal_phase) | Return true if the phase is terminal. |
| [`mirror_async_methods()`](#mirror_async_methods) |  |
| [`render_task_template()`](#render_task_template) |  |


## Methods

#### convert_to_flyte_phase()

```python
def convert_to_flyte_phase(
    state: str,
) -> <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1093a7750>
```
Convert the state from the connector to the phase in flyte.


| Parameter | Type | Description |
|-|-|-|
| `state` | `str` | |

#### get_agent_secret()

```python
def get_agent_secret(
    secret_key: str,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `secret_key` | `str` | |

#### get_connector_secret()

```python
def get_connector_secret(
    secret_key: str,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `secret_key` | `str` | |

#### is_terminal_phase()

```python
def is_terminal_phase(
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1093a7750>,
) -> bool
```
Return true if the phase is terminal.


| Parameter | Type | Description |
|-|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1093a7750>` | |

#### mirror_async_methods()

```python
def mirror_async_methods(
    func: typing.Callable,
    kwargs,
) -> typing.Coroutine
```
| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Callable` | |
| `kwargs` | `**kwargs` | |

#### render_task_template()

```python
def render_task_template(
    tt: flytekit.models.task.TaskTemplate,
    file_prefix: str,
) -> flytekit.models.task.TaskTemplate
```
| Parameter | Type | Description |
|-|-|-|
| `tt` | `flytekit.models.task.TaskTemplate` | |
| `file_prefix` | `str` | |

