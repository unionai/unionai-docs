---
title: union.app
version: 0.1.202
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
| `name` | `str` | The name of the application. |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate]` | The container image to use for the application. |
| `port` | `typing.Union[int, union.app._models.App.Port, NoneType]` | Port application listens to. Currently, this must be 8080 and the application must listen on 8080. |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` | Compute resource limits for application. |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` | Compute resource requests for application. |
| `secrets` | `typing.List[flytekit.models.security.Secret]` | Secrets that are requested for application. |
| `args` | `*args` | Entrypoint to start application. |
| `command` | `typing.Union[typing.List[str], str, NoneType]` | Command to start application. |
| `min_replicas` | `int` | Minimum number of replicas (ignore if autoscaling is set). |
| `max_replicas` | `int` | Maximum number of replicas (ignore if autoscaling is set). |
| `scaledown_after` | `typing.Union[datetime.timedelta, int, NoneType]` | Time to wait before scaling down a replica after it has been idle. |
| `scaling_metric` | `typing.Union[union.app._models.ScalingMetric.RequestRate, union.app._models.ScalingMetric.Concurrency, NoneType]` | Autoscale based on a parameter, e.g. request rate or concurrency (others may be added in the future). |
| `include` | `typing.List[str]` | Files to include for your application. |
| `inputs` | `typing.List[union.app._models.Input]` | Inputs for the application. |
| `env` | `dict` | Environment variables to set for the application. |
| `cluster_pool` | `str` | The target cluster_pool where the app should be deployed. |
| `accelerator` | `typing.Optional[flytekit.extras.accelerators.BaseAccelerator]` | |
| `requires_auth` | `bool` | Public URL does not require any authentication |
| `type` | `typing.Optional[str]` | Type of app |
| `description` | `typing.Optional[str]` | Description of app |
| `framework_app` | `typing.Optional[typing.Any]` | Object for serving framework. When this is set, all user defined files are uploaded. - For FastAPI, args is set to `uvicorn module_name:app_name --port port`. For more control you can set `args` directly. |
| `dependencies` | `typing.List[ForwardRef('App')]` | List of apps that this app depends on. |
| `config` | `typing.Optional[union.app._models.AppConfigProtocol]` | |
| `subdomain` | `typing.Optional[str]` | Custom subdomain for your app. |
| `custom_domain` | `typing.Optional[str]` | Custom full domain for your app. |
| `links` | `typing.List[union.app._models.Link]` | Links to external URLs or relative paths. |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` | If True, then shared memory will be attached to the container where the size is equal to the allocated memory. If str, then the shared memory is set to that size. |
| `request_timeout` | `typing.Union[datetime.timedelta, int, NoneType]` | Optional timeout for requests to the application. Must not exceed 1 hour. |

### Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` | Return endpoint for App. |
| `include_resolved` | `None` |  |

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

### Properties

| Property | Type | Description |
|-|-|-|
| `endpoint` | `None` | Return endpoint for App. |
| `include_resolved` | `None` |  |

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
| `value` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery, union.app._models.URLQuery]` | Value for input. |
| `name` | `typing.Optional[str]` | Name of input. |
| `env_var` | `typing.Optional[str]` | Environment name to set the value in the serving environment. |
| `type` | `typing.Optional[union.app._models.Input.Type]` | |
| `download` | `bool` | When True, the input will be automatically downloaded. This only works if the value refers to an item in a object store. i.e. `s3://...` |
| `mount` | `typing.Optional[str]` | If `value` is a directory, then the directory will be available at `mount`. If `value` is a file, then the file will be downloaded into the `mount` directory. |
| `ignore_patterns` | `list[str]` | If `value` is a directory, then this is a list of glob patterns to ignore. |

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

