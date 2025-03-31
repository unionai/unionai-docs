---
title: flytekit.core.tracked_abc
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.tracked_abc

## Directory

### Classes

| Class | Description |
|-|-|
| [`ABC`](.././flytekit.core.tracked_abc#flytekitcoretracked_abcabc) | Helper class that provides a standard way to create an ABC using. |
| [`FlyteTrackedABC`](.././flytekit.core.tracked_abc#flytekitcoretracked_abcflytetrackedabc) | This class exists because if you try to inherit from abc. |
| [`TrackedInstance`](.././flytekit.core.tracked_abc#flytekitcoretracked_abctrackedinstance) | Please see the notes for the metaclass above first. |

## flytekit.core.tracked_abc.ABC

Helper class that provides a standard way to create an ABC using
inheritance.


## flytekit.core.tracked_abc.FlyteTrackedABC

This class exists because if you try to inherit from abc.ABC and TrackedInstance by itself, you'll get the
well-known ``TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass
of the metaclasses of all its bases`` error.


### Methods

| Method | Description |
|-|-|
| [`register()`](#register) | Register a virtual subclass of an ABC. |


#### register()

```python
def register(
    cls,
    subclass,
)
```
Register a virtual subclass of an ABC.

Returns the subclass, to allow usage as a class decorator.


| Parameter | Type |
|-|-|
| `cls` |  |
| `subclass` |  |

## flytekit.core.tracked_abc.TrackedInstance

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
:py:class:`flytekit.extras.sqlite3.task.SQLite3Task` task.
* Task resolvers, because task resolvers are instances of :py:class:`flytekit.core.python_auto_container.TaskResolverMixin`
classes, not the classes themselves, which means we need to look on the left hand side of them to see how to
find them at task execution time.


```python
class TrackedInstance(
    args,
    kwargs,
)
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`find_lhs()`](#find_lhs) |  |


#### find_lhs()

```python
def find_lhs()
```
### Properties

| Property | Type | Description |
|-|-|-|
| `instantiated_in` |  |  |
| `lhs` |  |  |
| `location` |  |  |

