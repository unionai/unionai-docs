---
title: flytekit.core.artifact
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.artifact

## Directory

### Classes

| Class | Description |
|-|-|
| [`Artifact`](../flytekit.core.artifact/artifact) | An Artifact is effectively just a metadata layer on top of data that exists in Flyte. |
| [`ArtifactIDSpecification`](../flytekit.core.artifact/artifactidspecification) | This is a special object that helps specify how Artifacts are to be created. |
| [`ArtifactQuery`](../flytekit.core.artifact/artifactquery) |  |
| [`DefaultArtifactSerializationHandler`](../flytekit.core.artifact/defaultartifactserializationhandler) | This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |
| [`InputsBase`](../flytekit.core.artifact/inputsbase) | A class to provide better partition semantics. |
| [`Partition`](../flytekit.core.artifact/partition) |  |
| [`Partitions`](../flytekit.core.artifact/partitions) |  |
| [`Serializer`](../flytekit.core.artifact/serializer) |  |
| [`TimePartition`](../flytekit.core.artifact/timepartition) |  |

### Protocols

| Protocol | Description |
|-|-|
| [`ArtifactSerializationHandler`](../flytekit.core.artifact/artifactserializationhandler) | This protocol defines the interface for serializing artifact-related entities down to Flyte IDL. |

### Variables

| Property | Type | Description |
|-|-|-|
| `Inputs` | `InputsBase` |  |
| `MAX_PARTITIONS` | `int` |  |
| `O` | `TypeVar` |  |
| `TIME_PARTITION_KWARG` | `str` |  |

