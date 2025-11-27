---
title: RunLevelParams
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# RunLevelParams

**Package:** `flytekit.clis.sdk_in_container.run`

This class is used to store the parameters that are used to run a workflow / task / launchplan.


```python
class RunLevelParams(
    config_file: typing.Optional[str],
    verbose: bool,
    pkgs: typing.List[str],
    project: str,
    domain: str,
    destination_dir: str,
    copy_all: bool,
    copy: typing.Optional[flytekit.constants.CopyFileDetection],
    image_config: flytekit.configuration.ImageConfig,
    service_account: str,
    wait_execution: bool,
    poll_interval: int,
    dump_snippet: bool,
    overwrite_cache: bool,
    interruptible: typing.Optional[bool],
    envvars: typing.Dict[str, str],
    resource_requests: typing.Optional[flytekit.core.resources.Resources],
    resource_limits: typing.Optional[flytekit.core.resources.Resources],
    tags: typing.List[str],
    name: str,
    labels: typing.Dict[str, str],
    annotations: typing.Dict[str, str],
    raw_output_data_prefix: str,
    max_parallelism: int,
    disable_notifications: bool,
    remote: bool,
    limit: int,
    cluster_pool: str,
    execution_cluster_label: str,
    computed_params: flytekit.clis.sdk_in_container.run.RunLevelComputedParams,
    _remote: typing.Optional[flytekit.remote.remote.FlyteRemote],
)
```
| Parameter | Type | Description |
|-|-|-|
| `config_file` | `typing.Optional[str]` | |
| `verbose` | `bool` | |
| `pkgs` | `typing.List[str]` | |
| `project` | `str` | |
| `domain` | `str` | |
| `destination_dir` | `str` | |
| `copy_all` | `bool` | |
| `copy` | `typing.Optional[flytekit.constants.CopyFileDetection]` | |
| `image_config` | `flytekit.configuration.ImageConfig` | |
| `service_account` | `str` | |
| `wait_execution` | `bool` | |
| `poll_interval` | `int` | |
| `dump_snippet` | `bool` | |
| `overwrite_cache` | `bool` | |
| `interruptible` | `typing.Optional[bool]` | |
| `envvars` | `typing.Dict[str, str]` | |
| `resource_requests` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `resource_limits` | `typing.Optional[flytekit.core.resources.Resources]` | |
| `tags` | `typing.List[str]` | |
| `name` | `str` | |
| `labels` | `typing.Dict[str, str]` | |
| `annotations` | `typing.Dict[str, str]` | |
| `raw_output_data_prefix` | `str` | |
| `max_parallelism` | `int` | |
| `disable_notifications` | `bool` | |
| `remote` | `bool` | |
| `limit` | `int` | |
| `cluster_pool` | `str` | |
| `execution_cluster_label` | `str` | |
| `computed_params` | `flytekit.clis.sdk_in_container.run.RunLevelComputedParams` | |
| `_remote` | `typing.Optional[flytekit.remote.remote.FlyteRemote]` | |

## Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`options()`](#options) | Return the set of base parameters added to every pyflyte run workflow subcommand. |
| [`remote_instance()`](#remote_instance) |  |


### from_dict()

```python
def from_dict(
    d: typing.Dict[str, typing.Any],
) -> RunLevelParams
```
| Parameter | Type | Description |
|-|-|-|
| `d` | `typing.Dict[str, typing.Any]` | |

### options()

```python
def options()
```
Return the set of base parameters added to every pyflyte run workflow subcommand.


### remote_instance()

```python
def remote_instance()
```
## Properties

| Property | Type | Description |
|-|-|-|
| `is_remote` |  |  |

