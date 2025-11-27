---
title: StructuredDatasetType
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# StructuredDatasetType

**Package:** `flytekit.models.types`

```python
class StructuredDatasetType(
    columns: typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn],
    format: str,
    external_schema_type: str,
    external_schema_bytes: bytes,
)
```
| Parameter | Type | Description |
|-|-|-|
| `columns` | `typing.List[flytekit.models.types.StructuredDatasetType.DatasetColumn]` | |
| `format` | `str` | |
| `external_schema_type` | `str` | |
| `external_schema_bytes` | `bytes` | |

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
    proto: flyteidl.core.types_pb2.StructuredDatasetType,
) -> flyteidl.core.types_pb2.StructuredDatasetType
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.types_pb2.StructuredDatasetType` | |

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
| `columns` |  |  |
| `external_schema_bytes` |  |  |
| `external_schema_type` |  |  |
| `format` |  |  |
| `is_empty` |  |  |

