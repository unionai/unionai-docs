---
title: ActionInputs
version: 2.0.0b52
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# ActionInputs

**Package:** `flyte.remote`

A class representing the inputs of an action. It is used to manage the inputs of a task and its state on the
remote Union API.

ActionInputs extends from a `UserDict` and hence is accessible like a dictionary

Example Usage:
```python
action = Action.get(...)
print(action.inputs())
```
Output:
```bash
{
  "x": ...,
  "y": ...,
}
```


```python
class ActionInputs(
    pb2: common_pb2.Inputs,
    data: Dict[str, Any],
)
```
| Parameter | Type | Description |
|-|-|-|
| `pb2` | `common_pb2.Inputs` | |
| `data` | `Dict[str, Any]` | |

## Methods

| Method | Description |
|-|-|
| [`clear()`](#clear) | D. |
| [`copy()`](#copy) |  |
| [`fromkeys()`](#fromkeys) |  |
| [`get()`](#get) | D. |
| [`items()`](#items) | D. |
| [`keys()`](#keys) | D. |
| [`pop()`](#pop) | D. |
| [`popitem()`](#popitem) | D. |
| [`setdefault()`](#setdefault) | D. |
| [`to_dict()`](#to_dict) | Convert the object to a JSON-serializable dictionary. |
| [`to_json()`](#to_json) | Convert the object to a JSON string. |
| [`update()`](#update) | D. |
| [`values()`](#values) | D. |


### clear()

```python
def clear()
```
D.clear() -&gt; None.  Remove all items from D.


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
    key,
    default,
)
```
D.get(k[,d]) -&gt; D[k] if k in D, else d.  d defaults to None.


| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `default` |  | |

### items()

```python
def items()
```
D.items() -&gt; a set-like object providing a view on D's items


### keys()

```python
def keys()
```
D.keys() -&gt; a set-like object providing a view on D's keys


### pop()

```python
def pop(
    key,
    default,
)
```
D.pop(k[,d]) -&gt; v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised.


| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `default` |  | |

### popitem()

```python
def popitem()
```
D.popitem() -&gt; (k, v), remove and return some (key, value) pair
as a 2-tuple; but raise KeyError if D is empty.


### setdefault()

```python
def setdefault(
    key,
    default,
)
```
D.setdefault(k[,d]) -&gt; D.get(k,d), also set D[k]=d if k not in D


| Parameter | Type | Description |
|-|-|-|
| `key` |  | |
| `default` |  | |

### to_dict()

```python
def to_dict()
```
Convert the object to a JSON-serializable dictionary.

Returns:
    dict: A dictionary representation of the object.


### to_json()

```python
def to_json()
```
Convert the object to a JSON string.

Returns:
    str: A JSON string representation of the object.


### update()

```python
def update(
    other,
    kwds,
)
```
D.update([E, ]**F) -&gt; None.  Update D from mapping/iterable E and F.
If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k, v in F.items(): D[k] = v


| Parameter | Type | Description |
|-|-|-|
| `other` |  | |
| `kwds` |  | |

### values()

```python
def values()
```
D.values() -&gt; an object providing a view on D's values


