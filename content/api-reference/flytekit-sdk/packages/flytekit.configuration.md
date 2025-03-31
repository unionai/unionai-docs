---
title: flytekit.configuration
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.configuration


=====================
Configuration
=====================

.. currentmodule:: flytekit.configuration

Flytekit Configuration Sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are multiple ways to configure flytekit settings:

**Command Line Arguments**: This is the recommended way of setting configuration values for many cases.
For example, see `pyflyte package <pyflyte.html#pyflyte-package>`_ command.

**Python Config Object**: A :py:class:`~flytekit.configuration.Config` object can by used directly, e.g. when
initializing a :py:class:`~flytefit.remote.remote.FlyteRemote` object. See :doc:`here <design/control_plane>` for examples on
how to specify a ``Config`` object.

**Environment Variables**: Users can specify these at compile time, but when your task is run, Flyte Propeller will
also set configuration to ensure correct interaction with the platform. The environment variables must be specified
with the format ``FLYTE_{SECTION}_{OPTION}``, all in upper case. For example, to specify the
:py:class:`PlatformConfig.endpoint <flytekit.configuration.PlatformConfig>` setting, the environment variable would
be ``FLYTE_PLATFORM_URL``.

.. note::

   Environment variables won't work for image configuration, which need to be specified with the
   `pyflyte package --image ... <pyflyte.html#cmdoption-pyflyte-package-i>`_ option or in a configuration
   file.

**YAML Format Configuration File**: A configuration file that contains settings for both
`flytectl <https://docs.flyte.org/en/latest/flytectl/api/overview.html>`__ and ``flytekit``. This is the recommended configuration
file format. Invoke the :ref:`flytectl config init <flytectl_config_init>` command to create a boilerplate
``~/.flyte/config.yaml`` file, and  ``flytectl --help`` to learn about all of the configuration yaml options.

.. dropdown:: See example ``config.yaml`` file
   :animate: fade-in-slide-down

   .. literalinclude:: ../../tests/flytekit/unit/configuration/configs/sample.yaml
      :language: yaml
      :caption: config.yaml

**INI Format Configuration File**: A configuration file for ``flytekit``. By default, ``flytekit`` will look for a
file in two places:

1. First, a file named ``flytekit.config`` in the Python interpreter's working directory.
2. A file in ``~/.flyte/config`` in the home directory as detected by Python.

.. dropdown:: See example ``flytekit.config`` file
   :animate: fade-in-slide-down

   .. literalinclude:: ../../tests/flytekit/unit/configuration/configs/images.config
      :language: ini
      :caption: flytekit.config

.. warning::

   The INI format configuration is considered a legacy configuration format. We recommend using the yaml format
   instead if you're using a configuration file.

How is configuration used?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Configuration usage can roughly be bucketed into the following areas,

- **Compile-time settings**: these are settings like the default image and named images, where to look for Flyte code, etc.
- **Platform settings**: Where to find the Flyte backend (Admin DNS, whether to use SSL)
- **Registration Run-time settings**: these are things like the K8s service account to use, a specific S3/GCS bucket to write off-loaded data (dataframes and files) to, notifications, labels & annotations, etc.
- **Data access settings**: Is there a custom S3 endpoint in use? Backoff/retry behavior for accessing S3/GCS, key and password, etc.
- **Other settings** - Statsd configuration, which is a run-time applicable setting but is not necessarily relevant to the Flyte platform.

Configuration Objects
---------------------

The following objects are encapsulated in a parent object called ``Config``.

.. autosummary::
   :template: custom.rst
   :toctree: generated/
   :nosignatures:

   ~Config

.. _configuration-compile-time-settings:

Serialization Time Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are serialization/compile-time settings that are used when using commands like
`pyflyte package <pyflyte.html#pyflyte-package>`_ or `pyflyte register <pyflyte.html#pyflyte-register>`_. These
configuration settings are typically passed in as flags to the above CLI commands.

The image configurations are typically either passed in via an `--image <pyflyte.html#cmdoption-pyflyte-package-i>`_ flag,
or can be specified in the ``yaml`` or ``ini`` configuration files (see examples above).

.. autosummary::
   :template: custom.rst
   :toctree: generated/
   :nosignatures:

   ~Image
   ~ImageConfig
   ~SerializationSettings
   ~FastSerializationSettings

.. _configuration-execution-time-settings:

Execution Time Settings
^^^^^^^^^^^^^^^^^^^^^^^

