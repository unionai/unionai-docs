---
title: Config
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Config

**Package:** `flytekit.configuration`

This the parent configuration object and holds all the underlying configuration object types. An instance of
this object holds all the config necessary to

1. Interactive session with Flyte backend
2. Some parts are required for Serialization, for example Platform Config is not required
3. Runtime of a task

Attributes:
    platform (PlatformConfig): Settings to connect to a Flyte backend.
    secrets (SecretsConfig): Configuration for secrets management.
    stats (StatsConfig): Configuration for statsd metrics.
    data_config (DataConfig): Data storage configuration.
    local_sandbox_path (str): Path for local sandbox runs.


```python
class Config(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
)
```
| Parameter | Type | Description |
|-|-|-|
| `platform` | `PlatformConfig` | |
| `secrets` | `SecretsConfig` | |
| `stats` | `StatsConfig` | |
| `data_config` | `DataConfig` | |
| `local_sandbox_path` | `str` | |

## Methods

| Method | Description |
|-|-|
| [`auto()`](#auto) | Automatically constructs the Config Object. |
| [`for_endpoint()`](#for_endpoint) | Creates an automatic config for the given endpoint and uses the config_file or environment variable for default. |
| [`for_sandbox()`](#for_sandbox) | Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox`. |
| [`with_params()`](#with_params) |  |


### auto()

```python
def auto(
    config_file: typing.Union[str, ConfigFile, None],
) -> Config
```
Automatically constructs the Config Object. The order of precedence is as follows
  1. first try to find any env vars that match the config vars specified in the FLYTE_CONFIG format.
  2. If not found in environment then values ar read from the config file
  3. If not found in the file, then the default values are used.



| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Union[str, ConfigFile, None]` | file path to read the config from, if not specified default locations are searched :return: Config |

### for_endpoint()

```python
def for_endpoint(
    endpoint: str,
    insecure: bool,
    data_config: typing.Optional[DataConfig],
    config_file: typing.Union[str, ConfigFile],
) -> Config
```
Creates an automatic config for the given endpoint and uses the config_file or environment variable for default.
Refer to `Config.auto()` to understand the default bootstrap behavior.

data_config can be used to configure how data is downloaded or uploaded to a specific Blob storage like S3 / GCS etc.
But, for permissions to a specific backend just use Cloud providers reqcommendation. If using fsspec, then
refer to fsspec documentation


| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | -&gt; Endpoint where Flyte admin is available |
| `insecure` | `bool` | -&gt; if the connection should be insecure, default is secure (SSL ON) |
| `data_config` | `typing.Optional[DataConfig]` | -&gt; Data config, if using specialized connection params like minio etc |
| `config_file` | `typing.Union[str, ConfigFile]` | -&gt; Optional config file in the flytekit config format. :return: Config |

### for_sandbox()

```python
def for_sandbox()
```
Constructs a new Config object specifically to connect to :std:ref:`deployment-deployment-sandbox`.
If you are using a hosted Sandbox like environment, then you may need to use port-forward or ingress urls
:return: Config


### with_params()

```python
def with_params(
    platform: PlatformConfig,
    secrets: SecretsConfig,
    stats: StatsConfig,
    data_config: DataConfig,
    local_sandbox_path: str,
) -> Config
```
| Parameter | Type | Description |
|-|-|-|
| `platform` | `PlatformConfig` | |
| `secrets` | `SecretsConfig` | |
| `stats` | `StatsConfig` | |
| `data_config` | `DataConfig` | |
| `local_sandbox_path` | `str` | |

