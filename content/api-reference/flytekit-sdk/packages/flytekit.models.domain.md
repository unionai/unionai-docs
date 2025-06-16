---
title: flytekit.models.domain
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.domain

## Directory

### Classes

| Class | Description |
|-|-|
| [`Domain`](.././flytekit.models.domain#flytekitmodelsdomaindomain) | Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments. |

## flytekit.models.domain.Domain

Domains are fixed and unique at the global level, and provide an abstraction to isolate resources and feature configuration for different deployment environments.



```python
class Domain(
    id,
    name,
)
```
| Parameter | Type |
|-|-|
| `id` |  |
| `name` |  |

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
    pb2_object,
) -> e: Domain
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
:rtype: flyteidl.admin.project_pb2.Domain


#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `id` |  | {{< multiline >}}A globally unique identifier associated with this domain.
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}A human-readable name for this domain.
:rtype: Text
{{< /multiline >}} |

