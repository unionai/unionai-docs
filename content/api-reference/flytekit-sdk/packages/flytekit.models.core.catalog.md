---
title: flytekit.models.core.catalog
version: 0.1.dev2192+g7c539c3.d20250403
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
| Parameter | Type |
|-|-|
| `artifact_id` | `str` |
| `name` | `str` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    p: flyteidl.core.catalog_pb2.CatalogArtifactTag,
) -> CatalogArtifactTag
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `artifact_id` |  |  |
| `is_empty` |  |  |
| `name` |  |  |

## flytekit.models.core.catalog.CatalogMetadata

```python
class CatalogMetadata(
    dataset_id: flytekit.models.core.identifier.Identifier,
    artifact_tag: flytekit.models.core.catalog.CatalogArtifactTag,
    source_task_execution: flytekit.models.core.identifier.TaskExecutionIdentifier,
)
```
| Parameter | Type |
|-|-|
| `dataset_id` | `flytekit.models.core.identifier.Identifier` |
| `artifact_tag` | `flytekit.models.core.catalog.CatalogArtifactTag` |
| `source_task_execution` | `flytekit.models.core.identifier.TaskExecutionIdentifier` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) | :rtype: Text. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb: flyteidl.core.catalog_pb2.CatalogMetadata,
) -> CatalogMetadata
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
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
:rtype: Text


### Properties

| Property | Type | Description |
|-|-|-|
| `artifact_tag` |  |  |
| `dataset_id` |  |  |
| `is_empty` |  |  |
| `source_execution` |  | {{< multiline >}}This is a one of but for now there's only one thing in the one of
{{< /multiline >}} |
| `source_task_execution` |  |  |

