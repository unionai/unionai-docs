---
title: flyte
version: 2.0.0
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
sidebar_expanded: true
---

# flyte


Flyte SDK for authoring compound AI applications, services and workflows.

## Directory

### Classes

| Class | Description |
|-|-|
| [`Cache`](../flyte/cache) | Cache configuration for a task. |
| [`Cron`](../flyte/cron) | This class defines a Cron automation that can be associated with a Trigger in Flyte. |
| [`Device`](../flyte/device) | Represents a device type, its quantity and partition if applicable. |
| [`Environment`](../flyte/environment) |  |
| [`FixedRate`](../flyte/fixedrate) | This class defines a FixedRate automation that can be associated with a Trigger in Flyte. |
| [`Image`](../flyte/image) | This is a representation of Container Images, which can be used to create layered images programmatically. |
| [`ImageBuild`](../flyte/imagebuild) | Result of an image build operation. |
| [`PodTemplate`](../flyte/podtemplate) | Custom PodTemplate specification for a Task. |
| [`Resources`](../flyte/resources) | Resources such as CPU, Memory, and GPU that can be allocated to a task. |
| [`RetryStrategy`](../flyte/retrystrategy) | Retry strategy for the task or task environment. |
| [`ReusePolicy`](../flyte/reusepolicy) | ReusePolicy can be used to configure a task to reuse the environment. |
| [`Secret`](../flyte/secret) | Secrets are used to inject sensitive information into tasks or image build context. |
| [`TaskEnvironment`](../flyte/taskenvironment) | Environment class to define a new environment for a set of tasks. |
| [`Timeout`](../flyte/timeout) | Timeout class to define a timeout for a task. |
| [`Trigger`](../flyte/trigger) | This class defines specification of a Trigger, that can be associated with any Flyte V2 task. |

### Protocols

| Protocol | Description |
|-|-|
| [`AppHandle`](../flyte/apphandle) | Protocol defining the common interface between local and remote app handles. |
| [`CachePolicy`](../flyte/cachepolicy) |  |
| [`Link`](../flyte/link) |  |

### Methods

