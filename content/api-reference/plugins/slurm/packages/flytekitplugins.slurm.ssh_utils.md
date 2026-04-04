---
title: flytekitplugins.slurm.ssh_utils
version: 1.16.16
variants: +flyte +byoc +selfmanaged +union
layout: py_api
---

# flytekitplugins.slurm.ssh_utils

Utilities of asyncssh connections.
## Directory

### Classes

| Class | Description |
|-|-|
| [`SSHConfig`](.././flytekitplugins.slurm.ssh_utils#flytekitpluginsslurmssh_utilssshconfig) | A customized version of SSHClientConnectionOptions, tailored to specific needs. |
| [`SlurmCluster`](.././flytekitplugins.slurm.ssh_utils#flytekitpluginsslurmssh_utilsslurmcluster) | A Slurm cluster instance is defined by a pair of (Slurm host, username). |

### Methods

| Method | Description |
|-|-|
| [`get_ssh_conn()`](#get_ssh_conn) | Get an existing SSH connection or create a new one if needed. |
| [`ssh_connect()`](#ssh_connect) | Make an SSH client connection. |


### Variables

| Property | Type | Description |
|-|-|-|
| `SLURM_PRIVATE_KEY` | `str` |  |
| `T` | `TypeVar` |  |

## Methods

#### get_ssh_conn()

```python
def get_ssh_conn(
    ssh_config: typing.Dict[str, typing.Union[str, typing.List[str], typing.Tuple[str, ...]]],
    slurm_cluster_to_ssh_conn: typing.Dict[flytekitplugins.slurm.ssh_utils.SlurmCluster, asyncssh.connection.SSHClientConnection],
) -> typing.Tuple[flytekitplugins.slurm.ssh_utils.SlurmCluster, asyncssh.connection.SSHClientConnection]
```
Get an existing SSH connection or create a new one if needed.



| Parameter | Type | Description |
|-|-|-|
| `ssh_config` | `typing.Dict[str, typing.Union[str, typing.List[str], typing.Tuple[str, ...]]]` | SSH configuration dictionary, including host and username. |
| `slurm_cluster_to_ssh_conn` | `typing.Dict[flytekitplugins.slurm.ssh_utils.SlurmCluster, asyncssh.connection.SSHClientConnection]` | A mapping of SlurmCluster to existing SSHClientConnection objects. |

**Returns**

Tuple[SlurmCluster, SSHClientConnection]:
    A tuple containing (SlurmCluster, SSHClientConnection). If no connection
    for the given SlurmCluster exists, a new one is created and cached.

#### ssh_connect()

```python
def ssh_connect(
    ssh_config: typing.Dict[str, typing.Any],
) -> asyncssh.connection.SSHClientConnection
```
Make an SSH client connection.



| Parameter | Type | Description |
|-|-|-|
| `ssh_config` | `typing.Dict[str, typing.Any]` | Options of SSH client connection defined in SSHConfig. |

**Returns**

SSHClientConnection: An SSH client connection object.


**Raises**

| Exception | Description |
|-|-|
| `ValueError` | If both FLYTE_SLURM_PRIVATE_KEY secret and ssh_config['private_key'] are missing. |

## flytekitplugins.slurm.ssh_utils.SSHConfig

A customized version of SSHClientConnectionOptions, tailored to specific needs.

This config is based on the official SSHClientConnectionOptions but includes
only a subset of options, with some fields adjusted to be optional or required.
For the official options, please refer to:
https://asyncssh.readthedocs.io/en/latest/api.html#asyncssh.SSHClientConnectionOptions



### Parameters

```python
class SSHConfig(
    host: str,
    username: typing.Optional[str],
    client_keys: typing.Union[str, typing.List[str], typing.Tuple[str, ...]],
)
```
| Parameter | Type | Description |
|-|-|-|
| `host` | `str` | The hostname or address to connect to. |
| `username` | `typing.Optional[str]` | The username to authenticate as on the server. |
| `client_keys` | `typing.Union[str, typing.List[str], typing.Tuple[str, ...]]` | File paths to private keys which will be used to authenticate the client via public key authentication. The default value is an empty tuple since client public key authentication is mandatory. |

### Methods

| Method | Description |
|-|-|
| [`from_dict()`](#from_dict) |  |
| [`to_dict()`](#to_dict) |  |


#### from_dict()

```python
def from_dict(
    ssh_config: typing.Dict[str, typing.Any],
) -> ~T
```
| Parameter | Type | Description |
|-|-|-|
| `ssh_config` | `typing.Dict[str, typing.Any]` | |

#### to_dict()

```python
def to_dict()
```
## flytekitplugins.slurm.ssh_utils.SlurmCluster

A Slurm cluster instance is defined by a pair of (Slurm host, username).



### Parameters

```python
class SlurmCluster(
    host: str,
    username: typing.Optional[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `host` | `str` | The hostname or address to connect to. |
| `username` | `typing.Optional[str]` | The username to authenticate as on the server. |

