---
title: flytekit.interfaces.cli_identifiers
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interfaces.cli_identifiers

## Directory

### Classes

| Class | Description |
|-|-|
| [`Identifier`](.././flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifiersidentifier) |  |
| [`TaskExecutionIdentifier`](.././flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifierstaskexecutionidentifier) |  |
| [`WorkflowExecutionIdentifier`](.././flytekit.interfaces.cli_identifiers#flytekitinterfacescli_identifiersworkflowexecutionidentifier) |  |

## flytekit.interfaces.cli_identifiers.Identifier

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
| `domain` | `None` | :rtype: Text |
| `is_empty` | `None` |  |
| `name` | `None` | :rtype: Text |
| `project` | `None` | :rtype: Text |
| `resource_type` | `None` | enum value from ResourceType :rtype: int |
| `version` | `None` | :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### from_python_std()

```python
def from_python_std(
    string,
)
```
Parses a string in the correct format into an identifier


| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
)
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` |  | |

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


## flytekit.interfaces.cli_identifiers.TaskExecutionIdentifier

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
| `node_execution_id` | `None` | :rtype: NodeExecutionIdentifier |
| `retry_attempt` | `None` | :rtype: int |
| `task_id` | `None` | :rtype: Identifier |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### from_python_std()

```python
def from_python_std(
    string,
)
```
Parses a string in the correct format into an identifier


| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
)
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` |  | |

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


## flytekit.interfaces.cli_identifiers.WorkflowExecutionIdentifier

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
| `domain` | `None` | :rtype: Text |
| `is_empty` | `None` |  |
| `name` | `None` | :rtype: Text |
| `project` | `None` | :rtype: Text |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### from_python_std()

```python
def from_python_std(
    string,
)
```
Parses a string in the correct format into an identifier


| Parameter | Type | Description |
|-|-|-|
| `string` |  | |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
)
```
| Parameter | Type | Description |
|-|-|-|
| `base_model` |  | |

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


