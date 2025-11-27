---
title: NamedEntityIdentifier
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NamedEntityIdentifier

**Package:** `flytekit.models.common`

```python
class NamedEntityIdentifier(
    project,
    domain,
    name,
)
```
| Parameter | Type | Description |
|-|-|-|
| `project` |  | |
| `domain` |  | |
| `name` |  | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | Stores object to a Flyte-IDL defined protobuf. |


### from_flyte_idl()

```python
def from_flyte_idl(
    idl_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `idl_object` |  | |

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
Stores object to a Flyte-IDL defined protobuf.
:rtype: flyteidl.admin.common_pb2.NamedEntityIdentifier


## Properties

| Property | Type | Description |
|-|-|-|
| `domain` |  | {{< multiline >}}The name of the domain within the project.
:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}The name of the entity within the namespace of the project and domain.
:rtype: Text
{{< /multiline >}} |
| `project` |  | {{< multiline >}}The name of the project in which this entity lives.
:rtype: Text
{{< /multiline >}} |

