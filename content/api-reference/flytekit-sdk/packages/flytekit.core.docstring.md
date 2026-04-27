---
title: flytekit.core.docstring
version: 1.16.19
variants: +flyte +union
layout: py_api
---

# flytekit.core.docstring

## Directory

### Classes

| Class | Description |
|-|-|
| [`Docstring`](.././flytekit.core.docstring#flytekitcoredocstringdocstring) |  |

## flytekit.core.docstring.Docstring

### Parameters

```python
class Docstring(
    docstring: typing.Optional[str],
    callable_: typing.Optional[typing.Callable],
)
```
| Parameter | Type | Description |
|-|-|-|
| `docstring` | `typing.Optional[str]` | |
| `callable_` | `typing.Optional[typing.Callable]` | |

### Properties

| Property | Type | Description |
|-|-|-|
| `input_descriptions` | `typing.Dict[str, str]` |  |
| `long_description` | `typing.Optional[str]` |  |
| `output_descriptions` | `typing.Dict[str, str]` |  |
| `short_description` | `typing.Optional[str]` |  |

