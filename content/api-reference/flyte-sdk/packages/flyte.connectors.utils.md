---
title: flyte.connectors.utils
version: 2.0.0b26
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flyte.connectors.utils

## Directory

### Methods

| Method | Description |
|-|-|
| [`convert_to_flyte_phase()`](#convert_to_flyte_phase) | Convert the state from the connector to the phase in flyte. |
| [`is_terminal_phase()`](#is_terminal_phase) | Return true if the phase is terminal. |


## Methods

#### convert_to_flyte_phase()

```python
def convert_to_flyte_phase(
    state: str,
) -> <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10a5ef170>
```
Convert the state from the connector to the phase in flyte.


| Parameter | Type |
|-|-|
| `state` | `str` |

#### is_terminal_phase()

```python
def is_terminal_phase(
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10a5ef170>,
) -> bool
```
Return true if the phase is terminal.


| Parameter | Type |
|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x10a5ef170>` |

