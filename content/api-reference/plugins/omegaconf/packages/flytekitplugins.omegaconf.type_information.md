---
title: flytekitplugins.omegaconf.type_information
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.omegaconf.type_information

## Directory

### Methods

| Method | Description |
|-|-|
| [`all_annotations()`](#all_annotations) | Returns a dictionary-like ChainMap that includes annotations for all. |
| [`extract_node_type()`](#extract_node_type) | Provides typing information about DictConfig nodes. |
| [`substitute_types()`](#substitute_types) | Provides a substitute type hint to use when selecting transformers for serialisation. |


## Methods

#### all_annotations()

```python
def all_annotations(
    cls: typing.Type,
) -> collections.ChainMap
```
Returns a dictionary-like ChainMap that includes annotations for all
attributes defined in cls or inherited from superclasses.


| Parameter | Type |
|-|-|
| `cls` | `typing.Type` |

#### extract_node_type()

```python
def extract_node_type(
    python_val: typing.Union[omegaconf.dictconfig.DictConfig, omegaconf.listconfig.ListConfig],
    key: typing.Union[str, int],
) -> n:
```
Provides typing information about DictConfig nodes



| Parameter | Type |
|-|-|
| `python_val` | `typing.Union[omegaconf.dictconfig.DictConfig, omegaconf.listconfig.ListConfig]` |
| `key` | `typing.Union[str, int]` |

#### substitute_types()

```python
def substitute_types(
    t: typing.Type,
) -> n: A corrected typehint
```
Provides a substitute type hint to use when selecting transformers for serialisation.



| Parameter | Type |
|-|-|
| `t` | `typing.Type` |

