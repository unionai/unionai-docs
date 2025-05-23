---
title: flytekit.configuration
version: 0.1.dev2192+g7c539c3.d20250403
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.configuration


# Configuration

## Flytekit Configuration Sources

There are multiple ways to configure flytekit settings:

### Command Line Arguments
This is the recommended way of setting configuration values for many cases. For example, see `pyflyte package` command.

### Python Config Object
A `Config` object can be used directly, e.g. when initializing a `FlyteRemote` object. See the Control Plane design docs for examples on how to specify a `Config` object.

### Environment Variables
Users can specify these at compile time, but when your task is run, Flyte Propeller will also set configuration to ensure correct interaction with the platform. The environment variables must be specified with the format `FLYTE_{SECTION}_{OPTION}`, all in upper case. For example, to specify the `PlatformConfig.endpoint` setting, the environment variable would be `FLYTE_PLATFORM_URL`.

> [!NOTE]
> Environment variables won't work for image configuration, which need to be specified with the `pyflyte package --image ...` option or in a configuration file.

### YAML Format Configuration File
A configuration file that contains settings for both `flytectl` and `flytekit`. This is the recommended configuration file format. Invoke the `flytectl config init` command to create a boilerplate `~/.flyte/config.yaml` file, and `flytectl --help` to learn about all of the configuration yaml options.

