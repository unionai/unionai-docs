---
title: ArtifactValue
description: "Use a published artifact as an app parameter value."
icon: braces
version: 2.6.10
variants: +flyte +union
layout: py_api
---

# ArtifactValue

**Package:** `flyte.app`

Use a published artifact as an app parameter value.

The artifact is resolved from the artifact service at deployment time and
materializes to the File or Dir it stores — the type is inferred from the
artifact itself — so an app can mount e.g. a prefetched model directly:

```python
Parameter(
    name="model",
    value=ArtifactValue(name="bert-small"),
    mount="/models/bert-small",
)
```



## Parameters

```python
class ArtifactValue(
    type: typing.Optional[typing.Literal['string', 'file', 'directory', 'app_endpoint']] = None,
    name: str,
    version: str | None = None,
    project: str | None = None,
    domain: str | None = None,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `type` | `typing.Optional[typing.Literal['string', 'file', 'directory', 'app_endpoint']]` | Optional declared type ('file' or 'directory'). When set, materialization fails if the artifact stores something else; when omitted, the type is inferred. |
| `name` | `str` | The artifact name. |
| `version` | `str \| None` | The artifact version; None resolves the latest version at deploy time. |
| `project` | `str \| None` | Project to look in; defaults to the init configuration. |
| `domain` | `str \| None` | Domain to look in; defaults to the init configuration. |

## Properties

| Property | Type | Description |
|-|-|-|
| `resolved_version_id` | `None` | The exact artifact version this resolved to, or None before materialization. |

## Methods

| Method | Description |
|-|-|
| [`check_type()`](#check_type) |  |
| [`get()`](#get) |  |
| [`materialize()`](#materialize) |  |
| [`model_post_init()`](#model_post_init) | This function is meant to behave like a BaseModel method to initialize private attributes. |


### check_type()

```python
def check_type(
    data: typing.Any,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Any` | |

### get()

```python
def get()
```
### materialize()

```python
def materialize()
```
### model_post_init()

```python
def model_post_init(
    context: Any,
)
```
This function is meant to behave like a BaseModel method to initialize private attributes.

It takes context as an argument since that's what pydantic-core passes when calling it.



| Parameter | Type | Description |
|-|-|-|
| `context` | `Any` | The context. |

