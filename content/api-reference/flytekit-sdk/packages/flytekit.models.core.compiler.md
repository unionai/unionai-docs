---
title: flytekit.models.core.compiler
version: 0.1.dev2192+g7c539c3.d20250403
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
| Parameter | Type |
|-|-|
| `template` |  |

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
) -> e: CompiledTask
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
:rtype: flyteidl.core.compiler_pb2.CompiledTask


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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
| Parameter | Type |
|-|-|
| `template` |  |
| `connections` |  |

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
) -> e: CompiledWorkflow
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
:rtype: flyteidl.core.compiler_pb2.CompiledWorkflow


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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
| Parameter | Type |
|-|-|
| `primary` |  |
| `sub_workflows` |  |
| `tasks` |  |

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
) -> e: CompiledWorkflowClosure
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
:rtype: flyteidl.core.compiler_pb2.CompiledWorkflowClosure


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


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
| Parameter | Type |
|-|-|
| `upstream` |  |
| `downstream` |  |

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
) -> e: ConnectionSet
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
:rtype: flyteidl.core.compiler_pb2.ConnectionSet


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `downstream` |  | {{< multiline >}}:rtype: dict[Text, ConnectionSet.IdList]
{{< /multiline >}} |
| `is_empty` |  |  |
| `upstream` |  | {{< multiline >}}:rtype: dict[Text, ConnectionSet.IdList]
{{< /multiline >}} |

