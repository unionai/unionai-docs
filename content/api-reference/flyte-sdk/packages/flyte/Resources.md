---
title: Resources
version: 2.0.0b38
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Resources

**Package:** `flyte`

Resources such as CPU, Memory, and GPU that can be allocated to a task.

Example:
- Single CPU, 1GiB of memory, and 1 T4 GPU:
```python
@task(resources=Resources(cpu=1, memory="1GiB", gpu="T4:1"))
def my_task() -> int:
    return 42
```
- 1CPU with limit upto 2CPU, 2GiB of memory, and 8 A100 GPUs and 10GiB of disk:
```python
@task(resources=Resources(cpu=(1, 2), memory="2GiB", gpu="A100:8", disk="10GiB"))
def my_task() -> int:
    return 42
```



```python
class Resources(
    cpu: typing.Union[int, float, str, typing.Tuple[int | float | str, int | float | str], NoneType],
    memory: typing.Union[str, typing.Tuple[str, str], NoneType],
    gpu: typing.Union[typing.Literal['A10:1', 'A10:2', 'A10:3', 'A10:4', 'A10:5', 'A10:6', 'A10:7', 'A10:8', 'A10G:1', 'A10G:2', 'A10G:3', 'A10G:4', 'A10G:5', 'A10G:6', 'A10G:7', 'A10G:8', 'A100:1', 'A100:2', 'A100:3', 'A100:4', 'A100:5', 'A100:6', 'A100:7', 'A100:8', 'A100 80G:1', 'A100 80G:2', 'A100 80G:3', 'A100 80G:4', 'A100 80G:5', 'A100 80G:6', 'A100 80G:7', 'A100 80G:8', 'B200:1', 'B200:2', 'B200:3', 'B200:4', 'B200:5', 'B200:6', 'B200:7', 'B200:8', 'H100:1', 'H100:2', 'H100:3', 'H100:4', 'H100:5', 'H100:6', 'H100:7', 'H100:8', 'H200:1', 'H200:2', 'H200:3', 'H200:4', 'H200:5', 'H200:6', 'H200:7', 'H200:8', 'L4:1', 'L4:2', 'L4:3', 'L4:4', 'L4:5', 'L4:6', 'L4:7', 'L4:8', 'L40s:1', 'L40s:2', 'L40s:3', 'L40s:4', 'L40s:5', 'L40s:6', 'L40s:7', 'L40s:8', 'V100:1', 'V100:2', 'V100:3', 'V100:4', 'V100:5', 'V100:6', 'V100:7', 'V100:8', 'RTX PRO 6000:1', 'T4:1', 'T4:2', 'T4:3', 'T4:4', 'T4:5', 'T4:6', 'T4:7', 'T4:8', 'Trn1:1', 'Trn1:4', 'Trn1:8', 'Trn1:16', 'Trn1n:1', 'Trn1n:4', 'Trn1n:8', 'Trn1n:16', 'Trn2:1', 'Trn2:4', 'Trn2:8', 'Trn2:16', 'Trn2u:1', 'Trn2u:4', 'Trn2u:8', 'Trn2u:16', 'Inf1:1', 'Inf1:2', 'Inf1:3', 'Inf1:4', 'Inf1:5', 'Inf1:6', 'Inf1:7', 'Inf1:8', 'Inf1:9', 'Inf1:10', 'Inf1:11', 'Inf1:12', 'Inf1:13', 'Inf1:14', 'Inf1:15', 'Inf1:16', 'Inf2:1', 'Inf2:2', 'Inf2:3', 'Inf2:4', 'Inf2:5', 'Inf2:6', 'Inf2:7', 'Inf2:8', 'Inf2:9', 'Inf2:10', 'Inf2:11', 'Inf2:12', 'MI100:1', 'MI210:1', 'MI250:1', 'MI250X:1', 'MI300A:1', 'MI300X:1', 'MI325X:1', 'MI350X:1', 'MI355X:1', 'Gaudi1:1'], int, flyte._resources.Device, NoneType],
    disk: typing.Optional[str],
    shm: typing.Union[str, typing.Literal['auto'], NoneType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `cpu` | `typing.Union[int, float, str, typing.Tuple[int \| float \| str, int \| float \| str], NoneType]` | The amount of CPU to allocate to the task. This can be a string, int, float, list of ints or strings, or a tuple of two ints or strings. |
| `memory` | `typing.Union[str, typing.Tuple[str, str], NoneType]` | The amount of memory to allocate to the task. This can be a string, int, float, list of ints or strings, or a tuple of two ints or strings. |
| `gpu` | `typing.Union[typing.Literal['A10:1', 'A10:2', 'A10:3', 'A10:4', 'A10:5', 'A10:6', 'A10:7', 'A10:8', 'A10G:1', 'A10G:2', 'A10G:3', 'A10G:4', 'A10G:5', 'A10G:6', 'A10G:7', 'A10G:8', 'A100:1', 'A100:2', 'A100:3', 'A100:4', 'A100:5', 'A100:6', 'A100:7', 'A100:8', 'A100 80G:1', 'A100 80G:2', 'A100 80G:3', 'A100 80G:4', 'A100 80G:5', 'A100 80G:6', 'A100 80G:7', 'A100 80G:8', 'B200:1', 'B200:2', 'B200:3', 'B200:4', 'B200:5', 'B200:6', 'B200:7', 'B200:8', 'H100:1', 'H100:2', 'H100:3', 'H100:4', 'H100:5', 'H100:6', 'H100:7', 'H100:8', 'H200:1', 'H200:2', 'H200:3', 'H200:4', 'H200:5', 'H200:6', 'H200:7', 'H200:8', 'L4:1', 'L4:2', 'L4:3', 'L4:4', 'L4:5', 'L4:6', 'L4:7', 'L4:8', 'L40s:1', 'L40s:2', 'L40s:3', 'L40s:4', 'L40s:5', 'L40s:6', 'L40s:7', 'L40s:8', 'V100:1', 'V100:2', 'V100:3', 'V100:4', 'V100:5', 'V100:6', 'V100:7', 'V100:8', 'RTX PRO 6000:1', 'T4:1', 'T4:2', 'T4:3', 'T4:4', 'T4:5', 'T4:6', 'T4:7', 'T4:8', 'Trn1:1', 'Trn1:4', 'Trn1:8', 'Trn1:16', 'Trn1n:1', 'Trn1n:4', 'Trn1n:8', 'Trn1n:16', 'Trn2:1', 'Trn2:4', 'Trn2:8', 'Trn2:16', 'Trn2u:1', 'Trn2u:4', 'Trn2u:8', 'Trn2u:16', 'Inf1:1', 'Inf1:2', 'Inf1:3', 'Inf1:4', 'Inf1:5', 'Inf1:6', 'Inf1:7', 'Inf1:8', 'Inf1:9', 'Inf1:10', 'Inf1:11', 'Inf1:12', 'Inf1:13', 'Inf1:14', 'Inf1:15', 'Inf1:16', 'Inf2:1', 'Inf2:2', 'Inf2:3', 'Inf2:4', 'Inf2:5', 'Inf2:6', 'Inf2:7', 'Inf2:8', 'Inf2:9', 'Inf2:10', 'Inf2:11', 'Inf2:12', 'MI100:1', 'MI210:1', 'MI250:1', 'MI250X:1', 'MI300A:1', 'MI300X:1', 'MI325X:1', 'MI350X:1', 'MI355X:1', 'Gaudi1:1'], int, flyte._resources.Device, NoneType]` | The amount of GPU to allocate to the task. This can be an Accelerators enum, an int, or None. |
| `disk` | `typing.Optional[str]` | The amount of disk to allocate to the task. This is a string of the form "10GiB". |
| `shm` | `typing.Union[str, typing.Literal['auto'], NoneType]` | The amount of shared memory to allocate to the task. This is a string of the form "10GiB" or "auto". If "auto", then the shared memory will be set to max amount of shared memory available on the node. |

## Methods

| Method | Description |
|-|-|
| [`get_device()`](#get_device) | Get the accelerator string for the task. |
| [`get_shared_memory()`](#get_shared_memory) | Get the shared memory string for the task. |


### get_device()

```python
def get_device()
```
Get the accelerator string for the task.

:return: If GPUs are requested, return a tuple of the device name, and potentially a partition string.
         Default cloud provider labels typically use the following values: `1g.5gb`, `2g.10gb`, etc.


### get_shared_memory()

```python
def get_shared_memory()
```
Get the shared memory string for the task.

:return: The shared memory string.