Users typically shouldn't be concerned with these configurations, as they are typically set by FlytePropeller or
FlyteAdmin. The configurations below are useful for authenticating to a Flyte backend, configuring data access
credentials, secrets, and statsd metrics.

.. autosummary::
   :template: custom.rst
   :toctree: generated/
   :nosignatures:

   ~PlatformConfig
   ~StatsConfig
   ~SecretsConfig
   ~S3Config
   ~GCSConfig
   ~DataConfig


## Directory

### Classes

| Class | Description |
|-|-|
| [`AuthType`](.././flytekit.configuration#flytekitconfigurationauthtype) | Create a collection of name/value pairs. |
| [`AzureBlobStorageConfig`](.././flytekit.configuration#flytekitconfigurationazureblobstorageconfig) | Any Azure Blob Storage specific configuration. |
| [`BytesIO`](.././flytekit.configuration#flytekitconfigurationbytesio) | Buffered I/O implementation using an in-memory bytes buffer. |
| [`Config`](.././flytekit.configuration#flytekitconfigurationconfig) | This the parent configuration object and holds all the underlying configuration object types. |
| [`ConfigEntry`](.././flytekit.configuration#flytekitconfigurationconfigentry) | A top level Config entry holder, that holds multiple different representations of the config. |
| [`ConfigFile`](.././flytekit.configuration#flytekitconfigurationconfigfile) | None. |
| [`DataClassJsonMixin`](.././flytekit.configuration#flytekitconfigurationdataclassjsonmixin) | DataClassJsonMixin is an ABC that functions as a Mixin. |
| [`DataConfig`](.././flytekit.configuration#flytekitconfigurationdataconfig) | Any data storage specific configuration. |
| [`DefaultImages`](.././flytekit.configuration#flytekitconfigurationdefaultimages) | We may want to load the default images from remote - maybe s3 location etc?. |
| [`EntrypointSettings`](.././flytekit.configuration#flytekitconfigurationentrypointsettings) | This object carries information about the path of the entrypoint command that will be invoked at runtime. |
| [`FastSerializationSettings`](.././flytekit.configuration#flytekitconfigurationfastserializationsettings) | This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`GCSConfig`](.././flytekit.configuration#flytekitconfigurationgcsconfig) | Any GCS specific configuration. |
| [`GenericPersistenceConfig`](.././flytekit.configuration#flytekitconfigurationgenericpersistenceconfig) | Data storage configuration that applies across any provider. |
| [`Image`](.././flytekit.configuration#flytekitconfigurationimage) | Image is a structured wrapper for task container images used in object serialization. |
| [`ImageBuildEngine`](.././flytekit.configuration#flytekitconfigurationimagebuildengine) | ImageBuildEngine contains a list of builders that can be used to build an ImageSpec. |
| [`ImageConfig`](.././flytekit.configuration#flytekitconfigurationimageconfig) | We recommend you to use ImageConfig. |
| [`ImageSpec`](.././flytekit.configuration#flytekitconfigurationimagespec) | This class is used to specify the docker image that will be used to run the task. |
| [`LocalConfig`](.././flytekit.configuration#flytekitconfigurationlocalconfig) | Any configuration specific to local runs. |
| [`PlatformConfig`](.././flytekit.configuration#flytekitconfigurationplatformconfig) | This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`S3Config`](.././flytekit.configuration#flytekitconfigurations3config) | S3 specific configuration. |
| [`SecretsConfig`](.././flytekit.configuration#flytekitconfigurationsecretsconfig) | Configuration for secrets. |
| [`SerializationSettings`](.././flytekit.configuration#flytekitconfigurationserializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`StatsConfig`](.././flytekit.configuration#flytekitconfigurationstatsconfig) | Configuration for sending statsd. |

## flytekit.configuration.AuthType

Create a collection of name/value pairs.

Example enumeration:

>>> class Color(Enum):
...     RED = 1
...     BLUE = 2
...     GREEN = 3

Access them by:

- attribute access:

>>> Color.RED
<Color.RED: 1>

- value lookup:

>>> Color(1)
<Color.RED: 1>

- name lookup:

>>> Color['RED']
<Color.RED: 1>

Enumerations can be iterated over, and know how many members they have:

>>> len(Color)
3

>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

Methods can be added to enumerations, and members can have their own
attributes -- see the documentation for details.


## flytekit.configuration.AzureBlobStorageConfig

Any Azure Blob Storage specific configuration.


```python
def AzureBlobStorageConfig(
    account_name: typing.Optional[str],
    account_key: typing.Optional[str],
    tenant_id: typing.Optional[str],
    client_id: typing.Optional[str],
    client_secret: typing.Optional[str],
):
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
| [`auto()`](#auto) | None |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.BytesIO

Buffered I/O implementation using an in-memory bytes buffer.


## flytekit.configuration.Config

This the parent configuration object and holds all the underlying configuration object types. An instance of
this object holds all the config necessary to

1. Interactive session with Flyte backend
2. Some parts are required for Serialization, for example Platform Config is not required
3. Runtime of a task



```python
def Config(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
):
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
| [`auto()`](#auto) | Automatically constructs the Config Object |
| [`for_endpoint()`](#for_endpoint) | Creates an automatic config for the given endpoint and uses the config_file or environment variable for default |
| [`for_sandbox()`](#for_sandbox) | Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox` |
| [`with_params()`](#with_params) | None |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
):
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
):
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
):
```
| Parameter | Type |
|-|-|
| `platform` | `PlatformConfig` |
| `secrets` | `SecretsConfig` |
| `stats` | `StatsConfig` |
| `data_config` | `DataConfig` |
| `local_sandbox_path` | `str` |

## flytekit.configuration.ConfigEntry

A top level Config entry holder, that holds multiple different representations of the config.
Legacy means the INI style config files. YAML support is for the flytectl config file, which is there by default
when flytectl starts a sandbox


```python
def ConfigEntry(
    legacy: LegacyConfigEntry,
    yaml_entry: typing.Optional[YamlConfigEntry],
    transform: typing.Optional[typing.Callable[[str], typing.Any]],
):
```
| Parameter | Type |
|-|-|
| `legacy` | `LegacyConfigEntry` |
| `yaml_entry` | `typing.Optional[YamlConfigEntry]` |
| `transform` | `typing.Optional[typing.Callable[[str], typing.Any]]` |

### Methods

| Method | Description |
|-|-|
| [`read()`](#read) | Reads the config Entry from the various sources in the following order, |


#### read()

```python
def read(
    cfg: typing.Optional[ConfigFile],
):
```
Reads the config Entry from the various sources in the following order,
#. First try to read from the relevant environment variable,
#. If missing, then try to read from the legacy config file, if one was parsed.
#. If missing, then try to read from the yaml file.

The constructor for ConfigFile currently does not allow specification of both the ini and yaml style formats.



| Parameter | Type |
|-|-|
| `cfg` | `typing.Optional[ConfigFile]` |

## flytekit.configuration.ConfigFile

```python
def ConfigFile(
    location: str,
):
```
Load the config from this location


| Parameter | Type |
|-|-|
| `location` | `str` |

### Methods

| Method | Description |
|-|-|
| [`get()`](#get) | None |


#### get()

```python
def get(
    c: typing.Union[LegacyConfigEntry, YamlConfigEntry],
):
```
| Parameter | Type |
|-|-|
| `c` | `typing.Union[LegacyConfigEntry, YamlConfigEntry]` |

### Properties

| Property | Type | Description |
|-|-|-|
| legacy_config |  |  |
| yaml_config |  |  |

## flytekit.configuration.DataClassJsonMixin

DataClassJsonMixin is an ABC that functions as a Mixin.

As with other ABCs, it should not be instantiated directly.


### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
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
):
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
):
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
):
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
):
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

## flytekit.configuration.DataConfig

Any data storage specific configuration. Please do not use this to store secrets, in S3 case, as it is used in
Flyte sandbox environment we store the access key id and secret.
All DataPersistence plugins are passed all DataConfig and the plugin should correctly use the right config


```python
def DataConfig(
    s3: S3Config,
    gcs: GCSConfig,
    azure: AzureBlobStorageConfig,
    generic: GenericPersistenceConfig,
):
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
| [`auto()`](#auto) | None |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.DefaultImages

We may want to load the default images from remote - maybe s3 location etc?


### Methods

| Method | Description |
|-|-|
| [`default_image()`](#default_image) | None |
| [`find_image_for()`](#find_image_for) | None |
| [`get_version_suffix()`](#get_version_suffix) | None |


#### default_image()

```python
def default_image()
```
#### find_image_for()

```python
def find_image_for(
    python_version: typing.Optional[flytekit.configuration.default_images.PythonVersion],
    flytekit_version: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `python_version` | `typing.Optional[flytekit.configuration.default_images.PythonVersion]` |
| `flytekit_version` | `typing.Optional[str]` |

#### get_version_suffix()

```python
def get_version_suffix()
```
## flytekit.configuration.EntrypointSettings

This object carries information about the path of the entrypoint command that will be invoked at runtime.
This is where `pyflyte-execute` code can be found. This is useful for cases like pyspark execution.


```python
def EntrypointSettings(
    path: Optional[str],
):
```
| Parameter | Type |
|-|-|
| `path` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
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
):
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
):
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
):
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
):
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
def FastSerializationSettings(
    enabled: bool,
    destination_dir: Optional[str],
    distribution_location: Optional[str],
):
```
| Parameter | Type |
|-|-|
| `enabled` | `bool` |
| `destination_dir` | `Optional[str]` |
| `distribution_location` | `Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
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
):
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
):
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
):
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
):
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
def GCSConfig(
    gsutil_parallelism: bool,
):
```
| Parameter | Type |
|-|-|
| `gsutil_parallelism` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | None |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.GenericPersistenceConfig

Data storage configuration that applies across any provider.


```python
def GenericPersistenceConfig(
    attach_execution_metadata: bool,
):
```
| Parameter | Type |
|-|-|
| `attach_execution_metadata` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | None |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
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
def Image(
    name: str,
    fqn: str,
    tag: Optional[str],
    digest: Optional[str],
):
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
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`look_up_image_info()`](#look_up_image_info) | Creates an `Image` object from an image identifier string or a path to an ImageSpec yaml file |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |


#### from_dict()

```python
def from_dict(
    kvs: typing.Union[dict, list, str, int, float, bool, NoneType],
    infer_missing,
):
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
):
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
):
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
):
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
):
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
):
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
| full |  |  |
| version |  |  |

## flytekit.configuration.ImageBuildEngine

ImageBuildEngine contains a list of builders that can be used to build an ImageSpec.


### Methods

| Method | Description |
|-|-|
| [`build()`](#build) | None |
| [`get_registry()`](#get_registry) | None |
| [`register()`](#register) | None |


#### build()

```python
def build(
    image_spec: flytekit.image_spec.image_spec.ImageSpec,
):
```
| Parameter | Type |
|-|-|
| `image_spec` | `flytekit.image_spec.image_spec.ImageSpec` |

#### get_registry()

```python
def get_registry()
```
#### register()

```python
def register(
    builder_type: str,
    image_spec_builder: flytekit.image_spec.image_spec.ImageSpecBuilder,
    priority: int,
):
```
| Parameter | Type |
|-|-|
| `builder_type` | `str` |
| `image_spec_builder` | `flytekit.image_spec.image_spec.ImageSpecBuilder` |
| `priority` | `int` |

## flytekit.configuration.ImageConfig

We recommend you to use ImageConfig.auto(img_name=None) to create an ImageConfig.
For example, ImageConfig.auto(img_name=""ghcr.io/flyteorg/flytecookbook:v1.0.0"") will create an ImageConfig.

ImageConfig holds available images which can be used at registration time. A default image can be specified
along with optional additional images. Each image in the config must have a unique name.

Attributes:
default_image (Optional[Image]): The default image to be used as a container for task serialization.
images (List[Image]): Optional, additional images which can be used in task container definitions.


```python
def ImageConfig(
    default_image: Optional[Image],
    images: Optional[List[Image]],
):
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `images` | `Optional[List[Image]]` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from config file or from img_name |
| [`auto_default_image()`](#auto_default_image) | None |
| [`create_from()`](#create_from) | None |
| [`find_image()`](#find_image) | Return an image, by name, if it exists |
| [`from_dict()`](#from_dict) | None |
| [`from_images()`](#from_images) | Allows you to programmatically create an ImageConfig |
| [`from_json()`](#from_json) | None |
| [`schema()`](#schema) | None |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`validate_image()`](#validate_image) | Validates the image to match the standard format |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
    img_name: Optional[str],
):
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
):
```
| Parameter | Type |
|-|-|
| `default_image` | `Optional[Image]` |
| `other_images` | `typing.Optional[typing.List[Image]]` |

#### find_image()

```python
def find_image(
    name,
):
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
):
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
):
```
Allows you to programmatically create an ImageConfig. Usually only the default_image is required, unless
your workflow uses multiple images

.. code:: python

ImageConfig.from_dict(
"ghcr.io/flyteorg/flytecookbook:v1.0.0",
{
"spark": "ghcr.io/flyteorg/myspark:...",
"other": "...",
}
)

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
):
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
):
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
):
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
):
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
):
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

## flytekit.configuration.ImageSpec

This class is used to specify the docker image that will be used to run the task.



```python
def ImageSpec(
    name: str,
    python_version: str,
    builder: typing.Optional[str],
    source_root: typing.Optional[str],
    env: typing.Optional[typing.Dict[str, str]],
    registry: typing.Optional[str],
    packages: typing.Optional[typing.List[str]],
    conda_packages: typing.Optional[typing.List[str]],
    conda_channels: typing.Optional[typing.List[str]],
    requirements: typing.Optional[str],
    apt_packages: typing.Optional[typing.List[str]],
    cuda: typing.Optional[str],
    cudnn: typing.Optional[str],
    base_image: typing.Union[str, ForwardRef('ImageSpec'), NoneType],
    platform: str,
    pip_index: typing.Optional[str],
    pip_extra_index_url: typing.Optional[typing.List[str]],
    pip_secret_mounts: typing.Optional[typing.List[typing.Tuple[str, str]]],
    pip_extra_args: typing.Optional[str],
    registry_config: typing.Optional[str],
    entrypoint: typing.Optional[typing.List[str]],
    commands: typing.Optional[typing.List[str]],
    tag_format: typing.Optional[str],
    source_copy_mode: typing.Optional[flytekit.constants.CopyFileDetection],
    copy: typing.Optional[typing.List[str]],
    python_exec: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `name` | `str` |
| `python_version` | `str` |
| `builder` | `typing.Optional[str]` |
| `source_root` | `typing.Optional[str]` |
| `env` | `typing.Optional[typing.Dict[str, str]]` |
| `registry` | `typing.Optional[str]` |
| `packages` | `typing.Optional[typing.List[str]]` |
| `conda_packages` | `typing.Optional[typing.List[str]]` |
| `conda_channels` | `typing.Optional[typing.List[str]]` |
| `requirements` | `typing.Optional[str]` |
| `apt_packages` | `typing.Optional[typing.List[str]]` |
| `cuda` | `typing.Optional[str]` |
| `cudnn` | `typing.Optional[str]` |
| `base_image` | `typing.Union[str, ForwardRef('ImageSpec'), NoneType]` |
| `platform` | `str` |
| `pip_index` | `typing.Optional[str]` |
| `pip_extra_index_url` | `typing.Optional[typing.List[str]]` |
| `pip_secret_mounts` | `typing.Optional[typing.List[typing.Tuple[str, str]]]` |
| `pip_extra_args` | `typing.Optional[str]` |
| `registry_config` | `typing.Optional[str]` |
| `entrypoint` | `typing.Optional[typing.List[str]]` |
| `commands` | `typing.Optional[typing.List[str]]` |
| `tag_format` | `typing.Optional[str]` |
| `source_copy_mode` | `typing.Optional[flytekit.constants.CopyFileDetection]` |
| `copy` | `typing.Optional[typing.List[str]]` |
| `python_exec` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`exist()`](#exist) | Check if the image exists in the registry |
| [`force_push()`](#force_push) | Builder that returns a new image spec with force push enabled |
| [`from_env()`](#from_env) | Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment |
| [`image_name()`](#image_name) | Full image name with tag |
| [`is_container()`](#is_container) | Check if the current container image in the pod is built from current image spec |
| [`with_apt_packages()`](#with_apt_packages) | Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process |
| [`with_commands()`](#with_commands) | Builder that returns a new image spec with an additional list of commands that will be executed during the building process |
| [`with_copy()`](#with_copy) | Builder that returns a new image spec with the source files copied to the destination directory |
| [`with_packages()`](#with_packages) | Builder that returns a new image speck with additional python packages that will be installed during the building process |


#### exist()

```python
def exist()
```
Check if the image exists in the registry.
Return True if the image exists in the registry, False otherwise.
Return None if failed to check if the image exists due to the permission issue or other reasons.


#### force_push()

```python
def force_push()
```
Builder that returns a new image spec with force push enabled.


#### from_env()

```python
def from_env(
    pinned_packages: typing.Optional[typing.List[str]],
    kwargs,
):
```
Create ImageSpec with the environment's Python version and packages pinned to the ones in the environment.


| Parameter | Type |
|-|-|
| `pinned_packages` | `typing.Optional[typing.List[str]]` |
| `kwargs` | ``**kwargs`` |

#### image_name()

```python
def image_name()
```
Full image name with tag.


#### is_container()

```python
def is_container()
```
Check if the current container image in the pod is built from current image spec.
:return: True if the current container image in the pod is built from current image spec, False otherwise.


#### with_apt_packages()

```python
def with_apt_packages(
    apt_packages: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with an additional list of apt packages that will be executed during the building process.


| Parameter | Type |
|-|-|
| `apt_packages` | `typing.Union[str, typing.List[str]]` |

#### with_commands()

```python
def with_commands(
    commands: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with an additional list of commands that will be executed during the building process.


| Parameter | Type |
|-|-|
| `commands` | `typing.Union[str, typing.List[str]]` |

#### with_copy()

```python
def with_copy(
    src: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image spec with the source files copied to the destination directory.


| Parameter | Type |
|-|-|
| `src` | `typing.Union[str, typing.List[str]]` |

#### with_packages()

```python
def with_packages(
    packages: typing.Union[str, typing.List[str]],
):
```
Builder that returns a new image speck with additional python packages that will be installed during the building process.


| Parameter | Type |
|-|-|
| `packages` | `typing.Union[str, typing.List[str]]` |

### Properties

| Property | Type | Description |
|-|-|-|
| tag |  |  |

## flytekit.configuration.LocalConfig

Any configuration specific to local runs.


```python
def LocalConfig(
    cache_enabled: bool,
    cache_overwrite: bool,
):
```
| Parameter | Type |
|-|-|
| `cache_enabled` | `bool` |
| `cache_overwrite` | `bool` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | None |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.PlatformConfig

This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically).



```python
def PlatformConfig(
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
):
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
| [`auto()`](#auto) | Reads from Config file, and overrides from Environment variables |
| [`for_endpoint()`](#for_endpoint) | None |


#### auto()

```python
def auto(
    config_file: typing.Optional[typing.Union[str, ConfigFile]],
):
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
):
```
| Parameter | Type |
|-|-|
| `endpoint` | `str` |
| `insecure` | `bool` |

## flytekit.configuration.S3Config

S3 specific configuration


```python
def S3Config(
    enable_debug: bool,
    endpoint: typing.Optional[str],
    retries: int,
    backoff: datetime.timedelta,
    access_key_id: typing.Optional[str],
    secret_access_key: typing.Optional[str],
):
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
| [`auto()`](#auto) | Automatically configure |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
Automatically configure


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

## flytekit.configuration.SecretsConfig

Configuration for secrets.



```python
def SecretsConfig(
    env_prefix: str,
    default_dir: str,
    file_prefix: str,
):
```
| Parameter | Type |
|-|-|
| `env_prefix` | `str` |
| `default_dir` | `str` |
| `file_prefix` | `str` |

### Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Reads from environment variable or from config file |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
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
def SerializationSettings(
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
):
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
| [`default_entrypoint_settings()`](#default_entrypoint_settings) | Assumes the entrypoint is installed in a virtual-environment where the interpreter is |
| [`for_image()`](#for_image) | None |
| [`from_dict()`](#from_dict) | None |
| [`from_json()`](#from_json) | None |
| [`from_transport()`](#from_transport) | None |
| [`new_builder()`](#new_builder) | Creates a ``SerializationSettings |
| [`schema()`](#schema) | None |
| [`should_fast_serialize()`](#should_fast_serialize) | Whether or not the serialization settings specify that entities should be serialized for fast registration |
| [`to_dict()`](#to_dict) | None |
| [`to_json()`](#to_json) | None |
| [`venv_root_from_interpreter()`](#venv_root_from_interpreter) | Computes the path of the virtual environment root, based on the passed in python interpreter path |
| [`with_serialized_context()`](#with_serialized_context) | Use this method to create a new SerializationSettings that has an environment variable set with the SerializedContext |


#### default_entrypoint_settings()

```python
def default_entrypoint_settings(
    interpreter_path: str,
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
):
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
| entrypoint_settings |  |  |
| serialized_context |  |  |

## flytekit.configuration.StatsConfig

Configuration for sending statsd.



```python
def StatsConfig(
    host: str,
    port: int,
    disabled: bool,
    disabled_tags: bool,
):
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
| [`auto()`](#auto) | Reads from environment variable, followed by ConfigFile provided |


#### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile],
):
```
Reads from environment variable, followed by ConfigFile provided


| Parameter | Type |
|-|-|
| `config_file` | `typing.Union[str, ConfigFile]` |

