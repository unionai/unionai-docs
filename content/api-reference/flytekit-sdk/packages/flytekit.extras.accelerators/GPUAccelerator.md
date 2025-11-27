---
title: GPUAccelerator
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# GPUAccelerator

**Package:** `flytekit.extras.accelerators`

Class that represents a GPU accelerator. The class can be instantiated with any valid GPU device name, but
it is recommended to use one of the pre-defined constants below, as name has to match the name of the device
configured on the cluster.


```python
class GPUAccelerator(
    device: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `device` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### to_flyte_idl()

```python
def to_flyte_idl()
```
