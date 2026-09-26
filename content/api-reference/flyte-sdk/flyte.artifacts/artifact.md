---
title: Artifact
description: "Anything that can declare itself an artifact."
icon: diagram-3
version: 2.10.2
variants: +flyte +union
layout: py_api
---

# Artifact

**Package:** `flyte.artifacts`

Anything that can declare itself an artifact.

Deliberately method-only. A `runtime_checkable` protocol's `isinstance`
checks data members as well as methods, so declaring the wrapper's private
`_flyte_metadata` here would make `isinstance` reject every value that
implements the method without being an `ArtifactWrapper` -- which is the
whole point of the protocol. `ArtifactWrapper` still has the attribute;
the protocol simply does not require it, and nothing read it through this
type.


```python
protocol Artifact()
```
## Methods

| Method | Description |
|-|-|
| [`get_artifact_metadata()`](#get_artifact_metadata) | Metadata to publish for this value, or None to publish nothing. |


### get_artifact_metadata()

```python
def get_artifact_metadata()
```
Metadata to publish for this value, or None to publish nothing.

`None` is a normal answer, not an error: a type can participate in the
protocol while a given instance declares nothing (a volume with no
artifact identity, say). Callers must handle it -- `convert.py` and
`Artifact.create` both check before publishing.


