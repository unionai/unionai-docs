---
title: SlurmJobMetadata
icon: braces
version: 2.11.2
variants: +flyte +union
layout: py_api
---

# SlurmJobMetadata

**Package:** `flyteplugins.slurm`

## Parameters

```python
class SlurmJobMetadata(
    job_id: str,
    job_name: str,
    host: str,
    username: str,
    port: int,
    stdout_path: str,
    stderr_path: str,
    known_hosts: typing.Optional[str] = None,
    skip_host_key_verification: bool = False,
    declared_outputs: typing.Dict[str, typing.Dict[str, str]] = <factory>,
)
```
| Parameter | Type | Description |
|-|-|-|
| `job_id` | `str` | |
| `job_name` | `str` | |
| `host` | `str` | |
| `username` | `str` | |
| `port` | `int` | |
| `stdout_path` | `str` | |
| `stderr_path` | `str` | |
| `known_hosts` | `typing.Optional[str]` | |
| `skip_host_key_verification` | `bool` | |
| `declared_outputs` | `typing.Dict[str, typing.Dict[str, str]]` | |

## Methods

| Method | Description |
|-|-|
| [`decode()`](#decode) | Decode the resource meta from bytes. |
| [`encode()`](#encode) | Encode the resource meta to bytes. |


### decode()

```python
def decode(
    data: bytes,
) -> typing.Self
```
Decode the resource meta from bytes.


| Parameter | Type | Description |
|-|-|-|
| `data` | `bytes` | |

### encode()

```python
def encode()
```
Encode the resource meta to bytes.


