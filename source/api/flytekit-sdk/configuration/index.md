# Configuration

## What configuration is used for

Configuration usage can roughly be bucketed into the following areas:

- **Compile-time settings**: These are settings like the default image and named images, where to look for Flyte code, etc.
- **Platform settings**: Where to find the Flyte backend (Admin DNS, whether to use SSL).
- **Registration runtime settings**: These are things like the K8s service account to use, a specific S3/GCS bucket to write off-loaded data (dataframes and files) to, notifications, labels & annotations, etc.
- **Data access settings**: Is there a custom S3 endpoint in use? Backoff/retry behavior for accessing S3/GCS, key and password, etc.
- **Other settings**: Statsd configuration, which is a run-time applicable setting but is not necessarily relevant to the Flyte platform.

## Flytekit configuration sources

### Command line arguments

Command line arguments are the recommended way to set configuration values most of the time.
For example, see the [`union package`](https://docs.union.ai/serverless/api/union-cli#union-package) command.

### Configuration files

#### YAML format

A configuration file that contains settings for both [`uctl`](TK) and `flytekit`. This is the recommended configuration file format. Invoke the [`uctl config init`](TK) command to create a boilerplate
`~/.union/config.yaml` file, and  `uctl --help` to learn about all of the configuration YAML options.

::::{dropdown} See example `config.yaml` file
:animate: fade-in-slide-down

```{rli} https://raw.githubusercontent.com/flyteorg/flytekit/master/tests/flytekit/unit/configuration/configs/sample.yaml
:language: yaml
:caption: config.yaml
```
::::

#### INI format

```{warning}
The INI format configuration is considered a legacy configuration format. We recommend using the [YAML format](#yaml-format-configuration-file) instead if you're using a configuration file.
```

A configuration file for `flytekit`. By default, `flytekit` will look for a file in two places:

1. First, `flytekit` looks in the Python interpreter's working directory for a file named `flytekit.config`.
2. Next, `flytekit` looks in the home director as detected by Python for a file named `~/.flyte/config`.

::::{dropdown} See example `flytekit.config` file
:animate: fade-in-slide-down

```{rli} https://raw.githubusercontent.com/flyteorg/flytekit/master/tests/flytekit/unit/configuration/configs/images.config
:language: INI
:caption: flytekit.config
```
::::

{@@ if byoc @@}
### Python objects

#### Config object

:::{note}
You can use a [`Config`](TK) object directly, for example, when initializing a [`UnionRemote`](TK) object. See [TK](TK) for examples on how to specify a `Config` object.
:::

```{eval-rst}

.. currentmodule:: flytekit.configuration

.. autosummary::
   :nosignatures:

   ~Config
```

#### Compile time and serialization settings

```{eval-rst}

.. currentmodule:: flytekit.configuration

.. autosummary::
   :nosignatures:

   ~Image
   ~ImageConfig
   ~SerializationSettings
   ~FastSerializationSettings
```

:::{note}
These are compile-time and serialization settings that are usually passed in as flags to commands like [`union package`](TK) or [`union register](TK).

The image configurations are typically either passed in via an [`--image](https://docs.union.ai/serverless/api/union-cli#cmdoption-union-package-i) flag, or can be specified in a [`YAML` or `ini` configuration file](#configuration-file).
:::

#### Execution time settings

You usually won't need to worry about these configurations, as they are typically set by FlytePropeller or
FlyteAdmin. The configurations below are useful for authenticating to a Union backend, configuring data access
credentials, secrets, and `statsd` metrics.

```{eval-rst}

.. currentmodule:: flytekit.configuration

.. autosummary::
   :nosignatures:

   ~PlatformConfig
   ~StatsConfig
   ~SecretsConfig
   ~S3Config
   ~GCSConfig
   ~DataConfig
```

{@@ endif @@}

### Environment variables

You can specify environment variables at compile time, but when your task is run, FlytePropeller will also set configuration to ensure correct interaction with the platform. The environment variables must be specified with the format `FLYTE_{SECTION}_{OPTION}`, all in upper case. For example, to specify the [`PlatformConfig.endpoint`](TK) setting, the environment variable would be `FLYTE_PLATFORM_URL`.

:::{note}
Environment variables won't work for specifying an image, which needs to be specified with the
[`union package --image ...`](TK) option or in a configuration file.
:::
