---
title: flytekit.core.annotation
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.annotation

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlyteAnnotation`](.././flytekit.core.annotation#flytekitcoreannotationflyteannotation) | A core object to add arbitrary annotations to flyte types. |

## flytekit.core.annotation.FlyteAnnotation

A core object to add arbitrary annotations to flyte types.

This metadata is ingested as a python dictionary and will be serialized
into fields on the flyteidl type literals. This data is not accessible at
runtime but rather can be retrieved from flyteadmin for custom presentation
of typed parameters.

Flytekit expects to receive a maximum of one `FlyteAnnotation` object
within each typehint.

For a task definition:

```python
@task
def x(a: typing.Annotated[int, FlyteAnnotation({"foo": {"bar": 1}})]):
    return
```


```python
class FlyteAnnotation(
    data: typing.Dict[str, typing.Any],
)
```
| Parameter | Type |
|-|-|
| `data` | `typing.Dict[str, typing.Any]` |

### Properties

| Property | Type | Description |
|-|-|-|
| `data` |  |  |

