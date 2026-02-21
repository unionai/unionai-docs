---
title: flytekit.configuration.plugin
version: 1.16.14
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekit.configuration.plugin

Defines a plugin API allowing other libraries to modify the behavior of flytekit.

Libraries can register by defining an object that follows the same API as FlytekitPlugin
and providing an entrypoint with the group name "flytekit.plugin". In `setuptools`,
you can specific them with:

```python
setup(entry_points={
    "flytekit.configuration.plugin": ["my_plugin=my_module:MyCustomPlugin"]
})
```

or in pyproject.toml:

```toml
[project.entry-points."flytekit.configuration.plugin"]
my_plugin = "my_module:MyCustomPlugin"
```

## Directory

### Classes

| Class | Description |
|-|-|
| [`FlytekitPlugin`](.././flytekit.configuration.plugin#flytekitconfigurationpluginflytekitplugin) |  |

### Protocols

| Protocol | Description |
|-|-|
| [`FlytekitPluginProtocol`](.././flytekit.configuration.plugin#flytekitconfigurationpluginflytekitpluginprotocol) |  |

### Methods

| Method | Description |
|-|-|
| [`get_plugin()`](#get_plugin) | Get current plugin. |


## Methods

#### get_plugin()

```python
def get_plugin()
```
Get current plugin


## flytekit.configuration.plugin.FlytekitPlugin

### Methods

| Method | Description |
|-|-|
| [`configure_pyflyte_cli()`](#configure_pyflyte_cli) | Configure pyflyte's CLI. |
| [`get_auth_success_html()`](#get_auth_success_html) | Get default success html. |
| [`get_default_cache_policies()`](#get_default_cache_policies) | Get default cache policies for tasks. |
| [`get_default_image()`](#get_default_image) | Get default image. |
| [`get_remote()`](#get_remote) | Get FlyteRemote object for CLI session. |
| [`secret_requires_group()`](#secret_requires_group) | Return True if secrets require group entry during registration time. |


#### configure_pyflyte_cli()

```python
def configure_pyflyte_cli(
    main: click.core.Group,
) -> click.core.Group
```
Configure pyflyte's CLI.


| Parameter | Type | Description |
|-|-|-|
| `main` | `click.core.Group` | |

#### get_auth_success_html()

```python
def get_auth_success_html(
    endpoint: str,
) -> typing.Optional[str]
```
Get default success html. Return None to use flytekit's default success html.


| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |

#### get_default_cache_policies()

```python
def get_default_cache_policies()
```
Get default cache policies for tasks.


#### get_default_image()

```python
def get_default_image()
```
Get default image. Return None to use the images from flytekit.configuration.DefaultImages


#### get_remote()

```python
def get_remote(
    config: typing.Optional[str],
    project: str,
    domain: str,
    data_upload_location: typing.Optional[str],
) -> flytekit.remote.remote.FlyteRemote
```
Get FlyteRemote object for CLI session.


| Parameter | Type | Description |
|-|-|-|
| `config` | `typing.Optional[str]` | |
| `project` | `str` | |
| `domain` | `str` | |
| `data_upload_location` | `typing.Optional[str]` | |

#### secret_requires_group()

```python
def secret_requires_group()
```
Return True if secrets require group entry during registration time.


## flytekit.configuration.plugin.FlytekitPluginProtocol

```python
protocol FlytekitPluginProtocol()
```
### Methods

| Method | Description |
|-|-|
| [`configure_pyflyte_cli()`](#configure_pyflyte_cli) | Configure pyflyte's CLI. |
| [`get_auth_success_html()`](#get_auth_success_html) | Get default success html for auth. |
| [`get_default_cache_policies()`](#get_default_cache_policies) | Get default cache policies for tasks. |
| [`get_default_image()`](#get_default_image) | Get default image. |
| [`get_remote()`](#get_remote) | Get FlyteRemote object for CLI session. |
| [`secret_requires_group()`](#secret_requires_group) | Return True if secrets require group entry. |


#### configure_pyflyte_cli()

```python
def configure_pyflyte_cli(
    main: click.core.Group,
) -> click.core.Group
```
Configure pyflyte's CLI.


| Parameter | Type | Description |
|-|-|-|
| `main` | `click.core.Group` | |

#### get_auth_success_html()

```python
def get_auth_success_html(
    endpoint: str,
) -> typing.Optional[str]
```
Get default success html for auth. Return None to use flytekit's default success html.


| Parameter | Type | Description |
|-|-|-|
| `endpoint` | `str` | |

#### get_default_cache_policies()

```python
def get_default_cache_policies()
```
Get default cache policies for tasks.


#### get_default_image()

```python
def get_default_image()
```
Get default image. Return None to use the images from flytekit.configuration.DefaultImages


#### get_remote()

```python
def get_remote(
    config: typing.Optional[str],
    project: str,
    domain: str,
    data_upload_location: typing.Optional[str],
) -> flytekit.remote.remote.FlyteRemote
```
Get FlyteRemote object for CLI session.


| Parameter | Type | Description |
|-|-|-|
| `config` | `typing.Optional[str]` | |
| `project` | `str` | |
| `domain` | `str` | |
| `data_upload_location` | `typing.Optional[str]` | |

#### secret_requires_group()

```python
def secret_requires_group()
```
Return True if secrets require group entry.


