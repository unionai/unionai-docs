---
title: flyte.artifacts
description: "Artifacts module."
icon: box-seam
version: 2.10.2
variants: +flyte +union
layout: py_api
---

# flyte.artifacts

Artifacts module

This module provides a wrapper method to mark certain outputs as artifacts with associated metadata.
Artifacts are offloaded assets: a flyte.io File, Dir, or DataFrame.

Usage example:
```python
import flyte.artifacts as artifacts
from flyte.io import File

@env.task
async def my_task() -> File:
    file = await File.from_local("weights.pt")
    metadata = artifacts.Metadata(name="my_artifact", version="1.0", description="An example artifact")
    return artifacts.new(file, metadata)
```

Launching with known artifacts:
```python
flyte.run(main, x=flyte.remote.Artifact.get("name", version="1.0"))
```

Retrieve a set of artifacts and pass them as a list
```python
from flyte.remote import Artifact
flyte.run(main, x=[Artifact.get("name1", version="1.0"), Artifact.get("name2", version="2.0")])
```
OR, listing versions of one artifact. `listall` is an iterator, so materialize it
before binding it as an input — a run input must be an `Artifact` or a list of them.
```python
from flyte.remote import Artifact
flyte.run(main, x=list(Artifact.listall(name="name1", limit=5)))
```
Use `Artifact.list_names(search=...)` to browse distinct artifact names instead.

Publishing a model:
```python
metadata = artifacts.Metadata(name="sentiment-model", kind="model")
return artifacts.new(file, metadata)
```
`Metadata.create_model_metadata(...)` sets `kind="model"` for you, alongside the
model-specific attrs (framework, architecture, and so on).

Read it back with `flyte.remote.Artifact.kind`, which returns "model", "data", or
"generic" -- never None. It is stored under a reserved `flyte.io/kind` attr, but
callers should use the property rather than reading `user_metadata` directly, so the
key can move to a typed field later without breaking them.

`kind` is what an artifact *is*; a card's `card_type` is how its card *renders*. An
artifact can have one without the other.

Partitions are part of an artifact's identity. Give a version its partition values
in `Metadata.partitions`; a `date` is a daily time partition, a `datetime` an hourly
one, and anything else is a string partition:
```python
metadata = artifacts.Metadata(name="raw_events", partitions={"date": day, "region": region})
return artifacts.new(file, metadata)
```
Read a partition back with `Artifact.get("raw_events", date=day, region="us")`, list a
range with `Artifact.listall("raw_events", date=(start, end), latest_per_partition=True)`,
and list the values of one key with `Artifact.partition_values("raw_events", "region")`.

Producing artifacts from a task that does not wrap its outputs: the caller declares them.
```python
with artifacts.produces(o0=artifacts.Metadata(name="events", partitions={"date": day})):
    await clean.override(produces_artifacts=True)(raw=raw)
```
## Directory

### Classes

| Class | Description |
|-|-|
| [`ArtifactKey`](../flyte.artifacts/artifactkey) |  |
| [`ArtifactVersionId`](../flyte.artifacts/artifactversionid) |  |
| [`Card`](../flyte.artifacts/card) |  |
| [`Metadata`](../flyte.artifacts/metadata) | Structured metadata for Flyte artifacts. |
| [`TimePartition`](../flyte.artifacts/timepartition) | A time partition value with an explicit granularity. |

### Protocols

| Protocol | Description |
|-|-|
| [`Artifact`](../flyte.artifacts/artifact) | Anything that can declare itself an artifact. |

### Methods

| Method | Description |
|-|-|
| [`new()`](#new) | Wrap an object with Flyte metadata while preserving its type interface. |
| [`produces()`](#produces) | Declare that outputs of the task called inside this block are artifacts. |


### Variables

| Property | Type | Description |
|-|-|-|
| `KIND_KEY` | `str` |  |
| `MAX_PARENTS` | `int` |  |

## Methods

#### new()

```python
def new(
    obj: ~T,
    metadata: flyte.artifacts._metadata.Metadata,
) -> ~T
```
Wrap an object with Flyte metadata while preserving its type interface.

Only offloaded assets can be artifacts: flyte.io File, Dir, or DataFrame.
Anything else (primitives, bytes, dataclasses, pydantic models, arbitrary
objects) is rejected. Artifacts must be returned directly from a task
(top-level output); nesting a wrapped value inside another model is not
supported and fails at serialization time.



| Parameter | Type | Description |
|-|-|-|
| `obj` | `~T` | The object to wrap |
| `metadata` | `flyte.artifacts._metadata.Metadata` | Metadata to associate with the object |

**Returns**

A zero-copy wrapper that behaves exactly like the original object
but carries additional Flyte metadata accessible via get_artifact_metadata()

#### produces()

```python
def produces(
    **outputs: Metadata,
) -> Iterator[None]
```
Declare that outputs of the task called inside this block are artifacts.

The caller names the outputs, so a task that knows nothing about artifacts can still produce
them: its outputs are published by the platform exactly as if it had returned
`flyte.artifacts.new(...)`, with the action that ran it recorded as the source. Keyword names are
output slots, `o0` for the first output, `o1` for the second, and so on.

```python
with flyte.artifacts.produces(o0=Metadata(name="events", partitions={"date": day})):
    await clean.override(produces_artifacts=True)(raw=raw)
```

The called task must run with `produces_artifacts=True`: that flag is what lets the platform
publish its outputs. If the task also wraps an output itself, this declaration wins for the
artifact's name, version, partitions and parents, and the task's description, card and attrs fill
in whatever it leaves empty.

Every task called inside the block receives the declarations, so call one task per block. They
are not passed on to the actions that task itself spawns. Outside a task this does nothing.


| Parameter | Type | Description |
|-|-|-|
| `**outputs` | `Metadata` | |

