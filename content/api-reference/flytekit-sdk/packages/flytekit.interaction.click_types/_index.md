---
title: flytekit.interaction.click_types
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interaction.click_types

## Directory

### Classes

| Class | Description |
|-|-|
| [`DateTimeType`](../flytekit.interaction.click_types/datetimetype) | The DateTime type converts date strings into `datetime` objects. |
| [`DirParamType`](../flytekit.interaction.click_types/dirparamtype) | Represents the type of a parameter. |
| [`DurationParamType`](../flytekit.interaction.click_types/durationparamtype) | Represents the type of a parameter. |
| [`EnumParamType`](../flytekit.interaction.click_types/enumparamtype) | The choice type allows a value to be checked against a fixed set. |
| [`FileParamType`](../flytekit.interaction.click_types/fileparamtype) | Represents the type of a parameter. |
| [`FlyteLiteralConverter`](../flytekit.interaction.click_types/flyteliteralconverter) |  |
| [`JSONIteratorParamType`](../flytekit.interaction.click_types/jsoniteratorparamtype) | Represents the type of a parameter. |
| [`JsonParamType`](../flytekit.interaction.click_types/jsonparamtype) | Represents the type of a parameter. |
| [`PickleParamType`](../flytekit.interaction.click_types/pickleparamtype) | Represents the type of a parameter. |
| [`StructuredDatasetParamType`](../flytekit.interaction.click_types/structureddatasetparamtype) | TODO handle column types. |
| [`UnionParamType`](../flytekit.interaction.click_types/unionparamtype) | A composite type that allows for multiple types to be specified. |

### Methods

| Method | Description |
|-|-|
| [`is_pydantic_basemodel()`](#is_pydantic_basemodel) | Checks if the python type is a pydantic BaseModel. |
| [`key_value_callback()`](#key_value_callback) | Callback for click to parse key-value pairs. |
| [`labels_callback()`](#labels_callback) | Callback for click to parse labels. |
| [`literal_type_to_click_type()`](#literal_type_to_click_type) | Converts a Flyte LiteralType given a python_type to a click. |
| [`modify_literal_uris()`](#modify_literal_uris) | Modifies the literal object recursively to replace the URIs with the native paths. |
| [`resource_callback()`](#resource_callback) | Click callback to parse resource strings like 'cpu=1,mem=2Gi' into a Resources object. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SIMPLE_TYPE_CONVERTER` | `dict` |  |
| `click_version` | `str` |  |

## Methods

#### is_pydantic_basemodel()

```python
def is_pydantic_basemodel(
    python_type: typing.Type,
) -> bool
```
Checks if the python type is a pydantic BaseModel


| Parameter | Type | Description |
|-|-|-|
| `python_type` | `typing.Type` | |

#### key_value_callback()

```python
def key_value_callback(
    _: typing.Any,
    param: str,
    values: typing.List[str],
) -> typing.Optional[typing.Dict[str, str]]
```
Callback for click to parse key-value pairs.


| Parameter | Type | Description |
|-|-|-|
| `_` | `typing.Any` | |
| `param` | `str` | |
| `values` | `typing.List[str]` | |

#### labels_callback()

```python
def labels_callback(
    _: typing.Any,
    param: str,
    values: typing.List[str],
) -> typing.Optional[typing.Dict[str, str]]
```
Callback for click to parse labels.


| Parameter | Type | Description |
|-|-|-|
| `_` | `typing.Any` | |
| `param` | `str` | |
| `values` | `typing.List[str]` | |

#### literal_type_to_click_type()

```python
def literal_type_to_click_type(
    lt: flytekit.models.types.LiteralType,
    python_type: typing.Type,
) -> click.types.ParamType
```
Converts a Flyte LiteralType given a python_type to a click.ParamType


| Parameter | Type | Description |
|-|-|-|
| `lt` | `flytekit.models.types.LiteralType` | |
| `python_type` | `typing.Type` | |

#### modify_literal_uris()

```python
def modify_literal_uris(
    lit: flytekit.models.literals.Literal,
)
```
Modifies the literal object recursively to replace the URIs with the native paths.


| Parameter | Type | Description |
|-|-|-|
| `lit` | `flytekit.models.literals.Literal` | |

#### resource_callback()

```python
def resource_callback(
    _: typing.Any,
    param: str,
    value: typing.Optional[str],
) -> typing.Optional[flytekit.core.resources.Resources]
```
Click callback to parse resource strings like 'cpu=1,mem=2Gi' into a Resources object


| Parameter | Type | Description |
|-|-|-|
| `_` | `typing.Any` | |
| `param` | `str` | |
| `value` | `typing.Optional[str]` | |

