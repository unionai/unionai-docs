---
title: ConnectorEnvironment
version: 2.0.6
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# ConnectorEnvironment

**Package:** `flyte.app`

```python
class ConnectorEnvironment(
    name: str,
    depends_on: List[Environment],
    pod_template: Optional[Union[str, PodTemplate]],
    description: Optional[str],
    secrets: Optional[SecretRequest],
    env_vars: Optional[Dict[str, str]],
    resources: Optional[Resources],
    interruptible: bool,
    image: Union[str, Image, Literal['auto'], None],
    type: str,
    port: int | flyte.app._types.Port,
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
| `type` | `str` | |
| `port` | `int \| flyte.app._types.Port` | |
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

## Methods

| Method | Description |
|-|-|
| [`container_args()`](#container_args) |  |
| [`container_cmd()`](#container_cmd) |  |


### container_args()

```python
def container_args(
    serialize_context: flyte.models.SerializationContext,
) -> typing.List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `flyte.models.SerializationContext` | |

### container_cmd()

```python
def container_cmd(
    serialize_context: flyte.models.SerializationContext,
    parameter_overrides: list[flyte.app._parameter.Parameter] | None,
) -> typing.List[str]
```
| Parameter | Type | Description |
|-|-|-|
| `serialize_context` | `flyte.models.SerializationContext` | |
| `parameter_overrides` | `list[flyte.app._parameter.Parameter] \| None` | |

