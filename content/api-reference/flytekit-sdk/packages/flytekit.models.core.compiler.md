---
title: flytekit.models.core.compiler
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.core.compiler

## Directory

### Classes

| Class | Description |
|-|-|
| [`CompiledTask`](.././flytekit.models.core.compiler#flytekitmodelscorecompilercompiledtask) |  |
| [`CompiledWorkflow`](.././flytekit.models.core.compiler#flytekitmodelscorecompilercompiledworkflow) |  |
| [`CompiledWorkflowClosure`](.././flytekit.models.core.compiler#flytekitmodelscorecompilercompiledworkflowclosure) |  |
| [`ConnectionSet`](.././flytekit.models.core.compiler#flytekitmodelscorecompilerconnectionset) |  |

## flytekit.models.core.compiler.CompiledTask

```python
class CompiledTask(
    template,
)
```
| Parameter | Type | Description |
|-|-|-|
| `template` |  | |

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
:rtype: flyteidl.core.compiler_pb2.CompiledTask


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `template` |  | {{< multiline >}}:rtype: TODO
{{< /multiline >}} |

## flytekit.models.core.compiler.CompiledWorkflow

```python
class CompiledWorkflow(
    template,
    connections,
)
```
| Parameter | Type | Description |
|-|-|-|
| `template` |  | |
| `connections` |  | |

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
:rtype: flyteidl.core.compiler_pb2.CompiledWorkflow


### Properties

| Property | Type | Description |
|-|-|-|
| `connections` |  | {{< multiline >}}:rtype: ConnectionSet
{{< /multiline >}} |
| `is_empty` |  |  |
| `template` |  | {{< multiline >}}:rtype: flytekit.models.core.workflow.WorkflowTemplate
{{< /multiline >}} |

## flytekit.models.core.compiler.CompiledWorkflowClosure

```python
class CompiledWorkflowClosure(
    primary,
    sub_workflows,
    tasks,
)
```
| Parameter | Type | Description |
|-|-|-|
| `primary` |  | |
| `sub_workflows` |  | |
| `tasks` |  | |

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
:rtype: flyteidl.core.compiler_pb2.CompiledWorkflowClosure


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `primary` |  | {{< multiline >}}:rtype: CompiledWorkflow
{{< /multiline >}} |
| `sub_workflows` |  | {{< multiline >}}:rtype: list[CompiledWorkflow]
{{< /multiline >}} |
| `tasks` |  | {{< multiline >}}:rtype: list[CompiledTask]
{{< /multiline >}} |

## flytekit.models.core.compiler.ConnectionSet

```python
class ConnectionSet(
    upstream,
    downstream,
)
```
| Parameter | Type | Description |
|-|-|-|
| `upstream` |  | |
| `downstream` |  | |

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
:rtype: flyteidl.core.compiler_pb2.ConnectionSet


### Properties

| Property | Type | Description |
|-|-|-|
| `downstream` |  | {{< multiline >}}:rtype: dict[Text, ConnectionSet.IdList]
{{< /multiline >}} |
| `is_empty` |  |  |
| `upstream` |  | {{< multiline >}}:rtype: dict[Text, ConnectionSet.IdList]
{{< /multiline >}} |

