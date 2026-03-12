---
title: AppEndpoint
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# AppEndpoint

**Package:** `flyte.app`

Embed an upstream app's endpoint as an app parameter.

This enables the declaration of an app parameter dependency on a the endpoint of
an upstream app, given by a specific app name. This gives the app access to
the upstream app's endpoint as a public or private url.



```python
class AppEndpoint(
    type: typing.Literal['string'],
    app_name: str,
    public: bool,
)
```
Create a new model by parsing and validating input data from keyword arguments.

Raises [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) if the input data cannot be
validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.


| Parameter | Type | Description |
|-|-|-|
| `type` | `typing.Literal['string']` | |
| `app_name` | `str` | |
| `public` | `bool` | |

## Methods

| Method | Description |
|-|-|
| [`materialize()`](#materialize) | Returns the AppEndpoint object, the endpoint is retrieved at serving time by the fserve executable. |


### materialize()

```python
def materialize()
```
Returns the AppEndpoint object, the endpoint is retrieved at serving time by the fserve executable.


