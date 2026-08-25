---
title: Metadata
version: 2.6.6
variants: +flyte +union
layout: py_api
---

# Metadata

**Package:** `flyte.artifacts`

Structured metadata for Flyte artifacts.


## Parameters

```python
class Metadata(
    name: str,
    version: Optional[str] = None,
    description: Optional[str] = None,
    attrs: Optional[typing.Mapping[str, str]] = None,
    card: Optional[Card] = None,
    kind: Optional[Kind] = None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `version` | `Optional[str]` | |
| `description` | `Optional[str]` | |
| `attrs` | `Optional[typing.Mapping[str, str]]` | |
| `card` | `Optional[Card]` | |
| `kind` | `Optional[Kind]` | |

## Methods

| Method | Description |
|-|-|
| [`create_model_metadata()`](#create_model_metadata) | Helper method to create ModelMetadata. |


### create_model_metadata()

```python
def create_model_metadata(
    name: str,
    version: Optional[str] = None,
    description: Optional[str] = None,
    card: Optional[Card] = None,
    framework: Optional[str] = None,
    model_type: Optional[str] = None,
    architecture: Optional[str] = None,
    task: Optional[str] = None,
    modality: Tuple[str, ...] = ('text',),
    serial_format: str = 'safetensors',
    attrs: Optional[typing.Mapping[str, str]] = None,
) -> Metadata
```
Helper method to create ModelMetadata. This method sets the attrs keys specific to models.
Extra key/values passed via `attrs` are merged in; the model-specific keys win on conflict.

The reserved `kind` key is set to "model" here, so a model is identifiable
without depending on the shape of the key set or on a card being attached.


| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `version` | `Optional[str]` | |
| `description` | `Optional[str]` | |
| `card` | `Optional[Card]` | |
| `framework` | `Optional[str]` | |
| `model_type` | `Optional[str]` | |
| `architecture` | `Optional[str]` | |
| `task` | `Optional[str]` | |
| `modality` | `Tuple[str, ...]` | |
| `serial_format` | `str` | |
| `attrs` | `Optional[typing.Mapping[str, str]]` | |

