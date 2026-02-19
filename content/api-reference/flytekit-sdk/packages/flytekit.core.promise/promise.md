---
title: Promise
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Promise

**Package:** `flytekit.core.promise`

This object is a wrapper and exists for three main reasons. Let's assume we're dealing with a task like ::

    @task
    def t1() -&gt; (int, str): ...

#. Handling the duality between compilation and local execution - when the task function is run in a local execution
   mode inside a workflow function, a Python integer and string are produced. When the task is being compiled as
   part of the workflow, the task call creates a Node instead, and the task returns two Promise objects that
   point to that Node.
#. One needs to be able to call ::

      x = t1().with_overrides(...)

   If the task returns an integer or a ``(int, str)`` tuple like ``t1`` above, calling ``with_overrides`` on the
   result would throw an error. This Promise object adds that.
#. Assorted handling for conditionals.



```python
class Promise(
    var: str,
    val: Union[NodeOutput, _literals_models.Literal],
    type: typing.Optional[_type_models.LiteralType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `var` | `str` | |
| `val` | `Union[NodeOutput, _literals_models.Literal]` | |
| `type` | `typing.Optional[_type_models.LiteralType]` | |

## Properties

| Property | Type | Description |
|-|-|-|
| `attr_path` | `None` | The attribute path the promise will be resolved with. :rtype: List[Union[str, int]] |
| `is_ready` | `None` | Returns if the Promise is READY (is not a reference and the val is actually ready)  Usage ::     p = Promise(...)    ...    if p.is_ready():         print(p.val)    else:         print(p.ref) |
| `ref` | `None` | If the promise is NOT READY / Incomplete, then it maps to the origin node that owns the promise |
| `val` | `None` | If the promise is ready then this holds the actual evaluate value in Flyte's type system |
| `var` | `None` | Name of the variable bound with this promise |

## Methods

| Method | Description |
|-|-|
| [`deepcopy()`](#deepcopy) |  |
| [`eval()`](#eval) |  |
| [`is_()`](#is_) |  |
| [`is_false()`](#is_false) |  |
| [`is_none()`](#is_none) |  |
| [`is_true()`](#is_true) |  |
| [`with_overrides()`](#with_overrides) |  |
| [`with_var()`](#with_var) |  |


### deepcopy()

```python
def deepcopy()
```
### eval()

```python
def eval()
```
### is_()

```python
def is_(
    v: bool,
) -> ComparisonExpression
```
| Parameter | Type | Description |
|-|-|-|
| `v` | `bool` | |

### is_false()

```python
def is_false()
```
### is_none()

```python
def is_none()
```
### is_true()

```python
def is_true()
```
### with_overrides()

```python
def with_overrides(
    node_name: Optional[str],
    aliases: Optional[Dict[str, str]],
    requests: Optional[Resources],
    limits: Optional[Resources],
    timeout: Optional[Union[int, datetime.timedelta, object]],
    retries: Optional[int],
    interruptible: Optional[bool],
    name: Optional[str],
    task_config: Optional[Any],
    container_image: Optional[str],
    accelerator: Optional[BaseAccelerator],
    cache: Optional[Union[bool, Cache]],
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `node_name` | `Optional[str]` | |
| `aliases` | `Optional[Dict[str, str]]` | |
| `requests` | `Optional[Resources]` | |
| `limits` | `Optional[Resources]` | |
| `timeout` | `Optional[Union[int, datetime.timedelta, object]]` | |
| `retries` | `Optional[int]` | |
| `interruptible` | `Optional[bool]` | |
| `name` | `Optional[str]` | |
| `task_config` | `Optional[Any]` | |
| `container_image` | `Optional[str]` | |
| `accelerator` | `Optional[BaseAccelerator]` | |
| `cache` | `Optional[Union[bool, Cache]]` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### with_var()

```python
def with_var(
    new_var: str,
) -> Promise
```
| Parameter | Type | Description |
|-|-|-|
| `new_var` | `str` | |

