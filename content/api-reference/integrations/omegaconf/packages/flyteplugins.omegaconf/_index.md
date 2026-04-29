---
title: flyteplugins.omegaconf
version: 2.2.0
variants: +flyte +union
layout: py_api
---

# flyteplugins.omegaconf

OmegaConf DictConfig/ListConfig support for Flyte.
## Directory

### Methods

| Method | Description |
|-|-|
| [`log_yaml()`](#log_yaml) | Append a YAML rendering of an OmegaConf container to a Flyte report tab. |


## Methods

#### log_yaml()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await log_yaml.aio()`.
```python
def log_yaml(
    config: OmegaConfContainer,
    title: str,
    tab: str,
    sort_keys: bool,
    do_flush: bool,
)
```
Append a YAML rendering of an OmegaConf container to a Flyte report tab.


| Parameter | Type | Description |
|-|-|-|
| `config` | `OmegaConfContainer` | |
| `title` | `str` | |
| `tab` | `str` | |
| `sort_keys` | `bool` | |
| `do_flush` | `bool` | |

