---
title: FlagSpec
version: 2.5.6
variants: +flyte +union
layout: py_api
---

# FlagSpec

**Package:** `flyte.extras.shell`

How to render a typed input as a CLI flag in ``{flags.&lt;name&gt;}``.


## Parameters

```python
class FlagSpec(
    flag: str,
    list_mode: listMode,
    separator: str,
    dict_mode: DictMode,
)
```
| Parameter | Type | Description |
|-|-|-|
| `flag` | `str` | |
| `list_mode` | `listMode` | |
| `separator` | `str` | |
| `dict_mode` | `DictMode` | |

## Methods

| Method | Description |
|-|-|
| [`coerce()`](#coerce) |  |


### coerce()

```python
def coerce(
    name: str,
    alias: Union[str, Tuple[str, str], 'FlagSpec', None],
) -> 'FlagSpec'
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `alias` | `Union[str, Tuple[str, str], 'FlagSpec', None]` | |

