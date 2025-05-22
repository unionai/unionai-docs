---
title: flytekit.models.core.identifier
version: 0.1.dev2192+g7c539c3.d20250403
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
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> e: Identifier
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.identifier_pb2.Identifier


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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
| Parameter | Type |
|-|-|
| `node_id` |  |
| `execution_id` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> e: NodeExecutionIdentifier
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.identifier_pb2.NodeExecutionIdentifier


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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
| Parameter | Type |
|-|-|
| `signal_id` | `str` |
| `execution_id` | `flytekit.models.core.identifier.WorkflowExecutionIdentifier` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.identifier_pb2.SignalIdentifier,
) -> SignalIdentifier
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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
| Parameter | Type |
|-|-|
| `task_id` |  |
| `node_execution_id` |  |
| `retry_attempt` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto,
) -> e: TaskExecutionIdentifier
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.identifier_pb2.TaskExecutionIdentifier


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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
| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> e: WorkflowExecutionIdentifier
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.identifier_pb2.WorkflowExecutionIdentifier


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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

