---
title: flytekit.models.matchable_resource
version: 1.16.15
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.models.matchable_resource

## Directory

### Classes

| Class | Description |
|-|-|
| [`ClusterResourceAttributes`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceclusterresourceattributes) |  |
| [`ExecutionClusterLabel`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceexecutionclusterlabel) |  |
| [`ExecutionQueueAttributes`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourceexecutionqueueattributes) |  |
| [`MatchableResource`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcematchableresource) |  |
| [`MatchingAttributes`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcematchingattributes) |  |
| [`PluginOverride`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcepluginoverride) |  |
| [`PluginOverrides`](.././flytekit.models.matchable_resource#flytekitmodelsmatchable_resourcepluginoverrides) |  |

## flytekit.models.matchable_resource.ClusterResourceAttributes

### Parameters

```python
class ClusterResourceAttributes(
    attributes,
)
```
Custom resource attributes which will be applied in cluster resource creation (e.g. quotas).
Dict keys are the *case-sensitive* names of variables in templatized resource files.
Dict values should be the custom values which get substituted during resource creation.



| Parameter | Type | Description |
|-|-|-|
| `attributes` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `attributes` | `None` | Custom resource attributes which will be applied in cluster resource management |
| `is_empty` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** ClusterResourceAttributes

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.matchable_resource_pb2.ClusterResourceAttributes

## flytekit.models.matchable_resource.ExecutionClusterLabel

### Parameters

```python
class ExecutionClusterLabel(
    value,
)
```
Label value to determine where the execution will be run



| Parameter | Type | Description |
|-|-|-|
| `value` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `value` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** ExecutionClusterLabel

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.matchable_resource_pb2.ExecutionClusterLabel

## flytekit.models.matchable_resource.ExecutionQueueAttributes

### Parameters

```python
class ExecutionQueueAttributes(
    tags,
)
```
Tags used for assigning execution queues for tasks matching a project, domain and optionally, workflow.



| Parameter | Type | Description |
|-|-|-|
| `tags` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `tags` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** ExecutionQueueAttributes

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.matchable_resource_pb2.ExecutionQueueAttributes

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
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

**Returns:** Text

#### string_to_enum()

```python
def string_to_enum(
    val,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

**Returns:** int

## flytekit.models.matchable_resource.MatchingAttributes

### Parameters

```python
class MatchingAttributes(
    cluster_resource_attributes,
    execution_queue_attributes,
    execution_cluster_label,
    plugin_overrides,
)
```
At most one target from cluster_resource_attributes, execution_queue_attributes or execution_cluster_label
    can be set.


| Parameter | Type | Description |
|-|-|-|
| `cluster_resource_attributes` |  | |
| `execution_queue_attributes` |  | |
| `execution_cluster_label` |  | |
| `plugin_overrides` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `cluster_resource_attributes` | `None` | Custom resource attributes which will be applied in cluster resource creation (e.g. quotas). |
| `execution_cluster_label` | `None` | Label value to determine where the execution will be run. |
| `execution_queue_attributes` | `None` | Tags used for assigning execution queues for tasks. |
| `is_empty` | `None` |  |
| `plugin_overrides` | `None` | Plugin implementation overrides for specific task types. |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** MatchingAttributes

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.matchable_resource_pb2.MatchingAttributes

## flytekit.models.matchable_resource.PluginOverride

### Parameters

```python
class PluginOverride(
    task_type,
    plugin_id,
    missing_plugin_behavior,
)
```
Alternate plugin implementations requested for a specific task type.



| Parameter | Type | Description |
|-|-|-|
| `task_type` |  | |
| `plugin_id` |  | |
| `missing_plugin_behavior` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `missing_plugin_behavior` | `None` |  |
| `plugin_id` | `None` |  |
| `task_type` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`string_to_enum()`](#string_to_enum) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** PluginOverride

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### string_to_enum()

```python
def string_to_enum(
    val,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

**Returns:** int

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.matchable_resource_pb2.PluginOverride

## flytekit.models.matchable_resource.PluginOverrides

### Parameters

```python
class PluginOverrides(
    overrides,
)
```
Alternate plugin implementations for designated task types.



| Parameter | Type | Description |
|-|-|-|
| `overrides` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `overrides` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

**Returns:** PluginOverrides

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
**Returns:** Text

#### to_flyte_idl()

```python
def to_flyte_idl()
```
**Returns:** flyteidl.admin.matchable_resource_pb2.PluginOverrides

