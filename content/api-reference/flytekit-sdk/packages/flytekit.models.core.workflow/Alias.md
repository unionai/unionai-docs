---
title: Alias
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Alias

**Package:** `flytekit.models.core.workflow`

```python
class Alias(
    var,
    alias,
)
```
Links a variable to an alias.



| Parameter | Type | Description |
|-|-|-|
| `var` |  | |
| `alias` |  | |

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
:rtype: flyteidl.core.workflow_pb2.Alias


## Properties

| Property | Type | Description |
|-|-|-|
| `alias` |  | {{< multiline >}}A workflow-level unique alias that downstream nodes can refer to in their input.

:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `var` |  | {{< multiline >}}Must match one of the output variable names on a node.

:rtype: Text
{{< /multiline >}} |

