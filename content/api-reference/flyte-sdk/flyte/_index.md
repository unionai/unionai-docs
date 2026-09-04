---
title: flyte
description: "Flyte SDK for authoring compound AI applications, services and workflows."
icon: box-seam
version: 2.7.0
variants: +flyte +union
layout: py_api
---

# flyte

Flyte SDK for authoring compound AI applications, services and workflows.
## Directory

### Classes

| Class | Description |
|-|-|
| [`AsyncFunctionTaskTemplate`](../flyte/asyncfunctiontasktemplate) | A task template that wraps an asynchronous functions. |
| [`Backoff`](../flyte/backoff) | Exponential backoff policy applied between user retries. |
| [`BaseCheckpoint`](../flyte/basecheckpoint) | Base type for task checkpoint helpers. |
| [`Cache`](../flyte/cache) | Cache configuration for a task. |
| [`Checkpoint`](../flyte/checkpoint) | Checkpoint helper using `flyte.io.File` for all checkpoint blob I/O (load/save, async and sync). |
| [`ConditionWebhook`](../flyte/conditionwebhook) | Webhook configuration for a condition notification. |
| [`Cron`](../flyte/cron) | Cron-based automation schedule for use with `Trigger`. |
| [`Device`](../flyte/device) | Represents a device type, its quantity and partition if applicable. |
| [`Environment`](../flyte/environment) | Base class for execution environments, shared by `TaskEnvironment` and `AppEnvironment`. |
| [`FixedRate`](../flyte/fixedrate) | Fixed-rate (interval-based) automation schedule for use with `Trigger`. |
| [`Image`](../flyte/image) | Container image specification built using a fluent, two-step pattern. |
| [`ImageBuild`](../flyte/imagebuild) | Result of an image build operation. |
| [`OnArtifact`](../flyte/onartifact) | Artifact-based automation for use with `Trigger`: fire a run whenever a new version of the named artifact is created. |
| [`PodTemplate`](../flyte/podtemplate) | Custom PodTemplate specification for a Task. |
| [`Resources`](../flyte/resources) | Resources such as CPU, Memory, and GPU that can be allocated to a task. |
| [`RetryStrategy`](../flyte/retrystrategy) | Retry strategy for a task. |
| [`ReusePolicy`](../flyte/reusepolicy) | Configure a task environment for container reuse across multiple task invocations. |
| [`Secret`](../flyte/secret) | Secrets are used to inject sensitive information into tasks or image build context. |
| [`TaskEnvironment`](../flyte/taskenvironment) | Define an execution environment for a set of tasks. |
| [`TaskTemplate`](../flyte/tasktemplate) | Task template is a template for a task that can be executed. |
| [`Timeout`](../flyte/timeout) | Timeout bounds for a task. |
| [`Trigger`](../flyte/trigger) | Specification for a scheduled trigger that can be associated with any Flyte task. |

### Protocols

