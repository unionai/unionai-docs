---
title: Trigger
version: 2.0.11
variants: +flyte +byoc +selfmanaged
layout: py_api
---

# Trigger

**Package:** `flyte`

Specification for a scheduled trigger that can be associated with any Flyte task.

Triggers run tasks on a schedule (cron or fixed-rate). They are set only in the
`@env.task` decorator via the `triggers` parameter. The same `Trigger` object
can be associated with multiple tasks.

Predefined convenience constructors are available: `Trigger.hourly()`,
`Trigger.daily()`, `Trigger.weekly()`, `Trigger.monthly()`, and
`Trigger.minutely()`.

Example:

```python
my_trigger = flyte.Trigger(
    name="my_trigger",
    description="A trigger that runs every hour",
    inputs={"start_time": flyte.TriggerTime, "x": 1},
    automation=flyte.FixedRate(60),
)

@env.task(triggers=[my_trigger])
async def my_task(start_time: datetime, x: int) -> str:
    ...
```



## Parameters

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
    notifications: NamedRule | Notification | Tuple[Notification, ...] | None,
)
```
| Parameter | Type | Description |
|-|-|-|
| `name` | `str` | Unique name for the trigger (required). |
| `automation` | `Union[Cron, FixedRate]` | Schedule type — `Cron(...)` or `FixedRate(...)` (required). |
| `description` | `str` | Human-readable description (max 255 characters). Default `""`. |
| `auto_activate` | `bool` | Whether to activate the trigger automatically on deployment. Default `True`. |
| `inputs` | `Dict[str, Any] \| None` | Default input values for triggered runs. Use `flyte.TriggerTime` to bind the trigger's scheduled time to an input parameter. |
| `env_vars` | `Dict[str, str] \| None` | Environment variables for triggered runs (overrides the task's configured values). |
| `interruptible` | `bool \| None` | Whether triggered runs use spot/preemptible instances. `None` (default) preserves the task's configured behavior. Overrides the task's configured value. |
| `overwrite_cache` | `bool` | Force cache refresh on triggered runs. Default `False`. |
| `queue` | `str \| None` | Queue name for triggered runs (overrides the task's configured value). |
| `labels` | `Mapping[str, str] \| None` | Kubernetes labels to attach to triggered runs. |
| `annotations` | `Mapping[str, str] \| None` | Kubernetes annotations to attach to triggered runs. |
| `notifications` | `NamedRule \| Notification \| Tuple[Notification, ...] \| None` | |

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
| `trigger_time_input_key` | `str \| None` | The input key for the trigger time. If None, no trigger time input is added. |
| `name` | `str` | The name of the trigger, default is "daily". |
| `description` | `str` | A description of the trigger. |
| `auto_activate` | `bool` | Whether the trigger should be automatically activated. |
| `inputs` | `Dict[str, Any] \| None` | Optional inputs for the trigger. |
| `env_vars` | `Dict[str, str] \| None` | Optional environment variables. |
| `interruptible` | `bool \| None` | Whether the triggered run is interruptible. |
| `overwrite_cache` | `bool` | Whether to overwrite the cache. |
| `queue` | `str \| None` | Optional queue to run the trigger in. |
| `labels` | `Mapping[str, str] \| None` | Optional labels to attach to the trigger. |
| `annotations` | `Mapping[str, str] \| None` | Optional annotations to attach to the trigger. |

**Returns:** Trigger: A trigger that runs daily at midnight.

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
| `trigger_time_input_key` | `str \| None` | The input parameter for the trigger time. If None, no trigger time input is added. |
| `name` | `str` | The name of the trigger, default is "hourly". |
| `description` | `str` | A description of the trigger. |
| `auto_activate` | `bool` | Whether the trigger should be automatically activated. |
| `inputs` | `Dict[str, Any] \| None` | Optional inputs for the trigger. |
| `env_vars` | `Dict[str, str] \| None` | Optional environment variables. |
| `interruptible` | `bool \| None` | Whether the trigger is interruptible. |
| `overwrite_cache` | `bool` | Whether to overwrite the cache. |
| `queue` | `str \| None` | Optional queue to run the trigger in. |
| `labels` | `Mapping[str, str] \| None` | Optional labels to attach to the trigger. |
| `annotations` | `Mapping[str, str] \| None` | Optional annotations to attach to the trigger. |

**Returns:** Trigger: A trigger that runs every hour, on the hour.

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
| `trigger_time_input_key` | `str \| None` | The input parameter for the trigger time. If None, no trigger time input is added. |
| `name` | `str` | The name of the trigger, default is "every_minute". |
| `description` | `str` | A description of the trigger. |
| `auto_activate` | `bool` | Whether the trigger should be automatically activated. |
| `inputs` | `Dict[str, Any] \| None` | Optional inputs for the trigger. |
| `env_vars` | `Dict[str, str] \| None` | Optional environment variables. |
| `interruptible` | `bool \| None` | Whether the trigger is interruptible. |
| `overwrite_cache` | `bool` | Whether to overwrite the cache. |
| `queue` | `str \| None` | Optional queue to run the trigger in. |
| `labels` | `Mapping[str, str] \| None` | Optional labels to attach to the trigger. |
| `annotations` | `Mapping[str, str] \| None` | Optional annotations to attach to the trigger. |

**Returns:** Trigger: A trigger that runs every minute.

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
| `trigger_time_input_key` | `str \| None` | The input parameter for the trigger time. If None, no trigger time input is added. |
| `name` | `str` | The name of the trigger, default is "monthly". |
| `description` | `str` | A description of the trigger. |
| `auto_activate` | `bool` | Whether the trigger should be automatically activated. |
| `inputs` | `Dict[str, Any] \| None` | Optional inputs for the trigger. |
| `env_vars` | `Dict[str, str] \| None` | Optional environment variables. |
| `interruptible` | `bool \| None` | Whether the trigger is interruptible. |
| `overwrite_cache` | `bool` | Whether to overwrite the cache. |
| `queue` | `str \| None` | Optional queue to run the trigger in. |
| `labels` | `Mapping[str, str] \| None` | Optional labels to attach to the trigger. |
| `annotations` | `Mapping[str, str] \| None` | Optional annotations to attach to the trigger. |

**Returns:** Trigger: A trigger that runs monthly on the 1st at midnight.

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
| `trigger_time_input_key` | `str \| None` | The input parameter for the trigger time. If None, no trigger time input is added. |
| `name` | `str` | The name of the trigger, default is "weekly". |
| `description` | `str` | A description of the trigger. |
| `auto_activate` | `bool` | Whether the trigger should be automatically activated. |
| `inputs` | `Dict[str, Any] \| None` | Optional inputs for the trigger. |
| `env_vars` | `Dict[str, str] \| None` | Optional environment variables. |
| `interruptible` | `bool \| None` | Whether the trigger is interruptible. |
| `overwrite_cache` | `bool` | Whether to overwrite the cache. |
| `queue` | `str \| None` | Optional queue to run the trigger in. |
| `labels` | `Mapping[str, str] \| None` | Optional labels to attach to the trigger. |
| `annotations` | `Mapping[str, str] \| None` | Optional annotations to attach to the trigger. |

**Returns:** Trigger: A trigger that runs weekly on Sundays at midnight.