Example `config.yaml` file:
```yaml
# Sample config file

admin:
  # For GRPC endpoints you might want to use dns:///flyte.myexample.com
  endpoint: dns:///localhost:8089
  authType: Pkce
  insecure: true

logger:
  show-source: true
  level: 0

console:
  endpoint: http://localhost:8080
  insecure: true

# This section is used only in the control plane to trigger a remote execution
storage:
  type: minio
  stow:
    kind: s3
    config:
      auth_type: accesskey
      access_key_id: minio
      secret_key: miniostorage
      endpoint: http://localhost:9000
      region: us-east-1
      disable_ssl: true
      addressing_style: "path"


### INI Format Configuration File
A configuration file for `flytekit`. By default, `flytekit` will look for a file in two places:

1. First, a file named `flytekit.config` in the Python interpreter's working directory.
2. A file in `~/.flyte/config` in the home directory as detected by Python.

Example `flytekit.config` file:
```ini
[sdk]
workflow_packages=my_cool_workflows, other_workflows
```

> [!WARNING]
> The INI format configuration is considered a legacy configuration format. We recommend using the yaml format instead if you're using a configuration file.

## How is configuration used?

Configuration usage can roughly be bucketed into the following areas:

- **Compile-time settings**: these are settings like the default image and named images, where to look for Flyte code, etc.
- **Platform settings**: Where to find the Flyte backend (Admin DNS, whether to use SSL)
- **Registration Run-time settings**: these are things like the K8s service account to use, a specific S3/GCS bucket to write off-loaded data (dataframes and files) to, notifications, labels & annotations, etc.
- **Data access settings**: Is there a custom S3 endpoint in use? Backoff/retry behavior for accessing S3/GCS, key and password, etc.
- **Other settings** - Statsd configuration, which is a run-time applicable setting but is not necessarily relevant to the Flyte platform.

## Configuration Objects

The following objects are encapsulated in a parent object called `Config`:

### Serialization Time Settings

These are serialization/compile-time settings that are used when using commands like `pyflyte package` or `pyflyte register`. These configuration settings are typically passed in as flags to the above CLI commands.

The image configurations are typically either passed in via an `--image` flag, or can be specified in the `yaml` or `ini` configuration files (see examples above).

- **Image**: Represents a container image with optional configuration overrides.
- **ImageConfig**: Represents an image configuration for a given project/domain combination.
- **SerializationSettings**: Controls how to serialize Flyte entities when registering with Admin.
- **FastSerializationSettings**: Configuration for faster serialization settings.

### Execution Time Settings

Users typically shouldn't be concerned with these configurations, as they are typically set by FlytePropeller or FlyteAdmin. The configurations below are useful for authenticating to a Flyte backend, configuring data access credentials, secrets, and statsd metrics.

- **PlatformConfig**: Configuration for how to connect to the Flyte platform.
- **StatsConfig**: Configuration for how to emit statsd metrics.
- **SecretsConfig**: Configuration for how to access secrets.
- **S3Config**: Amazon S3 specific configuration.
- **GCSConfig**: Google Cloud Storage specific configuration.
- **DataConfig**: Configuration for data access.


## Directory

### Classes

| Class | Description |
|-|-|
| [`AzureBlobStorageConfig`](.././flytekit.configuration#flytekitconfigurationazureblobstorageconfig) | Any Azure Blob Storage specific configuration. |
| [`Config`](flytekit.configuration#flytekitconfigurationconfig) | This the parent configuration object and holds all the underlying configuration object types. |
| [`DataConfig`](.././flytekit.configuration#flytekitconfigurationdataconfig) | Any data storage specific configuration. |
| [`EntrypointSettings`](.././flytekit.configuration#flytekitconfigurationentrypointsettings) | This object carries information about the path of the entrypoint command that will be invoked at runtime. |
| [`FastSerializationSettings`](.././flytekit.configuration#flytekitconfigurationfastserializationsettings) | This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`GCSConfig`](.././flytekit.configuration#flytekitconfigurationgcsconfig) | Any GCS specific configuration. |
| [`GenericPersistenceConfig`](.././flytekit.configuration#flytekitconfigurationgenericpersistenceconfig) | Data storage configuration that applies across any provider. |
| [`Image`](.././flytekit.configuration#flytekitconfigurationimage) | Image is a structured wrapper for task container images used in object serialization. |
| [`ImageConfig`](.././flytekit.configuration#flytekitconfigurationimageconfig) | We recommend you to use ImageConfig. |
| [`LocalConfig`](.././flytekit.configuration#flytekitconfigurationlocalconfig) | Any configuration specific to local runs. |
| [`PlatformConfig`](.././flytekit.configuration#flytekitconfigurationplatformconfig) | This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`S3Config`](.././flytekit.configuration#flytekitconfigurations3config) | S3 specific configuration. |
| [`SecretsConfig`](.././flytekit.configuration#flytekitconfigurationsecretsconfig) | Configuration for secrets. |
| [`SerializationSettings`](.././flytekit.configuration#flytekitconfigurationserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`StatsConfig`](.././flytekit.configuration#flytekitconfigurationstatsconfig) | Configuration for sending statsd. |

### Variables

| Property | Type | Description |
|-|-|-|
| `DEFAULT_FLYTEKIT_ENTRYPOINT_FILELOC` | `str` |  |
| `DEFAULT_IMAGE_NAME` | `str` |  |
| `DEFAULT_IN_CONTAINER_SRC_PATH` | `str` |  |
| `DEFAULT_RUNTIME_PYTHON_INTERPRETER` | `str` |  |
| `DOMAIN_PLACEHOLDER` | `str` |  |
| `PROJECT_PLACEHOLDER` | `str` |  |
| `SERIALIZED_CONTEXT_ENV_VAR` | `str` |  |
| `VERSION_PLACEHOLDER` | `str` |  |

## flytekit.configuration.AzureBlobStorageConfig

Any Azure Blob Storage specific configuration.


```python
class AzureBlobStorageConfig(
    account_name: typing.Optional[str],
    account_key: typing.Optional[str],
    tenant_id: typing.Optional[str],
    client_id: typing.Optional[str],
    client_secret: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `account_name` | `typing.Optional[str]` |
| `account_key` | `typing.Optional[str]` |
| `tenant_id` | `typing.Optional[str]` |
| `client_id` | `typing.Optional[str]` |
| `client_secret` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> GCSConfig
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.Config

This the parent configuration object and holds all the underlying configuration object types. An instance of
this object holds all the config necessary to

1. Interactive session with Flyte backend
2. Some parts are required for Serialization, for example Platform Config is not required
3. Runtime of a task



```python
class Config(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
)
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `secrets` | `SecretsConfig` |
| `stats` | `StatsConfig` |
| `data_config` | `DataConfig` |
| `local_sandbox_path` | `str` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically constructs the Config Object. |
| [`for_endpoint()`](#for_endpoint) | Creates an automatic config for the given endpoint and uses the config_file or environment variable for default. |
| [`for_sandbox()`](#for_sandbox) | Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox`. |
| [`with_params()`](#with_params) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
) -> n: Config
```
Automatically constructs the Config Object. The order of precedence is as follows
  1. first try to find any env vars that match the config vars specified in the FLYTE_CONFIG format.
  2. If not found in environment then values ar read from the config file
  3. If not found in the file, then the default values are used.



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
    data_config: typing.Optional[DataConfig],
    config_file: typing.Union[str, ConfigFile],
) -> n: Config
```
Creates an automatic config for the given endpoint and uses the config_file or environment variable for default.
Refer to `Config.auto()` to understand the default bootstrap behavior.

data_config can be used to configure how data is downloaded or uploaded to a specific Blob storage like S3 / GCS etc.
But, for permissions to a specific backend just use Cloud providers reqcommendation. If using fsspec, then
refer to fsspec documentation


| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `data_config` | `typing.Optional[DataConfig]` |
| `config_file` | `typing.Union[str, ConfigFile]` |

#### for_sandbox()

```python
def for_sandbox()
```
Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox`.
If you are using a hosted Sandbox like environment, then you may need to use port-forward or ingress urls
:return: Config


#### with_params()

```python
def with_params(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
) -> Config
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `secrets` | `SecretsConfig` |
| `stats` | `StatsConfig` |
| `data_config` | `DataConfig` |
| `local_sandbox_path` | `str` |

## flytekit.configuration.DataConfig

Any data storage specific configuration. Please do not use this to store secrets, in S3 case, as it is used in
Flyte sandbox environment we store the access key id and secret.
All DataPersistence plugins are passed all DataConfig and the plugin should correctly use the right config


```python
class DataConfig(
    s3: S3Config,
    gcs: GCSConfig,
    azure: AzureBlobStorageConfig,
    generic: GenericPersistenceConfig,
)
```
| Parameter | Type |
|-|-|
| `s3` | `S3Config` |
| `gcs` | `GCSConfig` |
| `azure` | `AzureBlobStorageConfig` |
| `generic` | `GenericPersistenceConfig` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> DataConfig
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.EntrypointSettings

This object carries information about the path of the entrypoint command that will be invoked at runtime.
This is where `pyflyte-execute` code can be found. This is useful for cases like pyspark execution.


```python
class EntrypointSettings(
    path: Optional[str],
)
```
| Parameter | Type |
|-|-|
| `path` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

## flytekit.configuration.FastSerializationSettings

This object hold information about settings necessary to serialize an object so that it can be fast-registered.


```python
class FastSerializationSettings(
    enabled: bool,
    destination_dir: Optional[str],
    distribution_location: Optional[str],
)
```
| Parameter | Type |
|-|-|
| `enabled` | `bool` |
| `destination_dir` | `Optional[str]` |
| `distribution_location` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

## flytekit.configuration.GCSConfig

Any GCS specific configuration.


```python
class GCSConfig(
    gsutil_parallelism: bool,
)
```
| Parameter | Type |
|-|-|
| `gsutil_parallelism` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> GCSConfig
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.GenericPersistenceConfig

Data storage configuration that applies across any provider.


```python
class GenericPersistenceConfig(
    attach_execution_metadata: bool,
)
```
| Parameter | Type |
|-|-|
| `attach_execution_metadata` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> GCSConfig
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.Image

Image is a structured wrapper for task container images used in object serialization.

Attributes:
    name (str): A user-provided name to identify this image.
    fqn (str): Fully qualified image name. This consists of
        #. a registry location
        #. a username
        #. a repository name
        For example: `hostname/username/reponame`
    tag (str): Optional tag used to specify which version of an image to pull
    digest (str): Optional digest used to specify which version of an image to pull


```python
class Image(
    name: str,
    fqn: str,
    tag: Optional[str],
    digest: Optional[str],
)
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `fqn` | `str` |
| `tag` | `Optional[str]` |
| `digest` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`look_up_image_info()`](#look_up_image_info) | Creates an `Image` object from an image identifier string or a path to an ImageSpec yaml file. |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### look_up_image_info()

```python
def look_up_image_info(
    name: str,
    image_identifier: str,
    allow_no_tag_or_digest: bool,
) -> e: Image
```
Creates an `Image` object from an image identifier string or a path to an ImageSpec yaml file.

This function is used when registering tasks/workflows with Admin. When using
the canonical Python-based development cycle, the version that is used to
register workflows and tasks with Admin should be the version of the image
itself, which should ideally be something unique like the git revision SHA1 of
the latest commit.



| Parameter | Type |
|-|-|
| `name` | `str` |
| `image_identifier` | `str` |
| `allow_no_tag_or_digest` | `bool` |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

### Properties

| Property | Type | Description |
|-|-|-|
| `full` |  | {{< multiline >}}"
Return the full image name with tag or digest, whichever is available.

When using a tag the separator is `:` and when using a digest the separator is `@`.
{{< /multiline >}} |
| `version` |  | {{< multiline >}}Return the version of the image. This could be the tag or digest, whichever is available.
{{< /multiline >}} |

## flytekit.configuration.ImageConfig

We recommend you to use ImageConfig.auto(img_name=None) to create an ImageConfig.
For example, ImageConfig.auto(img_name=""ghcr.io/flyteorg/flytecookbook:v1.0.0"") will create an ImageConfig.

ImageConfig holds available images which can be used at registration time. A default image can be specified
along with optional additional images. Each image in the config must have a unique name.

Attributes:
    default_image (Optional[Image]): The default image to be used as a container for task serialization.
    images (List[Image]): Optional, additional images which can be used in task container definitions.


```python
class ImageConfig(
    default_image: Optional[Image],
    images: Optional[List[Image]],
)
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `images` | `Optional[List[Image]]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from config file or from img_name. |
| [`auto_default_image()`](#auto_default_image) |  |
| [`create_from()`](#create_from) |  |
| [`find_image()`](#find_image) | Return an image, by name, if it exists. |
| [`from_dict()`](#from_dict) |  |
| [`from_images()`](#from_images) | Allows you to programmatically create an ImageConfig. |
| [`from_json()`](#from_json) |  |
| [`schema()`](#schema) |  |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |
| [`validate_image()`](#validate_image) | Validates the image to match the standard format. |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
    img_name: Optional[str],
) -> n:
```
Reads from config file or from img_name
Note that this function does not take into account the flytekit default images (see the Dockerfiles at the
base of this repo). To pick those up, see the auto_default_image function..



| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` |
| `img_name` | `Optional[str]` |

#### auto_default_image()

```python
def auto_default_image()
```
#### create_from()

```python
def create_from(
    default_image: Optional[Image],
    other_images: typing.Optional[typing.List[Image]],
) -> ImageConfig
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `other_images` | `typing.Optional[typing.List[Image]]` |

#### find_image()

```python
def find_image(
    name,
) -> Optional[Image]
```
Return an image, by name, if it exists.


| Parameter | Type |
|-|-|
| `name` |  |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_images()

```python
def from_images(
    default_image: str,
    m: typing.Optional[typing.Dict[str, str]],
)
```
Allows you to programmatically create an ImageConfig. Usually only the default_image is required, unless
your workflow uses multiple images

```python
ImageConfig.from_dict(
    "ghcr.io/flyteorg/flytecookbook:v1.0.0",
    {
        "spark": "ghcr.io/flyteorg/myspark:...",
        "other": "...",
    }
)
```

urn:


| Parameter | Type |
|-|-|
| `default_image` | `str` |
| `m` | `typing.Optional[typing.Dict[str, str]]` |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

#### validate_image()

```python
def validate_image(
    _: typing.Any,
    param: str,
    values: tuple,
) -> n:
```
Validates the image to match the standard format. Also validates that only one default image
is provided. a default image, is one that is specified as ``default=<image_uri>`` or just ``<image_uri>``. All
other images should be provided with a name, in the format ``name=<image_uri>`` This method can be used with the
CLI



| Parameter | Type |
|-|-|
| `_` | `typing.Any` |
| `param` | `str` |
| `values` | `tuple` |

## flytekit.configuration.LocalConfig

Any configuration specific to local runs.


```python
class LocalConfig(
    cache_enabled: bool,
    cache_overwrite: bool,
)
```
| Parameter | Type |
|-|-|
| `cache_enabled` | `bool` |
| `cache_overwrite` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) |  |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> LocalConfig
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.PlatformConfig

