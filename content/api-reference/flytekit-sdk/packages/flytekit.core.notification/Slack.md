---
title: Slack
version: 1.16.10
variants: +flyte +byoc +selfmanaged +serverless
layout: py_api
---

# Slack

**Package:** `flytekit.core.notification`

This notification should be used when sending emails to the Slack.

```python
from flytekit.models.core.execution import WorkflowExecutionPhase

Slack(phases=[WorkflowExecutionPhase.SUCCEEDED], recipients_email=["my-team@email.com"])
```


```python
class Slack(
    phases: typing.List[int],
    recipients_email: typing.List[str],
)
```
| Parameter | Type | Description |
|-|-|-|
| `phases` | `typing.List[int]` | |
| `recipients_email` | `typing.List[str]` | |

## Methods

| Method | Description |
|-|-|
| [`from_flyte_idl()`](#from_flyte_idl) |  |
| [`serialize_to_string()`](#serialize_to_string) |  |
| [`short_string()`](#short_string) | :rtype: Text. |
| [`to_flyte_idl()`](#to_flyte_idl) | :rtype: flyteidl. |


### from_flyte_idl()

```python
def from_flyte_idl(
    p,
)
```
| Parameter | Type | Description |
|-|-|-|
| `p` |  | |

### serialize_to_string()

```python
def serialize_to_string()
```
### short_string()

```python
def short_string()
```
:rtype: Text


### to_flyte_idl()

```python
def to_flyte_idl()
```
:rtype: flyteidl.admin.common_pb2.Notification


## Properties

| Property | Type | Description |
|-|-|-|
| `email` |  | {{< multiline >}}:rtype: EmailNotification
{{< /multiline >}} |
| `is_empty` |  |  |
| `pager_duty` |  | {{< multiline >}}:rtype: PagerDutyNotification
{{< /multiline >}} |
| `phases` |  | {{< multiline >}}A list of phases to which users can associate the notifications.
:rtype: list[int]
{{< /multiline >}} |
| `slack` |  | {{< multiline >}}:rtype: SlackNotification
{{< /multiline >}} |

