---
title: EnvironmentVersion
description: "One environment version as returned by the list call: its summary and per-cluster summaries."
icon: braces
version: 0.14.0
variants: -flyte +union
layout: py_api
---

# EnvironmentVersion

**Package:** `flyteplugins.union.remote`

One environment version as returned by the list call: its summary and per-cluster summaries.

Versions are independent worker pools; one environment name can have several
retained versions, each listed separately.


## Parameters

```python
class EnvironmentVersion(
    pb2: EnvironmentVersionItem,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `EnvironmentVersionItem` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `action_count` | `int` |  |
| `cluster_summaries` | `list[EnvironmentClusterSummary]` |  |
| `gpu` | `str` |  |
| `id` | `EnvironmentId` |  |
| `image` | `str` |  |
| `last_updated` | `str` |  |
| `name` | `str` |  |
| `replicas` | `str` | ``min-max`` when the pool can scale, else the fixed replica count. |
| `resources` | `str` | Primary-container quantities as authored, e.g. ``cpu=2, memory=4Gi, gpu=1x A100``. |
| `state` | `str` |  |
| `version` | `str` |  |
| `worker_count` | `int` |  |

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

