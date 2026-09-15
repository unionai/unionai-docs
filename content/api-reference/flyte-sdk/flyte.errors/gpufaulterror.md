---
title: GPUFaultError
description: "This error is raised when the backend attributed the task failure to a GPU or NVSwitch fault that the GPU health daemon observed on the node, such as an Xid 31 (a GPU memory page fault) or an Xid 79 (the GPU fell off the bus)."
icon: exclamation-triangle
version: 2.8.0
variants: +flyte +union
layout: py_api
---

# GPUFaultError

**Package:** `flyte.errors`

This error is raised when the backend attributed the task failure to a GPU or NVSwitch fault that the GPU health
daemon observed on the node, such as an Xid 31 (a GPU memory page fault) or an Xid 79 (the GPU fell off the bus).

Catch this class to handle every GPU fault. It is the base of both concrete errors, GPUFaultUserError for a fault
the workload caused and GPUFaultSystemError for a hardware fault, so one except clause covers both, and the code,
severity and xid attributes are there to branch on afterwards.

The two do not reach user code on the same terms. A user severity Xid (13, 31, 43, 45) is the workload's own
doing, it will fault again if it is replayed unchanged, so the backend charges it to the task's own retry budget
and this error surfaces as soon as that budget is spent. A critical hardware fault is not the workload's doing, so
the platform retries it without charging the user's budget and reschedules onto other hardware where it can, which
means user code sees a critical fault only after platform policy has given up on it. Neither one is a signal to
retry in place: a user fault has already exhausted its own retries by the time it is raised, and a critical fault
has already been retried elsewhere.

This exception and its fields appear when the platform classified the fault and supplied the typed fault data with
the failure. On a platform or a version that did not, the same failure arrives as a generic runtime error with no
fault attributes on it, so user code must not depend on this exception firing. Write the handler for the case where
it does, and keep whatever handles an ordinary task failure for the case where it does not.

The fault attributes are read from the typed fault and are absent when the failure carried none, so any of them can
be None and they should be read defensively. The message still leads with the driver's own sentence either way.


## Parameters

```python
class GPUFaultError(
    code: str,
    kind: typing.Literal['system', 'unknown', 'user'],
    message: str,
    worker: str | None = None,
    fault_kind: str | None = None,
    fault_code: int | None = None,
    fault_name: str | None = None,
    severity: str | None = None,
    gpu_uuid: str | None = None,
    gpu_index: int | None = None,
    node: str | None = None,
    pci_bus_id: str | None = None,
    process: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `code` | `str` | |
| `kind` | `typing.Literal['system', 'unknown', 'user']` | |
| `message` | `str` | |
| `worker` | `str \| None` | |
| `fault_kind` | `str \| None` | |
| `fault_code` | `int \| None` | |
| `fault_name` | `str \| None` | |
| `severity` | `str \| None` | |
| `gpu_uuid` | `str \| None` | |
| `gpu_index` | `int \| None` | |
| `node` | `str \| None` | |
| `pci_bus_id` | `str \| None` | |
| `process` | `str \| None` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `sxid` | `int \| None` | The NVSwitch SXid number of the fault, or None when the fault was a GPU Xid or when the number could not be determined. |
| `xid` | `int \| None` | The NVIDIA Xid number of the fault, or None when the fault was an NVSwitch SXid or when the number could not be determined. Xid and SXid numbers share a numbering space but not a meaning, so a number alone never identifies a fault, read fault_kind together with fault_code to tell them apart. |

