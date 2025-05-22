---
title: flytekitplugins.omegaconf
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.omegaconf

## Directory

### Methods

| Method | Description |
|-|-|
| [`get_transformer_mode()`](#get_transformer_mode) | Get the global serialization mode for OmegaConf objects. |
| [`local_transformer_mode()`](#local_transformer_mode) | Context manager to set a local serialization mode for OmegaConf objects. |
| [`set_transformer_mode()`](#set_transformer_mode) | Set the global serialization mode for OmegaConf objects. |


## Methods

#### get_transformer_mode()

```python
def get_transformer_mode()
```
Get the global serialization mode for OmegaConf objects.


#### local_transformer_mode()

```python
def local_transformer_mode(
    mode: <enum 'OmegaConfTransformerMode'>,
)
```
Context manager to set a local serialization mode for OmegaConf objects.


| Parameter | Type |
|-|-|
| `mode` | `<enum 'OmegaConfTransformerMode'>` |

#### set_transformer_mode()

```python
def set_transformer_mode(
    mode: <enum 'OmegaConfTransformerMode'>,
)
```
Set the global serialization mode for OmegaConf objects.


| Parameter | Type |
|-|-|
| `mode` | `<enum 'OmegaConfTransformerMode'>` |

