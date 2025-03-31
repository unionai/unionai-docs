---
title: flytekit.interaction.parse_stdin
version: 0.1.dev2184+g1e0cbe7
variants: +flyte +byoc +byok +serverless
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

