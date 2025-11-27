---
title: FlyteABCMeta
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteABCMeta

**Package:** `flytekit.models.common`

Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC.  An ABC can be subclassed
directly, and then acts as a mix-in class.  You can also register
unrelated concrete classes (even built-in classes) and unrelated
ABCs as 'virtual subclasses' -- these and their descendants will
be considered subclasses of the registering ABC by the built-in
issubclass() function, but the registering ABC won't show up in
their MRO (Method Resolution Order) nor will method
implementations defined by the registering ABC be callable (not
even via super()).


## Methods

| Method | Description |
|-|-|
| [`register()`](#register) | Register a virtual subclass of an ABC. |


### register()

```python
def register(
    cls,
    subclass,
)
```
Register a virtual subclass of an ABC.

Returns the subclass, to allow usage as a class decorator.


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `subclass` |  | |

