---
title: NodeGroup
description: "One declared node group of a cluster: a pool of nodes and the shape each node has."
icon: braces
version: 0.20.2
variants: -flyte +union
layout: py_api
---

# NodeGroup

**Package:** `flyteplugins.union.remote`

One declared node group of a cluster: a pool of nodes and the shape each node has.


## Parameters

```python
class NodeGroup(
    pb2: NodeGroupPb2,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `NodeGroupPb2` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `accelerators` | `str` |  |
| `allocatable` | `dict[str, str]` | Allocatable resources of one node, keyed by lowercased resource name. |
| `architecture` | `str` |  |
| `capacity_types` | `list[str]` | What the group may launch nodes as (on-demand, spot, reserved). Empty means not established. |
| `instance_types` | `list[str]` |  |
| `labels` | `list[str]` |  |
| `limits` | `dict[str, str]` | Totals the group may not exceed across all its nodes (Karpenter NodePool spec.limits), Kubernetes resource name to quantity, sorted by name. Empty means none were declared. |
| `name` | `str` |  |
| `nodes` | `str` | min-max node count. A max of 0 means no node-count bound: the group is capped by `limits`, if anything. |
| `taints` | `list[str]` | Taints as `key=value:Effect`, the kubectl form. |
| `weight` | `int \| None` | Karpenter NodePool weight, or None when the group has none. |

## Methods

| Method | Description |
|-|-|
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.



**Returns:** dict: A dictionary representation of the object.

### to_json()

```python
def to_json()
```
Convert the object to a JSON string.



**Returns:** str: A JSON string representation of the object.

