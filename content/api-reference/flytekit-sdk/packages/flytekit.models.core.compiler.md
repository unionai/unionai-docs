---
title: flytekit.models.core.compiler
version: 1.16.16
variants: +flyte +union
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

### Parameters

```python
class CompiledTask(
    template,
)
```
| Parameter | Type | Description |
|-|-|-|
| `template` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `template` | `None` |  |

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

**Returns:** CompiledTask

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
**Returns:** flyteidl.core.compiler_pb2.CompiledTask

## flytekit.models.core.compiler.CompiledWorkflow

### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `connections` | `None` |  |
| `is_empty` | `None` |  |
| `template` | `None` |  |

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

**Returns:** CompiledWorkflow

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
**Returns:** flyteidl.core.compiler_pb2.CompiledWorkflow

## flytekit.models.core.compiler.CompiledWorkflowClosure

### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `primary` | `None` |  |
| `sub_workflows` | `None` |  |
| `tasks` | `None` |  |

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

**Returns:** CompiledWorkflowClosure

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
**Returns:** flyteidl.core.compiler_pb2.CompiledWorkflowClosure

## flytekit.models.core.compiler.ConnectionSet

### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `downstream` | `None` |  |
| `is_empty` | `None` |  |
| `upstream` | `None` |  |

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

**Returns:** ConnectionSet

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
**Returns:** flyteidl.core.compiler_pb2.ConnectionSet

