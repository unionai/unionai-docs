---
title: flytekit.core.annotation
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.annotation

## Directory

### Classes

| Class | Description |
|-|-|
| [`Any`](.././flytekit.core.annotation#flytekitcoreannotationany) | Special type indicating an unconstrained type. |
| [`FlyteAnnotation`](.././flytekit.core.annotation#flytekitcoreannotationflyteannotation) | A core object to add arbitrary annotations to flyte types. |

## flytekit.core.annotation.Any

Special type indicating an unconstrained type.

- Any is compatible with every type.
- Any assumed to have all methods.
- All values assumed to be instances of Any.

Note that all the above statements are true from the point of view of
static type checkers. At runtime, Any should not be used with instance
checks.


## flytekit.core.annotation.FlyteAnnotation

A core object to add arbitrary annotations to flyte types.

This metadata is ingested as a python dictionary and will be serialized
into fields on the flyteidl type literals. This data is not accessible at
runtime but rather can be retrieved from flyteadmin for custom presentation
of typed parameters.

Flytekit expects to receive a maximum of one `FlyteAnnotation` object
within each typehint.

For a task definition:

.. code-block:: python

@task
def x(a: typing.Annotated[int, FlyteAnnotation({"foo": {"bar": 1}})]):
return


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

