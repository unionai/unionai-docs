---
title: union.app
version: 0.1.198
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.app

## Directory

### Classes

| Class | Description |
|-|-|
| [`App`](.././union.app#unionappapp) | App specification. |
| [`ArizeConfig`](.././union.app#unionapparizeconfig) |  |
| [`FlyteConnectorApp`](.././union.app#unionappflyteconnectorapp) | FlyteConnector application specification that inherits from App. |
| [`Input`](.././union.app#unionappinput) | Input for application. |
| [`Link`](.././union.app#unionapplink) |  |
| [`PhoenixConfig`](.././union.app#unionappphoenixconfig) |  |
| [`ScalingMetric`](.././union.app#unionappscalingmetric) |  |
| [`URLQuery`](.././union.app#unionappurlquery) |  |
| [`WeaveConfig`](.././union.app#unionappweaveconfig) |  |

## union.app.App

App specification.



```python
class App(
    name: str,
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate],
    port: typing.Union[int, union.app._models.App.Port, NoneType],
    limits: typing.Optional[flytekit.core.resources.Resources],
    requests: typing.Optional[flytekit.core.resources.Resources],
    secrets: typing.List[flytekit.models.security.Secret],
    args: *args,
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
    framework_app: typing.Optional[typing.Any],
    dependencies: typing.List[ForwardRef('App')],
    config: typing.Optional[union.app._models.AppConfigProtocol],
    subdomain: typing.Optional[str],
    custom_domain: typing.Optional[str],
    links: typing.List[union.app._models.Link],
    shared_memory: typing.Union[typing.Literal[True], str, NoneType],
    request_timeout: typing.Union[datetime.timedelta, int, NoneType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate]` | |
| `port` | `typing.Union[int, union.app._models.App.Port, NoneType]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `secrets` | `typing.List[flytekit.models.security.Secret]` | |
| `args` | `*args` | |
| `command` | `typing.Union[typing.List[str], str, NoneType]` | |
| `min_replicas` | `int` | |
| `max_replicas` | `int` | |
| `scaledown_after` | `typing.Union[datetime.timedelta, int, NoneType]` | |
| `scaling_metric` | `typing.Union[union.app._models.ScalingMetric.RequestRate, union.app._models.ScalingMetric.Concurrency, NoneType]` | |
| `include` | `typing.List[str]` | |
| `inputs` | `typing.List[union.app._models.Input]` | |
| `env` | `dict` | |
| `cluster_pool` | `str` | |
| `accelerator` | `typing.Optional[flytekit.extras.accelerators.BaseAccelerator]` | |
| `requires_auth` | `bool` | |
| `type` | `typing.Optional[str]` | |
| `description` | `typing.Optional[str]` | |
| `framework_app` | `typing.Optional[typing.Any]` | |
| `dependencies` | `typing.List[ForwardRef('App')]` | |
| `config` | `typing.Optional[union.app._models.AppConfigProtocol]` | |
| `subdomain` | `typing.Optional[str]` | |
| `custom_domain` | `typing.Optional[str]` | |
| `links` | `typing.List[union.app._models.Link]` | |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` | |
| `request_timeout` | `typing.Union[datetime.timedelta, int, NoneType]` | |

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



| Parameter | Type | Description |
|-|-|-|
| `public` | `bool` | Whether to return the public or internal endpoint. :returns: Object representing a URL query. |

### Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` |  | {{< multiline >}}Return endpoint for App.
{{< /multiline >}} |
| `include_resolved` |  |  |

## union.app.ArizeConfig

```python
class ArizeConfig(
    endpoint: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |

### Methods

| Method | Description |
|-|-|
| [`before_to_union_idl()`](#before_to_union_idl) | Modify app in place at the beginning of `App. |


#### before_to_union_idl()

```python
def before_to_union_idl(
    app: App,
    settings: union.app._models.AppSerializationSettings,
)
```
Modify app in place at the beginning of `App._to_union_idl`.


| Parameter | Type | Description |
|-|-|-|
| `app` | `App` | |
| `settings` | `union.app._models.AppSerializationSettings` | |

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
    args: *args,
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
    framework_app: typing.Optional[typing.Any],
    dependencies: typing.List[ForwardRef('App')],
    config: typing.Optional[union.app._models.AppConfigProtocol],
    subdomain: typing.Optional[str],
    custom_domain: typing.Optional[str],
    links: typing.List[union.app._models.Link],
    shared_memory: typing.Union[typing.Literal[True], str, NoneType],
    request_timeout: typing.Union[datetime.timedelta, int, NoneType],
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate]` | |
| `port` | `typing.Union[int, union.app._models.App.Port]` | |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `secrets` | `typing.List[flytekit.models.security.Secret]` | |
| `args` | `*args` | |
| `command` | `typing.Union[typing.List[str], str, NoneType]` | |
| `min_replicas` | `int` | |
| `max_replicas` | `int` | |
| `scaledown_after` | `typing.Union[datetime.timedelta, int, NoneType]` | |
| `scaling_metric` | `typing.Union[union.app._models.ScalingMetric.RequestRate, union.app._models.ScalingMetric.Concurrency, NoneType]` | |
| `include` | `typing.List[str]` | |
| `inputs` | `typing.List[union.app._models.Input]` | |
| `env` | `dict` | |
| `cluster_pool` | `str` | |
| `accelerator` | `typing.Optional[flytekit.extras.accelerators.BaseAccelerator]` | |
| `requires_auth` | `bool` | |
| `type` | `str` | |
| `description` | `typing.Optional[str]` | |
| `framework_app` | `typing.Optional[typing.Any]` | |
| `dependencies` | `typing.List[ForwardRef('App')]` | |
| `config` | `typing.Optional[union.app._models.AppConfigProtocol]` | |
| `subdomain` | `typing.Optional[str]` | |
| `custom_domain` | `typing.Optional[str]` | |
| `links` | `typing.List[union.app._models.Link]` | |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` | |
| `request_timeout` | `typing.Union[datetime.timedelta, int, NoneType]` | |

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



| Parameter | Type | Description |
|-|-|-|
| `public` | `bool` | Whether to return the public or internal endpoint. :returns: Object representing a URL query. |

### Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` |  | {{< multiline >}}Return endpoint for App.
{{< /multiline >}} |
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
| Parameter | Type | Description |
|-|-|-|
| `value` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery, union.app._models.URLQuery]` | |
| `name` | `typing.Optional[str]` | |
| `env_var` | `typing.Optional[str]` | |
| `type` | `typing.Optional[union.app._models.Input.Type]` | |
| `download` | `bool` | |
| `mount` | `typing.Optional[str]` | |
| `ignore_patterns` | `list[str]` | |

## union.app.Link

```python
class Link(
    path: str,
    title: str,
    is_relative: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `path` | `str` | |
| `title` | `str` | |
| `is_relative` | `bool` | |

## union.app.PhoenixConfig

```python
class PhoenixConfig(
    endpoint: str,
    project: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |
| `project` | `str` | |

### Methods

| Method | Description |
|-|-|
| [`before_to_union_idl()`](#before_to_union_idl) | Modify app in place at the beginning of `App. |


#### before_to_union_idl()

```python
def before_to_union_idl(
    app: App,
    settings: union.app._models.AppSerializationSettings,
)
```
Modify app in place at the beginning of `App._to_union_idl`.


| Parameter | Type | Description |
|-|-|-|
| `app` | `App` | |
| `settings` | `union.app._models.AppSerializationSettings` | |

## union.app.ScalingMetric

## union.app.URLQuery

```python
class URLQuery(
    name: str,
    public: bool,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | |
| `public` | `bool` | |

## union.app.WeaveConfig

```python
class WeaveConfig(
    project: str,
    entity: str,
    api_host: str,
    host: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `project` | `str` | |
| `entity` | `str` | |
| `api_host` | `str` | |
| `host` | `str` | |

### Methods

| Method | Description |
|-|-|
| [`before_to_union_idl()`](#before_to_union_idl) | Modify app in place at the beginning of `App. |


#### before_to_union_idl()

```python
def before_to_union_idl(
    app: App,
    settings: union.app._models.AppSerializationSettings,
)
```
Modify app in place at the beginning of `App._to_union_idl`.


| Parameter | Type | Description |
|-|-|-|
| `app` | `App` | |
| `settings` | `union.app._models.AppSerializationSettings` | |

