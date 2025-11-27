---
title: CatalogArtifactTag
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CatalogArtifactTag

**Package:** `flytekit.models.core.catalog`

```python
class CatalogArtifactTag(
    artifact_id: str,
    name: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `artifact_id` | `str` | |
| `name` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.core.catalog_pb2.CatalogArtifactTag,
) -> CatalogArtifactTag
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.core.catalog_pb2.CatalogArtifactTag` | |

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
## Properties

| Property | Type | Description |
|-|-|-|
| `artifact_id` |  |  |
| `is_empty` |  |  |
| `name` |  |  |