| Method | Description |
|-|-|
| [`AMD_GPU()`](#amd_gpu) | Create an AMD GPU device instance. |
| [`GPU()`](#gpu) | Create a GPU device instance. |
| [`HABANA_GAUDI()`](#habana_gaudi) | Create a Habana Gaudi device instance. |
| [`Neuron()`](#neuron) | Create a Neuron device instance. |
| [`TPU()`](#tpu) | Create a TPU device instance. |
| [`build()`](#build) | Build an image. |
| [`build_images()`](#build_images) | Build the images for the given environments. |
| [`ctx()`](#ctx) | Returns flyte. |
| [`current_domain()`](#current_domain) | Returns the current domain from Runtime environment (on the cluster) or from the initialized configuration. |
| [`current_project()`](#current_project) | Returns the current project from the Runtime environment (on the cluster) or from the initialized configuration. |
| [`custom_context()`](#custom_context) | Synchronous context manager to set input context for tasks spawned within this block. |
| [`deploy()`](#deploy) | Deploy the given environment or list of environments. |
| [`get_custom_context()`](#get_custom_context) | Get the current input context. |
| [`group()`](#group) | Create a new group with the given name. |
| [`init()`](#init) | Initialize the Flyte system with the given configuration. |
| [`init_from_api_key()`](#init_from_api_key) | Initialize the Flyte system using an API key for authentication. |
| [`init_from_config()`](#init_from_config) | Initialize the Flyte system using a configuration file or Config object. |
| [`init_in_cluster()`](#init_in_cluster) |  |
| [`init_passthrough()`](#init_passthrough) | Initialize the Flyte system with passthrough authentication. |
| [`map()`](#map) | Map a function over the provided arguments with concurrent execution. |
| [`run()`](#run) | Run a task with the given parameters. |
| [`serve()`](#serve) | Serve a Flyte app using an AppEnvironment. |
| [`trace()`](#trace) | A decorator that traces function execution with timing information. |
| [`version()`](#version) | Returns the version of the Flyte SDK. |
| [`with_runcontext()`](#with_runcontext) | Launch a new run with the given parameters as the context. |
| [`with_servecontext()`](#with_servecontext) | Create a serve context with custom configuration. |


### Variables

| Property | Type | Description |
|-|-|-|
| `TimeoutType` | `UnionType` |  |
| `TriggerTime` | `_trigger_time` |  |
| `__version__` | `str` |  |
| `logger` | `Logger` |  |

## Methods

#### AMD_GPU()

```python
def AMD_GPU(
    device: typing.Literal['MI100', 'MI210', 'MI250', 'MI250X', 'MI300A', 'MI300X', 'MI325X', 'MI350X', 'MI355X'],
) -> flyte._resources.Device
```
Create an AMD GPU device instance.


| Parameter | Type | Description |
|-|-|-|
| `device` | `typing.Literal['MI100', 'MI210', 'MI250', 'MI250X', 'MI300A', 'MI300X', 'MI325X', 'MI350X', 'MI355X']` | Device type (e.g., "MI100", "MI210", "MI250", "MI250X", "MI300A", "MI300X", "MI325X", "MI350X", "MI355X"). :return: Device instance. |

#### GPU()

```python
def GPU(
    device: typing.Literal['A10', 'A10G', 'A100', 'A100 80G', 'B200', 'H100', 'H200', 'L4', 'L40s', 'T4', 'V100', 'RTX PRO 6000', 'GB10'],
    quantity: typing.Literal[1, 2, 3, 4, 5, 6, 7, 8],
    partition: typing.Union[typing.Literal['1g.5gb', '2g.10gb', '3g.20gb', '4g.20gb', '7g.40gb'], typing.Literal['1g.10gb', '2g.20gb', '3g.40gb', '4g.40gb', '7g.80gb'], typing.Literal['1g.18gb', '1g.35gb', '2g.35gb', '3g.71gb', '4g.71gb', '7g.141gb'], NoneType],
) -> flyte._resources.Device
```
Create a GPU device instance.


| Parameter | Type | Description |
|-|-|-|
| `device` | `typing.Literal['A10', 'A10G', 'A100', 'A100 80G', 'B200', 'H100', 'H200', 'L4', 'L40s', 'T4', 'V100', 'RTX PRO 6000', 'GB10']` | The type of GPU (e.g., "T4", "A100"). |
| `quantity` | `typing.Literal[1, 2, 3, 4, 5, 6, 7, 8]` | The number of GPUs of this type. |
| `partition` | `typing.Union[typing.Literal['1g.5gb', '2g.10gb', '3g.20gb', '4g.20gb', '7g.40gb'], typing.Literal['1g.10gb', '2g.20gb', '3g.40gb', '4g.40gb', '7g.80gb'], typing.Literal['1g.18gb', '1g.35gb', '2g.35gb', '3g.71gb', '4g.71gb', '7g.141gb'], NoneType]` | The partition of the GPU (e.g., "1g.5gb", "2g.10gb" for gpus) or ("1x1", ... for tpus). :return: Device instance. |

#### HABANA_GAUDI()

```python
def HABANA_GAUDI(
    device: typing.Literal['Gaudi1'],
) -> flyte._resources.Device
```
Create a Habana Gaudi device instance.


| Parameter | Type | Description |
|-|-|-|
| `device` | `typing.Literal['Gaudi1']` | Device type (e.g., "Gaudi1"). :return: Device instance. |

#### Neuron()

```python
def Neuron(
    device: typing.Literal['Inf1', 'Inf2', 'Trn1', 'Trn1n', 'Trn2', 'Trn2u'],
) -> flyte._resources.Device
```
Create a Neuron device instance.


| Parameter | Type | Description |
|-|-|-|
| `device` | `typing.Literal['Inf1', 'Inf2', 'Trn1', 'Trn1n', 'Trn2', 'Trn2u']` | Device type (e.g., "Inf1", "Inf2", "Trn1", "Trn1n", "Trn2", "Trn2u"). |

#### TPU()

```python
def TPU(
    device: typing.Literal['V5P', 'V6E'],
    partition: typing.Union[typing.Literal['2x2x1', '2x2x2', '2x4x4', '4x4x4', '4x4x8', '4x8x8', '8x8x8', '8x8x16', '8x16x16', '16x16x16', '16x16x24'], typing.Literal['1x1', '2x2', '2x4', '4x4', '4x8', '8x8', '8x16', '16x16'], NoneType],
)
```
Create a TPU device instance.


| Parameter | Type | Description |
|-|-|-|
| `device` | `typing.Literal['V5P', 'V6E']` | Device type (e.g., "V5P", "V6E"). |
| `partition` | `typing.Union[typing.Literal['2x2x1', '2x2x2', '2x4x4', '4x4x4', '4x4x8', '4x8x8', '8x8x8', '8x8x16', '8x16x16', '16x16x16', '16x16x24'], typing.Literal['1x1', '2x2', '2x4', '4x4', '4x8', '8x8', '8x16', '16x16'], NoneType]` | Partition of the TPU (e.g., "1x1", "2x2", ...). :return: Device instance. |

#### build()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await build.aio()`.
```python
def build(
    image: Image,
    dry_run: bool,
    force: bool,
    wait: bool,
) -> ImageBuild
```
Build an image. The existing async context will be used.



| Parameter | Type | Description |
|-|-|-|
| `image` | `Image` | The image(s) to build. |
| `dry_run` | `bool` | Tell the builder to not actually build. Different builders will have different behaviors. |
| `force` | `bool` | Skip the existence check. Normally if the image already exists we won't build it. |
| `wait` | `bool` | Wait for the build to finish. If wait is False, the function will return immediately and the build will run in the background. |

#### build_images()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await build_images.aio()`.
```python
def build_images(
    envs: Environment,
) -> ImageCache
```
Build the images for the given environments.


| Parameter | Type | Description |
|-|-|-|
| `envs` | `Environment` | Environment to build images for. :return: ImageCache containing the built images. |

#### ctx()

```python
def ctx()
```
Returns flyte.models.TaskContext if within a task context, else None
Note: Only use this in task code and not module level.


#### current_domain()

```python
def current_domain()
```
Returns the current domain from Runtime environment (on the cluster) or from the initialized configuration.
This is safe to be used during `deploy`, `run` and within `task` code.

NOTE: This will not work if you deploy a task to a domain and then run it in another domain.

Raises InitializationError if the configuration is not initialized or domain is not set.
:return: The current domain


#### current_project()

```python
def current_project()
```
Returns the current project from the Runtime environment (on the cluster) or from the initialized configuration.
This is safe to be used during `deploy`, `run` and within `task` code.

NOTE: This will not work if you deploy a task to a project and then run it in another project.

Raises InitializationError if the configuration is not initialized or project is not set.
:return: The current project


#### custom_context()

```python
def custom_context(
    context: str,
)
```
Synchronous context manager to set input context for tasks spawned within this block.

Example:
```python
import flyte

env = flyte.TaskEnvironment(name="...")

@env.task
def t1():
    ctx = flyte.get_custom_context()
    print(ctx)

@env.task
def main():
    # context can be passed via a context manager
    with flyte.custom_context(project="my-project"):
        t1()  # will have {'project': 'my-project'} as context
```



| Parameter | Type | Description |
|-|-|-|
| `context` | `str` | Key-value pairs to set as input context |

#### deploy()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await deploy.aio()`.
```python
def deploy(
    envs: Environment,
    dryrun: bool,
    version: str | None,
    interactive_mode: bool | None,
    copy_style: CopyFiles,
) -> List[Deployment]
```
Deploy the given environment or list of environments.


| Parameter | Type | Description |
|-|-|-|
| `envs` | `Environment` | Environment or list of environments to deploy. |
| `dryrun` | `bool` | dryrun mode, if True, the deployment will not be applied to the control plane. |
| `version` | `str \| None` | version of the deployment, if None, the version will be computed from the code bundle. TODO: Support for interactive_mode |
| `interactive_mode` | `bool \| None` | Optional, can be forced to True or False. If not provided, it will be set based on the current environment. For example Jupyter notebooks are considered interactive mode, while scripts are not. This is used to determine how the code bundle is created. |
| `copy_style` | `CopyFiles` | Copy style to use when running the task  :return: Deployment object containing the deployed environments and tasks. |

#### get_custom_context()

```python
def get_custom_context()
```
Get the current input context. This can be used within a task to retrieve
context metadata that was passed to the action.

Context will automatically propagate to sub-actions.

Example:
```python
import flyte

env = flyte.TaskEnvironment(name="...")

@env.task
def t1():
    # context can be retrieved with `get_custom_context`
    ctx = flyte.get_custom_context()
    print(ctx)  # {'project': '...', 'entity': '...'}
```

:return: Dictionary of context key-value pairs


#### group()

```python
def group(
    name: str,
)
```
Create a new group with the given name. The method is intended to be used as a context manager.

Example:
```python
@task
async def my_task():
    ...
    with group("my_group"):
        t1(x,y)  # tasks in this block will be grouped under "my_group"
    ...
```



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | The name of the group |

#### init()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await init.aio()`.
```python
def init(
    org: str | None,
    project: str | None,
    domain: str | None,
    root_dir: Path | None,
    log_level: int | None,
    log_format: LogFormat | None,
    reset_root_logger: bool,
    endpoint: str | None,
    headless: bool,
    insecure: bool,
    insecure_skip_verify: bool,
    ca_cert_file_path: str | None,
    auth_type: AuthType,
    command: List[str] | None,
    proxy_command: List[str] | None,
    api_key: str | None,
    client_id: str | None,
    client_credentials_secret: str | None,
    auth_client_config: ClientConfig | None,
    rpc_retries: int,
    http_proxy_url: str | None,
    storage: Storage | None,
    batch_size: int,
    image_builder: ImageBuildEngine.ImageBuilderType,
    images: typing.Dict[str, str] | None,
    source_config_path: Optional[Path],
    sync_local_sys_paths: bool,
    load_plugin_type_transformers: bool,
    local_persistence: bool,
)
```
Initialize the Flyte system with the given configuration. This method should be called before any other Flyte
remote API methods are called. Thread-safe implementation.



| Parameter | Type | Description |
|-|-|-|
| `org` | `str \| None` | Optional organization override for the client. Should be set by auth instead. |
| `project` | `str \| None` | Optional project name (not used in this implementation) |
| `domain` | `str \| None` | Optional domain name (not used in this implementation) |
| `root_dir` | `Path \| None` | Optional root directory from which to determine how to load files, and find paths to files. This is useful for determining the root directory for the current project, and for locating files like config etc. also use to determine all the code that needs to be copied to the remote location. defaults to the editable install directory if the cwd is in a Python editable install, else just the cwd. |
| `log_level` | `int \| None` | Optional logging level for the logger, default is set using the default initialization policies |
| `log_format` | `LogFormat \| None` | Optional logging format for the logger, default is "console" |
| `reset_root_logger` | `bool` | By default, we clear out root logger handlers and set up our own. |
| `endpoint` | `str \| None` | Optional API endpoint URL |
| `headless` | `bool` | Optional Whether to run in headless mode |
| `insecure` | `bool` | insecure flag for the client |
| `insecure_skip_verify` | `bool` | Whether to skip SSL certificate verification |
| `ca_cert_file_path` | `str \| None` | [optional] str Root Cert to be loaded and used to verify admin |
| `auth_type` | `AuthType` | The authentication type to use (Pkce, ClientSecret, ExternalCommand, DeviceFlow) |
| `command` | `List[str] \| None` | This command is executed to return a token using an external process |
| `proxy_command` | `List[str] \| None` | This command is executed to return a token for proxy authorization using an external process |
| `api_key` | `str \| None` | Optional API key for authentication |
| `client_id` | `str \| None` | This is the public identifier for the app which handles authorization for a Flyte deployment. More details here: https://www.oauth.com/oauth2-servers/client-registration/client-id-secret/. |
| `client_credentials_secret` | `str \| None` | Used for service auth, which is automatically called during pyflyte. This will allow the Flyte engine to read the password directly from the environment variable. Note that this is less secure! Please only use this if mounting the secret as a file is impossible |
| `auth_client_config` | `ClientConfig \| None` | Optional client configuration for authentication |
| `rpc_retries` | `int` | [optional] int Number of times to retry the platform calls |
| `http_proxy_url` | `str \| None` | [optional] HTTP Proxy to be used for OAuth requests |
| `storage` | `Storage \| None` | Optional blob store (S3, GCS, Azure) configuration if needed to access (i.e. using Minio) |
| `batch_size` | `int` | Optional batch size for operations that use listings, defaults to 1000, so limit larger than batch_size will be split into multiple requests. |
| `image_builder` | `ImageBuildEngine.ImageBuilderType` | Optional image builder configuration, if not provided, the default image builder will be used. |
| `images` | `typing.Dict[str, str] \| None` | Optional dict of images that can be used by referencing the image name. |
| `source_config_path` | `Optional[Path]` | Optional path to the source configuration file (This is only used for documentation) |
| `sync_local_sys_paths` | `bool` | Whether to include and synchronize local sys.path entries under the root directory into the remote container (default: True). |
| `load_plugin_type_transformers` | `bool` | If enabled (default True), load the type transformer plugins registered under the "flyte.plugins.types" entry point group. |
| `local_persistence` | `bool` | Whether to enable SQLite persistence for local run metadata (default :return: None |

#### init_from_api_key()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await init_from_api_key.aio()`.
```python
def init_from_api_key(
    api_key: str | None,
    project: str | None,
    domain: str | None,
    root_dir: Path | None,
    log_level: int | None,
    log_format: LogFormat | None,
    storage: Storage | None,
    batch_size: int,
    image_builder: ImageBuildEngine.ImageBuilderType,
    images: typing.Dict[str, str] | None,
    sync_local_sys_paths: bool,
)
```
Initialize the Flyte system using an API key for authentication. This is a convenience
method for API key-based authentication. Thread-safe implementation.

The API key should be an encoded API key that contains the endpoint, client ID, client secret,
and organization information. You can obtain this encoded API key from your Flyte administrator
or cloud provider.



| Parameter | Type | Description |
|-|-|-|
| `api_key` | `str \| None` | Optional encoded API key for authentication. If None, reads from FLYTE_API_KEY environment variable. The API key is a base64-encoded string containing endpoint, client_id, client_secret, and org information. |
| `project` | `str \| None` | Optional project name |
| `domain` | `str \| None` | Optional domain name |
| `root_dir` | `Path \| None` | Optional root directory from which to determine how to load files, and find paths to files. defaults to the editable install directory if the cwd is in a Python editable install, else just the cwd. |
| `log_level` | `int \| None` | Optional logging level for the logger |
| `log_format` | `LogFormat \| None` | Optional logging format for the logger, default is "console" |
| `storage` | `Storage \| None` | Optional blob store (S3, GCS, Azure) configuration |
| `batch_size` | `int` | Optional batch size for operations that use listings, defaults to 1000 |
| `image_builder` | `ImageBuildEngine.ImageBuilderType` | Optional image builder configuration |
| `images` | `typing.Dict[str, str] \| None` | Optional dict of images that can be used by referencing the image name |
| `sync_local_sys_paths` | `bool` | Whether to include and synchronize local sys.path entries under the root directory into the remote container (default: True) :return: None |

#### init_from_config()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await init_from_config.aio()`.
```python
def init_from_config(
    path_or_config: str | Path | Config | None,
    root_dir: Path | None,
    log_level: int | None,
    log_format: LogFormat,
    project: str | None,
    domain: str | None,
    storage: Storage | None,
    batch_size: int,
    image_builder: ImageBuildEngine.ImageBuilderType | None,
    images: tuple[str, ...] | None,
    sync_local_sys_paths: bool,
)
```
Initialize the Flyte system using a configuration file or Config object. This method should be called before any
other Flyte remote API methods are called. Thread-safe implementation.



| Parameter | Type | Description |
|-|-|-|
| `path_or_config` | `str \| Path \| Config \| None` | Path to the configuration file or Config object |
| `root_dir` | `Path \| None` | Optional root directory from which to determine how to load files, and find paths to files like config etc. For example if one uses the copy-style=="all", it is essential to determine the root directory for the current project. If not provided, it defaults to the editable install directory or if not available, the current working directory. |
| `log_level` | `int \| None` | Optional logging level for the framework logger, default is set using the default initialization policies |
| `log_format` | `LogFormat` | Optional logging format for the logger, default is "console" |
| `project` | `str \| None` | Project name, this will override any project names in the configuration file |
| `domain` | `str \| None` | Domain name, this will override any domain names in the configuration file |
| `storage` | `Storage \| None` | Optional blob store (S3, GCS, Azure) configuration if needed to access (i.e. using Minio) |
| `batch_size` | `int` | Optional batch size for operations that use listings, defaults to 1000 |
| `image_builder` | `ImageBuildEngine.ImageBuilderType \| None` | Optional image builder configuration, if provided, will override any defaults set in the configuration. :return: None |
| `images` | `tuple[str, ...] \| None` | List of image strings in format "imagename=imageuri" or just "imageuri". |
| `sync_local_sys_paths` | `bool` | Whether to include and synchronize local sys.path entries under the root directory into the remote container (default: True). |

#### init_in_cluster()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await init_in_cluster.aio()`.
```python
def init_in_cluster(
    org: str | None,
    project: str | None,
    domain: str | None,
    api_key: str | None,
    endpoint: str | None,
    insecure: bool,
) -> dict[str, typing.Any]
```
| Parameter | Type | Description |
|-|-|-|
| `org` | `str \| None` | |
| `project` | `str \| None` | |
| `domain` | `str \| None` | |
| `api_key` | `str \| None` | |
| `endpoint` | `str \| None` | |
| `insecure` | `bool` | |

#### init_passthrough()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await init_passthrough.aio()`.
```python
def init_passthrough(
    endpoint: str | None,
    org: str | None,
    project: str | None,
    domain: str | None,
    insecure: bool,
) -> dict[str, typing.Any]
```
Initialize the Flyte system with passthrough authentication.

This authentication mode allows you to pass custom authentication metadata
using the `flyte.remote.auth_metadata()` context manager.

The endpoint is automatically configured from the environment if in a flyte cluster with endpoint injected.



| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str \| None` | Optional API endpoint URL |
| `org` | `str \| None` | Optional organization name |
| `project` | `str \| None` | Optional project name |
| `domain` | `str \| None` | Optional domain name |
| `insecure` | `bool` | Whether to use an insecure channel :return: Dictionary of remote kwargs used for initialization |

#### map()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await flyte.map.aio()`.
```python
def map(
    func: typing.Union[flyte._task.AsyncFunctionTaskTemplate[~P, ~R, ~F], functools.partial[~R]],
    args: *args,
    group_name: str | None,
    concurrency: int,
    return_exceptions: bool,
) -> typing.Iterator[typing.Union[~R, Exception]]
```
Map a function over the provided arguments with concurrent execution.



| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Union[flyte._task.AsyncFunctionTaskTemplate[~P, ~R, ~F], functools.partial[~R]]` | The async function to map. |
| `args` | `*args` | Positional arguments to pass to the function (iterables that will be zipped). |
| `group_name` | `str \| None` | The name of the group for the mapped tasks. |
| `concurrency` | `int` | The maximum number of concurrent tasks to run. If 0, run all tasks concurrently. |
| `return_exceptions` | `bool` | If True, yield exceptions instead of raising them. :return: AsyncIterator yielding results in order. |

#### run()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await run.aio()`.
```python
def run(
    task: TaskTemplate[P, R, F],
    args: *args,
    kwargs: **kwargs,
) -> Run
```
Run a task with the given parameters


| Parameter | Type | Description |
|-|-|-|
| `task` | `TaskTemplate[P, R, F]` | task to run |
| `args` | `*args` | args to pass to the task |
| `kwargs` | `**kwargs` | kwargs to pass to the task :return: Run \| Result of the task |

#### serve()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await serve.aio()`.
```python
def serve(
    app_env: 'AppEnvironment',
) -> AppHandle
```
Serve a Flyte app using an AppEnvironment.

This is the simple, direct way to serve an app. For more control over
deployment settings (env vars, cluster pool, etc.), use with_servecontext().

Example:
```python
import flyte
from flyte.app.extras import FastAPIAppEnvironment

env = FastAPIAppEnvironment(name="my-app", ...)

# Simple serve
app = flyte.serve(env)
print(f"App URL: {app.url}")
```



| Parameter | Type | Description |
|-|-|-|
| `app_env` | `'AppEnvironment'` | The app environment to serve |

#### trace()

```python
def trace(
    func: typing.Callable[..., ~T],
) -> typing.Callable[..., ~T]
```
A decorator that traces function execution with timing information.
Works with regular functions, async functions, and async generators/iterators.


| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Callable[..., ~T]` | |

#### version()

```python
def version()
```
Returns the version of the Flyte SDK.


#### with_runcontext()

```python
def with_runcontext(
    mode: Mode | None,
    name: Optional[str],
    service_account: Optional[str],
    version: Optional[str],
    copy_style: CopyFiles,
    dry_run: bool,
    copy_bundle_to: pathlib.Path | None,
    interactive_mode: bool | None,
    raw_data_path: str | None,
    run_base_dir: str | None,
    overwrite_cache: bool,
    project: str | None,
    domain: str | None,
    env_vars: Dict[str, str] | None,
    labels: Dict[str, str] | None,
    annotations: Dict[str, str] | None,
    interruptible: bool | None,
    log_level: int | None,
    log_format: LogFormat,
    reset_root_logger: bool,
    disable_run_cache: bool,
    queue: Optional[str],
    custom_context: Dict[str, str] | None,
    cache_lookup_scope: CacheLookupScope,
    preserve_original_types: bool,
    _tracker: Any,
) -> _Runner
```
Launch a new run with the given parameters as the context.

Example:
```python
import flyte
env = flyte.TaskEnvironment("example")

@env.task
async def example_task(x: int, y: str) -> str:
    return f"{x} {y}"

if __name__ == "__main__":
    flyte.with_runcontext(name="example_run_id").run(example_task, 1, y="hello")
```



| Parameter | Type | Description |
|-|-|-|
| `mode` | `Mode \| None` | Optional The mode to use for the run, if not provided, it will be computed from flyte.init |
| `name` | `Optional[str]` | Optional The name to use for the run |
| `service_account` | `Optional[str]` | Optional The service account to use for the run context |
| `version` | `Optional[str]` | Optional The version to use for the run, if not provided, it will be computed from the code bundle |
| `copy_style` | `CopyFiles` | Optional The copy style to use for the run context |
| `dry_run` | `bool` | Optional If true, the run will not be executed, but the bundle will be created |
| `copy_bundle_to` | `pathlib.Path \| None` | When dry_run is True, the bundle will be copied to this location if specified |
| `interactive_mode` | `bool \| None` | Optional, can be forced to True or False. If not provided, it will be set based on the current environment. For example Jupyter notebooks are considered interactive mode, while scripts are not. This is used to determine how the code bundle is created. |
| `raw_data_path` | `str \| None` | Use this path to store the raw data for the run for local and remote, and can be used to store raw data in specific locations. |
| `run_base_dir` | `str \| None` | Optional The base directory to use for the run. This is used to store the metadata for the run, that is passed between tasks. |
| `overwrite_cache` | `bool` | Optional If true, the cache will be overwritten for the run |
| `project` | `str \| None` | Optional The project to use for the run |
| `domain` | `str \| None` | Optional The domain to use for the run |
| `env_vars` | `Dict[str, str] \| None` | Optional Environment variables to set for the run |
| `labels` | `Dict[str, str] \| None` | Optional Labels to set for the run |
| `annotations` | `Dict[str, str] \| None` | Optional Annotations to set for the run |
| `interruptible` | `bool \| None` | Optional If true, the run can be scheduled on interruptible instances and false implies that all tasks in the run should only be scheduled on non-interruptible instances. If not specified the original setting on all tasks is retained. |
| `log_level` | `int \| None` | Optional Log level to set for the run. If not provided, it will be set to the default log level set using `flyte.init()` |
| `log_format` | `LogFormat` | Optional Log format to set for the run. If not provided, it will be set to the default log format |
| `reset_root_logger` | `bool` | If true, the root logger will be preserved and not modified by Flyte. |
| `disable_run_cache` | `bool` | Optional If true, the run cache will be disabled. This is useful for testing purposes. |
| `queue` | `Optional[str]` | Optional The queue to use for the run. This is used to specify the cluster to use for the run. |
| `custom_context` | `Dict[str, str] \| None` | Optional global input context to pass to the task. This will be available via get_custom_context() within the task and will automatically propagate to sub-tasks. Acts as base/default values that can be overridden by context managers in the code. |
| `cache_lookup_scope` | `CacheLookupScope` | Optional Scope to use for the run. This is used to specify the scope to use for cache lookups. If not specified, it will be set to the default scope (global unless overridden at the system level). |
| `preserve_original_types` | `bool` | Optional If true, the type engine will preserve original types (e.g., pd.DataFrame) when guessing python types from literal types. If false (default), it will return the generic flyte.io.DataFrame. This option is automatically set to True if interactive_mode is True unless overridden explicitly by this parameter. |
| `_tracker` | `Any` | This is an internal only parameter used by the CLI to render the TUI.  :return: runner |

#### with_servecontext()

```python
def with_servecontext(
    mode: ServeMode | None,
    version: Optional[str],
    copy_style: CopyFiles,
    dry_run: bool,
    project: str | None,
    domain: str | None,
    env_vars: dict[str, str] | None,
    parameter_values: dict[str, dict[str, str | flyte.io.File | flyte.io.Dir]] | None,
    cluster_pool: str | None,
    log_level: int | None,
    log_format: LogFormat,
    interactive_mode: bool | None,
    copy_bundle_to: pathlib.Path | None,
    deactivate_timeout: float | None,
    activate_timeout: float | None,
    health_check_timeout: float | None,
    health_check_interval: float | None,
    health_check_path: str | None,
) -> _Serve
```
Create a serve context with custom configuration.

This function allows you to customize how an app is served, including
overriding environment variables, cluster pool, logging, and other deployment settings.

Use ``mode="local"`` to serve the app on localhost (non-blocking) so you can
immediately invoke tasks that call the app endpoint:

```python
import flyte

local_app = flyte.with_servecontext(mode="local").serve(app_env)
local_app.is_active()  # wait for the server to start
# ... call tasks that use app_env.endpoint ...
local_app.deactivate()
```

Use ``mode="remote"`` (or omit *mode* when a Flyte client is configured) to
deploy the app to the Flyte backend:

```python
app = flyte.with_servecontext(
    env_vars={"DATABASE_URL": "postgresql://..."},
    log_level=logging.DEBUG,
    log_format="json",
    cluster_pool="gpu-pool",
    project="my-project",
    domain="development",
).serve(env)

print(f"App URL: {app.url}")
```



| Parameter | Type | Description |
|-|-|-|
| `mode` | `ServeMode \| None` | "local" to run on localhost, "remote" to deploy to the Flyte backend. When ``None`` the mode is inferred from the current configuration. |
| `version` | `Optional[str]` | Optional version override for the app deployment |
| `copy_style` | `CopyFiles` | |
| `dry_run` | `bool` | |
| `project` | `str \| None` | Optional project override |
| `domain` | `str \| None` | Optional domain override |
| `env_vars` | `dict[str, str] \| None` | Optional environment variables to inject/override in the app container |
| `parameter_values` | `dict[str, dict[str, str \| flyte.io.File \| flyte.io.Dir]] \| None` | Optional parameter values to inject/override in the app container. Must be a dictionary that maps app environment names to a dictionary of parameter names to values. |
| `cluster_pool` | `str \| None` | Optional cluster pool to deploy the app to |
| `log_level` | `int \| None` | Optional log level (e.g., logging.DEBUG, logging.INFO). If not provided, uses init config or default |
| `log_format` | `LogFormat` | |
| `interactive_mode` | `bool \| None` | Optional, can be forced to True or False. If not provided, it will be set based on the current environment. For example Jupyter notebooks are considered interactive mode, while scripts are not. This is used to determine how the code bundle is created. This is used to determine if the app should be served in interactive mode or not. |
| `copy_bundle_to` | `pathlib.Path \| None` | When dry_run is True, the bundle will be copied to this location if specified |
| `deactivate_timeout` | `float \| None` | Timeout in seconds for waiting for the app to stop during ``deactivate(wait=True)``. Defaults to 6 s. |
| `activate_timeout` | `float \| None` | Total timeout in seconds when polling the health-check endpoint during ``activate(wait=True)``. Defaults to 60 s. |
| `health_check_timeout` | `float \| None` | Per-request timeout in seconds for each health-check HTTP request. Defaults to 2 s. |
| `health_check_interval` | `float \| None` | Interval in seconds between consecutive health-check polls. Defaults to 1 s. |
| `health_check_path` | `str \| None` | URL path used for the local health-check probe (e.g. ``"/healthz"``). Defaults to ``"/health"``. |

