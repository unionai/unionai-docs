---
title: Resources
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Resources

**Package:** `flytekit.models.task`

```python
class Resources(
    requests,
    limits,
)
```
| Parameter | Type | Description |
|-|-|-|
| `requests` |  | |
| `limits` |  | |

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
:rtype: flyteidl.core.tasks_pb2.Resources


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `limits` |  | {{< multiline >}}These are the limits required.  These are guaranteed to be satisfied.
:rtype: list[Resources.ResourceEntry]
{{< /multiline >}} |
| `requests` |  | {{< multiline >}}The desired resources for execution.  This is given on a best effort basis.
:rtype: list[Resources.ResourceEntry]
{{< /multiline >}} |

