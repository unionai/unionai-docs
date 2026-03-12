---
title: SandboxedTaskTemplate
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# SandboxedTaskTemplate

**Package:** `flyte.sandbox`

A task template that executes the function body in a Monty sandbox.

For pure Python functions (no external calls), Monty executes the
entire body without pausing. For functions that call other tasks or
durable operations, ``run_monty_async`` handles async dispatch.



```python
class SandboxedTaskTemplate(
    name: str,
    interface: NativeInterface,
    short_name: str,
    task_type: str,
    task_type_version: int,
    image: Union[str, Image, Literal['auto']] | None,
    resources: Optional[Resources],
    cache: CacheRequest,
    interruptible: bool,
    retries: Union[int, RetryStrategy],
    reusable: Union[ReusePolicy, None],
    docs: Optional[Documentation],
    env_vars: Optional[Dict[str, str]],
    secrets: Optional[SecretRequest],
    timeout: Optional[TimeoutType],
    pod_template: Optional[Union[str, PodTemplate]],
    report: bool,
    queue: Optional[str],
    debuggable: bool,
    parent_env: Optional[weakref.ReferenceType[TaskEnvironment]],
    parent_env_name: Optional[str],
    max_inline_io_bytes: int,
    triggers: Tuple[Trigger, ...],
    links: Tuple[Link, ...],
    _call_as_synchronous: bool,
    func: F,
    plugin_config: Optional[SandboxedConfig],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `interface` | `NativeInterface` | |
| `short_name` | `str` | |
| `task_type` | `str` | |
| `task_type_version` | `int` | |
| `image` | `Union[str, Image, Literal['auto']] \| None` | |
| `resources` | `Optional[Resources]` | |
| `cache` | `CacheRequest` | |
| `interruptible` | `bool` | |
| `retries` | `Union[int, RetryStrategy]` | |
| `reusable` | `Union[ReusePolicy, None]` | |
| `docs` | `Optional[Documentation]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `timeout` | `Optional[TimeoutType]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `report` | `bool` | |
| `queue` | `Optional[str]` | |
| `debuggable` | `bool` | |
| `parent_env` | `Optional[weakref.ReferenceType[TaskEnvironment]]` | |
| `parent_env_name` | `Optional[str]` | |
| `max_inline_io_bytes` | `int` | |
| `triggers` | `Tuple[Trigger, ...]` | |
| `links` | `Tuple[Link, ...]` | |
| `_call_as_synchronous` | `bool` | |
| `func` | `F` | |
| `plugin_config` | `Optional[SandboxedConfig]` | |

## Methods

| Method | Description |
|-|-|
| [`execute()`](#execute) | Execute the function body in a Monty sandbox. |
| [`forward()`](#forward) | Bypass Monty and call the function directly (for local/debug execution). |


### execute()

```python
def execute(
    args,
    kwargs,
) -> Any
```
Execute the function body in a Monty sandbox.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

### forward()

```python
def forward(
    args,
    kwargs,
) -> Any
```
Bypass Monty and call the function directly (for local/debug execution).


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

