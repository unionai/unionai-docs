---
title: flytekit.models.core.identifier
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.core.identifier

## Directory

### Classes

| Class | Description |
|-|-|
| [`Identifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifieridentifier) | None. |
| [`NodeExecutionIdentifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifiernodeexecutionidentifier) | None. |
| [`ResourceType`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifierresourcetype) | None. |
| [`SignalIdentifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifiersignalidentifier) | None. |
| [`TaskExecutionIdentifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifiertaskexecutionidentifier) | None. |
| [`WorkflowExecutionIdentifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifierworkflowexecutionidentifier) | None. |

## flytekit.models.core.identifier.Identifier

```python
def Identifier(
    resource_type,
    project,
    domain,
    name,
    version,
):
```
| Parameter | Type |
|-|-|
| `resource_type` |  |
| `project` |  |
| `domain` |  |
| `name` |  |
| `version` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`resource_type_name()`](#resource_type_name) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
```
| Parameter | Type |
|-|-|
| `p` |  |

#### resource_type_name()

```python
def resource_type_name()
```
#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| domain |  |  |
| is_empty |  |  |
| name |  |  |
| project |  |  |
| resource_type |  |  |
| version |  |  |

## flytekit.models.core.identifier.NodeExecutionIdentifier

```python
def NodeExecutionIdentifier(
    node_id,
    execution_id,
):
```
| Parameter | Type |
|-|-|
| `node_id` |  |
| `execution_id` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
```
| Parameter | Type |
|-|-|
| `p` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| execution_id |  |  |
| is_empty |  |  |
| node_id |  |  |

## flytekit.models.core.identifier.ResourceType

## flytekit.models.core.identifier.SignalIdentifier

```python
def SignalIdentifier(
    signal_id: str,
    execution_id: flytekit.models.core.identifier.WorkflowExecutionIdentifier,
):
```
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.identifier_pb2.SignalIdentifier,
):
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.identifier_pb2.SignalIdentifier` |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| execution_id |  |  |
| is_empty |  |  |
| signal_id |  |  |

## flytekit.models.core.identifier.TaskExecutionIdentifier

```python
def TaskExecutionIdentifier(
    task_id,
    node_execution_id,
    retry_attempt,
):
```
| Parameter | Type |
|-|-|
| `task_id` |  |
| `node_execution_id` |  |
| `retry_attempt` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
):
```
| Parameter | Type |
|-|-|
| `proto` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |
| node_execution_id |  |  |
| retry_attempt |  |  |
| task_id |  |  |

## flytekit.models.core.identifier.WorkflowExecutionIdentifier

```python
def WorkflowExecutionIdentifier(
    project,
    domain,
    name,
):
```
| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
```
| Parameter | Type |
|-|-|
| `p` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| domain |  |  |
| is_empty |  |  |
| name |  |  |
| project |  |  |

