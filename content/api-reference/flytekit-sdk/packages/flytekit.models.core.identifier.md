---
title: flytekit.models.core.identifier
version: 1.16.19
variants: +flyte +union
layout: py_api
---

# flytekit.models.core.identifier

## Directory

### Classes

| Class | Description |
|-|-|
| [`Identifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifieridentifier) |  |
| [`NodeExecutionIdentifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifiernodeexecutionidentifier) |  |
| [`ResourceType`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifierresourcetype) |  |
| [`SignalIdentifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifiersignalidentifier) |  |
| [`TaskExecutionIdentifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifiertaskexecutionidentifier) |  |
| [`WorkflowExecutionIdentifier`](.././flytekit.models.core.identifier#flytekitmodelscoreidentifierworkflowexecutionidentifier) |  |

## flytekit.models.core.identifier.Identifier

### Parameters

```python
class Identifier(
    resource_type,
    project,
    domain,
    name,
    version,
)
```
| Parameter | Type | Description |
|-|-|-|
| `resource_type` |  | |
| `project` |  | |
| `domain` |  | |
| `name` |  | |
| `version` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `domain` | `None` |  |
| `is_empty` | `None` |  |
| `name` | `None` |  |
| `project` | `None` |  |
| `resource_type` | `None` | enum value from ResourceType |
| `version` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

**Returns:** Identifier

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
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.identifier_pb2.Identifier

## flytekit.models.core.identifier.NodeExecutionIdentifier

### Parameters

```python
class NodeExecutionIdentifier(
    node_id,
    execution_id,
)
```
| Parameter | Type | Description |
|-|-|-|
| `node_id` |  | |
| `execution_id` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `execution_id` | `None` |  |
| `is_empty` | `None` |  |
| `node_id` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

**Returns:** NodeExecutionIdentifier

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.identifier_pb2.NodeExecutionIdentifier

## flytekit.models.core.identifier.ResourceType

## flytekit.models.core.identifier.SignalIdentifier

### Parameters

```python
class SignalIdentifier(
    signal_id: str,
    execution_id: flytekit.models.core.identifier.WorkflowExecutionIdentifier,
)
```
| Parameter | Type | Description |
|-|-|-|
| `signal_id` | `str` | User provided name for the gate node. |
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` | The workflow execution id this signal is for. |

### Properties

| Property | Type | Description |
|-|-|-|
| `execution_id` | `None` |  |
| `is_empty` | `None` |  |
| `signal_id` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.identifier_pb2.SignalIdentifier,
) -> SignalIdentifier
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.identifier_pb2.SignalIdentifier` | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.models.core.identifier.TaskExecutionIdentifier

### Parameters

```python
class TaskExecutionIdentifier(
    task_id,
    node_execution_id,
    retry_attempt,
)
```
| Parameter | Type | Description |
|-|-|-|
| `task_id` |  | |
| `node_execution_id` |  | |
| `retry_attempt` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `node_execution_id` | `None` |  |
| `retry_attempt` | `None` |  |
| `task_id` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

**Returns:** TaskExecutionIdentifier

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.identifier_pb2.TaskExecutionIdentifier

## flytekit.models.core.identifier.WorkflowExecutionIdentifier

### Parameters

```python
class WorkflowExecutionIdentifier(
    project,
    domain,
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `project` |  | |
| `domain` |  | |
| `name` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `domain` | `None` |  |
| `is_empty` | `None` |  |
| `name` | `None` |  |
| `project` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

**Returns:** WorkflowExecutionIdentifier

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.core.identifier_pb2.WorkflowExecutionIdentifier

