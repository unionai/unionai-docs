---
title: flytekit.models.interface
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.interface

## Directory

### Classes

| Class | Description |
|-|-|
| [`Parameter`](.././flytekit.models.interface#flytekitmodelsinterfaceparameter) | None. |
| [`ParameterMap`](.././flytekit.models.interface#flytekitmodelsinterfaceparametermap) | None. |
| [`TypedInterface`](.././flytekit.models.interface#flytekitmodelsinterfacetypedinterface) | None. |
| [`Variable`](.././flytekit.models.interface#flytekitmodelsinterfacevariable) | None. |
| [`VariableMap`](.././flytekit.models.interface#flytekitmodelsinterfacevariablemap) | None. |

## flytekit.models.interface.Parameter

```python
def Parameter(
    var,
    default,
    required,
    artifact_query: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactQuery],
    artifact_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
):
```
Declares an input parameter.  A parameter is used as input to a launch plan and has
the special ability to have a default value or mark itself as required.


| Parameter | Type |
|-|-|
| `var` |  |
| `default` |  |
| `required` |  |
| `artifact_query` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactQuery]` |
| `artifact_id` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| artifact_id |  |  |
| artifact_query |  |  |
| behavior |  |  |
| default |  |  |
| is_empty |  |  |
| required |  |  |
| var |  |  |

## flytekit.models.interface.ParameterMap

```python
def ParameterMap(
    parameters,
):
```
A map of Parameters


| Parameter | Type |
|-|-|
| `parameters` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |
| parameters |  |  |

## flytekit.models.interface.TypedInterface

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

## flytekit.models.interface.Variable

```python
def Variable(
    type,
    description,
    artifact_partial_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
    artifact_tag: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag],
):
```
| Parameter | Type |
|-|-|
| `type` |  |
| `description` |  |
| `artifact_partial_id` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID]` |
| `artifact_tag` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`to_flyte_idl_list()`](#to_flyte_idl_list) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    variable_proto,
):
```
| Parameter | Type |
|-|-|
| `variable_proto` |  |

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
#### to_flyte_idl_list()

```python
def to_flyte_idl_list()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| artifact_partial_id |  |  |
| artifact_tag |  |  |
| description |  |  |
| is_empty |  |  |
| type |  |  |

## flytekit.models.interface.VariableMap

```python
def VariableMap(
    variables,
):
```
A map of Variables



| Parameter | Type |
|-|-|
| `variables` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

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
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| is_empty |  |  |
| variables |  |  |

