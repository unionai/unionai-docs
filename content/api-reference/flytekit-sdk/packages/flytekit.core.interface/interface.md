---
title: Interface
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Interface

**Package:** `flytekit.core.interface`

A Python native interface object, like inspect.signature but simpler.



```python
class Interface(
    inputs: Union[Optional[Dict[str, Type]], Optional[Dict[str, Tuple[Type, Any]]]],
    outputs: Union[Optional[Dict[str, Type]], Optional[Dict[str, Optional[Type]]]],
    output_tuple_name: Optional[str],
    docstring: Optional[Docstring],
)
```
| Parameter | Type | Description |
|-|-|-|
| `inputs` | `Union[Optional[Dict[str, Type]], Optional[Dict[str, Tuple[Type, Any]]]]` | Map of input name to either a tuple where the first element is the python type, and the second value is the default, or just a single value which is the python type. The latter case is used by tasks for which perhaps a default value does not make sense. For consistency, we turn it into a tuple. |
| `outputs` | `Union[Optional[Dict[str, Type]], Optional[Dict[str, Optional[Type]]]]` | Output variables and their types as a dictionary |
| `output_tuple_name` | `Optional[str]` | This is used to store the name of a typing.NamedTuple when the task or workflow returns one. This is also used as a proxy for better or for worse for the presence of a tuple return type, primarily used when handling one-element NamedTuples. |
| `docstring` | `Optional[Docstring]` | Docstring of the annotated @task or @workflow from which the interface derives from. |

## Properties

| Property | Type | Description |
|-|-|-|
| `default_inputs_as_kwargs` | `None` |  |
| `docstring` | `None` |  |
| `inputs` | `None` |  |
| `inputs_with_defaults` | `None` |  |
| `output_names` | `None` |  |
| `output_tuple` | `None` |  |
| `output_tuple_name` | `None` |  |
| `outputs` | `None` |  |

## Methods

| Method | Description |
|-|-|
| [`remove_inputs()`](#remove_inputs) | This method is useful in removing some variables from the Flyte backend inputs specification, as these are. |
| [`with_inputs()`](#with_inputs) | Use this to add additional inputs to the interface. |
| [`with_outputs()`](#with_outputs) | This method allows addition of extra outputs are expected from a task specification. |


### remove_inputs()

```python
def remove_inputs(
    vars: Optional[List[str]],
) -> Interface
```
This method is useful in removing some variables from the Flyte backend inputs specification, as these are
implicit local only inputs or will be supplied by the library at runtime. For example, spark-session etc
It creates a new instance of interface with the requested variables removed


| Parameter | Type | Description |
|-|-|-|
| `vars` | `Optional[List[str]]` | |

### with_inputs()

```python
def with_inputs(
    extra_inputs: Dict[str, Type],
) -> Interface
```
Use this to add additional inputs to the interface. This is useful for adding additional implicit inputs that
are added without the user requesting for them


| Parameter | Type | Description |
|-|-|-|
| `extra_inputs` | `Dict[str, Type]` | |

### with_outputs()

```python
def with_outputs(
    extra_outputs: Dict[str, Type],
) -> Interface
```
This method allows addition of extra outputs are expected from a task specification


| Parameter | Type | Description |
|-|-|-|
| `extra_outputs` | `Dict[str, Type]` | |

