---
title: Device
version: 2.2.1
variants: +flyte +union
layout: py_api
---

# Device

**Package:** `flyte`

Represents a device type, its quantity and partition if applicable.
param device: The type of device (e.g., "T4", "A100").
param quantity: The number of devices of this type.
param partition: The partition of the device (e.g., "1g.5gb", "2g.10gb" for gpus) or ("1x1", ... for tpus).


## Parameters

```python
class Device(
    quantity: int,
    device_class: typing.Literal['GPU', 'TPU', 'NEURON', 'AMD_GPU', 'HABANA_GAUDI'],
    device: str | None,
    partition: str | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `quantity` | `int` | |
| `device_class` | `typing.Literal['GPU', 'TPU', 'NEURON', 'AMD_GPU', 'HABANA_GAUDI']` | |
| `device` | `str \| None` | |
| `partition` | `str \| None` | |

