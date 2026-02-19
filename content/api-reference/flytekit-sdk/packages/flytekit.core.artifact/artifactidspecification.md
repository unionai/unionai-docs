---
title: ArtifactIDSpecification
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ArtifactIDSpecification

**Package:** `flytekit.core.artifact`

This is a special object that helps specify how Artifacts are to be created. See the comment in the
call function of the main Artifact class. Also see the handling code in transform_variable_map for more
information. There's a limited set of information that we ultimately need in a TypedInterface, so it
doesn't make sense to carry the full Artifact object around. This object should be sufficient, despite
having a pointer to the main artifact.



```python
class ArtifactIDSpecification(
    a: Artifact,
)
```
| Parameter | Type | Description |
|-|-|-|
| `a` | `Artifact` | |

## Methods

| Method | Description |
|-|-|
| [`bind_partitions()`](#bind_partitions) |  |
| [`to_partial_artifact_id()`](#to_partial_artifact_id) |  |


### bind_partitions()

```python
def bind_partitions(
    args,
    kwargs,
) -> ArtifactIDSpecification
```
| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### to_partial_artifact_id()

```python
def to_partial_artifact_id()
```
