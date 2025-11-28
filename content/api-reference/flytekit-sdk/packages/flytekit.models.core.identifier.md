---
title: flytekit.models.core.identifier
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.identifier_pb2.Identifier


### Properties

| Property | Type | Description |
|-|-|-|
| `domain` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `project` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `resource_type` |  | {{< multiline >}}enum value from ResourceType
:rtype: int
{{< /multiline >}} |
| `version` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.core.identifier.NodeExecutionIdentifier

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.identifier_pb2.NodeExecutionIdentifier


### Properties

| Property | Type | Description |
|-|-|-|
| `execution_id` |  | {{< multiline >}}:rtype: WorkflowExecutionIdentifier
{{< /multiline >}} |
| `is_empty` |  |  |
| `node_id` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.core.identifier.ResourceType

## flytekit.models.core.identifier.SignalIdentifier

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `execution_id` |  |  |
| `is_empty` |  |  |
| `signal_id` |  |  |

## flytekit.models.core.identifier.TaskExecutionIdentifier

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.identifier_pb2.TaskExecutionIdentifier


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `node_execution_id` |  | {{< multiline >}}:rtype: NodeExecutionIdentifier
{{< /multiline >}} |
| `retry_attempt` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `task_id` |  | {{< multiline >}}:rtype: Identifier
{{< /multiline >}} |

## flytekit.models.core.identifier.WorkflowExecutionIdentifier

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.identifier_pb2.WorkflowExecutionIdentifier


### Properties

| Property | Type | Description |
|-|-|-|
| `domain` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `project` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

