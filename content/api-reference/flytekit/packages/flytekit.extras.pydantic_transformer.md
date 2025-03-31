---
title: flytekit.extras.pydantic_transformer
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.extras.pydantic_transformer

## Directory

### Methods

| Method | Description |
|-|-|
| [`model_serializer()`](#model_serializer) | Decorator that enables custom model serialization. |
| [`model_validator()`](#model_validator) | Usage docs: https://docs. |


### Variables

| Property | Type | Description |
|-|-|-|
| `logger` | `Logger` |  |

## Methods

#### model_serializer()

```python
def model_serializer(
    f: _ModelPlainSerializerT | _ModelWrapSerializerT | None,
    mode: Literal['plain', 'wrap'],
    when_used: WhenUsed,
    return_type: Any,
) -> _ModelPlainSerializerT | Callable[[_ModelWrapSerializerT], _ModelWrapSerializerT] | Callable[[_ModelPlainSerializerT], _ModelPlainSerializerT]
```
Decorator that enables custom model serialization.

This is useful when a model need to be serialized in a customized manner, allowing for flexibility beyond just specific fields.

An example would be to serialize temperature to the same temperature scale, such as degrees Celsius.

```python
from typing import Literal

from pydantic import BaseModel, model_serializer

class TemperatureModel(BaseModel):
unit: Literal['C', 'F']
value: int

@model_serializer()
def serialize_model(self):
if self.unit == 'F':
return {'unit': 'C', 'value': int((self.value - 32) / 1.8)}
return {'unit': self.unit, 'value': self.value}

temperature = TemperatureModel(unit='F', value=212)
print(temperature.model_dump())
#> {'unit': 'C', 'value': 100}
```

Two signatures are supported for `mode='plain'`, which is the default:

- `(self)`
- `(self, info: SerializationInfo)`

And two other signatures for `mode='wrap'`:

- `(self, nxt: SerializerFunctionWrapHandler)`
- `(self, nxt: SerializerFunctionWrapHandler, info: SerializationInfo)`

See [Custom serializers](../concepts/serialization.md#custom-serializers) for more information.



| Parameter | Type |
|-|-|
| `f` | `_ModelPlainSerializerT \| _ModelWrapSerializerT \| None` |
| `mode` | `Literal['plain', 'wrap']` |
| `when_used` | `WhenUsed` |
| `return_type` | `Any` |

#### model_validator()

```python
def model_validator(
    mode: Literal['wrap', 'before', 'after'],
) -> Any
```
Usage docs: https://docs.pydantic.dev/2.10/concepts/validators/#model-validators

Decorate model methods for validation purposes.

Example usage:
```python
from typing_extensions import Self

from pydantic import BaseModel, ValidationError, model_validator

class Square(BaseModel):
width: float
height: float

@model_validator(mode='after')
def verify_square(self) -> Self:
if self.width != self.height:
raise ValueError('width and height do not match')
return self

s = Square(width=1, height=1)
print(repr(s))
#> Square(width=1.0, height=1.0)

try:
Square(width=1, height=2)
except ValidationError as e:
print(e)
'''
1 validation error for Square
Value error, width and height do not match [type=value_error, input_value={'width': 1, 'height': 2}, input_type=dict]
'''
```

For more in depth examples, see [Model Validators](../concepts/validators.md#model-validators).



| Parameter | Type |
|-|-|
| `mode` | `Literal['wrap', 'before', 'after']` |

