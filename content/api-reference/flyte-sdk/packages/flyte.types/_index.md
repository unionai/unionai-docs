---
title: flyte.types
version: 2.0.0b53
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte.types


# Flyte Type System

The Flyte type system provides a way to define, transform, and manipulate types in Flyte workflows.
Since the data flowing through Flyte has to often cross process, container and langauge boundaries, the type system
is designed to be serializable to a universal format that can be understood across different environments. This
universal format is based on Protocol Buffers. The types are called LiteralTypes and the runtime
representation of data is called Literals.

The type system includes:
- **TypeEngine**: The core engine that manages type transformations and serialization. This is the main entry point for
  for all the internal type transformations and serialization logic.
- **TypeTransformer**: A class that defines how to transform one type to another. This is extensible
    allowing users to define custom types and transformations.
- **Renderable**: An interface for types that can be rendered as HTML, that can be outputted to a flyte.report.

It is always possible to bypass the type system and use the `FlytePickle` type to serialize any python object
 into a pickle format. The pickle format is not human-readable, but can be passed between flyte tasks that are
 written in python. The Pickled objects cannot be represented in the UI, and may be in-efficient for large datasets.

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlytePickle`](../flyte.types/flytepickle) | This type is only used by flytekit internally. |
| [`TypeEngine`](../flyte.types/typeengine) | Core Extensible TypeEngine of Flytekit. |
| [`TypeTransformer`](../flyte.types/typetransformer) | Base transformer type that should be implemented for every python native type that can be handled by flytekit. |

### Protocols

| Protocol | Description |
|-|-|
| [`Renderable`](../flyte.types/renderable) | Base class for protocol classes. |

### Errors

| Exception | Description |
|-|-|
| [`TypeTransformerFailedError`](../flyte.types/typetransformerfailederror) | Inappropriate argument type. |

### Methods

| Method | Description |
|-|-|
| [`guess_interface()`](#guess_interface) | Returns the interface of the task with guessed types, as types may not be present in current env. |
| [`literal_string_repr()`](#literal_string_repr) | This method is used to convert a literal map to a string representation. |


## Methods

#### guess_interface()

```python
def guess_interface(
    interface: flyteidl2.core.interface_pb2.TypedInterface,
    default_inputs: typing.Optional[typing.Iterable[flyteidl2.task.common_pb2.NamedParameter]],
) -> flyte.models.NativeInterface
```
Returns the interface of the task with guessed types, as types may not be present in current env.


| Parameter | Type | Description |
|-|-|-|
| `interface` | `flyteidl2.core.interface_pb2.TypedInterface` | |
| `default_inputs` | `typing.Optional[typing.Iterable[flyteidl2.task.common_pb2.NamedParameter]]` | |

#### literal_string_repr()

```python
def literal_string_repr(
    lm: typing.Union[flyteidl2.core.literals_pb2.Literal, flyteidl2.task.common_pb2.NamedLiteral, flyteidl2.task.common_pb2.Inputs, flyteidl2.task.common_pb2.Outputs, flyteidl2.core.literals_pb2.LiteralMap, typing.Dict[str, flyteidl2.core.literals_pb2.Literal]],
) -> typing.Dict[str, typing.Any]
```
This method is used to convert a literal map to a string representation.


| Parameter | Type | Description |
|-|-|-|
| `lm` | `typing.Union[flyteidl2.core.literals_pb2.Literal, flyteidl2.task.common_pb2.NamedLiteral, flyteidl2.task.common_pb2.Inputs, flyteidl2.task.common_pb2.Outputs, flyteidl2.core.literals_pb2.LiteralMap, typing.Dict[str, flyteidl2.core.literals_pb2.Literal]]` | |

