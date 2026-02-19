---
title: OutputMetadataTracker
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# OutputMetadataTracker

**Package:** `flytekit.core.context_manager`

This class is for the users to set arbitrary metadata on output literals.

Attributes:
    output_metadata Optional[TaskOutputMetadata]: is a sparse dictionary of metadata that the user wants to attach
        to each output of a task. The key is the output value (object) and the value is an OutputMetadata object.



```python
class OutputMetadataTracker(
    output_metadata: typing.Dict[typing.Any, OutputMetadata],
)
```
| Parameter | Type | Description |
|-|-|-|
| `output_metadata` | `typing.Dict[typing.Any, OutputMetadata]` | |

## Methods

| Method | Description |
|-|-|
| [`add()`](#add) |  |
| [`get()`](#get) |  |
| [`with_params()`](#with_params) | Produces a copy of the current object and set new things. |


### add()

```python
def add(
    obj: typing.Any,
    metadata: OutputMetadata,
)
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `typing.Any` | |
| `metadata` | `OutputMetadata` | |

### get()

```python
def get(
    obj: typing.Any,
) -> Optional[OutputMetadata]
```
| Parameter | Type | Description |
|-|-|-|
| `obj` | `typing.Any` | |

### with_params()

```python
def with_params(
    output_metadata: Optional[TaskOutputMetadata],
) -> OutputMetadataTracker
```
Produces a copy of the current object and set new things


| Parameter | Type | Description |
|-|-|-|
| `output_metadata` | `Optional[TaskOutputMetadata]` | |