This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically).



```python
class PlatformConfig(
    endpoint: str,
    insecure: bool,
    insecure_skip_verify: bool,
    ca_cert_file_path: typing.Optional[str],
    console_endpoint: typing.Optional[str],
    command: typing.Optional[typing.List[str]],
    proxy_command: typing.Optional[typing.List[str]],
    client_id: typing.Optional[str],
    client_credentials_secret: typing.Optional[str],
    scopes: List[str],
    auth_mode: AuthType,
    audience: typing.Optional[str],
    rpc_retries: int,
    http_proxy_url: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |
| `insecure_skip_verify` | `bool` |
| `ca_cert_file_path` | `typing.Optional[str]` |
| `console_endpoint` | `typing.Optional[str]` |
| `command` | `typing.Optional[typing.List[str]]` |
| `proxy_command` | `typing.Optional[typing.List[str]]` |
| `client_id` | `typing.Optional[str]` |
| `client_credentials_secret` | `typing.Optional[str]` |
| `scopes` | `List[str]` |
| `auth_mode` | `AuthType` |
| `audience` | `typing.Optional[str]` |
| `rpc_retries` | `int` |
| `http_proxy_url` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from Config file, and overrides from Environment variables. |
| [`for_endpoint()`](#for_endpoint) |  |


#### auto()

```python
def auto(
    config_file: typing.Optional[typing.Union[str, ConfigFile]],
) -> n:
```
Reads from Config file, and overrides from Environment variables. Refer to ConfigEntry for details


| Parameter | Type |
|-|-|
| `config_file` | `typing.Optional[typing.Union[str, ConfigFile]]` |

#### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
) -> PlatformConfig
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |

## flytekit.configuration.S3Config

S3 specific configuration


```python
class S3Config(
    enable_debug: bool,
    endpoint: typing.Optional[str],
    retries: int,
    backoff: datetime.timedelta,
    access_key_id: typing.Optional[str],
    secret_access_key: typing.Optional[str],
)
```
| Parameter | Type |
|-|-|
| `enable_debug` | `bool` |
| `endpoint` | `typing.Optional[str]` |
| `retries` | `int` |
| `backoff` | `datetime.timedelta` |
| `access_key_id` | `typing.Optional[str]` |
| `secret_access_key` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically configure. |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> n: Config
```
Automatically configure


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.SecretsConfig

