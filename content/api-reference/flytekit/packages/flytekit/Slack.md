---
title: Slack
version: 1.15.4.dev12+g71fb1647d.d20250316
variants: +flyte +byoc +byok +serverless
layout: api
---

# Slack

**Package:** `flytekit`

This notification should be used when sending emails to the Slack.

.. code-block:: python

from flytekit.models.core.execution import WorkflowExecutionPhase

Slack(phases=[WorkflowExecutionPhase.SUCCEEDED], recipients_email=["my-team@email.com"])


```python
def Slack(
    phases: typing.List[int],
    recipients_email: typing.List[str],
):
```
| Parameter | Type |
|-|-|
| `phases` | `typing.List[int]` |
| `recipients_email` | `typing.List[str]` |
## Methods

### from_flyte_idl()

```python
def from_flyte_idl(
    p,
):
```
| Parameter | Type |
|-|-|
| `p` |  |
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
