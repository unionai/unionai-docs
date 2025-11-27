---
title: Blob
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Blob

**Package:** `flytekit.models.literals`

```python
class Blob(
    metadata,
    uri,
)
```
This literal model is used to represent binary data offloaded to some storage location which is
identifiable with a unique string. See {{< py_class_ref flytekit.FlyteFile >}} as an example.



| Parameter | Type | Description |
|-|-|-|
| `metadata` |  | |
| `uri` |  | |

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
    proto,
)
```
| Parameter | Type | Description |
|-|-|-|
| `proto` |  | |

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
:rtype: flyteidl.core.literals_pb2.Blob


## Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `metadata` |  | {{< multiline >}}:rtype: BlobMetadata
{{< /multiline >}} |
| `uri` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

