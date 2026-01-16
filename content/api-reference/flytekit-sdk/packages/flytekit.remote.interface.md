---
title: flytekit.remote.interface
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.remote.interface

## Directory

### Classes

| Class | Description |
|-|-|
| [`TypedInterface`](.././flytekit.remote.interface#flytekitremoteinterfacetypedinterface) |  |

## flytekit.remote.interface.TypedInterface

```python
class TypedInterface(
    inputs,
    outputs,
)
```
Please note that this model is slightly incorrect, but is more user-friendly. The underlying inputs and
outputs are represented directly as Python dicts, rather than going through the additional VariableMap layer.



| Parameter | Type | Description |
|-|-|-|
| `inputs` |  | |
| `outputs` |  | |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`promote_from_model()`](#promote_from_model) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`transform_interface_to_list()`](#transform_interface_to_list) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.interface_pb2.TypedInterface,
) -> TypedInterface
```
| Parameter | Type | Description |
|-|-|-|
| `proto` | `flyteidl.core.interface_pb2.TypedInterface` | |

#### promote_from_model()

```python
def promote_from_model(
    model,
)
```
| Parameter | Type | Description |
|-|-|-|
| `model` |  | |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
:rtype: Text


#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### transform_interface_to_list()

```python
def transform_interface_to_list(
    bound_inputs: typing.Set[str],
    excluded_inputs: typing.Set[str],
) -> TypedInterface
```
Takes a single task interface and interpolates it to an array interface - to allow performing distributed
python map like functions


| Parameter | Type | Description |
|-|-|-|
| `bound_inputs` | `typing.Set[str]` | fixed inputs that should not be updated to a list and will be maintained as is |
| `excluded_inputs` | `typing.Set[str]` | inputs that should be excluded from the new interface |

### Properties

| Property | Type | Description |
|-|-|-|
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

