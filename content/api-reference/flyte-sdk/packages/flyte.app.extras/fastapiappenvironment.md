---
title: FastAPIAppEnvironment
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# FastAPIAppEnvironment

**Package:** `flyte.app.extras`

```python
class FastAPIAppEnvironment(
    name: str,
    depends_on: List[Environment],
    pod_template: Optional[Union[str, PodTemplate]],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env_vars: Optional[Dict[str, str]],
    resources: Optional[Resources],
    interruptible: bool,
    image: Union[str, Image, Literal['auto'], None],
    port: int | Port,
    args: *args,
    command: Optional[Union[List[str], str]],
    requires_auth: bool,
    scaling: Scaling,
    domain: Domain | None,
    links: List[Link],
    include: List[str],
    parameters: List[Parameter],
    cluster_pool: str,
    timeouts: Timeouts,
    type: str,
    app: fastapi.FastAPI,
    uvicorn_config: uvicorn.Config | None,
    _caller_frame: inspect.FrameInfo | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `depends_on` | `List[Environment]` | |
| `pod_template` | `Optional[Union[str, PodTemplate]]` | |
| `description` | `Optional[str]` | |
| `secrets` | `Optional[SecretRequest]` | |
| `env_vars` | `Optional[Dict[str, str]]` | |
| `resources` | `Optional[Resources]` | |
| `interruptible` | `bool` | |
| `image` | `Union[str, Image, Literal['auto'], None]` | |
| `port` | `int \| Port` | |
| `args` | `*args` | |
| `command` | `Optional[Union[List[str], str]]` | |
| `requires_auth` | `bool` | |
| `scaling` | `Scaling` | |
| `domain` | `Domain \| None` | |
| `links` | `List[Link]` | |
| `include` | `List[str]` | |
| `parameters` | `List[Parameter]` | |
| `cluster_pool` | `str` | |
| `timeouts` | `Timeouts` | |
| `type` | `str` | |
| `app` | `fastapi.FastAPI` | |
| `uvicorn_config` | `uvicorn.Config \| None` | |
| `_caller_frame` | `inspect.FrameInfo \| None` | |

## Methods

| Method | Description |
|-|-|
| [`container_command()`](#container_command) |  |


### container_command()

```python
def container_command(
    serialization_context: SerializationContext,
) -> list[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialization_context` | `SerializationContext` | |

