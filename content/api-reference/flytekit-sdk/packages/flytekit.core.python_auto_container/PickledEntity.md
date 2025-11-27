---
title: PickledEntity
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PickledEntity

**Package:** `flytekit.core.python_auto_container`

Represents the structure of the pickled object stored in the .pkl file for interactive mode.

Attributes:
    metadata: Metadata about the pickled entities including Python version
    entities: Dictionary mapping entity names to their PythonAutoContainerTask instances


```python
class PickledEntity(
    metadata: PickledEntityMetadata,
    entities: Dict[str, PythonAutoContainerTask],
)
```
| Parameter | Type | Description |
|-|-|-|
| `metadata` | `PickledEntityMetadata` | |
| `entities` | `Dict[str, PythonAutoContainerTask]` | |

