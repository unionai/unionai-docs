---
title: Artifact
version: 2.6.3
variants: +flyte +union
layout: py_api
---

# Artifact

**Package:** `flyte.artifacts`

Protocol for objects wrapped with Flyte metadata.


```python
protocol Artifact()
```
## Methods

| Method | Description |
|-|-|
| [`get_flyte_metadata()`](#get_flyte_metadata) | Get the Flyte metadata associated with this artifact. |


### get_flyte_metadata()

```python
def get_flyte_metadata()
```
Get the Flyte metadata associated with this artifact.


