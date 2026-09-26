---
title: ClusterConfig
description: "The tracked ConfigMaps of a single cluster."
icon: braces
version: 0.14.0
variants: -flyte +union
layout: py_api
---

# ClusterConfig

**Package:** `flyteplugins.union.remote`

The tracked ConfigMaps of a single cluster.

The control plane serves the ConfigMap ``.data`` maps verbatim — any YAML
nested inside a value is left as a raw string for the caller to parse.


## Parameters

```python
class ClusterConfig(
    cluster_name: str,
    pb2: GetClusterConfigResponse,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cluster_name` | `str` | |
| `pb2` | `GetClusterConfigResponse` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `config_maps` | `dict[str, dict[str, str]]` | ConfigMap name -&gt; its ``.data`` key/value pairs. |
| `names` | `list[str]` | Sorted names of the ConfigMaps the cluster reported. |
| `omitted` | `dict[str, str]` | ConfigMap name -&gt; why the cluster did not return it.  A tracked ConfigMap the cluster could not collect is reported here rather than being silently absent, so "the component is not installed" is distinguishable from "the dataplane was not permitted to read it". |

## Methods

| Method | Description |
|-|-|
| [`data()`](#data) | The ``.data`` of a single ConfigMap. |
| [`get()`](#get) | Get the tracked ConfigMaps for a cluster. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |


### data()

```python
def data(
    config_map: str,
) -> dict[str, str]
```
The ``.data`` of a single ConfigMap.



| Parameter | Type | Description |
|-|-|-|
| `config_map` | `str` | |

**Raises**

| Exception | Description |
|-|-|
| `KeyError` | if the cluster did not report a ConfigMap with that name. When the cluster explained the omission, the reason is included. |

### get()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await ClusterConfig.get.aio()`.
```python
def get(
    cls,
    cluster_name: str,
) -> ClusterConfig
```
Get the tracked ConfigMaps for a cluster.

The read is routed to the named cluster's dataplane directly when the org
runs zero trust, and over the control-plane tunnel otherwise.



| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `cluster_name` | `str` | Name of the cluster to read config from. |

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

