---
title: CatalogMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# CatalogMetadata

**Package:** `flytekit.models.core.catalog`

```python
class CatalogMetadata(
    dataset_id: flytekit.models.core.identifier.Identifier,
    artifact_tag: flytekit.models.core.catalog.CatalogArtifactTag,
    source_task_execution: flytekit.models.core.identifier.TaskExecutionIdentifier,
)
```
| Parameter | Type | Description |
|-|-|-|
| `dataset_id` | `flytekit.models.core.identifier.Identifier` | |
| `artifact_tag` | `flytekit.models.core.catalog.CatalogArtifactTag` | |
| `source_task_execution` | `flytekit.models.core.identifier.TaskExecutionIdentifier` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `artifact_tag` | `None` |  |
| `dataset_id` | `None` |  |
| `is_empty` | `None` |  |
| `source_execution` | `None` | This is a one of but for now there's only one thing in the one of |
| `source_task_execution` | `None` |  |

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
    pb: flyteidl.core.catalog_pb2.CatalogMetadata,
) -> CatalogMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `pb` | `flyteidl.core.catalog_pb2.CatalogMetadata` | |

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
