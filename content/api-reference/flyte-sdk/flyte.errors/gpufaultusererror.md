---
title: GPUFaultUserError
description: "This error is raised when the GPU fault the backend attributed the failure to was the workload's own doing, for example an out-of-bounds access that the driver reported as an Xid 31."
icon: exclamation-triangle
version: 2.8.0
variants: +flyte +union
layout: py_api
---

# GPUFaultUserError

**Package:** `flyte.errors`

This error is raised when the GPU fault the backend attributed the failure to was the workload's own doing, for
example an out-of-bounds access that the driver reported as an Xid 31. The GPU itself is fine once the process is
gone, so the failure was charged to the task's own retry budget.


## Parameters

```python
class GPUFaultUserError(
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

