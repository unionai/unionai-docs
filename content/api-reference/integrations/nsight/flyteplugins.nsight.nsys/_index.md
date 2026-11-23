---
title: flyteplugins.nsight.nsys
description: "Region profiling: collect only part of a task."
icon: box-seam
version: 2.11.1.dev3+g825fdbe57
variants: +flyte +union
layout: py_api
---

# flyteplugins.nsight.nsys

Region profiling: collect only part of a task.

Whole-task profiling of a long run produces an unwieldy multi-gigabyte trace. When you only
want the hot loop, put the task under nsys with `@nsys_profile(capture="manual")` and wrap the
region you care about. The region matches your task body — `async with` in an `async def` task,
plain `with` in a `def` task, since `@nsys_profile` accepts both:

    from flyteplugins.nsight import nsys, nvtx

    @nsys_profile(capture="manual")
    @env.task(report=True)
    async def train():                       # async task -> `async with`
        warmup()
        async with nsys.range("hot-loop"):
            for step in range(100):
                with nvtx.range("step"):
                    train_step()

    @nsys_profile(capture="manual")
    @env.task(report=True)
    def train_sync():                        # sync task -> plain `with`
        warmup()
        with nsys.range("hot-loop"):
            for step in range(100):
                with nvtx.range("step"):
                    train_step()

Each region collects independently, writes its own .nsys-rep, renders its own report section, and
attaches its own trace output. Outside a profiling run (local execution, or the task was not
launched under nsys) the region is a transparent no-op, so the same code runs anywhere.
## Directory

### Methods

| Method | Description |
|-|-|
| [`profile()`](#profile) | Profile the wrapped block as a named region. |
| [`range()`](#range) | Profile the wrapped block as a named region. |


## Methods

#### profile()

```python
def profile(
    name: str,
    reports: Sequence[str] = ('cuda_gpu_kern_sum', 'cuda_gpu_mem_time_sum', 'cuda_gpu_mem_size_sum', 'cuda_api_sum', 'nvtx_pushpop_sum'),
    attach: bool = True,
) -> _Region
```
Profile the wrapped block as a named region. No-op if not running under nsys.

Works both ways, matching your task body:

    async with nsys.range("hot-loop"):   # in an `async def` task
        ...
    with nsys.range("hot-loop"):          # in a plain `def` task
        ...


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `reports` | `Sequence[str]` | |
| `attach` | `bool` | |

#### range()

```python
def range(
    name: str,
    reports: Sequence[str] = ('cuda_gpu_kern_sum', 'cuda_gpu_mem_time_sum', 'cuda_gpu_mem_size_sum', 'cuda_api_sum', 'nvtx_pushpop_sum'),
    attach: bool = True,
) -> _Region
```
Profile the wrapped block as a named region. No-op if not running under nsys.

Works both ways, matching your task body:

    async with nsys.range("hot-loop"):   # in an `async def` task
        ...
    with nsys.range("hot-loop"):          # in a plain `def` task
        ...


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `reports` | `Sequence[str]` | |
| `attach` | `bool` | |

