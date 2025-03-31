---
title: flytekit.models.named_entity
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
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
| Parameter | Type |
|-|-|
| `project` |  |
| `domain` |  |
| `name` |  |

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
) -> Identifier
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
| `domain` |  |  |
| `is_empty` |  |  |
| `name` |  |  |
| `project` |  |  |

## flytekit.models.named_entity.NamedEntityMetadata

```python
class NamedEntityMetadata(
    description,
    state,
)
```
| Parameter | Type |
|-|-|
| `description` |  |
| `state` |  |

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
) -> Identifier
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
| `description` |  |  |
| `is_empty` |  |  |
| `state` |  | {{< multiline >}}enum value from NamedEntityState
{{< /multiline >}} |

## flytekit.models.named_entity.NamedEntityState

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) | . |


#### enum_to_string()

```python
def enum_to_string(
    val,
) -> Text
```
| Parameter | Type |
|-|-|
| `val` |  |

