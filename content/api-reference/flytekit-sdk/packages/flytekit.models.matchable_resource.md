---
title: flytekit.models.matchable_resource
version: 1.16.10
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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.admin.matchable_resource_pb2.ClusterResourceAttributes


### Properties

| Property | Type | Description |
|-|-|-|
| `attributes` |  | {{< multiline >}}Custom resource attributes which will be applied in cluster resource management
:rtype: dict[Text, Text]
{{< /multiline >}} |
| `is_empty` |  |  |

## flytekit.models.matchable_resource.ExecutionClusterLabel

```python
class ExecutionClusterLabel(
    value,
)
```
Label value to determine where the execution will be run



| Parameter | Type | Description |
|-|-|-|
| `value` |  | |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.admin.matchable_resource_pb2.ExecutionClusterLabel


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `value` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.matchable_resource.ExecutionQueueAttributes

```python
class ExecutionQueueAttributes(
    tags,
)
```
Tags used for assigning execution queues for tasks matching a project, domain and optionally, workflow.



| Parameter | Type | Description |
|-|-|-|
| `tags` |  | |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.admin.matchable_resource_pb2.ExecutionQueueAttributes


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `tags` |  | {{< multiline >}}:rtype: list[Text]
{{< /multiline >}} |

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

#### string_to_enum()

```python
def string_to_enum(
    val,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

## flytekit.models.matchable_resource.MatchingAttributes

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.admin.matchable_resource_pb2.MatchingAttributes


### Properties

| Property | Type | Description |
|-|-|-|
| `cluster_resource_attributes` |  | {{< multiline >}}Custom resource attributes which will be applied in cluster resource creation (e.g. quotas).
:rtype: ClusterResourceAttributes
{{< /multiline >}} |
| `execution_cluster_label` |  | {{< multiline >}}Label value to determine where the execution will be run.
:rtype: ExecutionClusterLabel
{{< /multiline >}} |
| `execution_queue_attributes` |  | {{< multiline >}}Tags used for assigning execution queues for tasks.
:rtype: ExecutionQueueAttributes
{{< /multiline >}} |
| `is_empty` |  |  |
| `plugin_overrides` |  | {{< multiline >}}Plugin implementation overrides for specific task types.
:rtype: PluginOverrides
{{< /multiline >}} |

## flytekit.models.matchable_resource.PluginOverride

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

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`string_to_enum()`](#string_to_enum) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### string_to_enum()

```python
def string_to_enum(
    val,
)
```
| Parameter | Type | Description |
|-|-|-|
| `val` |  | |

#### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.matchable_resource_pb2.PluginOverride


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `missing_plugin_behavior` |  | {{< multiline >}}:rtype: int
{{< /multiline >}} |
| `plugin_id` |  | {{< multiline >}}:rtype: list[Text]
{{< /multiline >}} |
| `task_type` |  | {{< multiline >}}:rtype: Text
{{< /multiline >}} |

## flytekit.models.matchable_resource.PluginOverrides

```python
class PluginOverrides(
    overrides,
)
```
Alternate plugin implementations for designated task types.



| Parameter | Type | Description |
|-|-|-|
| `overrides` |  | |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.admin.matchable_resource_pb2.PluginOverrides


### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` |  |  |
| `overrides` |  | {{< multiline >}}:rtype: list[PluginOverride]
{{< /multiline >}} |

