---
title: FixedRate
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# FixedRate

**Package:** `flytekit`

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
