---
title: MultiInstanceGPUAccelerator
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# MultiInstanceGPUAccelerator

**Package:** `flytekit.extras.accelerators`

Base class for all multi-instance GPU accelerator types. It is recommended to use one of the pre-defined constants
below, as name has to match the name of the device configured on the cluster.
For example, to specify a 10GB partition of an A100 GPU, use ``A100.partition_2g_10gb``.



## Properties

| Property | Type | Description |
|-|-|-|
| `unpartitioned` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`partitioned()`](#partitioned) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |


### partitioned()

```python
def partitioned(
    partition_size: str,
) -> ~MIG
```
| Parameter | Type | Description |
|-|-|-|
| `partition_size` | `str` | |

### to_flyte_idl()

```python
def to_flyte_idl()
```
