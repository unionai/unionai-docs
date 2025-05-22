---
title: union.configuration
version: 0.1.171.dev4+g052020f1.d20250404
variants: +byoc +selfmanaged +serverless -flyte
layout: py_api
---

# union.configuration

## Directory

### Classes

| Class | Description |
|-|-|
| [`UnionAIPlugin`](.././union.configuration#unionconfigurationunionaiplugin) |  |

## union.configuration.UnionAIPlugin

### Methods

| Method | Description |
|-|-|
| [`configure_pyflyte_cli()`](#configure_pyflyte_cli) | Configure pyflyte's CLI. |
| [`get_auth_success_html()`](#get_auth_success_html) | Get default success html. |
| [`get_default_cache_policies()`](#get_default_cache_policies) | Get default cache policies for tasks. |
| [`get_default_image()`](#get_default_image) | Return default image. |
| [`get_remote()`](#get_remote) |  |
| [`secret_requires_group()`](#secret_requires_group) | Return True if secrets require group entry. |


#### configure_pyflyte_cli()

```python
def configure_pyflyte_cli(
    main: click.core.Group,
) -> click.core.Group
```
Configure pyflyte's CLI.


| Parameter | Type |
|-|-|
| `main` | `click.core.Group` |

#### get_auth_success_html()

```python
def get_auth_success_html(
    endpoint: str,
) -> typing.Optional[str]
```
Get default success html. Return None to use flytekit's default success html.


| Parameter | Type |
|-|-|
| `endpoint` | `str` |

#### get_default_cache_policies()

```python
def get_default_cache_policies()
```
Get default cache policies for tasks.


#### get_default_image()

```python
def get_default_image()
```
Return default image.


#### get_remote()

```python
def get_remote(
    config: typing.Optional[str],
    project: str,
    domain: str,
    data_upload_location: typing.Optional[str],
) -> UnionRemote
```
| Parameter | Type |
|-|-|
| `config` | `typing.Optional[str]` |
| `project` | `str` |
| `domain` | `str` |
| `data_upload_location` | `typing.Optional[str]` |

#### secret_requires_group()

```python
def secret_requires_group()
```
Return True if secrets require group entry.


