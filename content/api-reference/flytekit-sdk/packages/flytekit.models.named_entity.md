---
title: flytekit.models.named_entity
version: 1.16.16
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# flytekit.models.named_entity

## Directory

### Classes

| Class | Description |
|-|-|
| [`NamedEntityIdentifier`](.././flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentityidentifier) |  |
| [`NamedEntityMetadata`](.././flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentitymetadata) |  |
| [`NamedEntityState`](.././flytekit.models.named_entity#flytekitmodelsnamed_entitynamedentitystate) |  |

## flytekit.models.named_entity.NamedEntityIdentifier

### Parameters

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

### Properties

| Property | Type | Description |
|-|-|-|
| `domain` | `None` |  |
| `is_empty` | `None` |  |
| `name` | `None` |  |
| `project` | `None` |  |

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

**Returns:** Identifier

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
**Returns:** flyteidl.admin.common_pb2.NamedEntityIdentifier

## flytekit.models.named_entity.NamedEntityMetadata

### Parameters

```python
class NamedEntityMetadata(
    description,
    state,
)
```
| Parameter | Type | Description |
|-|-|-|
| `description` |  | |
| `state` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `description` | `None` |  |
| `is_empty` | `None` |  |
| `state` | `None` | enum value from NamedEntityState |

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

**Returns:** Identifier

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
**Returns:** flyteidl.admin.common_pb2.NamedEntityMetadata

## flytekit.models.named_entity.NamedEntityState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |


#### enum_to_string()

```python
def enum_to_string(
    val,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

**Returns:** Text

