---
title: FlyteAnnotation
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteAnnotation

**Package:** `flytekit.core.annotation`

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
| Parameter | Type | Description |
|-|-|-|
| `data` | `typing.Dict[str, typing.Any]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `data` | `None` |  |

