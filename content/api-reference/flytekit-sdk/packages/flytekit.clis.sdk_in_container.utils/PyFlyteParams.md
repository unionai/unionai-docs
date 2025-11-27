---
title: PyFlyteParams
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# PyFlyteParams

**Package:** `flytekit.clis.sdk_in_container.utils`

```python
class PyFlyteParams(
    config_file: typing.Optional[str],
    verbose: bool,
    pkgs: typing.List[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Optional[str]` | |
| `verbose` | `bool` | |
| `pkgs` | `typing.List[str]` | |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |


### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
) -> PyFlyteParams
```
| Parameter | Type | Description |
|-|-|-|
| `d` | `typing.Dict[str, typing.Any]` | |