| Protocol | Description |
|-|-|
| [`AppHandle`](../flyte/apphandle) | Protocol defining the common interface between local and remote app handles. |
| [`CachePolicy`](../flyte/cachepolicy) | Protocol for custom cache version strategies. |
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
| [`build_images()`](#build_images) | Build the images for the given environment(s). |
| [`ctx()`](#ctx) | Returns the current flyte.models.TaskContext when running inside a task. |
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
| [`is_control_plane_available()`](#is_control_plane_available) | True when this process can submit work to a Flyte control plane — `flyte.run` launches real remote runs whose actions can be inspected, awaited, and replayed (recovered/forked). |
| [`latest_checkpoint()`](#latest_checkpoint) | Return the file under *root* matching *glob_pattern* with the largest `key(path)`, or `None`. |
| [`load_interactive_ctx()`](#load_interactive_ctx) | Restore the task execution context from the config file written by a debug-mode task pod. |
| [`load_plugin_config()`](#load_plugin_config) | Load a plugin config instance from a YAML file. |
| [`map()`](#map) | Map a function over the provided arguments with concurrent execution. |
| [`new_condition()`](#new_condition) | Create a condition that can be awaited in a workflow. |
| [`rerun()`](#rerun) | Re-run a prior run, returning a new `Run`. |
| [`run()`](#run) | Run a task with the given parameters. |
| [`run_python_script()`](#run_python_script) | Package and run a Python script on a remote Flyte cluster. |
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
| `TriggeredArtifact` | `_triggered_artifact` |  |
| `__version__` | `str` |  |
| `logger` | `Logger` |  |
| `system_logger` | `Logger` |  |

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
| `device` | `typing.Literal['MI100', 'MI210', 'MI250', 'MI250X', 'MI300A', 'MI300X', 'MI325X', 'MI350X', 'MI355X']` | Device type (e.g., "MI100", "MI210", "MI250", "MI250X", "MI300A", "MI300X", "MI325X", "MI350X", "MI355X"). |

**Returns:** Device instance.

#### GPU()

```python
def GPU(
    device: typing.Literal['A10', 'A10G', 'A100', 'A100 80G', 'B200', 'H100', 'H200', 'L4', 'L40s', 'T4', 'V100', 'RTX PRO 6000', 'GB10'],
    quantity: typing.Literal[1, 2, 3, 4, 5, 6, 7, 8],
    partition: typing.Union[typing.Literal['1g.5gb', '2g.10gb', '3g.20gb', '4g.20gb', '7g.40gb'], typing.Literal['1g.10gb', '2g.20gb', '3g.40gb', '4g.40gb', '7g.80gb'], typing.Literal['1g.10gb', '1g.20gb', '2g.20gb', '3g.40gb', '4g.40gb', '7g.80gb'], typing.Literal['1g.18gb', '1g.35gb', '2g.35gb', '3g.71gb', '4g.71gb', '7g.141gb'], NoneType] = None,
) -> flyte._resources.Device
```
Create a GPU device instance.



| Parameter | Type | Description |
|-|-|-|
| `device` | `typing.Literal['A10', 'A10G', 'A100', 'A100 80G', 'B200', 'H100', 'H200', 'L4', 'L40s', 'T4', 'V100', 'RTX PRO 6000', 'GB10']` | The type of GPU (e.g., "T4", "A100"). |
| `quantity` | `typing.Literal[1, 2, 3, 4, 5, 6, 7, 8]` | The number of GPUs of this type. |
| `partition` | `typing.Union[typing.Literal['1g.5gb', '2g.10gb', '3g.20gb', '4g.20gb', '7g.40gb'], typing.Literal['1g.10gb', '2g.20gb', '3g.40gb', '4g.40gb', '7g.80gb'], typing.Literal['1g.10gb', '1g.20gb', '2g.20gb', '3g.40gb', '4g.40gb', '7g.80gb'], typing.Literal['1g.18gb', '1g.35gb', '2g.35gb', '3g.71gb', '4g.71gb', '7g.141gb'], NoneType]` | The partition of the GPU (e.g., "1g.5gb", "2g.10gb" for gpus) or ("1x1", ... for tpus). |

**Returns:** Device instance.

#### HABANA_GAUDI()

```python
def HABANA_GAUDI(
    device: typing.Literal['Gaudi1'],
) -> flyte._resources.Device
```
Create a Habana Gaudi device instance.



| Parameter | Type | Description |
|-|-|-|
| `device` | `typing.Literal['Gaudi1']` | Device type (e.g., "Gaudi1"). |

**Returns:** Device instance.

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

**Returns:** Device instance.

#### TPU()

```python
def TPU(
    device: typing.Literal['V5P', 'V6E'],
    partition: typing.Union[typing.Literal['2x2x1', '2x2x2', '2x4x4', '4x4x4', '4x4x8', '4x8x8', '8x8x8', '8x8x16', '8x16x16', '16x16x16', '16x16x24'], typing.Literal['1x1', '2x2', '2x4', '4x4', '4x8', '8x8', '8x16', '16x16'], NoneType] = None,
)
```
Create a TPU device instance.



| Parameter | Type | Description |
|-|-|-|
| `device` | `typing.Literal['V5P', 'V6E']` | Device type (e.g., "V5P", "V6E"). |
| `partition` | `typing.Union[typing.Literal['2x2x1', '2x2x2', '2x4x4', '4x4x4', '4x4x8', '4x8x8', '8x8x8', '8x8x16', '8x16x16', '16x16x16', '16x16x24'], typing.Literal['1x1', '2x2', '2x4', '4x4', '4x8', '8x8', '8x16', '16x16'], NoneType]` | Partition of the TPU (e.g., "1x1", "2x2", ...). |

**Returns:** Device instance.

#### build()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await build.aio()`.
```python
def build(
    image: Image,
    dry_run: bool = False,
    force: bool = False,
    wait: bool = True,
) -> ImageBuild
```
Build an image. The existing async context will be used.

```python
import flyte
image = flyte.Image("example_image")
if __name__ == "__main__":
    result = asyncio.run(flyte.build.aio(image))
    print(result.uri)
```


| Parameter | Type | Description |
|-|-|-|
| `image` | `Image` | The image(s) to build. |
| `dry_run` | `bool` | Tell the builder to not actually build. Different builders will have different behaviors. |
| `force` | `bool` | Skip the existence check and force a rebuild. When using the remote builder, this also sets overwrite_cache=True on the build run. |
| `wait` | `bool` | Wait for the build to finish. If wait is False, the function will return immediately and the build will run in the background. |

**Returns**

An ImageBuild object containing the image URI and optionally the remote run that kicked off the build.


#### build_images()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await build_images.aio()`.
```python
def build_images(
    *envs: Environment,
    copy_style: 'CopyFiles' = 'loaded_modules',
    seed_cache: ImageCache | None = None,
) -> ImageCache
```
Build the images for the given environment(s).



| Parameter | Type | Description |
|-|-|-|
| `*envs` | `Environment` | One or more environments to build images for. When multiple environments are passed they are planned together in a single pass (mirroring `deploy`), and the resulting image caches are merged into one. |
| `copy_style` | `'CopyFiles'` | Copy style that the eventual deploy will use. Must match the deploy's `--copy-style` so the image content hashes — and therefore the registry tags — line up, letting deploy reuse the pre-built image. |
| `seed_cache` | `ImageCache \| None` | Optional ImageCache of environments already built by a prior deploy. Seeded environments reuse the recorded URI and skip the build pipeline entirely; see `_build_images` for details. |

**Returns:** ImageCache containing the built images.

#### ctx()

```python
def ctx()
```
Returns the current flyte.models.TaskContext when running inside a task.

Outside a task execution it returns a falsy null context whose fields are all None,
so task code can read `flyte.ctx().<field>` without a None-guard. To detect whether
a task context is active, rely on truthiness: `if flyte.ctx(): ...`.

Note: Only use this in task code and not module level.

Use `flyte.models.TaskContext.checkpoint` for durable task checkpointing
(object-store prefixes from the runtime).


#### current_domain()

```python
def current_domain()
```
Returns the current domain from Runtime environment (on the cluster) or from the initialized configuration.
This is safe to be used during `deploy`, `run` and within `task` code.

NOTE: This will not work if you deploy a task to a domain and then run it in another domain.

Raises InitializationError if the configuration is not initialized or domain is not set.


**Returns:** The current domain

#### current_project()

```python
def current_project()
```
Returns the current project from the Runtime environment (on the cluster) or from the initialized configuration.
This is safe to be used during `deploy`, `run` and within `task` code.

NOTE: This will not work if you deploy a task to a project and then run it in another project.

Raises InitializationError if the configuration is not initialized or project is not set.


**Returns:** The current project

#### custom_context()

```python
def custom_context(
    **context: str,
)
```
Synchronous context manager to set input context for tasks spawned within this block.

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
| `**context` | `str` | Key-value pairs to set as input context |

#### deploy()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await deploy.aio()`.
```python
def deploy(
    *envs: Environment,
    dryrun: bool = False,
    version: str | None = None,
    interactive_mode: bool | None = None,
    copy_style: CopyFiles = 'loaded_modules',
) -> List[Deployment]
```
Deploy the given environment or list of environments.



| Parameter | Type | Description |
|-|-|-|
| `*envs` | `Environment` | Environment or list of environments to deploy. |
| `dryrun` | `bool` | dryrun mode, if True, the deployment will not be applied to the control plane. |
| `version` | `str \| None` | version of the deployment, if None, the version will be computed from the code bundle. TODO: Support for interactive_mode |
| `interactive_mode` | `bool \| None` | Optional, can be forced to True or False. If not provided, it will be set based on the current environment. For example Jupyter notebooks are   considered interactive mode, while scripts are not. This is used to determine how the code bundle is   created. |
| `copy_style` | `CopyFiles` | Copy style to use when running the task |

**Returns:** Deployment object containing the deployed environments and tasks.

#### get_custom_context()

```python
def get_custom_context()
```
Get the current input context. This can be used within a task to retrieve
context metadata that was passed to the action.

Context will automatically propagate to sub-actions.

```python
import flyte

env = flyte.TaskEnvironment(name="...")

@env.task
def t1():
    # context can be retrieved with `get_custom_context`
    ctx = flyte.get_custom_context()
    print(ctx)  # {'project': '...', 'entity': '...'}
```



**Returns:** Dictionary of context key-value pairs

#### group()

```python
def group(
    name: str,
)
```
Create a new group with the given name. The method is intended to be used as a context manager.

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
    org: str | None = None,
    project: str | None = None,
    domain: str | None = None,
    root_dir: Path | None = None,
    log_level: int | None = None,
    log_format: LogFormat | None = None,
    reset_root_logger: bool = False,
    user_log_level: int | None = None,
    endpoint: str | None = None,
    headless: bool = False,
    insecure: bool = False,
    insecure_skip_verify: bool = False,
    ca_cert_file_path: str | None = None,
    auth_type: AuthType = 'Pkce',
    command: List[str] | None = None,
    proxy_command: List[str] | None = None,
    api_key: str | None = None,
    client_id: str | None = None,
    client_credentials_secret: str | None = None,
    auth_client_config: ClientConfig | None = None,
    rpc_retries: int = 3,
    http_proxy_url: str | None = None,
    disable_keyring: bool = False,
    storage: Storage | None = None,
    batch_size: int = 1000,
    image_builder: ImageBuildEngine.ImageBuilderType = 'local',
    images: typing.Dict[str, str] | None = None,
    image_registry: str | None = None,
    source_config_path: Optional[Path] = None,
    sync_local_sys_paths: bool = True,
    load_plugin_type_transformers: bool = True,
    local_persistence: bool = False,
    local_tracked: bool = False,
    local_tracked_strict: bool = False,
    scopes: List[str] | None = None,
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
| `reset_root_logger` | `bool` | If True, replace the root logger's handlers with Flyte's own, so lines from third-party libraries that propagate to the root logger are formatted the same way as Flyte's (JSON when `log_format` is `json`, otherwise Rich or plain console). Defaults to False, which leaves those handlers in place and instead wraps each one so its output carries the run and action context. Can also be turned on with the environment variable `FLYTE_RESET_ROOT_LOGGER=1`. |
| `user_log_level` | `int \| None` | |
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
| `disable_keyring` | `bool` | Disable storage of tokens in local keyring. |
| `storage` | `Storage \| None` | Optional blob store (S3, GCS, Azure) configuration if needed to access (i.e. using Minio) |
| `batch_size` | `int` | Optional batch size for operations that use listings, defaults to 1000, so limit larger than batch_size will be split into multiple requests. |
| `image_builder` | `ImageBuildEngine.ImageBuilderType` | Optional image builder configuration, if not provided, the default image builder will be used. |
| `images` | `typing.Dict[str, str] \| None` | Optional dict of images that can be used by referencing the image name. |
| `image_registry` | `str \| None` | Optional container registry to push built images to, overriding the built-in default base registry. Equivalent to the `image.registry` config entry. |
| `source_config_path` | `Optional[Path]` | Optional path to the source configuration file (This is only used for documentation) |
| `sync_local_sys_paths` | `bool` | Whether to include and synchronize local sys.path entries under the root directory into the remote container (default: True). |
| `load_plugin_type_transformers` | `bool` | If enabled (default True), load the type transformer plugins registered under the "flyte.plugins.types" entry point group. |
| `local_persistence` | `bool` | Whether to enable SQLite persistence for local run metadata (default: False). |
| `local_tracked` | `bool` | Whether to report tracked run state to the Flyte control plane (default: False). Requires an initialized client and a configured project/domain. |
| `local_tracked_strict` | `bool` | Strict tracked-run reporting for debugging (default: False). Any reporting failure fails the run loudly instead of being logged and swallowed. Only takes effect when reporting is enabled. |
| `scopes` | `List[str] \| None` | OAuth scopes to request. When omitted, scopes are discovered from the auth metadata service. |

**Returns:** None

#### init_from_api_key()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await init_from_api_key.aio()`.
```python
def init_from_api_key(
    api_key: str | None = None,
    project: str | None = None,
    domain: str | None = None,
    root_dir: Path | None = None,
    log_level: int | None = None,
    log_format: LogFormat | None = None,
    storage: Storage | None = None,
    batch_size: int = 1000,
    image_builder: ImageBuildEngine.ImageBuilderType = 'local',
    images: typing.Dict[str, str] | None = None,
    sync_local_sys_paths: bool = True,
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
| `sync_local_sys_paths` | `bool` | Whether to include and synchronize local sys.path entries under the root directory into the remote container (default: True) |

**Returns:** None

#### init_from_config()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await init_from_config.aio()`.
```python
def init_from_config(
    path_or_config: str | Path | Config | None = None,
    root_dir: Path | None = None,
    log_level: int | None = None,
    log_format: LogFormat = 'console',
    user_log_level: int | None = None,
    org: str | None = None,
    project: str | None = None,
    domain: str | None = None,
    storage: Storage | None = None,
    batch_size: int = 1000,
    image_builder: ImageBuildEngine.ImageBuilderType | None = None,
    images: tuple[str, ...] | None = None,
    sync_local_sys_paths: bool = True,
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
| `user_log_level` | `int \| None` | |
| `org` | `str \| None` | Org name, this will override the org in the configuration file when non-empty |
| `project` | `str \| None` | Project name, this will override any project names in the configuration file |
| `domain` | `str \| None` | Domain name, this will override any domain names in the configuration file |
| `storage` | `Storage \| None` | Optional blob store (S3, GCS, Azure) configuration if needed to access (i.e. using Minio) |
| `batch_size` | `int` | Optional batch size for operations that use listings, defaults to 1000 |
| `image_builder` | `ImageBuildEngine.ImageBuilderType \| None` | Optional image builder configuration, if provided, will override any defaults set in the configuration. |
| `images` | `tuple[str, ...] \| None` | List of image strings in format "imagename=imageuri" or just "imageuri". |
| `sync_local_sys_paths` | `bool` | Whether to include and synchronize local sys.path entries under the root directory into the remote container (default: True). |

**Returns:** None

#### init_in_cluster()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await init_in_cluster.aio()`.
```python
def init_in_cluster(
    org: str | None = None,
    project: str | None = None,
    domain: str | None = None,
    api_key: str | None = None,
    endpoint: str | None = None,
    insecure: bool = False,
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
    endpoint: str | None = None,
    org: str | None = None,
    project: str | None = None,
    domain: str | None = None,
    insecure: bool = False,
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
| `insecure` | `bool` | Whether to use an insecure channel |

**Returns:** Dictionary of remote kwargs used for initialization

#### is_control_plane_available()

```python
def is_control_plane_available()
```
True when this process can submit work to a Flyte control plane — `flyte.run` launches real
remote runs whose actions can be inspected, awaited, and replayed (recovered/forked).

The answer depends on where the code is executing:

* Inside a task launched on a Flyte cluster (`flyte.ctx().is_in_cluster()`): True. The
  in-cluster runtime configures the connection before user code runs.
* Inside a task executing locally (`flyte run --local` / `flyte.run(mode="local")`): False,
  even when a client happens to be configured — the local dev loop is expected to stay
  local, and a locally-orchestrated run has no control-plane actions to replay.
* Outside any task (a driver script, a notebook): True iff a client has been configured via
  `flyte.init` / `flyte.init_from_config` / `flyte.init_from_api_key`.

Typical use is a task that adapts to where it runs — e.g. an agent that launches and forks
real runs on a cluster, but falls back to invoking the task functions in-process when
developed locally:

```python
@env.task
async def agent() -> None:
    if flyte.is_control_plane_available():
        run = await flyte.run.aio(my_pipeline, x=1)
        await run.wait.aio()
    else:
        await my_pipeline.func(x=1)
```



**Returns:** True when remote submission is available, False otherwise.

#### latest_checkpoint()

```python
def latest_checkpoint(
    root: pathlib.Path,
    glob_pattern: str = '**/last.ckpt',
    key: Callable[[pathlib.Path], Any] | None = None,
) -> pathlib.Path | None
```
Return the file under *root* matching *glob_pattern* with the largest `key(path)`, or `None`.

By default *key* is `lambda p: p.stat().st_mtime` (newest modification time wins). Pass *key* to
rank matches another way (e.g. parse a step from the filename).

For example, the Lightning framework would use `**/last.ckpt` under the tree restored by
`flyte.Checkpoint.load_sync` / `flyte.Checkpoint.load`. Pass a different *glob_pattern* for other
layouts (e.g. `"**/*.ckpt"`).


| Parameter | Type | Description |
|-|-|-|
| `root` | `pathlib.Path` | |
| `glob_pattern` | `str` | |
| `key` | `Callable[[pathlib.Path], Any] \| None` | |

#### load_interactive_ctx()

```python
def load_interactive_ctx(
    path: str | os.PathLike | None = None,
) -> TaskContext
```
Restore the task execution context from the config file written by a debug-mode task pod.

Use this from a debugger, REPL, or notebook attached to a live task pod: it initializes
the SDK against the cluster and installs the task's context as the current one, so
`flyte.ctx()` and data IO (raw data prefix, inputs/outputs paths) behave as they would
inside the task.



| Parameter | Type | Description |
|-|-|-|
| `path` | `str \| os.PathLike \| None` | Optional explicit path to the config file. Defaults to the well-known location `<cwd>/.flyte/run_context.json`. |

**Returns**

The restored and installed `flyte.models.TaskContext`.


**Raises**

| Exception | Description |
|-|-|
| `FileNotFoundError` | If the config file does not exist at the given/known location. |
| `ValueError` | If the config file is missing required fields. |

#### load_plugin_config()

```python
def load_plugin_config(
    path: 'Union[str, pathlib.Path]',
) -> Any
```
Load a plugin config instance from a YAML file.

The file must be a mapping with a top-level `plugin` key holding the fully qualified
class name of the plugin config (e.g. `flyteplugins.ray.RayJobConfig`), and an optional
`config` mapping with the constructor arguments — including nested classes, expressed as
nested mappings/lists that mirror the plugin config's dataclass fields.

```yaml
plugin: flyteplugins.ray.RayJobConfig
config:
  worker_node_config:
    - group_name: workers
      replicas: 2
  head_node_config:
    ray_start_params:
      num-cpus: "0"
```


| Parameter | Type | Description |
|-|-|-|
| `path` | `'Union[str, pathlib.Path]'` | |

#### map()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await flyte.map.aio()`.
```python
def map(
    func: typing.Union[flyte._task.AsyncFunctionTaskTemplate[~P, ~R, ~F], functools.partial[~R]],
    *args: typing.Iterable[typing.Any],
    group_name: str | None = None,
    concurrency: int = 0,
    return_exceptions: bool = True,
) -> typing.Iterator[typing.Union[~R, Exception]]
```
Map a function over the provided arguments with concurrent execution.



| Parameter | Type | Description |
|-|-|-|
| `func` | `typing.Union[flyte._task.AsyncFunctionTaskTemplate[~P, ~R, ~F], functools.partial[~R]]` | The async function to map. |
| `*args` | `typing.Iterable[typing.Any]` | Positional arguments to pass to the function (iterables that will be zipped). |
| `group_name` | `str \| None` | The name of the group for the mapped tasks. |
| `concurrency` | `int` | The maximum number of concurrent tasks to run. If 0, run all tasks concurrently. |
| `return_exceptions` | `bool` | If True, yield exceptions instead of raising them. |

**Returns:** AsyncIterator yielding results in order.

#### new_condition()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await new_condition.aio()`.
```python
def new_condition(
    name: str,
    prompt: str = 'Approve?',
    prompt_type: typing.Literal['text', 'markdown'] = 'text',
    data_type: typing.Type[~ConditionType] = bool,
    description: str = '',
    timeout: typing.Union[datetime.timedelta, int, float, NoneType] = None,
    webhook: typing.Optional[flyte._condition.ConditionWebhook] = None,
) -> flyte._condition._Condition
```
Create a condition that can be awaited in a workflow. Conditions can be used to pause workflow execution
until an external signal is received.

**Condition protocol (remote execution):**

When running inside a task, `new_condition` registers a *condition action* with the
backend. Calling `condition.wait()` blocks until the condition is resolved. The backend
delivers the result as an inline `Literal` (protobuf scalar/primitive) in the
`ActionUpdate` stream — no `output_uri` is involved for conditions.

- On success, `wait()` returns the value converted to `data_type`
  (`True`/`False` for bool, Python `int`/`float`/`str` for the others).
- If the condition times out, `wait()` raises `flyte.errors.ConditionTimedoutError`.
- If the condition fails, `wait()` raises `flyte.errors.ConditionFailedError`.



| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Name of the condition |
| `prompt` | `str` | Prompt message for the condition |
| `prompt_type` | `typing.Literal['text', 'markdown']` | Type of prompt rendering - "text" or "markdown" |
| `data_type` | `typing.Type[~ConditionType]` | Data type of the condition payload — one of `bool`, `int`, `float`, `str` |
| `description` | `str` | Description of the condition |
| `timeout` | `typing.Union[datetime.timedelta, int, float, NoneType]` | Optional timeout as a timedelta or number of seconds. If the condition is not signaled within this duration, `wait()` will raise `flyte.errors.ConditionTimedoutError`. |
| `webhook` | `typing.Optional[flyte._condition.ConditionWebhook]` | Optional webhook configuration. When provided, the backend will POST to the given URL with the specified payload. The payload may use `{callback_uri}` as a template variable — the backend replaces it with the URI that can be used to signal the condition. |

**Returns:** An instance of _Condition representing the created condition

#### rerun()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await rerun.aio()`.
```python
def rerun(
    run_name: str,
    action_name: str = 'a0',
    recover: bool = False,
    force_rerun_actions: Sequence[str] | None = None,
    allow_missing_source_outputs: bool = False,
    **inputs: Any,
) -> Run
```
Re-run a prior run, returning a new `Run`.

`rerun("r1")` creates a whole new run with the prior run's exact inputs (fetching its code from
the platform); `rerun("r1", recover=True)` does the same but reuses the prior run's succeeded
actions, re-executing only what failed or never ran. Pass keyword inputs to change
parameters (`rerun("r1", x=2)`); inputs left out keep the prior run's values. New inputs
combine with recovery (`rerun("r1", recover=True, x=2)`), in which case recovered actions keep
the outputs they produced under the original inputs unless listed in `force_rerun_actions`.
Use `with_runcontext(...).rerun(...)` to apply run-context overrides (env_vars, labels, …).
The prior run's code is always replayed as-is.



| Parameter | Type | Description |
|-|-|-|
| `run_name` | `str` | Name of the prior run to re-run. |
| `action_name` | `str` | Action within the prior run to source the task + inputs from. Defaults to `a0`, the root action — i.e. the whole run. Naming a child action instead roots the new run at that action's task, run with the exact inputs it received. Cannot be combined with `recover`. |
| `recover` | `bool` | Reuse the prior run's succeeded actions, re-running only what failed or never ran. Remote-only; requires a backend (and flyteidl2 build) with RunSpec.relation recovery support. |
| `force_rerun_actions` | `Sequence[str] \| None` | With `recover`, names of actions that must re-execute even though they succeeded in the source run (escape hatch). A listed parent action re-enqueues its children — list them too to force the whole subtree. Unknown names are ignored. |
| `allow_missing_source_outputs` | `bool` | Proceed when the source run's outputs were cleaned up from storage, using its inputs URI directly. The client cannot verify the inputs still exist — if they were deleted too, the new run fails at runtime. Irrelevant when the new inputs cover every input of the task, since the source inputs are then not read at all. |
| `**inputs` | `Any` | Optional native keyword inputs to change parameters. Any input not passed keeps the source run's value, so passing none reuses the source run's inputs wholesale. |

**Returns:** the new Run.

#### run()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await run.aio()`.
```python
def run(
    task: TaskTemplate[P, R, F],
    *args: P.args,
    **kwargs: P.kwargs,
) -> Run
```
Run a task with the given parameters



| Parameter | Type | Description |
|-|-|-|
| `task` | `TaskTemplate[P, R, F]` | task to run |
| `*args` | `P.args` | args to pass to the task |
| `**kwargs` | `P.kwargs` | kwargs to pass to the task |

**Returns:** Run | Result of the task

#### run_python_script()


> [!NOTE] This method can be called both synchronously or asynchronously.
> Default invocation is sync and will block.
> To call it asynchronously, use the function `.aio()` on the method name itself, e.g.,:
> `result = await run_python_script.aio()`.
```python
def run_python_script(
    script: pathlib.Path,
    cpu: int = 4,
    memory: str = '16Gi',
    gpu: int = 0,
    gpu_type: str = 'T4',
    image: 'Union[Image, List[str], None]' = None,
    timeout: int = 3600,
    extra_args: 'Optional[List[str]]' = None,
    queue: 'Optional[str]' = None,
    wait: bool = False,
    name: 'Optional[str]' = None,
    debug: bool = False,
    output_dir: 'Optional[str]' = None,
    include_files: 'Optional[List[str]]' = None,
    plugin_config: 'Optional[Any]' = None,
    clustered: bool = False,
    replicas: 'Optional[int]' = None,
    nproc_per_node: 'Optional[int]' = None,
    runtime: 'Optional[TorchRun]' = None,
    failure_policy: 'Optional[ClusterFailurePolicy]' = None,
    ttl_seconds_after_finished: 'Optional[int]' = None,
) -> 'Run'
```
Package and run a Python script on a remote Flyte cluster.

Bundles the script into a Flyte code bundle and executes it remotely
with the requested resources.  Unlike `interactive_mode` (which
pickles the task), this approach uses an `InternalTaskResolver`
so the task can be properly debugged with `debug=True`.

Project and domain are read from the init config (set via `flyte.init()`
or `flyte.init_from_config()`), consistent with `flyte.run()`.

```python
import flyte
from pathlib import Path

flyte.init(endpoint="my-cluster.example.com")

# With a list of packages (auto-builds image)
run = flyte.run_python_script(
    Path("train.py"),
    gpu=1,
    gpu_type="A100",
    memory="64Gi",
    image=["torch", "transformers"],
)
print(run.url)

# With a custom Image object
img = flyte.Image.from_debian_base(name="my-img").with_pip_packages("numpy")
run = flyte.run_python_script(Path("analysis.py"), image=img)
```


| Parameter | Type | Description |
|-|-|-|
| `script` | `pathlib.Path` | Path to the Python script to run. |
| `cpu` | `int` | Number of CPUs to request (default: 4). |
| `memory` | `str` | Memory to request, e.g. `"16Gi"` (default: `"16Gi"`). |
| `gpu` | `int` | Number of GPUs to request (default: 0). |
| `gpu_type` | `str` | GPU accelerator type: `T4`, `A100`, `H100`, `L4`, etc. Only used when `gpu > 0` (default: `"T4"`). |
| `image` | `'Union[Image, List[str], None]'` | Container image to use. Accepts either: - A `flyte.Image` object for full control over the image. - A `list[str]` of pip package names to install on top of the   default Debian base image (e.g. `["torch", "transformers"]`). - `None` to use a plain Debian base image (default). |
| `timeout` | `int` | Task timeout in seconds (default: 3600). |
| `extra_args` | `'Optional[List[str]]'` | Extra arguments passed to the script. |
| `queue` | `'Optional[str]'` | Flyte queue / cluster override. |
| `wait` | `bool` | If True, block until execution completes before returning. |
| `name` | `'Optional[str]'` | Run name. If omitted, a random name is generated. |
| `debug` | `bool` | If True, run the task as a VS Code debug task, starting a code-server in the container so you can connect via the UI to interactively debug/run the task. |
| `output_dir` | `'Optional[str]'` | |
| `include_files` | `'Optional[List[str]]'` | Extra paths or glob patterns to bundle alongside the script. Relative entries anchor at the script's directory; absolute paths pass through unchanged. Example: `["*.py", "configs/settings.yaml"]`. |
| `plugin_config` | `'Optional[Any]'` | A plugin config instance (e.g. `flyteplugins.ray.RayJobConfig`) that selects and configures the underlying task type the script runs under. Use `flyte.load_plugin_config()` to build one from a YAML file (this is what the `flyte run python-script --plugin-config` CLI flag does under the hood). Mutually exclusive with `clustered=True`, which manages its own plugin config. |
| `clustered` | `bool` | If True, run the script under a `flyte.clustered.ClusteredTaskEnvironment` (a Kubernetes JobSet) instead of a plain `TaskEnvironment`, for distributed multi-node execution via `torchrun`. Requires `replicas` and `nproc_per_node`. |
| `replicas` | `'Optional[int]'` | Number of pods (== nodes) in the job set. Required when `clustered=True`. |
| `nproc_per_node` | `'Optional[int]'` | Number of processes per pod, passed to `torchrun --nproc-per-node`. Required when `clustered=True`. |
| `runtime` | `'Optional[TorchRun]'` | Launcher configuration for clustered execution, e.g. `flyte.clustered.TorchRun(rdzv_backend="c10d")`. Only used when `clustered=True`; defaults to `TorchRun()`. |
| `failure_policy` | `'Optional[ClusterFailurePolicy]'` | JobSet-level restart/eviction policy, e.g. `flyte.clustered.ClusterFailurePolicy(max_restarts=2)`. Only used when `clustered=True`; defaults to `ClusterFailurePolicy()`. |
| `ttl_seconds_after_finished` | `'Optional[int]'` | Seconds to retain the JobSet after completion. Only used when `clustered=True`. |

**Returns**

A `flyte.remote.Run` handle for the remote execution.


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

```python
import flyte
from flyte.app.extras import FastAPIAppEnvironment

env = FastAPIAppEnvironment(name="my-app", ...)

# Simple serve
app = flyte.serve(env)
print(f"App URL: {app.url}")
```

See Also:
    with_servecontext: For customizing deployment settings


| Parameter | Type | Description |
|-|-|-|
| `app_env` | `'AppEnvironment'` | The app environment to serve |

**Returns**

An `AppHandle` — either a `_LocalApp` (local) or `App` (remote)


#### trace()

```python
def trace(
    func: typing.Callable[..., ~T],
) -> typing.Callable[..., ~T]
```
A decorator that traces function execution with timing information.
Works with regular functions, sync generators, async functions, and async generators/iterators.


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
    mode: Mode | None = None,
    name: Optional[str] = None,
    service_account: Optional[str] = None,
    version: Optional[str] = None,
    copy_style: CopyFiles = 'loaded_modules',
    dry_run: bool = False,
    copy_bundle_to: pathlib.Path | None = None,
    interactive_mode: bool | None = None,
    raw_data_path: str | None = None,
    run_base_dir: str | None = None,
    run_start_time: Optional[datetime] = None,
    overwrite_cache: bool = False,
    project: str | None = None,
    domain: str | None = None,
    env_vars: Dict[str, str] | None = None,
    labels: Dict[str, str] | None = None,
    annotations: Dict[str, str] | None = None,
    interruptible: bool | None = None,
    log_level: int | None = None,
    log_format: LogFormat = 'console',
    user_log_level: int | None = None,
    reset_root_logger: bool = False,
    disable_run_cache: bool = False,
    queue: Optional[str] = None,
    max_action_concurrency: int | None = None,
    notifications: Notification | Tuple[Notification, ...] | None = None,
    custom_context: Dict[str, str] | None = None,
    cache_lookup_scope: CacheLookupScope = 'global',
    preserve_original_types: bool = False,
    debug: bool = False,
    tracked: bool = False,
    tracked_strict: bool = False,
    _tracker: Any = None,
) -> _Runner
```
Launch a new run with the given parameters as the context.

```python
import flyte
import flyte.notify as notify
from flyte.models import ActionPhase

env = flyte.TaskEnvironment("example")

@env.task
async def example_task(x: int, y: str) -> str:
    return f"{x} {y}"

if __name__ == "__main__":
    flyte.with_runcontext(
        name="example_run_id",
        notifications=notify.Slack(
            on_phase=ActionPhase.FAILED,
            webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL",
            message="Task failed: {run.error}",
        ),
    ).run(example_task, 1, y="hello")
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
| `run_start_time` | `Optional[datetime]` | Optional UTC datetime at which the run was triggered. If not provided, defaults to `datetime.now(timezone.utc)` at TaskContext construction. Useful for local simulation/tests that need a deterministic timestamp. Accessible inside a task via `flyte.ctx().run_start_time`. |
| `overwrite_cache` | `bool` | Optional If true, the cache will be overwritten for the run |
| `project` | `str \| None` | Optional The project to use for the run |
| `domain` | `str \| None` | Optional The domain to use for the run |
| `env_vars` | `Dict[str, str] \| None` | Optional Environment variables to set for the run |
| `labels` | `Dict[str, str] \| None` | Optional user-defined labels to attach to the run as KEY=VALUE pairs, used for filtering and organizing runs (e.g. `flyte get run --with-label team=ml`) |
| `annotations` | `Dict[str, str] \| None` | Optional Annotations to set for the run |
| `interruptible` | `bool \| None` | Optional If true, the run can be scheduled on interruptible instances and false implies that all tasks in the run should only be scheduled on non-interruptible instances. If not specified the original setting on all tasks is retained. |
| `log_level` | `int \| None` | Optional Log level to set for the run. If not provided, it will be set to the default log level set using `flyte.init()` |
| `log_format` | `LogFormat` | Optional Log format to set for the run. If not provided, it will be set to the default log format |
| `user_log_level` | `int \| None` | |
| `reset_root_logger` | `bool` | If True, replace the root logger's handlers with Flyte's own, so lines from third-party libraries that propagate to the root logger are formatted the same way as Flyte's (JSON when `log_format` is `json`, otherwise Rich or plain console). Defaults to False, which leaves those handlers in place and instead wraps each one so its output carries the run and action context. Can also be turned on with the environment variable `FLYTE_RESET_ROOT_LOGGER=1`. |
| `disable_run_cache` | `bool` | Optional If true, the run cache will be disabled. This is useful for testing purposes. |
| `queue` | `Optional[str]` | Optional The queue to use for the run. This is used to specify the cluster to use for the run. |
| `max_action_concurrency` | `int \| None` | Optional Maximum number of actions that can run concurrently within this run. Only applies to remote runs. If not provided, the platform default (configurable via the `run.max_action_concurrency` setting at org/domain/project scope) applies. Must be 0 (platform default) or at least 2 — a value of 1 would deadlock the run, since the parent action holds a concurrency slot while waiting for its child actions. |
| `notifications` | `Notification \| Tuple[Notification, ...] \| None` | Optional Notification(s) to send when the run reaches specific execution phases. Accepts a single notification or a tuple of notifications. Supports Email, Slack, Teams, and Webhook types. See `flyte.notify` for available notification types and template variables. |
| `custom_context` | `Dict[str, str] \| None` | Optional global input context to pass to the task. This will be available via get_custom_context() within the task and will automatically propagate to sub-tasks. Acts as base/default values that can be overridden by context managers in the code. |
| `cache_lookup_scope` | `CacheLookupScope` | Optional Scope to use for the run. This is used to specify the scope to use for cache lookups. If not specified, it will be set to the default scope (global unless overridden at the system level). |
| `preserve_original_types` | `bool` | Optional If true, the type engine will preserve original types (e.g., pd.DataFrame) when guessing python types from literal types. If false (default), it will return the generic flyte.io.DataFrame. This option is automatically set to True if interactive_mode is True unless overridden explicitly by this parameter. |
| `debug` | `bool` | Optional If true, the task will be run as a VSCode debug task, starting a code-server in the container so users can connect via the UI to interactively debug/run the task. |
| `tracked` | `bool` | Local-only. If true, report tracked run state (actions, attempts, outputs, reports) to the Flyte control plane via TrackedRunService so the run shows up in the console. Requires an initialized client and a configured project/domain. Can also be enabled globally with the `local.tracked` config key. Reporting is best-effort and never fails the local run. |
| `tracked_strict` | `bool` | Local-only, for debugging reporting itself. When true (with `tracked`), the first reporting failure — registration, an artifact upload, a rejected or undeliverable ReportActions update, or a flush timeout — fails the run loudly instead of being logged and swallowed. Can also be enabled globally with the `local.tracked_strict` config key. |
| `_tracker` | `Any` | This is an internal only parameter used by the CLI to render the TUI. |

**Returns:** runner

#### with_servecontext()

```python
def with_servecontext(
    mode: ServeMode | None = None,
    version: Optional[str] = None,
    copy_style: CopyFiles = 'loaded_modules',
    dry_run: bool = False,
    project: str | None = None,
    domain: str | None = None,
    env_vars: dict[str, str] | None = None,
    parameter_values: dict[str, dict[str, str | flyte.io.File | flyte.io.Dir]] | None = None,
    cluster_pool: str | None = None,
    log_level: int | None = None,
    log_format: LogFormat = 'console',
    user_log_level: int | None = None,
    interactive_mode: bool | None = None,
    copy_bundle_to: pathlib.Path | None = None,
    deactivate_timeout: float | None = None,
    activate_timeout: float | None = None,
    health_check_timeout: float | None = None,
    health_check_interval: float | None = None,
    health_check_path: str | None = None,
    raw_data_path: str | None = None,
) -> _Serve
```
Create a serve context with custom configuration.

This function allows you to customize how an app is served, including
overriding environment variables, cluster pool, logging, and other deployment settings.

Use `mode="local"` to serve the app on localhost (non-blocking) so you can
immediately invoke tasks that call the app endpoint:

```python
import flyte

local_app = flyte.with_servecontext(mode="local").serve(app_env)
local_app.is_active()  # wait for the server to start
# ... call tasks that use app_env.endpoint ...
local_app.deactivate()
```

Use `mode="remote"` (or omit *mode* when a Flyte client is configured) to
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
| `mode` | `ServeMode \| None` | "local" to run on localhost, "remote" to deploy to the Flyte backend. When `None` the mode is inferred from the current configuration. |
| `version` | `Optional[str]` | Optional version override for the app deployment |
| `copy_style` | `CopyFiles` | Code bundle copy style. Options: "loaded_modules", "all", "none" (default: "loaded_modules") |
| `dry_run` | `bool` | If True, don't actually deploy (default: False) |
| `project` | `str \| None` | Optional project override |
| `domain` | `str \| None` | Optional domain override |
| `env_vars` | `dict[str, str] \| None` | Optional environment variables to inject/override in the app container |
| `parameter_values` | `dict[str, dict[str, str \| flyte.io.File \| flyte.io.Dir]] \| None` | Optional parameter values to inject/override in the app container. Must be a dictionary that maps app environment names to a dictionary of parameter names to values. |
| `cluster_pool` | `str \| None` | Optional cluster pool to deploy the app to |
| `log_level` | `int \| None` | Optional log level (e.g., logging.DEBUG, logging.INFO). If not provided, uses init config or default |
| `log_format` | `LogFormat` | Optional log format ("console" or "json", default: "console") |
| `user_log_level` | `int \| None` | |
| `interactive_mode` | `bool \| None` | Optional, can be forced to True or False. If not provided, it will be set based on the current environment. For example Jupyter notebooks are considered interactive mode, while scripts are not. This is used to determine how the code bundle is created. This is used to determine if the app should be served in interactive mode or not. |
| `copy_bundle_to` | `pathlib.Path \| None` | When dry_run is True, the bundle will be copied to this location if specified |
| `deactivate_timeout` | `float \| None` | Timeout in seconds for waiting for the app to stop during `deactivate(wait=True)`. Defaults to 6 s. |
| `activate_timeout` | `float \| None` | Total timeout in seconds when polling the health-check endpoint during `activate(wait=True)`. Defaults to 60 s. |
| `health_check_timeout` | `float \| None` | Per-request timeout in seconds for each health-check HTTP request. Defaults to 2 s. |
| `health_check_interval` | `float \| None` | Interval in seconds between consecutive health-check polls. Defaults to 1 s. |
| `health_check_path` | `str \| None` | URL path used for the local health-check probe (e.g. `"/healthz"`). Defaults to `"/health"`. |
| `raw_data_path` | `str \| None` | Raw data path for the app. For local serving, sets ctx().raw_data_path so apps can read it. Defaults to `/tmp/flyte/raw_data` when mode is local. For remote serving, the backend provides this via the container command. |

**Returns**

_Serve: Serve context manager with configured settings


**Raises**

| Exception | Description |
|-|-|
| `NotImplementedError` | If called from a notebook/interactive environment (remote mode only) |

> [!NOTE]
> - Apps do not support pickle-based bundling (interactive mode)
> - LOG_LEVEL and LOG_FORMAT are automatically set as env vars if not explicitly provided in env_vars
> - The env_vars and cluster_pool overrides mutate the app IDL after creation
> - This is a temporary solution until the API natively supports these fields

