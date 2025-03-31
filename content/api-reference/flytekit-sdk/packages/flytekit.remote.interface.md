---
title: flytekit.remote.interface
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.remote.interface

## Directory

### Classes

| Class | Description |
|-|-|
| [`TypedInterface`](.././flytekit.remote.interface#flytekitremoteinterfacetypedinterface) | None. |

## flytekit.remote.interface.TypedInterface

```python
def TypedInterface(
    inputs,
    outputs,
):
```
Please note that this model is slightly incorrect, but is more user-friendly. The underlying inputs and
outputs are represented directly as Python dicts, rather than going through the additional VariableMap layer.



| Parameter | Type |
|-|-|
| `inputs` |  |
| `outputs` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) | None |
| [`transform_interface_to_list()`](#transform_interface_to_list) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.interface_pb2.TypedInterface,
):
```
| Parameter | Type |
|-|-|
| `proto` | `flyteidl.core.interface_pb2.TypedInterface` |

#### promote_from_model()

```python
def promote_from_model(
    model,
):
```
| Parameter | Type |
|-|-|
| `model` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### transform_interface_to_list()

```python
def transform_interface_to_list(
    bound_inputs: typing.Set[str],
    excluded_inputs: typing.Set[str],
):
```
Takes a single task interface and interpolates it to an array interface - to allow performing distributed
python map like functions


| Parameter | Type |
|-|-|
| `bound_inputs` | `typing.Set[str]` |
| `excluded_inputs` | `typing.Set[str]` |

#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| inputs |  |  |
| is_empty |  |  |
| outputs |  |  |

