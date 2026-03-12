---
title: CodeTaskTemplate
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# CodeTaskTemplate

**Package:** `flyte.sandbox`

A sandboxed task created from a code string rather than a decorated function.

Unlike ``SandboxedTaskTemplate`` (which extracts source from a Python
function), this class accepts pre-transformed source code and an explicit
dict of external functions.  It is constructed via :func:`flyte.sandbox.orchestrator_from_str`.



```python
class CodeTaskTemplate(
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
    _user_source: str,
    _user_input_names: List[str],
    _user_functions: Dict[str, Any],
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
| `_user_source` | `str` | |
| `_user_input_names` | `List[str]` | |
| `_user_functions` | `Dict[str, Any]` | |

## Methods

| Method | Description |
|-|-|
| [`forward()`](#forward) | Not supported — there is no Python function to call directly. |


### forward()

```python
def forward(
    args,
    kwargs,
) -> Any
```
Not supported — there is no Python function to call directly.


| Parameter | Type | Description |
|-|-|-|
| `args` | `*args` | |
| `kwargs` | `**kwargs` | |