Configuration for secrets.



```python
class SecretsConfig(
    env_prefix: str,
    default_dir: str,
    file_prefix: str,
)
```
| Parameter | Type |
|-|-|
| `env_prefix` | `str` |
| `default_dir` | `str` |
| `file_prefix` | `str` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from environment variable or from config file. |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> n:
```
Reads from environment variable or from config file


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.SerializationSettings

These settings are provided while serializing a workflow and task, before registration. This is required to get
runtime information at serialization time, as well as some defaults.

Attributes:
    project (str): The project (if any) with which to register entities under.
    domain (str): The domain (if any) with which to register entities under.
    version (str): The version (if any) with which to register entities under.
    image_config (ImageConfig): The image config used to define task container images.
    env (Optional[Dict[str, str]]): Environment variables injected into task container definitions.
    flytekit_virtualenv_root (Optional[str]):  During out of container serialize the absolute path of the flytekit
        virtualenv at serialization time won't match the in-container value at execution time. This optional value
        is used to provide the in-container virtualenv path
    python_interpreter (Optional[str]): The python executable to use. This is used for spark tasks in out of
        container execution.
    entrypoint_settings (Optional[EntrypointSettings]): Information about the command, path and version of the
        entrypoint program.
    fast_serialization_settings (Optional[FastSerializationSettings]): If the code is being serialized so that it
        can be fast registered (and thus omit building a Docker image) this object contains additional parameters
        for serialization.
    source_root (Optional[str]): The root directory of the source code.


```python
class SerializationSettings(
    image_config: ImageConfig,
    project: typing.Optional[str],
    domain: typing.Optional[str],
    version: typing.Optional[str],
    env: Optional[Dict[str, str]],
    git_repo: Optional[str],
    python_interpreter: str,
    flytekit_virtualenv_root: Optional[str],
    fast_serialization_settings: Optional[FastSerializationSettings],
    source_root: Optional[str],
)
```
| Parameter | Type |
|-|-|
| `image_config` | `ImageConfig` |
| `project` | `typing.Optional[str]` |
| `domain` | `typing.Optional[str]` |
| `version` | `typing.Optional[str]` |
| `env` | `Optional[Dict[str, str]]` |
| `git_repo` | `Optional[str]` |
| `python_interpreter` | `str` |
| `flytekit_virtualenv_root` | `Optional[str]` |
| `fast_serialization_settings` | `Optional[FastSerializationSettings]` |
| `source_root` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`default_entrypoint_settings()`](#default_entrypoint_settings) | Assumes the entrypoint is installed in a virtual-environment where the interpreter is. |
| [`for_image()`](#for_image) |  |
| [`from_dict()`](#from_dict) |  |
| [`from_json()`](#from_json) |  |
| [`from_transport()`](#from_transport) |  |
| [`new_builder()`](#new_builder) | Creates a ``SerializationSettings. |
| [`schema()`](#schema) |  |
| [`should_fast_serialize()`](#should_fast_serialize) | Whether or not the serialization settings specify that entities should be serialized for fast registration. |
| [`to_dict()`](#to_dict) |  |
| [`to_json()`](#to_json) |  |
| [`venv_root_from_interpreter()`](#venv_root_from_interpreter) | Computes the path of the virtual environment root, based on the passed in python interpreter path. |
| [`with_serialized_context()`](#with_serialized_context) | Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext. |


#### default_entrypoint_settings()

```python
def default_entrypoint_settings(
    interpreter_path: str,
) -> EntrypointSettings
```
Assumes the entrypoint is installed in a virtual-environment where the interpreter is


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### for_image()

```python
def for_image(
    image: str,
    version: str,
    project: str,
    domain: str,
    python_interpreter_path: str,
) -> SerializationSettings
```
| Parameter | Type |
|-|-|
| `image` | `str` |
| `version` | `str` |
| `project` | `str` |
| `domain` | `str` |
| `python_interpreter_path` | `str` |

#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
) -> ~A
```
| Parameter | Type |
|-|-|
| `kvs` | `typing.Union[dict, list, str, int, float, bool, NoneType]` |
| `infer_missing` |  |

