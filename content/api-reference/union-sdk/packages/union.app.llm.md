---
title: union.app.llm
version: 0.1.191
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.app.llm

## Directory

### Classes

| Class | Description |
|-|-|
| [`SGLangApp`](.././union.app.llm#unionappllmsglangapp) | App backed by FastAPI. |
| [`VLLMApp`](.././union.app.llm#unionappllmvllmapp) | App backed by FastAPI. |

### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_SGLANG_IMAGE` | `str` |  |
| `DEFAULT_VLLM_IMAGE` | `str` |  |
| `OPTIMIZED_SGLANG_IMAGE` | `str` |  |
| `OPTIMIZED_VLLM_IMAGE` | `str` |  |

## union.app.llm.SGLangApp

App backed by FastAPI.



```python
class SGLangApp(
    name: str,
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate, NoneType],
    port: int,
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
    extra_args: typing.Union[str, typing.List[str]],
    model: typing.Union[str, flytekit.core.artifact.ArtifactQuery],
    model_id: str,
    stream_model: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate, NoneType]` |
| `port` | `int` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `secrets` | `typing.List[flytekit.models.security.Secret]` |
| `args` | `*args` |
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
| `framework_app` | `typing.Optional[typing.Any]` |
| `dependencies` | `typing.List[ForwardRef('App')]` |
| `config` | `typing.Optional[union.app._models.AppConfigProtocol]` |
| `subdomain` | `typing.Optional[str]` |
| `custom_domain` | `typing.Optional[str]` |
| `links` | `typing.List[union.app._models.Link]` |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` |
| `request_timeout` | `typing.Union[datetime.timedelta, int, NoneType]` |
| `extra_args` | `typing.Union[str, typing.List[str]]` |
| `model` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery]` |
| `model_id` | `str` |
| `stream_model` | `bool` |

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
| `endpoint` |  | {{< multiline >}}Return endpoint for App.
{{< /multiline >}} |
| `include_resolved` |  |  |

## union.app.llm.VLLMApp

App backed by FastAPI.



```python
class VLLMApp(
    name: str,
    container_image: typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate, NoneType],
    port: int,
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
    extra_args: typing.Union[str, typing.List[str]],
    model: typing.Union[str, flytekit.core.artifact.ArtifactQuery],
    model_id: str,
    stream_model: bool,
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate, NoneType]` |
| `port` | `int` |
| `limits` | `typing.Optional[flytekit.core.resources.Resources]` |
| `requests` | `typing.Optional[flytekit.core.resources.Resources]` |
| `secrets` | `typing.List[flytekit.models.security.Secret]` |
| `args` | `*args` |
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
| `framework_app` | `typing.Optional[typing.Any]` |
| `dependencies` | `typing.List[ForwardRef('App')]` |
| `config` | `typing.Optional[union.app._models.AppConfigProtocol]` |
| `subdomain` | `typing.Optional[str]` |
| `custom_domain` | `typing.Optional[str]` |
| `links` | `typing.List[union.app._models.Link]` |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` |
| `request_timeout` | `typing.Union[datetime.timedelta, int, NoneType]` |
| `extra_args` | `typing.Union[str, typing.List[str]]` |
| `model` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery]` |
| `model_id` | `str` |
| `stream_model` | `bool` |

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
| `endpoint` |  | {{< multiline >}}Return endpoint for App.
{{< /multiline >}} |
| `include_resolved` |  |  |

