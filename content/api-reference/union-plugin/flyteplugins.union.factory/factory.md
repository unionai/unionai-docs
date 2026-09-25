---
title: Factory
description: "A set of builds."
icon: braces
version: 0.13.0
variants: -flyte +union
layout: py_api
---

# Factory

**Package:** `flyteplugins.union.factory`

A set of builds. You can materialize any artifact in it.

The graph is found by walking back from the artifacts the factory produces, through the
handles each build was given. Deploying it produces a task; running that task is a
materialization.



## Parameters

```python
class Factory(
    name: str,
    *produces: ArtifactHandle,
    description: str = '',
    project: Optional[str] = None,
    domain: Optional[str] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `*produces` | `ArtifactHandle` | |
| `description` | `str` | |
| `project` | `Optional[str]` | |
| `domain` | `Optional[str]` | |

## Methods

| Method | Description |
|-|-|
| [`deploy()`](#deploy) | Validate against the registry and the deployed tasks, compile to a task of type ``factory``, register it. |
| [`graph()`](#graph) | The definition as Mermaid. |
| [`graph_def()`](#graph_def) |  |
| [`materialize()`](#materialize) | Start a materialization run of this factory's task for ``target`` and return the ``flyte.remote.Run``. |
| [`validate()`](#validate) |  |


### deploy()

```python
def deploy(
    dryrun: bool = False,
    version: Optional[str] = None,
    image: Any = None,
    declare_sources: bool = True,
) -> Any
```
Validate against the registry and the deployed tasks, compile to a task of type ``factory``, register it.

``declare_sources`` locks the partition schema of every source and built artifact in the
registry, an empty one included, unless it is already declared. A version published later
with other keys is then stored as a mismatch and never read, instead of changing the schema.


| Parameter | Type | Description |
|-|-|-|
| `dryrun` | `bool` | |
| `version` | `Optional[str]` | |
| `image` | `Any` | |
| `declare_sources` | `bool` | |

### graph()

```python
def graph()
```
The definition as Mermaid. After a deploy this is the resolved graph, with the
dimensions and types the registry supplied for sources.


### graph_def()

```python
def graph_def()
```
### materialize()

```python
def materialize(
    target: Union[ArtifactHandle, str],
    params: Optional[Mapping[str, Mapping[str, Any]]] = None,
    rebuild: Optional[Sequence[Union[str, Any]]] = None,
    rebuild_all: bool = False,
    downstream: bool = False,
    plan_only: bool = False,
    concurrency: int = 0,
    queue: Optional[str] = None,
    versions: Optional[Mapping[str, str]] = None,
    **partitions: Any,
) -> Any
```
Start a materialization run of this factory's task for ``target`` and return the ``flyte.remote.Run``.

``queue`` runs the materialization and every build in it on that queue. ``versions`` pins
sources to artifact versions, e.g. ``versions={"tracks": "v2", "labels": "v1"}``; an
unpinned source reads its latest version.


| Parameter | Type | Description |
|-|-|-|
| `target` | `Union[ArtifactHandle, str]` | |
| `params` | `Optional[Mapping[str, Mapping[str, Any]]]` | |
| `rebuild` | `Optional[Sequence[Union[str, Any]]]` | |
| `rebuild_all` | `bool` | |
| `downstream` | `bool` | |
| `plan_only` | `bool` | |
| `concurrency` | `int` | |
| `queue` | `Optional[str]` | |
| `versions` | `Optional[Mapping[str, str]]` | |
| `**partitions` | `Any` | |

### validate()

```python
def validate()
```
