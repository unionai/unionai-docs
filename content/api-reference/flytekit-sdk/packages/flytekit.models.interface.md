---
title: flytekit.models.interface
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
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


| Parameter | Type | Description |
|-|-|-|
| `var` |  | |
| `default` |  | |
| `required` |  | |
| `artifact_query` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactQuery]` | Specify this to bind to a query instead of a constant. |
| `artifact_id` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID]` | When you want to bind to a known artifact pointer. |

### Properties

| Property | Type | Description |
|-|-|-|
| `artifact_id` | `None` |  |
| `artifact_query` | `None` |  |
| `behavior` | `None` | :rtype: T |
| `default` | `None` | This is the default literal value that will be applied for this parameter if not user specified. :rtype: flytekit.models.literals.Literal |
| `is_empty` | `None` |  |
| `required` | `None` | If True, this parameter must be specified.  There cannot be a default value. :rtype: bool |
| `var` | `None` | The variable definition for this input parameter. :rtype: Variable |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.core.interface_pb2.Parameter


## flytekit.models.interface.ParameterMap

```python
class ParameterMap(
    parameters,
)
```
A map of Parameters


| Parameter | Type | Description |
|-|-|-|
| `parameters` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `parameters` | `None` | :rtype: dict[Text, Parameter] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: flyteidl.core.interface_pb2.ParameterMap


## flytekit.models.interface.TypedInterface

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

### Properties

| Property | Type | Description |
|-|-|-|
| `inputs` | `None` |  |
| `is_empty` | `None` |  |
| `outputs` | `None` |  |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
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

## flytekit.models.interface.Variable

```python
class Variable(
    type,
    description,
    artifact_partial_id: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID],
    artifact_tag: typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag],
)
```
| Parameter | Type | Description |
|-|-|-|
| `type` |  | |
| `description` |  | |
| `artifact_partial_id` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactID]` | Optional Artifact object to control how the artifact is created when the task runs. |
| `artifact_tag` | `typing.Optional[flyteidl.core.artifact_id_pb2.ArtifactTag]` | Optional ArtifactTag object to automatically tag things. |

### Properties

| Property | Type | Description |
|-|-|-|
| `artifact_partial_id` | `None` |  |
| `artifact_tag` | `None` |  |
| `description` | `None` | This is a help string that can provide context for what this variable means in relation to a task or workflow. :rtype: Text |
| `is_empty` | `None` |  |
| `type` | `None` | This describes the type of value that must be provided to satisfy this variable. :rtype: flytekit.models.types.LiteralType |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |
| [`to_flyte_idl_list()`](#to_flyte_idl_list) | :rtype: flyteidl. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    variable_proto,
) -> flyteidl.core.interface_pb2.Variable
```
| Parameter | Type | Description |
|-|-|-|
| `variable_proto` |  | |

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
:rtype: flyteidl.core.interface_pb2.Variable


#### to_flyte_idl_list()

```python
def to_flyte_idl_list()
```
:rtype: flyteidl.core.interface_pb2.Variable


## flytekit.models.interface.VariableMap

```python
class VariableMap(
    variables,
)
```
A map of Variables



| Parameter | Type | Description |
|-|-|-|
| `variables` |  | |

### Properties

| Property | Type | Description |
|-|-|-|
| `is_empty` | `None` |  |
| `variables` | `None` | :rtype: dict[Text, Variable] |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: dict[Text, Variable]. |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2_object` |  | |

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
:rtype: dict[Text, Variable]


