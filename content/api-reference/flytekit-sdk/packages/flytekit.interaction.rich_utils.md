---
title: flytekit.interaction.rich_utils
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.interaction.rich_utils

## Directory

### Classes

| Class | Description |
|-|-|
| [`RichCallback`](.././flytekit.interaction.rich_utils#flytekitinteractionrich_utilsrichcallback) |  |

## flytekit.interaction.rich_utils.RichCallback

```python
class RichCallback(
    rich_kwargs: typing.Optional[typing.Dict],
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `rich_kwargs` | `typing.Optional[typing.Dict]` | |
| `kwargs` | `**kwargs` | |

### Methods

| Method | Description |
|-|-|
| [`absolute_update()`](#absolute_update) | Set the internal value state. |
| [`as_callback()`](#as_callback) | Transform callback=. |
| [`branch()`](#branch) | Set callbacks for child transfers. |
| [`branch_coro()`](#branch_coro) | Wraps a coroutine, and pass a new child callback to it. |
| [`branched()`](#branched) | Return callback for child transfers. |
| [`call()`](#call) | Execute hook(s) with current state. |
| [`close()`](#close) | Close callback. |
| [`no_op()`](#no_op) |  |
| [`relative_update()`](#relative_update) | Delta increment the internal counter. |
| [`set_size()`](#set_size) | Set the internal maximum size attribute. |
| [`wrap()`](#wrap) | Wrap an iterable to call ``relative_update`` on each iterations. |


#### absolute_update()

```python
def absolute_update(
    value,
)
```
Set the internal value state

Triggers ``call()``

Parameters
----------
value: int


| Parameter | Type | Description |
|-|-|-|
| `value` |  | |

#### as_callback()

```python
def as_callback(
    maybe_callback,
)
```
Transform callback=... into Callback instance

For the special value of ``None``, return the global instance of
``NoOpCallback``. This is an alternative to including
``callback=DEFAULT_CALLBACK`` directly in a method signature.


| Parameter | Type | Description |
|-|-|-|
| `maybe_callback` |  | |

#### branch()

```python
def branch(
    path_1,
    path_2,
    kwargs,
)
```
Set callbacks for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The passed kwargs are
to be *mutated* to add ``callback=``, if this class supports branching
to children.

Parameters
----------
path_1: str
    Child's source path
path_2: str
    Child's destination path
kwargs: dict
    arguments passed to child method, e.g., put_file.

Returns
-------


| Parameter | Type | Description |
|-|-|-|
| `path_1` |  | |
| `path_2` |  | |
| `kwargs` | `**kwargs` | |

#### branch_coro()

```python
def branch_coro(
    fn,
)
```
Wraps a coroutine, and pass a new child callback to it.


| Parameter | Type | Description |
|-|-|-|
| `fn` |  | |

#### branched()

```python
def branched(
    path_1,
    path_2,
    kwargs,
)
```
Return callback for child transfers

If this callback is operating at a higher level, e.g., put, which may
trigger transfers that can also be monitored. The function returns a callback
that has to be passed to the child method, e.g., put_file,
as `callback=` argument.

The implementation uses `callback.branch` for compatibility.
When implementing callbacks, it is recommended to override this function instead
of `branch` and avoid calling `super().branched(...)`.

Prefer using this function over `branch`.

Parameters
----------
path_1: str
    Child's source path
path_2: str
    Child's destination path
**kwargs:
    Arbitrary keyword arguments

Returns
-------
callback: Callback
    A callback instance to be passed to the child method


| Parameter | Type | Description |
|-|-|-|
| `path_1` |  | |
| `path_2` |  | |
| `kwargs` | `**kwargs` | |

#### call()

```python
def call(
    hook_name,
    kwargs,
)
```
Execute hook(s) with current state

Each function is passed the internal size and current value

Parameters
----------
hook_name: str or None
    If given, execute on this hook
kwargs: passed on to (all) hook(s)


| Parameter | Type | Description |
|-|-|-|
| `hook_name` |  | |
| `kwargs` | `**kwargs` | |

#### close()

```python
def close()
```
Close callback.


#### no_op()

```python
def no_op(
    _,
    __,
)
```
| Parameter | Type | Description |
|-|-|-|
| `_` |  | |
| `__` |  | |

#### relative_update()

```python
def relative_update(
    inc,
)
```
Delta increment the internal counter

Triggers ``call()``

Parameters
----------
inc: int


| Parameter | Type | Description |
|-|-|-|
| `inc` |  | |

#### set_size()

```python
def set_size(
    size,
)
```
Set the internal maximum size attribute

Usually called if not initially set at instantiation. Note that this
triggers a ``call()``.

Parameters
----------
size: int


| Parameter | Type | Description |
|-|-|-|
| `size` |  | |

#### wrap()

```python
def wrap(
    iterable,
)
```
Wrap an iterable to call ``relative_update`` on each iterations

Parameters
----------
iterable: Iterable
    The iterable that is being wrapped


| Parameter | Type | Description |
|-|-|-|
| `iterable` |  | |

