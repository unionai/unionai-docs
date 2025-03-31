---
title: flytekit.models.matchable_resource
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.matchable_resource

## Directory

### Classes

| Class | Description |
|-|-|
| [`ClusterResourceAttributes`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceclusterresourceattributes) | None. |
| [`ExecutionClusterLabel`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceexecutionclusterlabel) | None. |
| [`ExecutionQueueAttributes`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceexecutionqueueattributes) | None. |
| [`MatchableResource`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcematchableresource) | None. |
| [`MatchingAttributes`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcematchingattributes) | None. |
| [`PluginOverride`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcepluginoverride) | None. |
| [`PluginOverrides`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcepluginoverrides) | None. |

## flytekit.models.matchable_resource.ClusterResourceAttributes

```python
def ClusterResourceAttributes(
    attributes,
):
```
Custom resource attributes which will be applied in cluster resource creation (e.g. quotas).
Dict keys are the *case-sensitive* names of variables in templatized resource files.
Dict values should be the custom values which get substituted during resource creation.



| Parameter | Type |
|-|-|
| `attributes` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| attributes |  |  |
| is_empty |  |  |

## flytekit.models.matchable_resource.ExecutionClusterLabel

```python
def ExecutionClusterLabel(
    value,
):
```
Label value to determine where the execution will be run



| Parameter | Type |
|-|-|
| `value` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| is_empty |  |  |
| value |  |  |

## flytekit.models.matchable_resource.ExecutionQueueAttributes

```python
def ExecutionQueueAttributes(
    tags,
):
```
Tags used for assigning execution queues for tasks matching a project, domain and optionally, workflow.



| Parameter | Type |
|-|-|
| `tags` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| is_empty |  |  |
| tags |  |  |

## flytekit.models.matchable_resource.MatchableResource

### Methods

| Method | Description |
|-|-|
| [`enum_to_string()`](#enum_to_string) |  |
| [`string_to_enum()`](#string_to_enum) |  |


#### enum_to_string()

```python
def enum_to_string(
    val,
):
```
| Parameter | Type |
|-|-|
| `val` |  |

#### string_to_enum()

```python
def string_to_enum(
    val,
):
```
| Parameter | Type |
|-|-|
| `val` |  |

## flytekit.models.matchable_resource.MatchingAttributes

```python
def MatchingAttributes(
    cluster_resource_attributes,
    execution_queue_attributes,
    execution_cluster_label,
    plugin_overrides,
):
```
At most one target from cluster_resource_attributes, execution_queue_attributes or execution_cluster_label
can be set.


| Parameter | Type |
|-|-|
| `cluster_resource_attributes` |  |
| `execution_queue_attributes` |  |
| `execution_cluster_label` |  |
| `plugin_overrides` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| cluster_resource_attributes |  |  |
| execution_cluster_label |  |  |
| execution_queue_attributes |  |  |
| is_empty |  |  |
| plugin_overrides |  |  |

## flytekit.models.matchable_resource.PluginOverride

```python
def PluginOverride(
    task_type,
    plugin_id,
    missing_plugin_behavior,
):
```
Alternate plugin implementations requested for a specific task type.



| Parameter | Type |
|-|-|
| `task_type` |  |
| `plugin_id` |  |
| `missing_plugin_behavior` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`string_to_enum()`](#string_to_enum) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### string_to_enum()

```python
def string_to_enum(
    val,
):
```
| Parameter | Type |
|-|-|
| `val` |  |

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
| is_empty |  |  |
| missing_plugin_behavior |  |  |
| plugin_id |  |  |
| task_type |  |  |

## flytekit.models.matchable_resource.PluginOverrides

```python
def PluginOverrides(
    overrides,
):
```
Alternate plugin implementations for designated task types.



| Parameter | Type |
|-|-|
| `overrides` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
| is_empty |  |  |
| overrides |  |  |

