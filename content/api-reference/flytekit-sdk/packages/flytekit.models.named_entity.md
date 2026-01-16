---
title: flytekit.models.named_entity
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.common_pb2.NamedEntityIdentifier


### Properties

| Property | Type | Description |
|-|-|-|
| `domain` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `name` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `project` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.named_entity.NamedEntityMetadata

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

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
:rtype: flyteidl.admin.common_pb2.NamedEntityMetadata


### Properties

| Property | Type | Description |
|-|-|-|
| `description` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |
| `is_empty` |  |  |
| `state` |  | {{< multiline >}}enum value from NamedEntityState
:rtype: int
{{< /multiline >}} |

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

