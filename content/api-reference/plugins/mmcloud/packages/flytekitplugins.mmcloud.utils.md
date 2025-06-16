---
title: flytekitplugins.mmcloud.utils
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.mmcloud.utils

## Directory

### Methods

| Method | Description |
|-|-|
| [`async_check_output()`](#async_check_output) | This behaves similarly to subprocess. |
| [`flyte_to_mmcloud_resources()`](#flyte_to_mmcloud_resources) | Map Flyte (K8s) resources to MMCloud resources. |
| [`mmcloud_status_to_flyte_phase()`](#mmcloud_status_to_flyte_phase) | Map MMCloud status to Flyte phase. |


### Variables

| Property | Type | Description |
|-|-|-|
| `MMCLOUD_STATUS_TO_FLYTE_PHASE` | `dict` |  |
| `PIPE` | `int` |  |
| `ROUND_CEILING` | `str` |  |

## Methods

#### async_check_output()

```python
def async_check_output(
    args,
    kwargs,
)
```
This behaves similarly to subprocess.check_output().


| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

#### flyte_to_mmcloud_resources()

```python
def flyte_to_mmcloud_resources(
    requests: typing.Optional[flytekit.core.resources.Resources],
    limits: typing.Optional[flytekit.core.resources.Resources],
) -> typing.Tuple[int, int, int, int]
```
Map Flyte (K8s) resources to MMCloud resources.


| Parameter | Type |
|-|-|
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |

#### mmcloud_status_to_flyte_phase()

```python
def mmcloud_status_to_flyte_phase(
    status: str,
) -> <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x121406390>
```
Map MMCloud status to Flyte phase.


| Parameter | Type |
|-|-|
| `status` | `str` |

