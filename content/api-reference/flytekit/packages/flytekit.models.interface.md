---
title: flytekit.models.interface
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.models.interface

## Directory

### Classes

| Class | Description |
|-|-|
| [`Parameter`](.././flytekit.models.interface#flytekitmodelsinterfaceparameter) |  |
| [`ParameterMap`](.././flytekit.models.interface#flytekitmodelsinterfaceparametermap) |  |
| [`TypedInterface`](.././flytekit.models.interface#flytekitmodelsinterfacetypedinterface) |  |
| [`Variable`](.././flytekit.models.interface#flytekitmodelsinterfacevariable) |  |
| [`VariableMap`](.././flytekit.models.interface#flytekitmodelsinterfacevariablemap) |  |

## flytekit.models.interface.Parameter

```python
class Parameter(
    var,
    default,
    required,
    artifact_query: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactQuery],
    artifact_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
)
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> Parameter
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
| `artifact_id` |  |  |
| `artifact_query` |  |  |
| `behavior` |  |  |
| `default` |  | {{< multiline >}}This is the default literal value that will be applied for this parameter if not user specified.
{{< /multiline >}} |
| `is_empty` |  |  |
| `required` |  | {{< multiline >}}If True, this parameter must be specified.  There cannot be a default value.
{{< /multiline >}} |
| `var` |  | {{< multiline >}}The variable definition for this input parameter.
{{< /multiline >}} |

## flytekit.models.interface.ParameterMap

```python
class ParameterMap(
    parameters,
)
```
A map of Parameters


| Parameter | Type |
|-|-|
| `parameters` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> ParameterMap
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
| `is_empty` |  |  |
| `parameters` |  |  |

## flytekit.models.interface.TypedInterface

```python
class TypedInterface(
    inputs,
    outputs,
)
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`transform_interface_to_list()`](#transform_interface_to_list) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed. |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    proto: flyteidl.core.interface_pb2.TypedInterface,
) -> TypedInterface
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
) -> TypedInterface
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
| `inputs` |  |  |
| `is_empty` |  |  |
| `outputs` |  |  |

## flytekit.models.interface.Variable

```python
class Variable(
    type,
    description,
    artifact_partial_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
    artifact_tag: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag],
)
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
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`to_flyte_idl_list()`](#to_flyte_idl_list) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    variable_proto,
) -> flyteidl.core.interface_pb2.Variable
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
| `artifact_partial_id` |  |  |
| `artifact_tag` |  |  |
| `description` |  | {{< multiline >}}This is a help string that can provide context for what this variable means in relation to a task or workflow.
{{< /multiline >}} |
| `is_empty` |  |  |
| `type` |  | {{< multiline >}}This describes the type of value that must be provided to satisfy this variable.
{{< /multiline >}} |

## flytekit.models.interface.VariableMap

```python
class VariableMap(
    variables,
)
```
A map of Variables



| Parameter | Type |
|-|-|
| `variables` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) | . |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | . |
| [`to_flyte_idl()`](#to_flyte_idl) | . |
| [`verbose_string()`](#verbose_string) | . |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
) -> VariableMap
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
| `is_empty` |  |  |
| `variables` |  |  |

