---
title: flyteplugins.nsight.nvtx
description: "NVTX annotation helpers."
icon: box-seam
version: 2.11.1.dev3+g825fdbe57
variants: +flyte +union
layout: py_api
---

# flyteplugins.nsight.nvtx

NVTX annotation helpers.

Labels regions of your code so they show up as named spans on the Nsight timeline and in the
NVTX summary of the report. Thin wrappers over torch.cuda.nvtx so you annotate without importing
torch internals, and a no-op when torch is not installed or was built without CUDA, so the same
code runs unchanged off-GPU and outside a profiling run.

    from flyteplugins.nsight import nvtx

    with nvtx.range("forward"):
        out = model(x)

    nvtx.mark("checkpoint saved")
## Directory

### Methods

| Method | Description |
|-|-|
| [`mark()`](#mark) | Drop a single NVTX marker at this instant. |
| [`range()`](#range) | Push an NVTX range on enter and pop it on exit. |


## Methods

#### mark()

```python
def mark(
    message: str,
)
```
Drop a single NVTX marker at this instant. No-op if NVTX is unavailable.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

#### range()

```python
def range(
    message: str,
) -> Iterator[None]
```
Push an NVTX range on enter and pop it on exit. No-op if NVTX is unavailable.


| Parameter | Type | Description |
|-|-|-|
| `message` | `str` | |

