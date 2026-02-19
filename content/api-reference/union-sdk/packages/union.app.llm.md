---
title: union.app.llm
version: 0.1.201
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
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the application. |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate, NoneType]` | The container image to use for the application. |
| `port` | `int` | Port application listens to. |
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
| `type` | `str` | Type of app |
| `description` | `typing.Optional[str]` | Description of app |
| `framework_app` | `typing.Optional[typing.Any]` | |
| `dependencies` | `typing.List[ForwardRef('App')]` | |
| `config` | `typing.Optional[union.app._models.AppConfigProtocol]` | |
| `subdomain` | `typing.Optional[str]` | Custom subdomain for your app. |
| `custom_domain` | `typing.Optional[str]` | Custom full domain for your app. |
| `links` | `typing.List[union.app._models.Link]` | |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` | |
| `request_timeout` | `typing.Union[datetime.timedelta, int, NoneType]` | |
| `extra_args` | `typing.Union[str, typing.List[str]]` | Extra args to pass to `python -m sglang.launch_server`. See https://docs.sglang.ai/backend/server_arguments.html for details. |
| `model` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery]` | Artifact URI for model. - If `str`, it should start with `flyte://`. - Use `ArtifactQuery` to dynamically query an artifact. |
| `model_id` | `str` | model id that is exposed by vllm. |
| `stream_model` | `bool` | Set to True to stream model from blob store to the GPU directly. If False, the model will be downloaded to the local file system first and then loaded into the GPU. |

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
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the application. |
| `container_image` | `typing.Union[str, flytekit.image_spec.image_spec.ImageSpec, flytekit.core.pod_template.PodTemplate, NoneType]` | The container image to use for the application. |
| `port` | `int` | Port application listens to. Currently, this must be 8080 and the application must listen on 8080. |
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
| `type` | `str` | Type of app |
| `description` | `typing.Optional[str]` | Description of app |
| `framework_app` | `typing.Optional[typing.Any]` | |
| `dependencies` | `typing.List[ForwardRef('App')]` | |
| `config` | `typing.Optional[union.app._models.AppConfigProtocol]` | |
| `subdomain` | `typing.Optional[str]` | Custom subdomain for your app. |
| `custom_domain` | `typing.Optional[str]` | Custom full domain for your app. |
| `links` | `typing.List[union.app._models.Link]` | |
| `shared_memory` | `typing.Union[typing.Literal[True], str, NoneType]` | If True, then shared memory will be attached to the container where the size is equal to the allocated memory. If str, then the shared memory is set to that size. |
| `request_timeout` | `typing.Union[datetime.timedelta, int, NoneType]` | |
| `extra_args` | `typing.Union[str, typing.List[str]]` | Extra args to pass to `vllm serve`. See https://docs.vllm.ai/en/stable/serving/engine_args.html or run `vllm serve --help` for details. |
| `model` | `typing.Union[str, flytekit.core.artifact.ArtifactQuery]` | Artifact URI for model. - If `str`, it should start with `flyte://`. - Use `ArtifactQuery` to dynamically query an artifact. |
| `model_id` | `str` | model id that is exposed by vllm. |
| `stream_model` | `bool` | Set to True to stream model from blob store to the GPU directly. If False, the model will be downloaded to the local file system first and then loaded into the GPU. |

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

