---
title: GPUFaultSystemError
description: "This error is raised when the GPU fault the backend attributed the failure to condemned the device or the node, for example an uncorrectable ECC error or a GPU that fell off the bus."
icon: exclamation-triangle
version: 2.8.1
variants: +flyte +union
layout: py_api
---

# GPUFaultSystemError

**Package:** `flyte.errors`

This error is raised when the GPU fault the backend attributed the failure to condemned the device or the node,
for example an uncorrectable ECC error or a GPU that fell off the bus. The workload did not cause it, so the
platform retried the task on its own budget before this error reached user code.


## Parameters

```python
class GPUFaultSystemError(
    code: str,
    message: str,
    worker: str | None = None,
    **fault,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `message` | `str` | |
| `worker` | `str \| None` | |
| `**fault` |  | |

## Properties

| Property | Type | Description |
|-|-|-|
| `sxid` | `int \| None` | The NVSwitch SXid number of the fault, or None when the fault was a GPU Xid or when the number could not be determined. |
| `xid` | `int \| None` | The NVIDIA Xid number of the fault, or None when the fault was an NVSwitch SXid or when the number could not be determined. Xid and SXid numbers share a numbering space but not a meaning, so a number alone never identifies a fault, read fault_kind together with fault_code to tell them apart. |

