---
title: SensorMetadata
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SensorMetadata

**Package:** `flytekit.sensor.base_sensor`

```python
class SensorMetadata(
    sensor_module: str,
    sensor_name: str,
    sensor_config: typing.Optional[dict],
    inputs: typing.Optional[dict],
)
```
| Parameter | Type | Description |
|-|-|-|
| `sensor_module` | `str` | |
| `sensor_name` | `str` | |
| `sensor_config` | `typing.Optional[dict]` | |
| `inputs` | `typing.Optional[dict]` | |

## Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


### decode()

```python
def decode(
    data: bytes,
) -> ResourceMeta
```
Decode the resource meta from bytes.


| Parameter | Type | Description |
|-|-|-|
| `data` | `bytes` | |

### encode()

```python
def encode()
```
Encode the resource meta to bytes.


