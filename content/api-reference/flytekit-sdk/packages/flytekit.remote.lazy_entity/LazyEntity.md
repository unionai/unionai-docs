---
title: LazyEntity
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# LazyEntity

**Package:** `flytekit.remote.lazy_entity`

Fetches the entity when the entity is called or when the entity is retrieved.
The entity is derived from RemoteEntity so that it behaves exactly like the mimicked entity.


```python
class LazyEntity(
    name: str,
    getter: typing.Callable[[], ~T],
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `getter` | `typing.Callable[[], ~T]` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

## Methods

| Method | Description |
|-|-|
| [`compile()`](#compile) |  |
| [`construct_node_metadata()`](#construct_node_metadata) | Used when constructing the node that encapsulates this task as part of a broader workflow definition. |
| [`entity_fetched()`](#entity_fetched) |  |
| [`execute()`](#execute) |  |
| [`local_execute()`](#local_execute) |  |
| [`local_execution_mode()`](#local_execution_mode) |  |


### compile()

```python
def compile(
    ctx: flytekit.core.context_manager.FlyteContext,
    args,
    kwargs,
)
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### construct_node_metadata()

```python
def construct_node_metadata()
```
Used when constructing the node that encapsulates this task as part of a broader workflow definition.


### entity_fetched()

```python
def entity_fetched()
```
### execute()

```python
def execute(
    kwargs,
) -> typing.Any
```
| Parameter | Type | Description |
|-|-|-|
| `kwargs` | `**kwargs` | |

### local_execute()

```python
def local_execute(
    ctx: flytekit.core.context_manager.FlyteContext,
    kwargs,
) -> typing.Union[typing.Tuple[flytekit.core.promise.Promise], flytekit.core.promise.Promise, flytekit.core.promise.VoidPromise, NoneType]
```
| Parameter | Type | Description |
|-|-|-|
| `ctx` | `flytekit.core.context_manager.FlyteContext` | |
| `kwargs` | `**kwargs` | |

### local_execution_mode()

```python
def local_execution_mode()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `entity` |  | {{< multiline >}}If not already fetched / available, then the entity will be force fetched.
{{< /multiline >}} |
| `id` |  |  |
| `name` |  |  |
| `python_interface` |  |  |

