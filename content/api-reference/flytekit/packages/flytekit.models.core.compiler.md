---
title: flytekit.models.core.compiler
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.core.compiler

## Directory

### Classes

| Class | Description |
|-|-|
| [`CompiledTask`](.././flytekit.models.core.compiler#flytekitmodelscorecompilercompiledtask) | None. |
| [`CompiledWorkflow`](.././flytekit.models.core.compiler#flytekitmodelscorecompilercompiledworkflow) | None. |
| [`CompiledWorkflowClosure`](.././flytekit.models.core.compiler#flytekitmodelscorecompilercompiledworkflowclosure) | None. |
| [`ConnectionSet`](.././flytekit.models.core.compiler#flytekitmodelscorecompilerconnectionset) | None. |

## flytekit.models.core.compiler.CompiledTask

```python
def CompiledTask(
    template,
):
```
| Parameter | Type |
|-|-|
| `template` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
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
| is_empty |  |  |
| template |  |  |

## flytekit.models.core.compiler.CompiledWorkflow

```python
def CompiledWorkflow(
    template,
    connections,
):
```
| Parameter | Type |
|-|-|
| `template` |  |
| `connections` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
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
| connections |  |  |
| is_empty |  |  |
| template |  |  |

## flytekit.models.core.compiler.CompiledWorkflowClosure

```python
def CompiledWorkflowClosure(
    primary,
    sub_workflows,
    tasks,
):
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
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
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
| is_empty |  |  |
| primary |  |  |
| sub_workflows |  |  |
| tasks |  |  |

## flytekit.models.core.compiler.ConnectionSet

```python
def ConnectionSet(
    upstream,
    downstream,
):
```
| Parameter | Type |
|-|-|
| `upstream` |  |
| `downstream` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
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
| downstream |  |  |
| is_empty |  |  |
| upstream |  |  |

