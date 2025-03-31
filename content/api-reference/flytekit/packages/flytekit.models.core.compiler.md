---
title: flytekit.models.core.compiler
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> CompiledTask
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
| `is_empty` |  |  |
| `template` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> CompiledWorkflow
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
| `connections` |  |  |
| `is_empty` |  |  |
| `template` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> CompiledWorkflowClosure
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
| `is_empty` |  |  |
| `primary` |  |  |
| `sub_workflows` |  |  |
| `tasks` |  |  |

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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
) -> ConnectionSet
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
| `downstream` |  |  |
| `is_empty` |  |  |
| `upstream` |  |  |

