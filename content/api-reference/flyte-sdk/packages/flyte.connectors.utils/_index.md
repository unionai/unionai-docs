---
title: flyte.connectors.utils
version: 2.0.0b34.dev10+g162555e05
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.connectors.utils

## Directory

### Methods

| Method | Description |
|-|-|
| [`convert_to_flyte_phase()`](#convert_to_flyte_phase) | Convert the state from the connector to the phase in flyte. |
| [`is_terminal_phase()`](#is_terminal_phase) | Return true if the phase is terminal. |
| [`print_metadata()`](#print_metadata) |  |


## Methods

#### convert_to_flyte_phase()

```python
def convert_to_flyte_phase(
    state: str,
) -> <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1090a40b0>
```
Convert the state from the connector to the phase in flyte.


| Parameter | Type | Description |
|-|-|-|
| `state` | `str` | |

#### is_terminal_phase()

```python
def is_terminal_phase(
    phase: <google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1090a40b0>,
) -> bool
```
Return true if the phase is terminal.


| Parameter | Type | Description |
|-|-|-|
| `phase` | `<google.protobuf.internal.enum_type_wrapper.EnumTypeWrapper object at 0x1090a40b0>` | |

#### print_metadata()

```python
def print_metadata()
```
