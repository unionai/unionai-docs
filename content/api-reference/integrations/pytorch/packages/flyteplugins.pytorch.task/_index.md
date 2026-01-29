---
title: flyteplugins.pytorch.task
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyteplugins.pytorch.task

## Directory

### Classes

| Class | Description |
|-|-|
| [`Elastic`](../flyteplugins.pytorch.task/elastic) | Elastic defines the configuration for running a PyTorch elastic job using torch. |
| [`RunPolicy`](../flyteplugins.pytorch.task/runpolicy) | RunPolicy describes some policy to apply to the execution of a kubeflow job. |
| [`TorchFunctionTask`](../flyteplugins.pytorch.task/torchfunctiontask) | Plugin to transform local python code for execution as a PyTorch job. |

### Methods

| Method | Description |
|-|-|
| [`launcher_entrypoint()`](#launcher_entrypoint) |  |


## Methods

#### launcher_entrypoint()

```python
def launcher_entrypoint(
    tctx: flyte.models.TaskContext,
    fn: bytes,
    kwargs: **kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `tctx` | `flyte.models.TaskContext` | |
| `fn` | `bytes` | |
| `kwargs` | `**kwargs` | |

