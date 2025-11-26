---
title: Trigger
version: 2.0.0b33
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Trigger

**Package:** `flyte`

This class defines specification of a Trigger, that can be associated with any Flyte V2 task.
The trigger then is deployed to the Flyte Platform.

Triggers can be used to run tasks on a schedule, in response to events, or based on other conditions.
The `Trigger` class encapsulates the metadata and configuration needed to define a trigger.

You can associate the same Trigger object with multiple tasks.

Example usage:
```python
from flyte.trigger import Trigger
my_trigger = Trigger(
    name="my_trigger",
    description="A trigger that runs every hour",
)
```



```python
class Trigger(
    name: str,
    automation: Union[Cron, FixedRate],
    description: str,
    auto_activate: bool,
    inputs: Dict[str, Any] | None,
    env_vars: Dict[str, str] | None,
    interruptible: bool | None,
    overwrite_cache: bool,
    queue: str | None,
    labels: Mapping[str, str] | None,
    annotations: Mapping[str, str] | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | (str) The name of the trigger. |
| `automation` | `Union[Cron, FixedRate]` | (AutomationType) The automation type, currently only supports Cron. |
| `description` | `str` | (str) A description of the trigger, default is an empty string. |
| `auto_activate` | `bool` | (bool) Whether the trigger should be automatically activated, default is True. |
| `inputs` | `Dict[str, Any] \| None` | (Dict[str, Any]) Optional inputs for the trigger, default is None. If provided, will replace the values for inputs to these defaults. |
| `env_vars` | `Dict[str, str] \| None` | (Dict[str, str]) Optional environment variables for the trigger, default is None. If provided, will replace the environment variables set in the config of the task. |
| `interruptible` | `bool \| None` | (bool) Whether the trigger run is interruptible, default is None (maintains the configured behavior). If provided, it overrides whatever is set in the config of the task. |
| `overwrite_cache` | `bool` | (bool) Whether to overwrite the cache, default is False. |
| `queue` | `str \| None` | (str) Optional queue to run the trigger in, default is None. |
| `labels` | `Mapping[str, str] \| None` | (Mapping[str, str]) Optional labels to attach to the trigger, default is None. |
| `annotations` | `Mapping[str, str] \| None` | (Mapping[str, str]) Optional annotations to attach to the trigger, default is None. |

## Methods

| Method | Description |
|-|-|
| [`daily()`](#daily) | Creates a Cron trigger that runs daily at midnight. |
| [`hourly()`](#hourly) | Creates a Cron trigger that runs every hour. |
| [`minutely()`](#minutely) | Creates a Cron trigger that runs every minute. |
| [`monthly()`](#monthly) | Creates a Cron trigger that runs monthly on the 1st at midnight. |
| [`weekly()`](#weekly) | Creates a Cron trigger that runs weekly on Sundays at midnight. |


### daily()

```python
def daily(
    trigger_time_input_key: str | None,
    name: str,
    description: str,
    auto_activate: bool,
    inputs: Dict[str, Any] | None,
    env_vars: Dict[str, str] | None,
    interruptible: bool | None,
    overwrite_cache: bool,
    queue: str | None,
    labels: Mapping[str, str] | None,
    annotations: Mapping[str, str] | None,
) -> Trigger
```
Creates a Cron trigger that runs daily at midnight.



| Parameter | Type | Description |
|-|-|-|
| `trigger_time_input_key` | `str \| None` | |
| `name` | `str` | |
| `description` | `str` | |
| `auto_activate` | `bool` | |
| `inputs` | `Dict[str, Any] \| None` | |
| `env_vars` | `Dict[str, str] \| None` | |
| `interruptible` | `bool \| None` | |
| `overwrite_cache` | `bool` | |
| `queue` | `str \| None` | |
| `labels` | `Mapping[str, str] \| None` | |
| `annotations` | `Mapping[str, str] \| None` | |

### hourly()

```python
def hourly(
    trigger_time_input_key: str | None,
    name: str,
    description: str,
    auto_activate: bool,
    inputs: Dict[str, Any] | None,
    env_vars: Dict[str, str] | None,
    interruptible: bool | None,
    overwrite_cache: bool,
    queue: str | None,
    labels: Mapping[str, str] | None,
    annotations: Mapping[str, str] | None,
) -> Trigger
```
Creates a Cron trigger that runs every hour.



| Parameter | Type | Description |
|-|-|-|
| `trigger_time_input_key` | `str \| None` | |
| `name` | `str` | |
| `description` | `str` | |
| `auto_activate` | `bool` | |
| `inputs` | `Dict[str, Any] \| None` | |
| `env_vars` | `Dict[str, str] \| None` | |
| `interruptible` | `bool \| None` | |
| `overwrite_cache` | `bool` | |
| `queue` | `str \| None` | |
| `labels` | `Mapping[str, str] \| None` | |
| `annotations` | `Mapping[str, str] \| None` | |

### minutely()

```python
def minutely(
    trigger_time_input_key: str | None,
    name: str,
    description: str,
    auto_activate: bool,
    inputs: Dict[str, Any] | None,
    env_vars: Dict[str, str] | None,
    interruptible: bool | None,
    overwrite_cache: bool,
    queue: str | None,
    labels: Mapping[str, str] | None,
    annotations: Mapping[str, str] | None,
) -> Trigger
```
Creates a Cron trigger that runs every minute.



| Parameter | Type | Description |
|-|-|-|
| `trigger_time_input_key` | `str \| None` | |
| `name` | `str` | |
| `description` | `str` | |
| `auto_activate` | `bool` | |
| `inputs` | `Dict[str, Any] \| None` | |
| `env_vars` | `Dict[str, str] \| None` | |
| `interruptible` | `bool \| None` | |
| `overwrite_cache` | `bool` | |
| `queue` | `str \| None` | |
| `labels` | `Mapping[str, str] \| None` | |
| `annotations` | `Mapping[str, str] \| None` | |

### monthly()

```python
def monthly(
    trigger_time_input_key: str | None,
    name: str,
    description: str,
    auto_activate: bool,
    inputs: Dict[str, Any] | None,
    env_vars: Dict[str, str] | None,
    interruptible: bool | None,
    overwrite_cache: bool,
    queue: str | None,
    labels: Mapping[str, str] | None,
    annotations: Mapping[str, str] | None,
) -> Trigger
```
Creates a Cron trigger that runs monthly on the 1st at midnight.



| Parameter | Type | Description |
|-|-|-|
| `trigger_time_input_key` | `str \| None` | |
| `name` | `str` | |
| `description` | `str` | |
| `auto_activate` | `bool` | |
| `inputs` | `Dict[str, Any] \| None` | |
| `env_vars` | `Dict[str, str] \| None` | |
| `interruptible` | `bool \| None` | |
| `overwrite_cache` | `bool` | |
| `queue` | `str \| None` | |
| `labels` | `Mapping[str, str] \| None` | |
| `annotations` | `Mapping[str, str] \| None` | |

### weekly()

```python
def weekly(
    trigger_time_input_key: str | None,
    name: str,
    description: str,
    auto_activate: bool,
    inputs: Dict[str, Any] | None,
    env_vars: Dict[str, str] | None,
    interruptible: bool | None,
    overwrite_cache: bool,
    queue: str | None,
    labels: Mapping[str, str] | None,
    annotations: Mapping[str, str] | None,
) -> Trigger
```
Creates a Cron trigger that runs weekly on Sundays at midnight.



| Parameter | Type | Description |
|-|-|-|
| `trigger_time_input_key` | `str \| None` | |
| `name` | `str` | |
| `description` | `str` | |
| `auto_activate` | `bool` | |
| `inputs` | `Dict[str, Any] \| None` | |
| `env_vars` | `Dict[str, str] \| None` | |
| `interruptible` | `bool \| None` | |
| `overwrite_cache` | `bool` | |
| `queue` | `str \| None` | |
| `labels` | `Mapping[str, str] \| None` | |
| `annotations` | `Mapping[str, str] \| None` | |

