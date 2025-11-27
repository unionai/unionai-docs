---
title: LiteralsResolver
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LiteralsResolver

**Package:** `flytekit.core.type_engine`

LiteralsResolver is a helper class meant primarily for use with the FlyteRemote experience or any other situation
where you might be working with LiteralMaps. This object allows the caller to specify the Python type that should
correspond to an element of the map.


```python
class LiteralsResolver(
    literals: typing.Dict[str, Literal],
    variable_map: Optional[Dict[str, _interface_models.Variable]],
    ctx: Optional[FlyteContext],
)
```
| Parameter | Type | Description |
|-|-|-|
| `literals` | `typing.Dict[str, Literal]` | A Python map of strings to Flyte Literal models. |
| `variable_map` | `Optional[Dict[str, _interface_models.Variable]]` | This map should be basically one side (either input or output) of the Flyte TypedInterface model and is used to guess the Python type through the TypeEngine if a Python type is not specified by the user. TypeEngine guessing is flaky though, so calls to get() should specify the as_type parameter when possible. |
| `ctx` | `Optional[FlyteContext]` | |

## Methods

| Method | Description |
|-|-|
| [`as_python_native()`](#as_python_native) | This should return the native Python representation, compatible with unpacking. |
| [`clear()`](#clear) | D. |
| [`copy()`](#copy) |  |
| [`fromkeys()`](#fromkeys) |  |
| [`get()`](#get) | This will get the ``attr`` value from the Literal map, and invoke the TypeEngine to convert it into a Python. |
| [`get_literal()`](#get_literal) |  |
| [`items()`](#items) | D. |
| [`keys()`](#keys) | D. |
| [`pop()`](#pop) | D. |
| [`popitem()`](#popitem) | D. |
| [`setdefault()`](#setdefault) | D. |
| [`update()`](#update) | D. |
| [`update_type_hints()`](#update_type_hints) |  |
| [`values()`](#values) | D. |


### as_python_native()

```python
def as_python_native(
    python_interface: Interface,
) -> typing.Any
```
This should return the native Python representation, compatible with unpacking.
This function relies on Python interface outputs being ordered correctly.



| Parameter | Type | Description |
|-|-|-|
| `python_interface` | `Interface` | Only outputs are used but easier to pass the whole interface. |

### clear()

```python
def clear()
```
D.clear() -> None.  Remove all items from D.


### copy()

```python
def copy()
```
### fromkeys()

```python
def fromkeys(
    iterable,
    value,
)
```
| Parameter | Type | Description |
|-|-|-|
| `iterable` |  | |
| `value` |  | |

### get()

```python
def get(
    attr: str,
    as_type: Optional[typing.Type],
) -> typing.Any
```
This will get the ``attr`` value from the Literal map, and invoke the TypeEngine to convert it into a Python
native value. A Python type can optionally be supplied. If successful, the native value will be cached and
future calls will return the cached value instead.



| Parameter | Type | Description |
|-|-|-|
| `attr` | `str` | |
| `as_type` | `Optional[typing.Type]` | :return: Python native value from the LiteralMap |

### get_literal()

```python
def get_literal(
    key: str,
) -> Literal
```
| Parameter | Type | Description |
|-|-|-|
| `key` | `str` | |

### items()

```python
def items()
```
D.items() -> a set-like object providing a view on D's items


### keys()

```python
def keys()
```
D.keys() -> a set-like object providing a view on D's keys


### pop()

```python
def pop(
    key,
    default,
)
```
D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `default` |  | |

### popitem()

```python
def popitem()
```
D.popitem() -> (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


### setdefault()

```python
def setdefault(
    key,
    default,
)
```
D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D


| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `default` |  | |

### update()

```python
def update(
    other,
    kwds,
)
```
D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v


| Parameter | Type | Description |
|-|-|-|
| `other` |  | |
| `kwds` |  | |

### update_type_hints()

```python
def update_type_hints(
    type_hints: typing.Dict[str, typing.Type],
)
```
| Parameter | Type | Description |
|-|-|-|
| `type_hints` | `typing.Dict[str, typing.Type]` | |

### values()

```python
def values()
```
D.values() -> an object providing a view on D's values


## Properties

| Property | Type | Description |
|-|-|-|
| `literals` |  |  |
| `native_values` |  |  |
| `variable_map` |  |  |

