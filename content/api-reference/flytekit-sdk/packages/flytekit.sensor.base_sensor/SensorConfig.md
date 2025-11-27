---
title: SensorConfig
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# SensorConfig

**Package:** `flytekit.sensor.base_sensor`

Base class for protocol classes.

Protocol classes are defined as::

    class Proto(Protocol):
        def meth(self) -> int:
            ...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

    class C:
        def meth(self) -> int:
            return 0

    def func(x: Proto) -> int:
        return x.meth()

    func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

    class GenProto(Protocol[T]):
        def meth(self) -> T:
            ...


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


