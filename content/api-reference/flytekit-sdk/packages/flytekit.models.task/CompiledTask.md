---
title: CompiledTask
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CompiledTask

**Package:** `flytekit.models.task`

```python
class CompiledTask(
    template,
)
```
| Parameter | Type | Description |
|-|-|-|
| `template` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.compiler_pb2.CompiledTask


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `template` |  | {{< multiline >}}:rtype: TaskTemplate
{{< /multiline >}} |

