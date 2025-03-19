---
title: flytekit.core.schedule
version: 1.15.4.dev2+g3e3ce2426
variants: +flyte +byoc +byok +serverless
layout: py_api
---

# flytekit.core.schedule


.. autoclass:: flytekit.core.schedule.CronSchedule
   :noindex:


## Directory

### Classes

| Class | Description |
|-|-|
| [`CronSchedule`](.././flytekit.core.schedule#flytekitcoreschedulecronschedule) | Use this when you have a launch plan that you want to run on a cron expression. |
| [`FixedRate`](.././flytekit.core.schedule#flytekitcoreschedulefixedrate) | Use this class to schedule a fixed-rate interval for a launch plan. |
| [`LaunchPlanTriggerBase`](.././flytekit.core.schedule#flytekitcoreschedulelaunchplantriggerbase) | Base class for protocol classes. |
| [`OnSchedule`](.././flytekit.core.schedule#flytekitcorescheduleonschedule) | Base class for protocol classes. |
| [`Protocol`](.././flytekit.core.schedule#flytekitcorescheduleprotocol) | Base class for protocol classes. |

## flytekit.core.schedule.CronSchedule

Use this when you have a launch plan that you want to run on a cron expression.
This uses standard `cron format <https://docs.flyte.org/en/latest/concepts/schedules.html#cron-expression-table>`__
in case where you are using default native scheduler using the schedule attribute.

.. code-block::

CronSchedule(
schedule="*/1 * * * *",  # Following schedule runs every min
)

See the :std:ref:`User Guide <cookbook:cron schedules>` for further examples.


```python
def CronSchedule(
    cron_expression: typing.Optional[str],
    schedule: typing.Optional[str],
    offset: typing.Optional[str],
    kickoff_time_input_arg: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `cron_expression` | `typing.Optional[str]` |
| `schedule` | `typing.Optional[str]` |
| `offset` | `typing.Optional[str]` |
| `kickoff_time_input_arg` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| cron_expression |  |  |
| cron_schedule |  |  |
| is_empty |  |  |
| kickoff_time_input_arg |  |  |
| rate |  |  |
| schedule_expression |  |  |

## flytekit.core.schedule.FixedRate

Use this class to schedule a fixed-rate interval for a launch plan.

.. code-block:: python

from datetime import timedelta

FixedRate(duration=timedelta(minutes=10))

See the :std:ref:`fixed rate intervals` chapter in the cookbook for additional usage examples.


```python
def FixedRate(
    duration: datetime.timedelta,
    kickoff_time_input_arg: typing.Optional[str],
):
```
| Parameter | Type |
|-|-|
| `duration` | `datetime.timedelta` |
| `kickoff_time_input_arg` | `typing.Optional[str]` |

### Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) | None |
| [`short_string()`](#short_string) |  |
| [`to_flyte_idl()`](#to_flyte_idl) |  |
| [`verbose_string()`](#verbose_string) |  |


#### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |

#### serialize_to_string()

```python
def serialize_to_string()
```
#### short_string()

```python
def short_string()
```
#### to_flyte_idl()

```python
def to_flyte_idl()
```
#### verbose_string()

```python
def verbose_string()
```
### Properties

| Property | Type | Description |
|-|-|-|
| cron_expression |  |  |
| cron_schedule |  |  |
| is_empty |  |  |
| kickoff_time_input_arg |  |  |
| rate |  |  |
| schedule_expression |  |  |

## flytekit.core.schedule.LaunchPlanTriggerBase

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


```python
def LaunchPlanTriggerBase(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) | None |


#### to_flyte_idl()

```python
def to_flyte_idl(
    args,
    kwargs,
):
```
| Parameter | Type |
|-|-|
| `args` | ``*args`` |
| `kwargs` | ``**kwargs`` |

## flytekit.core.schedule.OnSchedule

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


```python
def OnSchedule(
    schedule: typing.Union[flytekit.core.schedule.CronSchedule, flytekit.core.schedule.FixedRate],
):
```
| Parameter | Type |
|-|-|
| `schedule` | `typing.Union[flytekit.core.schedule.CronSchedule, flytekit.core.schedule.FixedRate]` |

### Methods

| Method | Description |
|-|-|
| [`to_flyte_idl()`](#to_flyte_idl) | None |


#### to_flyte_idl()

```python
def to_flyte_idl()
```
## flytekit.core.schedule.Protocol

Base class for protocol classes.

Protocol classes are defined as::

class Proto(Protocol):
def meth(self) -> int:
...

Such classes are primarily used with static type checkers that recognize
structural subtyping (static duck-typing).

For example::

class C:
def meth(self) -> int:
return 0

def func(x: Proto) -> int:
return x.meth()

func(C())  # Passes static type check

See PEP 544 for details. Protocol classes decorated with
@typing.runtime_checkable act as simple-minded runtime protocols that check
only the presence of given attributes, ignoring their type signatures.
Protocol classes can be generic, they are defined as::

class GenProto[T](Protocol):
def meth(self) -> T:
...


