---
title: FlyteLiteralConverter
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteLiteralConverter

**Package:** `flytekit.interaction.click_types`

```python
class FlyteLiteralConverter(
    flyte_ctx: flytekit.core.context_manager.FlyteContext,
    literal_type: flytekit.models.types.LiteralType,
    python_type: typing.Type,
    is_remote: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `flyte_ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `literal_type` | `flytekit.models.types.LiteralType` | |
| `python_type` | `typing.Type` | |
| `is_remote` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`convert()`](#convert) | Convert the value to a Flyte Literal or a python native type. |
| [`is_bool()`](#is_bool) |  |


### convert()

```python
def convert(
    ctx: click.core.Context,
    param: typing.Optional[click.core.Parameter],
    value: typing.Any,
) -> typing.Union[flytekit.models.literals.Literal, typing.Any]
```
Convert the value to a Flyte Literal or a python native type. This is used by click to convert the input.


| Parameter | Type | Description |
|-|-|-|
| `ctx` | `click.core.Context` | |
| `param` | `typing.Optional[click.core.Parameter]` | |
| `value` | `typing.Any` | |

### is_bool()

```python
def is_bool()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `click_type` |  |  |

