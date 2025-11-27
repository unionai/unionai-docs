---
title: FlyteType
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# FlyteType

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
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`register()`](#register) | Register a virtual subclass of an ABC. |
| [`short_class_string()`](#short_class_string) | :rtype: Text. |
| [`verbose_class_string()`](#verbose_class_string) | :rtype: Text. |


### from_flyte_idl()

```python
def from_flyte_idl(
    cls,
    idl_object,
)
```
| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |
| `idl_object` |  | |

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

### short_class_string()

```python
def short_class_string(
    cls,
)
```
:rtype: Text


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |

### verbose_class_string()

```python
def verbose_class_string(
    cls,
)
```
:rtype: Text


| Parameter | Type | Description |
|-|-|-|
| `cls` |  | |

