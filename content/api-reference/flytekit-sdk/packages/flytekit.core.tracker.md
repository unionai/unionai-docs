---
title: flytekit.core.tracker
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.core.tracker

## Directory

### Classes

| Class | Description |
|-|-|
| [`InstanceTrackingMeta`](.././flytekit.core.tracker#flytekitcoretrackerinstancetrackingmeta) | Please see the original class :flytekit. |
| [`TrackedInstance`](.././flytekit.core.tracker#flytekitcoretrackertrackedinstance) | Please see the notes for the metaclass above first. |

### Methods

| Method | Description |
|-|-|
| [`extract_task_module()`](#extract_task_module) | Returns the task-name, absolute module and the string name of the callable. |
| [`get_full_module_path()`](#get_full_module_path) |  |
| [`import_module_from_file()`](#import_module_from_file) |  |
| [`is_functools_wrapped_module_level()`](#is_functools_wrapped_module_level) | Returns true if the function is a functools. |
| [`is_ipython_or_pickle_exists()`](#is_ipython_or_pickle_exists) | Returns true if the code is running in an IPython notebook or if a pickle file exists. |
| [`isnested()`](#isnested) | Returns true if a function is local to another function and is not accessible through a module. |
| [`istestfunction()`](#istestfunction) | Return true if the function is defined in a test module. |


## Methods

#### extract_task_module()

```python
def extract_task_module(
    f: typing.Union[typing.Callable, flytekit.core.tracker.TrackedInstance],
) -> n: [name to use: str, module_name: str, function_name: str, full_path: str]
```
Returns the task-name, absolute module and the string name of the callable.


| Parameter | Type |
|-|-|
| `f` | `typing.Union[typing.Callable, flytekit.core.tracker.TrackedInstance]` |

#### get_full_module_path()

```python
def get_full_module_path(
    mod: module,
    mod_name: str,
) -> str
```
| Parameter | Type |
|-|-|
| `mod` | `module` |
| `mod_name` | `str` |

#### import_module_from_file()

```python
def import_module_from_file(
    module_name,
    file,
)
```
| Parameter | Type |
|-|-|
| `module_name` |  |
| `file` |  |

#### is_functools_wrapped_module_level()

```python
def is_functools_wrapped_module_level(
    func: typing.Callable,
) -> bool
```
Returns true if the function is a functools.wraps-updated function that is defined in the module-level scope.

```python
import functools

def decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*arks, **kwargs)

    return wrapper

@decorator
def foo():
    ...

def define_inner_wrapped_fn():

    @decorator
    def foo_inner(*args, **kwargs):
        return fn(*arks, **kwargs)

    return foo_inner

bar = define_inner_wrapped_fn()

is_functools_wrapped_module_level(foo)  # True
is_functools_wrapped_module_level(bar)  # False
```

In this case, applying this function to ``foo`` returns true because ``foo`` was defined in the module-level scope.
Applying this function to ``bar`` returns false because it's being assigned to ``foo_inner``, which is a
functools-wrapped function but is actually defined in the local scope of ``define_inner_wrapped_fn``.

This works because functools.wraps updates the __name__ and __qualname__ attributes of the wrapper to match the
wrapped function. Since ``define_inner_wrapped_fn`` doesn't update the __qualname__ of ``foo_inner``, the inner
function's __qualname__ won't match its __name__.


| Parameter | Type |
|-|-|
| `func` | `typing.Callable` |

#### is_ipython_or_pickle_exists()

```python
def is_ipython_or_pickle_exists()
```
Returns true if the code is running in an IPython notebook or if a pickle file exists.

We skip module path resolution in both cases due to the following reasons:

1. In an IPython notebook, we cannot resolve the module path in the local file system.
2. When the code is serialized (pickled) and executed in a remote environment, only
   the pickled file exists at PICKLE_FILE_PATH. The remote environment won't have the
   plain python file and module path resolution will fail.

This check ensures we avoid attempting module path resolution in both environments.


#### isnested()

```python
def isnested(
    func: typing.Callable,
) -> bool
```
Returns true if a function is local to another function and is not accessible through a module

This would essentially be any function with a `.<local>.` (defined within a function) e.g.

```python
def foo():
    def foo_inner():
        pass
    pass
```

In the above example `foo_inner` is the local function or a nested function.


| Parameter | Type |
|-|-|
| `func` | `typing.Callable` |

#### istestfunction()

```python
def istestfunction(
    func,
) -> bool
```
Return true if the function is defined in a test module.

A test module has to have `test_` as the prefix or `_test` as the suffix.
False in all other cases.


| Parameter | Type |
|-|-|
| `func` |  |

## flytekit.core.tracker.InstanceTrackingMeta

Please see the original class :flytekit.common.mixins.registerable._InstanceTracker` also and also look
at the tests in the ``tests/flytekit/unit/core/tracker/test_tracking/`` folder to see how it's used.

Basically, this will make instances of classes that use this metaclass aware of the module (the .py file) that
caused the instance to be created. This is useful because it means that we can then (at least try to) find the
variable that the instance was assigned to.


## flytekit.core.tracker.TrackedInstance

Please see the notes for the metaclass above first.

This functionality has two use-cases currently,
* Keep track of naming for non-function ``PythonAutoContainerTasks``.  That is, things like the
  {{< py_class_ref flytekit.extras.sqlite3.task.SQLite3Task >}} task.
* Task resolvers, because task resolvers are instances of {{< py_class_ref flytekit.core.python_auto_container.TaskResolverMixin >}}
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

