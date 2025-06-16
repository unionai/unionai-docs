---
title: flytekit.extras.pydantic_transformer.decorator
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.extras.pydantic_transformer.decorator

## Directory

### Methods

| Method | Description |
|-|-|
| [`model_serializer()`](#model_serializer) | Placeholder decorator for Pydantic model_serializer. |
| [`model_validator()`](#model_validator) | Placeholder decorator for Pydantic model_validator. |


### Variables

| Property | Type | Description |
|-|-|-|
| `FuncType` | `TypeVar` |  |

## Methods

#### model_serializer()

```python
def model_serializer(
    __f: typing.Optional[typing.Callable[..., typing.Any]],
    mode: typing.Literal['plain', 'wrap'],
    when_used: typing.Literal['always', 'unless-none', 'json', 'json-unless-none'],
    return_type: typing.Any,
) -> typing.Callable[[typing.Any], typing.Any]
```
Placeholder decorator for Pydantic model_serializer.


| Parameter | Type |
|-|-|
| `__f` | `typing.Optional[typing.Callable[..., typing.Any]]` |
| `mode` | `typing.Literal['plain', 'wrap']` |
| `when_used` | `typing.Literal['always', 'unless-none', 'json', 'json-unless-none']` |
| `return_type` | `typing.Any` |

#### model_validator()

```python
def model_validator(
    mode: typing.Literal['wrap', 'before', 'after'],
) -> typing.Callable[[typing.Callable[..., typing.Any]], typing.Callable[..., typing.Any]]
```
Placeholder decorator for Pydantic model_validator.


| Parameter | Type |
|-|-|
| `mode` | `typing.Literal['wrap', 'before', 'after']` |

