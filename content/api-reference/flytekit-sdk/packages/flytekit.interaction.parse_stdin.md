---
title: flytekit.interaction.parse_stdin
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interaction.parse_stdin

## Directory

### Methods

| Method | Description |
|-|-|
| [`parse_stdin_to_literal()`](#parse_stdin_to_literal) | Parses the user input from stdin and converts it to a literal of the given type. |


## Methods

#### parse_stdin_to_literal()

```python
def parse_stdin_to_literal(
    ctx: FlyteContext,
    t: typing.Type,
    message: typing.Optional[str],
    lt: typing.Optional[LiteralType],
) -> Literal
```
Parses the user input from stdin and converts it to a literal of the given type.


| Parameter | Type |
|-|-|
| `ctx` | `FlyteContext` |
| `t` | `typing.Type` |
| `message` | `typing.Optional[str]` |
| `lt` | `typing.Optional[LiteralType]` |

