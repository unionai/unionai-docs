---
title: flytekit.interfaces.cli_identifiers
version: 0.1.dev2192+g7c539c3.d20250403
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
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`resource_type_name()`](#resource_type_name) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: Identifier
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    string,
) -> e: Identifier
```
Parses a string in the correct format into an identifier


| Parameter | Type |
|-|-|
| `string` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
) -> e: Identifier
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: TaskExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    string,
) -> e: TaskExecutionIdentifier
```
Parses a string in the correct format into an identifier


| Parameter | Type |
|-|-|
| `string` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
) -> e: TaskExecutionIdentifier
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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`from_python_std()`](#from_python_std) | Parses a string in the correct format into an identifier. |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> e: WorkflowExecutionIdentifier
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### from_python_std()

```python
def from_python_std(
    string,
) -> e: WorkflowExecutionIdentifier
```
Parses a string in the correct format into an identifier


| Parameter | Type |
|-|-|
| `string` |  |

#### promote_from_model()

```python
def promote_from_model(
    base_model,
) -> e: WorkflowExecutionIdentifier
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

