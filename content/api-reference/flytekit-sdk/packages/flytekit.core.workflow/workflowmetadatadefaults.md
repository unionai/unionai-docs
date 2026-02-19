---
title: WorkflowMetadataDefaults
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# WorkflowMetadataDefaults

**Package:** `flytekit.core.workflow`

This class is similarly named to the one above. Please see the IDL for more information but essentially, this
WorkflowMetadataDefaults class represents the defaults that are handed down to a workflow's tasks, whereas
WorkflowMetadata represents metadata about the workflow itself.



```python
class WorkflowMetadataDefaults(
    interruptible: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `interruptible` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`to_flyte_model()`](#to_flyte_model) |  |


### to_flyte_model()

```python
def to_flyte_model()
```
