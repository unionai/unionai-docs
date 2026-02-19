---
title: SensorConfig
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SensorConfig

**Package:** `flytekit.sensor.base_sensor`

```python
protocol SensorConfig()
```
## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | Deserialize the sensor config from a dictionary. |
| [`to_dict()`](#to_dict) | Serialize the sensor config to a dictionary. |


### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
) -> SensorConfig
```
Deserialize the sensor config from a dictionary.


| Parameter | Type | Description |
|-|-|-|
| `d` | `typing.Dict[str, typing.Any]` | |

### to_dict()

```python
def to_dict()
```
Serialize the sensor config to a dictionary.


