---
title: CronSchedule
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# CronSchedule

**Package:** `flytekit`

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
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    pb2_object,
):
```
| Parameter | Type |
|-|-|
| `pb2_object` |  |
### serialize_to_string()

```python
def serialize_to_string()
```
No parameters
### short_string()

```python
def short_string()
```
No parameters
### to_flyte_idl()

```python
def to_flyte_idl()
```
No parameters
### verbose_string()

```python
def verbose_string()
```
No parameters
