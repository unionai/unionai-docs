---
title: flytekit.models.core.catalog
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.core.catalog

## Directory

### Classes

| Class | Description |
|-|-|
| [`CatalogArtifactTag`](.././flytekit.models.core.catalog#flytekitmodelscorecatalogcatalogartifacttag) |  |
| [`CatalogMetadata`](.././flytekit.models.core.catalog#flytekitmodelscorecatalogcatalogmetadata) |  |

## flytekit.models.core.catalog.CatalogArtifactTag

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

### Properties

| Property | Type | Description |
|-|-|-|
| `artifact_id` | `None` |  |
| `is_empty` | `None` |  |
| `name` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.core.catalog_pb2.CatalogArtifactTag,
) -> CatalogArtifactTag
```
| Parameter | Type | Description |
|-|-|-|
| `p` | `flyteidl.core.catalog_pb2.CatalogArtifactTag` | |

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
## flytekit.models.core.catalog.CatalogMetadata

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

### Properties

| Property | Type | Description |
|-|-|-|
| `artifact_tag` | `None` |  |
| `dataset_id` | `None` |  |
| `is_empty` | `None` |  |
| `source_execution` | `None` | This is a one of but for now there's only one thing in the one of |
| `source_task_execution` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb: flyteidl.core.catalog_pb2.CatalogMetadata,
) -> CatalogMetadata
```
| Parameter | Type | Description |
|-|-|-|
| `pb` | `flyteidl.core.catalog_pb2.CatalogMetadata` | |

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
