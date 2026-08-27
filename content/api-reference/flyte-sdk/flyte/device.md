---
title: Device
version: 2.6.10
variants: +flyte +union
layout: py_api
---

# Device

**Package:** `flyte`

Represents a device type, its quantity and partition if applicable.



## Parameters

```python
class Device(
    quantity: int,
    device_class: typing.Literal['GPU', 'TPU', 'NEURON', 'AMD_GPU', 'HABANA_GAUDI'],
    device: str | None = None,
    partition: str | None = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `quantity` | `int` | The number of devices of this type. |
| `device_class` | `typing.Literal['GPU', 'TPU', 'NEURON', 'AMD_GPU', 'HABANA_GAUDI']` | |
| `device` | `str \| None` | The type of device (e.g., "T4", "A100"). |
| `partition` | `str \| None` | The partition of the device (e.g., "1g.5gb", "2g.10gb" for gpus) or ("1x1", ... for tpus). |

