---
title: Domain
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Domain

**Package:** `flytekit.models.domain`

Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments.



```python
class Domain(
    id,
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` |  | |
| `name` |  | |

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
:rtype: flyteidl.admin.project_pb2.Domain


## Properties

| Property | Type | Description |
|-|-|-|
| `id` |  | {{< multiline >}}A globally unique identifier associated with this domain.
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}A human-readable name for this domain.
:rtype: Text
{{< /multiline >}} |