#### from_json()

```python
def from_json(
    s: typing.Union[str, bytes, bytearray],
    parse_float,
    parse_int,
    parse_constant,
    infer_missing,
    kw,
) -> ~A
```
| Parameter | Type |
|-|-|
| `s` | `typing.Union[str, bytes, bytearray]` |
| `parse_float` |  |
| `parse_int` |  |
| `parse_constant` |  |
| `infer_missing` |  |
| `kw` |  |

#### from_transport()

```python
def from_transport(
    s: str,
) -> SerializationSettings
```
| Parameter | Type |
|-|-|
| `s` | `str` |

#### new_builder()

```python
def new_builder()
```
Creates a ``SerializationSettings.Builder`` that copies the existing serialization settings parameters and
allows for customization.


#### schema()

```python
def schema(
    infer_missing: bool,
    only,
    exclude,
    many: bool,
    context,
    load_only,
    dump_only,
    partial: bool,
    unknown,
) -> SchemaType[A]
```
| Parameter | Type |
|-|-|
| `infer_missing` | `bool` |
| `only` |  |
| `exclude` |  |
| `many` | `bool` |
| `context` |  |
| `load_only` |  |
| `dump_only` |  |
| `partial` | `bool` |
| `unknown` |  |

#### should_fast_serialize()

