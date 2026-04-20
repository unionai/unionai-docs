---
title: Environment
<<<<<<< HEAD
version: 2.0.11
variants: +flyte +byoc +selfmanaged
=======
version: 2.1.7
variants: +flyte +union
>>>>>>> origin/main
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
    depends_on: List[Environment],
    pod_template: Optional[Union[str, PodTemplate]],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env_vars: Optional[Dict[str, str]],
    resources: Optional[Resources],
    interruptible: bool,
    image: Union[str, Image, Literal['auto'], None],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the environment (required). Must be snake_case or kebab-case. |
| `depends_on` | `List[Environment]` | List of other environments to deploy alongside this one. |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | Kubernetes pod template as a string reference to a named template or a `PodTemplate` object. |
| `description` | `Optional[str]` | Human-readable description (max 255 characters). |
| `secrets` | `Optional[SecretRequest]` | Secrets to inject into the environment. |
| `env_vars` | `Optional[Dict[str, str]]` | Environment variables as `dict[str, str]`. |
| `resources` | `Optional[Resources]` | Compute resources (CPU, memory, GPU, disk) via a `Resources` object. |
| `interruptible` | `bool` | Whether the environment can be scheduled on spot/preemptible instances. |
| `image` | `Union[str, Image, Literal['auto'], None]` | Docker image for the environment. Can be a string (image URI), an `Image` object, or `"auto"` to use the default image. |

## Methods

| Method | Description |
|-|-|
| [`add_dependency()`](#add_dependency) | Add one or more environment dependencies so they are deployed together. |
| [`clone_with()`](#clone_with) |  |


### add_dependency()

```python
def add_dependency(
    env: Environment,
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
| `env` | `Environment` | One or more `Environment` instances to add as dependencies. |

### clone_with()

```python
def clone_with(
    name: str,
    image: Optional[Union[str, Image, Literal['auto']]],
    resources: Optional[Resources],
    env_vars: Optional[Dict[str, str]],
    secrets: Optional[SecretRequest],
    depends_on: Optional[List[Environment]],
    description: Optional[str],
    kwargs: **kwargs,
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
| `kwargs` | `**kwargs` | |

