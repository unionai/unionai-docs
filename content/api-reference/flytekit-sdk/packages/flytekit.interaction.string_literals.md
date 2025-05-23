---
title: flytekit.interaction.string_literals
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interaction.string_literals

## Directory

### Methods

| Method | Description |
|-|-|
| [`literal_map_string_repr()`](#literal_map_string_repr) | This method is used to convert a literal map to a string representation. |
| [`literal_string_repr()`](#literal_string_repr) | This method is used to convert a literal to a string representation. |
| [`primitive_to_string()`](#primitive_to_string) | This method is used to convert a primitive to a string representation. |
| [`scalar_to_string()`](#scalar_to_string) | This method is used to convert a scalar to a string representation. |


## Methods

#### literal_map_string_repr()

```python
def literal_map_string_repr(
    lm: typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, flytekit.models.literals.Literal]],
) -> typing.Dict[str, typing.Any]
```
This method is used to convert a literal map to a string representation.


| Parameter | Type |
|-|-|
| `lm` | `typing.Union[flytekit.models.literals.LiteralMap, typing.Dict[str, flytekit.models.literals.Literal]]` |

#### literal_string_repr()

```python
def literal_string_repr(
    lit: flytekit.models.literals.Literal,
) -> typing.Any
```
This method is used to convert a literal to a string representation. This is useful in places, where we need to
use a shortened string representation of a literal, especially a FlyteFile, FlyteDirectory, or StructuredDataset.


| Parameter | Type |
|-|-|
| `lit` | `flytekit.models.literals.Literal` |

#### primitive_to_string()

```python
def primitive_to_string(
    primitive: flytekit.models.literals.Primitive,
) -> typing.Any
```
This method is used to convert a primitive to a string representation.


| Parameter | Type |
|-|-|
| `primitive` | `flytekit.models.literals.Primitive` |

#### scalar_to_string()

```python
def scalar_to_string(
    scalar: flytekit.models.literals.Scalar,
) -> typing.Any
```
This method is used to convert a scalar to a string representation.


| Parameter | Type |
|-|-|
| `scalar` | `flytekit.models.literals.Scalar` |

