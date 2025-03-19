---
title: flytekit.models.core.catalog
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.core.catalog

## Directory

### Classes

| Class | Description |
|-|-|
| [`CatalogArtifactTag`](.././flytekit.models.core.catalog#flytekitmodelscorecatalogcatalogartifacttag) | None. |
| [`CatalogMetadata`](.././flytekit.models.core.catalog#flytekitmodelscorecatalogcatalogmetadata) | None. |

## flytekit.models.core.catalog.CatalogArtifactTag

```python
def CatalogArtifactTag(
    artifact_id: str,
    name: str,
):
```
| Parameter | Type |
|-|-|
| `artifact_id` | `str` |
| `name` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.core.catalog_pb2.CatalogArtifactTag,
):
```
| Parameter | Type |
|-|-|
| `p` | `flyteidl.core.catalog_pb2.CatalogArtifactTag` |

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
| artifact_id |  |  |
| is_empty |  |  |
| name |  |  |

## flytekit.models.core.catalog.CatalogMetadata

```python
def CatalogMetadata(
    dataset_id: flytekit.models.core.identifier.Identifier,
    artifact_tag: flytekit.models.core.catalog.CatalogArtifactTag,
    source_task_execution: flytekit.models.core.identifier.TaskExecutionIdentifier,
):
```
| Parameter | Type |
|-|-|
| `dataset_id` | `flytekit.models.core.identifier.Identifier` |
| `artifact_tag` | `flytekit.models.core.catalog.CatalogArtifactTag` |
| `source_task_execution` | `flytekit.models.core.identifier.TaskExecutionIdentifier` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | None |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb: flyteidl.core.catalog_pb2.CatalogMetadata,
):
```
| Parameter | Type |
|-|-|
| `pb` | `flyteidl.core.catalog_pb2.CatalogMetadata` |

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
| artifact_tag |  |  |
| dataset_id |  |  |
| is_empty |  |  |
| source_execution |  |  |
| source_task_execution |  |  |

