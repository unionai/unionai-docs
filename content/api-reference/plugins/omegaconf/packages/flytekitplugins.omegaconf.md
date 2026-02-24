---
title: flytekitplugins.omegaconf
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.omegaconf

## Directory

### Classes

| Class | Description |
|-|-|
| [`OmegaConfTransformerMode`](.././flytekitplugins.omegaconf#flytekitpluginsomegaconfomegaconftransformermode) | Operation Mode indicating whether a (potentially unannotated) DictConfig object or a structured config using the. |

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


| Parameter | Type | Description |
|-|-|-|
| `mode` | `<enum 'OmegaConfTransformerMode'>` | |

#### set_transformer_mode()

```python
def set_transformer_mode(
    mode: <enum 'OmegaConfTransformerMode'>,
)
```
Set the global serialization mode for OmegaConf objects.


| Parameter | Type | Description |
|-|-|-|
| `mode` | `<enum 'OmegaConfTransformerMode'>` | |

## flytekitplugins.omegaconf.OmegaConfTransformerMode

Operation Mode indicating whether a (potentially unannotated) DictConfig object or a structured config using the
underlying dataclass is returned.

Note: We define a single shared config across all transformers as recursive calls should refer to the same config
Note: The latter requires the use of structured configs.



