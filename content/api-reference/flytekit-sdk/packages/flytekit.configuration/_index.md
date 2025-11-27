---
title: flytekit.configuration
version: 1.16.10
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

```YAML
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
```

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
| [`AuthType`](../flytekit.configuration/authtype) | Create a collection of name/value pairs. |
| [`AzureBlobStorageConfig`](../flytekit.configuration/azureblobstorageconfig) | Any Azure Blob Storage specific configuration. |
| [`Config`](../flytekit.configuration/config) | This the parent configuration object and holds all the underlying configuration object types. |
| [`DataConfig`](../flytekit.configuration/dataconfig) | Any data storage specific configuration. |
| [`EntrypointSettings`](../flytekit.configuration/entrypointsettings) | This object carries information about the path of the entrypoint command that will be invoked at runtime. |
| [`FastSerializationSettings`](../flytekit.configuration/fastserializationsettings) | This object hold information about settings necessary to serialize an object so that it can be fast-registered. |
| [`GCSConfig`](../flytekit.configuration/gcsconfig) | Any GCS specific configuration. |
| [`GenericPersistenceConfig`](../flytekit.configuration/genericpersistenceconfig) | Data storage configuration that applies across any provider. |
| [`Image`](../flytekit.configuration/image) | Image is a structured wrapper for task container images used in object serialization. |
| [`ImageConfig`](../flytekit.configuration/imageconfig) | We recommend you to use ImageConfig. |
| [`LocalConfig`](../flytekit.configuration/localconfig) | Any configuration specific to local runs. |
| [`PlatformConfig`](../flytekit.configuration/platformconfig) | This object contains the settings to talk to a Flyte backend (the DNS location of your Admin server basically). |
| [`S3Config`](../flytekit.configuration/s3config) | S3 specific configuration. |
| [`SecretsConfig`](../flytekit.configuration/secretsconfig) | Configuration for secrets. |
| [`SerializationSettings`](../flytekit.configuration/serializationsettings) | These settings are provided while serializing a workflow and task, before registration. |
| [`StatsConfig`](../flytekit.configuration/statsconfig) | Configuration for sending statsd. |
| [`TaskConfig`](../flytekit.configuration/taskconfig) | Any Project/Domain/Org configuration. |

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

