---
title: Node
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Node

**Package:** `flytekit.core.node`

This class will hold all the things necessary to make an SdkNode but we won't make one until we know things like
ID, which from the registration step



```python
class Node(
    id: str,
    metadata: _workflow_model.NodeMetadata,
    bindings: List[_literal_models.Binding],
    upstream_nodes: List[Node],
    flyte_entity: Any,
)
```
| Parameter | Type | Description |
|-|-|-|
| `id` | `str` | |
| `metadata` | `_workflow_model.NodeMetadata` | |
| `bindings` | `List[_literal_models.Binding]` | |
| `upstream_nodes` | `List[Node]` | |
| `flyte_entity` | `Any` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `bindings` | `None` |  |
| `flyte_entity` | `None` |  |
| `id` | `None` |  |
| `metadata` | `None` |  |
| `name` | `None` |  |
| `outputs` | `None` |  |
| `run_entity` | `None` |  |
| `upstream_nodes` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`runs_before()`](#runs_before) | This is typically something we shouldn't do. |
| [`with_overrides()`](#with_overrides) |  |


### runs_before()

```python
def runs_before(
    other: Node,
)
```
This is typically something we shouldn't do. This modifies an attribute of the other instance rather than
self. But it's done so only because we wanted this English function to be the same as the shift function.
That is, calling node_1.runs_before(node_2) and node_1 &gt;&gt; node_2 are the same. The shift operator going the
other direction is not implemented to further avoid confusion. Right shift was picked rather than left shift
because that's what most users are familiar with.


| Parameter | Type | Description |
|-|-|-|
| `other` | `Node` | |

### with_overrides()

```python
def with_overrides(
    node_name: Optional[str],
    aliases: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    timeout: Optional[Union[int, datetime.timedelta, object]],
    retries: Optional[int],
    interruptible: Optional[bool],
    name: Optional[str],
    task_config: Optional[Any],
    container_image: Optional[str],
    accelerator: Optional[BaseAccelerator],
    cache: Optional[Union[bool, Cache]],
    shared_memory: Optional[Union[L[True], str]],
    pod_template: Optional[PodTemplate],
    resources: Optional[Resources],
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `node_name` | `Optional[str]` | |
| `aliases` | `Optional[Dict[str, str]]` | |
| `requests` | `Optional[Resources]` | |
| `limits` | `Optional[Resources]` | |
| `timeout` | `Optional[Union[int, datetime.timedelta, object]]` | |
| `retries` | `Optional[int]` | |
| `interruptible` | `Optional[bool]` | |
| `name` | `Optional[str]` | |
| `task_config` | `Optional[Any]` | |
| `container_image` | `Optional[str]` | |
| `accelerator` | `Optional[BaseAccelerator]` | |
| `cache` | `Optional[Union[bool, Cache]]` | |
| `shared_memory` | `Optional[Union[L[True], str]]` | |
| `pod_template` | `Optional[PodTemplate]` | |
| `resources` | `Optional[Resources]` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

