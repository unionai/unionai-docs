---
title: flytekit.loggers
version: 0.1.dev2175+gcd6bd01.d20250325
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.loggers

## Directory

### Methods

| Method | Description |
|-|-|
| [`_get_dev_env_logging_level()`](#_get_dev_env_logging_level) | Returns the logging level set in the environment variable, or logging. |
| [`_get_env_logging_level()`](#_get_env_logging_level) | Returns the logging level set in the environment variable, or logging. |
| [`get_level_from_cli_verbosity()`](#get_level_from_cli_verbosity) | Converts a verbosity level from the CLI to a logging level. |
| [`initialize_global_loggers()`](#initialize_global_loggers) | Initializes the global loggers to the default configuration. |
| [`is_display_progress_enabled()`](#is_display_progress_enabled) |  |
| [`is_rich_logging_enabled()`](#is_rich_logging_enabled) |  |
| [`set_developer_properties()`](#set_developer_properties) | developer logger is only used for debugging. |
| [`set_flytekit_log_properties()`](#set_flytekit_log_properties) | flytekit logger, refers to the framework logger. |
| [`set_user_logger_properties()`](#set_user_logger_properties) | user_space logger, refers to the user's logger. |
| [`upgrade_to_rich_logging()`](#upgrade_to_rich_logging) |  |


### Variables

| Property | Type | Description |
|-|-|-|
| `LOGGING_DEV_ENV_VAR` | `str` |  |
| `LOGGING_ENV_VAR` | `str` |  |
| `LOGGING_FMT_ENV_VAR` | `str` |  |
| `LOGGING_RICH_FMT_ENV_VAR` | `str` |  |
| `developer_logger` | `Logger` |  |
| `logger` | `Logger` |  |
| `user_space_logger` | `Logger` |  |

## Methods

#### _get_dev_env_logging_level()

```python
def _get_dev_env_logging_level(
    default_level: int,
) -> int
```
Returns the logging level set in the environment variable, or logging.INFO if the environment variable is not
set.


| Parameter | Type |
|-|-|
| `default_level` | `int` |

#### _get_env_logging_level()

```python
def _get_env_logging_level(
    default_level: int,
) -> int
```
Returns the logging level set in the environment variable, or logging.WARNING if the environment variable is not
set.


| Parameter | Type |
|-|-|
| `default_level` | `int` |

#### get_level_from_cli_verbosity()

```python
def get_level_from_cli_verbosity(
    verbosity: int,
) -> int
```
Converts a verbosity level from the CLI to a logging level.



| Parameter | Type |
|-|-|
| `verbosity` | `int` |

#### initialize_global_loggers()

```python
def initialize_global_loggers()
```
Initializes the global loggers to the default configuration.


#### is_display_progress_enabled()

```python
def is_display_progress_enabled()
```
#### is_rich_logging_enabled()

```python
def is_rich_logging_enabled()
```
#### set_developer_properties()

```python
def set_developer_properties(
    handler: typing.Optional[logging.Handler],
    filter: typing.Optional[logging.Filter],
    level: typing.Optional[int],
)
```
developer logger is only used for debugging. It is possible to selectively tune the logging for the developer.



| Parameter | Type |
|-|-|
| `handler` | `typing.Optional[logging.Handler]` |
| `filter` | `typing.Optional[logging.Filter]` |
| `level` | `typing.Optional[int]` |

#### set_flytekit_log_properties()

```python
def set_flytekit_log_properties(
    handler: typing.Optional[logging.Handler],
    filter: typing.Optional[logging.Filter],
    level: typing.Optional[int],
)
```
flytekit logger, refers to the framework logger. It is possible to selectively tune the logging for flytekit.

Sets the flytekit logger to the specified handler, filter, and level. If any of the parameters are None, then
the corresponding property on the flytekit logger will not be set.



| Parameter | Type |
|-|-|
| `handler` | `typing.Optional[logging.Handler]` |
| `filter` | `typing.Optional[logging.Filter]` |
| `level` | `typing.Optional[int]` |

#### set_user_logger_properties()

```python
def set_user_logger_properties(
    handler: typing.Optional[logging.Handler],
    filter: typing.Optional[logging.Filter],
    level: typing.Optional[int],
)
```
user_space logger, refers to the user's logger. It is possible to selectively tune the logging for the user.



| Parameter | Type |
|-|-|
| `handler` | `typing.Optional[logging.Handler]` |
| `filter` | `typing.Optional[logging.Filter]` |
| `level` | `typing.Optional[int]` |

#### upgrade_to_rich_logging()

```python
def upgrade_to_rich_logging(
    log_level: typing.Optional[int],
)
```
| Parameter | Type |
|-|-|
| `log_level` | `typing.Optional[int]` |

