---
title: flytekit.core.docstring
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.docstring

## Directory

### Classes

| Class | Description |
|-|-|
| [`Docstring`](.././flytekit.core.docstring#flytekitcoredocstringdocstring) |  |

### Methods

| Method | Description |
|-|-|
| [`parse()`](#parse) | Parse the docstring into its components. |


## Methods

#### parse()

```python
def parse(
    text: str,
    style: <enum 'DocstringStyle'>,
) -> docstring_parser.common.Docstring
```
Parse the docstring into its components.



| Parameter | Type |
|-|-|
| `text` | `str` |
| `style` | `<enum 'DocstringStyle'>` |

## flytekit.core.docstring.Docstring

```python
class Docstring(
    docstring: typing.Optional[str],
    callable_: typing.Optional[typing.Callable],
)
```
| Parameter | Type |
|-|-|
| `docstring` | `typing.Optional[str]` |
| `callable_` | `typing.Optional[typing.Callable]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `input_descriptions` |  |  |
| `long_description` |  |  |
| `output_descriptions` |  |  |
| `short_description` |  |  |

