# Configuration

## Flytekit configuration sources

There are multiple ways to configure flytekit settings:

### Command line Arguments

Command line arguments are the recommended way to set configuration values most of the time.
For example, see the `[union package](https://docs.union.ai/serverless/api/union-cli#union-package)` command.

{@@ if byoc @@}
### Python Config object

You can use a `[Config](TK)` object directly, for example, when
initializing a `[UnionRemote](TK)` object. See [TK](TK) for examples on how to specify a `Config` object.
{@@ endif @@}

### Environment variables

You can specify environment variables at compile time, but when your task is run, FlytePropeller will also set configuration to ensure correct interaction with the platform. The environment variables must be specified with the format `FLYTE_{SECTION}_{OPTION}`, all in upper case. For example, to specify the `[PlatformConfig.endpoint](TK)` setting, the environment variable would be `FLYTE_PLATFORM_URL`.

```{note}
Environment variables won't work for specifying an image, which needs to be specified with the
`[pyflyte package --image ...](TK)` option or in a configuration file.
```

### YAML format configuration file

A configuration file that contains settings for both `[uctl](TK)` and `flytekit`. This is the recommended configuration file format. Invoke the `[uctl config init](TK)` command to create a boilerplate
`~/.union/config.yaml` file, and  `uctl --help` to learn about all of the configuration YAML options.

::::{dropdown} {fas} See example `config.yaml` file
:animate: fade-in-slide-down

:::{button-link} https://signup.union.ai/
:color: secondary

Create an account
:::

Once you have a Union account, install `'union[byoc]'`

::::

```{eval-rst}

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

.. currentmodule:: flytekit.configuration

The following objects are encapsulated in a parent object called ``Config``.

.. autosummary::
   :template: custom.rst
   :nosignatures:
   :toctree: members/

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
   :nosignatures:
   :toctree: members/

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
   :toctree: members/
   
   :nosignatures:

   ~PlatformConfig
   ~StatsConfig
   ~SecretsConfig
   ~S3Config
   ~GCSConfig
   ~DataConfig
```