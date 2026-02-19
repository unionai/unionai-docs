---
title: Literal
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Literal

**Package:** `flytekit.models.literals`

```python
class Literal(
    scalar: typing.Optional[flytekit.models.literals.Scalar],
    collection: typing.Optional[flytekit.models.literals.LiteralCollection],
    map: typing.Optional[flytekit.models.literals.LiteralMap],
    hash: typing.Optional[str],
    metadata: typing.Optional[typing.Dict[str, str]],
    offloaded_metadata: typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata],
)
```
This IDL message represents a literal value in the Flyte ecosystem.



| Parameter | Type | Description |
|-|-|-|
| `scalar` | `typing.Optional[flytekit.models.literals.Scalar]` | |
| `collection` | `typing.Optional[flytekit.models.literals.LiteralCollection]` | |
| `map` | `typing.Optional[flytekit.models.literals.LiteralMap]` | |
| `hash` | `typing.Optional[str]` | |
| `metadata` | `typing.Optional[typing.Dict[str, str]]` | |
| `offloaded_metadata` | `typing.Optional[flytekit.models.literals.LiteralOffloadedMetadata]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `collection` | `None` | If not None, this value holds a collection of Literal values which can be further unpacked. :rtype: LiteralCollection |
| `hash` | `None` | If not None, this value holds a hash that represents the literal for caching purposes. :rtype: str |
| `is_empty` | `None` |  |
| `map` | `None` | If not None, this value holds a map of Literal values which can be further unpacked. :rtype: LiteralMap |
| `metadata` | `None` | This value holds metadata about the literal. |
| `offloaded_metadata` | `None` | This value holds metadata about the offloaded literal. |
| `scalar` | `None` | If not None, this value holds a scalar value which can be further unpacked. :rtype: Scalar |
| `value` | `None` | Returns one of the scalar, collection, or map properties based on which one is set. :rtype: T |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`set_metadata()`](#set_metadata) | Note: This is a mutation on the literal. |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object: flyteidl.core.literals_pb2.Literal,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` | `flyteidl.core.literals_pb2.Literal` | |

### serialize_to_string()

```python
def serialize_to_string()
```
### set_metadata()

```python
def set_metadata(
    metadata: typing.Dict[str, str],
)
```
Note: This is a mutation on the literal


| Parameter | Type | Description |
|-|-|-|
| `metadata` | `typing.Dict[str, str]` | |

### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.core.literals_pb2.Literal


