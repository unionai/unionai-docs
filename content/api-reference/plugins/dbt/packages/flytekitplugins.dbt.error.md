---
title: flytekitplugins.dbt.error
version: 0.0.0+develop
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# flytekitplugins.dbt.error

## Directory

### Errors

| Exception | Description |
|-|-|
| [`DBTHandledError`](.././flytekitplugins.dbt.error#flytekitpluginsdbterrordbthandlederror) | DBTHandledError wraps error logs and message from command execution that returns ``exit code 1``. |
| [`DBTUnhandledError`](.././flytekitplugins.dbt.error#flytekitpluginsdbterrordbtunhandlederror) | DBTUnhandledError wraps error logs and message from command execution that returns ``exit code 2``. |

## flytekitplugins.dbt.error.DBTHandledError

DBTHandledError wraps error logs and message from command execution that returns ``exit code 1``.

Parameters
----------
message : str
    Error message.
logs : list of str
    Logs produced by the command execution.

Attributes
----------
message : str
    Error message.
logs : list of str
    Logs produced by the command execution.


```python
class DBTHandledError(
    message: str,
    logs: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |
| `logs` | `typing.List[str]` |

## flytekitplugins.dbt.error.DBTUnhandledError

DBTUnhandledError wraps error logs and message from command execution that returns ``exit code 2``.

Parameters
----------
message : str
    Error message.
logs : list of str
    Logs produced by the command execution.

Attributes
----------
message : str
    Error message.
logs : list of str
    Logs produced by the command execution.


```python
class DBTUnhandledError(
    message: str,
    logs: typing.List[str],
)
```
| Parameter | Type |
|-|-|
| `message` | `str` |
| `logs` | `typing.List[str]` |