```python
def should_fast_serialize()
```
Whether or not the serialization settings specify that entities should be serialized for fast registration.


#### to_dict()

```python
def to_dict(
    encode_json,
) -> typing.Dict[str, typing.Union[dict, list, str, int, float, bool, NoneType]]
```
| Parameter | Type |
|-|-|
| `encode_json` |  |

#### to_json()

```python
def to_json(
    skipkeys: bool,
    ensure_ascii: bool,
    check_circular: bool,
    allow_nan: bool,
    indent: typing.Union[int, str, NoneType],
    separators: typing.Tuple[str, str],
    default: typing.Callable,
    sort_keys: bool,
    kw,
) -> str
```
| Parameter | Type |
|-|-|
| `skipkeys` | `bool` |
| `ensure_ascii` | `bool` |
| `check_circular` | `bool` |
| `allow_nan` | `bool` |
| `indent` | `typing.Union[int, str, NoneType]` |
| `separators` | `typing.Tuple[str, str]` |
| `default` | `typing.Callable` |
| `sort_keys` | `bool` |
| `kw` |  |

#### venv_root_from_interpreter()

```python
def venv_root_from_interpreter(
    interpreter_path: str,
) -> str
```
Computes the path of the virtual environment root, based on the passed in python interpreter path
for example /opt/venv/bin/python3 -> /opt/venv


| Parameter | Type |
|-|-|
| `interpreter_path` | `str` |

#### with_serialized_context()

```python
def with_serialized_context()
```
Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext
This is useful in transporting SerializedContext to serialized and registered tasks.
The setting will be available in the `env` field with the key `SERIALIZED_CONTEXT_ENV_VAR`
:return: A newly constructed SerializationSettings, or self, if it already has the serializationSettings


### Properties

| Property | Type | Description |
|-|-|-|
| `entrypoint_settings` |  |  |
| `serialized_context` |  | {{< multiline >}}:return: returns the serialization context as a base64encoded, gzip compressed, json strinnn
{{< /multiline >}} |

## flytekit.configuration.StatsConfig

Configuration for sending statsd.



```python
class StatsConfig(
    host: str,
    port: int,
    disabled: bool,
    disabled_tags: bool,
)
```
| Parameter | Type |
|-|-|
| `host` | `str` |
| `port` | `int` |
| `disabled` | `bool` |
| `disabled_tags` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from environment variable, followed by ConfigFile provided. |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
) -> n:
```
Reads from environment variable, followed by ConfigFile provided


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

