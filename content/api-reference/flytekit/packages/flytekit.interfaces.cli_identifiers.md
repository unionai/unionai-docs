---
title: flytekit.interfaces.cli_identifiers
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) | . |
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Identifier
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    string,
) -> Identifier
```
Parses a string in the correct format into an identifier


| Parameter | Type |
|-|-|
| `string` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
) -> Identifier
```
| Parameter | Type |
|-|-|
| `base_model` |  |

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
| `domain` |  |  |
| `is_empty` |  |  |
| `name` |  |  |
| `project` |  |  |
| `resource_type` |  | {{< multiline >}}enum value from ResourceType
{{< /multiline >}} |
| `version` |  |  |

## flytekit.interfaces.cli_identifiers.TaskExecutionIdentifier

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> TaskExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    string,
) -> TaskExecutionIdentifier
```
Parses a string in the correct format into an identifier


| Parameter | Type |
|-|-|
| `string` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
) -> TaskExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `base_model` |  |

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
| `is_empty` |  |  |
| `node_execution_id` |  |  |
| `retry_attempt` |  |  |
| `task_id` |  |  |

## flytekit.interfaces.cli_identifiers.WorkflowExecutionIdentifier

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> WorkflowExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    string,
) -> WorkflowExecutionIdentifier
```
Parses a string in the correct format into an identifier


| Parameter | Type |
|-|-|
| `string` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
) -> WorkflowExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `base_model` |  |

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
| `domain` |  |  |
| `is_empty` |  |  |
| `name` |  |  |
| `project` |  |  |

