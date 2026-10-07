---
title: NVIDIA Nsight Systems
description: "Flyte NVIDIA Nsight Systems plugin."
icon: book
version: 2.11.1.dev2+g6d3d72b81
variants: +flyte +union
layout: py_api
---

# NVIDIA Nsight Systems



Flyte NVIDIA Nsight Systems plugin.

Run a Flyte task under Nsight Systems (`nsys`) by adding one decorator. The task runs under the
profiler automatically, its GPU metrics are summarized into the task's Flyte report, and the full
.nsys-rep trace is handed back as a downloadable output. Your task's inputs, body, and return value
are unchanged, so profiling is something you add and remove without touching the work itself.

How it works: the decorator stamps the task's container so the Flyte runtime re-execs the whole
action under `nsys launch`. Inside the task, collection is bracketed with `nsys start` / `nsys stop`
(`nsys stop` flushes the report to disk while the task keeps running), the trace is summarized with
`nsys stats`, and the .nsys-rep is returned through a traced function so it appears as a trace output.

Basic usage:

    import flyte
    from flyteplugins.nsight import nsys_profile

    env = flyte.TaskEnvironment(
        name="train",
        image=flyte.Image.from_base("nvcr.io/nvidia/pytorch:24.08-py3")
            .clone(extendable=True, name="train", python_version=(3, 10))
            .with_pip_packages("flyte", "uv"),
        resources=flyte.Resources(gpu="L4:1"),
        # osrt tracing and GPU counters need CAP_SYS_ADMIN + unconfined AppArmor.
        pod_template=flyte.PodTemplate().allow_nested_sandboxing(),
    )

    @nsys_profile(trace=["cuda", "nvtx", "cudnn", "cublas"])
    @env.task
    async def train(epochs: int = 20) -> str:
        ...ordinary training code...
        return "done"

Profile only a region of a long task:

    from flyteplugins.nsight import nsys, nvtx

    @nsys_profile(capture="manual")
    @env.task
    async def train():
        warmup()
        async with nsys.range("hot-loop"):
            for step in range(100):
                with nvtx.range("step"):
                    train_step()

Requirements:
- The task image must have the `nsys` CLI on PATH (NGC PyTorch images ship it).
- `trace` domains osrt and GPU-counter sampling need elevated pod capabilities; restrict to
  cuda,nvtx if you cannot grant them.

Decorator order: @nsys_profile must be the outermost decorator, above @env.task.
## Directory

### Methods

| Method | Description |
|-|-|
| [`capture_report_file()`](#capture_report_file) | Upload the .nsys-rep and surface it as a trace output. |
| [`nsys_available()`](#nsys_available) | True if the `nsys` binary is on PATH in this container. |
| [`nsys_profile()`](#nsys_profile) | Profile a Flyte task with Nsight Systems. |
| [`session_name()`](#session_name) |  |
| [`under_nsys()`](#under_nsys) | True only when the runtime actually re-exec'd this process under `nsys launch`. |


### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_REPORTS` | `tuple` |  |

## Methods

#### capture_report_file()

```python
def capture_report_file(
    report_path: str,
) -> File
```
Upload the .nsys-rep and surface it as a trace output. Open it in the Nsight Systems GUI.


| Parameter | Type | Description |
|-|-|-|
| `report_path` | `str` | |

#### nsys_available()

```python
def nsys_available()
```
True if the `nsys` binary is on PATH in this container.


#### nsys_profile()

```python
def nsys_profile(
    trace: Sequence[str] = ('cuda', 'nvtx'),
    sample: Optional[str] = None,
    capture: str = 'task',
    reports: Sequence[str] = ('cuda_gpu_kern_sum', 'cuda_gpu_mem_time_sum', 'cuda_gpu_mem_size_sum', 'cuda_api_sum', 'nvtx_pushpop_sum'),
    attach_report: bool = True,
    enabled: bool = True,
) -> F
```
Profile a Flyte task with Nsight Systems.

Decorator order: @nsys_profile must be the outermost decorator, above @env.task.


| Parameter | Type | Description |
|-|-|-|
| `trace` | `Sequence[str]` | nsys trace domains, e.g. cuda, nvtx, cudnn, cublas, osrt. osrt (OS-runtime) and GPU-counter sampling need elevated pod capabilities; see allow_nested_sandboxing(). |
| `sample` | `Optional[str]` | CPU sampling mode passed to `nsys -s` (e.g. "cpu", "none"). Omitted by default. |
| `capture` | `str` | "task" profiles the whole task body automatically. "manual" launches the task under nsys but leaves collection to nsys.range(...) blocks in the body (`async with` in an async task, plain `with` in a sync task). |
| `reports` | `Sequence[str]` | which `nsys stats` reports to render into the deck. |
| `attach_report` | `bool` | also surface the .nsys-rep as a downloadable trace output. |
| `enabled` | `bool` | when False the decorator is a transparent passthrough, so profiling can be kept in code and turned off without removing it. |

#### session_name()

```python
def session_name()
```
#### under_nsys()

```python
def under_nsys()
```
True only when the runtime actually re-exec'd this process under `nsys launch`.

Requires both the generic wrapped-flag and an nsys session name, so a plain local run
(where the re-exec hook never fires) reports False and the task runs unprofiled.


