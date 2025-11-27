---
title: MatchingAttributes
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# MatchingAttributes

**Package:** `flytekit.models.matchable_resource`

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
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.admin.matchable_resource_pb2.MatchingAttributes


## Properties

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

