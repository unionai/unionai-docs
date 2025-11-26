---
title: NativeInterface
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# NativeInterface

**Package:** `flyte.models`

A class representing the native interface for a task. This is used to interact with the task and its execution
context.


```python
class NativeInterface(
    inputs: Dict[str, Tuple[Type, Any]],
    outputs: Dict[str, Type],
    docstring: Optional[Docstring],
    _remote_defaults: Optional[Dict[str, literals_pb2.Literal]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `inputs` | `Dict[str, Tuple[Type, Any]]` | |
| `outputs` | `Dict[str, Type]` | |
| `docstring` | `Optional[Docstring]` | |
| `_remote_defaults` | `Optional[Dict[str, literals_pb2.Literal]]` | |

## Methods

| Method | Description |
|-|-|
| [`convert_to_kwargs()`](#convert_to_kwargs) | Convert the given arguments to keyword arguments based on the native interface. |
| [`from_callable()`](#from_callable) | Extract the native interface from the given function. |
| [`from_types()`](#from_types) | Create a new NativeInterface from the given types. |
| [`get_input_types()`](#get_input_types) | Get the input types for the task. |
| [`has_outputs()`](#has_outputs) | Check if the task has outputs. |
| [`num_required_inputs()`](#num_required_inputs) | Get the number of required inputs for the task. |
| [`required_inputs()`](#required_inputs) | Get the names of the required inputs for the task. |


### convert_to_kwargs()

```python
def convert_to_kwargs(
    args,
    kwargs,
) -> Dict[str, Any]
```
Convert the given arguments to keyword arguments based on the native interface. This is used to convert the
arguments to the correct types for the task execution.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### from_callable()

```python
def from_callable(
    func: Callable,
) -> NativeInterface
```
Extract the native interface from the given function. This is used to create a native interface for the task.


| Parameter | Type | Description |
|-|-|-|
| `func` | `Callable` | |

### from_types()

```python
def from_types(
    inputs: Dict[str, Tuple[Type, Type[_has_default] | Type[inspect._empty]]],
    outputs: Dict[str, Type],
    default_inputs: Optional[Dict[str, literals_pb2.Literal]],
) -> NativeInterface
```
Create a new NativeInterface from the given types. This is used to create a native interface for the task.


| Parameter | Type | Description |
|-|-|-|
| `inputs` | `Dict[str, Tuple[Type, Type[_has_default] \| Type[inspect._empty]]]` | A dictionary of input names and their types and a value indicating if they have a default value. |
| `outputs` | `Dict[str, Type]` | A dictionary of output names and their types. |
| `default_inputs` | `Optional[Dict[str, literals_pb2.Literal]]` | Optional dictionary of default inputs for remote tasks. :return: A NativeInterface object with the given inputs and outputs. |

### get_input_types()

```python
def get_input_types()
```
Get the input types for the task. This is used to get the types of the inputs for the task execution.


### has_outputs()

```python
def has_outputs()
```
Check if the task has outputs. This is used to determine if the task has outputs or not.


### num_required_inputs()

```python
def num_required_inputs()
```
Get the number of required inputs for the task. This is used to determine how many inputs are required for the
task execution.


### required_inputs()

```python
def required_inputs()
```
Get the names of the required inputs for the task. This is used to determine which inputs are required for the
task execution.
:return: A list of required input names.


