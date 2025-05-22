---
title: union.app
version: 0.1.171.dev4+g052020f1.d20250404
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.app

## Directory

### Classes

| Class | Description |
|-|-|
| [`App`](.././union.app#unionappapp) | App specification. |
| [`FlyteConnectorApp`](.././union.app#unionappflyteconnectorapp) | FlyteConnector application specification that inherits from App. |
| [`Input`](.././union.app#unionappinput) | Input for application. |
| [`ScalingMetric`](.././union.app#unionappscalingmetric) |  |
| [`URLQuery`](.././union.app#unionappurlquery) |  |

## union.app.App

App specification.



```python
class App(
    name: str,
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate],
    port: typing.Union[int, union.app._models.App.Port],
    limits: typing.Optional[flytekit.core.resources.Resources],
    requests: typing.Optional[flytekit.core.resources.Resources],
    secrets: typing.List[flytekit.models.security.Secret],
    args: `*args`,
    command: typing.Union[typing.List[str], str, NoneType],
    min_replicas: int,
    max_replicas: int,
    scaledown_after: typing.Union[datetime.timedelta, int, NoneType],
    scaling_metric: typing.Union[union.app._models.ScalingMetric.RequestRate, union.app._models.ScalingMetric.Concurrency, NoneType],
    include: typing.List[str],
    inputs: typing.List[union.app._models.Input],
    env: dict,
    cluster_pool: str,
    accelerator: typing.Optional[flytekit.extras.accelerators.BaseAccelerator],
    requires_auth: bool,
    type: typing.Optional[str],
    description: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate]` |
| `port` | `typing.Union[int, union.app._models.App.Port]` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `secrets` | `typing.List[flytekit.models.security.Secret]` |
| `args` | ``*args`` |
| `command` | `typing.Union[typing.List[str], str, NoneType]` |
| `min_replicas` | `int` |
| `max_replicas` | `int` |
| `scaledown_after` | `typing.Union[datetime.timedelta, int, NoneType]` |
| `scaling_metric` | `typing.Union[union.app._models.ScalingMetric.RequestRate, union.app._models.ScalingMetric.Concurrency, NoneType]` |
| `include` | `typing.List[str]` |
| `inputs` | `typing.List[union.app._models.Input]` |
| `env` | `dict` |
| `cluster_pool` | `str` |
| `accelerator` | `typing.Optional[flytekit.extras.accelerators.BaseAccelerator]` |
| `requires_auth` | `bool` |
| `type` | `typing.Optional[str]` |
| `description` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`query_endpoint()`](#query_endpoint) | Query for endpoint. |


#### query_endpoint()

```python
def query_endpoint(
    public: bool,
) -> union.app._models.URLQuery
```
Query for endpoint.



| Parameter | Type |
|-|-|
| `public` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `include_resolved` |  |  |

## union.app.FlyteConnectorApp

FlyteConnector application specification that inherits from App.


```python
class FlyteConnectorApp(
    name: str,
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate],
    port: typing.Union[int, union.app._models.App.Port],
    limits: typing.Optional[flytekit.core.resources.Resources],
    requests: typing.Optional[flytekit.core.resources.Resources],
    secrets: typing.List[flytekit.models.security.Secret],
    args: `*args`,
    command: typing.Union[typing.List[str], str, NoneType],
    min_replicas: int,
    max_replicas: int,
    scaledown_after: typing.Union[datetime.timedelta, int, NoneType],
    scaling_metric: typing.Union[union.app._models.ScalingMetric.RequestRate, union.app._models.ScalingMetric.Concurrency, NoneType],
    include: typing.List[str],
    inputs: typing.List[union.app._models.Input],
    env: dict,
    cluster_pool: str,
    accelerator: typing.Optional[flytekit.extras.accelerators.BaseAccelerator],
    requires_auth: bool,
    type: str,
    description: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate]` |
| `port` | `typing.Union[int, union.app._models.App.Port]` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `secrets` | `typing.List[flytekit.models.security.Secret]` |
| `args` | ``*args`` |
| `command` | `typing.Union[typing.List[str], str, NoneType]` |
| `min_replicas` | `int` |
| `max_replicas` | `int` |
| `scaledown_after` | `typing.Union[datetime.timedelta, int, NoneType]` |
| `scaling_metric` | `typing.Union[union.app._models.ScalingMetric.RequestRate, union.app._models.ScalingMetric.Concurrency, NoneType]` |
| `include` | `typing.List[str]` |
| `inputs` | `typing.List[union.app._models.Input]` |
| `env` | `dict` |
| `cluster_pool` | `str` |
| `accelerator` | `typing.Optional[flytekit.extras.accelerators.BaseAccelerator]` |
| `requires_auth` | `bool` |
| `type` | `str` |
| `description` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`query_endpoint()`](#query_endpoint) | Query for endpoint. |


#### query_endpoint()

```python
def query_endpoint(
    public: bool,
) -> union.app._models.URLQuery
```
Query for endpoint.



| Parameter | Type |
|-|-|
| `public` | `bool` |

### Properties

| Property | Type | Description |
|-|-|-|
| `include_resolved` |  |  |

## union.app.Input

Input for application.



```python
class Input(
    value: typing.Union[str, flytekit.core.artifact.ArtifactQuery, union.app._models.URLQuery],
    name: typing.Optional[str],
    env_var: typing.Optional[str],
    type: typing.Optional[union.app._models.Input.Type],
    download: bool,
    mount: typing.Optional[str],
    ignore_patterns: list[str],
)
```
| Parameter | Type |
|-|-|
| `value` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery, union.app._models.URLQuery]` |
| `name` | `typing.Optional[str]` |
| `env_var` | `typing.Optional[str]` |
| `type` | `typing.Optional[union.app._models.Input.Type]` |
| `download` | `bool` |
| `mount` | `typing.Optional[str]` |
| `ignore_patterns` | `list[str]` |

## union.app.ScalingMetric

## union.app.URLQuery

```python
class URLQuery(
    name: str,
    public: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `public` | `bool` |

