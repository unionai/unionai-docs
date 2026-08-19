---
title: Environment
version: 2.6.2
variants: +flyte +union
layout: py_api
---

# Environment

**Package:** `flyte`

Base class for execution environments, shared by `TaskEnvironment` and
`AppEnvironment`. Defines common infrastructure settings such as container
image, compute resources, secrets, and deployment dependencies.

You typically don't instantiate `Environment` directly — use
`TaskEnvironment` for tasks or `AppEnvironment` for long-running apps.



## Parameters

```python
class Environment(
    name: str,
    depends_on: List[Environment] = <factory>,
    pod_template: Optional[Union[str, PodTemplate]] = None,
    description: Optional[str] = None,
    secrets: Optional[SecretRequest] = None,
    env_vars: Optional[Dict[str, str]] = None,
    resources: Optional[Resources] = None,
    interruptible: bool = False,
    image: Union[str, Image, Literal['auto'], None] = 'auto',
    include: Tuple[str, ...] = <factory>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the environment (required). Must be snake_case or kebab-case. |
| `depends_on` | `List[Environment]` | List of other environments to deploy alongside this one. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Kubernetes pod template as a string reference to a named template or a `PodTemplate` object. To set a termination grace period without depending on the `kubernetes` package, use `flyte.PodTemplate().with_termination_grace_period(...)`. |
| `description` | `Optional[str]` | Human-readable description (max 255 characters). |
| `secrets` | `Optional[SecretRequest]` | Secrets to inject into the environment. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables as `dict[str, str]`. |
| `resources` | `Optional[Resources]` | Compute resources (CPU, memory, GPU, disk) via a `Resources` object. |
| `interruptible` | `bool` | Whether the environment can be scheduled on spot/preemptible instances. |
| `image` | `Union[str, Image, Literal['auto'], None]` | Docker image for the environment. Can be a string (image URI), an `Image` object, or `"auto"` to use the default image. |
| `include` | `Tuple[str, ...]` | Extra files to bundle with the environment's code (e.g., HTML templates, config files, non-Python assets). Paths may be relative (resolved against the directory of the file where the environment is instantiated), absolute, directories (recursively included), or glob patterns. Files listed here are bundled **in addition to** the default `copy_style` discovery (`loaded_modules` or `all`), not in place of it. |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`clone_with()`](#clone_with) |  |


### add_dependency()

```python
def add_dependency(
    *env: Environment,
)
```
Add one or more environment dependencies so they are deployed together.

When you deploy this environment, any environments added via
`add_dependency` will also be deployed. This is an alternative to
passing `depends_on=[...]` at construction time, useful when the
dependency is defined after the environment is created.

Duplicate dependencies are silently ignored. An environment cannot
depend on itself.



| Parameter | Type | Description |
|-|-|-|
| `*env` | `Environment` | One or more `Environment` instances to add as dependencies. |

### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]] = None,
    resources: Optional[Resources] = None,
    env_vars: Optional[Dict[str, str]] = None,
    secrets: Optional[SecretRequest] = None,
    depends_on: Optional[List[Environment]] = None,
    description: Optional[str] = None,
    **kwargs: Any,
) -> Environment
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `image` | `Optional[Union[str, Image, Literal['auto']]]` | |
| `resources` | `Optional[Resources]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `depends_on` | `Optional[List[Environment]]` | |
| `description` | `Optional[str]` | |
| `**kwargs` | `Any` | |

