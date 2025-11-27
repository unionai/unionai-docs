---
title: flytekit.core.interface
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.interface

## Directory

### Classes

| Class | Description |
|-|-|
| [`Interface`](../flytekit.core.interface/interface) | A Python native interface object, like inspect. |

### Methods

| Method | Description |
|-|-|
| [`default_output_name()`](#default_output_name) |  |
| [`detect_artifact()`](#detect_artifact) | If the user wishes to control how Artifacts are created (i. |
| [`extract_return_annotation()`](#extract_return_annotation) | The purpose of this function is to sort out whether a function is returning one thing, or multiple things, and to. |
| [`output_name_generator()`](#output_name_generator) |  |
| [`remap_shared_output_descriptions()`](#remap_shared_output_descriptions) | Deals with mixed styles of return value descriptions used in docstrings. |
| [`repr_kv()`](#repr_kv) |  |
| [`repr_type_signature()`](#repr_type_signature) | Converts an inputs and outputs to a type signature. |
| [`transform_function_to_interface()`](#transform_function_to_interface) | From the annotations on a task function that the user should have provided, and the output names they want to use. |
| [`transform_inputs_to_parameters()`](#transform_inputs_to_parameters) | Transforms the given interface (with inputs) to a Parameter Map with defaults set. |
| [`transform_interface_to_list_interface()`](#transform_interface_to_list_interface) | Takes a single task interface and interpolates it to an array interface - to allow performing distributed python map. |
| [`transform_interface_to_typed_interface()`](#transform_interface_to_typed_interface) | Transform the given simple python native interface to FlyteIDL's interface. |
| [`transform_type()`](#transform_type) |  |
| [`transform_types_to_list_of_type()`](#transform_types_to_list_of_type) | Converts unbound inputs into the equivalent (optional) collections. |
| [`transform_variable_map()`](#transform_variable_map) | Given a map of str (names of inputs for instance) to their Python native types, return a map of the name to a. |
| [`verify_outputs_artifact_bindings()`](#verify_outputs_artifact_bindings) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `T` | `TypeVar` |  |

## Methods

#### default_output_name()

```python
def default_output_name(
    index: int,
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `index` | `int` | |

#### detect_artifact()

```python
def detect_artifact(
    ts: typing.Tuple[typing.Any, ...],
) -> Optional[art_id.ArtifactID]
```
If the user wishes to control how Artifacts are created (i.e. naming them, etc.) this is where we pick it up and
store it in the interface.


| Parameter | Type | Description |
|-|-|-|
| `ts` | `typing.Tuple[typing.Any, ...]` | |

#### extract_return_annotation()

```python
def extract_return_annotation(
    return_annotation: Union[Type, Tuple, None],
) -> Dict[str, Type]
```
The purpose of this function is to sort out whether a function is returning one thing, or multiple things, and to
name the outputs accordingly, either by using our default name function, or from a typing.NamedTuple.

    # Option 1
    nt1 = typing.NamedTuple("NT1", x_str=str, y_int=int)
    def t(a: int, b: str) -> nt1: ...

    # Option 2
    def t(a: int, b: str) -> typing.NamedTuple("NT1", x_str=str, y_int=int): ...

    # Option 3
    def t(a: int, b: str) -> typing.Tuple[int, str]: ...

    # Option 4
    def t(a: int, b: str) -> (int, str): ...

    # Option 5
    def t(a: int, b: str) -> str: ...

    # Option 6
    def t(a: int, b: str) -> None: ...

    # Options 7/8
    def t(a: int, b: str) -> List[int]: ...
    def t(a: int, b: str) -> Dict[str, int]: ...

Note that Options 1 and 2 are identical, just syntactic sugar. In the NamedTuple case, we'll use the names in the
definition. In all other cases, we'll automatically generate output names, indexed starting at 0.


| Parameter | Type | Description |
|-|-|-|
| `return_annotation` | `Union[Type, Tuple, None]` | |

#### output_name_generator()

```python
def output_name_generator(
    length: int,
) -> Generator[str, None, None]
```
| Parameter | Type | Description |
|-|-|-|
| `length` | `int` | |

#### remap_shared_output_descriptions()

```python
def remap_shared_output_descriptions(
    output_descriptions: Dict[str, str],
    outputs: Dict[str, Type],
) -> Dict[str, str]
```
Deals with mixed styles of return value descriptions used in docstrings. If the docstring contains a single entry of return value description, that output description is shared by each output variable.


| Parameter | Type | Description |
|-|-|-|
| `output_descriptions` | `Dict[str, str]` | Dict of output variable names mapping to output description |
| `outputs` | `Dict[str, Type]` | Interface outputs :return: Dict of output variable names mapping to shared output description |

#### repr_kv()

```python
def repr_kv(
    k: str,
    v: Union[Type, Tuple[Type, Any]],
) -> str
```
| Parameter | Type | Description |
|-|-|-|
| `k` | `str` | |
| `v` | `Union[Type, Tuple[Type, Any]]` | |

#### repr_type_signature()

```python
def repr_type_signature(
    io: Union[Dict[str, Tuple[Type, Any]], Dict[str, Type]],
) -> str
```
Converts an inputs and outputs to a type signature


| Parameter | Type | Description |
|-|-|-|
| `io` | `Union[Dict[str, Tuple[Type, Any]], Dict[str, Type]]` | |

#### transform_function_to_interface()

```python
def transform_function_to_interface(
    fn: typing.Callable,
    docstring: Optional[Docstring],
    is_reference_entity: bool,
    pickle_untyped: bool,
) -> Interface
```
From the annotations on a task function that the user should have provided, and the output names they want to use
for each output parameter, construct the TypedInterface object

For now the fancy object, maybe in the future a dumb object.


| Parameter | Type | Description |
|-|-|-|
| `fn` | `typing.Callable` | |
| `docstring` | `Optional[Docstring]` | |
| `is_reference_entity` | `bool` | |
| `pickle_untyped` | `bool` | |

#### transform_inputs_to_parameters()

```python
def transform_inputs_to_parameters(
    ctx: context_manager.FlyteContext,
    interface: Interface,
) -> _interface_models.ParameterMap
```
Transforms the given interface (with inputs) to a Parameter Map with defaults set


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `context_manager.FlyteContext` | context |
| `interface` | `Interface` | the interface object |

#### transform_interface_to_list_interface()

```python
def transform_interface_to_list_interface(
    interface: Interface,
    bound_inputs: typing.Set[str],
    excluded_inputs: typing.Set[str],
    optional_outputs: bool,
) -> Interface
```
Takes a single task interface and interpolates it to an array interface - to allow performing distributed python map
like functions


| Parameter | Type | Description |
|-|-|-|
| `interface` | `Interface` | Interface to be upgraded to a list interface |
| `bound_inputs` | `typing.Set[str]` | fixed inputs that should not be updated to a list and will be maintained as is |
| `excluded_inputs` | `typing.Set[str]` | inputs that should be excluded from the interface such as fixed_inputs in a launch_plan |
| `optional_outputs` | `bool` | |

#### transform_interface_to_typed_interface()

```python
def transform_interface_to_typed_interface(
    interface: typing.Optional[Interface],
    allow_partial_artifact_id_binding: bool,
) -> typing.Optional[_interface_models.TypedInterface]
```
Transform the given simple python native interface to FlyteIDL's interface


| Parameter | Type | Description |
|-|-|-|
| `interface` | `typing.Optional[Interface]` | |
| `allow_partial_artifact_id_binding` | `bool` | |

#### transform_type()

```python
def transform_type(
    x: type,
    description: Optional[str],
) -> _interface_models.Variable
```
| Parameter | Type | Description |
|-|-|-|
| `x` | `type` | |
| `description` | `Optional[str]` | |

#### transform_types_to_list_of_type()

```python
def transform_types_to_list_of_type(
    m: Dict[str, type],
    bound_inputs: typing.Set[str],
    list_as_optional: bool,
) -> Dict[str, type]
```
Converts unbound inputs into the equivalent (optional) collections. This is useful for array jobs / map style code.
It will create a collection of types even if any one these types is not a collection type.


| Parameter | Type | Description |
|-|-|-|
| `m` | `Dict[str, type]` | |
| `bound_inputs` | `typing.Set[str]` | |
| `list_as_optional` | `bool` | |

#### transform_variable_map()

```python
def transform_variable_map(
    variable_map: Dict[str, type],
    descriptions: Optional[Dict[str, str]],
) -> Dict[str, _interface_models.Variable]
```
Given a map of str (names of inputs for instance) to their Python native types, return a map of the name to a
Flyte Variable object with that type.


| Parameter | Type | Description |
|-|-|-|
| `variable_map` | `Dict[str, type]` | |
| `descriptions` | `Optional[Dict[str, str]]` | |

#### verify_outputs_artifact_bindings()

```python
def verify_outputs_artifact_bindings(
    inputs: Dict[str, type],
    outputs: Dict[str, _interface_models.Variable],
    allow_partial_artifact_id_binding: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `inputs` | `Dict[str, type]` | |
| `outputs` | `Dict[str, _interface_models.Variable]` | |
| `allow_partial_artifact_id_binding` | `bool` | |

